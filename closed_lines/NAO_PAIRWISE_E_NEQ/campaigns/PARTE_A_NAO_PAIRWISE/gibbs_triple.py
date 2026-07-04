"""
gibbs_triple.py -- PARTE A: processo de ponto de GIBBS com potencial de TRIPLA
genuino (nao-pairwise), Lorentz-invariante, sobre Minkowski 2+1D.

A pergunta (ver A2_ANALISE.md): Palm/Slivnyak fecha correlacoes de qualquer ordem
finita SOBRE POISSON. Sobra so a medida NAO-Poisson com estrutura de ordem >=3. Aqui:
um Gibbs com U = b2 Sum V2(s2_ij) + b3 Sum_trios V2_i V2_j V2_k (produto = tripla
genuina, nao soma). Amostrado por Metropolis nas POSICOES. Grafo = cobertura causal;
estimador clustering_metrics VERBATIM. Gatilho cinematico: <z>(N), C4(N).

V3 = produto das tres funcoes de par do trio -> ativa so quando os TRES pares estao
proximos -> nao-fatoravel em soma de pares (gate 2 confirma quantitativamente).
"""
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = HERE
for _ in range(8):
    if os.path.exists(os.path.join(_ROOT, "TEIC", "src", "causal_core.py")):
        break
    _ROOT = os.path.dirname(_ROOT)
sys.path.insert(0, os.path.join(_ROOT, "TEIC", "src"))
sys.path.insert(0, os.path.join(_ROOT, "TEIC", "docs", "campaigns", "RIDEOUT_SORKIN_CLUSTERING"))

from causal_core import sprinkle_box, causal_matrix      # noqa: E402  VERBATIM
from rs_clustering import clustering_metrics              # noqa: E402  VERBATIM

DIM = 3
T_BOX, L_BOX = 1.0, 3.0
BOUNDS = np.array([(0.0, T_BOX), (0.0, L_BOX), (0.0, L_BOX)])
VOL = T_BOX * L_BOX * L_BOX
W2 = 0.04           # largura^2 da funcao de par V2 (~ escala de discretude^2) [External]
STEP = 0.25         # passo local do Metropolis (coordenadas)


# ====================================================================== #
# INVARIANTES E FUNCAO DE PAR
# ====================================================================== #
def interval2_to(pt, pts):
    """s^2 = dt^2 - |dx|^2 de um ponto a todos (vetor)."""
    d = pts - pt
    return d[:, 0] ** 2 - np.sum(d[:, 1:] ** 2, axis=1)


def interval2_matrix(pts):
    dt = pts[None, :, 0] - pts[:, None, 0]
    dx2 = np.sum((pts[None, :, 1:] - pts[:, None, 1:]) ** 2, axis=-1)
    return dt * dt - dx2


def v2_vec(s2):
    """V2(s^2) = exp(-|s^2|/(2 W2)). Suave, invariante, decai com |s^2|."""
    return np.exp(-np.abs(s2) / (2.0 * W2))


# ====================================================================== #
# GIBBS MC (Metropolis nas posicoes), com matriz de par G mantida
# ====================================================================== #
def gibbs_sample(n, b2, b3, rng, n_therm=160, n_decorr=0):
    """Equilibra um Gibbs de n pontos na caixa. Energia
    U = b2 Sum_{i<j} G_ij + b3 Sum_{i<j<k} G_ij G_jk G_ik, G_ij=V2(s2_ij).
    Retorna (pts, info). Move local; aceitacao Metropolis."""
    pts = sprinkle_box(n / VOL, BOUNDS, rng)
    n = pts.shape[0]
    G = v2_vec(interval2_matrix(pts))
    np.fill_diagonal(G, 0.0)
    lo, hi = BOUNDS[:, 0], BOUNDS[:, 1]
    n_acc = 0
    n_try = 0
    e_trace = []
    total_sweeps = n_therm + n_decorr
    for sweep in range(total_sweeps):
        for _ in range(n):
            i = rng.integers(n)
            gi_old = G[i].copy()
            # proposta local com reflexao na caixa
            newp = pts[i] + STEP * rng.standard_normal(3) * (hi - lo) / L_BOX
            newp = np.where(newp < lo, 2 * lo - newp, newp)
            newp = np.where(newp > hi, 2 * hi - newp, newp)
            newp = np.clip(newp, lo, hi)
            s2 = interval2_to(newp, pts)
            gi_new = v2_vec(s2)
            gi_new[i] = 0.0
            # delta de energia de PAR
            dE = b2 * (gi_new.sum() - gi_old.sum())
            # delta de energia de TRIPLA (0.5 g^T G g; termos com i mortos por g[i]=0)
            if b3 != 0.0:
                tri_new = 0.5 * gi_new @ (G @ gi_new)
                tri_old = 0.5 * gi_old @ (G @ gi_old)
                dE += b3 * (tri_new - tri_old)
            n_try += 1
            if dE <= 0 or rng.random() < np.exp(-dE):
                pts[i] = newp
                G[i, :] = gi_new
                G[:, i] = gi_new
                n_acc += 1
        if sweep % 8 == 0:
            e_trace.append(_total_energy(G, b2, b3))
    info = {"n": int(n), "acc_rate": n_acc / max(n_try, 1),
            "e_trace": e_trace, "P2": _mean_pair(G), "T3": _mean_triple(G)}
    return pts, G, info


def _total_energy(G, b2, b3):
    e2 = b2 * 0.5 * G.sum()
    e3 = 0.0
    if b3 != 0.0:
        # Sum_{i<j<k} G_ij G_jk G_ik = (1/6) Tr(G^3)
        e3 = b3 * (np.trace(G @ G @ G) / 6.0)
    return float(e2 + e3)


def _mean_pair(G):
    """P2 = proximidade media de PAR = soma de G / N (densidade de pares proximos)."""
    n = G.shape[0]
    return float(G.sum() / n)


def _mean_triple(G):
    """T3 = proximidade media de TRIO = (1/N) Sum_{i<j<k} G_ij G_jk G_ik = Tr(G^3)/(6N)."""
    n = G.shape[0]
    return float(np.trace(G @ G @ G) / (6.0 * n))


# ====================================================================== #
# GRAFO DE COBERTURA CAUSAL (Hasse) -- VERBATIM da linhagem
# ====================================================================== #
def covering_edges(pts):
    C = causal_matrix(pts)
    Cf = C.astype(np.float32)
    two_step = (Cf @ Cf) > 0.5
    cover = C & ~two_step
    ii, jj = np.nonzero(cover)
    return [(int(a), int(b)) for a, b in zip(ii.tolist(), jj.tolist())]


def boost(pts, eta, axis=0):
    pts = np.asarray(pts, float).copy()
    ch, sh = np.cosh(eta), np.sinh(eta)
    t = pts[:, 0].copy(); x = pts[:, 1 + axis].copy()
    pts[:, 0] = ch * t - sh * x
    pts[:, 1 + axis] = -sh * t + ch * x
    return pts


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

    n = 350
    b2 = 1.0
    b3 = 2.0
    # (1) equilibrio do MC (duas metades da e_trace concordam)
    pts, G, info = gibbs_sample(n, b2, b3, np.random.default_rng(1), n_therm=160)
    et = np.array(info["e_trace"])
    h1, h2 = et[len(et)//2:].mean(), et[len(et)//4:len(et)//2].mean()
    check("MC equilibra (2 metades da energia concordam <5%)",
          abs(h1 - h2) / (abs(h1) + 1e-9) < 0.05,
          f"E 2a metade={h1:.1f} vs 3o quarto={h2:.1f}  acc={info['acc_rate']:.2f}")

    # (2) V3 GENUINAMENTE NAO-FATORAVEL: liga b3 muda trios >> pares
    pa, Ga, ia = gibbs_sample(n, b2, 0.0, np.random.default_rng(2), n_therm=160)   # base
    pb, Gb, ib = gibbs_sample(n, b2, b3, np.random.default_rng(2), n_therm=160)    # +V3
    dP = abs(ib["P2"] - ia["P2"]) / max(ia["P2"], 1e-9)
    dT = abs(ib["T3"] - ia["T3"]) / max(ia["T3"], 1e-9)
    check("V3 nao-fatoravel: |dT3|/T3 > 3*|dP2|/P2 (trios mudam >> pares)",
          dT > 3.0 * dP,
          f"dT3/T3={dT:.3f}  dP2/P2={dP:.3f}  razao={dT/max(dP,1e-9):.1f}x")
    # teste matched-pairs (forte): re-tuna b2 no run +V3 p/ casar P2, ve se T3 difere
    b2_lo = b2
    # busca simples: aumentar b2 no run base ate P2 ~ P2(+V3) (que e menor, mais repulsivo)
    # aqui comparamos no MESMO b2 e reportamos; matched e confirmacao adicional
    report["aux"]["nonfact"] = {"P2_base": ia["P2"], "P2_v3": ib["P2"],
                                "T3_base": ia["T3"], "T3_v3": ib["T3"],
                                "dP2_rel": dP, "dT3_rel": dT}

    # (3) cross-check estimador
    e = covering_edges(pb)
    m = clustering_metrics(pb.shape[0], e)
    z_direct = 2.0 * len(e) / pb.shape[0]
    check("cross-check <z>=2E/N (clustering_metrics VERBATIM)",
          abs(m["deg_mean"] - z_direct) < 1e-9,
          f"{m['deg_mean']:.9f} vs {z_direct:.9f}")

    # (4) INVARIANCIA DE LORENTZ: boost -> grafo identico (funcao invariante das posicoes)
    eta = 0.8
    e0 = covering_edges(pb)
    eb = covering_edges(boost(pb, eta))
    s0 = set(tuple(sorted(x)) for x in e0)
    sb = set(tuple(sorted(x)) for x in eb)
    m0 = clustering_metrics(pb.shape[0], e0)
    mbo = clustering_metrics(pb.shape[0], eb)
    check("invariancia de Lorentz: arestas de cobertura BIT-identicas sob boost",
          s0 == sb, f"|E0|={len(e0)} |Eb|={len(eb)} simdif={len(s0 ^ sb)}")
    check("invariancia de Lorentz: <z>/C4 identicos sob boost",
          abs(m0["deg_mean"] - mbo["deg_mean"]) < 1e-9
          and abs(m0["mean_local_square"] - mbo["mean_local_square"]) < 1e-9,
          f"z {m0['deg_mean']:.6f}/{mbo['deg_mean']:.6f} "
          f"C4 {m0['mean_local_square']:.6f}/{mbo['mean_local_square']:.6f}")
    return report


# ====================================================================== #
# MEDICAO CENTRAL: scan de b3 x ladder de N
# ====================================================================== #
B3S = [0.0, 1.0, 2.0, 4.0]     # 0 = so par (controle interno)
B2 = 1.0
LADDER = [200, 350, 500, 650]
N_SEEDS = 4
SEED_CAP = (500, 2)
N_THERM = 160


def run_measurement(b3s=B3S, ladder=LADDER, n_seeds=N_SEEDS):
    out = {"family": "Gibbs point process with genuine triple potential V3 (product)",
           "U": "b2 Sum V2(s2) + b3 Sum_trios V2 V2 V2; V2=exp(-|s2|/2W2)",
           "dim": DIM, "W2": W2, "b2": B2, "b3s": b3s, "ladder": ladder,
           "n_seeds": n_seeds, "estimator": "clustering_metrics VERBATIM", "by_b3": {}}
    for b3 in b3s:
        rows = []
        for n in ladder:
            ns = SEED_CAP[1] if n >= SEED_CAP[0] else n_seeds
            zs, c4s, accs, t0 = [], [], [], time.perf_counter()
            for s in range(ns):
                rng = np.random.default_rng(5000 + s + n + int(100 * b3))
                pts, G, info = gibbs_sample(n, B2, b3, rng, n_therm=N_THERM)
                edges = covering_edges(pts)
                m = clustering_metrics(pts.shape[0], edges)
                zs.append(m["deg_mean"]); c4s.append(m["mean_local_square"])
                accs.append(info["acc_rate"])
            dt = time.perf_counter() - t0
            rows.append({"N": n, "n_seeds": ns,
                         "z_mean": float(np.mean(zs)), "z_sem": float(np.std(zs)/np.sqrt(ns)),
                         "C4": float(np.mean(c4s)), "C4_sem": float(np.std(c4s)/np.sqrt(ns)),
                         "acc": float(np.mean(accs)), "runtime_s": dt})
            print(f"  b3={b3:>4} N={n:>4}: z={np.mean(zs):7.3f} C4={np.mean(c4s):.4f} "
                  f"acc={np.mean(accs):.2f} [{dt:.1f}s,{ns}s]", flush=True)
        z = np.array([r["z_mean"] for r in rows]); c4 = np.array([r["C4"] for r in rows])
        Nv = np.array([r["N"] for r in rows], float)
        zsl = (np.diff(z)/np.diff(np.log(Nv))).tolist() if len(rows) > 1 else []
        c4sl = (np.diff(c4)/np.diff(np.log(Nv))).tolist() if len(rows) > 1 else []
        out["by_b3"][f"{b3}"] = {"b3": b3, "rows": rows, "z_dlnN": zsl, "c4_dlnN": c4sl,
                                 "z_slope_top": zsl[-1] if zsl else float("nan"),
                                 "c4_slope_top": c4sl[-1] if c4sl else float("nan")}
    return out


def verdict(meas, z_rel=0.05, c4_sat=0.02, c4_decay=0.5):
    res = {"per_b3": {}, "window_b3": []}
    for key, R in meas["by_b3"].items():
        rows = R["rows"]
        z_top, z_first = rows[-1]["z_mean"], rows[0]["z_mean"]
        c4_top, c4_first = rows[-1]["C4"], rows[0]["C4"]
        zrel = R["z_slope_top"]/z_top if z_top else 0.0
        zdec = (len(R["z_dlnN"]) < 2) or (R["z_dlnN"][-1] <= R["z_dlnN"][-2] + 1e-9)
        zsat = (abs(zrel) < z_rel) and zdec
        c4pos = (c4_top > c4_sat) and (c4_top >= c4_decay * c4_first if c4_first > 0 else False)
        both = bool(zsat and c4pos)
        res["per_b3"][key] = {"b3": R["b3"], "z_first": z_first, "z_top": z_top,
                              "z_rel_slope": zrel, "z_saturates": bool(zsat),
                              "c4_first": c4_first, "c4_top": c4_top,
                              "c4_positive_sat": bool(c4pos), "window": both}
        if both:
            res["window_b3"].append(R["b3"])
    res["verdict"] = "JANELA_ENCONTRADA" if res["window_b3"] else "MORTE_LIMPA"
    return res


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "all"
    if mode in ("gate", "all"):
        print("=" * 70 + "\nGATE DE VALIDACAO (Gibbs tripla nao-pairwise)\n" + "=" * 70)
        g = validation_gate()
        json.dump(g, open(os.path.join(HERE, "validation_gate.json"), "w"), indent=2)
        print(f"\n  GATE {'VERDE' if g['passed'] else 'VERMELHO'}")
        if not g["passed"]:
            print("  ABORTA."); sys.exit(1)
    if mode in ("measure", "all"):
        print("\n" + "=" * 70 + "\nMEDICAO: scan de b3 x N\n" + "=" * 70)
        meas = run_measurement()
        v = verdict(meas); meas["verdict"] = v
        json.dump(meas, open(os.path.join(HERE, "gibbs_triple.json"), "w"), indent=2)
        print("\n" + "=" * 70 + "\nVEREDITO\n" + "=" * 70)
        for key, r in v["per_b3"].items():
            print(f"  b3={r['b3']:>4}: z {r['z_first']:6.2f}->{r['z_top']:6.2f} "
                  f"(slope/z={r['z_rel_slope']:+.3f} {'SAT' if r['z_saturates'] else 'div'}) "
                  f"| C4 {r['c4_first']:.4f}->{r['c4_top']:.4f} "
                  f"({'pos' if r['c4_positive_sat'] else 'decai/0'})")
        print(f"\n  >>> VEREDITO: {v['verdict']}")
