"""gate1_stationarity.py -- NESS_GEOMETRIA Gate 1: estacionariedade estatística.

A armadilha central (MEMORIA_DIAGNOSTICO): "nunca atinge platô" != NESS. Gate 1 testa a
CONDIÇÃO 1: sob o drive periódico, os observáveis geométricos (d_H, z, volume) atingem
distribuição ESTÁVEL no tempo (estroboscópica, fase fixa do ciclo) -- o oposto de drift.

PASSA: sem deriva significativa (slope estroboscópico ~0 dentro do erro de blocking) E
1ª-metade ≈ 2ª-metade. MORTE: drift persistente até o limite computacional (= α=0.1).

Critério congelado no PRE_REGISTRO §3. Reusa driven_cdt (que reusa F1b intacto).
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np
from scipy import stats

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from driven_cdt import build_driven, driven_run  # noqa: E402

K0_BAR, A, P = 2.5, 1.5, 8          # primário (PRE_REGISTRO §2)
T = 10


def stationarity_stats(series, n_blocks=8):
    """Testa estacionariedade (charter §3: média/variância constantes ENTRE janelas,
    dentro do erro de blocking). Distingue flutuação BOUNDED autocorrelada (estacionário)
    de DERIVA monotônica não-limitada (a armadilha α=0.1).

    Método (Flyvbjerg blocking): parte a série em n_blocks janelas, mede médias de bloco
    μ_i. A DERIVA é significativa só se a regressão de μ_i vs i tem t-stat alto (a inclinação
    excede o espalhamento entre blocos). Não usa |span|/std da série crua (confundido por
    modos lentos autocorrelados)."""
    s = np.asarray(series, float)
    s = s[np.isfinite(s)]
    n = len(s)
    if n < 12:
        return {"n": n, "stationary": None, "reason": "amostras insuficientes"}
    nb = min(n_blocks, n // 3)
    edges = np.linspace(0, n, nb + 1).astype(int)
    mu = np.array([s[edges[i]:edges[i + 1]].mean() for i in range(nb)])
    vb = np.array([s[edges[i]:edges[i + 1]].var(ddof=1) for i in range(nb)])
    x = np.arange(nb, dtype=float)
    # regressão das MÉDIAS DE BLOCO; SE da inclinação a partir dos resíduos
    A_ = np.vstack([x, np.ones_like(x)]).T
    coef, res, *_ = np.linalg.lstsq(A_, mu, rcond=None)
    slope, intercept = coef
    yhat = A_ @ coef
    dof = max(1, nb - 2)
    s_err = np.sqrt(np.sum((mu - yhat) ** 2) / dof)
    sxx = np.sum((x - x.mean()) ** 2)
    se_slope = s_err / np.sqrt(sxx) if sxx > 0 else float("inf")
    t_slope = abs(slope) / se_slope if se_slope > 0 else float("inf")
    drift_span_over_scatter = abs(slope * (nb - 1)) / (mu.std(ddof=1) + 1e-12)
    # 1ª vs 2ª metade dos BLOCOS (média e variância)
    h = nb // 2
    m1, m2 = mu[:h].mean(), mu[h:].mean()
    sem = np.sqrt(mu[:h].var(ddof=1) / h + mu[h:].var(ddof=1) / (nb - h)) if h >= 2 else float("inf")
    half_z = abs(m1 - m2) / sem if sem > 0 and np.isfinite(sem) else float("inf")
    # variância constante: F-test dof-aware nas DUAS metades da série crua (1% bilateral).
    # (bounds fixos 0.33-3.0 dão falso-negativo p/ estimador ruidoso esparso, ex. d_H n~16.)
    nh = n // 2
    s1, s2 = s[:nh], s[nh:]
    v1, v2 = s1.var(ddof=1), s2.var(ddof=1)
    var_ratio = v2 / v1 if v1 > 0 else float("inf")
    d1, d2 = len(s2) - 1, len(s1) - 1
    lo, hi = stats.f.ppf(0.005, d1, d2), stats.f.ppf(0.995, d1, d2)
    var_stable = bool(lo < var_ratio < hi) if v1 > 0 and v2 > 0 else False
    # CRITÉRIO PRE-REGISTRO §3 (faithful): "média E variância constantes ENTRE janelas, dentro
    # do erro de BLOCKING". Isso É o teste de duas-metades com SEM-bloqueado (half_z<3) + o
    # F-test de variância (var_stable). O t_slope (tendência linear) é sensível à
    # autocorrelação (médias de bloco correlacionadas -> falso-positivo de deriva ~2.7 mesmo no
    # NULL de equilíbrio, que é estacionário por definição); fica como GUARDA lenta contra a
    # armadilha de deriva NÃO-LIMITADA monotônica (α=0.1: t_slope explode), não como gate fino.
    # Calibração: o controle NULO (equilíbrio) DEVE passar -> define a validade do estimador.
    stationary = (half_z < 3.0) and var_stable and (t_slope < 4.0)
    return {"n": n, "n_blocks": nb, "mean": float(s.mean()), "std": float(s.std(ddof=1)),
            "block_slope": float(slope), "t_slope": float(t_slope),
            "drift_span_over_blockscatter": float(drift_span_over_scatter),
            "half1_mean": float(m1), "half2_mean": float(m2), "half_diff_in_sem": float(half_z),
            "var_ratio_2nd_1st": float(var_ratio), "var_Fbounds": [float(lo), float(hi)],
            "var_stable": var_stable, "stationary": bool(stationary)}


def cycle_average(rec, key, P):
    """Média de rec[key] sobre cada ciclo completo de P sweeps -> série 1 ponto/ciclo
    (remove a oscilação imposta pelo drive; usa TODOS os sweeps, não só a fase 0)."""
    tau = rec["tau"].astype(int)
    vals = rec[key]
    ncyc = (tau.max() + 1) // P
    out = []
    for c in range(ncyc):
        m = (tau >= c * P) & (tau < (c + 1) * P)
        if m.any():
            out.append(float(vals[m].mean()))
    return np.asarray(out)


def run_one(label, k0_bar, A, P, Vt, n_cycles, seed, therm, dH_per_cycles=2):
    n_sweeps = n_cycles * P
    dH_every = max(1, dH_per_cycles * P)        # mede d_H a cada dH_per_cycles ciclos
    t0 = time.time()
    g, k3 = build_driven(k0_bar, T, Vt, seed=seed, therm=therm)
    rec = driven_run(g, k3, k0_bar, A, P, Vt, n_sweeps, seed_meas=seed,
                     dH_every=dH_every)
    dt = time.time() - t0
    # descarta 1º terço (transiente) p/ o teste de estacionariedade
    burn = n_cycles // 3
    out = {"label": label, "k0_bar": k0_bar, "A": A, "P": P, "Vt": Vt,
           "n_cycles": n_cycles, "n_sweeps": n_sweeps, "seed": seed,
           "burn_cycles": burn, "runtime_s": round(dt, 1),
           "manifold_ok": bool(rec["manifold_ok"]),
           "k0_range": [float(rec["k0"].min()), float(rec["k0"].max())]}
    # observáveis: média por ciclo (remove a oscilação imposta), pós-burn
    for key in ("N3", "N0", "z"):
        ca = cycle_average(rec, key, P)
        out[key] = stationarity_stats(ca[burn:])
    # d_H: série esparsa pós-burn
    dH_tau, dH_val = rec["dH_tau"], rec["dH"]
    mb = dH_tau >= burn * P
    out["dH"] = stationarity_stats(dH_val[mb], n_blocks=5)
    geo_keys = ("N3", "z", "dH")
    out["gate1_pass"] = bool(out["manifold_ok"] and
                             all(out[k].get("stationary") for k in geo_keys))
    print(f"  [{label}] {dt:.0f}s manifold_ok={out['manifold_ok']} "
          f"N3 stat={out['N3']['stationary']} z stat={out['z']['stationary']} "
          f"dH stat={out['dH']['stationary']} (dH={out['dH'].get('mean',float('nan')):.2f}"
          f"±{out['dH'].get('std',float('nan')):.2f}) -> PASS={out['gate1_pass']}", flush=True)
    return out


def main():
    smoke = "--smoke" in sys.argv
    t0 = time.time()
    if smoke:
        Vt, n_cycles, therm = 600, 48, 120
    else:
        # therm=450: relaxação de d_H/z a Vt=1500 platô em ~350-400 sweeps (diagnóstico
        # de horizonte); therm=140 media ainda na subida -> deriva espúria (não a armadilha).
        Vt, n_cycles, therm = 1500, 70, 450
    results = {"config": {"K0_BAR": K0_BAR, "A": A, "P": P, "T": T, "Vt": Vt,
                          "n_cycles": n_cycles, "therm": therm}, "runs": []}
    print(f"=== GATE 1 (estacionariedade) Vt={Vt} n_cycles={n_cycles} ===", flush=True)
    # controle NULO A=0 (deve ser estacionário trivialmente = equilíbrio)
    results["runs"].append(run_one("NULO_A0", K0_BAR, 0.0, P, Vt, n_cycles, seed=101, therm=therm))
    # drive primário A=1.5 P=8 -- 2 seeds
    for s in (201, 202):
        results["runs"].append(run_one(f"DRIVE_A{A}_P{P}_s{s}", K0_BAR, A, P, Vt,
                                        n_cycles, seed=s, therm=therm))
    drive_runs = [r for r in results["runs"] if r["A"] > 0]
    results["gate1_drive_pass"] = bool(all(r["gate1_pass"] for r in drive_runs))
    results["null_pass"] = bool(results["runs"][0]["gate1_pass"])
    results["runtime_s"] = round(time.time() - t0, 1)
    name = "gate1_smoke.json" if smoke else "gate1.json"
    (HERE / name).write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(f"\n>>> GATE 1: drive_pass={results['gate1_drive_pass']} "
          f"null_pass={results['null_pass']} [{results['runtime_s']:.0f}s] -> {name}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
