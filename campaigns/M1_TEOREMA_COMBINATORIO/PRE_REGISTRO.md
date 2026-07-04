# M1 — TEOREMA COMBINATÓRIO: pré-registro

**Data:** 2026-07-02 · **Pasta:** `FRONTEIRA_COMPACTA/M1_TEOREMA_COMBINATORIO/`
**Linha:** ROADMAP_V2, Linha 1 (matemática), alvo nº 1. Analítico, ZERO código
(toys só para contraexemplo, declarados). Escrito ANTES de tentar as provas.

## Alvo

Transformar o lado COMBINATÓRIO do binário (hoje: padrão medido em 7 famílias)
em teorema(s): *"nenhuma ordem aleatória invariante carrega estrutura de laços
de dimensão finita"* — ou destruí-lo.

## Enunciados-candidatos (a provar OU destruir)

- **T1 (dobradiça, "laços forçam foliação"):** se o espaço de ciclos de um
  subgrafo conexo do diagrama de Hasse é GERADO por 4-ciclos, então existe
  função de rank (grading) nesse subgrafo — i.e., estrutura de plaquetas
  quadradas ⇒ foliação intrínseca. [candidato a teorema exato; é a recíproca
  matemática da dobradiça empírica das 7 mortes: "folhear arma C4"]
- **T2 (dicotomia exchangeable):** ordem aleatória exchangeable em ℕ ⇒
  comparabilidade densa ou vazia (Aldous–Hoover); mapear onde vive a valência
  finita nesse mundo.
- **T3 (box orders):** ordem de dominância sobre n pontos iid em [0,1]^d,
  d≥2 ⇒ valência de Hasse média Θ((log n)^{d−1}) → ∞ (a sombra abstrata da
  camada 1: exchangeable genuinamente ≥2-dim diverge).
- **T4 (confinamento de ciclos em crescimento covariante):** em transitive
  percolation (o exemplar CSG), posts têm densidade positiva [literatura] ⇒
  nenhuma aresta de Hasse cruza um post ⇒ TODO ciclo fica confinado num bloco
  finito ⇒ topologia de larga escala = caminho/árvore; sem condensação de
  laços em escala alguma > ξ(p). Corolário-retrodição: o platô sub-MF de C4 do
  CSG medido = ciclos intra-bloco.
- **Tricotomia organizadora:** valência ∞ (exchangeable/embutido d≥2) XOR
  ciclos confinados (crescimento/posts) XOR foliação intrínseca (graded/CDT) —
  com hipóteses nomeadas e o que restar de fora DECLARADO.

## Mortes pré-registradas

1. **T1 falhar:** um espaço de ciclos gerado por quadrados SEM função de rank
   (obstrução tipo-Möbius). ⇒ a dobradiça não é teorema; porta Wen reaberta.
2. **Contraexemplo geral:** ordem aleatória homogênea com valência de Hasse
   finita E espaço de ciclos 2-dimensional percolante (≥R² ciclos independentes
   no raio R) SEM grading. Candidato nomeado de antemão: construções
   **rank-frustradas** (geradores pentagonais, tipo N5) — se existirem
   homogêneas e 2D, T1 não as cobre. ⇒ descoberta maior, reabre Wen por uma
   porta NOVA (substrato pentagonal ≠ CDT).
3. Qualquer T_i destruído é reportado como resultado.

## O que M1 NÃO reivindica

Prova para "toda invariância" sem definir a classe — as classes são nomeadas
(exchangeable; crescimento covariante tipo RS; graded). O que escapar das três
é o flanco declarado do teorema, não letra miúda.
