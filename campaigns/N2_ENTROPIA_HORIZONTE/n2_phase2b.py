"""n2_phase2b.py -- N2 Phase 2b: ONE declared repair of the phase-2 estimator
(criteria identical to phase 2; this is the only repair attempt -- if it is not
clean, phase 2 closes as INCONCLUSIVE with the diagnosis).

Diagnosis from phase 2 (n2_phase2.json):
  (i)  the global Goldstone zero mode is SHARED by both blocks (the whole sample
       rides one slowly-diffusing order-parameter direction), so the Gaussian MI
       saturates at a few shared modes instead of exposing the boundary term;
  (ii) the disordered control at J=0.05 is not disordered at L=4 (m=0.45): the
       causal graph's average degree grows with volume (known non-locality), so
       J_c(L) drifts below 0.05.

Repairs (declared here, before running):
  (i)  per-sample GLOBAL-MODE PROJECTION: from each site variable subtract the
       instantaneous all-site mean of that component (removes the k=0 mode);
  (ii) control at J = 0.005.
Everything else (grids, blocks, samples, criteria) is verbatim phase 2.
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "N1_CONTROLE_SU4"))
import n2_core as nc
import sun_core as sc
from n2_phase2 import (hasse_graph, blocks, gaussian_mi,
                       RHO, TX, LS, N_SEEDS, BURN, MEAS, EVERY)

HERE = Path(__file__).resolve().parent
J_ORD, J_DIS = 1.0, 0.005


def run_case(L, seed, J):
    rng = np.random.default_rng(61000 + seed)
    pts = nc.sprinkle(RHO, TX, L, 4, rng)
    g = hasse_graph(pts, L)
    A, Bb = blocks(pts)
    mdl = sc.SUNChiralModel(g, 2, J=J, seed=71000 + seed)
    mdl.equilibrate(BURN, adapt=True)
    comp = 1
    XA = np.empty((MEAS, A.size))
    XB = np.empty((MEAS, Bb.size))
    ms = []
    taken = s = 0
    while taken < MEAS:
        mdl.sweep()
        s += 1
        if s % EVERY == 0:
            gmean = mdl.v[:, comp].mean()          # global zero mode, this sample
            XA[taken] = mdl.v[A, comp] - gmean
            XB[taken] = mdl.v[Bb, comp] - gmean
            ms.append(mdl.order_parameter())
            taken += 1
    I = gaussian_mi(XA, XB)
    perm = np.random.default_rng(81000 + seed).permutation(MEAS)
    I0 = gaussian_mi(XA, XB[perm])
    tau, ess = sc.tau_int(np.array(ms))
    return {"I": I, "I_shuffle": I0, "dA": int(A.size), "dB": int(Bb.size),
            "m": float(np.mean(ms)), "tau_int": tau, "ess": ess}


def main():
    t0 = time.time()
    print("=" * 74)
    print("N2 Phase 2b -- zero-mode-projected MI (single declared repair)")
    print("=" * 74)
    out = {}
    for J, tag in ((J_ORD, "ordered"), (J_DIS, "disordered")):
        out[tag] = {}
        print(f"\n[{tag}] J={J}")
        for L in LS:
            rows = [run_case(L, s, J) for s in range(N_SEEDS)]
            Im = float(np.mean([r["I"] for r in rows]))
            Ie = float(np.std([r["I"] for r in rows], ddof=1) / np.sqrt(N_SEEDS))
            I0m = float(np.mean([r["I_shuffle"] for r in rows]))
            out[tag][L] = {"I": [Im, Ie], "I_shuffle": I0m, "I_net": Im - I0m,
                           "dA": float(np.mean([r["dA"] for r in rows])),
                           "m": float(np.mean([r["m"] for r in rows])),
                           "tau_max": float(np.max([r["tau_int"] for r in rows])),
                           "ess_min": float(np.min([r["ess"] for r in rows]))}
            d = out[tag][L]
            print(f"  L={L:3.1f}: I={Im:7.3f}+-{Ie:.3f}  shuf={I0m:6.3f}  "
                  f"net={d['I_net']:7.3f}  I_net/L2={d['I_net']/L**2:6.4f}  "
                  f"m={d['m']:.3f}  tau<={d['tau_max']:.1f} ESS>={d['ess_min']:.0f}")

    ord_ = out["ordered"]
    net = {L: ord_[L]["I_net"] for L in LS}
    perA = [net[L] / L ** 2 for L in LS]
    flat = (max(perA) - min(perA)) / max(np.mean(perA), 1e-12)
    area_ok = flat < 0.8 and all(v > 0 for v in perA)
    s_net, s_e = nc.loglog_slope(LS, [max(net[L], 1e-9) for L in LS])
    ctrl = all(out["disordered"][L]["I_net"]
               < 0.2 * max(out["ordered"][L]["I_net"], 1e-12) for L in LS)
    print("-" * 74)
    print(f"  I_net/L^2 spread (< 0.8): {flat:.2f}  -> {area_ok}")
    print(f"  I_net ~ L^{s_net:.2f}+-{s_e:.2f} (area=2)")
    print(f"  control < 20%: {ctrl}")
    verdict = ("AREA_LAW_MATTER" if (area_ok and ctrl)
               else ("INCONCLUSIVE" if not ctrl else "FAIL"))
    print(f"PHASE 2b VERDICT: {verdict}")
    print(f"({time.time()-t0:.0f}s)")

    payload = {"campaign": "N2_ENTROPIA_HORIZONTE", "stage": "phase2b_repair",
               "repairs": ["global zero-mode projection", "control J=0.005"],
               "results": {tag: {str(L): out[tag][L] for L in LS} for tag in out},
               "slope_net": [s_net, s_e], "perA_spread": flat,
               "control_ok": bool(ctrl), "verdict": verdict,
               "runtime_s": time.time() - t0}
    (HERE / "n2_phase2b.json").write_text(json.dumps(payload, indent=2))
    print("saved n2_phase2b.json")


if __name__ == "__main__":
    main()
