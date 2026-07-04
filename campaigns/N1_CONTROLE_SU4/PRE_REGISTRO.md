# N1 — CONTROLE_SU4: pré-registro

**Data:** 2026-07-01 · **Pasta:** `FRONTEIRA_COMPACTA/N1_CONTROLE_SU4/`
**Charter:** `../CHARTER.md` §N1. Escrito ANTES de qualquer código da campanha.

## Pergunta

O substrato causal seleciona SU(3) ou hospeda qualquer grupo compacto?

## Previsões pré-registradas (do charter, tornadas operacionais)

- **A (esperada):** SU(4) funciona igual — ordena a J_c finito com LRO genuína
  (Mermin C_long=m²), 15/15 modos de Goldstone sem gap, Skyrmion B=±1 inteiro
  (π₃(SU(4))=ℤ, Bott), confinamento a acoplamento forte (Creutz σ>0) com σ(β)
  decrescente. ⇒ "SU(3) é HOSPEDADO, não emergente; o 3 é escolha do mundo."
- **B (descoberta):** qualquer quebra (não ordena; 15-pleto não degenera; B não
  inteiro; desconfina) ⇒ seleção escondida ⇒ vira prioridade do programa.
- **Sub-previsão de escala (fraca, não é critério):** J_c(SU4, causal) desloca de
  J_c(SU3)≈0.3 por fator ≲2 (dim do alvo 15 vs 8; mesma coordenação alta ~45).

**Critério de morte da campanha:** NENHUM (as duas saídas informam) — conforme o
charter. O que pode morrer é o GATE (abaixo): sem gate verde, nada de SU(4).

## Gate de engenharia (anti-bug, obrigatório antes de SU(4))

Motor GENERALIZADO `sun_core.py` (SU(N) qualquer, base de Gell-Mann generalizada,
Tr(T_aT_b)=2δ_ab) instanciado em N=3 deve reproduzir o FL1 medido:

1. **J_c(causal) ≈ 0.3**: pico de χ no grid em J ∈ [0.2, 0.5]; fase desordenada
   exposta em J ≤ 0.1 (m ≲ 3/√N); LRO (winner `const`) para todo J ≥ 0.5.
2. **Mermin:** |C_long − m²|/m² < 0.10 nos J ordenados.
3. **Confinamento SU(3):** no setor de gauge L=6, β=4.5 (config FLC quick),
   Creutz χ(2,2) > 0.05 e V(r) crescente.
4. **Álgebra:** para N=3 a base generalizada satisfaz Tr(T_aT_b)=2δ_ab (err<1e-12)
   e f_123=1 (mesmas constantes de estrutura do su3_core, a menos de ordenação).

Gate FALHA ⇒ consertar motor, nunca rodar SU(4) com gate vermelho.

## Protocolo SU(4) (verbatim da suíte SU(3), N=4)

- **Substrato:** idêntico ao FL1 — sprinkling Poisson 3+1D ρ=2, caixa
  [(0,24),(0,3)³] (escala quick do FLB), grafo de Hasse (`causal_link_graph`
  IMPORTADO de su3_core, mesmo código), C(r) por cadeia-mais-longa.
- **Ordenamento:** J ∈ {0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.7, 1.0, 2.0}, 4 seeds,
  burn 500 (adaptativo), 120 medidas a cada 2 sweeps. Medir m, χ, U₄ (Binder),
  E/link, C(r)+classificador. Grid SU(3)-gate: {0.05,0.1,0.2,0.3,0.5,1.0,2.0}.
- **Goldstones:** teste de twist estático (protocolo D2 do FLD, verbatim): vácuo
  alinhado U₀, twist exp(i k x T_a) por gerador, dE(k)→0 com dE~ρ_s k² ⇒ sem gap.
  Esperado: 15/15 (dim SU(4)). Grid L=14, k = 2πn/L, n=1,2,3.
- **Topologia:** hedgehog SU(2)⊂SU(4) (bloco 2×2 superior), L=21: B=+1 (e B=−1
  p/ anti). Derrick radial com e_sk=0.5 (funcional radial idêntico — embedding).
- **Gauge/confinamento:** L=6⁴, β escalonados por 2N/g²: β₄ = β₃ × (16/9) →
  {8.0, 10.7} (quick FLC ×16/9), 60 sweeps térmicos + loops r,t ≤ 3, V(r) e
  Creutz χ(2,2). Esperado: σ>0 no β forte, σ(β) decrescente.

## Higiene N-hig (obrigatória, declarada aqui)

- **τ_int/ESS:** τ_int da série de m por janela de Sokal (soma de ρ(t) até
  ρ<0), ESS = n_meas/(2τ_int); reportar por (J, seed) no JSON; alertar ESS<20.
- **Dois algoritmos:** NÃO — justificativa declarada: o motor usa o MESMO
  Metropolis colorido vetorizado do FL1 (validado contra âncora cúbica de
  literatura J_c≈2.65 e contra E1); a campanha é um CONTROLE comparativo onde
  usar exatamente o mesmo updater é uma feature (qualquer viés cancela na
  comparação SU(3)↔SU(4)). Cross-check independente = consistência hot/cold nos
  pontos ordenados do gate.
- **Janelas de estimador (lição max_tau=15):** classificador C(r) verbatim FL1
  (`fit_forms`: r_lo=2, platô = média da metade externa, LRO se C_long>0.05 e
  C_long/C_mid>0.85); R_CAP=24; MIN_COUNT=200; τ_int com janela automática, sem
  corte fixo. Todos declarados AQUI, antes de rodar.

## G₂ (segundo controle, GATED)

Só se SU(4) passar limpo (previsão A). G₂ tem centro TRIVIAL ⇒ discrimina se o
confinamento medido depende do centro Z(N). Implementação (7×7 real, 14
geradores via octonions) é campanha própria — NÃO nesta sessão; registrado.

## Anti-circularidade

Nenhum número de QCD/física entra; β e J varridos; σ, J_c, contagens MEDIDOS.
A previsão de 15 Goldstones é teoria de grupos (dim SU(4)), não input dinâmico.
Seeds fixas; JSON com meta. Toys/exploração fora do protocolo: proibidos.
