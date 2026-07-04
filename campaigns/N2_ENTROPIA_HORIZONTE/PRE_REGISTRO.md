# N2 — ENTROPIA_HORIZONTE: pré-registro

**Data:** 2026-07-02 · **Pasta:** `FRONTEIRA_COMPACTA/N2_ENTROPIA_HORIZONTE/`
**Charter:** `../CHARTER.md` §N2. Escrito ANTES de qualquer código da campanha.
**Ancoragem declarada:** a contagem de links de horizonte é linha conhecida da CST
(Dou–Sorkin, "moléculas de horizonte") — a fase 1 REPRODUZ a forma no nosso
substrato com protocolo próprio; a novidade do programa é a fase 2 (matéria).

## Pergunta

S ∝ A emerge por contagem de estruturas causais atravessando um horizonte de
Rindler no sprinkling de Poisson? (Fase 2, gated: e a entropia configuracional do
ferromagneto — o vácuo do programa — através do mesmo horizonte?)

## Setup geométrico (declarado)

Sprinkling de Poisson em caixa de M^d (d = 2, 3, 4), coordenadas (t, x, y⃗_⊥):
- **Horizonte** H: plano nulo u ≡ t − x = 0.
- **Corte** Σ: fatia t = 0. A superfície de entropia é o CANTO (codim-2)
  H ∩ Σ = {t=0, x=0}, de "área" A = L^{d−2} (extensão transversal da caixa).
- **Transversal PERIÓDICA** (mín-imagem em y⃗_⊥): remove efeito de borda
  transversal por construção; a contagem fica estritamente proporcional a A se a
  lei de área valer.
- Quadrantes: W_p = {u<0, t<0} (lado externo, passado do corte);
  B_f = {u>0, t>0} (lado interno/futuro).

## Contagens (declaradas ANTES de rodar — janelas de estimador N-hig)

1. **N_link (ingênua):** # de links de Hasse i→j (relação de cobertura, teste de
   linkness contra TODO o sprinkle) com i ∈ W_p e j ∈ B_f — cruza o plano nulo E
   a fatia ⇒ localiza no canto por construção. *Expectativa declarada:* PODE ser
   dependente da caixa (não-localidade conhecida dos links CST ao longo do cone);
   reportada como comparação, NÃO é critério de morte.
2. **N_mol (molécula, à la Dou–Sorkin):** o mesmo, com i MAXIMAL em W_p (sem
   sucessor dentro de W_p) e j MINIMAL em B_f (sem predecessor dentro de B_f).
   *Este é o objeto da lei de área.*
3. **N_rel (relações):** # de pares causais i≺j (não só links) cruzando o canto —
   comparação; expectativa: não-lei-de-área (não-local), cresce com a caixa.

## Grades (fixadas agora)

- d=4: ρ=8, t,x ∈ [−2.5, 2.5], L ∈ {1.5, 2, 3, 4}, 12 seeds.
  Checagem-T em L=3: t,x-extensão ∈ {±2.0, ±2.5, ±3.5}.
- d=3: ρ=10, t,x ∈ [−3, 3], L ∈ {2, 3, 4, 6, 8}, 12 seeds.
- d=2: ρ ∈ {10, 20, 40, 80}, t,x ∈ [−4, 4], 16 seeds (não há transversal:
  previsão = contagem CONSTANTE, um número puro, independente de ρ e da caixa).

## Previsões pré-registradas e critérios

- **P-forma (a tese):** N_mol ∝ A: expoente de log N_mol vs log L igual a
  d−2 ± 0.3 (d=4: 2±0.3; d=3: 1±0.3), E independência-T (variação da extensão
  t,x muda N_mol por menos que 3σ combinado). d=2: N_mol constante
  (|expoente vs ρ| ≤ 0.15).
- **P-coeficiente:** a_d ≡ N_mol/(L^{d−2} ρ^{(d−2)/d}) é adimensional e converge;
  o VALOR é medido e reportado como número de rede — o 1/4 (ℓ_P) fica EXTERNO,
  como toda escala do programa. Secundário: expoente de ρ em d=4 = 0.5 ± 0.15.
- **MORTE (fase 1):** N_mol com expoente incompatível com d−2 (ex.: compatível
  com d−1, "lei de volume") OU N_mol crescendo com a extensão-T (não é
  propriedade do canto). Se disparar: primeira falha da tese "formas derivam" —
  reportar com prioridade MÁXIMA (mais informativo que o sucesso).

## Fase 2 — matéria (GATED: só roda se a fase 1 der lei de área limpa)

Ferromagneto do programa (SUNChiralModel N=2 do motor N1, = setor de orientação)
sobre o grafo de Hasse do MESMO sprinkling d=4, fase ordenada J=1.0 (e controle
desordenado J=0.05). **Estimador declarado:** informação mútua Gaussiana entre os
blocos A = {sites: −0.5<u<0, |t|<1.0} e B = {0<u<0.5, |t|<1.0} (lajes junto ao
canto), sobre UMA componente interna (simetria ⇒ todas iguais):
I_G = −½ ln det(I − Σ_AA^{−1}Σ_AB Σ_BB^{−1}Σ_BA), covariâncias de amostras MC
(burn 500, 3000 medidas a cada 2 sweeps, τ_int/ESS reportados).
- Grade: L ∈ {2, 3, 4}, ρ=4, 4 seeds.
- **Previsão:** I_G ∝ A (I_G/L² constante em L, ±40% — estimador de MI é
  ruidoso, tolerância declarada); controle desordenado I_G ≈ 0 (< 20% do
  ordenado).
- **Morte (fase 2):** I_G claramente super-área (compatível com ∝L³) ou controle
  desordenado ≥ ordenado (estimador inválido ⇒ reportar como INCONCLUSIVO, não
  morte).

## Higiene e anti-circularidade

Seeds fixas; JSON com meta; erros = SEM sobre seeds; fits em log-log OLS
ponderado. Nenhum número físico entra (nem 1/4, nem ℓ_P); coeficientes MEDIDOS.
τ_int/ESS na fase 2 (fase 1 não tem MC — contagem determinística por seed).
2º algoritmo (fase 2): mesma justificativa declarada de N1 (updater validado;
controle comparativo) + controle desordenado como cross-check.
