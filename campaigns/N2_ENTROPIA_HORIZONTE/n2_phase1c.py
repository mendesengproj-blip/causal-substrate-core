"""n2_phase1c.py -- N2 Phase 1c: convergence run for the BD molecule (declared
BEFORE running, in this header):

Phase 1b showed the BD-molecule per-area density in d=4 still RISING with L
(0.30 -> 0.53, finite-size transient from the periodic transverse box), which
inflates the 4-point slope to 2.44; and d=2 counts were underpowered (16 seeds
x ~0.4 counts).  This run extends the ranges WITHOUT touching the estimator:

  d=4: L in {3, 4, 5, 6} at rho=8; CRITERION: slope over the three largest
       L in 2 +- 0.3, and per-area of the two largest L consistent (< 2 sigma).
  d=2: 128 seeds per rho; CRITERION: slope consistent with 0 within 2 sigma
       AND |slope| <= 0.15 if powered; report power honestly.

Memory: chunked causal matrix (no n^2 float temporaries at n ~ 7200).
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import n2_core as nc
from n2_phase1b import bd_molecules

HERE = Path(__file__).resolve().parent


def causal_matrix_chunked(pts, L_perp, chunk=1500):
    n = len(pts)
    rel = np.zeros((n, n), dtype=bool)
    t = pts[:, 0].astype(np.float32)
    X = pts[:, 1:].astype(np.float32)
    for a in range(0, n, chunk):
        b = min(a + chunk, n)
        dt = t[None, :] - t[a:b, None]
        dx2 = (X[None, :, 0] - X[a:b, None, 0]) ** 2
        for k in range(1, X.shape[1]):
            dp = np.abs(X[None, :, k] - X[a:b, None, k])
            dp = np.minimum(dp, np.float32(L_perp) - dp)
            dx2 += dp ** 2
        rel[a:b] = (dt > 0) & (dt * dt > dx2)
    return rel


def run_point(rho, tx_half, L_perp, d, seed):
    rng = np.random.default_rng(31000 + seed)
    pts = nc.sprinkle(rho, tx_half, L_perp, d, rng)
    rel = causal_matrix_chunked(pts, L_perp)
    return bd_molecules(pts, rel)


def stats(vals):
    v = np.asarray(vals, float)
    sem = float(v.std(ddof=1) / np.sqrt(len(v))) if len(v) > 1 else 0.0
    return float(v.mean()), sem


def main():
    t0 = time.time()
    print("=" * 74)
    print("N2 Phase 1c -- BD molecule convergence (larger L, more seeds)")
    print("=" * 74)

    print("\n[1] d=4, rho=8, L in {3,4,5,6}, 16 seeds")
    r4 = {}
    for L in (3.0, 4.0, 5.0, 6.0):
        r4[L] = stats([run_point(8.0, 2.5, L, 4, s) for s in range(16)])
        print(f"  L={L:3.1f}: N_BD={r4[L][0]:8.2f}+-{r4[L][1]:.2f}   "
              f"per area = {r4[L][0]/L**2:.4f}")
    Ls_big = [4.0, 5.0, 6.0]
    s4, s4e = nc.loglog_slope(Ls_big, [r4[L][0] for L in Ls_big],
                              [r4[L][1] for L in Ls_big])
    pa5, pe5 = r4[5.0][0] / 25.0, r4[5.0][1] / 25.0
    pa6, pe6 = r4[6.0][0] / 36.0, r4[6.0][1] / 36.0
    conv_sig = abs(pa6 - pa5) / np.sqrt(pe5 ** 2 + pe6 ** 2 + 1e-12)
    print(f"  -> slope (L>=4): {s4:.3f}+-{s4e:.3f} (area=2); "
          f"per-area L=5 vs 6: {conv_sig:.2f} sigma")

    print("\n[2] d=2, 128 seeds per rho")
    r2 = {}
    for rho in (10.0, 20.0, 40.0, 80.0):
        r2[rho] = stats([run_point(rho, 4.0, 1.0, 2, 200 + s)
                         for s in range(128)])
        print(f"  rho={rho:5.1f}: N_BD={r2[rho][0]:.3f}+-{r2[rho][1]:.3f}")
    s2, s2e = nc.loglog_slope(list(r2), [v[0] for v in r2.values()],
                              [v[1] for v in r2.values()])
    print(f"  -> N_BD ~ rho^{s2:.3f}+-{s2e:.3f} (predicted 0)")

    a4 = float(np.mean([r4[L][0] / (L ** 2 * 8.0 ** 0.5) for L in Ls_big]))
    a2 = float(np.mean([r2[r][0] for r in r2]))

    area4 = abs(s4 - 2.0) <= 0.3
    conv4 = conv_sig < 2.0
    const2 = (abs(s2) <= 0.15) or (abs(s2) <= 2.0 * s2e)
    powered2 = s2e <= 0.15
    verdict_ok = area4 and conv4 and const2
    print("-" * 74)
    print(f"  d=4 slope L>=4 (2+-0.3):     {area4}  [{s4:.3f}+-{s4e:.3f}]")
    print(f"  d=4 per-area converged:      {conv4}  [{conv_sig:.2f} sigma]")
    print(f"  d=2 consistent w/ constant:  {const2}  [{s2:.3f}+-{s2e:.3f}, "
          f"powered={powered2}]")
    print(f"  coefficients: a_4={a4:.4f}   a_2={a2:.4f}")
    print(f"PHASE 1c VERDICT: {'AREA LAW CONFIRMED (BD molecule)' if verdict_ok else 'STILL FAILING'}")
    print(f"({time.time()-t0:.0f}s)")

    payload = {"campaign": "N2_ENTROPIA_HORIZONTE", "stage": "phase1c_convergence",
               "d4": {str(L): r4[L] for L in r4}, "d4_slope_Lge4": [s4, s4e],
               "d4_perarea_conv_sigma": conv_sig,
               "d2": {str(k): r2[k] for k in r2}, "d2_slope": [s2, s2e],
               "coefficients": {"a4": a4, "a2": a2},
               "checks": {"area4": bool(area4), "conv4": bool(conv4),
                          "const2": bool(const2), "powered2": bool(powered2)},
               "verdict": "AREA_LAW" if verdict_ok else "FAIL",
               "runtime_s": time.time() - t0}
    (HERE / "n2_phase1c.json").write_text(json.dumps(payload, indent=2))
    print("saved n2_phase1c.json")


if __name__ == "__main__":
    main()
