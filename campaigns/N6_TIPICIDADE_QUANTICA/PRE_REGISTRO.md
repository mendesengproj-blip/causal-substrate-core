# N6 — TIPICIDADE QUÂNTICA: pré-registro (congelado ANTES de qualquer código)

**Data:** 2026-07-04 · **Pasta:** `FRONTEIRA_COMPACTA/N6_TIPICIDADE_QUANTICA/`
**Antecedentes:** M10 (levantamento; C3 = candidato único) → **FASE 0 EXECUTADA
(`FASE0_ANCORAS.md`: 5/5 âncoras conferidas na fonte + revisão de prior §3)**.
**Natureza:** campanha computacional MODERADA (MCMC novo + bateria já paga) +
1 módulo analítico. A primeira sonda QUÂNTICA (regime continuado) da checklist.

---

## 1. A pergunta

> **O ensemble de causets pesado pela ação quântica (BD, analiticamente
> continuado) fica do lado invariante da classificação de M5 — ou a dinâmica
> concentra peso em fases que cruzam a fronteira (SNA)?**

Equivalente: as restrições C1–C8, provadas na cinemática clássica, são
**quântico-robustas** — ou o path integral realiza o escape que a cinemática
proíbe, via quebra espontânea (fase cristalina)?

## 2. Objetos (fixados pelas âncoras A1)

Espaço amostral: **2D-orders de N elementos** (par de permutações U,V;
e_i≺e_j ⟺ u_i<u_j ∧ v_i<v_j). Peso: **e^{−β̃ S_BD-2D(ε)}** (continuação
e^{iβS}→e^{−β̃S} DECLARADA; toda conclusão carrega a qualificação "no regime
continuado"). Parâmetros: β̃ (varrido pela transição), ε ∈ {0.12, 0.21} (dois
valores na faixa publicada; robustez), N ∈ {30, 50, 70, 90, 120}.
Fases conhecidas (A1): **random** (of~0.5, altura~10) e **cristalina** (of~0.6,
altura~3), transição de 1ª ordem em β̃_c(N,ε) ≈ 1.66/(Nε²).

## 3. Predições pré-registradas (prior ATUALIZADO pela Fase 0 §3)

| # | Predição | Prior |
|---|---|---|
| P-N6-1 | Fase random: não-SNA por valência (≡ box-order, controle M5/T3) | ALTO (~90%) |
| P-N6-2 | **Fase cristalina: não-SNA por valência** (camadas densas, altura~3 ⟹ ⟨z⟩~O(N)) ⟹ **D2: checklist quântico-robusta no regime continuado** | **~75%** |
| P-N6-3 | Nenhum ponto do diagrama (β̃, ε) varrido dá SNA=True | ~75% (segue de P-N6-2) |
| P-N6-4 (a morte-descoberta) | Alguma fase/região é SNA ⟹ escape dinâmico por quebra espontânea | ~15% |

**Leitura pré-declarada dos desfechos:** em QUALQUER desfecho o iff de M5
(SNA ⟺ não-invariante) SOBREVIVE — a fase cristalina é não-invariante. O que
está em teste é se a DINÂMICA leva o ensemble até o lado não-invariante-SNA
(escape com custo de Lorentz espontâneo) ou não (robustez). Redigir sem
upgrade retórico nos dois casos.

## 4. Instrumento

`n6_sampler.py`: MCMC sobre pares de permutações (moves: transposições em U
e/ou V; Metropolis em e^{−β̃S}); ação BD-2D com smearing ε (fórmula das
abundâncias de intervalos, conferida no full-text na implementação — A1).
`n6_battery.py`: bateria SNA **reusada** (gate_m1c/gate_m5: ⟨z⟩_Hasse, C4/N,
posts, altura/perfil de camadas; bola R adaptativo como secundário).

**Discriminadores PRIMÁRIOS (ressalva de resolução, Fase 0 §4, congelada):**
- **SNA-1 em série de N:** slope de ⟨z⟩_Hasse vs N dentro de CADA fase
  (janela: slope d⟨z⟩/dlnN < 0.3 e ⟨z⟩ ≤ 30 = valência finita; ⟨z⟩ ∝ N =
  falha clara).
- **SNA-3:** C4/N > 0.3 e não-decrescente em N.
- Perfil de camadas (altura, ocupação) e densidade de posts como
  caracterização de fase.
- **SNA-2 (bola/poly/exp_rate): SECUNDÁRIO** — N≤120 é pequeno;
  INCONCLUSIVO-por-resolução declarável sem penalidade.

## 5. Gate de engenharia (obrigatório VERDE antes de medição nova)

| # | Check | Critério |
|---|---|---|
| G1 | 2D-order válido (interseção de 2 lineares; DAG; fecho exato) | exaustivo em N pequeno |
| G2 | Ação BD-2D: valores de fase batem o publicado | random ~+4, cristalina ~−45 (nos parâmetros do review; tolerância 20%) |
| G3 | **β̃_c(N,ε) reproduz 1.66(3)/(Nε²)** | dentro de 2σ combinado, nos N∈{30,50,70} |
| G4 | 1ª ordem: bimodalidade/coexistência na transição + Binder | assinatura qualitativa clara |
| G5 | Fases: of~0.5/altura~10 (random) vs of~0.6/altura~3 (cristalina) | tolerância 15% |

Falha de gate = parar e diagnosticar; NENHUMA medição SNA vale com gate
não-verde.

## 6. Mortes pré-registradas

- **D1 (a descoberta, ~15%):** região do diagrama com SNA=True (valência
  finita E plaquetas percolantes, janelas do §4) ⟹ o path integral continuado
  realiza o escape por quebra espontânea ⟹ o custo do fóton vira transição de
  fase; delta maior nos papers (o "how to break" ganha uma rota DINÂMICA).
- **D2 (o fechamento, prior ~75%):** nenhuma região é SNA ⟹ **primeira
  extensão quântica da checklist**: "as restrições são robustas ao peso
  quântico continuado sobre 2D-orders" — sobe ao paper de restrições como
  qualificação de C2 (delta de revisão).
- **D3:** INCONCLUSIVO-por-resolução (transição não resolvida, ou SNA-1
  ambíguo na série de N) ⟹ escalar N (se orçamento) ou declarar e parar.
- Regra: janelas do §4 e gate do §5 NÃO se movem pós-dado; emendas só pré-run
  com trilha git (precedente N4/F2/M5).

## 7. Módulo A (analítico, recomendado, independente do MCMC)

**Lema C2 (posts sob interferência):** usando A4 (expressão de
Bombelli–Seggev–Watson para o nº esperado de posts em TP) e A3 (posts =
eventos-tronco covariantes), computar a **medida quantal** μ(post) na TP
COMPLEXA (t ∈ ℂ, |t| na faixa clássica) e perguntar: **a interferência suprime
ou reforça posts?** Congelado: (i) se μ(post)→0 mais rápido que o caso reAL ⟹
indício de fuga do confinamento-por-blocos (alimenta D1); (ii) se μ(post)
permanece positiva/estável ⟹ o mecanismo T4 tem eco quântico (alimenta D2).
Entregável: nota analítica; sem código além de avaliação numérica de fórmula.

## 8. Fases de execução

0. ✅ Âncoras (FASE0_ANCORAS.md). 1. Gate (§5). 2. Bateria nas fases: 2 pontos
β̃ bem dentro de cada fase + 3 pontos pela transição, × 2 valores de ε, ×
N∈{30,50,70,90,120}, seeds ≥ 8/ponto. 3. Módulo A (paralelo). 4. RESULTADO
consolidado. Orçamento: dias de máquina no máximo (sweeps O(N²), N≤120);
checkpoint JSONL; τ_int/ESS reportados (N-hig).

## 9. O que N6 NÃO reivindica

- TUDO no regime **analiticamente continuado** (β̃ real) — como TODA a
  literatura de MCMC causal citada; a versão genuinamente quântica (pesos
  complexos + funcional de decoerência) NÃO está em teste (só o Módulo A a
  sonda, no nível da medida quantal de UM evento). Dizer sempre.
- Nada sobre 4D; nada sobre matéria acoplada; nada sobre ħ/colapso (N4).
- O sample space é a classe 2D-orders (dimensionalmente restrita) — restrição
  herdada da literatura, declarada; generalizar é campanha futura.
- Anti-circularidade: ação = contagens de intervalos (intrínseca); nenhum
  número do mundo; o rótulo de fase vem dos observáveis covariantes.
