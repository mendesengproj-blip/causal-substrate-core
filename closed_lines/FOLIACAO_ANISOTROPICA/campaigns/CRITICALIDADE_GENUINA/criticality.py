"""
criticality.py -- ferromagneto O(3) da TEIC sobre o substrato FOLIADO vs CONTROLE de
reticulado puro. Decide: Horava-Lifshitz discreto com FISICA NOVA (classe de
universalidade distinta do reticulado) ou apenas Ising/Heisenberg empilhado conhecido?

#### ESTE SUBSTRATO NAO E MAIS LORENTZ-INVARIANTE MANIFESTO. ####
(Foliacao preferida + distancia intra-fatia; ver ../../README.md e ../GATILHO_FOLIADO/.)

Reuso VERBATIM: orientation_core (O3Model, Graph), xi_suite (measure_point, locate_Jc,
build_lattice_3d = CONTROLE positivo). A unica novidade e build_foliated_fss (o
substrato foliado em modo FSS: densidade fixa, tamanho linear m crescente -> N~m^3,
diretamente comparavel ao reticulado m x m x m).

Funil (PRE_REGISTRO): controle primeiro -> foliado em lam=0.75 fixo -> comparacao.
Varredura de lam SO se a comparacao em lam fixo mostrar classe distinta. NAO roda aqui
o que nao foi autorizado.
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
sys.path.insert(0, os.path.join(_ROOT, "TEIC", "docs", "campaigns", "ESCALA_XI"))
sys.path.insert(0, os.path.join(_ROOT, "TEIC", "results", "vacuum_structure", "orientation"))

from xi_suite import measure_point, locate_Jc, build_lattice_3d   # noqa: E402  VERBATIM
from orientation_core import Graph                                 # noqa: E402  VERBATIM

K_INTRA = 6.0      # grau-alvo intra-fatia (= do gatilho GATILHO_FOLIADO)


# ====================================================================== #
# SUBSTRATO FOLIADO em modo FSS (densidade fixa, tamanho linear m crescente)
# ====================================================================== #
def build_foliated_fss(m, lam, rng, rho_s=1.0):
    """(Graph, xs) do substrato foliado: T=m fatias 2D de lado m (densidade rho_s
    fixa -> r_s fixo -> estrutura local fixa, tamanho linear m). N ~ m^3, comparavel
    ao reticulado m^3. xs=(t,x,y) p/ o structure factor; L_s=m.

    NAO Lorentz-invariante: conexao = distancia espacial sobre a foliacao."""
    T = m
    r_s = np.sqrt(K_INTRA / (np.pi * rho_s))
    r_t = lam * r_s
    slices, offs, off = [], [], 0
    for t in range(T):
        n_t = rng.poisson(rho_s * m * m)
        pts = rng.uniform(0.0, m, size=(n_t, 2))
        slices.append(pts); offs.append(off); off += n_t
    N = off
    edges, rs2 = [], r_s * r_s
    for t in range(T):
        p = slices[t]; nt = p.shape[0]
        if nt < 2:
            continue
        d2 = np.sum((p[:, None, :] - p[None, :, :]) ** 2, axis=-1)
        iu = np.triu_indices(nt, 1); mask = d2[iu] < rs2
        edges += list(zip((iu[0][mask] + offs[t]).tolist(), (iu[1][mask] + offs[t]).tolist()))
    if lam > 0:
        rt2 = r_t * r_t
        for t in range(T):
            tn = (t + 1) % T
            p0, p1 = slices[t], slices[tn]
            if p0.shape[0] == 0 or p1.shape[0] == 0:
                continue
            d2 = np.sum((p0[:, None, :] - p1[None, :, :]) ** 2, axis=-1)
            ii, jj = np.nonzero(d2 < rt2)
            edges += list(zip((ii + offs[t]).tolist(), (jj + offs[tn]).tolist()))
    e = np.array(edges, dtype=np.int64) if edges else np.zeros((0, 2), np.int64)
    g = Graph(N, e)
    g.n_links = int(g.edges.shape[0])
    xs = np.zeros((N, 3))
    for t in range(T):
        s = slices[t]
        xs[offs[t]:offs[t] + s.shape[0], 0] = t
        xs[offs[t]:offs[t] + s.shape[0], 1:] = s
    return g, xs


# ====================================================================== #
# Suite de criticalidade sobre um construtor de substrato
# ====================================================================== #
def run_substrate(name, builder, ms, Js, n_seeds, cfg):
    """builder(m, seed) -> (Graph, xs). Para cada m: J-scan (measure_point VERBATIM),
    localiza J_c (pico de chi), registra chi_max, U4(J), xi/L(J), drift de J_c."""
    sizes = []
    for m in ms:
        graphs = [builder(m, s) for s in range(n_seeds)]
        N_mean = float(np.mean([g.n for g, _ in graphs]))
        z_mean = float(np.mean([g.degree.mean() for g, _ in graphs]))
        rows = [measure_point(graphs, J, L_s=float(m), **cfg) for J in Js]
        Jc = locate_Jc(rows)
        chi_max = max(r["chi"] for r in rows)
        # m no maior J (fase ordenada) p/ confirmar LRO
        m_ord = rows[-1]["m"]
        sizes.append({"m": m, "L_s": float(m), "N_mean": N_mean, "z_mean": z_mean,
                      "Jc": Jc, "chi_max": chi_max, "m_ordered": m_ord, "rows": rows})
        print(f"  [{name}] m={m:2d} N={N_mean:6.0f} z={z_mean:5.2f}  Jc={Jc:.3f} "
              f"chi_max={chi_max:6.2f}  m(ord)={m_ord:.3f}", flush=True)
    return sizes


def fit_exponent(sizes):
    """chi_max ~ N^x: ajuste log-log + jackknife leave-one-size-out p/ a incerteza."""
    N = np.array([s["N_mean"] for s in sizes], float)
    chi = np.array([s["chi_max"] for s in sizes], float)
    lx, ly = np.log(N), np.log(chi)
    x_full = np.polyfit(lx, ly, 1)[0]
    jack = []
    for i in range(len(N)):
        keep = np.arange(len(N)) != i
        jack.append(np.polyfit(lx[keep], ly[keep], 1)[0])
    jack = np.array(jack)
    x_err = float(np.sqrt((len(jack) - 1) / len(jack) * np.sum((jack - jack.mean()) ** 2)))
    return float(x_full), x_err


def jc_drift(sizes):
    """Tendencia de J_c com N: <0 (deriva p/ baixo) = assinatura MF/sem ponto-fixo."""
    N = np.array([s["N_mean"] for s in sizes], float)
    Jc = np.array([s["Jc"] for s in sizes], float)
    return float(np.polyfit(np.log(N), Jc, 1)[0])


def u4_crossing(sizes, Js):
    """U4(J) por tamanho; retorna a tabela p/ inspecao de cruzamento (RG-invariante)."""
    tab = {}
    for s in sizes:
        tab[s["m"]] = {r["J"]: r["U4"] for r in s["rows"]}
    return tab


# ====================================================================== #
# Configuracao (PRE_REGISTRO)
# ====================================================================== #
MS = [6, 8, 10, 12]
N_SEEDS = 8         # 8 (vs 4): combate o ruido do chi_max (trap noise-limited da linhagem)
CFG = dict(n_burn=400, n_meas=80, meas_every=2)

JS_LATTICE = [0.55, 0.62, 0.66, 0.69, 0.72, 0.78, 0.90]    # O(3) cubico, J_c~0.69
JS_FOLIATED = [0.18, 0.22, 0.25, 0.27, 0.29, 0.32, 0.38]   # foliado lam=0.75, J_c~0.27
LAM_FIXED = 0.75


def main():
    t0 = time.time()
    out = {"note": "NAO Lorentz-invariante (Horava-Lifshitz discreto)",
           "ms": MS, "n_seeds": N_SEEDS, "cfg": CFG, "lam_fixed": LAM_FIXED}

    print("=" * 72)
    print("2.1 CONTROLE: reticulado cubico 3D puro (anchor)  [build_lattice_3d VERBATIM]")
    print("=" * 72)
    ctrl = run_substrate("lattice", lambda m, s: build_lattice_3d(m),
                         MS, JS_LATTICE, N_SEEDS, CFG)
    out["control_lattice"] = {"Js": JS_LATTICE, "sizes": ctrl}

    print("\n" + "=" * 72)
    print(f"2.2 FOLIADO em lam={LAM_FIXED} fixo  [NAO Lorentz-invariante]")
    print("=" * 72)
    fol = run_substrate(f"foliated(lam={LAM_FIXED})",
                        lambda m, s: build_foliated_fss(m, LAM_FIXED, np.random.default_rng(s)),
                        MS, JS_FOLIATED, N_SEEDS, CFG)
    out["foliated_lam075"] = {"Js": JS_FOLIATED, "lam": LAM_FIXED, "sizes": fol}

    # ---- 2.3 comparacao decisiva ----
    xc, xce = fit_exponent(ctrl)
    xf, xfe = fit_exponent(fol)
    dc, df = jc_drift(ctrl), jc_drift(fol)
    lro_ctrl = ctrl[-1]["m_ordered"] > 0.3
    lro_fol = fol[-1]["m_ordered"] > 0.3
    # criterio de distincao: expoentes diferem fora de 2 sigma combinados?
    dx = abs(xc - xf)
    sig = np.sqrt(xce ** 2 + xfe ** 2)
    distinct = dx > 2.0 * sig and sig > 0
    out["comparison"] = {
        "chi_exp_control": xc, "chi_exp_control_err": xce,
        "chi_exp_foliated": xf, "chi_exp_foliated_err": xfe,
        "exp_diff": dx, "combined_sigma": float(sig), "diff_over_sigma": float(dx / sig) if sig else None,
        "Jc_drift_control": dc, "Jc_drift_foliated": df,
        "LRO_control": bool(lro_ctrl), "LRO_foliated": bool(lro_fol),
        "u4_control": u4_crossing(ctrl, JS_LATTICE),
        "u4_foliated": u4_crossing(fol, JS_FOLIATED),
        "classes_distinct_2sigma": bool(distinct)}

    # ---- veredito ----
    # MF se expoente foliado <= ~0.5 e/ou J_c deriva forte p/ baixo e xi/L sem pico
    foliated_mf = xf < 0.5 and df < -0.02
    if not lro_fol:
        verdict = "SEM_LRO (ferromagneto nao ordena -- gate falha)"
    elif foliated_mf:
        verdict = "MEAN-FIELD (replica as 7 familias; xi sem classe nao-MF)"
    elif distinct:
        verdict = ("HORAVA-LIFSHITZ DISCRETO COM FISICA NOVA "
                   "(classe DISTINTA do reticulado, fora de 2sigma)")
    else:
        verdict = ("CRITICALIDADE DE RETICULADO CONHECIDA "
                   "(classe INDISTINGUIVEL do reticulado puro; nao e assinatura nova)")
    out["verdict"] = verdict
    out["runtime_s"] = time.time() - t0

    json.dump(out, open(os.path.join(HERE, "criticality.json"), "w"), indent=2)
    print("\n" + "=" * 72 + "\n2.3 COMPARACAO DECISIVA\n" + "=" * 72)
    print(f"  chi_max ~ N^x :  controle x={xc:.3f}±{xce:.3f}   "
          f"foliado x={xf:.3f}±{xfe:.3f}")
    print(f"  |dx|={dx:.3f}  sigma_comb={sig:.3f}  dx/sigma={dx/sig if sig else float('nan'):.2f}")
    print(f"  J_c drift:  controle {dc:+.4f}   foliado {df:+.4f}")
    print(f"  LRO:  controle={lro_ctrl}  foliado={lro_fol}")
    print(f"  classes distintas (2sigma)?  {distinct}")
    print(f"\n  >>> VEREDITO: {verdict}")
    print(f"  [{out['runtime_s']:.0f}s]")
    return out


if __name__ == "__main__":
    main()
