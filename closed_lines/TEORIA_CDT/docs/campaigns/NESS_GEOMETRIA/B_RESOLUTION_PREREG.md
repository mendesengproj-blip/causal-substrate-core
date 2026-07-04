# PRÉ-REGISTRO — Resolução da Pergunta B: varredura de amplitude x(A)

> **Congelado ANTES de medir.** Data: 2026-06-29. Follow-up direto do `SYNTHESIS.md` (B
> NÃO-RESOLVIDO: χ_max~N^0,53 — dobro do equilíbrio mas no limiar MF, J_c derivando). Reusa
> `ferro_cdt.question_B` + `driven_cdt` + `cdt_substrate` verbatim. Sem reimplementar.

## A pergunta afiada
χ_max~N^0,53 (sob NESS, A=1,5) é **realce genuíno do não-equilíbrio** ou **MF com ruído**? O
discriminante decisivo e barato: o expoente **escala com a intensidade do drive A**?

## O experimento (congelado)
Varrer **A ∈ {0,0; 0,75; 1,5; 2,25}** com TODO o resto fixo (k̄₀=2,5, P=8, T=10; mesma suíte
`question_B`). Para cada A, medir o expoente **x(A)** de χ_max~N^x em 3 volumes (1500/3000/6000) e
a **deriva de J_c(N)**. **A=0 = controle de equilíbrio embutido** (deve recuperar x≈0,24 do
CDT-equilíbrio — sanidade do pipeline).

## Predições pré-registradas (sem ajuste posterior)
- **ESCAPE genuíno (NESS mecanístico):** x(A) **cresce monotonicamente** com A (de ~0,24 em A=0
  rumo a >0,53), **E** a deriva de J_c **diminui** com A (drift→0 = aproximação a ponto-fixo de
  criticalidade). → resolve B para **escape**, reabre o programa.
- **MEAN-FIELD (ruído):** x(A) **plano/disperso** (~0,3–0,5 sem tendência clara em A), J_c segue
  derivando em todo A. → resolve B para **MF**: a barreira de alta-coordenação (z~13) é robusta a
  equilíbrio **E** não-equilíbrio. → **fecha o programa de escala** (combina com FS-3D +
  MEMORIA_DIAGNOSTICO); parar passa a ser a escolha honesta.
- **Ambíguo persistente:** se x(A) sobe mas J_c não converge, ou as barras não separam — reportar
  ainda NÃO-RESOLVIDO e o que falta (tamanhos maiores). Não forçar.

## Anti-circularidade
A é `[External]` (declarado). O teste é a **dependência estrutural x(A)**, não um número que
emerge. A=0 ancora no equilíbrio conhecido.
