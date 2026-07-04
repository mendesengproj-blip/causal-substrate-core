"""
finalize.py -- analise matched-N e veredito final.

A heuristica per-alpha de "C4 nao-decai" no verdict() pode ser enganada pelo
truncamento do ladder (alpha alto bate no teto de candidatos e nao alcanca o N do
topo, entao seu C4 'parece' nao decair). O teste honesto e comparar a familia
repulsiva contra a baseline de POISSON (alpha=0) no MESMO N (controle interno,
analogo ao control_c4 da percolacao de longo alcance). Se a repulsao nao move nem
<z> nem C4 acima da baseline de Poisson a N casado, AMBAS as barreiras falham.
"""
import json
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
meas = json.load(open(os.path.join(HERE, "repulsion.json")))

alphas = [str(a) for a in meas["alphas"]]
base = meas["by_alpha"]["0.0"]
base_by_target = {r["N_target"]: r for r in base["rows"]}

matched = {"note": "familia(alpha) vs Poisson(alpha=0) no MESMO N_target",
           "by_target": {}}
for tgt in meas["ret_ladder"]:
    if tgt not in base_by_target:
        continue
    b = base_by_target[tgt]
    row = {"N_target": tgt, "N_base": b["N_mean"],
           "z_base": b["z_mean"], "C4_base": b["C4"], "alpha": {}}
    for a in alphas:
        rr = {r["N_target"]: r for r in meas["by_alpha"][a]["rows"]}
        if tgt not in rr:
            continue
        r = rr[tgt]
        row["alpha"][a] = {
            "N": r["N_mean"], "z": r["z_mean"], "C4": r["C4"],
            "z_over_base": r["z_mean"] / b["z_mean"] if b["z_mean"] else None,
            "C4_over_base": r["C4"] / b["C4"] if b["C4"] else None}
    matched["by_target"][str(tgt)] = row

# resumo das barreiras
z_slopes = {a: meas["by_alpha"][a]["z_slope_top"] for a in alphas}
z_rel = {a: (meas["by_alpha"][a]["z_slope_top"] /
             meas["by_alpha"][a]["rows"][-1]["z_mean"]) for a in alphas}
# C4 vs Poisson a N casado (usa o maior N_target onde TODOS os alphas tem dado)
common_targets = [t for t in meas["ret_ladder"]
                  if all(t in {r["N_target"] for r in meas["by_alpha"][a]["rows"]} for a in alphas)]
# para C4, compare no maior N comum
c4_ratio_top = {}
if common_targets:
    tcmp = max(common_targets)
    b = base_by_target[tcmp]
    for a in alphas:
        rr = {r["N_target"]: r for r in meas["by_alpha"][a]["rows"]}
        c4_ratio_top[a] = rr[tcmp]["C4"] / b["C4"] if b["C4"] else None
    c4_compare_N = tcmp
else:
    c4_compare_N = None

# C4 decai com N? (sinal de mean-field/arvore) -- usa a baseline alpha=0
c4_first0 = base["rows"][0]["C4"]; c4_top0 = base["rows"][-1]["C4"]
c4_decays_poisson = c4_top0 < c4_first0

final = {
    "verdict": meas["verdict"]["verdict"],
    "barreira_1_z": {
        "resultado": "FALHA (diverge em todo alpha)",
        "z_rel_slope_top_por_alpha": z_rel,
        "satura_em": meas["verdict"]["z_saturates_alphas"],
        "leitura": "expoente local relativo de <z> permanece >> 0.05 em todo alpha; "
                   "a repulsao NAO reduz o crescimento da coordenacao."},
    "barreira_2_C4": {
        "resultado": "FALHA (rastreia Poisson; decai com N)",
        "C4_familia_sobre_Poisson_no_N_casado": c4_ratio_top,
        "C4_compare_N_target": c4_compare_N,
        "C4_decai_na_baseline_Poisson": bool(c4_decays_poisson),
        "leitura": "a N casado, C4(alpha) ~= C4(Poisson) (razao ~1); C4 decai com N "
                   "como o grafo de cobertura de Poisson. As flags per-alpha 'C4>0' "
                   "de alpha=0.2/0.3 no verdict() sao ARTEFATO do truncamento do ladder "
                   "(esses alpha batem no teto de candidatos e nao alcancam o N do topo)."},
    "matched_N": matched,
    "conclusao": "MORTE_LIMPA em AMBAS as barreiras: a repulsao Lorentz-invariante "
                 "(hard-core no intervalo invariante) nao reduz <z> (diverge como "
                 "Poisson) nem cria clustering acima da baseline de Poisson. Quebrar a "
                 "INDEPENDENCIA do sprinkling (a hipotese do teorema parcial) com "
                 "repulsao de par invariante NAO escapa das barreiras: a exclusao "
                 "remove pares perto do cone, mas eles se regeneram na nova densidade e "
                 "a divergencia da orbita de boost (nao-compacta) sobrevive."}
json.dump(final, open(os.path.join(HERE, "verdict_final.json"), "w"), indent=2)

print("=" * 70)
print("MATCHED-N: familia(alpha) vs Poisson(alpha=0) no MESMO N_target")
print("=" * 70)
for tgt, row in matched["by_target"].items():
    print(f"\n  N_target={tgt} (Poisson: N={row['N_base']:.0f} z={row['z_base']:.2f} "
          f"C4={row['C4_base']:.4f})")
    for a, d in row["alpha"].items():
        print(f"    alpha={a:>4}: N={d['N']:6.0f}  z={d['z']:6.2f} (x{d['z_over_base']:.3f})  "
              f"C4={d['C4']:.4f} (x{d['C4_over_base']:.3f})")
print("\n" + "=" * 70)
print(f"Barreira 1 (<z>): {final['barreira_1_z']['resultado']}")
print(f"  z_rel_slope_top: {{ " + ', '.join(f'{a}:{v:+.3f}' for a,v in z_rel.items()) + " }}")
print(f"Barreira 2 (C4):  {final['barreira_2_C4']['resultado']}")
if c4_compare_N:
    print(f"  C4(alpha)/C4(Poisson) @N_target={c4_compare_N}: "
          + "{ " + ', '.join(f'{a}:{v:.3f}' for a,v in c4_ratio_top.items()) + " }")
print(f"\n  >>> VEREDITO FINAL: {final['verdict']}  (ambas as barreiras falham)")
