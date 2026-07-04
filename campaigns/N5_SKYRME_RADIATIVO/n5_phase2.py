"""n5_phase2.py -- N5/M2 window analysis (death criteria D1/D2, pre-registered).

Reads n5_phase1.json (+ n5_phase0_jc.json) and evaluates, per free node on
the SAME graphs (volume normalisation cancels):

    Q(J) = J * e4_tree_B + alpha4_loop_B          (hedgehog net quartic)
    J_max = alpha4_loop_B / |e4_tree_B|           (if alpha4_loop_B > 0)

D1: c_K_loop <= 0 within 2 sigma, OR alpha4_loop_B <= 0  -> total death.
D2: window empty: J_max <= J_c                          -> ordered-phase death.
Else window exists -> phase 3 (Derrick).  Marginality flag if the window
lies entirely below 1.5*J_c (declared perturbative caveat).
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

import n5_core as core

HERE = Path(__file__).resolve().parent


def main():
    p1 = json.loads((HERE / "n5_phase1.json").read_text())
    jc = json.loads((HERE / "n5_phase0_jc.json").read_text())
    J_c = float(jc["J_c_est"])

    agg = p1["agg_L8"]
    seeds = p1["seeds_L8"]

    a4B = np.array([s["fits_B"]["loop"]["a4"] for s in seeds])
    a4A = np.array([s["fits_A"]["loop"]["a4"] for s in seeds])
    e4B = np.array([s["fits_B"]["tree"]["a4"] for s in seeds])
    cK = (a4B - a4A) / 6.0

    def stats(v):
        return {"mean": float(v.mean()),
                "sem": float(v.std(ddof=1) / np.sqrt(len(v)))}

    cK_s, a4B_s, e4B_s = stats(cK), stats(a4B), stats(e4B)

    d1_cK = cK_s["mean"] <= 2.0 * cK_s["sem"]           # not positive at 2 sigma
    d1_hh = a4B_s["mean"] <= 0.0
    D1 = bool(d1_cK or d1_hh)

    out = {"J_c": J_c, "c_K_loop": cK_s, "alpha4_loop_B": a4B_s,
           "e4_tree_B": e4B_s, "D1": D1,
           "D1_reason": {"cK_not_positive_2sigma": bool(d1_cK),
                         "loop_hedgehog_nonpositive": bool(d1_hh)}}

    if not D1:
        jmax = a4B / np.abs(e4B)
        jmax_s = stats(jmax)
        D2 = bool(jmax_s["mean"] <= J_c)
        out["J_max"] = jmax_s
        out["D2"] = D2
        if not D2:
            out["window"] = [J_c, jmax_s["mean"]]
            out["marginal"] = bool(jmax_s["mean"] < 1.5 * J_c)
    else:
        out["D2"] = None

    # L=6 volume-trend consistency (report only)
    if "agg_L6" in p1:
        out["L6_c_K_loop"] = p1["agg_L6"]["c_K_loop"]
        out["L6_loop_a4_B"] = p1["agg_L6"]["loop_a4_B"]

    verdict = ("D1 TOTAL DEATH (radiative route)" if D1 else
               "D2 WINDOW DEATH" if out["D2"] else
               "WINDOW EXISTS -> phase 3")
    out["verdict_phase2"] = verdict
    core.save_json("n5_phase2.json", out)
    print(json.dumps(out, indent=2, default=str))
    print("\nVERDICT:", verdict)


if __name__ == "__main__":
    main()
