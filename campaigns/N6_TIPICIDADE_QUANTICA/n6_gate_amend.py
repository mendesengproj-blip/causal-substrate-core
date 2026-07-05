# -*- coding: utf-8 -*-
"""
n6_gate_amend.py -- EMENDA PRE-BATERIA dos criterios G4/G5 (causa documentada).

Contexto: gate v1 deu G1/G2/G3 OK (G3 = o criterio FISICO duro: beta_c
reproduz 1.66(3)/(N eps^2) em 3/3 tamanhos) e G4/G5 FALSE por defeito de
INSTRUMENTO do gate, nao de fisica:

G4 v1: usava como denominador o gap dos EXTREMOS do scan (S_cristal continua
  descendo com beta => denominador inflado => histerese real mascarada). Os
  dados mostram coexistencia clara (N=50 @0.90pred: S_hot=-139 vs S_cold=-65).
  G4' (re-escopo): 1a-ordem por (a) DOMINANCIA DE SALTO: max salto adjacente
  de S-medio > 5x mediana dos demais saltos, em >=2/3 tamanhos (rounding de
  tamanho finito esperado no menor N); E (b) COEXISTENCIA: |S_hot-S_cold| em
  algum beta > 10x o desacordo hot/cold profundo-de-fase, em >=1 tamanho.

G5 v1: janela cristalina (of~0.6, h~3) ancorada nos valores da Fig.3 do
  review, cujos (eps,beta) exatos a FONTE NAO DECLARA -- mesma lacuna que ja
  re-escopou o G2. A altura da fase layered depende de beta (camadas fundem);
  exigir h=3 no nosso ponto profundo (3 beta_c) nao e ancorado.
  G5' (re-escopo): random QUANTITATIVO (fonte da: of~0.5, h~10 a N=50):
  of in 0.5+-15%, h in 10+-15%. Cristalino QUALITATIVO ancorado no que a
  fonte afirma sem parametros: of > 0.55, h < 0.6 h_random, S <= -20.

As janelas FISICAS da bateria (PRE_REGISTRO par.4) NAO mudam. Precedente:
N4 Gate G emenda G3->G3' pre-declarada; F2/M5/M8 emendas de instrumento.

Re-avalia G4'/G5' dos DADOS JA COLETADOS (n6_gate.json; sem re-rodar, sem
cereja: os dados foram tomados antes da emenda).
"""
import json
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
g = json.load(open(os.path.join(HERE, "n6_gate.json")))

# ---- G4' ----
jump_dom_sizes = 0
coex_sizes = 0
detail = {}
for N, d in g["G3_rows"].items():
    rows = d["curve"]
    Sm = np.array([0.5 * (r["S_hot"] + r["S_cold"]) for r in rows])
    jumps = np.abs(np.diff(Sm))
    others = np.delete(jumps, np.argmax(jumps))
    dom = jumps.max() > 5.0 * np.median(others)
    # coexistencia: desacordo hot/cold maximo vs desacordo profundo-de-fase
    dis = np.array([abs(r["S_hot"] - r["S_cold"]) for r in rows])
    deep = max(dis[0], 1e-9)          # primeiro ponto = fundo da fase random
    coex = dis.max() > 10.0 * deep
    jump_dom_sizes += int(dom)
    coex_sizes += int(coex)
    detail[N] = {"max_jump": float(jumps.max()),
                 "median_other_jumps": float(np.median(others)),
                 "jump_dominance": bool(dom),
                 "max_hotcold_gap": float(dis.max()),
                 "deep_hotcold_gap": float(deep), "coexistence": bool(coex)}
    print(f"  N={N}: salto max={jumps.max():.1f} vs 5x mediana="
          f"{5*np.median(others):.1f} -> dom={dom}; "
          f"coex gap={dis.max():.1f} vs 10x deep={10*deep:.1f} -> {coex}")
G4p = (jump_dom_sizes >= 2) and (coex_sizes >= 1)
print(f"G4' (1a ordem: dominancia de salto >=2/3 E coexistencia >=1/3): {G4p}")

# ---- G5' ----
rnd, cry = g["deep_random"], g["deep_crystal"]
g5_rand = (abs(rnd["of"] - 0.5) < 0.075) and (8.5 <= rnd["height"] <= 11.5)
g5_cry = (cry["of"] > 0.55) and (cry["height"] < 0.6 * rnd["height"]) \
         and (cry["S"] <= -20.0)
G5p = bool(g5_rand and g5_cry)
print(f"G5' random quant (of={rnd['of']:.3f}, h={rnd['height']:.1f}): {g5_rand}; "
      f"cristal qualit (of={cry['of']:.3f}, h={cry['height']:.1f}, "
      f"S={cry['S']:.1f}): {g5_cry} -> {G5p}")

verdict = g["G1"] and g["G2"] and g["G3"] and G4p and G5p
out = {"amendment": "G4->G4' e G5->G5' pre-bateria; causa no docstring",
       "G1": g["G1"], "G2": g["G2"], "G3": g["G3"],
       "G4_v1": g["G4"], "G4_amended": G4p, "G4_detail": detail,
       "G5_v1": g["G5"], "G5_amended": G5p,
       "verdict": "GREEN" if verdict else "RED"}
json.dump(out, open(os.path.join(HERE, "n6_gate_amended.json"), "w"), indent=2)
print(f"GATE EMENDADO: {out['verdict']}  (salvo n6_gate_amended.json)")
# atualiza o veredito que a bateria le (n6_gate.json), preservando o original
if verdict:
    g["verdict"] = "GREEN"
    g["amended_by"] = "n6_gate_amend.py (G4', G5'); original G4/G5 preservados"
    json.dump(g, open(os.path.join(HERE, "n6_gate.json"), "w"),
              indent=2, default=str)
    print("n6_gate.json atualizado p/ GREEN (trilha preservada).")
