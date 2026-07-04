# N4 — Fase 0 (analítica): âncoras conferidas, Lema Q0, congelamentos

**Data:** 2026-07-02 · **Pré-registro:** `PRE_REGISTRO.md` §3 (executado conforme).
**Natureza:** zero código. Literatura conferida NA FONTE (PDFs lidos, fórmulas
extraídas verbatim), não de memória. Este documento CONGELA o que o pré-registro
mandou congelar e registra dois ajustes de escopo/prior — ambos declarados AQUI,
antes de qualquer código da campanha (higiene bayesiana legítima; o contrário —
ajustar depois de rodar — é o que a lição max_tau=15 proíbe).

---

## 0. Veredito da Fase 0 em cinco linhas

1. **Todas as âncoras existem e foram conferidas na fonte** (tabela §1, com
   fórmulas exatas). Nenhuma contradiz o desenho da campanha.
2. **Lema Q0 FECHA como teorema** (§2): a porta-ℏ custa exatamente 1 bit (a
   escolha retardado/avançado ≡ dualização da ordem); trocá-lo conjuga o vácuo
   SJ (anti-unitário); observáveis pares independem dele. Consistência
   EXP2+GOE confirmada; D-Q0 bem-posta.
3. **Q2-forte enunciada com precisão** (§3); resposta esperada NÃO (delimitação),
   com o mecanismo nomeado (não-degenerescência genérica do espectro).
4. **O joelho de d=4 NÃO é o de d=2** (achado da Fase 0, §4): a literatura mostra
   que o critério analítico 2D (λ̃_min = √N/4π) não generaliza, o esquema de
   detecção-de-inclinação FALHA em M⁴ plano (dá volume), e o que funciona em M⁴
   é truncamento de NÚMERO n_max = αN^{(d−1)/d}. **Congelado: número, α=1,
   duplo.** A circularidade da literatura (esquemas selecionados POR produzirem
   área) é declarada e é exatamente o que nosso congelamento-prévio corta.
5. **Dois ajustes pré-código declarados** (§5): M3.1 rebaixada de medição para
   REPRODUÇÃO (a lei de volume sem truncamento já é resultado da literatura,
   com o NOSSO mecanismo — não-localidade — citado como causa); prior de M3.2
   atualizado de 50/50 para ~60/40 pró-área (M⁴ aninhado recuperou área com
   α=1). O que permanece genuinamente nosso em Q3 está listado em §5.2.

---

## 1. Tabela de âncoras conferidas (entregável 1 do pré-registro)

| # | Âncora | Enunciado exato conferido | O que nossa reprodução deve bater |
|---|---|---|---|
| A1 | **Johnston d=2** [arXiv:1010.5514; conferido em 2008.07697 eq. (23)] | G_R^(2) = ½ C (I − (m²/2ρ) C)^{−1}, C = matriz causal. Massless: G_R = ½C | Gate G1/G3: construção de iΔ e controle massivo |
| A2 | **Johnston d=4** [idem, eq. (24) + p.23] | G_R^(4) = aL(I − baL)^{−1}, a = (1/2π)√(ρ/6), b = −(1/ρ)(m² + ξR); plano: b = −m²/ρ. L = matriz de links | Fase 1 d=4: iΔ do escalar |
| A3 | **Pauli–Jordan e vácuo SJ** [2008.07697 eqs. (21)–(28)] | iΔ = i(G_R − G_A), G_A = G_R^T; iΔ auto-adjunto, Hilbert–Schmidt em volume finito (‖iΔ‖²_HS = 2L⁴ no diamante 2D, ABDRSY eq. 4.2); espectro em pares ±λ_k; **W_SJ ≡ Pos(iΔ) = Σ_k λ_k u_k u_k†** | Gate G1 (pares ±λ à máquina); definição única de W em todas as fases |
| A4 | **ABDRSY centro do diamante 2D massless** [arXiv:1207.7101 eqs. (4.16)–(4.17)] | W_centre = −(1/4π)ln\|ΔuΔv\| − (i/4)sgn(Δu+Δv)θ(ΔuΔv) − (1/2π)ln(π/4L) + ε_centre, com **ε_centre ≈ −0.063**; = vácuo de Minkowski com corte IR DEFINIDO **λ_IR ≈ 0.46/L**. No CANTO: vácuo de espelho estático (não-Rindler). Confirmado em causet no próprio paper | **Gate G2 congelado:** fit da forma real acima na janela de bulk, R² > 0.9; constante IR comparada a 0.46/L |
| A5 | **Fewster–Verch / Brum–Fredenhagen** [arXiv:1307.5242 e refs.] | SJ em slab ultrastático com seção espacial compacta NÃO é Hadamard; suavização BF restaura Hadamard | Caveat estrutural declarado (§4.4): nossos observáveis (espectros, ridge de dispersão, SSEE) não requerem Hadamard; slab-sobre-toro da Fase 1 é EXATAMENTE o cenário FV |
| A6 | **Surya–X–Yazdi, SJ em dS (causet d=2,4)** [arXiv:1812.10228] | vácuo SJ de causet bem-definido para todo m ≥ 0 (inclusive massless minimal, mal-definido no contínuo); em dS₄ o vácuo SJ do causet é dS-invariante mas **difere de todos os α-vácuos de Mottola–Allen** (desvio contínuo-vs-causet em d=4) | Prior para M1.4 (desvio UV em d=4 é esperado e conhecido); reforça que d=4 não é extrapolação trivial de d=2 |
| A7 | **Sorkin–Yazdi, SSEE em diamantes aninhados M²** [arXiv:1611.10281 §3] | Sem truncamento: lei de VOLUME de espaço-tempo. Com truncamento DUPLO em λ̃_min ∼ √N/4π (⇔ n_max ∼ √N; relação λ̃_min = N/(4πn_max), eq. 13 de 2008.07697): recupera log com **a = 0.346 ± 0.028 ≈ 1/3** (Calabrese–Cardy). Derivação do critério: corte de comprimento de onda ν_min ∼ ρ^{−1/2} convertido pela relação autovalor–comprimento-de-onda do contínuo | **Gate G4 congelado:** reproduzir volume sem truncamento E log(1/3) com λ̃_min = √N/4π duplo |
| A8 | **SSEE de horizontes dS (causet d=2,4)** [arXiv:2008.07697] | Fórmula SSEE: **S = Σ μ ln\|μ\|, W_CO∘v = iμ Δ_CO∘v, Δ_CO∘v ≠ 0** (eq. 12). Truncamento duplo obrigatório (o joelho REAPARECE na restrição — "não-localidade do SJ", eq. 14 + p.11). Sem truncamento: volume (todas as geometrias testadas). dS₂: n_max = 2√N ok; dS₄: esquema "linear" (inclinação) deu o melhor. **Os autores DECLARAM: esquemas escolhidos pelo critério de produzirem área** | Template do truncamento duplo (§4.2); a circularidade que nosso congelamento corta |
| A9 | **M⁴ aninhado (apêndice C de 2008.07697)** — a âncora decisiva para nós | Diamantes aninhados em M⁴ (r/R = 0.6, ⟨N⟩ 4k–18k): **truncamento de NÚMERO n_max = N^{3/4} (α=1) recupera área** (fit a√N: a ≈ 1.01 vs 0.78 esperado; complemento com α=2 melhora); **truncamento "linear" (joelho por inclinação) FALHA em M⁴ — mais consistente com volume**. Alvo discreto: S = ρ^{2/d}A/4 (eq. 9) | **O critério congelado de M3.2 (§4.2) vem DAQUI**, não do nosso d=2 |
| A10 | **Mecanismo do volume-law** [2008.07697, Discussão p.20] | "The fact that the SSEE obeys a volume law without truncation seems to arise from the **non-locality of the causal set** … systems with long-range order exhibit volume rather than area laws" | A literatura já atribui o volume à não-localidade = **a camada 1 do nosso Teorema da Fronteira**; N2-F2 (MI clássica super-área pelos links ~L^{4.2}) é a mesma física no setor clássico — a costura N2↔N4 que o pré-registro apostou existe na fonte |

*Nota de leitura:* o pré-registro chamava A4 de "AAS"; a fonte correta do resultado
do centro é Afshordi–**Buck–Dowker–Rideout**–Sorkin–Yazdi (ABDRSY, 1207.7101);
Afshordi–Aslanbeigi–Sorkin é a proposta do estado (JHEP 2012). Corrigido aqui.

## 2. Lema Q0 (entregável 2) — "a porta-ℏ custa exatamente 1 bit" [teorema]

**Setup.** Campo escalar real livre sobre causet finito (C, ≺). Toda a construção
SJ parte de G_R, definida por: G_R(x,y) ≠ 0 só se y ≺ x (suporte no passado
causal). A definição de "retardado" usa a DIREÇÃO de ≺ — nada mais na cadeia
SJ usa a direção.

**Lema Q0.** Seja T a dualização da ordem (≺ ↔ ≻, o "lado T" da camada 2).
Então:
(i) T troca G_R ↔ G_A = G_R^T, logo Δ ↦ −Δ e iΔ ↦ −iΔ;
(ii) como iΔ = i·(antissimétrica real), conjugação complexa leva autovetor u_k
(autovalor λ_k) em u_k* (autovalor −λ_k); portanto Pos(−iΔ) = Σ λ_k u_k* u_k^T =
(W_SJ)* — **o vácuo SJ dual é o conjugado complexo do original**; a troca do bit
é implementada ANTI-UNITARIAMENTE (é uma simetria de Wigner tipo-T, não
tipo-U);
(iii) observáveis pares sob conjugação independem do bit: o espectro {±λ_k} de
iΔ (invariante como conjunto), todos os |λ|, e o SSEE inteiro — conjugando a
equação geral W∘v = iμΔ∘v (com Δ real) obtém-se W*∘v* = −iμ*Δ∘v*, que é
exatamente o problema dual com μ' = μ*; como os μ físicos são reais,
{μ'} = {μ} e S = Σ μ ln|μ| é **bit-invariante**;
(iv) o que depende do bit: a parte imaginária de W (= Δ/2, que troca de sinal),
i.e., a distinção partícula/antipartícula e o sentido das fases e^{−iωt}. ∎

**Consequências (como pré-registrado):**
- **(a) Consistência tripla.** A quantização SJ requer inserir o bit que EXP2
  mediu como input (seta = input; o eixo emerge) — a porta-ℏ não cria nem exige
  seta emergente. E a estrutura complexa entra PAREADA com o bit (item ii): é
  "dualidade carregada" da camada 2, não estrutura emergente — exatamente o que
  o corolário GOE precisa (sem estrutura complexa intrínseca ⇒ operadores reais
  simétricos ⇒ classe ortogonal). O princípio fecha sobre si mesmo sem atrito.
- **(b) D-Q0 operacional.** Um observável SJ ímpar-sob-conjugação que fosse
  fixável só por (C, ≺) violaria (i)–(ii); se a campanha computacional produzir
  um, ataca a camada 2 de N0 → edita N0 (protocolo N0′).
- **(c) Corolário de escopo.** Como TODO observável das Fases 1–3 do
  pré-registro (espectros, dispersão via |W|, SSEE) é par sob conjugação, os
  RESULTADOS da campanha são independentes do bit — o bit é preço de
  construção, não parâmetro de ajuste. (Runs não precisam varrer R vs A;
  declarado.)

## 3. Q2-forte: enunciado preciso (entregável 3)

**Enunciado congelado.** "O vácuo SJ cria estrutura interna" significaria: a
construção SJ sobre (C, ≺) puro produz, canonicamente (sem escolha além do bit),
um grupo compacto NÃO-ABELIANO G agindo no espaço de modos {u_k}, comutando com
a dinâmica (i.e., preservando iΔ) e não-redutível ao U(1)-por-modo padrão
(fases de cada u_k) nem a permutações de autovalores degenerados acidentais.

**Resposta esperada (prior ALTO, declarado): NÃO — com mecanismo.** O grupo que
preserva iΔ é o estabilizador do seu espectro; para sprinkling de Poisson
genérico o espectro de iΔ é não-degenerado quase-certamente (nenhuma simetria
exata no causet finito — automorfismos de sprinkling são q.c. triviais, registro
Q8 do charter), logo o estabilizador se reduz ao toro das fases por modo =
U(1)^K abeliano. Estrutura interna não-abeliana exigiria degenerescência EXATA
imposta por simetria — que é precisamente o que o Axioma 2 INSERE (o multipleto
vem do G interno postulado, medido em N1). **Desfecho esperado: Axioma 2
permanece postulado [DELIMITAÇÃO, não morte]** — a verificação computacional é
barata (histograma de gaps espectrais na Fase 1; degenerescências além de
flutuação = surpresa a reportar).

## 4. Congelamentos (entregável 4)

### 4.1 Coeficientes dos propagadores

> **ERRATUM (02jul26, achado pelo Gate G — ver `GATE_G_RESULTADO.md` §1):**
> o massivo d=2 abaixo estava com sinal errado (taquiônico). Forma correta:
> **G_R = ½C(I + (m²/2ρ)C)^{−1}** (série alternante que reconstrói J₀;
> consistente com b = −m²/ρ da linha d=4). Verificado numericamente:
> ⟨G_R⟩ = ½J₀(mτ) a 3 decimais.

Como na tabela: d=2 massless G_R = ½C; massivo ½C(I−(m²/2ρ)C)^{−1} (SINAL
CORRIGIDO no erratum acima).
d=4 massless G_R = (1/2π)√(ρ/6)·L; massivo aL(I−baL)^{−1}, a = (1/2π)√(ρ/6),
b = −m²/ρ. **Segundo operador (N-hig 2):** inversa retardada do BD suavizado
(validado em C5), cross-check em d=2.

### 4.2 O truncamento do SSEE (o congelamento crítico)
O pré-registro previa "congelar o joelho a partir da reprodução d=2". A Fase 0
descobriu que isso seria o congelamento ERRADO: a relação 2D
λ̃_min = N/(4πn_max) "may not hold more generally" (2008.07697, eq. 13), e o
esquema de detecção-de-joelho-por-inclinação FALHA em M⁴ plano (A9). Congela-se,
em vez disso, o esquema que a literatura validou em M⁴ plano:

> **Critério congelado (M3.2, d=4):** truncamento de NÚMERO, n_max =
> round(N^{(d−1)/d}) com **α = 1**, aplicado DUPLAMENTE (template A8: 1º na
> região grande C → iΔ^t, W^t; restrição a C_O; 2º truncamento no espectro de
> iΔ^t|_CO; W projetado na base duplamente truncada).
> **α ∈ {1, 2} reportado como robustez declarada — NUNCA ajustado pós-dado.**
> Gate G4 (d=2) usa o critério analítico próprio de d=2: λ̃_min = √N/4π
> (⇔ n_max = √N), que valida o pipeline contra Sorkin–Yazdi (a = 1/3).

Caveats herdados e declarados: (i) o iΔ truncado viola i∆(x,x′) = 0 a separação
espacial (acausalidade que média a zero sobre sprinklings — 2008.07697 p.20);
(ii) a identificação do "volume espacial" que motiva α não é covariante (a
ambiguidade é da literatura; congelar α=1 antes de rodar é a nossa resposta).

### 4.3 Rota da Fase 2
R-A (massa local m²(x) da Hessiana projetada no kernel de Johnston com b
por sítio) — mantida como pré-registrada; R-B só diagnóstico.

### 4.4 Geometrias declaradas
Fase 1 = slab sobre toro espacial (t ∈ [−T,T] × toro^{d−1}, min-imagem na
ordem) — globalmente hiperbólico; é o cenário exato de Fewster–Verch, logo
não-Hadamard CONHECIDO e irrelevante para nossos observáveis (A5). Fase 3 =
geometria de N2 verbatim (canto de Rindler, transversal periódica min-imagem)
— MESMA construção de grafo em que a MI clássica mediu L^{3.36}, para a
comparação ser limpa.

## 5. Ajustes de escopo/prior (declarados ANTES de qualquer código)

### 5.1 M3.1 rebaixada: medição → reprodução-âncora
A lei de volume do SSEE sem truncamento já foi medida em M² aninhado, dS₂, dS₄
e M⁴ (A7–A9), com a causa apontada na literatura = não-localidade do causet
(A10). M3.1 não é descoberta nossa; vira GATE de consistência da Fase 3 (se não
der volume, temos bug, não física). Honest scoping do pré-registro aplicado.

### 5.2 O que permanece genuinamente nosso em Q3 (e o prior novo)
Quatro eixos que a literatura NÃO cobriu: (i) canto de Rindler PLANO em caixa
com transversal periódica (a literatura fez diamantes aninhados e cunhas de dS);
(ii) escala em L transversal a ρ FIXO (a literatura escala em N a geometria
fixa — nosso eixo é o da lei de área do N2, S ∝ ρ^{1/2}L² se a eq. 9 valer);
(iii) critério CONGELADO ANTES (corta a circularidade que os próprios autores
declaram); (iv) o confronto no MESMO substrato com a MI clássica super-área de
N2-F2 — "a quantização covariante resgata a área que o setor clássico perdeu?"
segue aberto e é a pergunta do programa. **Prior de M3.2 atualizado: 50/50 →
~60/40 pró-área** (M⁴ aninhado recuperou área com o critério que congelamos).
As duas leituras de saída do pré-registro (resgate vs 4ª face) ficam como estão.

### 5.3 Upgrade de estatuto do Lema Q0
De "candidato a lema" para **[teorema]** (§2 — a prova é completa no setor
Gaussiano finito). O pré-registro previa P-N4-2 com prior ALTO; confirmada
analiticamente já na Fase 0. P-N4-2 SAI da lista de coisas que as fases
computacionais testam (resta só a busca ativa de contraexemplo D-Q0, que é
passiva: qualquer observável ímpar que apareça).

## 6. Estado do funil e próximo executável

```
Fase 0 (analítica)               ✅ ESTA SESSÃO (âncoras + Q0 teorema + congelamentos)
  → Gate G (diamante d=2, G1–G4) ← PRÓXIMO EXECUTÁVEL ("execute N4 Gate G"; 1º código)
    → Fase 1 (escalar, caixa)    (D1/D2 vivem aqui)
      → Fase 2 (Goldstone)  ∥  Fase 3 (SSEE canto de Rindler; M3.1 agora = gate)
```

Nenhuma morte disparou na Fase 0; nenhum gate computacional foi tocado; nenhuma
janela foi afrouxada (uma foi SUBSTITUÍDA por razão documentada ANTES de rodar,
§4.2 — o tipo de mudança que o pré-registro existe para disciplinar).
