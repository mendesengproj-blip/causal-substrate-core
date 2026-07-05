# -*- coding: utf-8 -*-
"""
n6_gate.py -- gate de engenharia do N6 (PRE_REGISTRO par.5; VERDE obrigatorio).

G1 validade exata da 2D-order; G2 (RE-ESCOPADO, emenda pre-run documentada:
o review nao da os (eps,beta) exatos da Fig.3 => G2 vira padrao QUALITATIVO de
sinal/magnitude; o gate quantitativo DURO e G3) ; G3 beta_c(N,eps) reproduz
1.66(3)/(N eps^2) em N={30,50,70}; G4 assinatura de 1a ordem (histerese
hot/cold); G5 valores de fase (of/altura) a N=50 com tolerancia 15%.
"""
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from n6_core import TwoOrderMCMC, action, observables, relation_matrix, run_point

EPS = 0.21
BETA_PRED = lambda N, eps: 1.66 / (N * eps * eps)
SIG_PUB_REL = 0.03 / 1.66


def g1_validity():
    rng = np.random.default_rng(1)
    ok = True
    for _ in range(50):
        u = rng.permutation(30)
        v = rng.permutation(30)
        R = relation_matrix(u, v)
        Rf = R.astype(np.float32)
        trans_ok = not np.any(((Rf @ Rf) > 0.5) & ~R)      # fecho ja contido
        irrefl = not np.any(np.diag(R))
        antisym = not np.any(R & R.T)
        ok = ok and trans_ok and irrefl and antisym
    return ok


def scan_beta_c(N, eps, n_scan=7, therm=800, meas=100):
    """Estima beta_c pelo cruzamento do ponto-medio de S entre os ramos
    hot (random) e cold (layered3). Retorna (est, sigma_est, curva)."""
    bp = BETA_PRED(N, eps)
    betas = bp * np.linspace(0.6, 1.5, n_scan)
    rows = []
    for b in betas:
        Sh = run_point(N, eps, b, 100 + N, "random", therm, meas, 2)["S"]
        Sc = run_point(N, eps, b, 200 + N, "layered3", therm, meas, 2)["S"]
        rows.append({"beta": float(b), "S_hot": Sh, "S_cold": Sc})
        print(f"    N={N} beta={b:.3f} (x{b/bp:.2f}pred): "
              f"S_hot={Sh:+8.2f}  S_cold={Sc:+8.2f}")
    # ramo medio cruza o ponto medio entre S_random e S_cryst
    S_hi = rows[0]["S_hot"]                     # fase random (beta baixo)
    S_lo = rows[-1]["S_cold"]                   # fase cristalina (beta alto)
    mid = 0.5 * (S_hi + S_lo)
    Sm = np.array([0.5 * (r["S_hot"] + r["S_cold"]) for r in rows])
    idx = np.where(np.diff(np.sign(Sm - mid)))[0]
    if idx.size == 0:
        return None, None, rows
    i = int(idx[0])
    b1, b2 = rows[i]["beta"], rows[i + 1]["beta"]
    s1, s2 = Sm[i] - mid, Sm[i + 1] - mid
    est = b1 - s1 * (b2 - b1) / (s2 - s1)
    sigma_est = 0.5 * (b2 - b1)
    return float(est), float(sigma_est), rows


def main():
    t0 = time.time()
    print("=" * 74)
    print("N6 GATE -- amostrador 2D-orders + acao BD-2D vs fisica publicada")
    print("=" * 74)
    out = {}

    print("\n[G1] validade exata da 2D-order (transitiva, irreflexiva, antisim.)")
    g1 = g1_validity()
    print(f"   -> {'OK' if g1 else 'FALHA'}")
    out["G1"] = bool(g1)

    print("\n[G2+G5] fases profundas a N=50 (G2 qualitativo: emenda documentada)")
    bp50 = BETA_PRED(50, EPS)
    rnd = run_point(50, EPS, 0.2 * bp50, 11, "random", 1200, 150, 2)
    cry = run_point(50, EPS, 3.0 * bp50, 12, "layered3", 1200, 150, 2)
    print(f"   random  : S={rnd['S']:+8.2f} of={rnd['of']:.3f} h={rnd['height']:.1f} "
          f"z={rnd['z_hasse']:.1f} acc={rnd['acc_rate']:.2f} ESS={rnd['ess']:.0f}")
    print(f"   crystal : S={cry['S']:+8.2f} of={cry['of']:.3f} h={cry['height']:.1f} "
          f"z={cry['z_hasse']:.1f} acc={cry['acc_rate']:.2f} ESS={cry['ess']:.0f}")
    g2 = (0.0 < rnd["S"] < 20.0) and (cry["S"] < -20.0)
    g5 = (abs(rnd["of"] - 0.5) < 0.075 and 8.5 <= rnd["height"] <= 11.5 and
          0.51 <= cry["of"] <= 0.69 and 2.0 <= cry["height"] <= 4.0)
    print(f"   G2 (padrao de sinal/magnitude): {g2}   G5 (of/altura 15%): {g5}")
    out["G2"] = bool(g2)
    out["G5"] = bool(g5)
    out["deep_random"] = rnd
    out["deep_crystal"] = cry

    print("\n[G3] beta_c(N,eps) vs 1.66(3)/(N eps^2), eps=0.21")
    g3_all = True
    out["G3_rows"] = {}
    for N in (30, 50, 70):
        bp = BETA_PRED(N, EPS)
        est, sig_est, rows = scan_beta_c(N, EPS)
        if est is None:
            g3_all = False
            print(f"   N={N}: transicao NAO detectada na janela — FALHA")
            continue
        sig = np.hypot(SIG_PUB_REL * bp, sig_est)
        ok = abs(est - bp) <= 2 * sig
        g3_all = g3_all and ok
        print(f"   N={N}: beta_c est={est:.3f} vs pred={bp:.3f} "
              f"(|d|={abs(est-bp):.3f} <= 2sig={2*sig:.3f}) -> {'OK' if ok else 'FALHA'}")
        out["G3_rows"][N] = {"est": est, "pred": bp, "sigma": float(sig),
                             "ok": bool(ok), "curve": rows}
    out["G3"] = bool(g3_all)

    print("\n[G4] assinatura de 1a ordem: histerese hot/cold perto de beta_c")
    # usa as curvas do G3: existe beta com gap |S_hot-S_cold| > 50% do gap de fase
    g4 = False
    for N, d in out["G3_rows"].items():
        rows = d["curve"]
        gap_phase = abs(rows[0]["S_hot"] - rows[-1]["S_cold"])
        for r in rows:
            if abs(r["S_hot"] - r["S_cold"]) > 0.5 * gap_phase:
                g4 = True
    print(f"   -> histerese/coexistencia detectada: {g4}")
    out["G4"] = bool(g4)

    verdict = all(out[k] for k in ("G1", "G2", "G3", "G4", "G5"))
    out["verdict"] = "GREEN" if verdict else "RED"
    out["runtime_s"] = time.time() - t0
    print("\n" + "=" * 74)
    for k in ("G1", "G2", "G3", "G4", "G5"):
        print(f"   {k}: {out[k]}")
    print(f"   GATE: {'VERDE -- bateria autorizada' if verdict else 'VERMELHO'}"
          f"  ({out['runtime_s']:.0f}s)")
    json.dump(out, open(os.path.join(HERE, "n6_gate.json"), "w"),
              indent=2, default=str)
    print("   saved n6_gate.json")


if __name__ == "__main__":
    main()
