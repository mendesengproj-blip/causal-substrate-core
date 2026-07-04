"""
fs_run3d.py — FS-3D: o teste VINCULANTE da semente, com controles EMBUTIDOS desde o início.

Pré-registro: ../SEMENTE_PRE_REGISTRO.md (D1/D2 §2; prior §4 = passa D1, morre D2).
Escrutínio (2026-06-28): rodar em ≥2 pontos da fase estendida (k0≈1 e k0≈3) E construir o
controle de campo genérico (markoviano) como PARTE do experimento — não como reação a um
resultado "impressionante" (o erro do FS-2D, onde o controle veio depois).

Desenho (por ponto k0, mesmo ensemble/seed-base):
  - BLIND  (γ=0):          CDT cega — o NULO de D1.
  - SEED   (γ>0, mode=seed):    informação SOURCE o crescimento (φ memória + transporte).
  - MARKOV (γ>0, mode=markov):  peso GEOMÉTRICO local (coordenação), SEM memória — o NULO de D2,
                                calibrado p/ a MESMA intensidade de modulação da semente.

D1 = a geometria de SEED difere de BLIND? (d_H, clumping, com erro por blocking)
D2 = a diferença de SEED é reproduzível por MARKOV à mesma intensidade? E C_mem(τ) de SEED tem
     CAUDA acima de MARKOV? (a assinatura única da memória não-markoviana)

Sem importação de TEIC/DEV/SR.
"""
import json
import math
import os
import sys
import time

import numpy as np

from fs_seed3d import SeedCDT3D, blocking_error, c_mem
from f1b_phase import _avg_N3


def cmem_tail_with_error(growth, max_tau=15, n_blocks=8):
    """C_mem(τ) (série cheia) + tail (Σ_{τ=1..max_tau}) com erro por blocking.
    Garante bloco > max_tau (senão a autocorr do bloco é indefinida)."""
    G = np.asarray(growth, float)
    n = len(G)
    # ajusta n_blocks p/ que cada bloco comporte max_tau (bloco >= 2*max_tau)
    while n_blocks > 2 and n // n_blocks < 2 * max_tau:
        n_blocks -= 1
    cm_full = c_mem(G, max_tau=max_tau)
    tail_full = float(np.nansum(cm_full[1:]))
    bs = n // n_blocks
    tails = []
    for b in range(n_blocks):
        seg = G[b * bs:(b + 1) * bs]
        if len(seg) <= max_tau + 2:
            continue
        cmb = c_mem(seg, max_tau=max_tau)
        tails.append(np.nansum(cmb[1:]))
    tails = np.array(tails)
    tail_err = float(np.nanstd(tails) / np.sqrt(max(1, len(tails)))) if len(tails) else float('nan')
    return cm_full, tail_full, tail_err


def calibrate_k3(g, k0, eps, Vt, k3_0=0.8):
    stats = {}
    k3 = k3_0
    for _ in range(3):
        n3 = _avg_N3(g, k0, k3, eps, Vt, 22, stats)
        k3 = k3 + 2.0 * eps * (n3 - Vt)
    return k3


def calibrate_k3_seeded(g, gamma, kappa, k0, eps, Vt, k3_0=0.8, rounds=5):
    """Calibra k3 COM o bias da semente ATIVO (o bias infla volume; k3 compensa).
    Crucial p/ D1/D2 justos: ⟨N3⟩ casado entre cego/semente/markov."""
    k3 = k3_0
    for _ in range(rounds):
        vals = []
        for _ in range(22):
            g.seed_sweep(gamma, kappa, k0, k3, eps, Vt, n_steps=Vt)
            vals.append(g.N3)
        n3 = float(np.mean(vals[len(vals) // 2:]))
        k3 = k3 + 2.0 * eps * (n3 - Vt)
    return k3


def modulation_std(g, gamma, k0, k3, eps, Vt, n=12):
    """std do EXPOENTE do bias (γ·m_local) ao longo de n sweeps — mede a 'intensidade'."""
    vals = []
    for _ in range(n):
        g.seed_sweep(gamma, g._kappa_run, k0, k3, eps, Vt, n_steps=Vt)
        phibar = g._phibar()
        if g.mode == 'markov':
            g._coordbar = (4 * g.N3 / g.N0) if g.N0 else 1.0
        sample = []
        for f in g.spatial_set.items[:200]:
            sample.append(g._mod_local(tuple(f), phibar))
        vals.append(np.std(sample) * gamma)
    return float(np.mean(vals))


def run_mode(mode, gamma, k0, T, Vt, seed, kappa, delta, eps,
             equil, sample, sample_every, n_blocks, markov_gain=1.0):
    g = SeedCDT3D(T, seed=seed, delta=delta, mode=mode)
    g._kappa_run = kappa
    g.markov_gain = markov_gain
    rng = g.rng
    while g.N3 < Vt * 0.7:
        g.move_26(g.spatial_set.sample(rng))
    # calibra k3 COM o bias ativo, depois mantém k3 ADAPTATIVO (trava ⟨N3⟩ no alvo
    # em TODOS os modos — D1/D2 justos a volume casado; só fixa volume, não a forma).
    k3 = calibrate_k3_seeded(g, gamma, kappa, k0, eps, Vt)
    gain = 0.4 * eps
    for _ in range(equil):
        g.seed_sweep(gamma, kappa, k0, k3, eps, Vt, n_steps=Vt)
        k3 += gain * (g.N3 - Vt)
    clump, pr, n3s, growth = [], [], [], []
    for s in range(sample):
        gline = g.seed_sweep(gamma, kappa, k0, k3, eps, Vt, n_steps=Vt)
        k3 += gain * (g.N3 - Vt)
        growth.append(gline)
        if s % sample_every == 0:
            clump.append(g.slice_clumping())
            pr.append(g.phi_participation_ratio())
            n3s.append(g.N3)
    dH = np.mean([g.measure_dH(50) for _ in range(6)])
    clump = np.array(clump); pr = np.array(pr)
    cm, tail, tail_err = cmem_tail_with_error(growth, max_tau=40, n_blocks=n_blocks)
    res = {
        'mode': mode, 'gamma': gamma, 'k0': k0, 'k3': round(k3, 3),
        'N3_mean': float(np.mean(n3s)), 'N0': g.N0, 'dH': float(dH),
        'clump_mean': float(np.mean(clump)), 'clump_err': blocking_error(clump, n_blocks),
        'PRphi_mean': float(np.mean(pr)), 'PRphi_err': blocking_error(pr, n_blocks),
        'Cmem': [round(float(x), 4) for x in cm],
        'Cmem_tail': tail, 'Cmem_tail_err': tail_err,
        'manifold_ok': len(g.check_manifold()) == 0,
    }
    print(f"    [{mode:6s} γ={gamma}] dH={res['dH']:.2f} clump={res['clump_mean']:.3f}"
          f"±{res['clump_err']:.3f} Cmem_tail={tail:.2f}±{tail_err:.2f} "
          f"N3={res['N3_mean']:.0f} ok={res['manifold_ok']}", flush=True)
    return res, g


def run_point(k0, T=16, Vt=1400, gamma=2.0, kappa=0.3, delta=0.5, eps=0.0015,
              equil=120, sample=160, sample_every=3, n_blocks=10, seed=7):
    print(f"\n=== FS-3D ponto k0={k0} (fase estendida), γ={gamma} ===", flush=True)
    out = {'k0': k0, 'T': T, 'Vt': Vt, 'gamma': gamma, 'kappa': kappa, 'delta': delta}

    # 1) BLIND (γ=0) — nulo de D1
    blind, _ = run_mode('blind', 0.0, k0, T, Vt, seed, kappa, delta, eps,
                        equil, sample, sample_every, n_blocks)
    # 2) SEED (γ>0) — informação source crescimento
    sd, g_seed = run_mode('seed', gamma, k0, T, Vt, seed, kappa, delta, eps,
                          equil, sample, sample_every, n_blocks)
    # calibra a intensidade do markoviano p/ casar com a da semente
    inten_seed = modulation_std(g_seed, gamma, k0, sd['k3'], eps, Vt)
    g_mk0 = SeedCDT3D(T, seed=seed, delta=delta, mode='markov')
    g_mk0._kappa_run = kappa
    rng = g_mk0.rng
    while g_mk0.N3 < Vt * 0.7:
        g_mk0.move_26(g_mk0.spatial_set.sample(rng))
    k3m = calibrate_k3(g_mk0, k0, eps, Vt)
    inten_mk_raw = modulation_std(g_mk0, gamma, k0, k3m, eps, Vt)
    markov_gain = (inten_seed / inten_mk_raw) if inten_mk_raw > 1e-6 else 1.0
    print(f"    [calibração D2] intensidade semente={inten_seed:.3f}, "
          f"markov_raw={inten_mk_raw:.3f} → markov_gain={markov_gain:.3f}", flush=True)
    # 3) MARKOV (γ>0, sem memória, mesma intensidade) — nulo de D2
    mk, _ = run_mode('markov', gamma, k0, T, Vt, seed, kappa, delta, eps,
                     equil, sample, sample_every, n_blocks, markov_gain=markov_gain)

    # --- vereditos por ponto ---
    # D1: SEED vs BLIND (clumping move além do erro?)
    d_clump = sd['clump_mean'] - blind['clump_mean']
    e_clump = math.sqrt(sd['clump_err']**2 + blind['clump_err']**2)
    D1_sigma = d_clump / e_clump if e_clump > 0 else 0.0
    D1_pass = (abs(D1_sigma) > 3) or (abs(sd['dH'] - blind['dH']) > 0.15)
    # D2: SEED vs MARKOV — geometria difere? E Cmem_tail maior?
    d_clump2 = sd['clump_mean'] - mk['clump_mean']
    e_clump2 = math.sqrt(sd['clump_err']**2 + mk['clump_err']**2)
    D2_geom_sigma = d_clump2 / e_clump2 if e_clump2 > 0 else 0.0
    # discriminador de memória: diferença das caudas C_mem (seed − markov) em σ
    d_cmem = sd['Cmem_tail'] - mk['Cmem_tail']
    e_cmem = math.sqrt(sd.get('Cmem_tail_err', 0)**2 + mk.get('Cmem_tail_err', 0)**2)
    D2_cmem_sigma = d_cmem / e_cmem if e_cmem > 0 else 0.0
    cmem_ratio = sd['Cmem_tail'] / mk['Cmem_tail'] if mk['Cmem_tail'] not in (0, float('nan')) else float('inf')
    out.update({
        'blind': blind, 'seed': sd, 'markov': mk,
        'intensity_seed': inten_seed, 'markov_gain': markov_gain,
        'D1_clump_sigma': float(D1_sigma), 'D1_pass': bool(D1_pass),
        'D2_geom_sigma_seed_vs_markov': float(D2_geom_sigma),
        'D2_Cmem_tail_seed': sd['Cmem_tail'], 'D2_Cmem_tail_markov': mk['Cmem_tail'],
        'D2_Cmem_sigma': float(D2_cmem_sigma), 'D2_Cmem_ratio': float(cmem_ratio),
    })
    # D2: a semente SOBREVIVE se sua memória (Cmem tail) excede a markoviana > 3σ
    D2_seed_survives = (D2_cmem_sigma > 3) and (sd['Cmem_tail'] > mk['Cmem_tail'])
    out['D2_seed_survives'] = bool(D2_seed_survives)
    print(f"  >>> D1 (seed vs cega): clump {D1_sigma:+.1f}σ → {'PASSA' if D1_pass else 'NULO'}")
    print(f"  >>> D2 (seed vs markov): geom {D2_geom_sigma:+.1f}σ; Cmem_tail "
          f"seed={sd['Cmem_tail']:.2f}±{sd.get('Cmem_tail_err',0):.2f} vs "
          f"markov={mk['Cmem_tail']:.2f}±{mk.get('Cmem_tail_err',0):.2f} "
          f"({D2_cmem_sigma:+.1f}σ) → semente {'SOBREVIVE' if D2_seed_survives else 'MORRE/ambíguo'}")
    return out


if __name__ == "__main__":
    t0 = time.time()
    pts = [1.0, 3.0]
    if len(sys.argv) > 1:
        pts = [float(x) for x in sys.argv[1:]]
    results = [run_point(k0) for k0 in pts]
    p = os.path.join(os.path.dirname(__file__), "fs3d_result.json")
    with open(p, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\n[tempo total: {time.time()-t0:.0f}s]  [escrito: {p}]", flush=True)
