"""n5_phase3.py -- N5/M2 conditional Derrick (only if phase 2 found a window).

Hedgehog F = pi * e^{-u} radial quadrature (SC4 functional), with NET
coefficients from the measured fits:

  e2_net(J)  = J*e2_tree + alpha2_loop            (channel-B quadratic)
  cS_net(J)  = (J*e4_tree_A + alpha4_loop_A)/9
  cK_net(J)  = ((J*e4_tree_B + alpha4_loop_B) - (J*e4_tree_A + alpha4_loop_A))/6

  lambda*^2(J) = [cS_net*I_S + cK_net*I_K] / [(e2_net/3) * I_2]

Criterion (pre-registered D3): lambda* >= a_eff somewhere in the window,
else partial death ("emerges too small for Derrick").
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

import n5_core as core

HERE = Path(__file__).resolve().parent


def hedgehog_integrals():
    """I2, I_S, I_K for F = pi*e^{-u} (log-radial quadrature)."""
    u = np.geomspace(1e-6, 40.0, 40000)
    F = np.pi * np.exp(-u)
    Fp = -np.pi * np.exp(-u)
    s2 = np.sin(F) ** 2 / u ** 2
    e2 = Fp ** 2 + 2 * s2
    dens_S = e2 ** 2
    dens_K = (2 * s2) * (2 * Fp ** 2 + s2)
    w = 4 * np.pi * u ** 2
    I2 = np.trapz(w * e2, u)
    IS = np.trapz(w * dens_S, u)
    IK = np.trapz(w * dens_K, u)
    return float(I2), float(IS), float(IK)


def main():
    p1 = json.loads((HERE / "n5_phase1.json").read_text())
    p2 = json.loads((HERE / "n5_phase2.json").read_text())
    if "window" not in p2:
        print("phase 2 did not open a window; phase 3 not run (funnel).")
        return
    J_c, J_max = p2["window"]
    seeds = p1["seeds_L8"]
    I2, IS, IK = hedgehog_integrals()

    def mean(key_ch, fit, coef):
        return float(np.mean([s[f"fits_{key_ch}"][fit][coef] for s in seeds]))

    e2_tree = mean("B", "tree", "a2")
    a2_loop = mean("B", "loop", "a2")
    e4A_tree, e4B_tree = mean("A", "tree", "a4"), mean("B", "tree", "a4")
    a4A_loop, a4B_loop = mean("A", "loop", "a4"), mean("B", "loop", "a4")
    a_eff = float(np.mean([s["a_eff"] for s in seeds]))

    rows = []
    for J in np.linspace(J_c, J_max, 25):
        e2n = J * e2_tree / 3.0 + a2_loop / 3.0
        cS = (J * e4A_tree + a4A_loop) / 9.0
        cK = ((J * e4B_tree + a4B_loop) - (J * e4A_tree + a4A_loop)) / 6.0
        num = cS * IS + cK * IK
        lam2 = num / (e2n * I2) if e2n > 0 else np.nan
        lam = float(np.sqrt(lam2)) if lam2 > 0 else 0.0
        rows.append({"J": float(J), "e2_net": e2n, "cS_net": cS, "cK_net": cK,
                     "lambda_star": lam})
    lam_max = max(r["lambda_star"] for r in rows)
    ok = lam_max >= a_eff
    out = {"I2": I2, "I_S": IS, "I_K": IK, "a_eff": a_eff,
           "rows": rows, "lambda_star_max": lam_max,
           "derrick_sufficient": bool(ok),
           "verdict_phase3": ("SUCCESS lambda* >= a_eff" if ok
                              else "D3 PARTIAL DEATH (too small for Derrick)")}
    core.save_json("n5_phase3.json", out)
    print(json.dumps({k: out[k] for k in ("a_eff", "lambda_star_max",
                                          "derrick_sufficient", "verdict_phase3")},
                     indent=2))


if __name__ == "__main__":
    main()
