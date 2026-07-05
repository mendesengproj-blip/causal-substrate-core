# N6 — TIPICIDADE QUÂNTICA: RESULTADO

**Data:** 2026-07-05 · **Pré-registro:** `PRE_REGISTRO.md` (congelado após Fase 0
com âncoras na fonte e revisão de prior declarada) · **Gate:** VERDE com emenda
pré-bateria documentada (`n6_gate.json` + `n6_gate_amended.json`) · **Dados:**
`n6_battery.jsonl` (390 runs) + `n6_module_a.json` · **Veredito:**
`n6_verdict.json`. A primeira travessia QUÂNTICA da checklist de restrições.

---

## 0. Veredito em uma página

**D2 — NENHUMA região do diagrama de fases é SNA: a checklist de restrições é
QUÂNTICO-ROBUSTA no regime analiticamente continuado.** O ensemble de 2D-orders
pesado pela ação de Benincasa–Dowker (continuada, e^{−β̃S}) nunca cruza a
fronteira de invariância da classificação M5 — em 14/14 células (fase × ε ×
acoplamento) o veredito SNA é NÃO, sempre por **SNA-1 (valência divergente)**,
cada fase pelo seu mecanismo:

| Bloco | ⟨z⟩_Hasse em N=30→120 | slope d⟨z⟩/dlnN | mecanismo | SNA |
|---|---|---|---|---|
| **random** (2 β × 2 ε) | 4.4 → ~7.1 | +1.7 a +1.8 | **log-divergente** (box-order, T3 — o eco do M5) | não |
| **cristalina** (2 β × 2 ε) | ~14 → 44–49 | **+21 a +25** | **linear em N** (camadas densas tipo-KR, z ≈ 0.4·N) | não |
| **transição** (3 β × 2 ε; N=30–50) | interpola | +1.1 a +16 | mistura bimodal das duas | não |

E o achado estrutural que fecha o círculo do programa: **SNA-3 (laços) passa em
TODAS as células** — o ensemble quântico é RICO em plaquetas (C4/N de 13 no
random a ~25.000 no cristal) — mas o preço é sempre a valência. **O binário
clássico do programa (valência finita XOR laços percolantes, nunca ambos)
REAPARECE INTACTO no lado quântico.** A dinâmica quântica continuada não compra
a interseção que a cinemática proíbe; ela apenas escolhe de que lado da mesma
tensão o ensemble senta.

**Módulo A (amplitudes genuinamente complexas):** a interferência **REFORÇA**
posts monotonicamente em todo o domínio de normalizabilidade (log-ratio +11 na
borda |q|→1) — o mecanismo T4 (posts ⟹ 1D) tem eco quântico FORTE. Nenhum
indício de fuga.

**O prior da Fase 0 (~75% D2) confirmou-se, com o mecanismo previsto** (a fase
cristalina "altura ~3" da fonte é o layered denso, não o cristal-E1).

## 1. O que foi medido (trilha completa)

**Gate VERDE** (com emenda de instrumento pré-bateria, causa documentada):
- **G3, o critério físico duro, passou 3/3:** β_c estimado 1.174/0.657/0.541 vs
  previsto 1.255/0.753/0.538 (N=30/50/70) — o motor reproduz a lei publicada
  β_c=1.66(3)/(Nε²) dentro de 2σ. Smoke igualmente forte: valores de fase batem
  a fonte quase dígito a dígito (random S=+3.5/of=0.506/h=9 vs ~+4/0.5/~10;
  layered S=−41.6/of=0.69/h=3 vs ~−45/0.6/3).
- G4′/G5′: dominância de salto (93 vs 43; 198 vs 41) + coexistência 3/3 (1ª
  ordem confirmada nos nossos dados); fases profundas nas janelas re-escopadas.
  (v1 G4/G5 literal-false por defeito de instrumento do gate — denominador
  inflado; janela ancorada em Fig.3 sem (ε,β) declarados na fonte — emendados
  ANTES da bateria, dados do scan preservados, física da bateria intocada.)

**Bateria (janelas FROZEN do pré-registro §4):** blocos de FASE completos
(crystal 160/160, random 160/160, N até 120, 8 seeds/ponto = 4 hot + 4 cold);
transição N=30 completo (48/48) + N=50 parcial (22/48).
- **Cristalina — a medição decisiva, inédita:** valência linear em N
  (z̄ = 13.9→45.7 em ε=0.12/m=2.0; idem nas 4 células), **nos DOIS ramos de
  equilibração** (hot +15 a +21; cold +26 a +29) — a conclusão independe da
  equilibração lenta do cristal profundo (acc ~1%, hc_dz 0.22–0.38, declarado;
  os ramos discordam na TAXA, não na direção). C4/N ~ 22.000–29.000 (plaquetas
  abundantes): é o layered denso tipo-Kleitman–Rothschild.
- **Random:** z̄_top ≈ 7 em N=120 com slope ~1.8 em lnN = a divergência
  LOGARÍTMICA do box-order (T3) — exatamente a linha `box_order_2D` da bateria
  M5, agora como fase do path integral. Posts ~ 0 (sem confinamento por blocos
  aqui; a falha é por valência).
- **Transição (medida em N=30–50):** interpola entre os dois mecanismos
  (slopes +1.1 a +16; C4/N 17→1050); nenhuma célula SNA.

## 2. Cláusula de orçamento (declarada) e o fechamento analítico da transição

A cauda do bloco de transição (N≥70; 148 dos 560 runs) foi APARADA por
orçamento (execução interrompida 2×; precedente N4 §9). O fechamento não fica
descoberto, por um argumento com grau declarado [argumento, não medição]:

> A transição é de **1ª ordem** (publicado; confirmado por G4′). Num ponto de
> 1ª ordem o ensemble é MISTURA BIMODAL das duas fases puras (coexistência),
> não uma terceira estrutura. Ambas as fases puras têm valência divergente
> (medido, blocos completos). Uma mistura de ensembles de valência divergente
> tem valência divergente. Logo nenhuma janela SNA em N grande na transição.

As células de transição MEDIDAS (N=30–50) confirmam a interpolação sem
estrutura nova. O bloco N≥70 fica listado como executável decorativo futuro.

## 3. Leitura fina (pré-declarada no pré-registro §3, sem upgrade retórico)

1. **O iff de M5 sobrevive** — trivialmente, porque nenhuma fase é SNA; nem foi
   preciso invocar a cláusula "a cristalina é não-invariante".
2. **A primeira extensão quântica da checklist:** as restrições C1–C8, provadas
   na cinemática clássica, valem no ensemble quanticamente pesado (continuado)
   sobre 2D-orders — nenhuma região do diagrama (β̃, ε) realiza o substrato que
   um fóton emergente exigiria. Delta para o paper de restrições: qualificação
   de C2 ("robusta ao peso quântico continuado sobre 2D-orders [medido]").
3. **O binário é mais fundo que a medida:** uniforme (KR), clássica-Poisson,
   covariante-CSG e agora quântica-continuada-BD — TODAS as medidas testadas
   pousam do lado "laços sem valência finita" ou "valência finita sem laços".
   A tensão é da ORDEM, não do peso.
4. **Módulo A** é a única sonda de amplitude genuinamente complexa: posts são
   REFORÇADOS pela interferência (μ_quantal cresce monotonicamente até divergir
   na borda de normalizabilidade |q|=1) — o confinamento-por-blocos do T4
   ganha eco quântico, na direção OPOSTA à fuga.

## 4. Escopo honesto (o que N6 NÃO estabelece)

- Tudo no regime **analiticamente continuado** (β̃ real) — como toda a
  literatura de MCMC causal. A dinâmica genuinamente quântica (pesos complexos
  + funcional de decoerência) NÃO foi testada além do Módulo A (medida quantal
  de UM evento-tronco, com a prescrição declarada).
- Classe **2D-orders** (dimensionalmente restrita), N ≤ 120, ε ∈ {0.12, 0.21}
  — herdados da literatura; 4D/classes maiores são campanha futura.
- SNA-2 (expoentes de bola) não foi usado como critério (ressalva de resolução
  do pré-registro §4 — N pequeno); a decisão veio de SNA-1/SNA-3, que são
  exatos nestes N.
- Equilibração do cristal profundo é lenta (declarado); conclusão robusta por
  independência de ramo.
- Transição N≥70 aparada (cláusula §2).

## 5. Custo e disciplina

Gate 244 s; bateria 390 runs (~2h de máquina em 3 sessões, checkpoint JSONL
sobreviveu a 2 kills sem perda); Módulo A ~1 min. Pré-registro congelado APÓS
Fase 0 com âncoras na fonte e prior revisado ANTES do congelamento; emendas de
gate pré-bateria com causa e trilha; nenhuma janela FÍSICA movida pós-dado.

*Reprodução:* `python n6_gate.py` → `python n6_gate_amend.py` →
`python n6_battery.py` (retomável) → `python n6_verdict.py`;
`python n6_module_a.py` independente. numpy; reusa `gate_m1c`/`rs_trigger`.
