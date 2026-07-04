"""gate2_detailed_balance.py -- NESS_GEOMETRIA Gate 2: quebra de balanço detalhado.

SÓ roda se Gate 1 PASSOU. Testa a CONDIÇÃO 2 (PRE_REGISTRO §4): no estado estacionário
periódico, o sistema NÃO satisfaz reversibilidade microscópica -> há corrente de
probabilidade no espaço de configurações, manifesta como HISTERESE (área da curva k0 vs
resposta geométrica = produção de entropia por ciclo) e como ASSIMETRIA de fluxo aceito
entre cada par de Pachner e seu inverso, integrada no ciclo.

NESS genuíno: histerese estável != 0, NÃO decai com mais amostragem, em ao menos um P
não-adiabático. MORTE (equilíbrio disfarçado): adiabático em todo P acessível -> área -> 0
(DB restaura). A varredura de P exibe a transição adiabático<->não-adiabático -> torna o
Gate falsificável dos DOIS lados.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from driven_cdt import build_driven, driven_run  # noqa: E402

K0_BAR, A = 2.5, 1.5
T = 10


def cycle_loop_area(k0, resp, P, burn_cycles):
    """Área média (com sinal) da curva de histerese (k0, resp) por ciclo, pós-burn.

    Para cada ciclo, ordena pela fase e aplica o shoelace na curva fechada (k0,resp)
    do ciclo. Em equilíbrio adiabático resp segue k0 sem atraso -> curva degenera numa
    linha -> área 0. Atraso (NESS) abre o laço -> área != 0. Normaliza por (range k0 *
    range resp) p/ dar fração adimensional do retângulo envolvente; reporta também a
    área crua e o desvio entre ciclos (estabilidade)."""
    k0 = np.asarray(k0, float)
    resp = np.asarray(resp, float)
    n = len(k0)
    ncyc = n // P
    areas = []
    for c in range(burn_cycles, ncyc):
        sl = slice(c * P, (c + 1) * P)
        x, y = k0[sl], resp[sl]
        if len(x) < 3:
            continue
        # shoelace na ordem temporal (o ciclo já percorre a fase 0..P-1 e fecha)
        area = 0.5 * np.sum(x * np.roll(y, -1) - np.roll(x, -1) * y)
        areas.append(area)
    areas = np.asarray(areas)
    if areas.size == 0:
        return {"n_cycles_used": 0}
    krange = k0.max() - k0.min()
    rrange = resp[burn_cycles * P:].max() - resp[burn_cycles * P:].min()
    norm = krange * rrange if (krange > 0 and rrange > 0) else 1.0
    mean_area = float(areas.mean())
    sem = float(areas.std(ddof=1) / np.sqrt(len(areas))) if len(areas) > 1 else float("inf")
    return {"n_cycles_used": int(areas.size),
            "mean_area": mean_area, "sem_area": sem,
            "area_over_sem": float(abs(mean_area) / sem) if sem > 0 else float("inf"),
            "frac_envelope": float(abs(mean_area) / norm) if norm > 0 else 0.0,
            "k0_range": float(krange), "resp_range": float(rrange)}


def phase_resolved_flux(rec, P, burn_cycles):
    """Fluxo líquido aceito (26-62) e (23-32) resolvido por fase do ciclo, pós-burn.
    Em DB o fluxo líquido integrado é 0 (volume conservado); o que importa p/ corrente é
    o PERFIL por fase ser anti-simétrico (adiabático) ou ter componente de atraso (NESS).
    Retorna o perfil médio por fase e a 'circulação' (assimetria fase-resolvida)."""
    tau = rec["tau"].astype(int)
    net26 = rec["acc_26"] - rec["acc_62"]
    net23 = rec["acc_23"] - rec["acc_32"]
    prof26 = np.zeros(P); prof23 = np.zeros(P); cnt = np.zeros(P)
    for i, t in enumerate(tau):
        if t // P < burn_cycles:
            continue
        ph = t % P
        prof26[ph] += net26[i]; prof23[ph] += net23[i]; cnt[ph] += 1
    cnt = np.maximum(cnt, 1)
    return {"flux26_by_phase": (prof26 / cnt).tolist(),
            "flux23_by_phase": (prof23 / cnt).tolist(),
            "net26_total_per_sweep": float(net26[tau // P >= burn_cycles].mean()),
            "net23_total_per_sweep": float(net23[tau // P >= burn_cycles].mean())}


def run_P(P, Vt, n_cycles, seed, therm):
    n_sweeps = n_cycles * P
    burn = n_cycles // 3
    t0 = time.time()
    g, k3 = build_driven(K0_BAR, T, Vt, seed=seed, therm=therm)
    rec = driven_run(g, k3, K0_BAR, A, P, Vt, n_sweeps, seed_meas=seed)
    dt = time.time() - t0
    out = {"P": P, "Vt": Vt, "n_cycles": n_cycles, "seed": seed, "runtime_s": round(dt, 1),
           "manifold_ok": bool(rec["manifold_ok"]), "burn_cycles": burn}
    out["hyst_z"] = cycle_loop_area(rec["k0"], rec["z"], P, burn)
    out["hyst_N0"] = cycle_loop_area(rec["k0"], rec["N0"], P, burn)
    out["flux"] = phase_resolved_flux(rec, P, burn)
    hz = out["hyst_z"]
    print(f"  [P={P:>3} Vt={Vt} s{seed}] {dt:.0f}s  hyst_z: area={hz.get('mean_area',0):+.3f} "
          f"±{hz.get('sem_area',0):.3f} (|a|/sem={hz.get('area_over_sem',0):.1f}, "
          f"frac_env={hz.get('frac_envelope',0):.3f})  manifold_ok={out['manifold_ok']}",
          flush=True)
    return out


def main():
    smoke = "--smoke" in sys.argv
    t0 = time.time()
    if smoke:
        Vt, Ps, therm = 600, [4, 12, 32], 60
        cyc = {4: 80, 12: 40, 32: 18}
        seeds = [301]
    else:
        Vt, Ps, therm = 800, [4, 12, 32, 96], 280
        cyc = {4: 200, 12: 80, 32: 40, 96: 16}
        seeds = [301, 302]
    print(f"=== GATE 2 (quebra de balanço detalhado) Vt={Vt} P-sweep={Ps} ===", flush=True)
    print("  histerese (área do laço k0 vs resposta) = produção de entropia/ciclo;"
          " adiabático->0, NESS->!=0", flush=True)
    out = {"config": {"K0_BAR": K0_BAR, "A": A, "T": T, "Vt": Vt, "Ps": Ps, "seeds": seeds},
           "runs": []}
    for P in Ps:
        for s in seeds:
            out["runs"].append(run_P(P, Vt, cyc[P], s, therm))
    # veredito: existe algum P com histerese significativa E estável (|area|/sem grande)?
    by_P = {}
    for P in Ps:
        rs = [r for r in out["runs"] if r["P"] == P]
        a = np.array([r["hyst_z"].get("mean_area", 0.0) for r in rs])
        sgn_consistent = bool(np.all(a > 0) or np.all(a < 0)) if len(a) > 1 else True
        sig = bool(np.all([r["hyst_z"].get("area_over_sem", 0) > 3.0 for r in rs]))
        frac = float(np.mean([abs(r["hyst_z"].get("frac_envelope", 0)) for r in rs]))
        by_P[str(P)] = {"mean_area": float(a.mean()), "significant": sig,
                        "sign_consistent": sgn_consistent, "frac_envelope": frac}
    out["by_P"] = by_P
    # NESS confirmado: algum P não-adiabático com histerese significativa, estável, sinal consistente
    ness = any(v["significant"] and v["sign_consistent"] and v["frac_envelope"] > 0.01
               for v in by_P.values())
    # adiabático (morte): a área CAI com P crescente (vai a 0 no lento) e nenhum P significativo
    fr = [by_P[str(P)]["frac_envelope"] for P in Ps]
    decays_with_P = bool(fr[-1] < 0.5 * fr[0]) if fr[0] > 0 else False
    out["gate2_pass"] = bool(ness)
    out["adiabatic_death"] = bool((not ness))
    out["frac_envelope_vs_P"] = {str(P): by_P[str(P)]["frac_envelope"] for P in Ps}
    out["decays_with_P"] = decays_with_P
    out["runtime_s"] = round(time.time() - t0, 1)
    name = "gate2_smoke.json" if smoke else "gate2.json"
    (HERE / name).write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(f"\n  frac_envelope vs P: {out['frac_envelope_vs_P']}", flush=True)
    print(f">>> GATE 2: pass(NESS)={out['gate2_pass']} adiabatic_death={out['adiabatic_death']} "
          f"[{out['runtime_s']:.0f}s] -> {name}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
