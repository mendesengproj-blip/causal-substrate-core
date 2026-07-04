"""
repulsion_trigger.py -- 3a FAMILIA AUTONOMA: processo de ponto com REPULSAO
Lorentz-invariante sobre o espaco de Minkowski.

Gatilho cinematico barato (so <z> e C4), na MESMA linhagem dos Gatilhos 1-3
(RIDEOUT_SORKIN_*, CDT_VIABILIDADE) e da percolacao de longo alcance. NAO roda
ferromagneto, NAO mede xi.

A pergunta (ver ../../README.md): o teorema parcial de IMPOSSIBILIDADE_PARCIAL
prova <z> divergente para QUALQUER regra de par invariante de Lorentz *sobre um
sprinkling de Poisson*. A hipotese crucial e a INDEPENDENCIA dos eventos (medida
de Poisson). Esta campanha relaxa essa hipotese: os eventos sao correlacionados
NEGATIVAMENTE (repulsao) de forma invariante de Lorentz EM MEDIA. Campbell-Mecke
nao se aplica diretamente; a divergencia de <z> deixa de estar garantida.

SUBSTRATO:
  * sprinkling de Poisson de CANDIDATOS .... causal_core.sprinkle_box  (VERBATIM)
  * ordem causal .......................... causal_core.causal_matrix  (VERBATIM)
  * estimador <z>, C4 ..................... rs_clustering.clustering_metrics (VERBATIM)

A UNICA novidade: o processo de ponto. Em vez de Poisson puro, aplica-se um
afinamento (thinning) repulsivo tipo MATERN II sobre o intervalo invariante
s^2_ij = dt^2 - |dx|^2 (a UNICA quantidade Lorentz-invariante de um par de
eventos). Dois eventos retidos nunca ficam a |s^2| < r0^2 um do outro -> correlacao
de par NEGATIVA (g(dtau) -> 0 em curto alcance), invariante de Lorentz por
construcao (|s^2| e invariante; as marcas sao chaveadas por IDENTIDADE de no).

O parametro de repulsao alpha = r0 / dtau0 (dtau0 = rho_cand^(-1/d), escala de
discretude [External]). alpha=0 => sem exclusao => Poisson puro (a baseline
mean-field conhecida, embutida como controle). alpha cresce => repulsao mais forte.

Escolha do MATERN II (hard-core) em vez do DPP determinantal completo: sancionada
pelo charter (Secao 2.1) como aproximacao aceitavel. Captura a mesma fenomenologia
-- correlacao de par negativa, densidade marginal uniforme -- a custo O(N^2) (sem
eigendecomposicao, sem risco de PSD do kernel de Minkowski indefinido), no mesmo
perfil de custo do resto da linhagem. O DPP idealizado tem a MESMA assinatura
g(dtau)<1; o que o gatilho testa (escapar das barreiras cinematicas) nao depende
do hard-core vs soft-core, so da existencia da repulsao -- validada no gate 2.3.

GRAFO: relacao de cobertura causal (Hasse) -- a "rede do substrato" canonica,
mesmo observavel do controle de Poisson da RS-CLUSTERING -- aplicada ao conjunto
de eventos RETIDO.
"""
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))

# --- localizar a raiz que contem TEIC/src e importar os modulos VERBATIM ---
_ROOT = HERE
for _ in range(8):
    if os.path.exists(os.path.join(_ROOT, "TEIC", "src", "causal_core.py")):
        break
    _ROOT = os.path.dirname(_ROOT)
sys.path.insert(0, os.path.join(_ROOT, "TEIC", "src"))
sys.path.insert(0, os.path.join(_ROOT, "TEIC", "docs", "campaigns", "RIDEOUT_SORKIN_CLUSTERING"))

from causal_core import sprinkle_box, causal_matrix          # noqa: E402  VERBATIM
from rs_clustering import clustering_metrics                  # noqa: E402  VERBATIM

DIM = 3            # 2+1D Minkowski (t,x,y) -- IDENTICO a percolacao de longo alcance
T_BOX = 1.0
L_BOX = 3.0
BOUNDS = [(0.0, T_BOX), (0.0, L_BOX), (0.0, L_BOX)]
VOL = T_BOX * L_BOX * L_BOX


# ====================================================================== #
# INTERVALO INVARIANTE de par (a unica quantidade Lorentz-invariante)
# ====================================================================== #
def invariant_interval2(pts):
    """s^2_ij = dt^2 - |dx|^2 (assinatura +---). Invariante de Lorentz e de
    translacao. Matriz NxN simetrica."""
    pts = np.asarray(pts, float)
    dt = pts[None, :, 0] - pts[:, None, 0]
    dx2 = np.sum((pts[None, :, 1:] - pts[:, None, 1:]) ** 2, axis=-1)
    return dt * dt - dx2


# ====================================================================== #
# PROCESSO DE PONTO REPULSIVO -- afinamento MATERN II no intervalo invariante
# ====================================================================== #
def matern_thin(pts, r0, marks):
    """Retem o subconjunto MATERN-II: um candidato i e retido sse e o de MENOR
    marca entre todos os candidatos dentro da regiao de exclusao invariante
    {j : |s^2_ij| < r0^2}. Retorna mascara booleana de retidos.

    A regiao de exclusao e uma banda invariante ao redor do cone de luz; as
    marcas sao chaveadas por IDENTIDADE de candidato -> conjunto retido invariante
    de Lorentz por construcao. Dois retidos nunca ficam a |s^2| < r0^2 (hard-core
    invariante => g(dtau)=0 para dtau<r0)."""
    s2 = invariant_interval2(pts)
    n = pts.shape[0]
    close = np.abs(s2) < (r0 * r0)
    np.fill_diagonal(close, False)
    # marca minima entre vizinhos de exclusao (inf se nao houver vizinho)
    neigh_mark = np.where(close, marks[None, :], np.inf)
    min_neigh = neigh_mark.min(axis=1)
    keep = marks < min_neigh                       # i e o mais cedo na sua vizinhanca
    return keep


# ====================================================================== #
# GRAFO DE COBERTURA CAUSAL (Hasse) -- reducao transitiva, nao-direcionada
# ====================================================================== #
def covering_edges(pts):
    """Arestas de cobertura (Hasse) nao-direcionadas: i cobre j sse i<j (causal) e
    nao existe k com i<k<j. Reducao transitiva da ordem causal (causal_matrix
    VERBATIM), identica ao controle de Poisson da RS-CLUSTERING."""
    C = causal_matrix(pts)                          # C[i,j] = i precede j
    Cf = C.astype(np.float32)
    two_step = (Cf @ Cf) > 0.5                      # existe k: i<k<j
    cover = C & ~two_step
    ii, jj = np.nonzero(cover)
    return [(int(a), int(b)) for a, b in zip(ii.tolist(), jj.tolist())]


# ====================================================================== #
# CORRELACAO DE PAR g(dtau) -- prova de que ha repulsao (gate 2.3)
# ====================================================================== #
def pair_correlation(pts, dtau0, nbins=12, taumax_mult=4.0):
    """g(dtau) = rho2(dtau)/rho^2 estimada sobre os pares TIMELIKE dos eventos
    RETIDOS, normalizada por um sprinkling de Poisson da MESMA densidade e caixa
    (controle nao-correlacionado). g<1 em curto alcance = repulsao."""
    n = pts.shape[0]
    rho = n / VOL
    s2 = invariant_interval2(pts)
    tl = np.triu(s2 > 0, k=1)                       # pares timelike (i<j arbitrario)
    tau = np.sqrt(np.maximum(s2, 0.0))
    taus = tau[tl]
    taumax = taumax_mult * dtau0
    edges = np.linspace(0.0, taumax, nbins + 1)
    obs, _ = np.histogram(taus, bins=edges)
    # controle de Poisson nao-correlacionado, mesma densidade/caixa, varias seeds
    ref = np.zeros(nbins)
    nrep = 6
    for s in range(nrep):
        rngp = np.random.default_rng(50_000 + s)
        pp = sprinkle_box(rho, BOUNDS, rngp)
        s2p = invariant_interval2(pp)
        tlp = np.triu(s2p > 0, k=1)
        taup = np.sqrt(np.maximum(s2p, 0.0))[tlp]
        hp, _ = np.histogram(taup, bins=edges)
        ref += hp
    ref /= nrep
    with np.errstate(divide="ignore", invalid="ignore"):
        g = np.where(ref > 0, obs / ref, np.nan)
    centers = 0.5 * (edges[:-1] + edges[1:])
    return centers.tolist(), g.tolist(), {"n_retained": int(n),
                                          "dtau0": float(dtau0), "taumax": float(taumax)}


# ====================================================================== #
# BOOST (so para o gate de invariancia -- NUNCA no gerador de fisica)
# ====================================================================== #
def boost(pts, eta, axis=0):
    """Boost de Lorentz de rapidez eta no eixo espacial `axis` (0->x)."""
    pts = np.asarray(pts, float).copy()
    ch, sh = np.cosh(eta), np.sinh(eta)
    t = pts[:, 0].copy()
    x = pts[:, 1 + axis].copy()
    pts[:, 0] = ch * t - sh * x
    pts[:, 1 + axis] = -sh * t + ch * x
    return pts


# ====================================================================== #
# CONSTRUCAO DE UMA REALIZACAO REPULSIVA
# ====================================================================== #
def dtau0_for(rho):
    """Escala de discretude [External]: rho^(-1/d)."""
    return rho ** (-1.0 / DIM)


def repulsive_realization(rho_cand, alpha, rng):
    """Gera candidatos Poisson em densidade rho_cand, afina por Matern II com
    r0 = alpha*dtau0(rho_cand), retorna (pts_retidos, marks_de_retidos, info)."""
    pts = sprinkle_box(rho_cand, BOUNDS, rng)
    n_cand = pts.shape[0]
    marks = rng.random(n_cand)                      # chaveadas por identidade
    dtau0 = dtau0_for(rho_cand)
    r0 = alpha * dtau0
    if alpha <= 0.0:
        keep = np.ones(n_cand, bool)                # Poisson puro (baseline)
    else:
        keep = matern_thin(pts, r0, marks)
    info = {"n_cand": int(n_cand), "n_retained": int(keep.sum()),
            "p_retained": float(keep.sum() / max(n_cand, 1)),
            "dtau0_cand": float(dtau0), "r0": float(r0)}
    return pts[keep], marks[keep], info


# ====================================================================== #
# CALIBRACAO p_ret(alpha): a regiao de exclusao invariante e uma BANDA ao redor
# do cone de luz, de volume V_excl ~ r0^2 * L (NAO ~ r0^d) -- a nao-compacidade
# do cone. Logo rho_cand*V_excl cresce com a densidade e p_ret(alpha,rho) NAO e
# density-independent: e preciso estimar p_ret na densidade-alvo de candidatos.
# ====================================================================== #
def calibrate_pret(alpha, n_cand_cal=3000, n_seeds=3):
    """p_ret estimado na densidade de candidatos n_cand_cal (probe). Usado SO para
    escolher quantos candidatos gerar p/ atingir um N RETIDO alvo; o N retido real
    e medido e reportado (N_mean), entao a estimativa nao precisa ser exata."""
    if alpha <= 0.0:
        return 1.0
    rho = n_cand_cal / VOL
    ps = []
    for s in range(n_seeds):
        rng = np.random.default_rng(70_000 + s + int(1000 * alpha))
        _, _, info = repulsive_realization(rho, alpha, rng)
        ps.append(info["p_retained"])
    return float(np.mean(ps))


# ====================================================================== #
# GATE DE VALIDACAO
# ====================================================================== #
def validation_gate(verbose=True):
    report = {"checks": [], "passed": True, "aux": {}}

    def check(name, ok, detail):
        report["checks"].append({"name": name, "ok": bool(ok), "detail": detail})
        if not ok:
            report["passed"] = False
        if verbose:
            print(f"  [{'OK' if ok else 'FAIL'}] {name}: {detail}")

    alpha_test = 0.3                      # regime de repulsao bem-definido (p_ret~0.3)
    n_cand = 4500
    rho_cand = n_cand / VOL
    rng = np.random.default_rng(7)
    pts, marks, info = repulsive_realization(rho_cand, alpha_test, rng)
    n = pts.shape[0]
    pret = info["p_retained"]

    # (1) o afinamento de fato retem menos que os candidatos (ha repulsao estrutural)
    check("Matern II afina (p_ret < 1, repulsao ativa)",
          0.05 < info["p_retained"] < 0.99,
          f"p_ret(alpha={alpha_test})={info['p_retained']:.3f}  "
          f"n_cand={info['n_cand']} -> n_ret={info['n_retained']}")

    # (2) HARD-CORE invariante: nenhum par retido com |s^2| < r0^2
    s2 = invariant_interval2(pts)
    np.fill_diagonal(s2, np.inf)
    min_abs_s2 = float(np.min(np.abs(s2)))
    r0 = info["r0"]
    check("hard-core invariante: nenhum par retido com |s^2| < r0^2",
          min_abs_s2 >= r0 * r0 - 1e-9,
          f"min|s^2|_retido={min_abs_s2:.5f}  r0^2={r0*r0:.5f}")

    # (3) REPULSAO real: g(dtau) < 1 em curto alcance, -> 1 em longo (gate 2.3)
    rho_ret = n / VOL
    centers, g, ginfo = pair_correlation(pts, dtau0_for(rho_ret))
    g_arr = np.array(g, float)
    short = np.nanmean(g_arr[:2]) if g_arr.size >= 2 else np.nan
    longr = np.nanmean(g_arr[-3:])
    check("g(dtau)<1 em curto alcance (repulsao, nao Poisson)",
          (not np.isnan(short)) and short < 0.8,
          f"g_curto={short:.3f}  g_longo={longr:.3f}")
    check("g(dtau)->1 em longo alcance (independencia assintotica)",
          (not np.isnan(longr)) and 0.7 < longr < 1.4,
          f"g_longo={longr:.3f}")
    report["aux"]["g_curve"] = {"centers": centers, "g": g, **ginfo}

    # (4) cross-check do estimador VERBATIM: <z> = 2E/N do grafo de cobertura
    edges = covering_edges(pts)
    m = clustering_metrics(n, edges)
    z_direct = 2.0 * len(edges) / n
    check("cross-check <z> = 2E/N (clustering_metrics VERBATIM)",
          abs(m["deg_mean"] - z_direct) < 1e-9,
          f"clustering_metrics={m['deg_mean']:.9f} vs 2E/N={z_direct:.9f}")

    # (5) INVARIANCIA DE LORENTZ: boost eta=0.8 -> MESMO conjunto retido e MESMO grafo
    eta = 0.8
    rng2 = np.random.default_rng(123)
    pts0 = sprinkle_box(rho_cand, BOUNDS, rng2)
    marks0 = rng2.random(pts0.shape[0])
    r0c = alpha_test * dtau0_for(rho_cand)
    keep0 = matern_thin(pts0, r0c, marks0)
    keepb = matern_thin(boost(pts0, eta), r0c, marks0)
    keep_identical = bool(np.array_equal(keep0, keepb))
    e0 = covering_edges(pts0[keep0])
    eb = covering_edges(boost(pts0, eta)[keepb])
    set0 = set(tuple(sorted(e)) for e in e0)
    setb = set(tuple(sorted(e)) for e in eb)
    edges_identical = (set0 == setb)
    m0 = clustering_metrics(int(keep0.sum()), e0)
    mb = clustering_metrics(int(keepb.sum()), eb)
    check("invariancia de Lorentz: conjunto RETIDO identico sob boost",
          keep_identical,
          f"n_ret {int(keep0.sum())}/{int(keepb.sum())} iguais={keep_identical}")
    check("invariancia de Lorentz: arestas de cobertura BIT-identicas sob boost",
          edges_identical,
          f"|E0|={len(e0)} |Eb|={len(eb)} simdif={len(set0 ^ setb)}")
    check("invariancia de Lorentz: <z> e C4 identicos sob boost",
          abs(m0["deg_mean"] - mb["deg_mean"]) < 1e-9
          and abs(m0["mean_local_square"] - mb["mean_local_square"]) < 1e-9,
          f"z {m0['deg_mean']:.6f}/{mb['deg_mean']:.6f} "
          f"C4 {m0['mean_local_square']:.6f}/{mb['mean_local_square']:.6f}")

    report["aux"].update({"alpha_test": alpha_test, "p_ret": pret,
                          "z_test": m["deg_mean"], "c4_test": m["mean_local_square"],
                          "N_test": n})
    return report


# ====================================================================== #
# MEDICAO CENTRAL: scan de alpha x ladder de N
# ====================================================================== #
ALPHAS = [0.0, 0.1, 0.2, 0.3]   # 0 = Poisson puro (baseline). alpha>0.3 torna a
# exclusao invariante (banda do cone) NAO-LOCAL demais: p_ret colapsa (<0.1) e a
# densidade retida atinge teto -> regime degenerado (registrado no SYNTHESIS como
# achado: repulsao Lorentz-invariante e estruturalmente nao-local).
RET_LADDER = [400, 800, 1500, 2500]   # alvo de N RETIDO (a fisica e o N retido)
NCAND_CAP = 6500                       # teto de candidatos (memoria do s^2 NxN)
N_SEEDS = 5
SEED_CAP = (1500, 3)           # topo: menos seeds (custo do square-clustering)


def run_measurement(alphas=ALPHAS, ret_ladder=RET_LADDER, n_seeds=N_SEEDS):
    out = {"family": "Lorentz-invariant repulsive point process (Matern II in s^2)",
           "rule": "retain Matern-II w/ exclusion |s^2_ij|<r0^2, r0=alpha*dtau0(cand); "
                   "graph = causal covering (Hasse)",
           "dim": DIM, "T_box": T_BOX, "L_box": L_BOX, "alphas": alphas,
           "ret_ladder": ret_ladder, "ncand_cap": NCAND_CAP,
           "n_seeds": n_seeds, "estimator": "rs_clustering.clustering_metrics VERBATIM",
           "p_ret_probe": {}, "by_alpha": {}}
    for alpha in alphas:
        out["p_ret_probe"][f"{alpha}"] = calibrate_pret(alpha)
    print("  p_ret_probe(alpha) @ncand=3000:",
          {k: round(v, 3) for k, v in out["p_ret_probe"].items()})

    for alpha in alphas:
        rows = []
        pret = out["p_ret_probe"][f"{alpha}"]
        for n_ret_target in ret_ladder:
            # quantos candidatos p/ reter ~n_ret_target (p_ret aprox.; N retido real medido)
            n_cand = min(int(round(n_ret_target / max(pret, 1e-3))), NCAND_CAP)
            ns = SEED_CAP[1] if n_ret_target >= SEED_CAP[0] else n_seeds
            rho_cand = n_cand / VOL
            zs, c4s, ctris, nret, fr, t0 = [], [], [], [], [], time.perf_counter()
            for s in range(ns):
                rng = np.random.default_rng(10_000 + s + n_ret_target + int(1000 * alpha))
                pts, _, info = repulsive_realization(rho_cand, alpha, rng)
                n = pts.shape[0]
                edges = covering_edges(pts)
                m = clustering_metrics(n, edges)
                zs.append(m["deg_mean"]); c4s.append(m["mean_local_square"])
                ctris.append(m["transitivity"]); nret.append(n); fr.append(info["p_retained"])
            dt = time.perf_counter() - t0
            rows.append({"N_target": n_ret_target, "N_mean": float(np.mean(nret)),
                         "n_cand": n_cand, "p_ret": float(np.mean(fr)), "n_seeds": ns,
                         "z_mean": float(np.mean(zs)), "z_sem": float(np.std(zs) / np.sqrt(ns)),
                         "C4": float(np.mean(c4s)), "C4_sem": float(np.std(c4s) / np.sqrt(ns)),
                         "C_trans": float(np.mean(ctris)), "runtime_s": dt})
            print(f"  alpha={alpha:>4}  ret~{n_ret_target:>4} (got={np.mean(nret):.0f}, "
                  f"ncand={n_cand}, p_ret={np.mean(fr):.2f}): "
                  f"z={np.mean(zs):7.3f} C4={np.mean(c4s):.4f} [{dt:.1f}s, {ns}s]")
        z = np.array([r["z_mean"] for r in rows])
        c4 = np.array([r["C4"] for r in rows])
        Nv = np.array([r["N_mean"] for r in rows], float)
        z_slope = (np.diff(z) / np.diff(np.log(Nv))).tolist() if len(rows) > 1 else []
        c4_slope = (np.diff(c4) / np.diff(np.log(Nv))).tolist() if len(rows) > 1 else []
        out["by_alpha"][f"{alpha}"] = {
            "alpha": alpha, "rows": rows,
            "z_dlnN": z_slope, "c4_dlnN": c4_slope,
            "z_slope_top": z_slope[-1] if z_slope else float("nan"),
            "c4_slope_top": c4_slope[-1] if c4_slope else float("nan")}
    return out


# ====================================================================== #
# VEREDITO (criterios congelados no PRE_REGISTRO Secao 2.5)
# ====================================================================== #
def verdict(meas, z_rel_thresh=0.05, c4_sat_thresh=0.02, c4_decay_ratio=0.5):
    res = {"per_alpha": {}, "window_alphas": [],
           "z_saturates_alphas": [], "c4_positive_alphas": []}
    for key, R in meas["by_alpha"].items():
        rows = R["rows"]
        z_top = rows[-1]["z_mean"]; z_first = rows[0]["z_mean"]
        c4_top = rows[-1]["C4"]; c4_first = rows[0]["C4"]
        z_slope = R["z_slope_top"]; c4_slope = R["c4_slope_top"]
        z_rel = (z_slope / z_top) if z_top else 0.0
        z_dec = (len(R["z_dlnN"]) < 2) or (R["z_dlnN"][-1] <= R["z_dlnN"][-2] + 1e-9)
        z_sat = (abs(z_rel) < z_rel_thresh) and z_dec
        c4_nondecay = (c4_top >= c4_decay_ratio * c4_first) if c4_first > 0 else False
        c4_pos = (c4_top > c4_sat_thresh) and c4_nondecay
        both = bool(z_sat and c4_pos)
        res["per_alpha"][key] = {
            "alpha": R["alpha"], "z_first": z_first, "z_top": z_top,
            "z_slope_top": z_slope, "z_rel_slope": z_rel, "z_saturates": bool(z_sat),
            "c4_first": c4_first, "c4_top": c4_top, "c4_slope_top": c4_slope,
            "c4_positive_sat": bool(c4_pos), "window": both}
        if z_sat:
            res["z_saturates_alphas"].append(R["alpha"])
        if c4_pos:
            res["c4_positive_alphas"].append(R["alpha"])
        if both:
            res["window_alphas"].append(R["alpha"])
    res["verdict"] = "GATILHO_ARMADO" if res["window_alphas"] else "MORTE_LIMPA"
    return res


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "all"
    if mode in ("gate", "all"):
        print("=" * 70 + "\nGATE DE VALIDACAO (repulsao Lorentz-invariante)\n" + "=" * 70)
        g = validation_gate()
        json.dump(g, open(os.path.join(HERE, "validation_gate.json"), "w"), indent=2)
        print(f"\n  GATE {'VERDE' if g['passed'] else 'VERMELHO'}")
        if not g["passed"]:
            print("  ABORTA: sem leitura fisica sem gate verde.")
            sys.exit(1)
    if mode in ("measure", "all"):
        print("\n" + "=" * 70 + "\nMEDICAO CENTRAL: scan de alpha x N\n" + "=" * 70)
        meas = run_measurement()
        v = verdict(meas)
        meas["verdict"] = v
        json.dump(meas, open(os.path.join(HERE, "repulsion.json"), "w"), indent=2)
        print("\n" + "=" * 70 + "\nVEREDITO\n" + "=" * 70)
        for key, r in v["per_alpha"].items():
            tag = "JANELA" if r["window"] else (
                "z-sat" if r["z_saturates"] else ("C4>0" if r["c4_positive_sat"] else "--"))
            print(f"  alpha={r['alpha']:>4}: z {r['z_first']:7.2f}->{r['z_top']:7.2f} "
                  f"(slope/z={r['z_rel_slope']:+.3f} {'SAT' if r['z_saturates'] else 'div'}) "
                  f"| C4 {r['c4_first']:.4f}->{r['c4_top']:.4f} "
                  f"({'pos' if r['c4_positive_sat'] else 'decai/0'}) [{tag}]")
        print(f"\n  z satura em alpha = {v['z_saturates_alphas']}")
        print(f"  C4>0     em alpha = {v['c4_positive_alphas']}")
        print(f"  JANELA   em alpha = {v['window_alphas']}")
        print(f"\n  >>> VEREDITO: {v['verdict']}")
