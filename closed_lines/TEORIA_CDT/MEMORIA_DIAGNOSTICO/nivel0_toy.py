"""nivel0_toy.py — Diagnostico Nivel 0: a memoria (C_mem) lava por ESTRUTURA ou por KERNEL?

Pre-registro: PRE_REGISTRO.md (criterios congelados). Modelo de brinquedo 1D, SEM CDT/TEIC.
Reusa o estimador C_mem VERBATIM de F1b_acao (fs_seed3d.c_mem, fs_run3d.cmem_tail_with_error).

Processo (Langevin generalizado discreto, overdamped, mean-revertido com memoria):
    x_t = x_{t-1} - theta*dt*sum_j K(j) x_{t-j} + sigma*sqrt(dt)*xi_t,   sum_j K(j)=1
O sinal medido = INCREMENTOS dx_t (analogo do growth_by_slice de FS-3D, um fluxo), sobre
n_real realizacoes independentes (as "colunas/fatias" do estimador C_mem).

Eixo 1 (FORMA do kernel): K1 exponencial | K2 lei-de-potencia | K3 envelhecimento.
Eixo 2 (REGIME): (a) estacionario (apos burn + checagem de plato) | (b) transiente (de t=0).
Controle: ruido branco (sem memoria) -> C_mem-tail ~ 0 por construcao.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "F1b_acao"))
from fs_seed3d import c_mem                    # noqa: E402  (estimador VERBATIM)
from fs_run3d import cmem_tail_with_error      # noqa: E402  (cauda + erro blocking)


# ============================================================== #
# kernels (pesos K(1..W), normalizados a soma 1)
# ============================================================== #
def kernel_exp(W, tau_m):
    j = np.arange(1, W + 1)
    K = np.exp(-j / tau_m)
    return K / K.sum()


def kernel_power(W, alpha):
    j = np.arange(1, W + 1)
    K = j.astype(float) ** (-alpha)
    return K / K.sum()


# ============================================================== #
# Langevin generalizado: retorna incrementos dx [n_steps, n_real]
# ============================================================== #
def run_gle(kind, n_steps, n_real, rng, W=800, theta=0.6, dt=1.0, sigma=1.0,
            tau_m=5.0, alpha=0.5, tau_m0=5.0, t_age=400.0):
    """kind in {'exp','power','aging','white'}. dx = incrementos."""
    if kind == "white":
        # ruido branco puro (markoviano, sem memoria) -> incrementos iid
        return sigma * rng.standard_normal((n_steps, n_real))

    if kind == "exp":
        K = kernel_exp(W, tau_m)
    elif kind == "power":
        K = kernel_power(W, alpha)
    elif kind == "aging":
        K = None  # kernel recomputado a cada passo (escala cresce com t)
    else:
        raise ValueError(kind)

    hist = np.zeros((W, n_real))          # hist[0]=x_{t-1}, hist[1]=x_{t-2}, ...
    x = 0.01 * rng.standard_normal(n_real)
    dxs = np.empty((n_steps, n_real))
    Krev = K[::-1].copy() if K is not None else None   # alinhado p/ hist[j]=x_{t-1-j}
    for t in range(n_steps):
        if kind == "aging":
            tau_t = tau_m0 * (1.0 + t / t_age)          # memoria CRESCE com o tempo
            Kt = kernel_exp(W, tau_t)
            Fmem = -theta * (Kt[:, None] * hist).sum(axis=0)
        else:
            # hist[j] = x_{t-1-j}; K(j+1) pondera x_{t-(j+1)} -> usa K direto
            Fmem = -theta * (K[:, None] * hist).sum(axis=0)
        dx = Fmem * dt + sigma * np.sqrt(dt) * rng.standard_normal(n_real)
        x = x + dx
        hist = np.roll(hist, 1, axis=0)
        hist[0] = x
        dxs[t] = dx
    return dxs


# ============================================================== #
# checagem de estacionariedade (plato de variancia 1a vs 2a metade)
# ============================================================== #
def is_stationary(series, tol=0.15):
    """series [n,n_real]: var da 1a metade ~ var da 2a metade (dentro de tol relativo)."""
    n = series.shape[0]
    v1 = series[: n // 2].var()
    v2 = series[n // 2:].var()
    if v2 <= 0:
        return False, float("inf")
    rel = abs(v1 - v2) / v2
    return bool(rel < tol), float(rel)


# ============================================================== #
# medicao C_mem-tail num bloco de incrementos
# ============================================================== #
def measure_tail(dx_block, max_tau=15, n_blocks=8):
    cm, tail, tail_err = cmem_tail_with_error(dx_block, max_tau=max_tau, n_blocks=n_blocks)
    return cm, float(tail), float(tail_err)


def run_one(kind, seed, n_steps_eq=6000, n_meas=3000, n_real=48, **kw):
    """Roda um kernel; mede C_mem-tail nos regimes (a) estacionario e (b) transiente."""
    rng = np.random.default_rng(seed)
    # ---- regime (b) TRANSIENTE: incrementos a partir de t=0 (sem burn) ----
    dx_all = run_gle(kind, n_steps_eq, n_real, rng, **kw)
    dx_trans = dx_all[:n_meas]
    cm_t, tail_t, err_t = measure_tail(dx_trans)
    # ---- regime (a) ESTACIONARIO: 2a metade (apos burn longo) ----
    burn = n_steps_eq - n_meas
    dx_stat = dx_all[burn:]
    stat_ok, stat_rel = is_stationary(dx_all[burn // 2:])  # checa plato na 2a metade
    cm_s, tail_s, err_s = measure_tail(dx_stat)
    return {
        "kind": kind,
        "stationary_declared": stat_ok, "stationarity_rel": stat_rel,
        "transient": {"tail": tail_t, "tail_err": err_t, "cmem": [round(float(x), 4) for x in cm_t]},
        "stationary": {"tail": tail_s, "tail_err": err_s, "cmem": [round(float(x), 4) for x in cm_s]},
    }


def sigma_vs_control(tail, err, ctrl_tail, ctrl_err):
    e = np.sqrt(err ** 2 + ctrl_err ** 2)
    return (tail - ctrl_tail) / e if e > 0 else 0.0


def main():
    t0 = time.time()
    smoke = "--smoke" in sys.argv
    n_steps_eq = 3000 if smoke else 8000
    n_meas = 1500 if smoke else 3500
    n_real = 32 if smoke else 64
    n_seeds = 2 if smoke else 5

    print("=== NIVEL 0 — memoria lava por ESTRUTURA ou por KERNEL? (toy 1D, sem CDT) ===",
          flush=True)
    configs = {
        "white_CONTROL": dict(kind="white"),
        "K1_exp":        dict(kind="exp", tau_m=5.0),
        "K2_power":      dict(kind="power", alpha=0.5),
        "K3_aging":      dict(kind="aging", tau_m0=5.0, t_age=400.0),
    }
    results = {}
    for name, kw in configs.items():
        kind = kw.pop("kind")
        # media sobre seeds (incrementos independentes)
        tails_t, errs_t, tails_s, errs_s, stat_flags, cms_s, cms_t = [], [], [], [], [], [], []
        for s in range(n_seeds):
            r = run_one(kind, seed=100 + 17 * s, n_steps_eq=n_steps_eq, n_meas=n_meas,
                        n_real=n_real, **kw)
            tails_t.append(r["transient"]["tail"]); errs_t.append(r["transient"]["tail_err"])
            tails_s.append(r["stationary"]["tail"]); errs_s.append(r["stationary"]["tail_err"])
            stat_flags.append(r["stationary_declared"])
            cms_s.append(r["stationary"]["cmem"]); cms_t.append(r["transient"]["cmem"])
        # combina seeds: media das caudas, erro = std/sqrt(nseeds) (conservador)
        def comb(vals):
            v = np.array(vals); return float(v.mean()), float(v.std(ddof=1) / np.sqrt(len(v)))
        Tt, Et = comb(tails_t); Ts, Es = comb(tails_s)
        results[name] = {
            "kind": kind, "params": kw,
            "transient_tail": Tt, "transient_err": Et,
            "stationary_tail": Ts, "stationary_err": Es,
            "stationary_declared_frac": float(np.mean(stat_flags)),
            "cmem_stationary_mean": np.mean(np.array(cms_s), axis=0).round(4).tolist(),
            "cmem_transient_mean": np.mean(np.array(cms_t), axis=0).round(4).tolist(),
        }
        print(f"  [{name:14s}] transiente tail={Tt:+.3f}+/-{Et:.3f} | "
              f"estacionario tail={Ts:+.3f}+/-{Es:.3f} | stat_declared="
              f"{results[name]['stationary_declared_frac']:.0%}", flush=True)

    # ---- vereditos (criterios congelados) ----
    ctrl = results["white_CONTROL"]
    ct_s, ce_s = ctrl["stationary_tail"], ctrl["stationary_err"]
    ct_t, ce_t = ctrl["transient_tail"], ctrl["transient_err"]
    verdicts = {}
    for name in ("K1_exp", "K2_power", "K3_aging"):
        r = results[name]
        sig_s = sigma_vs_control(r["stationary_tail"], r["stationary_err"], ct_s, ce_s)
        sig_t = sigma_vs_control(r["transient_tail"], r["transient_err"], ct_t, ce_t)
        # preserva: cauda POSITIVA e > 3 sigma acima do controle
        preserves_stat = (r["stationary_tail"] > 0) and (sig_s > 3)
        preserves_trans = (r["transient_tail"] > 0) and (sig_t > 3)
        verdicts[name] = {
            "sigma_stat_vs_ctrl": float(sig_s), "sigma_trans_vs_ctrl": float(sig_t),
            "preserves_stationary": bool(preserves_stat),
            "preserves_transient": bool(preserves_trans),
        }
        print(f"  >>> {name}: stat {sig_s:+.1f}sigma (preserva={preserves_stat}) | "
              f"trans {sig_t:+.1f}sigma (preserva={preserves_trans})", flush=True)

    any_stat = any(v["preserves_stationary"] for v in verdicts.values())
    any_trans_k1 = verdicts["K1_exp"]["preserves_transient"]
    if any_stat:
        overall = "ESPECIFICO_DO_KERNEL (algum kernel preserva C_mem em estacionariedade -> ARMA Nivel 1)"
    elif any_trans_k1:
        overall = "TRANSIENTE_PRESERVA (regime transiente preserva C_mem p/ K1 -> ARMA Nivel 1)"
    else:
        overall = ("ESTRUTURAL (memoria lava em equilibrio p/ TODO kernel; transiente nao salva K1) "
                   "-> NAO rodar Nivel 1; busca por semente-de-equilibrio FECHADA")
    print(f"\n  ==== VEREDITO NIVEL 0: {overall} ====", flush=True)

    out = {"config": {"n_steps_eq": n_steps_eq, "n_meas": n_meas, "n_real": n_real,
                      "n_seeds": n_seeds, "smoke": smoke},
           "results": results, "verdicts": verdicts, "overall": overall,
           "runtime_s": time.time() - t0}
    name = "nivel0_smoke.json" if smoke else "nivel0_toy.json"
    (HERE / name).write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(f"[{out['runtime_s']:.0f}s] -> {name}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
