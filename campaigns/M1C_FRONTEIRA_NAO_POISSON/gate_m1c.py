# -*- coding: utf-8 -*-
"""
gate_m1c.py -- M1c: fronteira nao-Poisson (CSG Rideout-Sorkin).

Estende rs_trigger.py (gerador de percolacao transitiva + estimador de Hasse,
byte-identicos e reusados por import) com as tres medicoes que o T4 pivota:
  - densidade de POSTS (elemento comparavel a todos)  [K3]
  - estrutura de BLOCOS entre posts                    [K4]
  - DIMENSAO do espaco de ciclos do Hasse (crescimento de bola R^d vs
    exponencial; rank de H1 em bolas)                  [K5]
  + C4/transitividade (ancora de retrodicao)           [K6]
  + <z>_Hasse (valencia)                               [K2]

Familias varridas (PRE_REGISTRO par.6):
  A  p fixo           -> valencia DIVERGE (boost-like); posts densos (T4 aplica)
  B  p = lambda/N     -> valencia FINITA (o canto: T4 nao coberto aqui)
  C  dust (lam->0)    -> antichain trivial

Anti-circularidade: so p adimensional + ordem de nascimento. Nenhuma metrica.
"""
import json
import math
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
RS = os.path.join(HERE, "..", "..", "TEIC", "docs", "campaigns",
                  "RIDEOUT_SORKIN_TRIGGER")
sys.path.insert(0, RS)

import rs_trigger as rs  # gerador + estimador de Hasse, reusados verbatim


# ====================================================================== #
# MEDICOES NOVAS
# ====================================================================== #

def post_stats(anc, n):
    """Densidade de posts + estrutura de blocos.

    k e POST <=> comparavel a todos: anc_count[k] + desc_count[k] == n-1.
    Posts particionam a ordem (soma ordinal): blocos entre posts consecutivos.
    """
    anc_count = np.array([rs._popcount(anc[j]) for j in range(n)], dtype=np.int64)
    desc_count = np.zeros(n, dtype=np.int64)
    for j in range(n):
        ks = rs._bits_to_indices(anc[j])
        if ks.size:
            desc_count[ks] += 1
    is_post = (anc_count + desc_count) == (n - 1)
    post_idx = np.nonzero(is_post)[0]
    n_post = int(post_idx.size)
    # blocos entre posts consecutivos (na ordem de nascimento, que respeita a
    # ordem linear induzida pelos posts: um post e comparavel a todos, logo os
    # posts aparecem em ordem total e cortam a ordem em intervalos)
    if n_post == 0:
        max_block = n
        mean_block = float(n)
    else:
        cuts = np.concatenate([[-1], np.sort(post_idx), [n]])
        blocks = np.diff(cuts) - 1  # elementos estritamente entre posts
        blocks = blocks[blocks > 0]
        max_block = int(blocks.max()) if blocks.size else 0
        mean_block = float(blocks.mean()) if blocks.size else 0.0
    return {"n_post": n_post, "post_density": n_post / n,
            "max_block": max_block, "max_block_frac": max_block / n,
            "mean_block": mean_block}


def hasse_edges(anc, n):
    """Lista de arestas de cobertura (i<j) do Hasse. Mesma logica de
    rs.hasse_links_count, mas coletando as arestas."""
    edges = []
    W = anc.shape[1]
    for j in range(n):
        aj = anc[j]
        ks = rs._bits_to_indices(aj)
        if ks.size == 0:
            continue
        inter = np.bitwise_or.reduce(anc[ks], axis=0)
        linkparents = aj & ~inter
        for i in rs._bits_to_indices(linkparents):
            edges.append((int(i), j))
    return edges


def build_adj(edges, n):
    adj = [[] for _ in range(n)]
    for (i, j) in edges:
        adj[i].append(j)
        adj[j].append(i)
    return adj


def cycle_rank_total(edges, n):
    """rank(H1) = E - V + (#componentes) do grafo de Hasse nao-dirigido."""
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for (i, j) in edges:
        ri, rj = find(i), find(j)
        if ri != rj:
            parent[ri] = rj
    comps = len({find(x) for x in range(n)})
    return len(edges) - n + comps, comps


def ball_growth(adj, n, roots, r_max):
    """Para cada root: |bola(R)| e rank(H1 da bola) para R=1..r_max.
    Classifica crescimento: expoente polinomial (log V vs log R) e taxa
    exponencial (log V vs R). Rank em R^d discrimina reticulado 2D (rank~R^2,
    poly) de arvore/hiperbolico (V~exp, rank per-vertex ~const)."""
    Vs = np.zeros(r_max)
    Rk = np.zeros(r_max)
    used = 0
    for root in roots:
        # BFS por camadas
        dist = {root: 0}
        frontier = [root]
        layers = [[root]]
        while frontier and len(layers) <= r_max:
            nxt = []
            for u in frontier:
                for v in adj[u]:
                    if v not in dist:
                        dist[v] = dist[u] + 1
                        nxt.append(v)
            if nxt:
                layers.append(nxt)
            frontier = nxt
        if len(layers) <= r_max:
            continue  # bola bate na borda do grafo; nao usa este root
        used += 1
        for R in range(1, r_max + 1):
            ball = [u for u in dist if dist[u] <= R]
            bset = set(ball)
            V = len(ball)
            E = 0
            for u in ball:
                for v in adj[u]:
                    if v in bset and v > u:
                        E += 1
            Vs[R - 1] += V
            Rk[R - 1] += E - V + 1  # bola conexa
    if used == 0:
        return None
    Vs /= used
    Rk /= used
    Rrange = np.arange(1, r_max + 1)
    # expoente polinomial (ajuste log-log em R>=2)
    m = Rrange >= 2
    poly_exp = float(np.polyfit(np.log(Rrange[m]), np.log(Vs[m] + 1e-9), 1)[0])
    # taxa exponencial (log V vs R linear)
    exp_rate = float(np.polyfit(Rrange[m], np.log(Vs[m] + 1e-9), 1)[0])
    # expoente do rank de ciclos (a "dimensao de laco" do PRE_REGISTRO K5)
    if np.all(Rk[m] > 0):
        cyc_exp = float(np.polyfit(np.log(Rrange[m]), np.log(Rk[m]), 1)[0])
    else:
        cyc_exp = 0.0
    return {"roots_used": used, "V_of_R": Vs.tolist(), "rank_of_R": Rk.tolist(),
            "poly_growth_exp": poly_exp, "exp_growth_rate": exp_rate,
            "cycle_dim_exp": cyc_exp}


def clustering_c4(adj, n, edges):
    """Transitividade global (triangulos) e densidade de C4 do Hasse
    nao-dirigido. Hasse NAO tem triangulos (Lema 0 de M1) => transitividade ~0
    esperada; C4 e a medida de laco relevante (ancora ~0.019)."""
    deg = np.array([len(a) for a in adj])
    # triangulos: para cada aresta conta vizinhos comuns
    tri = 0
    for (i, j) in edges:
        si = set(adj[i])
        common = si.intersection(adj[j])
        tri += len(common)
    tri //= 3
    paths2 = int(np.sum(deg * (deg - 1)) // 2)
    transitivity = (3 * tri / paths2) if paths2 else 0.0
    # C4: conta pares de vizinhos comuns por par de vertices (quadrilateros)
    # aproximacao barata: sum_v C(deg_v,2) conta caminhos de comprimento 2;
    # C4 ~ #pares de vertices com >=2 vizinhos comuns. Amostra p/ custo.
    from collections import defaultdict
    common = defaultdict(int)
    for v in range(n):
        nb = adj[v]
        L = len(nb)
        if L < 2:
            continue
        for a in range(L):
            for b in range(a + 1, L):
                x, y = nb[a], nb[b]
                if x > y:
                    x, y = y, x
                common[(x, y)] += 1
    c4 = sum(c * (c - 1) // 2 for c in common.values())
    c4_norm = c4 / n
    return {"transitivity": float(transitivity), "c4_per_node": float(c4_norm),
            "n_triangles": int(tri)}


# ====================================================================== #
# FAMILIAS E MEDICAO
# ====================================================================== #

def p_of(fam, N):
    if fam["kind"] == "fixed":
        return fam["p"]
    if fam["kind"] == "scaled":
        return fam["lam"] / N
    if fam["kind"] == "dust":
        return 0.5 / N ** 1.5  # lam-> 0: quase antichain
    raise ValueError(fam)


FAMILIES = [
    # A: regime DENSO / post (T4 aplica) -- posts densos, blocos finitos
    {"label": "A_dense_p0.70", "kind": "fixed", "p": 0.70},
    {"label": "A_dense_p0.50", "kind": "fixed", "p": 0.50},
    # knife-edge: onset de posts entre hiperbolico e confinado-por-blocos
    {"label": "K_edge_p0.40", "kind": "fixed", "p": 0.40},
    {"label": "K_edge_p0.30", "kind": "fixed", "p": 0.30},
    {"label": "M_fixed_p0.10", "kind": "fixed", "p": 0.10},   # valencia satura, sem posts
    # B: canto de valencia FINITA -- p = lambda/N
    {"label": "B_scaled_lam2.0", "kind": "scaled", "lam": 2.0},
    {"label": "B_scaled_lam4.0", "kind": "scaled", "lam": 4.0},
    {"label": "B_scaled_lam8.0", "kind": "scaled", "lam": 8.0},
    # C: dust
    {"label": "C_dust", "kind": "dust"},
]

LADDER = [500, 1000]          # medicoes pesadas (grafo/bola/C4) ate 1000
LADDER_Z = [500, 1000, 2000]  # z e posts ate 2000
N_SEEDS = 6
R_MAX = 6
N_ROOTS = 25


def measure_family(fam, seeds=N_SEEDS):
    rows = []
    for N in LADDER_Z:
        heavy = N in LADDER   # medicoes pesadas (grafo/bola) so ate 2000
        p = p_of(fam, N)
        acc = {"z": [], "post_density": [], "max_block_frac": [],
               "cycle_rank_per_n": [], "poly_exp": [], "exp_rate": [],
               "cycle_dim": [], "c4": [], "transitivity": [], "comps_per_n": []}
        t0 = time.perf_counter()
        for s in range(seeds):
            rng = np.random.default_rng(20260704 + s + 7 * N)
            anc, _ = rs.grow_transitive_percolation(N, p, rng)
            acc["z"].append(rs.z_mean_hasse(anc, N))
            ps = post_stats(anc, N)
            acc["post_density"].append(ps["post_density"])
            acc["max_block_frac"].append(ps["max_block_frac"])
            if heavy:
                edges = hasse_edges(anc, N)
                adj = build_adj(edges, N)
                rank, comps = cycle_rank_total(edges, N)
                acc["cycle_rank_per_n"].append(rank / N)
                acc["comps_per_n"].append(comps / N)
                roots = list(rng.choice(N, size=min(N_ROOTS, N), replace=False))
                bg = ball_growth(adj, N, roots, R_MAX)
                if bg:
                    acc["poly_exp"].append(bg["poly_growth_exp"])
                    acc["exp_rate"].append(bg["exp_growth_rate"])
                    acc["cycle_dim"].append(bg["cycle_dim_exp"])
                cc = clustering_c4(adj, N, edges)
                acc["c4"].append(cc["c4_per_node"])
                acc["transitivity"].append(cc["transitivity"])
        dt = time.perf_counter() - t0

        def m(key):
            return float(np.mean(acc[key])) if acc[key] else None

        row = {"N": N, "p": p, "seeds": seeds,
               "z_mean": m("z"), "post_density": m("post_density"),
               "max_block_frac": m("max_block_frac"),
               "cycle_rank_per_n": m("cycle_rank_per_n"),
               "comps_per_n": m("comps_per_n"),
               "poly_growth_exp": m("poly_exp"), "exp_growth_rate": m("exp_rate"),
               "cycle_dim_exp": m("cycle_dim"),
               "c4_per_node": m("c4"), "transitivity": m("transitivity"),
               "runtime_s": dt}
        rows.append(row)
        zc = row["z_mean"]
        er = row["exp_growth_rate"] if row["exp_growth_rate"] is not None else -1
        pe = row["poly_growth_exp"] if row["poly_growth_exp"] is not None else -1
        cr = row["cycle_rank_per_n"] if row["cycle_rank_per_n"] is not None else -1
        mb = row["max_block_frac"] if row["max_block_frac"] is not None else -1
        print(f"  {fam['label']:>18} N={N:>4} p={p:.4g}: z={zc:6.2f} "
              f"post={row['post_density']:.4f} maxblk={mb:.3f} "
              f"cyc_rank/N={cr:.3f} exp_rate={er:.2f} poly={pe:.2f} [{dt:.0f}s]")
    # tendencias
    z = np.array([r["z_mean"] for r in rows], float)
    Nv = np.array([r["N"] for r in rows], float)
    z_slope = float(np.polyfit(np.log(Nv), z, 1)[0])
    pd = np.array([r["post_density"] for r in rows], float)
    pd_slope = float(np.polyfit(np.log(Nv), pd, 1)[0])
    return {"family": fam, "rows": rows,
            "z_slope_dlnN": z_slope, "z_top": float(z[-1]),
            "post_density_slope_dlnN": pd_slope,
            "post_density_top": float(pd[-1])}


def classify(fam_result):
    """Aplica as janelas FROZEN do PRE_REGISTRO par.6.

    Requisito string-net = valencia finita (satisfeito em muitos regimes CSG) +
    laco de dimensao FINITA percolante = reticulado 2D AMENAVEL (exp_rate~0,
    crescimento poly~2) COM ciclos (rank/N > 0). DISCOVERY sse algum regime der
    isso. Fechamento por: (a) valencia divergente; (b) posts=>blocos 1D
    (confinado); (c) hiperbolico (crescimento exponencial de bola)."""
    heavy = fam_result["rows"][1]        # N=1000: medicoes pesadas
    z_growing = fam_result["z_slope_dlnN"] > 0.3     # <z> cresce com N
    z_bounded = (not z_growing) and fam_result["z_top"] <= 30.0
    posts_positive = fam_result["post_density_top"] >= 0.02
    cyc_rank = heavy["cycle_rank_per_n"]
    exp_rate = heavy["exp_growth_rate"]
    poly_exp = heavy["poly_growth_exp"]
    max_block = heavy["max_block_frac"]
    amenable_2d = (exp_rate is not None and exp_rate < 0.35 and
                   poly_exp is not None and 1.6 <= poly_exp <= 2.4)
    loops_present = (cyc_rank is not None and cyc_rank > 0.05)
    loops_2d = amenable_2d and loops_present          # o requisito string-net
    hyperbolic = exp_rate is not None and exp_rate >= 0.35
    block_confined = posts_positive and (max_block is not None and max_block < 0.1)
    # veredito por familia
    if loops_2d:
        verdict = "DISCOVERY"
    elif z_growing:
        verdict = "closed_divergent_valence"
    elif block_confined:
        verdict = "closed_posts_1D_blocks"
    elif hyperbolic:
        verdict = "closed_hyperbolic_growth"
    elif not loops_present:
        verdict = "closed_treelike_no_loops"
    else:
        verdict = "INCONCLUSIVE"
    return {"z_growing": z_growing, "z_bounded": z_bounded, "z_top": fam_result["z_top"],
            "posts_positive": posts_positive, "max_block_frac": max_block,
            "cycle_rank_per_n": cyc_rank, "exp_growth_rate": exp_rate,
            "poly_growth_exp": poly_exp, "amenable_2d": amenable_2d,
            "loops_present": loops_present, "loops_2d": loops_2d,
            "verdict": verdict}


def main():
    print("=" * 72)
    print("M1c GATE -- fronteira nao-Poisson (CSG). Validacao do gerador:")
    print("=" * 72)
    vg = rs.validation_gate(verbose=True)
    if not vg["passed"]:
        print("GERADOR NAO VALIDADO -- aborta.")
        sys.exit(1)
    print("  gerador VALIDADO (formas fechadas TP, DAG, fecho, percolacao).")

    print("\n" + "=" * 72)
    print("MEDICAO por familia de acoplamento")
    print("=" * 72)
    results = {}
    verdicts = {}
    for fam in FAMILIES:
        R = measure_family(fam)
        results[fam["label"]] = R
        verdicts[fam["label"]] = classify(R)

    print("\n" + "=" * 72)
    print("VEREDITO por familia (janelas FROZEN do PRE_REGISTRO)")
    print("=" * 72)
    any_discovery = False
    for label, v in verdicts.items():
        er = v["exp_growth_rate"] if v["exp_growth_rate"] is not None else -1
        pe = v["poly_growth_exp"] if v["poly_growth_exp"] is not None else -1
        cr = v["cycle_rank_per_n"] if v["cycle_rank_per_n"] is not None else -1
        print(f"  {label:>18}: z_top={v['z_top']:.1f} posts+={v['posts_positive']} "
              f"loops={v['loops_present']} amenable2D={v['amenable_2d']} "
              f"(exp_rate={er:.2f} poly={pe:.2f} rank/N={cr:.2f}) => {v['verdict']}")
        if v["verdict"] == "DISCOVERY":
            any_discovery = True
    overall = ("DISCOVERY -- non-Poisson escape found" if any_discovery
               else "CLOSURE-consistent -- no finite-valence + 2D-percolating corner")
    print(f"\n  >>> {overall}")

    payload = {"campaign": "M1c_FRONTEIRA_NAO_POISSON", "generator_validated": True,
               "ladder": LADDER_Z, "ladder_heavy": LADDER, "n_seeds": N_SEEDS,
               "r_max": R_MAX, "results": results, "verdicts": verdicts,
               "overall": overall}
    json.dump(payload, open(os.path.join(HERE, "gate_m1c.json"), "w"), indent=2)
    print("  saved gate_m1c.json")


if __name__ == "__main__":
    main()
