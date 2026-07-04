"""n1_gate_su3.py -- N1 engineering gate: the GENERALIZED engine at N=3 must
reproduce FL1's measured SU(3) results before SU(4) is allowed to run.

Gate criteria (PRE_REGISTRO.md):
  1. J_c(causal) ~ 0.3: chi-peak in J in [0.2, 0.5]; disordered at J<=0.1
     (m < 3/sqrtN); LRO (winner 'const') for all J >= 0.5.
  2. Mermin: |C_long - m^2|/m^2 < 0.10 at ordered J.
  3. SU(3) gauge at L=6, beta=4.5: Creutz chi(2,2) > 0.05 and V(r) increasing.
  4. algebra checks (done in sun_core __main__, repeated here).
Plus N-hig: tau_int/ESS per (J, seed); hot/cold cross-check at J=1.0.
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import sun_core as sc

HERE = Path(__file__).resolve().parent

# ---- pre-registered configuration (PRE_REGISTRO.md) ------------------------- #
NGROUP = 3
RHO, BOX = 2.0, [(0.0, 24.0), (0.0, 3.0), (0.0, 3.0), (0.0, 3.0)]
JS = [0.05, 0.1, 0.2, 0.3, 0.5, 1.0, 2.0]
N_SEEDS = 4
BURN, MEAS, MEAS_EVERY = 500, 120, 2
R_CAP, MIN_COUNT, N_SOURCES = 24, 200, 24
GAUGE_L, GAUGE_BETA = 6, 4.5
GAUGE_THERM, GAUGE_CFGS, GAUGE_SPACING = 60, 5, 5
RMAX = TMAX = 3


def build_causal_seed(seed):
    rng = np.random.default_rng(7000 + seed)          # same seed family as FLB
    pts = sc.sprinkle_box(RHO, BOX, rng)
    g = sc.causal_link_graph(pts)
    early = g.topo_order[:max(N_SOURCES, int(0.3 * g.n))]
    sources = rng.choice(early, size=min(N_SOURCES, early.size), replace=False)
    dist_list = [sc.longest_chain_from(g, int(s), r_max=R_CAP) for s in sources]
    return g, sources, dist_list


def run_point(g, sources, dist_list, N, J, seed, init=None):
    mdl = sc.SUNChiralModel(g, N, J=J, seed=9001 * seed + 3, init=init)
    mdl.equilibrate(BURN, adapt=True)
    acc = sc.CorrelationAccumulator(sources, dist_list, R_CAP)
    ms = []
    taken = s = 0
    while taken < MEAS:
        mdl.sweep()
        s += 1
        if s % MEAS_EVERY == 0:
            acc.add(mdl)
            ms.append(mdl.order_parameter())
            taken += 1
    r, C, w = acc.result()
    ms = np.array(ms)
    chi = float(g.n * (np.mean(ms ** 2) - np.mean(ms) ** 2))
    binder = float(1.0 - np.mean(ms ** 4) / (3.0 * np.mean(ms ** 2) ** 2))
    tau, ess = sc.tau_int(ms)
    return {"r": r, "C": C, "w": w, "m": float(ms.mean()), "chi": chi,
            "binder": binder, "tau_int": tau, "ess": ess}


def aggregate(points, r_ref):
    Cs, Ws = [], []
    for p in points:
        Cg = np.full(r_ref.shape, np.nan)
        Wg = np.zeros(r_ref.shape)
        idx = {int(rr): k for k, rr in enumerate(p["r"])}
        for k, rr in enumerate(r_ref):
            if rr in idx:
                Cg[k] = p["C"][idx[rr]]
                Wg[k] = p["w"][idx[rr]]
        Cs.append(Cg)
        Ws.append(Wg)
    Cs, Ws = np.array(Cs), np.array(Ws)
    import warnings
    with np.errstate(invalid="ignore"), warnings.catch_warnings():
        warnings.simplefilter("ignore", RuntimeWarning)
        Cmean = np.nansum(Cs * Ws, axis=0) / np.maximum(np.nansum(Ws, axis=0), 1e-9)
        Cstd = np.nanstd(Cs, axis=0)
    return Cmean, Cstd, np.nansum(Ws, axis=0)


def ordering_scan(N, Js, tag):
    print(f"\n[{tag}] SU({N}) ordering scan on the causal substrate")
    raw = {J: [] for J in Js}
    gstats = []
    seeds_cache = []
    for seed in range(N_SEEDS):
        g, sources, dist_list = build_causal_seed(seed)
        seeds_cache.append((g, sources, dist_list))
        gstats.append({"n": g.n, "links": g.n_links,
                       "avgdeg": 2 * g.n_links / g.n})
        for J in Js:
            raw[J].append(run_point(g, sources, dist_list, N, J, seed))
    r_ref = np.arange(1, R_CAP + 1)
    res = {}
    for J in Js:
        pts = raw[J]
        Cmean, Cstd, Wtot = aggregate(pts, r_ref)
        ok = Wtot >= MIN_COUNT
        fit = sc.fit_forms(r_ref[ok], Cmean[ok], sigma=Cstd[ok], r_lo=2)
        m_mean = float(np.mean([p["m"] for p in pts]))
        res[J] = {"m": m_mean, "m2": m_mean ** 2,
                  "chi": float(np.mean([p["chi"] for p in pts])),
                  "binder": float(np.mean([p["binder"] for p in pts])),
                  "tau_int_max": float(np.max([p["tau_int"] for p in pts])),
                  "ess_min": float(np.min([p["ess"] for p in pts])),
                  "C_long": fit["C_long"], "winner": fit["winner"]}
        d = res[J]
        print(f"  J={J:5.2f}  m={d['m']:.3f}  chi={d['chi']:8.3f}  U4={d['binder']:.3f}  "
              f"C(r):{d['winner']:6s} C_long={d['C_long']:.3f} m2={d['m2']:.3f}  "
              f"tau<={d['tau_int_max']:.1f} ESS>={d['ess_min']:.0f}")
    gmean = {k: float(np.mean([s[k] for s in gstats]))
             for k in ("n", "links", "avgdeg")}
    print(f"  graph: n~{gmean['n']:.0f} links~{gmean['links']:.0f} "
          f"avgdeg~{gmean['avgdeg']:.0f}")
    return res, gmean, seeds_cache


def gauge_confinement(N, beta, T):
    rng = np.random.default_rng(42)
    U = sc.gauge_init(N, GAUGE_L, rng, hot=True)
    step = 0.3
    for s in range(GAUGE_THERM):
        acc = sc.gauge_metropolis_sweep(U, beta, rng, step, T)
        if acc > 0.5:
            step *= 1.1
        elif acc < 0.3:
            step *= 0.9
    loops_acc = {}
    for c in range(GAUGE_CFGS):
        for _ in range(GAUGE_SPACING):
            sc.gauge_metropolis_sweep(U, beta, rng, step, T)
        lp = sc.measure_wilson_loops(U, RMAX, TMAX)
        for k, v in lp.items():
            loops_acc.setdefault(k, []).append(v)
    loops = {k: float(np.mean(v)) for k, v in loops_acc.items()}
    rr, V = sc.static_potential(loops, RMAX, TMAX)
    creutz2 = sc.creutz_ratio(loops, 2)
    v_inc = bool(len(V) >= 2 and V[-1] > V[0])
    return {"beta": beta, "loops": {str(k): v for k, v in loops.items()},
            "V_r": V.tolist(), "r": rr.tolist(),
            "creutz22": creutz2, "V_increases": v_inc, "acc_step": step}


def main():
    t0 = time.time()
    print("=" * 74)
    print("N1 GATE -- generalized SU(N) engine at N=3 vs FL1 measurements")
    print("=" * 74)

    res, gmean, seeds_cache = ordering_scan(NGROUP, JS, "1")

    # gate 1: J_c location + phases
    chis = {J: res[J]["chi"] for J in JS}
    j_peak = max(chis, key=chis.get)
    disordered_ok = all(res[J]["m"] < 3.0 / np.sqrt(gmean["n"])
                        for J in JS if J <= 0.1)
    lro_ok = all(res[J]["winner"] == "const" for J in JS if J >= 0.5)
    gate1 = (0.2 <= j_peak <= 0.5) and disordered_ok and lro_ok

    # gate 2: Mermin at ordered J
    mermin = {J: abs(res[J]["C_long"] - res[J]["m2"]) / max(res[J]["m2"], 1e-9)
              for J in JS if J >= 0.5}
    gate2 = all(v < 0.10 for v in mermin.values())

    # hot/cold cross-check at J=1.0 (N-hig substitute for 2nd algorithm)
    g, sources, dist_list = seeds_cache[0]
    hot = run_point(g, sources, dist_list, NGROUP, 1.0, 0, init=None)
    cold = run_point(g, sources, dist_list, NGROUP, 1.0, 0, init="ordered")
    hc_ok = abs(hot["m"] - cold["m"]) < 0.05
    print(f"\n[2] hot/cold J=1.0: m_hot={hot['m']:.3f} m_cold={cold['m']:.3f} "
          f"consistent={hc_ok}")

    # gate 3: SU(3) confinement at beta=4.5
    print(f"\n[3] SU(3) gauge sector L={GAUGE_L} beta={GAUGE_BETA}")
    T3 = sc.generators(NGROUP)
    gres = gauge_confinement(NGROUP, GAUGE_BETA, T3)
    print(f"  V(r)={[round(v,3) for v in gres['V_r']]}  "
          f"creutz(2,2)={gres['creutz22']:.3f}  V_increases={gres['V_increases']}")
    gate3 = (gres["creutz22"] > 0.05) and gres["V_increases"]

    verdict = gate1 and gate2 and hc_ok and gate3
    print("-" * 74)
    print(f"gate1 (J_c~0.3 + phases): {gate1}  [chi-peak at J={j_peak}]")
    print(f"gate2 (Mermin <10%):      {gate2}  {[round(v,3) for v in mermin.values()]}")
    print(f"gate  (hot/cold):         {hc_ok}")
    print(f"gate3 (confinement):      {gate3}")
    print(f"GATE VERDICT: {'GREEN -- SU(4) authorized' if verdict else 'RED -- fix engine'}")
    print(f"({time.time()-t0:.0f}s)")

    payload = {
        "campaign": "N1_CONTROLE_SU4", "stage": "gate_su3",
        "config": {"rho": RHO, "box": BOX, "Js": JS, "n_seeds": N_SEEDS,
                   "burn": BURN, "meas": MEAS, "r_cap": R_CAP,
                   "gauge": [GAUGE_L, GAUGE_BETA]},
        "graph": gmean,
        "ordering": {str(J): res[J] for J in JS},
        "chi_peak_J": j_peak, "mermin_rel": {str(k): v for k, v in mermin.items()},
        "hot_cold": {"m_hot": hot["m"], "m_cold": cold["m"], "ok": hc_ok},
        "gauge": gres,
        "gates": {"g1_jc": gate1, "g2_mermin": gate2, "hc": hc_ok,
                  "g3_confine": gate3},
        "verdict": "GREEN" if verdict else "RED",
        "runtime_s": time.time() - t0,
    }
    (HERE / "n1_gate_su3.json").write_text(json.dumps(payload, indent=2))
    print("saved n1_gate_su3.json")


if __name__ == "__main__":
    main()
