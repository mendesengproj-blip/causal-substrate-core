# PRÉ-REGISTRO — Criticalidade genuína sobre FOLIACAO_ANISOTROPICA

> # ⚠️ **ESTE SUBSTRATO NÃO É MAIS LORENTZ-INVARIANTE MANIFESTO.**
> Foliação preferida + distância intra-fatia (Hořava–Lifshitz discreto). Nenhum
> resultado desta linha muda isso. Rótulo obrigatório em todo documento/código/figura.

**Data:** 2026-06-30 · **Critérios travados ANTES de rodar.** Não se ajustam após ver dados.

## 1. Pergunta

O substrato foliado (que armou o gatilho cinemático) sustenta **criticalidade genuína
com classe de universalidade DISTINTA do reticulado puro** (assinatura de Hořava–Lifshitz
discreto), ou é apenas a física conhecida de um Heisenberg/Ising em reticulado regular
empilhado (mesma classe, sem nada novo)?

> **Prior honesto (registrado antes):** o ferromagneto O(3) tem **só acoplamento
> ferromagnético** (intra- e inter-fatia), sem competição ferro/antiferro ⇒ **não há
> ponto de Lifshitz genuíno** ⇒ a expectativa teórica é **classe 3D-Heisenberg padrão**,
> idêntica ao reticulado. A anisotropia `λ≠1` é, para acoplamento puramente ferromagnético,
> **irrelevante no IR** (não muda a classe). Mede-se para confirmar, não para assumir.

## 2. Reuso VERBATIM

`xi_suite.measure_point` / `locate_Jc` / `build_lattice_3d` (controle positivo) e
`orientation_core` (O3Model, Graph). Única novidade: `build_foliated_fss(m, λ)` — o
substrato foliado em modo FSS (densidade fixa `ρ_s=1`, `k_intra=6`; lado linear `m`
crescente; `T=m` fatias ⇒ `N~m³`, comparável ao reticulado `m×m×m`).

## 3. Estrutura (funil)

- **2.1 Controle (PRIMEIRO):** reticulado cúbico 3D, `build_lattice_3d`, ladder
  `m∈{6,8,10,12}`, J em torno de 0.69. Deve reproduzir 3D-Heisenberg (χ_max~N^~0.66,
  U₄ cruza, ξ/L cresce). **Anchor.**
- **2.2 Foliado em λ=0.75 FIXO:** mesma suíte, J em torno de 0.27 (J_c localizado em
  probe). **Gate:** confirmar que o ferromagneto **ordena** (LRO, `m(ordenado)>0.3`)
  antes de ler criticalidade.
- **2.3 Comparação decisiva (λ fixo):** expoente `χ_max~N^x` (ajuste log-log +
  jackknife leave-one-size-out p/ erro), drift de J_c, cruzamento de U₄, forma de ξ/L.
- **2.4 Varredura de λ:** **SÓ se 2.3 mostrar classe distinta.** Senão, não roda.

## 4. Critérios de veredito (TRAVADOS)

Discriminador primário = expoente `x` de `χ_max ~ N^x` (a base do tripé da ESCALA_XI;
ξ/L é suporte ruidoso por Goldstone, U₄ é cruzamento qualitativo).

- **HOŘAVA-LIFSHITZ DISCRETO COM FÍSICA NOVA:** foliado ordena (LRO), ξ diverge, e o
  expoente é **distinto do controle fora de 2σ combinados** (`|x_c − x_f| > 2√(σ_c²+σ_f²)`).
  ⇒ (e só então) rodar 2.4 (varredura de λ) p/ ver se a classe varia com λ (expoente de
  Lifshitz).
- **CRITICALIDADE DE RETICULADO CONHECIDA:** foliado ordena, mas `x_f` **indistinguível**
  de `x_c` (dentro de 2σ). Reportar com este rótulo — **mesmo que ξ divirja**. Não inflar.
- **MEAN-FIELD:** `x_f < 0.5` **e** J_c deriva p/ baixo (`<−0.02`) — replica as 7 famílias.
- **SEM_LRO:** o ferromagneto não ordena no foliado (gate falha).
- **AMBÍGUO:** não-resolvido, com N estimado p/ resolver. Não forçar.

## 5. O que NÃO se faz

Divergência de ξ **sozinha não é sucesso** — o critério é divergência **com classe
distinta do reticulado**. Não varrer λ antes de 2.3 decidir. Não remover o rótulo em
negrito. "Classe idêntica" **não é fracasso** — é a distinção que a tarefa existe p/ fazer.
