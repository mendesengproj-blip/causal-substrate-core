"""f2_g2.py -- F2 main run: the verbatim N1 suite measured for G2.

RUNS ONLY IF f2_gate.json is GREEN.

Suite (PRE_REGISTRO.md + ADENDO):
  [1] ordering on the causal substrate (P-F2-1; weak P-F2-5: J_c in [0.4,0.8]);
  [2] Goldstone twists: expected 14/14 (dim G2) (P-F2-2);
  [3] topology: diag-so(3) hedgehog, B_est -> 8 = 2 x Dynkin index (P-F2-3,
      corrected pre-run in the ADENDO), monotone ladder, anti = -B;
  [4] gauge at u-matched betas {24.5, 32.7}: Creutz chi(2,2) > 0, V(r)
      increasing, sigma decreasing with beta (P-F2-4).
Deaths D-F2-1..4 as pre-registered.
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
from f2_gate import (run_point_stack, ordering_scan_stack,
                     gauge_confinement_stack)

JS_G2 = [0.05, 0.1, 0.3, 0.5, 0.7, 1.0, 1.4, 2.0]
GAUGE_BETAS = [24.5, 32.7]        # u = beta/(2 N^2) matched to N1: 0.25, 0.333
LADDER_LS = (15, 21, 31)
B_TARGET = 8.0                    # ADENDO: 2 x Dynkin index (T(7)=1 vs 1/2)


def main():
    t0 = time.time()
    gate = json.loads((HERE / "f2_gate.json").read_text())
    if gate["verdict"] != "GREEN":
        print("GATE IS RED -- refusing to run G2.")
        sys.exit(1)
    print("=" * 74)
    print("F2 -- G2 verbatim suite (gate GREEN)")
    print("=" * 74)

    T, _ = gc.g2_generators()
    sampler = lambda n, r: gc.haar_walk(T, n, r)

    # [1] ordering
    res, gmean, _ = ordering_scan_stack(T, sampler, JS_G2, "1")
    chis = {J: res[J]["chi"] for J in JS_G2}
    j_peak = max(chis, key=chis.get)
    lro_Js = [J for J in JS_G2 if res[J]["winner"] == "const"]
    ordered = bool(lro_Js)
    j_cross = min(lro_Js) if lro_Js else None
    mermin = {J: abs(res[J]["C_long"] - res[J]["m2"]) / max(res[J]["m2"], 1e-9)
              for J in lro_Js}
    mermin_ok = all(v < 0.10 for v in mermin.values()) if mermin else False
    disordered_ok = all(res[J]["m"] < 3.0 / np.sqrt(gmean["n"])
                        for J in JS_G2 if J <= 0.1)
    print(f"  -> chi-peak J={j_peak}; LRO at J in {lro_Js}; "
          f"Mermin rel dev {[round(v, 3) for v in mermin.values()]}")

    # [2] Goldstones (expected 14 = dim G2)
    print("\n[2] Goldstone twist test (expected 14 = dim G2)")
    gold = gc.goldstone_twists_stack(T, sampler, L=14)
    print(f"  gapless modes: {gold['found']}/{gold['expected']}")
    gold_ok = gold["found"] == gold["expected"]

    # [3] topology: diag-so(3) hedgehog ladder, target 8 = 2 x index
    print("\n[3] topology: G2 hedgehog ladder (target B_est -> 8)")
    J3gen, _, _ = gc.diag_so3(T)
    ladder = {}
    for L in LADDER_LS:
        B = sc.baryon_number(*gc.g2_hedgehog(J3gen, L))
        Bs3 = sc.baryon_number(*sc.embedded_hedgehog(3, L))
        ladder[L] = {"B_g2": B, "B_su3": Bs3, "ratio_vs_su3": B / (8.0 * Bs3)}
        print(f"  L={L}: B_g2={B:+.6f}  B_su3={Bs3:+.6f}  "
              f"B_g2/(8 B_su3)={B/(8.0*Bs3):.6f}")
    Ua, dxa = gc.g2_hedgehog(J3gen, 21, charge=-1)
    Ba = sc.baryon_number(Ua, dxa)
    B21 = ladder[21]["B_g2"]
    print(f"  anti (L=21): B = {Ba:+.4f} (target -B)")
    Bs = [ladder[L]["B_g2"] for L in LADDER_LS]
    topo_ok = (Bs[0] < Bs[1] < Bs[2] <= B_TARGET
               and abs(Ba + B21) < 1e-6
               and all(abs(ladder[L]["ratio_vs_su3"] - 1.0) < 0.005
                       for L in LADDER_LS))

    # [4] gauge / confinement at u-matched betas
    print("\n[4] G2 gauge sector, u-matched betas")
    gres = {}
    for beta in GAUGE_BETAS:
        gres[beta] = gauge_confinement_stack(T, sampler, 7, beta)
        d = gres[beta]
        print(f"  beta={beta:5.1f}: V(r)={[round(v, 3) for v in d['V_r']]}  "
              f"creutz(2,2)={d['creutz22']:.3f}  V_inc={d['V_increases']}")
    beta_strong = min(GAUGE_BETAS)
    confine_ok = (gres[beta_strong]["creutz22"] > 0.05
                  and gres[beta_strong]["V_increases"])
    sigma_trend_ok = (gres[beta_strong]["creutz22"]
                      > gres[max(GAUGE_BETAS)]["creutz22"])

    # P-F2-5 (weak): J_c bracket
    jc_weak_ok = (j_cross is not None) and (0.4 <= j_cross <= 0.8)

    checks = {"orders_with_LRO": ordered, "disordered_low_J": disordered_ok,
              "mermin": mermin_ok, "goldstone_14": gold_ok,
              "topology_B8": topo_ok, "confinement_strong": confine_ok,
              "sigma_decreasing": sigma_trend_ok}
    all_ok = all(checks.values())
    verdict = ("A -- G2 mirrors SU(3)/SU(4): layer 3 is group-generic beyond "
               "SU(N); measured confinement signature is center-independent "
               "at these scales" if all_ok else
               "B -- a break was found: check the corresponding death D-F2-*")
    print("-" * 74)
    for k, v in checks.items():
        print(f"  {k:22s}: {v}")
    print(f"  P-F2-5 weak (J_c in [0.4,0.8]): {jc_weak_ok} "
          f"[crossover at J={j_cross}]")
    print(f"VERDICT: {verdict}")
    print(f"({time.time() - t0:.0f}s)")

    payload = {
        "campaign": "F2_CONTROLE_G2", "stage": "g2_suite",
        "config": {"Js": JS_G2, "gauge_betas": GAUGE_BETAS,
                   "B_target": B_TARGET},
        "graph": gmean,
        "ordering": {str(J): res[J] for J in JS_G2},
        "chi_peak_J": j_peak, "lro_Js": lro_Js, "j_crossover": j_cross,
        "mermin_rel": {str(k): v for k, v in mermin.items()},
        "goldstone": {"expected": gold["expected"], "found": gold["found"]},
        "topology": {"ladder": {str(L): ladder[L] for L in ladder},
                     "B_anti_L21": Ba},
        "gauge": {str(b): gres[b] for b in GAUGE_BETAS},
        "checks": checks, "p_f2_5_weak": jc_weak_ok,
        "verdict": verdict,
        "runtime_s": time.time() - t0,
    }
    (HERE / "f2_g2.json").write_text(json.dumps(payload, indent=2))
    print("saved f2_g2.json")


if __name__ == "__main__":
    main()
