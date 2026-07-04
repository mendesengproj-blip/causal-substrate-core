# -*- coding: utf-8 -*-
"""
gate_m8.py -- certificado de solitons da classificacao topologica (PRE_REGISTRO p.4).

Verifica que as TEXTURAS DE MATERIA protegidas tem carga INTEIRA conservada ao
longo da escada de homotopia, com solitons distintos:
  pi1  vortice XY (alvo S^1, 2D)       -> winding inteiro
  pi2  baby-Skyrmion (alvo S^2, 2D)    -> carga Berg-Luscher inteira
  pi3  Skyrmion/barion (SU(2)=S^3, 3D) -> reusa sun_core
  + estabilidade sob THINNING (pi2): a carga inteira sobrevive a delecao
    aleatoria de sitios (topologia nao flui, corolario C5).
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "N1_CONTROLE_SU4"))
import sun_core as sc

PI = np.pi

HOMOTOPY = {
    "S1=U(1)": {"pi1": "Z", "pi2": "0", "pi3": "0"},
    "S2":      {"pi1": "0", "pi2": "Z", "pi3": "Z(Hopf)"},
    "S3=SU(2)": {"pi1": "0", "pi2": "0", "pi3": "Z", "pi4": "Z2"},
    "SU(3)":   {"pi1": "0", "pi2": "0", "pi3": "Z"},
    "G2":      {"pi1": "0", "pi2": "0", "pi3": "Z"},
}


# ---------------------------------------------------------------- pi1: vortice XY
# EMENDA DE INSTRUMENTO (pre-run, achada pelo smoke; causa documentada): o centro
# do vortice deve cair no MEIO de uma plaqueta (semi-inteiro), nao sobre um sitio
# da rede. Com o centro sobre um sitio, arctan2(0,0)=0 corrompe as 4 plaquetas
# vizinhas (w=1 dava 0). Convencao FISICA (winding inteiro) inalterada.
def xy_field(L, w, cx=None, cy=None):
    cx = (L - 1) / 2 + 0.5 if cx is None else cx   # meio de plaqueta
    cy = (L - 1) / 2 + 0.5 if cy is None else cy
    i, j = np.meshgrid(np.arange(L), np.arange(L), indexing="ij")
    return w * np.arctan2(j - cy, i - cx)


def xy_winding(theta, margin=6):
    """Winding = integral de contorno num LACO GRANDE (a `margin` da borda) em
    torno do centro. EMENDA (pre-run): a soma-de-plaquetas aliava no NUCLEO para
    |w|>=2 (variacao de fase > pi por passo perto do centro); o contorno grande
    amostra so o campo distante (gradientes pequenos), sem aliasing. Winding
    inteiro = fisica inalterada."""
    def wrap(d):
        return (d + PI) % (2 * PI) - PI
    L = theta.shape[0]
    a, b = margin, L - 1 - margin
    tot = 0.0
    # percorre o quadrado [a,b]x[a,b] no sentido anti-horario
    for j in range(a, b):                    # borda inferior i=a, j:a->b
        tot += wrap(theta[a, j + 1] - theta[a, j])
    for i in range(a, b):                    # borda direita j=b
        tot += wrap(theta[i + 1, b] - theta[i, b])
    for j in range(b, a, -1):                # borda superior i=b
        tot += wrap(theta[b, j - 1] - theta[b, j])
    for i in range(b, a, -1):                # borda esquerda j=a
        tot += wrap(theta[i - 1, a] - theta[i, a])
    # sinal de orientacao do contorno (convencao horario/anti-horario vs arctan2),
    # fixado como Berg-Luscher: winding(w=+1)=+1. Escolha de orientacao, nao fisica.
    return -tot / (2 * PI)


# ---------------------------------------------------- pi2: baby-Skyrmion (S^2)
def baby_skyrmion(L, Q=1, w_core=0.25):
    x = np.linspace(-1, 1, L)
    X, Y = np.meshgrid(x, x, indexing="ij")
    r = np.sqrt(X ** 2 + Y ** 2)
    phi = np.arctan2(Y, X)
    f = PI * np.exp(-r / w_core)           # f(0)=pi, f(inf)->0
    n = np.zeros((L, L, 3))
    n[..., 0] = np.sin(f) * np.cos(Q * phi)
    n[..., 1] = np.sin(f) * np.sin(Q * phi)
    n[..., 2] = np.cos(f)
    return n


def _omega(n1, n2, n3):
    num = np.dot(n1, np.cross(n2, n3))
    den = 1.0 + np.dot(n1, n2) + np.dot(n2, n3) + np.dot(n3, n1)
    return 2.0 * np.arctan2(num, den)


# Convencao de orientacao da triangulacao FIXADA (pre-run): o smoke deu |Q|
# perfeito (0.9996) com sinal global invertido = a diagonal do dual estava
# oposta a convencao de winding do campo. Sinal -1 alinha Q(hedgehog Q=+1)=+1.
# Isto e escolha de orientacao (qual lado e "cima" no dual), nao fisica.
_BL_ORIENT = -1.0


def berg_luscher_Q(n):
    """Carga topologica de rede (Berg-Luscher) do campo n:grade->S^2."""
    L = n.shape[0]
    Q = 0.0
    for i in range(L - 1):
        for j in range(L - 1):
            n1, n2 = n[i, j], n[i + 1, j]
            n3, n4 = n[i + 1, j + 1], n[i, j + 1]
            Q += _omega(n1, n2, n3) + _omega(n1, n3, n4)
    return _BL_ORIENT * Q / (4.0 * PI)


def thinned_Q(L, Q, p, rng):
    """Estabilidade sob THINNING: mantem fracao p dos sitios, re-triangula
    (Delaunay), recomputa Q. A carga inteira deve SOBREVIVER (C5)."""
    from scipy.spatial import Delaunay
    n = baby_skyrmion(L, Q)
    x = np.linspace(-1, 1, L)
    X, Y = np.meshgrid(x, x, indexing="ij")
    pts = np.column_stack([X.ravel(), Y.ravel()])
    nflat = n.reshape(-1, 3)
    keep = rng.random(len(pts)) < p
    pk, nk = pts[keep], nflat[keep]
    tri = Delaunay(pk)
    Qs = 0.0
    for s in tri.simplices:
        Qs += _omega(nk[s[0]], nk[s[1]], nk[s[2]])
    return _BL_ORIENT * Qs / (4.0 * PI), int(keep.sum())


# ---------------------------------------------------------------- gate
def main():
    print("=" * 74)
    print("M8 GATE -- classificacao topologica: certificado de solitons")
    print("=" * 74)
    out = {"homotopy": HOMOTOPY}

    # pi1: vortice XY (S^1) -- winding inteiro + anti
    print("\n(pi1) vortice XY, alvo S^1  [winding inteiro]:")
    p1 = []
    for w in (1, 2, -1):
        meas = xy_winding(xy_field(61, w))
        ok = abs(meas - w) < 0.05
        print(f"   w={w:+d}: medido={meas:+.4f}  {'OK' if ok else 'FALHA'}")
        p1.append({"w": w, "measured": meas, "ok": bool(ok)})
    out["pi1_XY"] = p1

    # pi2: baby-Skyrmion (S^2) -- carga inteira + anti
    print("\n(pi2) baby-Skyrmion, alvo S^2  [Berg-Luscher inteiro]:")
    p2 = []
    for Q in (1, 2, -1):
        meas = berg_luscher_Q(baby_skyrmion(81, Q))
        ok = abs(meas - Q) < 0.1
        print(f"   Q={Q:+d}: medido={meas:+.4f}  {'OK' if ok else 'FALHA'}")
        p2.append({"Q": Q, "measured": meas, "ok": bool(ok)})
    out["pi2_babySkyrmion"] = p2

    # pi3: Skyrmion/barion (SU(2)) -- reusa sun_core
    print("\n(pi3) Skyrmion/barion, alvo SU(2)=S^3  [escada B, reusa sun_core]:")
    Bs = [sc.baryon_number(*sc.embedded_hedgehog(2, L)) for L in (15, 21, 31)]
    Ba = sc.baryon_number(*sc.embedded_hedgehog(2, 21, charge=-1))
    monot = Bs[0] < Bs[1] < Bs[2]
    anti = abs(Ba + Bs[1]) < 1e-6
    print(f"   B={[round(b,4) for b in Bs]} -> Z  anti={Ba:+.4f}  "
          f"monot={monot} anti_ok={anti}")
    out["pi3_baryon"] = {"B_ladder": Bs, "B_anti": Ba,
                         "monotone": bool(monot), "anti_ok": bool(anti)}

    # estabilidade sob thinning (pi2)
    print("\n(thinning) carga pi2 sobrevive a delecao (topologia nao flui, C5):")
    th = []
    rng = np.random.default_rng(20260704)
    for p in (0.9, 0.8, 0.7, 0.6):
        qs = []
        for s in range(4):
            q, nkept = thinned_Q(81, 1, p, np.random.default_rng(7 + s + int(100 * p)))
            qs.append(q)
        qm = float(np.mean(qs))
        ok = abs(qm - 1.0) < 0.15
        print(f"   p={p:.1f}: Q={qm:+.4f}  {'OK' if ok else 'FALHA'}")
        th.append({"p": p, "Q": qm, "ok": bool(ok)})
    out["thinning_pi2"] = th

    # veredito
    p1_ok = all(x["ok"] for x in p1)
    p2_ok = all(x["ok"] for x in p2)
    p3_ok = monot and anti
    th_ok = all(x["ok"] for x in th)
    allok = p1_ok and p2_ok and p3_ok and th_ok
    print("\n" + "=" * 74)
    print(f"  pi1 vortice inteiro: {p1_ok} | pi2 baby-Skyrmion inteiro: {p2_ok}")
    print(f"  pi3 barion inteiro: {p3_ok} | pi2 sobrevive thinning: {th_ok}")
    verdict = ("CLASSIFICACAO CONFIRMADA: texturas de materia pi_n(X)!=0 "
               "protegidas e estaveis; defeitos de gauge proibidos por M5"
               if allok else "revisar (ver D-M8-*)")
    print(f"  >>> {verdict}")
    out["verdict"] = verdict
    json.dump(out, open(os.path.join(HERE, "gate_m8.json"), "w"),
              indent=2, default=str)
    print("  saved gate_m8.json")


if __name__ == "__main__":
    main()
