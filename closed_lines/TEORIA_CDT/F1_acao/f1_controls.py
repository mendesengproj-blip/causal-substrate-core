"""
f1_controls.py — validação do ESTIMADOR de d_H contra geometrias conhecidas.

Charter §3.4: gate de engenharia antes da física. Antes de confiar no d_H medido
na CDT, o estimador de Hausdorff (shelling BFS no grafo, N(r)~r^d) tem que devolver
o valor certo em grafos cuja dimensão é conhecida exatamente:
  - anel 1D (toro 1D)         -> d = 1
  - rede quadrada 2D (toro)   -> d = 2   (mesmo alvo da CDT)
  - rede cúbica 3D (toro)     -> d = 3
  - árvore binária            -> d ~ grande/indefinido (controle de patologia)

Se o estimador erra nesses, qualquer d_H da CDT é suspeito. Reusa a mesma rotina
de ajuste (janela 2..0.5*Nmax) que medindo a CDT.
"""
import numpy as np


def fit_dH_from_adj(adj, n_sources=60, seed=0, frac=0.5, rmin=2):
    """adj: lista de listas (vizinhos). Retorna (d, r, Nbar)."""
    rng = np.random.default_rng(seed)
    N = len(adj)
    srcs = rng.choice(N, size=min(n_sources, N), replace=False)
    profiles = []
    maxlen = 0
    for s in srcs:
        dist = np.full(N, -1, dtype=np.int64)
        dist[s] = 0
        frontier = [int(s)]
        counts = [1]
        d = 0
        while frontier:
            nxt = []
            for u in frontier:
                for v in adj[u]:
                    if dist[v] < 0:
                        dist[v] = d + 1
                        nxt.append(v)
            if nxt:
                counts.append(len(nxt))
            frontier = nxt
            d += 1
        cum = np.cumsum(counts)
        profiles.append(cum)
        maxlen = max(maxlen, len(cum))
    M = np.full((len(profiles), maxlen), N, dtype=np.float64)
    for k, p in enumerate(profiles):
        M[k, : len(p)] = p
    Nbar = M.mean(axis=0)
    r = np.arange(maxlen)
    mask = (r >= rmin) & (Nbar < frac * N) & (r < len(r))
    if mask.sum() < 3:
        return float('nan'), r, Nbar
    x = np.log(r[mask])
    y = np.log(Nbar[mask])
    A = np.vstack([x, np.ones_like(x)]).T
    slope, _ = np.linalg.lstsq(A, y, rcond=None)[0]
    return float(slope), r, Nbar


def ring(n):
    adj = [[(i - 1) % n, (i + 1) % n] for i in range(n)]
    return adj


def torus2d(L):
    def idx(x, y):
        return (x % L) * L + (y % L)
    adj = [[] for _ in range(L * L)]
    for x in range(L):
        for y in range(L):
            i = idx(x, y)
            adj[i] = [idx(x + 1, y), idx(x - 1, y), idx(x, y + 1), idx(x, y - 1)]
    return adj


def torus3d(L):
    def idx(x, y, z):
        return ((x % L) * L + (y % L)) * L + (z % L)
    adj = [[] for _ in range(L ** 3)]
    for x in range(L):
        for y in range(L):
            for z in range(L):
                i = idx(x, y, z)
                adj[i] = [idx(x + 1, y, z), idx(x - 1, y, z),
                          idx(x, y + 1, z), idx(x, y - 1, z),
                          idx(x, y, z + 1), idx(x, y, z - 1)]
    return adj


def binary_tree(depth):
    # árvore binária completa (controle de patologia: cresce exponencial, d->inf)
    n = 2 ** (depth + 1) - 1
    adj = [[] for _ in range(n)]
    for i in range(n):
        l, r = 2 * i + 1, 2 * i + 2
        if l < n:
            adj[i].append(l); adj[l].append(i)
        if r < n:
            adj[i].append(r); adj[r].append(i)
    return adj


if __name__ == "__main__":
    print("=== CONTROLE DO ESTIMADOR d_H ===")
    d, *_ = fit_dH_from_adj(ring(4000), seed=1)
    print(f"  anel 1D (N=4000):      d_H = {d:.3f}   (esperado 1)")
    d, *_ = fit_dH_from_adj(torus2d(64), seed=1)
    print(f"  toro 2D (64x64):       d_H = {d:.3f}   (esperado 2)")
    d, *_ = fit_dH_from_adj(torus3d(20), seed=1)
    print(f"  toro 3D (20^3):        d_H = {d:.3f}   (esperado 3)")
    d, *_ = fit_dH_from_adj(binary_tree(13), seed=1, frac=0.3)
    print(f"  árvore binária (d=13): d_H = {d:.3f}   (patologia: alto/indefinido)")
