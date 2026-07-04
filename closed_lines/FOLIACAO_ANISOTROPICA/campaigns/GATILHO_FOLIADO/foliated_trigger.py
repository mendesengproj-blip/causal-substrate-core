"""
foliated_trigger.py -- substrato FOLIADO ANISOTROPICO (Horava-Lifshitz discreto).

#### ESTE SUBSTRATO NAO E MAIS LORENTZ-INVARIANTE MANIFESTO. ####
Adota uma foliacao preferida e distancia INTRA-FATIA (grupo SO(2) compacto). E a unica
saida estrutural da estrutura binaria das 7 mortes (SINTESE_SETE_MORTES/RESULTADO.md),
ao custo de trocar a premissa do programa (quebra Lorentz; recuperada so no IR, em tese).

Pilha de T fatias 2D (tempo periodico). Intra-fatia: |dx|<r_s (grau fixo k_intra).
Inter-fatia adjacente: |dx_proj|<r_t=lam*r_s (lam = parametro de Lifshitz). Estimador
clustering_metrics VERBATIM. Gatilho cinematico: <z>(N), C4(N) vs lam. NAO roda
ferromagneto nem xi.
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
sys.path.insert(0, os.path.join(_ROOT, "TEIC", "docs", "campaigns", "RIDEOUT_SORKIN_CLUSTERING"))
from rs_clustering import clustering_metrics              # noqa: E402  VERBATIM

L = 4.0            # lado da fatia espacial 2D [External]
K_INTRA = 6.0      # grau-alvo intra-fatia (numero esperado de vizinhos espaciais)
T_SLICES = 8       # numero de fatias (tempo), periodico S^1


def r_s_for(n_slice):
    """raio intra-fatia p/ grau medio = K_INTRA: pi r_s^2 rho = K_INTRA."""
    rho = n_slice / (L * L)
    return np.sqrt(K_INTRA / (np.pi * rho))


def build_foliated(n_slice, T, lam, rng, return_slices=False):
    """Constroi a pilha foliada. Retorna (n_total, edges) ou tambem as fatias.

    Pontos: id global; slice[t] = array (n_t, 2) de posicoes espaciais.
    Intra-fatia: |dx|<r_s. Inter-fatia (t,t+1 mod T): |dx|<r_t=lam*r_s."""
    r_s = r_s_for(n_slice)
    r_t = lam * r_s
    slices = []
    offsets = []
    off = 0
    for t in range(T):
        n_t = rng.poisson(n_slice)
        pts = rng.uniform(0.0, L, size=(n_t, 2))
        slices.append(pts)
        offsets.append(off)
        off += n_t
    n_total = off
    edges = []
    # intra-fatia
    rs2 = r_s * r_s
    for t in range(T):
        pts = slices[t]
        nt = pts.shape[0]
        if nt < 2:
            continue
        d2 = np.sum((pts[:, None, :] - pts[None, :, :]) ** 2, axis=-1)
        iu = np.triu_indices(nt, k=1)
        mask = d2[iu] < rs2
        a = (iu[0][mask] + offsets[t]).tolist()
        b = (iu[1][mask] + offsets[t]).tolist()
        edges.extend(zip(a, b))
    # inter-fatia (adjacente, periodico)
    if lam > 0.0:
        rt2 = r_t * r_t
        for t in range(T):
            tn = (t + 1) % T
            if tn == t:
                continue
            p0, p1 = slices[t], slices[tn]
            if p0.shape[0] == 0 or p1.shape[0] == 0:
                continue
            d2 = np.sum((p0[:, None, :] - p1[None, :, :]) ** 2, axis=-1)
            ii, jj = np.nonzero(d2 < rt2)
            a = (ii + offsets[t]).tolist()
            b = (jj + offsets[tn]).tolist()
            edges.extend(zip(a, b))
    edges = [(int(u), int(v)) for u, v in edges]
    if return_slices:
        return n_total, edges, slices, offsets, (r_s, r_t)
    return n_total, edges


def time_percolates(n_total, edges, slices, offsets, T):
    """Componente gigante atravessa as T fatias? (gate 3, anti-reclassificacao)."""
    # rotulo de fatia por id global
    slice_of = np.empty(n_total, dtype=int)
    for t in range(T):
        n_t = slices[t].shape[0]
        slice_of[offsets[t]:offsets[t] + n_t] = t
    # union-find
    parent = list(range(n_total))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for u, v in edges:
        ru, rv = find(u), find(v)
        if ru != rv:
            parent[ru] = rv
    comp = {}
    for i in range(n_total):
        comp.setdefault(find(i), []).append(i)
    if not comp:
        return False, 0
    giant = max(comp.values(), key=len)
    n_slices_spanned = len(set(slice_of[i] for i in giant))
    return n_slices_spanned == T, n_slices_spanned


def boost_refoliate(slices, offsets, T, eta):
    """Demonstra frame-dependencia: trata o indice de fatia como tempo, aplica boost
    (t,x)->(t',x'), re-folheia por arredondamento de t' ao inteiro mod T, e devolve
    novas fatias. (gate 2: mostrar que o grafo MUDA -> nao e Lorentz-invariante.)"""
    ch, sh = np.cosh(eta), np.sinh(eta)
    new_slabs = {t: [] for t in range(T)}
    for t in range(T):
        pts = slices[t]
        if pts.shape[0] == 0:
            continue
        tt = float(t) * np.ones(pts.shape[0])
        x = pts[:, 0]
        tp = ch * tt - sh * x                    # tempo boosteado
        xp = -sh * tt + ch * x
        tnew = np.mod(np.rint(tp).astype(int), T)
        for k in range(pts.shape[0]):
            new_slabs[int(tnew[k])].append((xp[k], pts[k, 1]))
    out = [np.array(new_slabs[t]).reshape(-1, 2) for t in range(T)]
    return out


def edges_from_slices(slices, lam, n_slice_ref, T):
    r_s = r_s_for(n_slice_ref); r_t = lam * r_s
    offsets = []; off = 0
    for t in range(T):
        offsets.append(off); off += slices[t].shape[0]
    n_total = off
    edges = []
    rs2 = r_s * r_s
    for t in range(T):
        pts = slices[t]; nt = pts.shape[0]
        if nt < 2:
            continue
        d2 = np.sum((pts[:, None, :] - pts[None, :, :]) ** 2, axis=-1)
        iu = np.triu_indices(nt, k=1); mask = d2[iu] < rs2
        edges.extend(zip((iu[0][mask] + offsets[t]).tolist(),
                         (iu[1][mask] + offsets[t]).tolist()))
    if lam > 0:
        rt2 = r_t * r_t
        for t in range(T):
            tn = (t + 1) % T
            p0, p1 = slices[t], slices[tn]
            if p0.shape[0] == 0 or p1.shape[0] == 0:
                continue
            d2 = np.sum((p0[:, None, :] - p1[None, :, :]) ** 2, axis=-1)
            ii, jj = np.nonzero(d2 < rt2)
            edges.extend(zip((ii + offsets[t]).tolist(), (jj + offsets[tn]).tolist()))
    return n_total, [(int(u), int(v)) for u, v in edges]


# ====================================================================== #
# GATE
# ====================================================================== #
def validation_gate(verbose=True):
    report = {"checks": [], "passed": True, "aux": {}}

    def check(name, ok, detail, abort=True):
        report["checks"].append({"name": name, "ok": bool(ok), "detail": detail})
        if abort and not ok:
            report["passed"] = False
        if verbose:
            print(f"  [{'OK' if ok else ('!!' if not abort else 'FAIL')}] {name}: {detail}")

    n_slice, lam = 200, 0.75
    rng = np.random.default_rng(7)
    n_total, edges, slices, offsets, (r_s, r_t) = build_foliated(n_slice, T_SLICES, lam, rng, True)
    m = clustering_metrics(n_total, edges)

    # (1) cross-check estimador
    z_direct = 2.0 * len(edges) / n_total
    check("cross-check <z>=2E/N (clustering_metrics VERBATIM)",
          abs(m["deg_mean"] - z_direct) < 1e-9,
          f"{m['deg_mean']:.9f} vs {z_direct:.9f}")

    # (2) frame-dependencia DEMONSTRADA (esperado mudar -> nao Lorentz)
    sb = boost_refoliate(slices, offsets, T_SLICES, 0.8)
    nb, eb = edges_from_slices(sb, lam, n_slice, T_SLICES)
    mb = clustering_metrics(nb, eb)
    dz = abs(m["deg_mean"] - mb["deg_mean"])
    dc4 = abs(m["mean_local_square"] - mb["mean_local_square"])
    check("frame-dependencia DEMONSTRADA: <z>/C4 MUDAM sob boost+refoliacao (nao Lorentz)",
          dz > 1e-6 or dc4 > 1e-6,
          f"d<z>={dz:.4f} dC4={dc4:.4f}  (z {m['deg_mean']:.2f}->{mb['deg_mean']:.2f}, "
          f"C4 {m['mean_local_square']:.3f}->{mb['mean_local_square']:.3f})", abort=False)

    # (3) espaco-tempo genuino: percola no tempo p/ lam>0
    perc, spanned = time_percolates(n_total, edges, slices, offsets, T_SLICES)
    check("espaco-tempo genuino: componente gigante atravessa as T fatias (lam>0)",
          perc, f"fatias atravessadas={spanned}/{T_SLICES}")

    report["aux"] = {"n_total": n_total, "z": m["deg_mean"], "C4": m["mean_local_square"],
                     "transitivity": m["transitivity"], "r_s": r_s, "r_t": r_t,
                     "frame_dep_dz": dz, "frame_dep_dC4": dc4}
    return report


# ====================================================================== #
# MEDICAO CENTRAL: scan de lam x ladder de N
# ====================================================================== #
LAMS = [0.0, 0.25, 0.5, 0.75, 1.0, 1.5, 2.0]
N_SLICE_LADDER = [50, 100, 200, 400]      # N total = T * N_slice
N_SEEDS = 4
SEED_CAP = (400, 2)


def run_measurement(lams=LAMS, ladder=N_SLICE_LADDER, n_seeds=N_SEEDS):
    out = {"family": "foliated anisotropic (Horava-Lifshitz discrete) -- NOT Lorentz-invariant",
           "rule": "intra-slice |dx|<r_s (k_intra fixed) + inter-slice adjacent |dx|<lam*r_s",
           "L": L, "k_intra": K_INTRA, "T": T_SLICES, "lams": lams,
           "n_slice_ladder": ladder, "n_seeds": n_seeds,
           "estimator": "clustering_metrics VERBATIM", "by_lam": {}}
    for lam in lams:
        rows = []
        for n_slice in ladder:
            ns = SEED_CAP[1] if n_slice >= SEED_CAP[0] else n_seeds
            zs, c4s, ctr, perc_ok, ntot, t0 = [], [], [], [], [], time.perf_counter()
            for s in range(ns):
                rng = np.random.default_rng(3000 + s + n_slice + int(100 * lam))
                n_total, edges, slices, offsets, _ = build_foliated(
                    n_slice, T_SLICES, lam, rng, True)
                m = clustering_metrics(n_total, edges)
                zs.append(m["deg_mean"]); c4s.append(m["mean_local_square"])
                ctr.append(m["transitivity"]); ntot.append(n_total)
                if lam > 0:
                    p, _ = time_percolates(n_total, edges, slices, offsets, T_SLICES)
                    perc_ok.append(p)
            dt = time.perf_counter() - t0
            rows.append({"N_slice": n_slice, "N": float(np.mean(ntot)), "n_seeds": ns,
                         "z_mean": float(np.mean(zs)), "z_sem": float(np.std(zs)/np.sqrt(ns)),
                         "C4": float(np.mean(c4s)), "C4_sem": float(np.std(c4s)/np.sqrt(ns)),
                         "C_trans": float(np.mean(ctr)),
                         "perc_frac": float(np.mean(perc_ok)) if perc_ok else None,
                         "runtime_s": dt})
            print(f"  lam={lam:>4} Nsl={n_slice:>4} (N={np.mean(ntot):.0f}): "
                  f"z={np.mean(zs):6.2f} C4={np.mean(c4s):.4f} Ctr={np.mean(ctr):.3f} "
                  f"[{dt:.1f}s]", flush=True)
        z = np.array([r["z_mean"] for r in rows]); c4 = np.array([r["C4"] for r in rows])
        Nv = np.array([r["N"] for r in rows], float)
        zsl = (np.diff(z)/np.diff(np.log(Nv))).tolist() if len(rows) > 1 else []
        c4sl = (np.diff(c4)/np.diff(np.log(Nv))).tolist() if len(rows) > 1 else []
        out["by_lam"][f"{lam}"] = {"lam": lam, "rows": rows, "z_dlnN": zsl, "c4_dlnN": c4sl,
                                   "z_slope_top": zsl[-1] if zsl else float("nan"),
                                   "c4_slope_top": c4sl[-1] if c4sl else float("nan")}
    return out


def verdict(meas, z_rel=0.05, c4_sat=0.02, c4_decay=0.5):
    res = {"per_lam": {}, "arms_lams": [], "arms_lams_pos": []}
    for key, R in meas["by_lam"].items():
        rows = R["rows"]
        z_top, z_first = rows[-1]["z_mean"], rows[0]["z_mean"]
        c4_top, c4_first = rows[-1]["C4"], rows[0]["C4"]
        zrel = R["z_slope_top"]/z_top if z_top else 0.0
        zsat = abs(zrel) < z_rel
        c4pos = (c4_top > c4_sat) and (c4_top >= c4_decay * c4_first if c4_first > 0 else False)
        perc = rows[-1]["perc_frac"]
        genuine = (R["lam"] == 0.0) or (perc is not None and perc >= 0.99)
        arms = bool(zsat and c4pos)
        res["per_lam"][key] = {"lam": R["lam"], "z_top": z_top, "z_rel_slope": zrel,
                               "z_saturates": bool(zsat), "c4_first": c4_first, "c4_top": c4_top,
                               "c4_positive_sat": bool(c4pos), "perc_frac": perc,
                               "genuine_spacetime": bool(genuine), "arms": arms}
        if arms:
            res["arms_lams"].append(R["lam"])
            if R["lam"] > 0 and genuine:
                res["arms_lams_pos"].append(R["lam"])
    if res["arms_lams_pos"]:
        res["verdict"] = "GATILHO_ARMA (espaco-tempo foliado genuino; NAO Lorentz-invariante)"
    elif res["arms_lams"] == [0.0]:
        res["verdict"] = "RECLASSIFICACAO (so lam=0 arma = fatias desconexas, nao espaco-tempo)"
    elif not res["arms_lams"]:
        res["verdict"] = "MORTE (nem com foliacao arma)"
    else:
        res["verdict"] = "AMBIGUO"
    return res


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "all"
    if mode in ("gate", "all"):
        print("=" * 70 + "\nGATE (substrato foliado -- NAO Lorentz-invariante)\n" + "=" * 70)
        g = validation_gate()
        json.dump(g, open(os.path.join(HERE, "validation_gate.json"), "w"), indent=2)
        print(f"\n  GATE {'VERDE' if g['passed'] else 'VERMELHO'}")
        if not g["passed"]:
            print("  ABORTA."); sys.exit(1)
    if mode in ("measure", "all"):
        print("\n" + "=" * 70 + "\nMEDICAO: scan de lam x N\n" + "=" * 70)
        meas = run_measurement()
        v = verdict(meas); meas["verdict"] = v
        json.dump(meas, open(os.path.join(HERE, "foliated.json"), "w"), indent=2)
        print("\n" + "=" * 70 + "\nVEREDITO\n" + "=" * 70)
        for key, r in v["per_lam"].items():
            tag = "ARMA" if r["arms"] else "--"
            pf = f"perc={r['perc_frac']:.2f}" if r["perc_frac"] is not None else "perc=n/a"
            print(f"  lam={r['lam']:>4}: z->{r['z_top']:6.2f} "
                  f"(slope/z={r['z_rel_slope']:+.3f} {'SAT' if r['z_saturates'] else 'div'}) "
                  f"C4 {r['c4_first']:.3f}->{r['c4_top']:.3f} "
                  f"({'pos' if r['c4_positive_sat'] else 'decai'}) {pf} [{tag}]")
        print(f"\n  >>> VEREDITO: {v['verdict']}")
