"""
f1b_dH_scaling2.py — F1b: d_H(volume) na fase estendida COM barras de erro por blocking.

Responde à Condição 1 do escrutínio: tornar "d_H rumo a 3" uma afirmação ESTATÍSTICA
(blocking, como no G5 de F1), não visual. Mede d_H em ≥4 volumes, com n_meas medições por
volume separadas por `gap` sweeps, erro por blocking; depois extrapola V→∞ e reporta se o
crescimento é significativo além das barras.

Baseline: fase estendida k0=1 (CDT 3D puro, F1b). Sem importação de TEIC/DEV/SR.
"""
import json
import os
import time

import numpy as np

from f1b_dH import equilibrate
from fs_seed3d import blocking_error


def dH_with_blocking(k0, T, Vt, seed, therm=160, n_meas=40, gap=4, n_blocks=10):
    g, k3 = equilibrate(k0, T, Vt, seed, therm=therm)
    eps = 0.0012
    dHs = []
    for _ in range(n_meas):
        for _ in range(gap):
            g.sweep(k0, k3, eps, Vt, n_steps=Vt)
        dHs.append(g.measure_dH(n_sources=50))
    dHs = np.array(dHs)
    ok = len(g.check_manifold()) == 0
    return {
        'k0': k0, 'T': T, 'Vt': Vt, 'N3': g.N3, 'N0': g.N0,
        'dH_mean': float(np.nanmean(dHs)),
        'dH_block_err': blocking_error(dHs, n_blocks),
        'dH_naive_err': float(np.nanstd(dHs) / np.sqrt(len(dHs))),
        'manifold_ok': ok,
        'n_meas': n_meas, 'gap': gap,
    }


def extrapolate(rows):
    """d_H(V) = d_inf - a/log(N3): regressão ponderada pelo erro de blocking."""
    N = np.array([r['N3'] for r in rows], float)
    y = np.array([r['dH_mean'] for r in rows])
    w = 1.0 / np.array([max(r['dH_block_err'], 1e-4) for r in rows]) ** 2
    x = 1.0 / np.log(N)
    # ajuste linear ponderado y = d_inf + a*x  (x->0 quando V->inf)
    W = np.diag(w)
    A = np.vstack([np.ones_like(x), x]).T
    cov = np.linalg.inv(A.T @ W @ A)
    beta = cov @ (A.T @ (w * y))
    d_inf, a = beta[0], beta[1]
    d_inf_err = float(np.sqrt(cov[0, 0]))
    return float(d_inf), d_inf_err, float(a)


if __name__ == "__main__":
    t0 = time.time()
    print("=== F1b: d_H(volume) na fase estendida (k0=1) com blocking ===", flush=True)
    T = 10
    volumes = [1500, 3000, 6000, 9000, 12000]
    rows = []
    for Vt in volumes:
        r = dH_with_blocking(1.0, T, Vt, seed=int(Vt))
        rows.append(r)
        print(f"  Vt={Vt:6d} N3={r['N3']:6d}: d_H = {r['dH_mean']:.3f} "
              f"± {r['dH_block_err']:.3f} (blocking; naive {r['dH_naive_err']:.3f})  "
              f"manifold_ok={r['manifold_ok']}", flush=True)
    d_inf, d_inf_err, a = extrapolate(rows)
    # significância do crescimento: primeiro vs último ponto
    r0, r1 = rows[0], rows[-1]
    diff = r1['dH_mean'] - r0['dH_mean']
    differr = np.sqrt(r0['dH_block_err'] ** 2 + r1['dH_block_err'] ** 2)
    out = {'rows': rows, 'extrap_dinf': d_inf, 'extrap_dinf_err': d_inf_err,
           'extrap_a': a, 'growth_diff': float(diff), 'growth_diff_err': float(differr),
           'growth_sigma': float(diff / differr) if differr > 0 else float('inf')}
    print(f"\n  crescimento {r0['Vt']}→{r1['Vt']}: Δd_H = {diff:.3f} ± {differr:.3f} "
          f"= {out['growth_sigma']:.1f}σ", flush=True)
    print(f"  extrapolação V→∞ (d_H = d_inf − a/log N): d_inf = {d_inf:.2f} ± {d_inf_err:.2f}",
          flush=True)
    p = os.path.join(os.path.dirname(__file__), "f1b_dH_scaling2.json")
    with open(p, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"\n[tempo: {time.time()-t0:.0f}s]  [escrito: {p}]", flush=True)
