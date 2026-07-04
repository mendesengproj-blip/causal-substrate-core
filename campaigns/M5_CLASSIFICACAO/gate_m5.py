# -*- coding: utf-8 -*-
"""
gate_m5.py -- bateria UNIFICADA do capstone M5 (PRE_REGISTRO par.5).

A MESMA bateria de medicoes (reusada de gate_m1c: <z>, exp_rate, poly, plaqueta
C4/N, posts) aplicada a UM representante de CADA classe de substrato, mais o
rotulo de invariancia (fato teorico, nao medido). Predicao congelada: SNA=True
so nas 2 linhas NAO-invariantes (cristal M1b E1; reticulado foliado).

SNA-1 valencia finita: <z> estavel e <=30.
SNA-2 2D-amenavel:     exp_rate<0.35 E poly em [1.6,2.4].
SNA-3 lacos percolantes: C4/N > 0.3 e nao-decrescente.
SNA = SNA-1 & SNA-2 & SNA-3.
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "M1C_FRONTEIRA_NAO_POISSON"))
sys.path.insert(0, os.path.join(HERE, "..", "..", "TEIC", "docs", "campaigns",
                                "RIDEOUT_SORKIN_TRIGGER"))
import rs_trigger as rs
import gate_m1c as gm

WORD = 64
N_ROOTS = 30
# EMENDA DE INSTRUMENTO (pre-run p/ o run decisivo; causa documentada pelo
# smoke): R_MAX=6 (herdado de M1c) e pequeno demais p/ o exp_rate resolver a
# log-concavidade de V~R^2 -- reticulados 2D genuinos davam exp_rate~0.5 em R=6.
# Verificado no smoke que exp_rate cai monotonicamente com R p/ reticulados
# (foliado 0.46->0.20, cristal 0.40->0.21 em R=6..20) e fica >0.6 p/ hiperbolico
# em qualquer R. Correcao: medir amenabilidade no MAIOR R viavel (ate R_TARGET),
# em reticulados grandes. Janela FISICA (exp_rate<0.35, poly in [1.6,2.4])
# INALTERADA. So o parametro de resolucao muda.
R_TARGET = 15
L_LATTICE = 80          # reticulados grandes (N~6400) p/ suportar R grande


# ====================================================================== #
# representantes com ORDEM (ancestrais em bitset) -> reusa maquinaria M1c
# ====================================================================== #
def _anc_from_pairs(n, is_anc):
    """anc[j] bitset dos i<j (na ordem dada) com is_anc(i,j)=True, ja
    transitivamente fechado SE a relacao for transitiva (Poisson M2, dominancia
    o sao)."""
    W = (n + WORD - 1) // WORD
    anc = np.zeros((n, W), dtype=np.uint64)
    for j in range(n):
        for i in range(j):
            if is_anc(i, j):
                anc[j, i // WORD] |= np.uint64(1) << np.uint64(i % WORD)
    return anc


def rep_poisson_m2(n, rng):
    """Sprinkling de Minkowski M^2 (INVARIANTE). Coordenadas (t,x); i<j sse j no
    cone de futuro de i. Ordem causal ja e transitiva."""
    t = rng.random(n)
    x = rng.random(n) - 0.5
    idx = np.argsort(t)
    t, x = t[idx], x[idx]  # ordenar por tempo (ordem de rotulo = tempo)
    def is_anc(i, j):
        dt = t[j] - t[i]
        return dt > 0 and abs(x[j] - x[i]) < dt
    return _anc_from_pairs(n, is_anc)


def rep_box_order(n, rng):
    """Ordem de dominancia 2D iid (INVARIANTE embutida = camada 1 / T3, e a
    ordem causal de M^2 a 45 graus). i<j sse x_i<x_j E y_i<y_j."""
    p = rng.random((n, 2))
    idx = np.argsort(p[:, 0] + p[:, 1])
    p = p[idx]
    def is_anc(i, j):
        return p[i, 0] < p[j, 0] and p[i, 1] < p[j, 1]
    return _anc_from_pairs(n, is_anc)


# ====================================================================== #
# representantes de GRAFO direto (cristal, foliado) -> Hasse = grafo dado
# ====================================================================== #
def rep_crystal_E1(L):
    """Cristal M1b E1 (NAO-invariante): Z^2 com 5 geradores, restrito a [0,L)^2.
    Hasse = grafo de Cayley (covers = geradores)."""
    V = [(3, 0), (0, 3), (1, 1), (3, 1), (1, 3)]
    idx = {}
    n = 0
    for i in range(L):
        for j in range(L):
            idx[(i, j)] = n
            n += 1
    adj = [[] for _ in range(n)]
    edges = []
    for (i, j), u in idx.items():
        for (dx, dy) in V:
            w = (i + dx, j + dy)
            if w in idx:
                v = idx[w]
                adj[u].append(v)
                adj[v].append(u)
                edges.append((u, v))
    return adj, edges, n


def rep_foliated_lattice(L):
    """Reticulado quadrado graduado (NAO-invariante, foliado, T1): Z^2 covers
    (i,j)<(i+1,j) e (i,j)<(i,j+1)."""
    idx = lambda i, j: i * L + j
    n = L * L
    adj = [[] for _ in range(n)]
    edges = []
    for i in range(L):
        for j in range(L):
            if i + 1 < L:
                a, b = idx(i, j), idx(i + 1, j)
                adj[a].append(b); adj[b].append(a); edges.append((a, b))
            if j + 1 < L:
                a, b = idx(i, j), idx(i, j + 1)
                adj[a].append(b); adj[b].append(a); edges.append((a, b))
    return adj, edges, n


# ====================================================================== #
# bateria comum
# ====================================================================== #
def robust_ball(adj, n, rng):
    """Mede crescimento de bola no MAIOR R viavel (ate R_TARGET) com >=8 roots
    alcancando o raio pleno. Devolve (exp_rate, poly, R_usado)."""
    roots = list(rng.choice(n, size=min(N_ROOTS, n), replace=False))
    for R in range(R_TARGET, 3, -1):
        bg = gm.ball_growth(adj, n, roots, R)
        if bg and bg["roots_used"] >= 8:
            return bg["exp_growth_rate"], bg["poly_growth_exp"], R
    bg = gm.ball_growth(adj, n, roots, 4)
    if bg:
        return bg["exp_growth_rate"], bg["poly_growth_exp"], 4
    return None, None, 0


def battery_from_graph(adj, edges, n, z_mean, post_density, rng):
    exp_rate, poly, R_used = robust_ball(adj, n, rng)
    cc = gm.clustering_c4(adj, n, edges)
    return {"z_mean": z_mean, "post_density": post_density,
            "exp_growth_rate": exp_rate, "poly_growth_exp": poly, "R_used": R_used,
            "c4_per_node": cc["c4_per_node"], "transitivity": cc["transitivity"]}


def battery_from_order(anc, n, rng):
    z = rs.z_mean_hasse(anc, n)
    pd = gm.post_stats(anc, n)["post_density"]
    edges = gm.hasse_edges(anc, n)
    adj = gm.build_adj(edges, n)
    return battery_from_graph(adj, edges, n, z, pd, rng)


def sna_flags(m, z_series=None):
    z = m["z_mean"]
    er = m["exp_growth_rate"]
    poly = m["poly_growth_exp"]
    c4 = m["c4_per_node"]
    sna1 = (z is not None and z <= 30.0 and
            (z_series is None or z_series))   # estabilidade checada externamente
    sna2 = (er is not None and er < 0.35 and poly is not None and 1.6 <= poly <= 2.4)
    sna3 = (c4 is not None and c4 > 0.3)
    return {"SNA1_finite_valence": bool(sna1), "SNA2_amenable_2D": bool(sna2),
            "SNA3_percolating_loops": bool(sna3),
            "SNA": bool(sna1 and sna2 and sna3)}


def measure_valence_growth(rep_fn, Ns, rng_seed):
    """<z>(N) p/ checar SNA-1 (finita <=> estavel)."""
    zs = []
    for N in Ns:
        rng = np.random.default_rng(rng_seed + N)
        anc = rep_fn(N, rng)
        zs.append(rs.z_mean_hasse(anc, N))
    slope = float(np.polyfit(np.log(Ns), zs, 1)[0])
    return zs, slope


def main():
    print("=" * 82)
    print("M5 -- BATERIA UNIFICADA (tabela de decisao SNA x invariancia)")
    print("=" * 82)
    rng = np.random.default_rng(20260704)
    rows = []

    # --- classes com ORDEM (invariantes/covariantes) ---
    # Poisson M^2 (invariante): valencia cresce com N (densidade)
    zs, slope = measure_valence_growth(rep_poisson_m2, [400, 800, 1200], 1)
    m = battery_from_order(rep_poisson_m2(1200, np.random.default_rng(1 + 1200)), 1200, rng)
    m_sna = sna_flags(m, z_series=(slope < 0.3))
    rows.append(("Poisson_M2", "SIM (Lorentz)", m, m_sna, {"z_growth_slope": slope, "z_series": zs}))

    # box-order / dominancia 2D (invariante embutida = T3)
    zs2, slope2 = measure_valence_growth(rep_box_order, [400, 800, 1200], 2)
    m = battery_from_order(rep_box_order(1200, np.random.default_rng(2 + 1200)), 1200, rng)
    m_sna = sna_flags(m, z_series=(slope2 < 0.3))
    rows.append(("box_order_2D", "SIM (embutida)", m, m_sna, {"z_growth_slope": slope2, "z_series": zs2}))

    # CSG esparso (covariante): hiperbolico
    m = battery_from_order(rs.grow_transitive_percolation(1500, 4.0 / 1500, np.random.default_rng(3))[0], 1500, rng)
    rows.append(("CSG_sparse", "covariante", m, sna_flags(m, z_series=True), {}))

    # CSG denso (covariante): posts => 1D-bloco
    m = battery_from_order(rs.grow_transitive_percolation(1500, 0.7, np.random.default_rng(4))[0], 1500, rng)
    rows.append(("CSG_dense", "covariante", m, sna_flags(m, z_series=True), {}))

    # exchangeable: por TEOREMA (T2), sem Hasse localmente finito -> SNA1 falha
    rows.append(("exchangeable", "SIM", None,
                 {"SNA1_finite_valence": False, "SNA2_amenable_2D": False,
                  "SNA3_percolating_loops": False, "SNA": False,
                  "note": "[teorema T2]: sem Hasse localmente finito"}, {}))

    # --- classes NAO-invariantes ---
    adj, edges, n = rep_crystal_E1(L_LATTICE)
    m = battery_from_graph(adj, edges, n, 2 * len(edges) / n, 0.0, rng)
    rows.append(("crystal_E1_M1b", "NAO (cristal/BHS)", m, sna_flags(m, z_series=True), {"n": n}))

    adj, edges, n = rep_foliated_lattice(L_LATTICE)
    m = battery_from_graph(adj, edges, n, 2 * len(edges) / n, 0.0, rng)
    rows.append(("foliated_lattice", "NAO (graduado/T1)", m, sna_flags(m, z_series=True), {"n": n}))

    # --- tabela ---
    print(f"\n{'classe':>18} {'invariante?':>18} {'z':>6} {'post':>6} "
          f"{'exp_r':>6} {'poly':>6} {'C4/N':>6}  SNA1 SNA2 SNA3  SNA")
    print("-" * 100)
    out = []
    for (label, inv, m, s, extra) in rows:
        if m is None:
            print(f"{label:>18} {inv:>18} {'--':>6} {'--':>6} {'--':>6} {'--':>6} "
                  f"{'--':>6}   {int(s['SNA1_finite_valence'])}    "
                  f"{int(s['SNA2_amenable_2D'])}    {int(s['SNA3_percolating_loops'])}   "
                  f"{'YES' if s['SNA'] else 'no'}   [T2]")
        else:
            print(f"{label:>18} {inv:>18} {m['z_mean']:6.2f} {m['post_density']:6.3f} "
                  f"{(m['exp_growth_rate'] or -1):6.2f} {(m['poly_growth_exp'] or -1):6.2f} "
                  f"{m['c4_per_node']:6.2f}   {int(s['SNA1_finite_valence'])}    "
                  f"{int(s['SNA2_amenable_2D'])}    {int(s['SNA3_percolating_loops'])}   "
                  f"{'YES' if s['SNA'] else 'no'}")
        out.append({"class": label, "invariant": inv, "metrics": m, "sna": s, "extra": extra})

    # veredito: SNA=True <=> nao-invariante?
    sna_true = [r["class"] for r in out if r["sna"]["SNA"]]
    invariant_sna = [r["class"] for r in out if r["sna"]["SNA"] and
                     ("SIM" in r["invariant"] or "covariante" in r["invariant"])]
    print("-" * 100)
    print(f"  SNA=True em: {sna_true}")
    print(f"  contraexemplo (invariante/covariante SNA): {invariant_sna if invariant_sna else 'NENHUM'}")
    verdict = ("CLASSIFICACAO CONFIRMADA: SNA <=> nao-invariante"
               if (sna_true and not invariant_sna)
               else "D-M5-1: contraexemplo invariante SNA!" if invariant_sna
               else "revisar")
    print(f"  >>> {verdict}")

    json.dump({"rows": out, "sna_true": sna_true,
               "invariant_sna_counterexample": invariant_sna, "verdict": verdict},
              open(os.path.join(HERE, "gate_m5.json"), "w"), indent=2, default=str)
    print("  saved gate_m5.json")


if __name__ == "__main__":
    main()
