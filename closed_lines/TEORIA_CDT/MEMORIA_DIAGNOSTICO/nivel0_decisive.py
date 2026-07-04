"""nivel0_decisive.py — Nivel 0 DEFINITIVO: o C_mem-tail curto (max_tau=15, estimador FS-3D)
da' FALSO-POSITIVO de memoria para kernels lentos; a integral de JANELA LARGA (que captura a
decaida completa) decide. Mostra o artefato E a resolucao, na mesma tabela.

Descoberta-chave (vs a 1a leitura 'ESPECIFICO'): o tail positivo de K2/K3/exp-longo no
max_tau=15 e' o BUMP de curto-lag que qualquer kernel lento tem; ao alargar a janela ate'
capturar a decaida, a integral reverte para ~ -0.5 (anti-persistente, = FS-3D) para TODO kernel
que de fato equilibra. So' kernels que NUNCA equilibram (memoria ~infinita = fora-do-equilibrio)
retem o sinal. => ESTRUTURAL.

Reusa run_gle (modelo) e c_mem VERBATIM (estimador FS-3D).
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "F1b_acao"))
from fs_seed3d import c_mem               # noqa: E402  (estimador VERBATIM)
from nivel0_toy import run_gle, is_stationary  # noqa: E402  (modelo do Nivel 0)

MAXW = 400                                # janela LARGA (captura decaida completa)
SHORT = 15                                # janela do estimador FS-3D (mostra artefato)


def integ(cm, lo, hi):
    return float(np.nansum(cm[lo:hi + 1]))


def measure(dx_block):
    """C_mem do bloco de incrementos; retorna (tail_curto[1..15], integral_larga[1..MAXW])."""
    cm = c_mem(dx_block, max_tau=MAXW)
    return integ(cm, 1, SHORT), integ(cm, 1, MAXW), cm


def run_kernel(kind, seed, burn, n_meas, n_real, W, **kw):
    rng = np.random.default_rng(seed)
    dx = run_gle(kind, burn + n_meas, n_real, rng, W=W, **kw)
    # transiente: cabeca; estacionario: cauda (apos burn)
    st_short, st_wide, _ = measure(dx[burn:])
    tr_short, tr_wide, _ = measure(dx[:n_meas])
    stat_ok, stat_rel = is_stationary(dx[burn // 2:])   # equilibrou de fato?
    return dict(stat_short=st_short, stat_wide=st_wide,
                trans_short=tr_short, trans_wide=tr_wide,
                stationary_ok=stat_ok, stat_rel=stat_rel)


def main():
    t0 = time.time()
    smoke = "--smoke" in sys.argv
    burn = 12000 if smoke else 30000
    n_meas = 6000 if smoke else 12000
    n_real = 48 if smoke else 64
    W = 1500
    n_seeds = 2 if smoke else 3

    configs = {
        "white_CONTROL":   dict(kind="white"),
        "K1_exp_tau5":     dict(kind="exp", tau_m=5.0),     # FS-3D
        "exp_tau50_LONGO": dict(kind="exp", tau_m=50.0),    # controle: exp de tau longo
        "K2_power_a0.5":   dict(kind="power", alpha=0.5),
        "K2_power_a0.3":   dict(kind="power", alpha=0.3),
        "power_a0.1_EXTR": dict(kind="power", alpha=0.1),   # quase nao-equilibra
        "K3_aging":        dict(kind="aging", tau_m0=5.0, t_age=4000.0),
    }
    print("=== NIVEL 0 DEFINITIVO: janela-curta (FS-3D, max_tau=15) vs janela-LARGA (decisiva) ===",
          flush=True)
    print(f"   burn={burn} n_meas={n_meas} n_real={n_real} W={W} seeds={n_seeds} | "
          f"SHORT=Sum[1..{SHORT}], WIDE=Sum[1..{MAXW}]", flush=True)
    rows = {}
    for name, kw in configs.items():
        kind = kw.pop("kind")
        acc = {k: [] for k in ("stat_short", "stat_wide", "trans_short", "trans_wide",
                               "stationary_ok", "stat_rel")}
        for s in range(n_seeds):
            r = run_kernel(kind, 200 + 31 * s, burn, n_meas, n_real, W, **kw)
            for k in acc:
                acc[k].append(r[k])

        def me(vals):
            v = np.array(vals, float)
            return float(v.mean()), float(v.std(ddof=1) / np.sqrt(len(v))) if len(v) > 1 else 0.0
        sS, sSe = me(acc["stat_short"]); sW, sWe = me(acc["stat_wide"])
        tS, tSe = me(acc["trans_short"]); tW, tWe = me(acc["trans_wide"])
        rows[name] = dict(kind=kind, params=kw,
                          stat_short=sS, stat_short_err=sSe, stat_wide=sW, stat_wide_err=sWe,
                          trans_short=tS, trans_wide=tW,
                          stationary_ok=float(np.mean(acc["stationary_ok"])),
                          stat_rel=float(np.mean(acc["stat_rel"])))
        print(f"  [{name:16s}] estac: CURTO={sS:+.3f} -> LARGO={sW:+.3f}+/-{sWe:.3f} | "
              f"transiente LARGO={tW:+.3f} | equilibrou={rows[name]['stationary_ok']:.0%} "
              f"(rel={rows[name]['stat_rel']:.2f})", flush=True)

    # ---- veredito DECISIVO (janela larga, estacionario) ----
    ctrlW = rows["white_CONTROL"]["stat_wide"]
    ctrlWe = max(rows["white_CONTROL"]["stat_wide_err"], 1e-3)
    verdicts, preserves_any = {}, False
    for name, r in rows.items():
        if name == "white_CONTROL":
            continue
        sig = (r["stat_wide"] - ctrlW) / np.sqrt(r["stat_wide_err"] ** 2 + ctrlWe ** 2)
        # preserva memoria SO' se: integral larga POSITIVA, >3sigma acima do controle, E equilibrou
        equilibrated = r["stationary_ok"] >= 0.5
        preserves = (r["stat_wide"] > 0) and (sig > 3) and equilibrated
        # falso-positivo de janela curta: curto positivo mas largo nao
        false_pos = (r["stat_short"] > 0.05) and not (r["stat_wide"] > 0 and sig > 3)
        verdicts[name] = dict(sigma_wide_vs_ctrl=float(sig), equilibrated=bool(equilibrated),
                              preserves_memory=bool(preserves),
                              short_window_false_positive=bool(false_pos))
        if preserves:
            preserves_any = True
        print(f"  >>> {name}: LARGO {sig:+.1f}sigma vs ctrl, equilibrou={equilibrated}, "
              f"PRESERVA={preserves}, falso-pos-curto={false_pos}", flush=True)

    if preserves_any:
        overall = ("ESPECIFICO_DO_KERNEL: algum kernel que EQUILIBRA preserva C_mem na janela larga "
                   "-> ARMA Nivel 1")
    else:
        overall = ("ESTRUTURAL: na janela larga (decisiva) TODO kernel que equilibra LAVA a memoria "
                   "(integral ~ -0.5, anti-persistente = FS-3D); os positivos de janela-curta sao "
                   "ARTEFATO. Memoria so' sobrevive em kernel que NUNCA equilibra (fora-do-equilibrio). "
                   "=> NAO rodar Nivel 1; busca por semente-de-EQUILIBRIO estruturalmente FECHADA.")
    print(f"\n  ==== VEREDITO DECISIVO: {overall} ====", flush=True)
    out = dict(config=dict(burn=burn, n_meas=n_meas, n_real=n_real, W=W, n_seeds=n_seeds,
                           SHORT=SHORT, WIDE=MAXW, smoke=smoke),
               rows=rows, verdicts=verdicts, overall=overall, runtime_s=time.time() - t0)
    name = "nivel0_decisive_smoke.json" if smoke else "nivel0_decisive.json"
    (HERE / name).write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(f"[{out['runtime_s']:.0f}s] -> {name}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
