# -*- coding: utf-8 -*-
"""
harden_m1c.py -- endurecimento dos 2 sketches do RESULTADO do M1c.

SKETCH 1 (esparso => localmente arvore) vira TEOREMA:
  Lema A: todo elo de cobertura (aresta de Hasse) da percolacao transitiva e
          uma aresta DIRETAMENTE sorteada do grafo gerador. (cobertura => sem
          intermediario => nao vem de caminho >=2 => aresta direta.)
  => Hasse e SUBGRAFO do grafo ER G(N, lambda/N).
  Lema B: subgrafo de G(N,c/N) tem, p/ cada k fixo, <= (#k-ciclos de G) = O(1)
          k-ciclos => densidade de ciclos -> 0 => localmente arvore => NAO e
          reticulado 2D-amenavel (que tem Theta(N) plaquetas).

Certificados finitos aqui:
  (A) Lema A: em todo regime, TODA aresta de Hasse esta no grafo direto. [0 violacoes]
  (B) densidade de 4-ciclos (plaquetas) do Hasse esparso -> 0, vs grade 2D = const.
  (C) discharge do T1 p/ TP: sweep fino de p mostra que NENHUM p da
      simultaneamente (posts~0) E (densidade de plaqueta Theta(1)) E (amenavel)
      -- os dois pilares (Lema A+B esparso; T4+Bollobas-Brightwell denso) cobrem
      o eixo inteiro, sem precisar do argumento T1 p/ a subfamilia TP.
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "..", "TEIC", "docs", "campaigns",
                                "RIDEOUT_SORKIN_TRIGGER"))
import rs_trigger as rs
import gate_m1c as g

WORD = 64


def grow_with_direct(n, p, rng):
    """Como grow_transitive_percolation, mas TAMBEM devolve o conjunto de
    arestas DIRETAS (i->j sorteadas). O fecho e identico (mesma ordem de
    consumo do RNG)."""
    W = (n + WORD - 1) // WORD
    anc = np.zeros((n, W), dtype=np.uint64)
    word_of = np.arange(n) // WORD
    mask_of = (np.uint64(1) << (np.arange(n) % WORD).astype(np.uint64))
    direct = set()
    for j in range(1, n):
        draws = rng.random(j) < p
        parents = np.nonzero(draws)[0]
        if parents.size == 0:
            continue
        for i in parents:
            direct.add((int(i), j))
        acc = np.bitwise_or.reduce(anc[parents], axis=0)
        pw = word_of[parents]
        pm = mask_of[parents]
        np.bitwise_or.at(acc, pw, pm)
        anc[j] = acc
    return anc, direct


def certify_lemma_A(regimes, seeds=6):
    """(A) Toda aresta de Hasse e uma aresta direta. 0 violacoes esperado."""
    out = []
    for (label, N, p) in regimes:
        viol = 0
        n_hasse = 0
        for s in range(seeds):
            rng = np.random.default_rng(20260704 + s + N)
            anc, direct = grow_with_direct(N, p, rng)
            edges = g.hasse_edges(anc, N)
            n_hasse += len(edges)
            for (i, j) in edges:
                if (i, j) not in direct:
                    viol += 1
        out.append({"regime": label, "N": N, "p": p, "seeds": seeds,
                    "hasse_edges": n_hasse, "violations": viol,
                    "subset_holds": viol == 0})
        print(f"  Lema A {label:>14} N={N} p={p:.4g}: "
              f"{n_hasse} arestas de Hasse, {viol} fora do grafo direto "
              f"=> {'SUBGRAFO OK' if viol == 0 else 'FALHA'}")
    return out


def grid2d_adj(L):
    """Grade 2D LxL (reticulado amenavel de referencia): Theta(N) plaquetas."""
    idx = lambda i, j: i * L + j
    n = L * L
    adj = [[] for _ in range(n)]
    for i in range(L):
        for j in range(L):
            if i + 1 < L:
                a, b = idx(i, j), idx(i + 1, j)
                adj[a].append(b); adj[b].append(a)
            if j + 1 < L:
                a, b = idx(i, j), idx(i, j + 1)
                adj[a].append(b); adj[b].append(a)
    return adj, n


def plaquette_density_vs_N():
    """(B) densidade de 4-ciclos: esparso CSG (->0) vs grade 2D (const)."""
    print("\n(B) densidade de 4-ciclos (plaquetas) por vertice:")
    rows = []
    # CSG esparso (valencia finita) lam=4
    for N in [500, 1000, 2000, 4000]:
        c4s = []
        for s in range(6):
            rng = np.random.default_rng(20260704 + s + N)
            anc, _ = rs.grow_transitive_percolation(N, 4.0 / N, rng)
            edges = g.hasse_edges(anc, N)
            adj = g.build_adj(edges, N)
            c4s.append(g.clustering_c4(adj, N, edges)["c4_per_node"])
        rows.append({"kind": "CSG_sparse_lam4", "N": N, "c4_per_node": float(np.mean(c4s))})
        print(f"    CSG esparso lam=4  N={N:>4}: C4/N = {np.mean(c4s):.4f}")
    # grade 2D de referencia
    for L in [22, 32, 45, 63]:
        adj, n = grid2d_adj(L)
        edges = [(u, v) for u in range(n) for v in adj[u] if v > u]
        c4 = g.clustering_c4(adj, n, edges)["c4_per_node"]
        rows.append({"kind": "grid2D", "N": n, "c4_per_node": float(c4)})
        print(f"    grade 2D L={L}     N={n:>4}: C4/N = {c4:.4f}")
    return rows


def discharge_T1_sweep():
    """(C) sweep fino de p: nenhum p da (posts~0) E (C4-dens alta) E (amenavel).
    Os dois pilares cobrem o eixo. Reporta (p, post_dens, c4_per_node, exp_rate)."""
    print("\n(C) sweep fino do eixo p (N=1500): posts vs plaqueta vs crescimento")
    rows = []
    N = 1500
    for p in [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50, 0.70, 0.90]:
        pds, c4s, ers = [], [], []
        for s in range(4):
            rng = np.random.default_rng(20260704 + s + int(1000 * p))
            anc, _ = rs.grow_transitive_percolation(N, p, rng)
            pds.append(g.post_stats(anc, N)["post_density"])
            edges = g.hasse_edges(anc, N)
            adj = g.build_adj(edges, N)
            c4s.append(g.clustering_c4(adj, N, edges)["c4_per_node"])
            roots = list(rng.choice(N, size=25, replace=False))
            bg = g.ball_growth(adj, N, roots, 6)
            ers.append(bg["exp_growth_rate"] if bg else float("nan"))
        pd, c4, er = np.mean(pds), np.mean(c4s), np.nanmean(ers)
        # "2D-amenavel" = posts~0 E crescimento sub-exponencial E plaquetas densas
        amen = (pd < 0.01) and (er < 0.35) and (c4 > 0.5)
        rows.append({"p": p, "post_density": float(pd), "c4_per_node": float(c4),
                     "exp_growth_rate": float(er), "is_2D_amenable": bool(amen)})
        print(f"    p={p:.2f}: posts={pd:.4f} C4/N={c4:.3f} exp_rate={er:.2f} "
              f"amenavel2D={amen}")
    any_amen = any(r["is_2D_amenable"] for r in rows)
    print(f"  => algum p 2D-amenavel? {any_amen}  "
          f"({'FALHA' if any_amen else 'NENHUM -- eixo coberto pelos 2 pilares'})")
    return rows, any_amen


def main():
    print("=" * 72)
    print("M1c HARDENING -- Lema A (certificado) + discharge do T1 (TP)")
    print("=" * 72)
    print("\n(A) Lema A: Hasse subset grafo direto (0 violacoes esperado)")
    regimes = [("dense_p0.7", 800, 0.7), ("mid_p0.2", 800, 0.2),
               ("sparse_lam4", 1000, 4.0 / 1000), ("sparse_lam2", 1000, 2.0 / 1000)]
    lemA = certify_lemma_A(regimes)
    A_ok = all(r["subset_holds"] for r in lemA)

    plaq = plaquette_density_vs_N()
    sweep, any_amen = discharge_T1_sweep()

    payload = {"lemma_A_certificate": lemA, "lemma_A_holds": A_ok,
               "plaquette_density": plaq,
               "T1_discharge_sweep": sweep, "any_2D_amenable": any_amen}
    json.dump(payload, open(os.path.join(HERE, "harden_m1c.json"), "w"), indent=2)

    print("\n" + "=" * 72)
    print(f"  Lema A (Hasse subgrafo do gerador): "
          f"{'CERTIFICADO' if A_ok else 'FALHOU'}")
    print(f"  T1 discharge (nenhum p 2D-amenavel no eixo TP): "
          f"{'OK' if not any_amen else 'FALHOU'}")
    print("  saved harden_m1c.json")


if __name__ == "__main__":
    main()
