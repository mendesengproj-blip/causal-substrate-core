"""
task2_generic_control.py — controle de campo genérico vs barreira c=1.

Pré-registro: ../SEMENTE_PRE_REGISTRO.md, ADENDO TAREFA-2 (critério congelado).
Pergunta: o colapso d_H->1 do FS-2D é a barreira c=1/branched-polymer GENÉRICA
(dirigida pelo acoplamento γ) ou algo específico da semente (o transporte κ)?
Teste: o colapso é κ-independente? κ=0 = controle genérico (sem transporte).
"""
import json
import math
import os

import numpy as np

from fs_seed2d import run_fs2d


def main():
    gammas = (0.0, 1.0, 2.0, 4.0)
    kappas = [0.0, 0.3, 0.6]  # 0 = controle genérico; 0.3 = semente FS-2D; 0.6 = transporte forte
    results = {}
    print("=== TAREFA 2 — colapso é κ-independente? (controle c=1) ===\n")
    for kappa in kappas:
        tag = 'GENERICO(κ=0)' if kappa == 0 else f'κ={kappa}'
        print(f"  --- {tag} ---")
        r = run_fs2d(gammas=gammas, kappa=kappa, equil=1300, sample=800, seed=11)
        results[f'{kappa}'] = r['rows']
        print()

    # extrai d_H(γ=4) e clumping(γ=4) por κ
    dH4 = {k: results[k]['4.0']['dH_band'] for k in results}
    clump4 = {k: results[k]['4.0']['O2_clump'] for k in results}
    dH0 = {k: results[k]['0.0']['dH_band'] for k in results}
    clump0 = {k: results[k]['0.0']['O2_clump'] for k in results}

    dH4_vals = list(dH4.values())
    spread_dH4 = max(dH4_vals) - min(dH4_vals)
    clump4_vals = [v for v in clump4.values() if v > 0]
    clump4_ratio = max(clump4_vals) / min(clump4_vals) if min(clump4_vals) > 0 else float('inf')

    # critério congelado
    kappa_independent = (spread_dH4 < 0.15) and (clump4_ratio < 2.0)
    qualitative_diff = (spread_dH4 > 0.30)
    if kappa_independent:
        verdict = ("REBAIXA D1: colapso é κ-INDEPENDENTE -> dirigido pelo ACOPLAMENTO, "
                   "não pelo transporte -> barreira c=1/branched-polymer GENÉRICA. O 'positivo' "
                   "FS-2D é não-específico à semente; evidência pró-semente passa a depender "
                   "inteiramente de D2 (memória/C_mem) em 3D.")
    elif qualitative_diff:
        verdict = ("D1 SOBREVIVE: κ muda o colapso qualitativamente -> o transporte faz algo "
                   "que o feedback genérico não faz. Prior elevado; D2/3D continua o discriminador real.")
    else:
        verdict = "AMBÍGUO (não-decisivo): resultado intermediário, não força direção."

    out = dict(gammas=list(gammas), kappas=kappas,
               dH_at_gamma4=dH4, clump_at_gamma4=clump4,
               dH_at_gamma0=dH0, clump_at_gamma0=clump0,
               spread_dH4=round(spread_dH4, 4), clump4_ratio=round(clump4_ratio, 3),
               kappa_independent=bool(kappa_independent),
               qualitative_diff=bool(qualitative_diff),
               verdict=verdict, full=results)

    print("  RESUMO (γ=4, onde o colapso é máximo):")
    for k in kappas:
        print(f"    κ={k}: d_H={dH4[str(float(k))]:.3f}  clumping={clump4[str(float(k))]:.3f}")
    print(f"  spread d_H(γ=4) entre κ = {spread_dH4:.4f} (<0.15 = κ-indep)")
    print(f"  razão clumping(γ=4) entre κ = {clump4_ratio:.3f} (<2 = κ-indep)")
    print(f"\n  >>> {verdict}")

    p = os.path.join(os.path.dirname(__file__), "task2_generic_control.json")
    with open(p, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False, default=str)
    print(f"\n[escrito: {p}]")
    return out


if __name__ == "__main__":
    main()
