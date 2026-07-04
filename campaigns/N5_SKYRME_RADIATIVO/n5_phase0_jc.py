"""n5_phase0_jc.py -- gate G5: J_c of the SU(2) chiral model on the TORUS
Poisson Hasse substrate (same instrument as phase 1; refined grid after the
first box run localised J_c in (0.05, 0.1) -- see n5_phase0_jc_box.json).

Engine: sun_core (N1, validated against FL1 at N=3) at N=2; for N=2
(1/N)ReTr(U_i U_j^dag) = dot4(q_i,q_j), so J_c is directly comparable to
the J of n5_core.  tau_int/ESS reported per (J, seed) (N-hig).
"""

from __future__ import annotations

import numpy as np

import n5_core as core
import sun_core as sc
import su3_core as s3

RHO, TMAX, L = 2.0, 4.0, 8.0
J_GRID = [0.02, 0.03, 0.035, 0.04, 0.045, 0.05, 0.06]   # 2nd refinement: torus
# ordered already at J=0.05 (m=0.35, z~82 no-boundary coordination); the box
# run (n5_phase0_jc_box.json) had J_c in (0.05,0.1) -- torus J_c sits lower.
N_SEEDS = 4
BURN, N_MEAS, STRIDE = 500, 200, 2


def torus_graph():
    rng = np.random.default_rng(777)
    pts = core.sprinkle(rng, RHO, TMAX, L)
    links = core.causal_links_torus(pts, L)
    g = s3.Graph(len(pts), links)
    g.n_links = int(len(links))
    return g


def run_point(graph, J, seed):
    model = sc.SUNChiralModel(graph, 2, J, seed=seed)
    model.equilibrate(BURN, adapt=True)
    ms = []
    for _ in range(N_MEAS):
        for _ in range(STRIDE):
            model.sweep()
        ms.append(model.order_parameter())
    ms = np.asarray(ms)
    tau, ess = sc.tau_int(ms)
    m2, m4 = float(np.mean(ms ** 2)), float(np.mean(ms ** 4))
    return {"J": float(J), "seed": int(seed),
            "m": float(ms.mean()), "m_std": float(ms.std(ddof=1)),
            "chi": float(graph.n * ms.var(ddof=1)),
            "U4": float(1.0 - m4 / (3.0 * m2 * m2)) if m2 > 0 else 0.0,
            "tau_int": float(tau), "ess": float(ess)}


def main():
    graph = torus_graph()
    print(f"substrate (torus): n={graph.n}, links={graph.n_links}", flush=True)
    rows = []
    for J in J_GRID:
        for k in range(N_SEEDS):
            r = run_point(graph, J, seed=5000 + k)
            rows.append(r)
            print(f"J={J} seed{k}: m={r['m']:.4f} chi={r['chi']:.2f} "
                  f"U4={r['U4']:.3f} tau={r['tau_int']:.1f} ess={r['ess']:.0f}",
                  flush=True)
    Js = sorted(set(r["J"] for r in rows))
    chi_mean = {J: float(np.mean([r["chi"] for r in rows if r["J"] == J])) for J in Js}
    m_mean = {J: float(np.mean([r["m"] for r in rows if r["J"] == J])) for J in Js}
    j_peak = max(chi_mean, key=chi_mean.get)
    thresh = 3.0 / np.sqrt(graph.n)
    interior = min(Js) < j_peak < max(Js)
    ok = interior and (m_mean[min(Js)] < thresh)
    out = {"n": graph.n, "n_links": graph.n_links, "rows": rows,
           "chi_mean": chi_mean, "m_mean": m_mean,
           "J_c_est": float(j_peak), "m_disordered": m_mean[min(Js)],
           "disorder_threshold": float(thresh), "pass": bool(ok)}
    core.save_json("n5_phase0_jc.json", out)
    print(f"G5: J_c approx {j_peak} (chi peak, interior={interior}), "
          f"m({min(Js)})={m_mean[min(Js)]:.4f} < {thresh:.4f}: "
          f"{'PASS' if ok else 'FAIL'}")


if __name__ == "__main__":
    main()
