# N5 / M2 — SKYRME_RADIATIVO: pré-registro

**Data:** 2026-07-02 · **Pasta:** `FRONTEIRA_COMPACTA/N5_SKYRME_RADIATIVO/`
**Charter:** `../CHARTER.md` §N5; **Roadmap:** `../ROADMAP_V2.md` item M2.
Escrito ANTES de qualquer código da campanha.

## Pergunta

Integrar as flutuações do campo interno SU(2) (1-loop gaussiano em torno de
fundos lentos) **gera** o termo de Skyrme com coeficiente efetivo — e, se gera,
o quártico **líquido** (árvore + loop) fica positivo em alguma janela da fase
ordenada (J ≥ J_c) com tamanho de Derrick λ* acima da granularidade?

## O que já é teorema (ponto de partida, não re-testado)

- **Árvore (SC1–SC3):** o 4º ordem do cosseno de link sob a média de Poisson é
  E⁽⁴⁾ = −(3a⁴/5760)·S + (a⁴/2880)·K, razão K:S = +2:−3 travada pela isotropia;
  razão B/A dos canais = 5/9 (medida 0.5552±0.0003 em SC2 e em links causais
  reais em SD3).
- **Dominância em árvore (SD1–SD5): MORTE por identidade pontual** —
  K ≤ (1−1/d)S (Cauchy–Schwarz no Gram PSD), quártico líquido
  −(a⁴/384)⟨|ℓ|⁴⟩ ≤ 0 sob QUALQUER medida de links. Não há regime clássico.
- O que NUNCA foi testado (Q20 do PERGUNTAS_II): a contribuição **radiativa**.
  A identidade pontual de SD1 governa a expansão da AÇÃO clássica; o ½ ln det
  das flutuações é um objeto novo, fora do alcance do teorema.

## A estrutura que decide (fixada antes de rodar)

Peso de Boltzmann e^{−J·E[U]}, E = Σ_links (1 − ½Tr(U_i†U_j)). Ponto de sela
com twist clampado: F(g) = J·E[Ū*(g)] + ½ ln det′ h[Ū*(g)] + O(1/J), onde
h = Hessiana de E (independente de J) e Ū*(g) é o mínimo restrito com fronteira
espacial clampada no fundo alvo. **A parte dependente de g do termo de loop é
independente de J** (ln det(J·h) = const + ln det h). Logo o quártico líquido
por nó no canal hedgehog é

  Q(J) = J·e₄_tree^B + α₄_loop^B,

decrescente em J (e₄_tree^B < 0 por SD1). Janela = (J_c, J_max),
J_max = α₄_loop^B / |e₄_tree^B| (se α₄_loop^B > 0). A física da campanha
inteira está em DOIS números medidos (α₄_loop^A, α₄_loop^B) e um terceiro já
conhecido em árvore.

## Previsões pré-registradas

1. **Esperado (do contínuo):** loops de Goldstone em modelos sigma geram
   operadores de 4 derivadas genericamente; a expectativa honesta é
   c_K^loop > 0 (canal de Skyrme gerado, sinal estabilizador) mas de tamanho
   O(1/16π²) por modo — **provável D2 ou D3 abaixo** ("emerge pequeno demais"),
   exatamente a morte parcial anunciada no charter. Esta expectativa é
   contextual, NÃO entra em nenhum fit.
2. **Sub-previsão de estrutura:** se o loop for apenas "árvore renormalizada",
   a razão α₄^B/α₄^A do loop cai em 5/9; desvio de 5/9 = estrutura radiativa
   NOVA (diagnóstico, não critério de morte).
3. **Controle cúbico:** a grade é cega a K em árvore (SC1). Se o loop gerar
   canal K na grade também, o efeito é universal (continuum); se só no
   Poisson, a isotropia gera o operador também radiativamente.

## Critérios de morte (antes de rodar)

- **D1 (morte total da rota radiativa):** c_K^loop ≡ (s₄^B − s₄^A)/6 ≤ 0
  dentro de 2σ (sem canal de Skyrme radiativo estabilizador), OU
  α₄_loop^B ≤ 0 (loop hedgehog já saturante ⇒ J_max ≤ 0).
  ⇒ Skyrme permanece [EXTERNO com prova], agora reforçado também no loop.
- **D2 (morte da janela):** c_K^loop > 0 mas J_max ≤ J_c (não existe J na fase
  ordenada com quártico líquido positivo).
- **D3 (morte parcial pré-registrada no charter):** janela existe mas
  λ*(J) < a_eff em TODA a janela (Skyrmion abaixo da granularidade).
- **SUCESSO:** janela com λ* ≥ a_eff em algum J ∈ (J_c, J_max)
  ⇒ Skyrme sobe de [EXTERNO-T] para [DERIVADO-radiativo]; teoria → 2 axiomas.
  **Ressalva declarada:** 1-loop é não-confiável em J ≈ J_c; se a janela
  existir apenas em J < 1.5·J_c, reportar como "SUCESSO
  PERTURBATIVAMENTE MARGINAL", não sucesso pleno.

Qualquer gate vermelho ⇒ consertar engenharia, nunca prosseguir ao veredito.

## Protocolo

### Substrato

- Sprinkling Poisson 3+1D, ρ=2, caixa [t: 0..4] × [espaço: 0..L]³,
  L=8 primário (8 seeds), L=10 secundário (4 seeds, tendência de volume).
  Grafo de Hasse via `causal_links` (mesmo código de FL1/N1, importado).
- **Controle cúbico:** rede periódica L_c=8³ (×4 réplicas de eixo temporal não —
  grade espacial 3D pura com os mesmos fundos estáticos; `lattice_periodic`),
  mesmo pipeline, clamps nas faces.
- a_eff ≡ comprimento ESPACIAL médio dos links de Hasse, medido por seed.

### Fundos (canais de SC2, agora como campos reais nos nós)

Coordenadas medidas do CENTRO da caixa espacial. Nós com distância < b = 1.0
de qualquer face espacial são CLAMPADOS no fundo alvo; interior relaxado
(Newton amortecido) até |∇E|_∞ < 1e−10. Fundos estáticos (sem twist no tempo).

- **Canal A (abeliano, K=0):** U_A(x⃗) = exp_q(ê₁ · g(x+y+z)/2)
  (c_x=c_y=c_z = g ê₁; S = 9g⁴, K = 0). Exato (correntes constantes).
- **Canal B (hedgehog-frame, K máximo a S casado):**
  U_B(x⃗) = exp_q((x ê₁ + y ê₂ + z ê₃) g/2) (S = 9g⁴, K = 6g⁴ no alvo;
  distorção O((g|x⃗|)²) do mapa exponencial é ABSORVIDA pela relaxação e
  vigiada pelo gate G3).

### Medidas e janelas (declaradas AQUI — lição max_tau=15)

- Grid de twist: g ∈ {0.04, 0.06, 0.08, 0.12, 0.16, 0.20, 0.24}, mais g=0.
- Árvore: E[Ū*(g)] restrita a links interior–interior, por nó livre;
  fit polinomial par grau 6 em g ⇒ e₂, e₄ por canal.
- Loop: ½[ln det h(g) − ln det h(0)] nos nós livres, por nó livre;
  mesmo fit ⇒ α₂, α₄ por canal.
- **Estabilidade de janela (critério):** α₄ deve mudar menos que 2× o erro
  combinado ao remover os DOIS maiores g do fit (mínimo 5 pontos). Falha ⇒
  encolher a janela superior e documentar; nunca alargar.
- Erros: espalhamento entre seeds (média ± sem); "compatível com 0" = |média| < 2·sem.
- Decomposição de canal: s₄ ≡ α₄/g⁴ por nó livre; c_S^loop = s₄^A/9;
  c_K^loop = (s₄^B − s₄^A)/6 (S casado por construção, vigiado por G3).

### Gates de engenharia (Fase 0, obrigatórios)

- **G0 (derivadas):** gradiente e Hessiana analíticos vs diferenças finitas
  em configuração aleatória: erro relativo < 1e−6.
- **G1 (zero-modes):** sem clamps, h do vácuo tem EXATAMENTE 3 autovalores
  |λ| < 1e−10×mediana (multiplicação global à esquerda) e é PSD; com clamps,
  λ_min > 0.
- **G2 (dois algoritmos de ln det):** Cholesky vs soma de ln de autovalores,
  |Δ| < 1e−8 relativo, num caso de cada canal.
- **G3 (âncora de árvore):** razão e₄^B/e₄^A dos fundos RELAXADOS na janela
  de fit = 5/9 ± 15% (âncora SC2/SD3). Vigia simultaneamente o casamento de S
  e a distorção do mapa exponencial.
- **G4 (null abeliano):** canais A construídos em ê₁ vs ê₂: |α₄(ê₁)−α₄(ê₂)|
  compatível com 0 (simetria exata do pipeline).
- **G5 (J_c):** motor `sun_core` (N1, validado) instanciado em N=2 sobre o
  MESMO grafo: J_c localizado pelo pico de χ num grid J ∈ {0.05, 0.1, 0.2,
  0.3, 0.5, 1.0, 2.0}, 4 seeds; fase desordenada exposta em J ≤ 0.05.
  Esperado J_c = O(0.1–0.5) (SU(3) causal deu ≈0.3). τ_int/ESS reportados.

### Fase 3 (condicional — só se janela existir)

Quadratura radial hedgehog F = π e^{−r/λ} (funcional de SC4): densidades
E₂ = F′² + 2sin²F/r², S = (F′² + 2sin²F/r²)², K = (2sin²F/r²)(2F′² + sin²F/r²),
com coeficientes líquidos (árvore·J + loop medido); λ*(J) na janela;
critério λ* ≥ a_eff.

## Higiene N-hig (declarada)

- **τ_int/ESS:** a medida PRINCIPAL não tem cadeia MC (determinante gaussiano
  determinístico por seed) — justificativa declarada. O único MC é o gate G5
  (J_c), que reporta τ_int (janela de Sokal) e ESS por (J, seed), verbatim N1.
- **Dois algoritmos:** ln det por Cholesky E por autovalores (G2); relaxação
  verificada por gradiente final e por decrescimento monotônico de E.
- **Segundo operador BD:** N/A (nenhum d'Alembertiano discretizado nesta
  campanha) — declarado.
- **Janelas de estimador:** grid de g, grau do fit, regra de estabilidade,
  margem de clamp b, tolerância de G3 — todos fixados acima, antes de rodar.

## ADENDO (02jul26, pós-G3-vermelho, ANTES de qualquer medida de loop válida)

O gate G3 do instrumento clampado FALHOU (razão de árvore B/A = −1.31 no
Poisson, 4.35 no cúbico): em grafo irregular, o clamp de fronteira injeta
forças O(g) de ruído-de-grafo e a resposta de relaxação domina/contamina o
quártico (diagnóstico: relaxação remove ~40% da energia já em O(g²), e trata
A≠B). MUDANÇA DE INSTRUMENTO declarada (permitida pré-veredito):

- **Substrato → toro espacial** [0,4]×(ℝ/L)³, relação causal por distância
  mínima-imagem (sem fronteira). Tamanhos L ∈ {6, 8} (8 seeds cada; L=8
  primário). L=10 abandonado por custo de memória do denso (documentado).
- **Twist → transportadores de link** Ω_ij = exp_q(g·C·δ⃗_ij) (min-image):
  realiza EXATAMENTE a estatística de links de SC1 em U≡1; em U≡1 a energia
  bare é Σ(1−cos(|v|/2)) — o cosseno de SC1, aritmética exata.
- **Pino em 1 nó** (nó 0) no determinante e na relaxação (mata os 3 modos
  globais com artefato mínimo; sem clamps).
- **Árvore dupla:** BARE (U≡1; âncora G3: razão B/A = 5/9 por isotropia dos
  links reais, e fit≡soma direta na máquina) e RELAXADA (vestida pelo meio
  desordenado — a fisicamente relevante). **Q(J) e J_max usam a árvore
  RELAXADA** (declarado agora, antes de medir o loop no instrumento novo);
  a bare é reportada como comparação com SC1/SD.
- G1 → 3 zero-modes sem pino / λ_min > 0 com pino. Controle cúbico →
  rede periódica (mesma blindness exata a K na árvore bare).
- Critérios D1–D3, definição de Q(J), grid de g, fits, regra de
  estabilidade, seeds: INALTERADOS.
- G5 (J_c): grid refinado {0.05, 0.06, 0.07, 0.08, 0.09, 0.10, 0.12}
  (o grid original localizou J_c ∈ (0.05, 0.1) — pico fora da malha),
  substrato torus, 200 medidas.

## Anti-circularidade

- O operador de Skyrme NUNCA é alvo de fit: os fits são polinômios pares em g
  da energia e do ln det; K só aparece na DECOMPOSIÇÃO algébrica declarada.
- A razão 5/9 entra apenas como GATE de árvore (âncora já publicada), não como
  prior do loop. A expectativa contínua (previsão 1) não entra em nenhum número.
- Nenhum número de QCD/física; aritmética real (quaternions); seeds fixas;
  JSON com metadados; toys fora do protocolo proibidos.
- Ajustes de engenharia (tamanho de caixa, margem b, janela de g via regra de
  estabilidade) são permitidos ANTES do veredito e documentados; os critérios
  de morte D1–D3 e a definição de Q(J) são imutáveis.
