"""f2_gate.py -- F2 engineering gate (PRE_REGISTRO.md par.3, G1..G8).

The STACK engine must (i) have a certified g2 algebra and (ii) reproduce the
FL1/N1 SU(3) measurements with the Gell-Mann stack, BEFORE G2 runs.
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent / "N1_CONTROLE_SU4"))

import g2_core as gc
import sun_core as sc
from n1_gate_su3 import (build_causal_seed, aggregate, RHO, BOX, JS, N_SEEDS,
                         BURN, MEAS, MEAS_EVERY, R_CAP, MIN_COUNT,
                         GAUGE_L, GAUGE_BETA, GAUGE_THERM, GAUGE_CFGS,
                         GAUGE_SPACING, RMAX, TMAX)

FL1_LADDER = {15: 0.794678, 21: 0.892081}     # measured FL1/N1 constants


def run_point_stack(g, sources, dist_list, T, sampler, J, seed, init=None):
    mdl = gc.StackChiralModel(g, T, sampler, J=J, seed=9001 * seed + 3,
                              init=init)
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


def ordering_scan_stack(T, sampler, Js, tag):
    print(f"\n[{tag}] stack-engine ordering scan (dimA={T.shape[0]})")
    raw = {J: [] for J in Js}
    gstats, seeds_cache = [], []
    for seed in range(N_SEEDS):
        g, sources, dist_list = build_causal_seed(seed)
        seeds_cache.append((g, sources, dist_list))
        gstats.append({"n": g.n, "links": g.n_links,
                       "avgdeg": 2 * g.n_links / g.n})
        for J in Js:
            raw[J].append(run_point_stack(g, sources, dist_list, T, sampler,
                                          J, seed))
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
        print(f"  J={J:5.2f}  m={d['m']:.3f}  chi={d['chi']:8.3f}  "
              f"U4={d['binder']:.3f}  C(r):{d['winner']:6s} "
              f"C_long={d['C_long']:.3f} m2={d['m2']:.3f}  "
              f"tau<={d['tau_int_max']:.1f} ESS>={d['ess_min']:.0f}")
    gmean = {k: float(np.mean([s[k] for s in gstats]))
             for k in ("n", "links", "avgdeg")}
    return res, gmean, seeds_cache


def gauge_confinement_stack(T, sampler, N, beta):
    rng = np.random.default_rng(42)
    U = gc.gauge_init_stack(sampler, N, GAUGE_L, rng, hot=True)
    step = 0.3
    for _ in range(GAUGE_THERM):
        acc = gc.gauge_metropolis_sweep_stack(U, beta, rng, step, T)
        if acc > 0.5:
            step *= 1.1
        elif acc < 0.3:
            step *= 0.9
    loops_acc = {}
    for _ in range(GAUGE_CFGS):
        for _ in range(GAUGE_SPACING):
            gc.gauge_metropolis_sweep_stack(U, beta, rng, step, T)
        lp = sc.measure_wilson_loops(U, RMAX, TMAX)
        for k, v in lp.items():
            loops_acc.setdefault(k, []).append(v)
    loops = {k: float(np.mean(v)) for k, v in loops_acc.items()}
    rr, V = sc.static_potential(loops, RMAX, TMAX)
    return {"beta": beta, "loops": {str(k): v for k, v in loops.items()},
            "V_r": V.tolist(), "r": rr.tolist(),
            "creutz22": sc.creutz_ratio(loops, 2),
            "V_increases": bool(len(V) >= 2 and V[-1] > V[0]),
            "acc_step": step}


def main():
    t0 = time.time()
    print("=" * 74)
    print("F2 GATE -- g2 algebra + stack engine vs FL1 (PRE_REGISTRO par.3)")
    print("=" * 74)
    T, phi = gc.g2_generators()
    gates = {}

    # G1 dim
    gates["G1_dim14"] = bool(T.shape[0] == 14)

    # G2 closure
    res = 0.0
    for a in range(14):
        for b in range(a + 1, 14):
            C = 1j * (T[a] @ T[b] - T[b] @ T[a])
            coef = np.einsum("ij,cji->c", C, T).real / 2.0
            res = max(res, float(np.max(np.abs(
                C - np.einsum("c,cij->ij", coef, T)))))
    gates["G2_closure"] = bool(res < 1e-10)

    # G3 Casimir = 4 I
    Cas = np.einsum("aij,ajk->ik", T, T)
    cas_err = float(np.max(np.abs(Cas - 4.0 * np.eye(7))))
    gates["G3_casimir"] = bool(cas_err < 1e-10)

    # G4 3-form invariance under exp(g2)
    rng = np.random.default_rng(1)
    inv_err = 0.0
    for _ in range(20):
        U = gc.haar_walk(T, 1, rng)[0].real
        phi_t = np.einsum("abc,ai,bj,ck->ijk", phi, U, U, U)
        inv_err = max(inv_err, float(np.max(np.abs(phi_t - phi))))
    gates["G4_3form"] = bool(inv_err < 1e-10)

    # G5 Haar walk character test
    rng = np.random.default_rng(2)
    Uh = gc.haar_walk(T, 4000, rng)
    chi7 = np.real(np.trace(Uh, axis1=-2, axis2=-1))
    m1, m2 = float(chi7.mean()), float((chi7 ** 2).mean())
    gates["G5_haar"] = bool(abs(m1) < 0.03 and abs(m2 - 1.0) < 0.06)
    print(f"G1 dim14={gates['G1_dim14']}  G2 closure res={res:.1e}  "
          f"G3 casimir err={cas_err:.1e}")
    print(f"G4 3-form err={inv_err:.1e}  G5 haar <chi>={m1:+.4f} "
          f"<chi^2>={m2:.4f}")

    # G6 so(4) split + diagonal so(3)
    J, JX, JY = gc.diag_so3(T)
    X, Y = gc.so4_split(T)
    spec = np.sort(np.linalg.eigvalsh(0.6 * J[0] - 0.64 * J[1] + 0.48 * J[2]))
    spec_target = np.array([-1, -1, 0, 0, 0, 1, 1], float)
    spec_err = float(np.max(np.abs(spec - spec_target)))
    resJ = max(gc.su2_residual(J), gc.su2_residual(JX), gc.su2_residual(JY))
    gates["G6_so4"] = bool(X.shape[0] == 3 and Y.shape[0] == 3
                           and resJ < 1e-10 and spec_err < 1e-8)
    print(f"G6 dims(X,Y)=({X.shape[0]},{Y.shape[0]}) su2 res={resJ:.1e} "
          f"spectrum err={spec_err:.1e}")

    # G7 stack engine at SU(3) reproduces FL1/N1
    T3 = sc.generators(3)
    s3sampler = lambda n, r: sc.sun_random(3, n, r)
    res3, gmean, _ = ordering_scan_stack(T3, s3sampler, JS, "G7")
    chis = {Jv: res3[Jv]["chi"] for Jv in JS}
    j_peak = max(chis, key=chis.get)
    disordered_ok = all(res3[Jv]["m"] < 3.0 / np.sqrt(gmean["n"])
                        for Jv in JS if Jv <= 0.1)
    lro_ok = all(res3[Jv]["winner"] == "const" for Jv in JS if Jv >= 0.5)
    mermin = {Jv: abs(res3[Jv]["C_long"] - res3[Jv]["m2"])
              / max(res3[Jv]["m2"], 1e-9) for Jv in JS if Jv >= 0.5}
    mermin_ok = all(v < 0.10 for v in mermin.values())
    print(f"\nG7 su3-stack: chi-peak J={j_peak} disord={disordered_ok} "
          f"LRO={lro_ok} mermin={[round(v,3) for v in mermin.values()]}")
    g3 = gauge_confinement_stack(T3, s3sampler, 3, GAUGE_BETA)
    print(f"G7 su3 gauge beta={GAUGE_BETA}: creutz22={g3['creutz22']:.3f} "
          f"V_inc={g3['V_increases']} V={[round(v,3) for v in g3['V_r']]}")
    ladder_ok = True
    lad = {}
    for L, ref in FL1_LADDER.items():
        B3 = sc.baryon_number(*sc.embedded_hedgehog(3, L))
        lad[L] = B3
        ladder_ok = ladder_ok and abs(B3 - ref) < 1e-3
    print(f"G7 B-ladder su3: {lad} vs {FL1_LADDER}")
    gates["G7_su3_reproduces"] = bool(
        (0.2 <= j_peak <= 0.5) and disordered_ok and lro_ok and mermin_ok
        and g3["creutz22"] > 0.05 and g3["V_increases"] and ladder_ok)

    # G8 G2 disordered at J=0.05 (quick, 1 seed)
    g, sources, dist_list = build_causal_seed(0)
    g2sampler = lambda n, r: gc.haar_walk(T, n, r)
    p = run_point_stack(g, sources, dist_list, T, g2sampler, 0.05, 0)
    floor = 3.0 / np.sqrt(g.n)
    gates["G8_g2_disordered"] = bool(p["m"] < floor)
    print(f"\nG8 G2 J=0.05: m={p['m']:.4f} floor={floor:.4f}")

    verdict = all(gates.values())
    print("-" * 74)
    for k, v in gates.items():
        print(f"  {k:22s}: {v}")
    print(f"GATE VERDICT: {'GREEN -- G2 suite authorized' if verdict else 'RED'}")
    print(f"({time.time()-t0:.0f}s)")

    payload = {
        "campaign": "F2_CONTROLE_G2", "stage": "gate",
        "algebra": {"closure_res": res, "casimir_err": cas_err,
                    "3form_err": inv_err,
                    "haar": {"chi_mean": m1, "chi2_mean": m2},
                    "su2_residual": resJ, "spec_err": spec_err},
        "su3_stack": {"ordering": {str(k): v for k, v in res3.items()},
                      "chi_peak_J": j_peak,
                      "mermin_rel": {str(k): v for k, v in mermin.items()},
                      "gauge": g3, "B_ladder": lad},
        "g2_disordered": {"m": p["m"], "floor": floor},
        "gates": gates,
        "verdict": "GREEN" if verdict else "RED",
        "runtime_s": time.time() - t0,
    }
    (HERE / "f2_gate.json").write_text(json.dumps(payload, indent=2))
    print("saved f2_gate.json")


if __name__ == "__main__":
    main()
