# N3 — WEN_COMPLEMENT: resultado

**Data:** 2026-07-02 · **Pasta:** `FRONTEIRA_COMPACTA/N3_WEN_COMPLEMENT/`
**Gate:** N0(c) ✓ (enunciado de assinatura) + N0′ ✓ (stress test adversarial) —
conforme o charter, publicado só após ataque.
**Entregável:** `wen_complement.tex/.bib` → `wen_complement.pdf` (4 páginas,
revtex4-2 PRD reprint, compila limpo com pdflatex+bibtex).

## O paper

**"Why Lorentz-invariant causal sets cannot support an emergent U(1): a causal
complement to string-net theory"** — paper de perspectiva curto, o raro paper
que EXPLICA UM NEGATIVO. Estrutura:

1. **Dois programas de emergência que nunca se encontram** — string-nets
   (Wen/Levin: fótons emergem de laços em rede) vs causal sets (cinemática
   Lorentziana recuperada, nenhum fóton emergente jamais).
2. **O que a luz emergente exige** (3 requisitos): valência finita; laços de
   dimensão finita (com a ressalva Polyakov: necessário, não suficiente);
   2-célula tipo-espaço orientada para B.
3. **O que o substrato causal recusa, camada por camada:**
   - Camada 1 [teorema]: ⟨z⟩=∞ forçado (Campbell–Mecke em H^{d−1},
     eq. central do paper; fecha não-pairwise via Palm; N(i,j)=Δτ disfarçado).
   - Camada 2 [medido]: o binário das 7 mortes (Matérn-s², percolação-Δτ,
     CSG, CDT-like 2D/3D/stacked, foliado-Hořava) — valência finita OU laços,
     nunca ambos; o foliado passa as duas barreiras QUEBRANDO Lorentz e cai na
     classe de rede espacial conhecida (0.89σ).
   - Camada 3 [teorema+medido]: a 2-célula magnética não tem portador (Lema 0:
     tempo com sinal, espaço sem sinal/estrutura; antichains amorfas; diamantes
     100% elétricos; frac_B∝H² agora derivado por paridade-T).
4. **A fronteira é a assinatura** (N0c): definida (órbita = esfera, divergência
   ESCOLHIDA) vs indefinida (toda quádrica não-compacta, divergência FORÇADA);
   Wick rotation = a operação que compactifica o grupo; uma ordem não pode
   rotacionar e continuar ordem. Precedente de Wigner (o mesmo H^{d−1}).
5. **Consequências:** o que um programa de fóton emergente precisa quebrar
   (com as 3 juntas nomeadas = falseabilidade); a face entrópica nova de N2
   (geometria lei-de-área vs matéria super-área — a MESMA fronteira).
6. **Escopo e aberturas declaradas:** teorema sobre a CLASSE, cinemático;
   camada 1 rigorosa até a relação de cobertura; teorema combinatório pendente
   (medido, não provado); geometria dinâmica = flanco aberto.

## Disciplina editorial cumprida

- Regra do charter ("teorema sobre a classe, nunca 'a Natureza obedece'"):
  §Scope explícito, comparação com o caráter cinemático de Wigner.
- Todos os inputs medidos citados como companion papers (MatterGravityPRD,
  SU3PRD) + literatura externa real (Levin–Wen, FNN, Polyakov, BLMS, BHS,
  Malament-linha via Surya, Dou–Sorkin, Barton et al.).
- Ressalvas de N0′ incorporadas (Palm/covering na camada 1; flanco dinâmico).
- N2 entrou como "face entrópica" — o paper ganhou um resultado novinho que
  nenhuma versão anterior do argumento tinha.

## Status

RASCUNHO COMPLETO compilado. Decisão de submissão (venue: perspectiva em PRD /
Classical & Quantum Gravity / essay) é decisão humana — fora do escopo da
campanha. A linha FRONTEIRA_COMPACTA atinge seu critério de encerramento
(N0 respondido + N1 + N2 executados) COM o paper-síntese pronto.

*Reprodução:* `pdflatex wen_complement && bibtex wen_complement && pdflatex ×2`.
