"""n2_phase1b.py -- N2 Phase 1b: POST-HOC DIAGNOSTIC (declared as such).

The pre-registered DS-type count N_mol FAILED the d=4 area law (slope 2.93,
T-drift 6 sigma) -- and the literature says this failure is the KNOWN pathology
of the original Dou-Sorkin definition in d >= 3 (links far from the corner;
count unbounded in infinite environments).  Barton-Counsell-Dowker-Padia-
Wingham-Zalel (PRD 100, 126008 (2019), arXiv:1909.08620) define the corrected
horizon molecule:

    pair {p-, p+} with p- < p+ (causal), BOTH in J^-(Sigma) (t<0 here),
    p- outside the horizon (u<0), p+ inside (u>0), and
    p+ is the ONLY element of J^+(p-) inside J^-(Sigma).

Theorem (ibid.): expected count = area of the corner in discreteness units, up
to a dimension-dependent O(1) factor.  This script measures that molecule on
the SAME pre-registered grids (same seeds).  It is labelled post-hoc: the
pre-registered estimator's failure stands as reported in n2_phase1.py; this is
the literature-exact estimator, not a re-tuned window.
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import n2_core as nc

HERE = Path(__file__).resolve().parent

D4 = {"rho": 8.0, "tx": 2.5, "Ls": [1.5, 2.0, 3.0, 4.0], "seeds": 12}
D4_TCHECK = {"L": 3.0, "txs": [2.0, 2.5, 3.5]}
D3 = {"rho": 10.0, "tx": 3.0, "Ls": [2.0, 3.0, 4.0, 6.0, 8.0], "seeds": 12}
D3_TCHECK = {"L": 4.0, "txs": [2.0, 3.0, 4.0]}
D2 = {"rhos": [10.0, 20.0, 40.0, 80.0], "tx": 4.0, "seeds": 16}


def bd_molecules(pts, rel):
    """Barton et al. horizon molecules: i<j, t_i<0, t_j<0, u_i<0, u_j>0,
    and j is the UNIQUE element of J^+(i) with t<0."""
    t = pts[:, 0]
    u = pts[:, 0] - pts[:, 1]
    below = t < 0
    fut_below = rel & below[None, :]              # future elements below Sigma
    nfut = fut_below.sum(axis=1)
    cand = np.nonzero((u < 0) & below & (nfut == 1))[0]
    if cand.size == 0:
        return 0
    j_idx = np.argmax(fut_below[cand], axis=1)    # the unique successor
    return int(np.sum(u[j_idx] > 0))


def run_point(rho, tx_half, L_perp, d, seed):
    rng = np.random.default_rng(31000 + seed)     # SAME seed family as phase 1
    pts = nc.sprinkle(rho, tx_half, L_perp, d, rng)
    rel = nc.causal_matrix(pts, L_perp)
    return bd_molecules(pts, rel)


def stats(vals):
    v = np.asarray(vals, float)
    sem = float(v.std(ddof=1) / np.sqrt(len(v))) if len(v) > 1 else 0.0
    return float(v.mean()), sem


def main():
    t0 = time.time()
    print("=" * 74)
    print("N2 Phase 1b -- Barton et al. horizon molecules (post-hoc, literature)")
    print("=" * 74)

    # d=4
    print(f"\n[1] d=4, rho={D4['rho']}")
    r4 = {}
    for L in D4["Ls"]:
        r4[L] = stats([run_point(D4["rho"], D4["tx"], L, 4, s)
                       for s in range(D4["seeds"])])
        print(f"  L={L:4.1f}: N_BD={r4[L][0]:8.2f}+-{r4[L][1]:.2f}   "
              f"per area = {r4[L][0]/L**2:.3f}")
    s4, s4e = nc.loglog_slope(list(r4), [v[0] for v in r4.values()],
                              [v[1] for v in r4.values()])
    print(f"  -> N_BD ~ L^{s4:.3f}+-{s4e:.3f}  (area = 2)")

    print(f"\n[2] d=4 T-check at L={D4_TCHECK['L']}")
    tv = {}
    for tx in D4_TCHECK["txs"]:
        tv[tx] = stats([run_point(D4["rho"], tx, D4_TCHECK["L"], 4, 500 + s)
                        for s in range(D4["seeds"])])
        print(f"  tx=+-{tx}: N_BD={tv[tx][0]:.2f}+-{tv[tx][1]:.2f}")
    m_lo, e_lo = tv[min(tv)]
    m_hi, e_hi = tv[max(tv)]
    t4_sig = abs(m_hi - m_lo) / np.sqrt(e_lo ** 2 + e_hi ** 2 + 1e-12)
    print(f"  -> T-drift {t4_sig:.2f} sigma (< 3 required)")

    print("\n[3] d=4 rho-scaling at L=3")
    rr = {}
    for rho in (4.0, 8.0, 16.0):
        rr[rho] = stats([run_point(rho, 2.5, 3.0, 4, 900 + s)
                         for s in range(12)])
        print(f"  rho={rho:5.1f}: N_BD={rr[rho][0]:.2f}+-{rr[rho][1]:.2f}")
    srho, srho_e = nc.loglog_slope(list(rr), [v[0] for v in rr.values()],
                                   [v[1] for v in rr.values()])
    print(f"  -> N_BD ~ rho^{srho:.3f}+-{srho_e:.3f} (predicted 0.5)")

    # d=3
    print(f"\n[4] d=3, rho={D3['rho']}")
    r3 = {}
    for L in D3["Ls"]:
        r3[L] = stats([run_point(D3["rho"], D3["tx"], L, 3, s)
                       for s in range(D3["seeds"])])
        print(f"  L={L:4.1f}: N_BD={r3[L][0]:8.2f}+-{r3[L][1]:.2f}   "
              f"per area = {r3[L][0]/L:.3f}")
    s3, s3e = nc.loglog_slope(list(r3), [v[0] for v in r3.values()],
                              [v[1] for v in r3.values()])
    print(f"  -> N_BD ~ L^{s3:.3f}+-{s3e:.3f}  (area = 1)")

    print(f"\n[5] d=3 T-check at L={D3_TCHECK['L']}")
    tv3 = {}
    for tx in D3_TCHECK["txs"]:
        tv3[tx] = stats([run_point(D3["rho"], tx, D3_TCHECK["L"], 3, 600 + s)
                         for s in range(D3["seeds"])])
        print(f"  tx=+-{tx}: N_BD={tv3[tx][0]:.2f}+-{tv3[tx][1]:.2f}")
    m_lo, e_lo = tv3[min(tv3)]
    m_hi, e_hi = tv3[max(tv3)]
    t3_sig = abs(m_hi - m_lo) / np.sqrt(e_lo ** 2 + e_hi ** 2 + 1e-12)
    print(f"  -> T-drift {t3_sig:.2f} sigma")

    # d=2
    print(f"\n[6] d=2 (pure number vs rho)")
    r2 = {}
    for rho in D2["rhos"]:
        r2[rho] = stats([run_point(rho, D2["tx"], 1.0, 2, 200 + s)
                         for s in range(D2["seeds"])])
        print(f"  rho={rho:5.1f}: N_BD={r2[rho][0]:.3f}+-{r2[rho][1]:.3f}")
    s2, s2e = nc.loglog_slope(list(r2), [v[0] for v in r2.values()],
                              [v[1] for v in r2.values()])
    print(f"  -> N_BD ~ rho^{s2:.3f}+-{s2e:.3f} (predicted 0)")

    # coefficients
    a4 = float(np.mean([r4[L][0] / (L ** 2 * D4["rho"] ** 0.5) for L in r4]))
    a3 = float(np.mean([r3[L][0] / (L * D3["rho"] ** (1 / 3)) for L in r3]))
    a2 = float(np.mean([r2[r][0] for r in r2]))
    print(f"\n[7] coefficients: a_4={a4:.4f}  a_3={a3:.4f}  a_2={a2:.4f}")

    area4 = abs(s4 - 2.0) <= 0.3
    area3 = abs(s3 - 1.0) <= 0.3
    const2 = abs(s2) <= 0.15
    t_ok = (t4_sig < 3.0) and (t3_sig < 3.0)
    rho_ok = abs(srho - 0.5) <= 0.15
    verdict_ok = area4 and area3 and const2 and t_ok
    print("-" * 74)
    print(f"  d=4 area (2+-0.3):        {area4}  [{s4:.3f}+-{s4e:.3f}]")
    print(f"  d=3 area (1+-0.3):        {area3}  [{s3:.3f}+-{s3e:.3f}]")
    print(f"  d=2 pure number:          {const2}  [{s2:.3f}+-{s2e:.3f}]")
    print(f"  T-independence d=4/d=3:   {t_ok}  [{t4_sig:.2f}/{t3_sig:.2f} sigma]")
    print(f"  rho^0.5 (secondary):      {rho_ok}  [{srho:.3f}+-{srho_e:.3f}]")
    print(f"PHASE 1b VERDICT: {'AREA LAW (literature molecule)' if verdict_ok else 'FAIL EVEN WITH LITERATURE MOLECULE'}")
    print(f"({time.time()-t0:.0f}s)")

    payload = {
        "campaign": "N2_ENTROPIA_HORIZONTE", "stage": "phase1b_posthoc_BD",
        "anchor": "Barton et al., PRD 100, 126008 (2019), arXiv:1909.08620",
        "d4": {str(L): r4[L] for L in r4}, "d4_slope": [s4, s4e],
        "d4_tcheck": {str(k): v for k, v in tv.items()}, "t4_sigma": t4_sig,
        "d4_rho": {str(k): v for k, v in rr.items()}, "rho_slope": [srho, srho_e],
        "d3": {str(L): r3[L] for L in r3}, "d3_slope": [s3, s3e],
        "d3_tcheck": {str(k): v for k, v in tv3.items()}, "t3_sigma": t3_sig,
        "d2": {str(k): r2[k] for k in r2}, "d2_slope": [s2, s2e],
        "coefficients": {"a4": a4, "a3": a3, "a2": a2},
        "checks": {"area4": bool(area4), "area3": bool(area3),
                   "const2": bool(const2), "t_ok": bool(t_ok),
                   "rho_ok": bool(rho_ok)},
        "verdict": "AREA_LAW" if verdict_ok else "FAIL",
        "runtime_s": time.time() - t0,
    }
    (HERE / "n2_phase1b.json").write_text(json.dumps(payload, indent=2))
    print("saved n2_phase1b.json")


if __name__ == "__main__":
    main()
