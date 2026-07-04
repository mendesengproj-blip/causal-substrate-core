"""n1_su4.py -- N1 main run: the verbatim SU(3) suite measured for SU(4).

RUNS ONLY IF the engineering gate (n1_gate_su3.py) is GREEN.

Suite (PRE_REGISTRO.md):
  [1] ordering on the causal substrate: J_c, U4, LRO + Mermin C_long = m^2;
  [2] Goldstone twist test: expected 15/15 gapless (dim SU(4));
  [3] topology: embedded hedgehog B = +1 / -1 (pi_3(SU(4)) = Z, Bott);
  [4] gauge sector: scale-matched betas {8.0, 10.7} (= FLC quick x 16/9),
      Creutz chi(2,2) > 0 at strong coupling, sigma(beta) decreasing.
Verdicts: A = all four mirror SU(3) => "SU(3) hosted, not selected";
          B = any break => hidden selection (investigate immediately).
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import sun_core as sc
from n1_gate_su3 import (build_causal_seed, ordering_scan, gauge_confinement,
                         JS as JS_GATE)

HERE = Path(__file__).resolve().parent

NGROUP = 4
JS_SU4 = [0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.7, 1.0, 2.0]
GAUGE_BETAS = [8.0, 10.7]           # FLC quick {4.5, 6.0} x 16/9 (scale-matched)


def main():
    t0 = time.time()
    gate = json.loads((HERE / "n1_gate_su3.json").read_text())
    if gate["verdict"] != "GREEN":
        print("GATE IS RED -- refusing to run SU(4).")
        sys.exit(1)
    print("=" * 74)
    print("N1 -- SU(4) verbatim suite (gate GREEN)")
    print("=" * 74)

    # [1] ordering
    res, gmean, _ = ordering_scan(NGROUP, JS_SU4, "1")
    chis = {J: res[J]["chi"] for J in JS_SU4}
    j_peak = max(chis, key=chis.get)
    lro_Js = [J for J in JS_SU4 if res[J]["winner"] == "const"]
    ordered = bool(lro_Js)
    mermin = {J: abs(res[J]["C_long"] - res[J]["m2"]) / max(res[J]["m2"], 1e-9)
              for J in lro_Js}
    mermin_ok = all(v < 0.10 for v in mermin.values()) if mermin else False
    disordered_ok = all(res[J]["m"] < 3.0 / np.sqrt(gmean["n"])
                        for J in JS_SU4 if J <= 0.1)
    print(f"  -> chi-peak J={j_peak}; LRO at J in {lro_Js}; "
          f"Mermin rel dev {[round(v,3) for v in mermin.values()]}")

    # [2] Goldstones
    print("\n[2] Goldstone twist test (expected 15 = dim SU(4))")
    gold = sc.goldstone_twists(NGROUP, L=14)
    print(f"  gapless modes: {gold['found']}/{gold['expected']}")
    gold_ok = gold["found"] == gold["expected"]

    # [3] topology -- CORRECTED CHECK (documented in RESULTADO.md): FL1 itself
    # measures B on a convergence ladder (L=15..41: 0.806, 0.892, 0.948, 0.969
    # -> 1); B at fixed L is discretization-limited, identically for every N
    # (the log acts only in the SU(2) block).  The right pi_3 check is therefore
    # N-INVARIANCE at each L plus monotone convergence toward 1 -- not |B-1|<eps
    # at the quick L (that check is unpassable for SU(3) itself).
    print("\n[3] topology: embedded hedgehog ladder, SU(4) vs SU(3) (live)")
    ladder = {}
    for L in (15, 21, 31):
        B3 = sc.baryon_number(*sc.embedded_hedgehog(3, L))
        B4 = sc.baryon_number(*sc.embedded_hedgehog(NGROUP, L))
        ladder[L] = {"B_su3": B3, "B_su4": B4, "diff": abs(B4 - B3)}
        print(f"  L={L}: B_su3={B3:+.6f}  B_su4={B4:+.6f}  |diff|={abs(B4-B3):.2e}")
    Ua, dxa = sc.embedded_hedgehog(NGROUP, 21, charge=-1)
    Ba = sc.baryon_number(Ua, dxa)
    B = ladder[21]["B_su4"]
    print(f"  anti (L=21): B = {Ba:+.4f} (target -B)")
    Bs = [ladder[L]["B_su4"] for L in (15, 21, 31)]
    topo_ok = (all(ladder[L]["diff"] < 0.005 for L in ladder)
               and Bs[0] < Bs[1] < Bs[2] <= 1.0
               and abs(Ba + B) < 1e-6)

    # [4] gauge / confinement
    print("\n[4] SU(4) gauge sector, scale-matched betas")
    T4 = sc.generators(NGROUP)
    gres = {}
    for beta in GAUGE_BETAS:
        gres[beta] = gauge_confinement(NGROUP, beta, T4)
        d = gres[beta]
        print(f"  beta={beta:5.1f}: V(r)={[round(v,3) for v in d['V_r']]}  "
              f"creutz(2,2)={d['creutz22']:.3f}  V_inc={d['V_increases']}")
    beta_strong = min(GAUGE_BETAS)
    confine_ok = (gres[beta_strong]["creutz22"] > 0.05
                  and gres[beta_strong]["V_increases"])
    sigma_trend_ok = (gres[beta_strong]["creutz22"]
                      > gres[max(GAUGE_BETAS)]["creutz22"])

    # verdict
    checks = {"orders_with_LRO": ordered, "disordered_low_J": disordered_ok,
              "mermin": mermin_ok, "goldstone_15": gold_ok,
              "topology_B": topo_ok, "confinement_strong": confine_ok,
              "sigma_decreasing": sigma_trend_ok}
    all_ok = all(checks.values())
    verdict = ("A -- SU(4) works the same: SU(3) is HOSTED, not selected"
               if all_ok else
               "B -- a break was found: hidden selection, investigate")
    print("-" * 74)
    for k, v in checks.items():
        print(f"  {k:22s}: {v}")
    print(f"VERDICT: {verdict}")
    print(f"({time.time()-t0:.0f}s)")

    payload = {
        "campaign": "N1_CONTROLE_SU4", "stage": "su4_suite",
        "config": {"Js": JS_SU4, "gauge_betas": GAUGE_BETAS},
        "graph": gmean,
        "ordering": {str(J): res[J] for J in JS_SU4},
        "chi_peak_J": j_peak, "lro_Js": lro_Js,
        "mermin_rel": {str(k): v for k, v in mermin.items()},
        "goldstone": {"expected": gold["expected"], "found": gold["found"]},
        "topology": {"ladder": {str(L): ladder[L] for L in ladder},
                     "B_anti_L21": Ba,
                     "check_note": "corrected to FL1 ladder protocol; see RESULTADO"},
        "gauge": {str(b): gres[b] for b in GAUGE_BETAS},
        "checks": checks, "verdict": verdict,
        "runtime_s": time.time() - t0,
    }
    (HERE / "n1_su4.json").write_text(json.dumps(payload, indent=2))
    print("saved n1_su4.json")


if __name__ == "__main__":
    main()
