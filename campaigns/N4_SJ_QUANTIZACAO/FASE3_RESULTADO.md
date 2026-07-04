# N4 — FASE 3: RESULTADO (SSEE pelo canto de Rindler)

**Data:** 2026-07-03 · **Runner:** `n4_fase3.py` (declaração v1 c5a595d +
emenda pré-run v2 acf053c, ambas commitadas ANTES do run que avaliaram) ·
**Dados:** `n4_fase3.json` + `n4_fase3_rows.jsonl` (72 runs: L ∈ {1.5, 2, 3}
× 24 seeds, ρ=8, geometria N2) · **Custo:** 407 s (a mais barata da campanha).

## 0. Veredito em uma página

**M3.1 (gate de reprodução) PASSA. M3.2 (a medição central): SUB-ÁREA,
robusto em α — NENHUMA das duas saídas nomeadas no pré-registro ocorreu.**
O prior era 60/40 entre ÁREA (resgate quântico) e SUPER-ÁREA (4ª face);
o dado deu a terceira saída declarada ("surpresa; reportar como tal"),
com estrutura interna que **divide a pergunta em duas** (§3):

- a propriedade **qualitativa** da lei de área — localização no canto — É
  resgatada pelo truncamento (S truncada independe da janela: razão 0.93 vs
  4.0 do volume);
- o **expoente** em L não é 2: κ = 1.57 ± 0.02 (α=1) / 1.50 ± 0.03 (α=2),
  estatisticamente colado no expoente do próprio corte (n₂ ∝ N_O^{3/4} ⇒
  1.48) — o corte de número domina a escala em L nesta geometria.

| Medição | Critério (congelado) | Medido | Veredito |
|---|---|---|---|
| M3.1 volume sem trunc. | κ_un ∈ [1.5, 2.5] E S_un/S_tr(L=3) > 2 | **κ_un = 2.46 ± 0.04; razão 17.6** | ✅ gate |
| M3.2 α=1 (critério) | \|κ−2\| ≤ max(0.30, 2·SE) | **κ = 1.566 ± 0.025** (Δ = 0.43) | **SUB_AREA** |
| M3.2 α=2 (robustez) | mesma classificação? | **κ = 1.500 ± 0.034** | SUB_AREA ✓ (sem flag) |
| Eixo-janela L=3 (diag.) | volume ⇒ ~4; área ⇒ ~1 | **trunc 0.934 ± 0.017; untrunc 4.78** | trunc LOCALIZA no canto |
| Higiene | pares ±λ; S₀ caixa-inteira | max 1e-15; S₀ ≤ 1.6e-11 | ✅ |

**Nenhuma morte (pré-reg §8.6: qualquer saída de M3 = refinamento).**
P-N4-3 resolvida: **não-área** — mas na direção que ninguém nomeou.

## 1. M3.1 — o gate de reprodução (volume sem truncamento) PASSA

S_untrunc(W_MAIN) = 42.0 / 82.5 / 229.6 em L = 1.5/2/3 ⇒ κ_un = 2.46 ± 0.04,
dentro da banda extensiva declarada [1.5, 2.5]; razão untrunc/trunc em L=3 =
17.6 ≫ 2. A lei de volume da literatura (A7–A10, atribuída à não-localidade
do causet) reproduz no nosso canto de Rindler — pipeline validado, a medição
central está autorizada a falar. *Observação (não gated):* κ_un = 2.46 > 2 e
razão de janela untrunc 4.78 > 4 — levemente SUPER-extensivo, eco quântico
do super-volume clássico de N2-F2; registrado.

## 2. M3.2 — SUB-ÁREA robusta, e o mecanismo visível nos dados

S_trunc(α=1, W_MAIN) = 4.421 ± 0.038 / 6.779 ± 0.074 / 13.034 ± 0.074
⇒ **κ = 1.566 ± 0.025**; 2 − κ = 0.43 > tol 0.30 ⇒ SUB_AREA pelo critério
congelado. α=2 dá κ = 1.500 ± 0.034 ⇒ mesma classe, sem ROBUSTEZ_FRACA.

**O expoente é o do corte.** n₂ = round(N_O^{3/4}) com N_O ∝ L^{1.97} dá
expoente previsto 1.48 — o medido (1.57/1.50) está colado nele, e a entropia
por modo retido é quase constante: S/n₂ = 0.181 / 0.185 / 0.192 (+6% no
dobro de L). **Hipótese mundana líder, declarada:** nesta geometria o corte
de número α N_O^{3/4} é a restrição ativa — S conta modos retidos, e o
expoente 3/2 = (3/4)·2 é aritmética do corte, não física do horizonte.

**Mas o rastreio do corte NÃO é total — o teste de janela o refuta na forma
pura:** em L=3 fixo, W_MAIN tem n₂ = 2.75× o de W_HALF e S(W_MAIN)/S(W_HALF)
= 0.941 ± 0.017 (pareado por seed) — a S truncada NÃO segue o corte entre
janelas; segue o CANTO. Se S fosse pura contagem de modos, a razão seria
~2.75. A imagem consistente: o truncamento remove a não-localidade de volume
e deixa um objeto localizado no canto (qualitativamente área), cuja
NORMALIZAÇÃO em L é governada pelo corte, não pela área.

**Curvatura (3 tamanhos, sem poder):** inclinações por segmento 1.486
(1.5→2) e 1.612 (2→3) — subindo; razão medido/alvo-eq.9 (ρ^{1/2}L²/4):
2.78 → 2.40 → 2.05 — caindo em direção a ~2. Uma aproximação-à-área por
baixo em L maior NÃO é excluída por 3 tamanhos; fica como fronteira aberta
(a extensão honesta seria L ∈ {4, 6}, N até ~7000/13000, custo denso ~horas
— não rodada: fora da grade congelada).

## 3. Leitura para o programa (o que sobe ao paper-núcleo)

O pré-registro nomeou duas leituras: ÁREA = "resgate quântico" e SUPER-ÁREA
= "4ª face". O dado deu uma TERCEIRA, que separa o que as duas leituras
tratavam como um bloco:

1. **A localização (o conteúdo qualitativo da lei de área) é resgatada pela
   quantização + corte declarado.** A MI clássica de N2-F2 era super-área
   L^{3.36} e de VOLUME entre janelas; a SSEE truncada é janela-independente
   (0.93). O que a camada 1 (não-localidade) quebrava no setor clássico, o
   corte UV covariante conserta NO ASPECTO GEOMÉTRICO.
2. **O valor do expoente NÃO é resgatado:** fica preso ao esquema de corte
   (κ ≈ expoente do corte), não à área. O "S = ρ^{2/d}A/4" da eq. 9 (A9) não
   emerge aqui — nossa geometria de canto plano com transversal periódica
   difere dos diamantes aninhados da literatura, onde S ∝ √N ≁ n_max ∝
   N^{3/4} (lá o corte NÃO dominava; aqui domina — diferença de geometria,
   registrada como achado).
3. **Consequência para o Teorema da Fronteira:** a tensão binária ganha uma
   face quântica REFINADA, não a 4ª face bruta: *"a quantização covariante
   com corte declarado localiza a entropia na fronteira (resgate
   qualitativo), mas a escala quantitativa é do corte, não da geometria"* —
   entre o resgate total (que apoiaria S∝A no substrato) e a quebra total
   (que mataria). Delta próprio para o paper-núcleo, redigido SEM upgrade
   retórico (regra 3 do ROADMAP_V2).

## 4. Emenda pré-run (trilha completa)

O smoke (commit v1, `n4_fase3_rows_smoke_v1.jsonl` preservado) mediu um piso
de resolução do estimador: com N_O ≤ 17 o pipeline INVERTE (S_trunc > S_un)
e instabiliza entre seeds; com N_O ≤ 5 degenera (S = −9e15, |Im μ| = 0.07);
com N_O ≥ 60 é sadio (padrão do G4). Causa: a laje N2-fase-2 (u < 0.5) é
mais FINA que a discretude ρ^{−1/4} = 0.59. Emenda v2 (acf053c, ANTES do run
real): W_MAIN = mesma família escalada ×2 (u:t = 1:2 mantido), piso N_O ≥ 40
declarado, W_HALF (N2 verbatim) vira diagnóstico em L=3. Critérios físicos
INALTERADOS. Parente direto das emendas no-wrap/k_res da Fase 1 e da lição
m·a ≲ 0.3: **a escala de discretude come janelas finas — dimensionar
sub-regiões em unidades de ρ^{−1/d} ANTES do smoke** (banco de lições).

Caveat de enrolamento (declarado na v1): fração de links enrolados ~0.40,
quase constante em L (0.408/0.401/0.389) — não dirige a tendência em L;
contaminação uniforme da normalização do kernel, registrada.

## 5. Estado do funil

```
Fase 0 ✅ → Gate G ✅ 4/4 → Fase 1 ✅ (D1/D2 não)
  → Fase 3 ✅ ESTA SESSÃO (M3.1 gate ✓; M3.2 = SUB_AREA robusta,
     localização-resgatada/expoente-do-corte; nenhuma morte)
  → Fase 2 (Goldstone/multipleto) — ÚNICA fase restante da campanha
```

Q3 respondida (com a terceira saída); Q0 [teorema, Fase 0]; Q1 respondida
(Fase 1); Q2 aberta (Fase 2). Nenhum observável ímpar-sob-conjugação
apareceu (D-Q0 quieta). Após a Fase 2: RESULTADO.md consolidado da campanha
e delta do paper-núcleo.
