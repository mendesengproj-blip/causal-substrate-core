# -*- coding: utf-8 -*-
"""
gate_m6.py -- gate ESTRUTURAL barato do teorema de hospedagem (PRE_REGISTRO p.3).

Mede so invariantes de teoria de grupos (contagem de Goldstone por twist +
carga pi3 por hedgehog), NUNCA a MC de ordenamento (respeita 'SU(5+) nunca').
Reusa sun_core (SU(N)) e g2_core (G2). Adiciona o COSET O(3)=SU(2)/U(1)=S^2, a
prova afiada de que a forma rastreia X=G/H (=2), nao o grupo (=3).
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "N1_CONTROLE_SU4"))
sys.path.insert(0, os.path.join(HERE, "..", "F2_CONTROLE_G2"))
import sun_core as sc
import g2_core as gc

PI = np.pi


# ====================================================================== #
# COSET O(3) = SU(2)/U(1) = S^2 : twist de Goldstone (esperado 2 = dim S^2)
# ====================================================================== #
def _rot(axis, th):
    c, s = np.cos(th), np.sin(th)
    if axis == 0:
        return np.array([[1, 0, 0], [0, c, -s], [0, s, c]])
    if axis == 1:
        return np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]])
    return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])


def o3_goldstone_twists(L=14):
    """Campo n in S^2, vacuo n0=zhat. Twist por rotacao em torno de cada eixo
    so(3); E = soma_ligacoes (1 - n.n'). Rotacao em torno de zhat fixa n0 (dE=0,
    U(1) nao-quebrado); em torno de x,y precessa (dE~k^2, Goldstone). Esperado 2."""
    n0 = np.array([0.0, 0.0, 1.0])
    x = np.arange(L)
    ks = [2 * PI * nk / L for nk in (1, 2, 3)]
    found = 0
    modes = {}
    for a in range(3):                       # 3 geradores so(3)
        dEs, stiff = [], []
        for k in ks:
            ncol = np.array([_rot(a, k * xx) @ n0 for xx in x])   # (L,3)
            dots = np.sum(ncol[:-1] * ncol[1:], axis=1)           # ligacoes ao longo do eixo
            E = (L * L) * float(np.sum(1.0 - dots))               # L^2 linhas; outros eixos = 0
            dEs.append(E)
            stiff.append(E / k ** 2)
        gapless = (dEs[0] > 1e-9) and (dEs[0] < dEs[-1]) and (stiff[0] > 1e-6)
        found += int(gapless)
        modes[f"gen_{a}"] = {"dE": dEs, "gapless": bool(gapless)}
    return {"target": "O(3)=SU(2)/U(1)=S^2", "expected": 2, "found": found,
            "modes": modes}


# ====================================================================== #
# GATE
# ====================================================================== #
def goldstone_group(label, expected, twist_fn):
    r = twist_fn()
    ok = (r["found"] == expected)
    print(f"  Goldstone {label:>16}: {r['found']}/{expected}  "
          f"=> {'OK' if ok else 'FALHA'}")
    return {"target": label, "expected": expected, "found": r["found"], "ok": ok}


def pi3_ladder(label, hedgehog_fn, Ls=(15, 21, 31)):
    """Escada de carga pi3 (hedgehog); confirma inteiro monotono + anti=-B."""
    Bs = []
    for L in Ls:
        U, dx = hedgehog_fn(L)
        Bs.append(sc.baryon_number(U, dx))
    Ua, dxa = hedgehog_fn(21, charge=-1)
    Ba = sc.baryon_number(Ua, dxa)
    monot = Bs[0] < Bs[1] < Bs[2]
    anti = abs(Ba + Bs[1]) < 1e-6
    print(f"  pi3-ladder {label:>14}: B={[round(b,4) for b in Bs]} "
          f"anti={Ba:+.4f} monot={monot} anti_ok={anti}")
    return {"target": label, "B_ladder": Bs, "B_anti": Ba,
            "monotone": bool(monot), "anti_ok": bool(anti)}


def main():
    print("=" * 72)
    print("M6 GATE -- hospedagem: contagem de Goldstone = dim X + carga pi3")
    print("=" * 72)
    out = {}

    # (G-count) Goldstone = dim X
    print("\n(1) Goldstone = dim X (twist estatico):")
    gcount = []
    # SU(N): dim = N^2-1
    for N in (2, 3, 4):
        gcount.append(goldstone_group(
            f"SU({N})", N * N - 1, lambda N=N: sc.goldstone_twists(N, L=14)))
    # G2: dim 14
    T, _ = gc.g2_generators()
    sampler = lambda n, r: gc.haar_walk(T, n, r)
    gcount.append(goldstone_group(
        "G2", 14, lambda: gc.goldstone_twists_stack(T, sampler, L=14)))
    # COSET O(3)=S^2: dim 2 (a prova afiada)
    gcount.append(goldstone_group("O(3)=S^2", 2, lambda: o3_goldstone_twists(L=14)))
    out["goldstone"] = gcount

    # (pi3) carga inteira -- reconfirma SU(2), SU(3) barato (G2/SU4 ja em F2/N1)
    print("\n(2) carga pi3 (hedgehog; SU4/G2 ja em N1/F2, reconfirma SU2/SU3):")
    p3 = []
    for N in (2, 3):
        p3.append(pi3_ladder(
            f"SU({N})", lambda L, charge=1, N=N: sc.embedded_hedgehog(N, L, charge=charge)))
    out["pi3"] = p3

    # (tabela a-priori) grupos NAO simulados
    apriori = {
        "SU(5)": {"dim": 24, "pi3": "Z"}, "SO(5)": {"dim": 10, "pi3": "Z"},
        "Sp(2)": {"dim": 10, "pi3": "Z"}, "F4": {"dim": 52, "pi3": "Z"},
        "E6": {"dim": 78, "pi3": "Z"},
    }
    print("\n(3) tabela a-priori (dim G/H = Goldstones; pi3=Z universal, Bott):")
    for g, d in apriori.items():
        print(f"     {g:>6}: dim={d['dim']:>3}  pi3={d['pi3']}")
    out["apriori"] = apriori

    # veredito
    gc_ok = all(x["ok"] for x in gcount)
    coset_ok = [x for x in gcount if x["target"] == "O(3)=S^2"][0]["ok"]
    p3_ok = all(x["monotone"] and x["anti_ok"] for x in p3)
    print("\n" + "=" * 72)
    print(f"  Goldstone=dim X (todos): {gc_ok}")
    print(f"  COSET O(3) rastreia G/H (=2, nao 3): {coset_ok}")
    print(f"  pi3 inteiro/monotono: {p3_ok}")
    verdict = ("HOSPEDAGEM CONFIRMADA: forma = funcao a-priori de X; grupo=input"
               if (gc_ok and coset_ok and p3_ok) else "revisar (ver D-M6-*)")
    print(f"  >>> {verdict}")
    out["verdict"] = verdict
    json.dump(out, open(os.path.join(HERE, "gate_m6.json"), "w"),
              indent=2, default=str)
    print("  saved gate_m6.json")


if __name__ == "__main__":
    main()
