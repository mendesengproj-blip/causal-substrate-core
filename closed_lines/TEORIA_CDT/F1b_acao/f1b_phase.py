"""
f1b_phase.py — TEORIA_CDT, Fase F1b: gate de FÍSICA do motor CDT 3D.

Pré-registro: ../F1b_PHASE_GATE.md §4 (gate de física). Motor: f1b_cdt3d.py (E0-3D VERDE).

PERGUNTA (gate-mor de F1b): varrendo k0 (∝1/G), o diagrama de fases conhecido da 3D-CDT
emerge? — i.e. existem (a) fase "crumpled" (k0 pequeno: volume colapsa, coordenação alta),
(b) fase "branched-polymer/estendida" (k0 grande), e em alguma janela uma fase ESTENDIDA
cujo perfil de volume espacial ⟨N31(t)⟩ tem a forma de-Sitter (blob suave ∝ cos^a),
NÃO uma reta nem um colapso.

Observáveis por k0 (todos internos, [GABARITO]=AJL só p/ comparar, anti-contaminação):
  - ⟨N3⟩,⟨N0⟩ (controle de volume via auto-sintonia de k3 ao alvo Vt).
  - perfil n(t)=N31(t) (centralizado pelo máximo, média sobre medições).
  - IPR = (Σn)²/Σn²  = #efetivo de fatias ocupadas (1≈colapso, T≈espalhado uniforme).
  - coordenação máxima de vértice (diverge no crumpled).
  - ajuste de-Sitter cos^3 ao blob centralizado (R²).

Sem importação de TEIC/DEV/SR.
"""

import json
import os
import time

import numpy as np

from f1b_cdt3d import CDT3D


def max_vertex_coordination(g):
    return max((len(s) for s in g.vert2tet.values()), default=0)


def centered_profile(prof):
    """Desloca circularmente p/ pôr o CENTRO-DE-MASSA circular no centro (T//2).

    Centro-de-massa (não o máximo): evita o viés de selecionar a fatia-pico a cada
    amostra (que inflaria artificialmente o centro mesmo num perfil uniforme).
    """
    T = len(prof)
    theta = 2 * np.pi * np.arange(T) / T
    R = (prof * np.exp(1j * theta)).sum()
    if abs(R) < 1e-12:
        return prof.copy()
    phi = np.angle(R)                       # ângulo médio
    center_idx = phi * T / (2 * np.pi)
    shift = int(round(T // 2 - center_idx))
    return np.roll(prof, shift)


def desitter_fit(prof_centered, power=2):
    """Ajusta n(t) ∝ A·cos^p((t-t0)/B) ao blob (p=2 em 3D: fatias S² de S³).
    Retorna (R2, B). Varre B; t0 fixo no centro (perfil já centralizado)."""
    T = len(prof_centered)
    t = np.arange(T)
    t0 = T // 2
    y = prof_centered.astype(float)
    if y.sum() <= 0:
        return float('nan'), float('nan')
    best_r2, best_B = -np.inf, np.nan
    x = (t - t0)
    for B in np.linspace(1.0, T / 1.5, 80):
        arg = x / B
        c = np.cos(np.clip(arg, -np.pi / 2, np.pi / 2)) ** power
        shape = np.where(np.abs(arg) < np.pi / 2, c, 0.0)
        if shape.sum() <= 0:
            continue
        A = (y * shape).sum() / (shape * shape).sum()
        pred = A * shape
        ss_res = ((y - pred) ** 2).sum()
        ss_tot = ((y - y.mean()) ** 2).sum()
        r2 = 1 - ss_res / ss_tot if ss_tot > 0 else -np.inf
        if r2 > best_r2:
            best_r2, best_B = r2, B
    return float(best_r2), float(best_B)


def _avg_N3(g, k0, k3, eps, Vt, sweeps, stats):
    vals = []
    for _ in range(sweeps):
        g.sweep(k0, k3, eps, Vt, n_steps=Vt, stats=stats)
        vals.append(g.N3)
    return float(np.mean(vals[len(vals) // 2:]))


def run_k0(k0, T=24, Vt=2200, seed=0, therm_sweeps=180, meas_sweeps=180,
           eps=0.0015, k3_0=0.8, verbose=True):
    g = CDT3D(T, seed=seed)
    rng = g.rng
    # cresce até perto do volume alvo (só (2,6))
    while g.N3 < Vt * 0.7:
        g.move_26(g.spatial_set.sample(rng))
    stats = {}
    # ---- CALIBRAÇÃO de k3 (Newton: ⟨N3⟩(k3) é monótona decrescente) ----
    # μ(k0) = potencial químico entrópico ≈ k3 + 2·eps·(⟨N3⟩−Vt). Centrar: k3 ← μ.
    k3 = k3_0
    for _ in range(3):
        n3 = _avg_N3(g, k0, k3, eps, Vt, 25, stats)
        k3 = k3 + 2.0 * eps * (n3 - Vt)   # passo de Newton (1/[dN3/dk3]≈2eps)
    # termalização final no k3 calibrado
    for _ in range(therm_sweeps):
        g.sweep(k0, k3, eps, Vt, n_steps=Vt, stats=stats)
    # medição
    profiles = []
    n3s, n0s, iprs, maxcoord = [], [], [], []
    for s in range(meas_sweeps):
        g.sweep(k0, k3, eps, Vt, n_steps=Vt, stats=stats)
        if s % 3 == 0:
            prof = g.spatial_volume_profile().astype(float)
            profiles.append(centered_profile(prof))
            n3s.append(g.N3)
            n0s.append(g.N0)
            ssum = prof.sum()
            iprs.append((ssum ** 2) / (prof ** 2).sum() if (prof**2).sum() > 0 else 0)
            maxcoord.append(max_vertex_coordination(g))
    mean_prof = np.mean(profiles, axis=0)
    r2, B = desitter_fit(mean_prof, power=2)
    n0_mean = float(np.mean(n0s))
    n3_mean = float(np.mean(n3s))
    avg_coord = 4 * n3_mean / n0_mean
    peak = float(mean_prof.max())
    baseline = float(np.sort(mean_prof)[:max(1, T // 5)].mean())  # média do 1/5 menor
    errs = g.check_manifold()
    res = {
        'k0': k0, 'T': T, 'Vt': Vt, 'k3_final': round(k3, 4),
        'N3_mean': n3_mean, 'N3_std': float(np.std(n3s)),
        'N0_mean': n0_mean, 'avg_coord': avg_coord,
        'IPR_mean': float(np.mean(iprs)), 'IPR_std': float(np.std(iprs)),
        'maxcoord_mean': float(np.mean(maxcoord)), 'maxcoord_max': int(np.max(maxcoord)),
        'maxcoord_over_avg': float(np.mean(maxcoord)) / avg_coord,
        'desitter_R2': r2, 'desitter_B': B,
        'peak_over_baseline': peak / baseline if baseline > 0 else float('inf'),
        'mean_profile': [round(float(x), 2) for x in mean_prof],
        'manifold_ok': len(errs) == 0,
    }
    if verbose:
        print(f"k0={k0:.2f}: N3={res['N3_mean']:.0f}±{res['N3_std']:.0f} N0={n0_mean:.0f} "
              f"IPR={res['IPR_mean']:.1f}/{T} coord_avg={avg_coord:.0f} "
              f"maxcoord={res['maxcoord_mean']:.0f}(={res['maxcoord_over_avg']:.1f}x) "
              f"deSitter_R2={r2:.3f} pk/base={res['peak_over_baseline']:.1f} "
              f"manifold_ok={res['manifold_ok']}")
    return res


if __name__ == "__main__":
    import sys
    t0 = time.time()
    T = 24
    Vt = 1800
    k0_values = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]
    if len(sys.argv) > 1:
        k0_values = [float(x) for x in sys.argv[1:]]
    print(f"=== F1b GATE DE FÍSICA — scan de k0 (T={T}, Vt={Vt}, cos^2) ===")
    results = []
    for k0 in k0_values:
        results.append(run_k0(k0, T=T, Vt=Vt, seed=int(100 + 10 * k0),
                              therm_sweeps=130, meas_sweeps=130))
    out = os.path.join(os.path.dirname(__file__), "f1b_phase_scan.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\n[tempo total: {time.time()-t0:.0f}s]  [escrito: {out}]")
