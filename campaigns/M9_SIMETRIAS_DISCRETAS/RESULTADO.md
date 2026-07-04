# M9 — CLASSIFICAÇÃO DAS QUEBRAS DE SIMETRIA DISCRETA: RESULTADO

**Data:** 2026-07-04 · **Pré-registro:** `PRE_REGISTRO.md` (bfe2e3f) ·
**Gate:** `gate_m9.py` → `gate_m9.json` (certificado de ação de simetria, VERDE) ·
**Natureza:** síntese analítica + certificado. 3º teorema da série de
classificação, após [[m5-classificacao]] / [[m6-hospedagem]] / M8 (topologia).

---

## 0. Veredito em uma página

**Uma simetria de espaço-tempo discreta é quebrável (mesmo espontaneamente) SE
E SOMENTE SE tem um CARRIER intrínseco** — um observável de $(\mathcal C,\prec,n)$
sobre o qual ela age não-trivialmente. O critério do carrier UNIFICA a
assimetria P-vs-T do programa sob um único mecanismo e certifica a hierarquia:
**P nunca (cinemático), T empírico, C dinâmico.**

| Simetria | Ação intrínseca (medida) | Carrier | Quebra |
|---|---|---|---|
| **P** | preserva a classe de ordem (20/20) — age como identidade | **NÃO** | inexprimível E espontânea impossível [teorema] |
| **T** | dualidade $\prec\leftrightarrow\succ$: troca in↔out (20/20), T-ímpar troca sinal (20/20) | **SIM** | quebrável; ⟨T-ímpar⟩→0 (auto-dual em lei); ausência = empírica |
| **C** | involução interna: C-ímpar troca sinal | **SIM** (interno) | quebra dinâmica (camada 3) |

## 1. O critério do carrier (o teorema)

**Enunciado.** Seja $S$ uma simetria discreta agindo sobre a configuração
intrínseca $(\mathcal C,\prec,n)$. Então $S$ é quebrável (explícita ou
espontaneamente) se e somente se existe um funcional intrínseco $S$-ímpar
não-nulo (um *carrier*). Se $S$ age trivialmente (é um automorfismo da
configuração), todo $S$-ímpar satisfaz $O=-O\equiv0$ e a quebra é inexprimível;
a quebra espontânea também é impossível, pois uma redundância não tem parâmetro
de ordem sobre o qual agir (mecanismo de Elitzur).

Este é o mecanismo ÚNICO por trás das três simetrias — e prediz que P e T,
ambas simetrias de espaço-tempo, têm destinos OPOSTOS: não porque P seja
especial, mas porque **reflexão espacial preserva a ordem causal (sem carrier)
e reversão temporal a dualiza (com carrier).**

## 2. Certificado (gate_m9.json, VERDE)

**(P) sem carrier.** Sob reflexão espacial $x\to-x$, a classe de isomorfismo de
ordem é preservada em **20/20** sprinklings, e ⟨P-ímpar⟩ = 21 ± 47 (compatível
com 0). Reflexão espacial é um isomorfismo de ordem ⟹ age como identidade nos
dados intrínsecos ⟹ nenhum funcional P-ímpar sobrevive. No-go cinemático,
fecha os dois canais (explícito e espontâneo).

**(T) com carrier.** Sob reversão temporal $t\to-t$, a ação troca in↔out
(dualidade de ordem) em **20/20**; o funcional T-ímpar intrínseco
$\sum_i(\mathrm{outdeg}_i^2-\mathrm{indeg}_i^2)$ é **não-nulo por causet**
(|T-ímpar| ~ 10⁵) e **troca de sinal sob dualidade 20/20** — o carrier existe.
Mas ⟨T-ímpar⟩ é compatível com 0 (a lei é auto-dual: a caixa $t\to-t$ é
simétrica), então em equilíbrio a assimetria não aparece. A quebra espontânea
NÃO é cinematicamente excluída — foi *medida ausente* (o eixo emerge, a seta é
input). Fechamento empírico, declarado.

**(C) com carrier interno.** A involução $U\to U^*$ (conjugação SU(2)) age
não-trivialmente no campo: o funcional C-ímpar troca de sinal exatamente
($\langle C\text{-ímpar}\rangle=-0.087\to+0.087$). C tem carrier interno ⟹ pode
quebrar dinamicamente (camada 3).

**Corolário CP.** Como P age trivialmente, $CP\equiv C$ operacionalmente;
qualquer violação de CP com conteúdo genuinamente P-emaranhado é input externo.

## 3. O alinhamento com o Modelo Padrão (observação, não derivação)

Os três setores quirais do MP — neutrinos, estrutura de gerações, setor de
calibre eletrofraco — são precisamente os três **sem carrier geométrico**. O
critério do carrier explica por que: chiralidade correlaciona algo interno com
o *handedness espacial*, e o handedness espacial não tem carrier na classe
(reflexão preserva a ordem). A quiralidade exata e nunca-restaurada do neutrino
é evidência estrutural contra qualquer origem de quiralidade em substrato causal.

## 4. O que muda no programa

1. **Nova linha C8 na checklist de restrições** ([[m7-paper-restricoes]]): "seu
   modelo quebra P/T/C só onde há carrier?". Junta de ataque: exibir funcional
   P-ímpar intrínseco não-nulo (quebraria o no-go de paridade).
2. **A Sec. de paridade + o P-vs-T do core_paper ganham teorema único:** o
   critério do carrier substitui as afirmações dispersas por um mecanismo com
   certificado. Delta de revisão.
3. **A série de classificação está completa em 3 eixos:** grupos (M6),
   substratos/fases (M5), topologias (M8), simetrias (M9) — a "teoria de
   restrições" tem suas colunas.

## 5. O que M9 NÃO reivindica (escopo)

- É a ação CINEMÁTICA das simetrias. A quebra dinâmica efetiva (C condensar; a
  seta T como input) é medida/dinâmica, não derivada — o lado T é empírico, como
  no core_paper.
- Não re-deriva os setores quirais do MP; observa que o critério do carrier os
  alinha.
- CPT do EFT emergente é assumido do contínuo (escopo do core_paper).
- Anti-circularidade: o funcional T-ímpar é INTRÍNSECO (só in/out-degree da
  ordem; a 1ª versão usava a coordenada t e foi corrigida pré-resultado — trilha
  no código); nenhum número do mundo.

## 6. Nota de instrumento (honestidade)

A 1ª versão do funcional T-ímpar usava a coordenada de embedding $t$, violando a
anti-circularidade e dando ⟨T-ímpar⟩ ≠ 0 espúrio. Corrigido pré-resultado para o
funcional intrínseco $\sum(\mathrm{outdeg}^2-\mathrm{indeg}^2)$ (só da ordem),
que dá per-causet não-nulo (carrier) + média compatível com 0 (auto-dual). A
ação de simetria (o resultado central: P trivial, T dual, C interno) nunca
dependeu disso.

*Reprodução:* `python gate_m9.py` (~30 s). numpy; causet explícito de M².
