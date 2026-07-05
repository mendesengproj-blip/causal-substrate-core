# -*- coding: utf-8 -*-
"""
n6_verdict.py -- consolida a bateria (n6_battery.jsonl) nas janelas FROZEN do
PRE_REGISTRO par.4 e emite o veredito D1/D2/D3.

Por (block, eps, mult): serie em N de <z>_Hasse -> slope d<z>/dlnN;
SNA-1: slope < 0.3 E z(N_max) <= 30.  SNA-3: C4/N > 0.3 e nao-decrescente.
(SNA-2 bola: SECUNDARIO, resolucao limitada a N<=120 -- declarado.)
Equilibracao: hot vs cold por ponto (|dz| relativo); pontos discordantes
reportados separadamente (nao descartados).
DISCOVERY (D1): algum (block,eps,mult) com SNA-1 E SNA-3.
D2: nenhum. D3: ambiguidade declarada (slope em [0.25,0.35] ou hot/cold
discordante no ponto decisivo).
"""
import json
import os
from collections import defaultdict

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
rows = [json.loads(l) for l in open(os.path.join(HERE, "n6_battery.jsonl"))]
print(f"runs carregados: {len(rows)}")

groups = defaultdict(list)
for r in rows:
    groups[(r["block"], r["eps"], r["mult"])].append(r)

verdicts = {}
any_sna = False
ambiguous = []
print(f"\n{'bloco':>10} {'eps':>5} {'mult':>5} | slope_z  z_top  C4/N(topN)  "
      f"posts  hc_ok | SNA1 SNA3 -> SNA")
print("-" * 95)
for (block, eps, mult), g in sorted(groups.items()):
    byN = defaultdict(list)
    for r in g:
        byN[r["N"]].append(r)
    Ns = sorted(byN)
    zbar, c4bar, pdbar, hc = [], [], [], []
    for N in Ns:
        hot = [r["z_hasse"] for r in byN[N] if r["init"] == "random"]
        cold = [r["z_hasse"] for r in byN[N] if r["init"] == "layered3"]
        zh, zc = np.mean(hot), np.mean(cold)
        zall = np.mean(hot + cold)
        zbar.append(zall)
        c4bar.append(np.mean([r["c4_per_node"] for r in byN[N]]))
        pdbar.append(np.mean([r["post_density"] for r in byN[N]]))
        hc.append(abs(zh - zc) / max(zall, 1e-9))
    slope = float(np.polyfit(np.log(Ns), zbar, 1)[0])
    z_top = float(zbar[-1])
    c4_top = float(c4bar[-1])
    c4_nondec = all(c4bar[i + 1] >= c4bar[i] - 0.05 * abs(c4bar[i])
                    for i in range(len(c4bar) - 1))
    hc_ok = all(h < 0.15 for h in hc)
    sna1 = (slope < 0.3) and (z_top <= 30.0)
    sna3 = (c4_top > 0.3) and c4_nondec
    sna = sna1 and sna3
    any_sna = any_sna or sna
    if 0.25 <= slope <= 0.35 or (sna and not hc_ok):
        ambiguous.append((block, eps, mult))
    verdicts[f"{block}|{eps}|{mult}"] = {
        "Ns": Ns, "z_series": [float(z) for z in zbar],
        "z_slope_dlnN": slope, "z_top": z_top,
        "c4_series": [float(c) for c in c4bar], "c4_top": c4_top,
        "c4_nondecreasing": bool(c4_nondec),
        "post_density_series": [float(p) for p in pdbar],
        "hotcold_rel_dz": [float(h) for h in hc], "hotcold_ok": bool(hc_ok),
        "SNA1": bool(sna1), "SNA3": bool(sna3), "SNA": bool(sna)}
    print(f"{block:>10} {eps:>5} {mult:>5} | {slope:+7.2f} {z_top:6.1f} "
          f"{c4_top:10.2f} {pdbar[-1]:6.3f}  {str(hc_ok):>5} |  "
          f"{int(sna1)}    {int(sna3)}  -> {'SIM' if sna else 'nao'}")

if any_sna:
    overall = ("D1 DISCOVERY: regiao SNA no diagrama -- escape dinamico por "
               "quebra espontanea; INVESTIGAR antes de reivindicar")
elif ambiguous:
    overall = f"D3 INCONCLUSIVO nas celulas {ambiguous}; demais fecham"
else:
    overall = ("D2: NENHUMA regiao do diagrama e SNA -- checklist "
               "QUANTICO-ROBUSTA no regime analiticamente continuado "
               "(1a extensao quantica das restricoes)")
print(f"\n>>> {overall}")
json.dump({"per_cell": verdicts, "any_sna": any_sna,
           "ambiguous": [list(a) for a in ambiguous], "overall": overall},
          open(os.path.join(HERE, "n6_verdict.json"), "w"), indent=2)
print("saved n6_verdict.json")
