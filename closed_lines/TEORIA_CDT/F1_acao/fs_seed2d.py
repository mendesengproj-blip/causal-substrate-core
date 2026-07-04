"""
fs_seed2d.py — Fase SEMENTE, sonda 2D (indicador antecipado, NÃO o teste vinculante).

Pré-registro: ../SEMENTE_PRE_REGISTRO.md (mecanismo + ADENDO FS-2D, congelados).
Estatuto: EXPLORATÓRIO. γ=0 reduz à CDT cega validada em F1 (controle). Inferência
ASSIMÉTRICA congelada: positivo dispara FS-3D; nulo é NÃO-INFORMATIVO (não mata).

Mecanismo (φ no DUAL = por triângulo):
  source:    aceitação de `add` em i ganha fator exp(γ(φ_i − φ̄))
  depósito:  ao crescer em i, triângulos novos herdam φ_i + δ; φ_i += δ (registro)
  transporte: φ ← (1−κ)φ + κ·⟨φ_vizinhos_dual⟩ por sweep; renormaliza ⟨φ⟩=1
"""
import json
import math
import os
import sys

import numpy as np

from f1_cdt2d import CDT2D, UP, DOWN
from f1_run import shelling_profile, dH_estimates, blocking_error


class SeedCDT2D(CDT2D):
    """CDT2D + campo de informação φ por triângulo, acoplado ao crescimento."""

    def __init__(self, T, ell0, seed=0, cap=None, delta=0.5):
        super().__init__(T, ell0, seed=seed, cap=cap)
        self.phi = np.ones(self.cap, dtype=np.float64)  # φ por slot, ⟨φ⟩≈1
        self.delta = delta

    def _grow(self):
        oldcap = self.cap
        super()._grow()
        newphi = np.ones(self.cap, dtype=np.float64)
        newphi[:oldcap] = self.phi
        self.phi = newphi

    def _move_slot(self, src, dst):
        super()._move_slot(src, dst)
        self.phi[dst] = self.phi[src]

    def info_sweep(self, gamma, kappa, lam, eps, Vtarget, ell_min=3,
                   n_moves=None, p_flip=0.5, accept_stats=None):
        """Sweep com `add` SOURCED por φ. γ=0 ⇒ idêntico ao sweep cego de F1."""
        if n_moves is None:
            n_moves = self.N
        rng = self.rng
        phibar = float(self.phi[:self.N].mean()) if self.N else 1.0
        for _ in range(n_moves):
            i = int(rng.integers(self.N))
            u = rng.random()
            if u < p_flip:
                if self.can_flip(i):
                    self.do_flip(i)
            elif u < p_flip + 0.5 * (1 - p_flip):
                N2 = self.N
                dS = 2 * lam + 0.5 * eps * ((N2 + 2 - Vtarget) ** 2 - (N2 - Vtarget) ** 2)
                # FATOR SEMENTE: exp(γ(φ_i − φ̄)) — clamp p/ estabilidade numérica
                bias = math.exp(max(-30.0, min(30.0, gamma * (self.phi[i] - phibar))))
                A = math.exp(-dS) * N2 / (N2 + 2) * bias
                if rng.random() < A:
                    phi_i = self.phi[i]
                    self.do_add(i)  # cria 2 slots no fim (N-2, N-1)
                    # depósito: novos triângulos herdam φ_i+δ; i recebe bump (registro)
                    self.phi[self.N - 2] = phi_i + self.delta
                    self.phi[self.N - 1] = phi_i + self.delta
                    self.phi[i] = phi_i + self.delta
            else:
                if self.can_delete(i, ell_min):
                    N2 = self.N
                    dS = -2 * lam + 0.5 * eps * ((N2 - 2 - Vtarget) ** 2 - (N2 - Vtarget) ** 2)
                    A = math.exp(-dS) * N2 / (N2 - 2)
                    if rng.random() < A:
                        self.do_delete(i)
        # transporte de φ no grafo dual + renormalização ⟨φ⟩=1
        self._transport_phi(kappa)

    def _transport_phi(self, kappa):
        N = self.N
        if N == 0:
            return
        ph = self.phi[:N]
        nb = (self.phi[self.nbL[:N]] + self.phi[self.nbR[:N]] + self.phi[self.nbC[:N]]) / 3.0
        new = (1 - kappa) * ph + kappa * nb
        m = new.mean()
        if m > 0:
            new = new / m  # renormaliza ⟨φ⟩=1 (γ controla contraste)
        self.phi[:N] = np.clip(new, 0.0, None)

    # observáveis
    def participation_ratio(self):
        ph = self.phi[:self.N]
        s1 = ph.mean()
        s2 = (ph ** 2).mean()
        return float(s1 * s1 / s2) if s2 > 0 else float('nan')

    def slice_clumping(self):
        """R = Var(ℓ_t)/⟨ℓ_t⟩²."""
        e = self.ell.astype(float)
        return float(e.var() / (e.mean() ** 2)) if e.mean() > 0 else float('nan')


def measure_dH(g, n_sources, rng):
    adj = [list(map(int, (g.nbL[i], g.nbR[i], g.nbC[i]))) for i in range(g.N)]
    r, Nbar = shelling_profile(adj, n_sources, rng)
    return dH_estimates(r, Nbar, g.N)


def run_fs2d(T=28, ell0=28, gammas=(0.0, 1.0, 2.0, 4.0), kappa=0.3, delta=0.5,
             eps=0.02, ell_min=3, equil=1500, sample=900, sample_every=3,
             n_sources=40, seed=7, n_blocks=10):
    lam = math.log(2.0)
    Vt = 2 * ell0 * T
    out = {'params': dict(T=T, ell0=ell0, gammas=list(gammas), kappa=kappa,
                          delta=delta, eps=eps, Vt=Vt, equil=equil, sample=sample)}
    rows = {}
    for gamma in gammas:
        g = SeedCDT2D(T, ell0, seed=seed, delta=delta)
        for _ in range(equil):
            g.info_sweep(gamma, kappa, lam, eps, Vt, ell_min=ell_min)
        clump, prs = [], []
        for s in range(sample):
            g.info_sweep(gamma, kappa, lam, eps, Vt, ell_min=ell_min)
            if s % sample_every == 0:
                clump.append(g.slice_clumping())
                prs.append(g.participation_ratio())
        rng = np.random.default_rng(seed + 500)
        est = measure_dH(g, n_sources, rng)
        clump = np.array(clump); prs = np.array(prs)
        rows[f'{gamma:.1f}'] = dict(
            dH_band=round(est['band'], 3), dH_extrap=round(est['extrap'], 3),
            O2_clump=round(float(clump.mean()), 4),
            O2_clump_err=round(blocking_error(clump, n_blocks), 4),
            O3_PR=round(float(prs.mean()), 4),
            O3_PR_err=round(blocking_error(prs, n_blocks), 4),
            vol=int(g.N))
        print(f"  γ={gamma:.1f}: d_H={est['band']:.3f}  O2(clump)={clump.mean():.4f}"
              f"±{blocking_error(clump,n_blocks):.4f}  O3(PR)={prs.mean():.4f}"
              f"±{blocking_error(prs,n_blocks):.4f}  vol={g.N}", flush=True)
    out['rows'] = rows

    # veredito assimétrico congelado
    g0 = rows[f'{gammas[0]:.1f}']
    gmax = rows[f'{gammas[-1]:.1f}']
    dc = abs(g0['O2_clump'] - gmax['O2_clump'])
    err = math.sqrt(g0['O2_clump_err']**2 + gmax['O2_clump_err']**2)
    clump_moves = (dc > 3 * err) and (gmax['O2_clump'] > g0['O2_clump'])
    dH_moves = abs(g0['dH_band'] - gmax['dH_band']) > 0.15
    pr_moves = abs(g0['O3_PR'] - gmax['O3_PR']) > 3 * math.sqrt(
        g0['O3_PR_err']**2 + gmax['O3_PR_err']**2)
    out['O2_clump_moves'] = bool(clump_moves)
    out['O1_dH_moves'] = bool(dH_moves)
    out['O3_PR_moves'] = bool(pr_moves)
    positive = bool(clump_moves or dH_moves or pr_moves)
    out['FS2D_INDICATOR'] = 'POSITIVO (dispara FS-3D)' if positive else \
        'NULO (NAO-INFORMATIVO, nao mata; defere a FS-3D)'
    print(f"\n  O2 clumping move? {clump_moves} | d_H move? {dH_moves} | PR move? {pr_moves}")
    print(f"  >>> FS-2D: {out['FS2D_INDICATOR']}")
    return out


if __name__ == "__main__":
    print("=== FS-2D: sonda barata da semente (γ=0 = CDT cega) ===")
    res = run_fs2d()
    p = os.path.join(os.path.dirname(__file__), "fs2d_result.json")
    with open(p, "w", encoding="utf-8") as f:
        json.dump(res, f, indent=2, ensure_ascii=False, default=str)
    print(f"[escrito: {p}]")
