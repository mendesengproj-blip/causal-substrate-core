"""
f1b_dH.py — F1b: dimensão de Hausdorff d_H nas fases do CDT 3D (gate-mor de geometria).

Paralelo ao gate-mor de F1 (d_H=2 em 2D). Aqui a pergunta de "geometria emerge": a fase
ESTENDIDA exibe d_H ≈ 3 (espaço-tempo 3D genuíno), enquanto a fase CRUMPLED degenera?
E — o ponto novo do 3D — d_H agora DEPENDE de k0 (curvatura dinâmica), ao contrário do 2D
onde d_H=2 independia da ação (folheação só).

Calibração: d_H também medido na config regular (referência) e reportado.
"""
import json
import os
import time

import numpy as np

from f1b_cdt3d import CDT3D
from f1b_phase import _avg_N3


def equilibrate(k0, T, Vt, seed, therm=140, eps=0.0012, k3_0=0.8):
    g = CDT3D(T, seed=seed)
    rng = g.rng
    while g.N3 < Vt * 0.7:
        g.move_26(g.spatial_set.sample(rng))
    stats = {}
    k3 = k3_0
    for _ in range(3):
        n3 = _avg_N3(g, k0, k3, eps, Vt, 25, stats)
        k3 = k3 + 2.0 * eps * (n3 - Vt)
    for _ in range(therm):
        g.sweep(k0, k3, eps, Vt, n_steps=Vt, stats=stats)
    return g, k3


def dH_phase(k0, T=12, Vt=4000, seed=0, n_meas=8, gap=8):
    g, k3 = equilibrate(k0, T, Vt, seed)
    eps = 0.0012
    dHs = []
    for _ in range(n_meas):
        for _ in range(gap):
            g.sweep(k0, k3, eps, Vt, n_steps=Vt)
        dHs.append(g.measure_dH(n_sources=40))
    dHs = np.array(dHs)
    ok = len(g.check_manifold()) == 0
    res = {'k0': k0, 'T': T, 'Vt': Vt, 'k3': round(k3, 3),
           'dH_mean': float(np.nanmean(dHs)), 'dH_std': float(np.nanstd(dHs)),
           'dH_samples': [round(float(x), 3) for x in dHs],
           'N3': g.N3, 'N0': g.N0, 'manifold_ok': ok}
    print(f"k0={k0:.1f} [{'estendida' if k0<5 else 'crumpled'}]: "
          f"d_H = {res['dH_mean']:.2f} ± {res['dH_std']:.2f}  "
          f"(N3={g.N3}, N0={g.N0}, manifold_ok={ok})")
    return res


if __name__ == "__main__":
    t0 = time.time()
    print("=== F1b d_H nas fases (gate-mor de geometria) ===")
    # referência: config regular (sem dinâmica)
    g0 = CDT3D(12, seed=0)
    rng = g0.rng
    while g0.N3 < 4000 * 0.7:
        g0.move_26(g0.spatial_set.sample(rng))
    print(f"referência (regular, sem ação, N3={g0.N3}): d_H = {g0.measure_dH(n_sources=40):.2f}")
    results = []
    for k0 in [1.0, 2.0, 3.0, 7.0, 8.0]:
        results.append(dH_phase(k0, seed=int(200 + 10 * k0)))
    out = os.path.join(os.path.dirname(__file__), "f1b_dH.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\n[tempo: {time.time()-t0:.0f}s]  [escrito: {out}]")
