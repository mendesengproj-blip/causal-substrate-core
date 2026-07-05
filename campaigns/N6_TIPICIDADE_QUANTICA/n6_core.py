# -*- coding: utf-8 -*-
"""
n6_core.py -- motor da campanha N6 TIPICIDADE QUANTICA (PRE_REGISTRO.md).

Espaco amostral: 2D-orders de N elementos = par de permutacoes (u,v);
  e_i < e_j  sse  u_i<u_j E v_i<v_j   (intersecao de 2 ordens lineares; A1).
Peso: e^{-beta S_2D(eps)} (continuacao analitica declarada).

ACAO (conferida NA FONTE, review Glaser arXiv:2306.09904 eqs. 13-14):
  S_2D(eps) = 4 eps ( N - 2 eps * sum_{pares relacionados} f2(n, eps) )
  f2(n,eps) = (1-eps)^n [ 1 - 2 eps n/(1-eps) + eps^2 n(n-1)/(2(1-eps)^2) ]
  n = cardinalidade do intervalo Alexandrov EXCLUSIVO do par (n_mat = R@R).

MOVE (publicado): coordinate-flip -- sorteia 2 elementos e UMA coordenada
(u ou v), troca. Metropolis em e^{-beta dS} com recomputo INTEGRAL de S
(N<=120: matmul e barato; sem ddS incremental = sem bug de bookkeeping).
Sweep = N moves propostos.

Observaveis por config: S, ordering fraction, altura (cadeia mais longa),
valencia de Hasse <z> (covers = R & n==0), densidade de posts, C4/N e
transitividade do Hasse (reusa gate_m1c.clustering_c4).
"""
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "M1C_FRONTEIRA_NAO_POISSON"))
sys.path.insert(0, os.path.join(HERE, "..", "..", "TEIC", "docs", "campaigns",
                                "RIDEOUT_SORKIN_TRIGGER"))
import gate_m1c as gm  # clustering_c4, build_adj (bateria M1c/M5, reusada)


# ---------------------------------------------------------------- estado/ordem
def relation_matrix(u, v):
    """R[i,j] = 1 sse i<j na 2D-order (u_i<u_j e v_i<v_j)."""
    return ((u[:, None] < u[None, :]) & (v[:, None] < v[None, :]))


def f2(n, eps):
    """Funcao de smearing BD-2D (eq. 14 do review; n>=0 inteiro)."""
    n = n.astype(np.float64)
    om = 1.0 - eps
    return np.exp(n * np.log(om)) * (1.0 - 2.0 * eps * n / om
                                     + eps * eps * n * (n - 1.0) / (2.0 * om * om))


def action(R, eps):
    """S_2D(eps) = 4 eps (N - 2 eps sum_rel f2(n_ij, eps)); n_ij=(R@R)_ij."""
    N = R.shape[0]
    Rf = R.astype(np.float32)
    nmat = Rf @ Rf
    ns = nmat[R]
    return float(4.0 * eps * (N - 2.0 * eps * np.sum(f2(ns, eps))))


# ---------------------------------------------------------------- MCMC
class TwoOrderMCMC:
    def __init__(self, N, eps, beta, rng, init="random"):
        self.N, self.eps, self.beta, self.rng = N, eps, beta, rng
        self.u = np.arange(N)
        if init == "random":
            self.v = rng.permutation(N)
        elif init == "layered3":
            # 3 blocos: dentro do bloco v DECRESCE (antichain); blocos crescentes
            # em v (toda relacao entre blocos) => altura 3, cristalino-like.
            B = N // 3
            parts, lo = [], 0
            for b in range(3):
                hi = N if b == 2 else lo + B
                parts.append(np.arange(hi - 1, lo - 1, -1))
                lo = hi
            self.v = np.concatenate(parts)
        else:
            raise ValueError(init)
        self.R = relation_matrix(self.u, self.v)
        self.S = action(self.R, eps)

    def sweep(self):
        """N moves coordinate-flip; retorna taxa de aceitacao."""
        acc = 0
        for _ in range(self.N):
            i, j = self.rng.integers(0, self.N, 2)
            if i == j:
                continue
            coord = self.u if self.rng.random() < 0.5 else self.v
            coord[i], coord[j] = coord[j], coord[i]
            Rp = relation_matrix(self.u, self.v)
            Sp = action(Rp, self.eps)
            dS = Sp - self.S
            if dS <= 0 or self.rng.random() < np.exp(-min(self.beta * dS, 50.0)):
                self.R, self.S = Rp, Sp
                acc += 1
            else:
                coord[i], coord[j] = coord[j], coord[i]   # desfaz
        return acc / self.N


# ---------------------------------------------------------------- observaveis
def height(R):
    """Cadeia mais longa (nº de elementos). DP em ordem topologica de u."""
    N = R.shape[0]
    order = np.argsort(np.arange(N))          # u=0..N-1 pode ter sido trocado:
    # ordem topologica correta = ordenar por u (relacao exige u crescer)
    return _height_topo(R)


def _height_topo(R):
    N = R.shape[0]
    indeg_sorted = np.argsort(R.sum(axis=0))  # fallback topologico
    # topological order: qualquer extensao linear; usar ordenacao por (nº de
    # ancestrais) funciona p/ DAG transitivo (ancestrais crescem ao longo de <)
    anc = R.sum(axis=0)
    order = np.argsort(anc, kind="stable")
    L = np.ones(N, dtype=np.int64)
    for idx in order:
        preds = np.nonzero(R[:, idx])[0]
        if preds.size:
            L[idx] = 1 + L[preds].max()
    return int(L.max())


def observables(R, eps, S=None):
    N = R.shape[0]
    Rf = R.astype(np.float32)
    nmat = Rf @ Rf
    covers = R & (nmat < 0.5)
    n_cov = int(covers.sum())
    z = 2.0 * n_cov / N
    nrel = int(R.sum())
    of = nrel / (N * (N - 1) / 2.0)
    anc = R.sum(axis=0)
    desc = R.sum(axis=1)
    posts = int(np.sum(anc + desc == N - 1))
    # C4/N e transitividade do Hasse (bateria M5)
    ii, jj = np.nonzero(covers)
    edges = list(zip(ii.tolist(), jj.tolist()))
    adj = gm.build_adj(edges, N)
    cc = gm.clustering_c4(adj, N, edges)
    return {"S": float(S if S is not None else action(R, eps)),
            "of": of, "height": _height_topo(R), "z_hasse": z,
            "posts": posts, "post_density": posts / N,
            "c4_per_node": cc["c4_per_node"],
            "transitivity": cc["transitivity"], "n_covers": n_cov}


def run_point(N, eps, beta, seed, init, n_therm, n_meas, meas_every):
    """Um ponto MCMC; medias sobre n_meas configs + tau_int da serie de S."""
    rng = np.random.default_rng(seed)
    mc = TwoOrderMCMC(N, eps, beta, rng, init=init)
    for _ in range(n_therm):
        mc.sweep()
    obs_list, S_series = [], []
    acc = 0.0
    for m in range(n_meas):
        for _ in range(meas_every):
            acc += mc.sweep()
        obs_list.append(observables(mc.R, eps, S=mc.S))
        S_series.append(mc.S)
    # tau_int (Sokal window, reusa rs_trigger via gate_m1c? implementa local)
    x = np.asarray(S_series, float)
    tau = 0.5
    if x.size >= 8 and np.std(x) > 0:
        xc = x - x.mean()
        var = float(np.dot(xc, xc) / x.size)
        for t in range(1, x.size // 2):
            rho = float(np.dot(xc[:-t], xc[t:]) / ((x.size - t) * var))
            if rho <= 0:
                break
            tau += rho
    keys = ["S", "of", "height", "z_hasse", "post_density", "c4_per_node",
            "transitivity"]
    out = {k: float(np.mean([o[k] for o in obs_list])) for k in keys}
    out.update({"N": N, "eps": eps, "beta": beta, "seed": seed, "init": init,
                "tau_int_S": float(tau), "ess": float(len(S_series) / (2 * tau)),
                "acc_rate": acc / max(n_meas * meas_every, 1)})
    return out


if __name__ == "__main__":
    # smoke: acao e fases a N=30
    rng = np.random.default_rng(0)
    N, eps = 30, 0.21
    for init in ("random", "layered3"):
        mc = TwoOrderMCMC(N, eps, 0.0, rng, init=init)
        o = observables(mc.R, eps, S=mc.S)
        print(f"{init:>9}: S={o['S']:+8.2f} of={o['of']:.3f} h={o['height']} "
              f"z={o['z_hasse']:.1f} posts={o['posts']} C4/N={o['c4_per_node']:.2f}")
