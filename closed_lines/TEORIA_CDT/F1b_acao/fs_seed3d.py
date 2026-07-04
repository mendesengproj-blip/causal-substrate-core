"""
fs_seed3d.py — Fase SEMENTE em 3D (o teste VINCULANTE D1/D2 da semente).

Pré-registro: ../SEMENTE_PRE_REGISTRO.md (mecanismo §1 + critérios D1/D2 §2, congelados).
Motor: f1b_cdt3d.py (E0-3D VERDE). Baseline: fase ESTENDIDA do CDT 3D puro (k0≈2, F1b).

A semente (charter §0.1): "a informação SOURCE o crescimento". Mecanismo (φ nos VÉRTICES):
  source (γ):    aceitação do (2,6) [inserção de vértice] ganha exp(γ(φ_local − φ̄));
                 φ_local = média de φ nos 3 vértices do triângulo. γ=0 ⇒ CDT cega (= F1b).
  depósito:      ao crescer, o vértice novo recebe φ_local+δ; os 3 vértices-fonte +δ (registro).
  transporte (κ): φ_v ← (1−κ)φ_v + κ·⟨φ vizinhos-de-aresta⟩ por sweep; renormaliza ⟨φ⟩=1.

DOIS critérios de morte empilhados (§2):
  D1 (vs CDT cega γ=0):  a GEOMETRIA com γ>0 difere de γ=0? (d_H, clumping de fatia, homogen.)
  D2 (vs regra geométrica MARKOVIANA): a diferença é reproduzível por um peso geométrico LOCAL
      sem memória (coordenação local), à MESMA intensidade? Assinatura única da semente =
      MEMÓRIA não-markoviana C_mem(τ) com cauda acima do controle.

Prior honesto (§4): passa D1 (qualquer peso muda a geometria) mas provavelmente MORRE em D2
(a memória lava no equilíbrio). Resultado é reportado como medido, sem annealing.

Sem importação de TEIC/DEV/SR.
"""
import json
import math
import os
import time
from collections import defaultdict

import numpy as np

from f1b_cdt3d import CDT3D
from f1b_phase import _avg_N3


class SeedCDT3D(CDT3D):
    """CDT3D + campo de informação φ nos vértices, acoplado ao crescimento (2,6)."""

    def __init__(self, T, seed=0, delta=0.5, mode='seed'):
        self.phi = {}          # v -> φ_v   (precisa existir antes de _build_regular)
        super().__init__(T, seed=seed)
        self.delta = delta
        self.mode = mode       # 'seed' (φ memória) | 'markov' (geométrico sem memória) | 'blind'
        self.markov_gain = 1.0 # calibrado p/ casar intensidade com a semente
        self._gamma = 0.0      # default: cego (calibração de k3 usa o sweep base)
        self._growth_by_slice = np.zeros(self.T, dtype=np.int64)
        self._coordbar = 1.0

    def _new_vertex(self, t):
        v = super()._new_vertex(t)
        self.phi[v] = 1.0
        return v

    def _del_vertex(self, v):
        super()._del_vertex(v)
        self.phi.pop(v, None)

    # --- campo de modulação local m_v (mean≈1) que entra no bias ---
    def _phibar(self):
        if not self.phi:
            return 1.0
        return sum(self.phi.values()) / len(self.phi)

    def _mod_local(self, verts, phibar):
        """Modulação local no triângulo: φ (semente) ou coordenação (markoviano)."""
        if self.mode == 'markov':
            # peso GEOMÉTRICO local, instantâneo, SEM memória: coordenação média
            c = np.mean([len(self.vert2tet[v]) for v in verts])
            return self.markov_gain * (c - self._coordbar)
        # semente: desvio de φ local em relação à média
        return np.mean([self.phi[v] for v in verts]) - phibar

    # --- (2,6) SOURCED pela informação (sobrescreve o do motor puro) ---
    def _try_26(self, k0, k3, eps, Vt, stats):
        self._bump(stats, 'try_26')
        if self.n_tri_spatial == 0:
            return '26'
        tri = self.spatial_set.sample(self.rng)
        verts = tuple(tri)
        n_st_before = self.n_tri_spatial
        phibar = self._phibar()
        dS = self._dS(+1, +4, k0, k3, eps, Vt)
        # fator semente/markoviano (γ=0 ou modo 'blind' ⇒ 1.0 ⇒ CDT cega)
        if self.mode == 'blind' or self._gamma == 0.0:
            bias = 1.0
        else:
            x = self._gamma * self._mod_local(verts, phibar)
            bias = math.exp(max(-30.0, min(30.0, x)))
        if not self.move_26(tri):
            return '26'
        q = n_st_before / self.N0
        a = q * math.exp(-dS) * bias
        if a >= 1.0 or self.rng.random() < a:
            self._bump(stats, 'acc_26')
            xv = self._next_vid - 1            # vértice recém-criado
            phi_local = float(np.mean([self.phi[v] for v in verts]))
            self.phi[xv] = phi_local + self.delta
            for v in verts:                    # registro: fontes recebem bump
                self.phi[v] = self.phi.get(v, 1.0) + self.delta
            # rastro de crescimento por fatia (p/ C_mem)
            self._growth_by_slice[self.vt[xv]] += 1
        else:
            self.move_62(self._next_vid - 1)
        return '26'

    def _transport_phi(self, kappa):
        """φ_v ← (1−κ)φ_v + κ·⟨φ vizinhos-de-aresta⟩; renormaliza ⟨φ⟩=1."""
        if kappa <= 0 or not self.phi:
            self._renorm_phi()
            return
        nb_sum = defaultdict(float)
        nb_cnt = defaultdict(int)
        for e in self.edge_set.items:
            u, w = tuple(e)
            nb_sum[u] += self.phi[w]; nb_cnt[u] += 1
            nb_sum[w] += self.phi[u]; nb_cnt[w] += 1
        for v in self.phi:
            if nb_cnt[v] > 0:
                self.phi[v] = (1 - kappa) * self.phi[v] + kappa * (nb_sum[v] / nb_cnt[v])
        self._renorm_phi()

    def _renorm_phi(self):
        if not self.phi:
            return
        m = sum(self.phi.values()) / len(self.phi)
        if m > 0:
            for v in self.phi:
                self.phi[v] = max(0.0, self.phi[v] / m)

    def seed_sweep(self, gamma, kappa, k0, k3, eps, Vt, n_steps=None):
        """Sweep com (2,6) SOURCED. Retorna o vetor de crescimento por fatia deste sweep."""
        self._gamma = gamma
        self._growth_by_slice = np.zeros(self.T, dtype=np.int64)
        if self.mode == 'markov':
            # média de coordenação p/ centrar o peso geométrico (recalculada por sweep)
            self._coordbar = (4 * self.N3 / self.N0) if self.N0 else 1.0
        if n_steps is None:
            n_steps = max(1, self.N3)
        for _ in range(n_steps):
            self.mc_step(k0, k3, eps, Vt)
        self._transport_phi(kappa)
        return self._growth_by_slice.copy()

    # --- observáveis D1 ---
    def slice_clumping(self):
        """R = Var(N31_t)/⟨N31_t⟩² (inomogeneidade do volume espacial)."""
        prof = self.spatial_volume_profile().astype(float)
        m = prof.mean()
        return float(prof.var() / (m * m)) if m > 0 else float('nan')

    def phi_participation_ratio(self):
        ph = np.array(list(self.phi.values()))
        s1 = ph.mean(); s2 = (ph * ph).mean()
        return float(s1 * s1 / s2) if s2 > 0 else float('nan')


def blocking_error(x, n_blocks=10):
    x = np.asarray(x, float)
    x = x[np.isfinite(x)]
    if len(x) < n_blocks:
        return float(np.std(x) / max(1, np.sqrt(len(x))))
    bs = len(x) // n_blocks
    means = [x[i * bs:(i + 1) * bs].mean() for i in range(n_blocks)]
    return float(np.std(means) / np.sqrt(n_blocks))


def c_mem(growth_series, max_tau=40):
    """C_mem(τ) = autocorrelação temporal do padrão de crescimento por fatia (mean≈0).
    Markoviano ⇒ cai rápido; semente (memória) ⇒ cauda. Normalizado a C_mem(0)=1."""
    G = np.asarray(growth_series, float)           # [n_sweeps, T]
    G = G - G.mean(axis=0, keepdims=True)           # remove média por fatia
    n = G.shape[0]
    c0 = (G * G).sum() / n
    if c0 <= 0:
        return np.full(max_tau + 1, np.nan)
    out = []
    for tau in range(max_tau + 1):
        if tau >= n:
            out.append(np.nan); continue
        c = (G[tau:] * G[:n - tau]).sum() / (n - tau)
        out.append(c / c0)
    return np.array(out)
