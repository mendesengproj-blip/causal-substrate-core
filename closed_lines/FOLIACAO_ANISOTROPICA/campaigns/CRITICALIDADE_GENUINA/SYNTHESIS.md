# SÍNTESE — Criticalidade genuína sobre FOLIACAO_ANISOTROPICA

> # ⚠️ **ESTE SUBSTRATO NÃO É MAIS LORENTZ-INVARIANTE MANIFESTO.**
> Foliação preferida + distância intra-fatia (Hořava–Lifshitz discreto). Nenhum
> resultado abaixo muda isso — nem que pareça positivo.

**Data:** 2026-06-30 · `FOLIACAO_ANISOTROPICA/campaigns/CRITICALIDADE_GENUINA/`
**VEREDITO: `CRITICALIDADE DE RETICULADO CONHECIDA`** — criticalidade genuína (ξ/χ
divergindo, J_c estável, LRO), mas em **classe de universalidade indistinguível de um
reticulado regular puro**. **NÃO é uma assinatura nova de Hořava–Lifshitz discreto.**

---

## 1. Pergunta e disciplina

O substrato foliado armou o gatilho cinemático (⟨z⟩ finito + C4 positivo). Aqui: o
ferromagneto O(3) da TEIC sobre ele sustenta **criticalidade genuína com classe distinta
do reticulado** (= física nova), ou é só Heisenberg empilhado conhecido? **O controle de
reticulado puro é obrigatório** — divergência de ξ sozinha não é sucesso; o critério é
**ξ divergindo COM classe distinta do reticulado**.

Reuso VERBATIM: `xi_suite.measure_point`/`locate_Jc`/`build_lattice_3d`, `orientation_core`.
Única novidade: `build_foliated_fss` (substrato foliado em modo FSS, densidade fixa,
lado linear `m` crescente, `N~m³`, comparável ao reticulado `m×m×m`).

## 2. Controle de reticulado puro (anchor) — `build_lattice_3d` VERBATIM

| m | N | z | J_c | χ_max | m(ord) |
|---|---|---|---|---|---|
| 6 | 216 | 6 | 0.660 | 2.15 | 0.67 |
| 8 | 512 | 6 | 0.660 | 3.14 | 0.66 |
| 10 | 1000 | 6 | 0.660 | 5.83 | 0.65 |
| 12 | 1728 | 6 | 0.660 | 6.84 | 0.64 |

**χ_max ~ N^0.592±0.066**, J_c **fixo** (0.660), U₄~0.5–0.6, ξ/L~0.10–0.14, LRO. Reproduz
a criticalidade de 2ª ordem 3D-Heisenberg (anchor sadio; o expoente vem um pouco abaixo
do textbook 0.667 por tamanho finito `m≤12` — mas isso afeta os DOIS substratos igualmente,
então a **comparação** é válida).

## 3. Foliado em λ=0.75 fixo — **NÃO Lorentz-invariante**

| m | N | z | J_c | χ_max | m(ord) | ξ/L@J_c |
|---|---|---|---|---|---|---|
| 6 | 228 | 11.2 | 0.32 | 2.61 | 0.47 | 0.16 |
| 8 | 523 | 11.4 | 0.38 | 3.85 | 0.42 | 0.20 |
| 10 | 987 | 11.2 | 0.32 | 5.21 | 0.39 | 0.15 |
| 12 | 1716 | 11.6 | 0.32 | 7.50 | 0.39 | 0.16 |

**Gate LRO:** ordena (m(ord)~0.4) ✓. **χ_max ~ N^0.516±0.054**, J_c **estável** (~0.32,
drift −0.007 ≈ 0), ξ/L~0.15–0.20 (ordem-1, estável). **Criticalidade genuína — NÃO
mean-field** (contraste nítido com as 7 famílias causais: x~0.07–0.24, J_c→0).

## 4. Comparação decisiva (λ fixo)

| | controle (reticulado) | foliado (λ=0.75) |
|---|---|---|
| χ_max ~ N^x | **0.592 ± 0.066** | **0.516 ± 0.054** |
| J_c drift | −0.000 (fixo) | −0.007 (≈fixo) |
| ξ/L em J_c | 0.10–0.14 | 0.15–0.20 |
| LRO | sim | sim |

`|Δx| = 0.076`, `σ_comb = 0.086` ⇒ **`Δx/σ = 0.89 < 2` ⇒ classes INDISTINGUÍVEIS.**
Ambos no mesmo intervalo (~0.5–0.6), **muito acima** do MF causal (0.07–0.24) e **iguais
entre si dentro do erro**.

> **Nota de honestidade (a armadilha do ruído, evitada):** com **4 seeds** o χ_max do
> foliado era não-monotônico (2.75, 2.70, 6.08, 3.18) e o ajuste dava x≈0.20 (falso "MF").
> Subindo para **8 seeds** o χ_max ficou monotônico (2.61→7.50) e o expoente subiu para
> 0.516 — o "MF" de 4 seeds era **ruído**, exatamente o trap noise-limited que
> `CDT_TEIC_FERRO`/`NESS` documentaram. O veredito robusto é o de 8 seeds.

## 5. Veredito e leitura

**`CRITICALIDADE DE RETICULADO CONHECIDA`.** O substrato foliado sustenta criticalidade
de 2ª ordem genuína (χ diverge, J_c estável, ξ/L ordem-1, LRO) — mas na **mesma classe de
universalidade que um reticulado regular puro**. **Não há assinatura nova de
Hořava–Lifshitz discreto.**

**Por que era esperado (prior do PRE_REGISTRO, confirmado):** o ferromagneto tem **só
acoplamento ferromagnético** (intra- e inter-fatia), **sem competição** ⇒ **não há ponto
de Lifshitz genuíno** ⇒ a anisotropia `λ` é **irrelevante no IR** para a classe. Um
substrato foliado de alcance espacial fixo é, para o parâmetro de ordem, um **reticulado
desordenado 3D** — classe 3D-Heisenberg. O "Hořava–Lifshitz discreto" não compra física
nova **neste setor** (parâmetro de ordem O(3) ferromagnético).

**Refina o entendimento (z alto ≠ MF):** o foliado tem `z≈11.5` (alto, como CDT) e MESMO
ASSIM **não** é MF — porque a conectividade é **local e de dimensão finita** (grafo
geométrico de raio fixo em 3D). Confirma que o MF das 7 mortes vinha da **não-localidade /
coordenação divergente / estrutura tipo-árvore-ou-Bethe**, NÃO da mera magnitude de z.
Um grafo 3D genuíno (curto alcance, z finito) dá criticalidade 3D — trivialmente.

**Funil:** como 2.3 deu classe **idêntica** ao reticulado, a **varredura de λ (2.4) NÃO
roda** (não há classe distinta para mapear vs λ — a expectativa de Lifshitz `z≠1` exigiria
acoplamentos competitivos, ausentes aqui). Decisão pré-registrada respeitada.

## 6. Posição no programa

Este é o desfecho honesto da linha foliada: ela **arma o gatilho** e **sustenta
criticalidade real** — mas a criticalidade é **mecânica estatística de reticulado
conhecida**, obtida **às custas da invariância de Lorentz**. Em uma frase: é um
**Heisenberg 3D (desordenado) empilhado com um rótulo de espaço-tempo** — não uma física
nova. O programa de "escala emergente de um substrato causal Lorentz-invariante"
permanece fechado (síntese das 7 mortes); a única saída estrutural (foliação) entrega
exatamente o que a mecânica estatística de reticulado já entregava, sem invariância de
Lorentz e sem novidade de classe.

## Arquivos
`PRE_REGISTRO.md` · `criticality.py` (controle + foliado, reuso VERBATIM) ·
`make_figure.py` · `criticality.json` · `criticality.png`.
