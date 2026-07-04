# N0 — O PRINCÍPIO: resultado da campanha analítica

**Data:** 2026-07-01 · **Pasta:** `FRONTEIRA_COMPACTA/N0_PRINCIPIO/`
**Natureza:** inteiramente analítica, **zero código** (nenhum toy numérico foi necessário —
nenhum contraexemplo candidato sobreviveu ao papel). Pré-registro: `../CHARTER.md` §N0.
**Etiquetas:** [teorema] = demonstrado aqui ou na literatura citada; [prova-esboço] =
argumento completo em esboço, lacunas declaradas no Apêndice B; [conjectura];
[medido] = campanha pré-registrada do programa; [literatura].

---

## 0. Veredito em uma página

**A tese da metade tipo-tempo é um PRINCÍPIO, não um sumário** — no nível preciso em que
um princípio de exclusão pode sê-lo: ela é cinemática (diz o que a classe *pode carregar*,
não o que a dinâmica *faz acontecer*), e nesse nível os quatro resultados seguem de um
único enunciado, o enunciado gera consequências que ninguém procurou, e dois dos
sub-alvos produziram teoremas novos (o no-go de paridade em forma forte; o afiamento da
assinatura para *definida vs. indefinida*).

| Sub-alvo | Veredito | Morte pré-registrada disparou? |
|---|---|---|
| **N0(a)** unificação | **FECHA** — os 4 são corolários de um enunciado único (Teorema da Fronteira, §1), com 2 ressalvas de escopo *declaradas* (existência dinâmica dos positivos; seta espontânea fechada empiricamente, não cinematicamente) | NÃO (ressalvas ≠ hipóteses adicionais; são qualificadores de escopo) |
| **N0(b)** RG de thinning | **FECHA FORTE** — Poisson é ponto fixo exato E atrator global (nível de lei, via teorema de limites de thinning); nenhuma direção relevante invariante ergódica; a única direção marginal é ρ = a unidade externa | NÃO (nenhuma perturbação relevante encontrada) |
| **N0(c)** assinatura | **FECHA COM AFIAMENTO** — a fronteira é *assinatura definida vs. indefinida* (não "Lorentz vs. Euclides"); contraexemplo do tipo exigido é impossível (assimetria forçado-vs-escolhido) | NÃO |
| **N0(d)** no-go P/quiralidade | **TEOREMA NOVO FECHA, na forma forte** — P não age sobre dados intrínsecos (sem portador); violação explícita E espontânea de P são impossíveis na classe. T é mais fraco (dualidade carregada; simetria só estatística; espontâneo fechado por medição, EXP2). CP ≡ C operacionalmente | NÃO (a quebra espontânea foi tratada e *não* abre porta: não há parâmetro de ordem P-ímpar) |
| **N0(e)** geração de previsões | **PASSA** — ≥5 consequências novas além dos 4 negativos conhecidos (P1–P6, §6) | NÃO ("sumário, não princípio" não se aplica) |

**Resposta à pergunta-mestra da linha** (*o que torna inevitável a fronteira
compacto/não-compacto?*): emergência estatística sobre um substrato invariante é feita de
médias sobre órbitas de grupo. Órbitas têm volume finito ⟺ o grupo relevante é compacto;
invariantes têm espectro discreto ⟺ o grupo é compacto. **A assinatura da métrica decide,
estrutura por estrutura, de que lado cada uma cai** — e a ordem causal, por ser o dado
Lorentziano por excelência, não pode trocar de assinatura sem deixar de ser ordem.

---

## 1. O núcleo axiomático

> Este parágrafo é o entregável exigido pelo charter: legível como matemática por quem
> nunca viu os papers.

**Axioma 1 (substrato).** O substrato é um conjunto causal (C, ≺) obtido por sprinkling
de Poisson de densidade ρ em M^d (Minkowski, d≥2), com a correspondência
discreto–contínuo independente de referencial. [Poisson não é postulado independente:
é a única medida discreta invariante — Bombelli–Henson–Sorkin [literatura]; o contraste
foi medido no programa (rede regular falha isotropia, campanha R1) [medido].]

**Axioma 2 (matéria).** Sobre C vive um campo interno genérico n: C → X, com X compacto
(variedade de grupo G ou coset G/H, G compacto), acoplado por um funcional invariante das
quantidades intrínsecas (ordem + contagem); genericidade fixa o termo líder ∝ (1−n_i·n_j)
[literatura: universalidade; robustez ±10% medida, FLR].

**Definição (classe intrínseca).** Uma *regra/observável intrínseco* é um funcional
mensurável de (C, ≺, n) apenas — ordem, contagem e campo interno; nenhuma coordenada de
embedding.

**Lema 0 (o conteúdo intrínseco de um par).** [prova-esboço] Para dois eventos i, j do
sprinkling:

- **i ≺ j (tipo-tempo):** o dado intrínseco é *assinado e estruturado* — a relação tem
  direção (quem precede), e o intervalo de Alexandrov [i,j] ⊂ C carrega estrutura interna:
  N(i,j) ~ Poisson(ρ c_d Δτ^d) e o comprimento da cadeia máxima ≈ m_d ρ^{1/d} Δτ estimam o
  tempo próprio **com sinal** (a ordem dá o sinal; a contagem dá o módulo).
- **i ∥ j (tipo-espaço):** o dado intrínseco é **um bit** (incomparabilidade). Toda
  informação adicional vem de terceiros (passados/futuros comuns) e produz apenas
  invariantes **não-assinados** (contagens ⇒ estimativas de |s²|, dados de Gram). Uma
  coleção de estimativas de distância determina uma configuração espacial no máximo a
  menos de **O(d−1)** — o grupo ortogonal completo, *incluindo reflexões* — nunca a menos
  de SO(d−1) apenas.

> **Slogan exato da tese:** *a ordem causal carrega o tempo com sinal e o espaço sem
> sinal — e sem estrutura.* A "metade tipo-tempo" do enunciado original é isto.

**Teorema da Fronteira.** [prova-esboço; peças rigorosas citadas] Na classe intrínseca
(Axiomas 1–2), a estatística emergente vê o grupo O(d−1,1) × G_int através de exatamente
três camadas estruturais, e cada camada dita um veredito:

1. **Órbitas não-compactas ⇒ divergência/ausência.** Toda quantidade invariante de par
   causal é função de Δτ (Lema 0); a órbita dos "vizinhos a Δτ fixo" é o hiperbolóide
   H^{d−1} = SO⁺(d−1,1)/SO(d−1), de volume infinito; por Campbell–Mecke,
   ⟨z⟩ = ρ·Vol(H^{d−1})·∫Δτ^{d−1}q(Δτ)dΔτ = ∞ para toda regra não-trivial
   [teorema — `IMPOSSIBILIDADE_PARCIAL` §3.1]. *Recusados:* valência finita, comprimento
   de correlação, criticalidade, escala emergente.
2. **Componentes desconexas ⇒ bits não-fixáveis.** π₀(O(d−1,1)) = ℤ₂×ℤ₂ (paridade ×
   reversão temporal). A componente-P age **trivialmente** sobre dados intrínsecos (é um
   isomorfismo de (C,≺)); a componente-T age como **dualidade de ordem** (≺ ↔ ≻),
   estatisticamente simétrica. *Recusados:* orientação espacial (nem espontânea — §5),
   seta do tempo (estatisticamente; espontâneo fechado por medição).
3. **Parte compacta ⇒ índices discretos protegidos.** Invariantes de grupos compactos
   têm espectro discreto: π₃(G)=ℤ (Bott) para todo G simples compacto, π₄(SU(2))=ℤ₂,
   reps de H finito-dimensionais e discretas. *Permitidos* (e, quando a dinâmica ordena,
   protegidos): cargas topológicas, multipletos exatos, estatística de troca ℤ₂,
   contagem de Goldstones.

**Corolários (nomeados):** sem-escala (camada 1), sem-fóton (camadas 1+2, via B = fluxo
por 2-célula tipo-espaço orientada — §2.3), sem-quiralidade (camada 2, §5),
eixo-sem-seta (camada 2, lado T), matéria topológica (camada 3, condicional ao Axioma 2).

**Escopo declarado (as duas ressalvas que NÃO são hipóteses adicionais):** o princípio é
*cinemático* — governa o que a classe pode exprimir/carregar e a *forma* do que emerge.
(i) A **existência** dos positivos (LRO a J finito, confinamento) é dinâmica e foi
*medida*, não deduzida; o princípio fixa a permissão e a forma (quais índices, quais
degenerescências), não o diagrama de fases. (ii) No lado T, a exclusão da seta espontânea
é empírica (COLAPSO EXP2), não cinemática — a assimetria P-vs-T é real e está enunciada
como tal (§5.4).

---

## 2. N0(a) — Unificação: os quatro como corolários

### 2.1 Âncora contínua (Malament/HKM) e a tese como versão a densidade finita

[literatura] Malament (1977) / Hawking–King–McCarthy (1976): em espaços-tempos
future- e past-distinguishing, a ordem causal determina a métrica a menos de fator
conforme; a contagem (volume) fixa o fator. "Order + number = geometry" é o slogan CST.

Isso parece *contradizer* a tese ("só a metade tipo-tempo") — e a resolução é o conteúdo
real do sub-alvo: **Malament recupera a geometria inteira apenas no limite de informação
infinita** (a ordem completa do contínuo). A densidade finita, o que existe é o Lema 0:
pares tipo-tempo carregam dado assinado e estruturado; pares tipo-espaço carregam um bit,
e o resto é reconstrução estatística não-assinada. A tese é, portanto, **a forma
correta do teorema de Malament para o substrato discreto**: a metade tipo-tempo é
intrínseca; a metade tipo-espaço é assintótica/estatística. A versão discreta completa
("order+number ⇒ variedade aproximada") é a Hauptvermutung da CST — conjectura na
literatura, com instâncias medidas no programa (dimensão de Myrheim–Meyer, curvatura BD a
23.5σ, Schwarzschild 0.2%) [medido].

### 2.2 O objeto ausente, dito com precisão (âncora antichain)

**Lema (antichains são amorfas).** [teorema, trivial mas central] A subordem induzida em
qualquer antichain A ⊂ C é a relação vazia; seu grupo de automorfismos é o simétrico
S_|A| inteiro; duas antichains de mesma cardinalidade são isomorfas como subestruturas.
**O único dado intrínseco de uma antichain é |A|.**

O objeto que a metade tipo-espaço *não tem*, dito com precisão: **p-células tipo-espaço
com estrutura intrínseca e orientação, para todo p ≥ 1.** No contínuo, uma hipersuperfície
de Cauchy Σ carrega métrica Riemanniana intrínseca h_ij, formas de área e orientação; no
substrato, o suporte discreto de Σ é uma antichain — amorfa pelo lema. A reconstrução de
topologia/geometria espacial a partir da ordem existe como programa
(Major–Rideout–Surya, antichains engrossadas [literatura]) e é *estatística e
não-assinada* — exatamente o que o Lema 0 permite, nada mais.

**A 2-célula do fóton cai como caso particular:** B = fluxo de F por uma 2-célula
tipo-espaço **orientada**. A 2-célula tipo-espaço falha duas vezes: não há estrutura
(lema da antichain) e não há sinal (dados de Gram determinam configurações a menos de
O(d−1) — a orientação da célula não tem portador). O campo E, fluxo por uma 2-célula
tipo-tempo, tem as duas coisas: o diamante causal é estruturado (N(i,j), cadeias) e
orientado (pela ordem). **"Diamantes 100% elétricos" (E6-3) [medido] deixa de ser
acidente e vira o corolário mais literal da tese.**

### 2.3 Os quatro corolários, com o que cada um usa

| # | Resultado | O que usa do Teorema | Insumo além do teorema? |
|---|---|---|---|
| C1 | ⟨z⟩=∞ / sem escala [teorema + medido 7×] | Camada 1 (órbita H^{d−1}) + Lema 0 (invariante de par causal ⇒ função de Δτ) | Só os Axiomas (Campbell–Mecke é propriedade do Poisson do Axioma 1). **Corolário limpo.** |
| C2 | Diamantes 100% elétricos / morte do fóton [medido, E6-3 + 3 alavancas] | Lema 0 + lema da antichain (célula sem estrutura E sem sinal) | A identificação padrão B ≡ fluxo espacial (definição, não hipótese). **Corolário limpo.** |
| C3 | Emergência topológica (B=π₃, FR=ℤ₂, octeto) [medido, FL1/FN3] | Camada 3 (compacto ⇒ índice discreto) | Axioma 2 (o alvo compacto é postulado) + *existência* dinâmica medida. **Corolário no nível de forma/permissão** — ressalva de escopo declarada. |
| C4 | Eixo-sem-seta [medido, COLAPSO EXP2] | Camada 2, lado T (dualidade carregada, lei auto-dual) | Fechamento do espontâneo é empírico (EXP2). **Corolário com ressalva declarada.** |

**Veredito N0(a): FECHA.** Os quatro seguem de UM enunciado (o Teorema da Fronteira) mais
os dois Axiomas que o próprio enunciado pressupõe. As duas ressalvas (C3: existência
dinâmica; C4: espontâneo empírico) são qualificadores de escopo do princípio — um
princípio de exclusão não deve mesmo prever diagramas de fase — e não hipóteses
independentes. O critério de morte ("algum dos 4 exige hipótese adicional independente")
não dispara.

### 2.4 A sub-pergunta do índice universal

| Positivo [medido] | Estrutura compacta | Invariante | Tipo |
|---|---|---|---|
| Carga bariônica B | alvo G (S³≅SU(2); SU(3)) | π₃(G) = ℤ, todo G simples compacto (Bott) | homotopia |
| Estatística spin-½ (FR) | laços no espaço de configs | π₁(Conf₁) ≅ π₄(SU(2)) = ℤ₂ | homotopia |
| Octeto degenerado | H = SU(3)_V não-quebrado | rep adjunta, dim 8, degenerescência exata | teoria de reps |
| Contagem de Goldstones | coset G/H | dim(G/H) | geometria de coset |
| Confinamento σ>0 | centro Z(G)? | **em teste** (G₂ discrimina — N1) | centro |
| LRO / vácuo | G compacto | padrão SSB G→H | dinâmico [medido] |

**Veredito: NÃO há um índice único** — há uma **família** {π₃, π₄, reps de H, dim G/H}
com **uma raiz comum única: compacidade ⇒ espectro discreto** (grupos de homotopia de
alvos compactos são finitamente gerados; irreps de grupos compactos são
finito-dimensionais e discretas; grupos não-compactos têm famílias contínuas de
invariantes). A resposta pré-registrada correta é a segunda opção do charter: *"família
de homotopias/representações do alvo compacto"* — mas a família tem UM porquê, e o porquê
é a camada 3 do Teorema.

### 2.5 O precedente de Wigner (verificado)

[literatura — Wigner 1939; Weinberg QFT I cap. 2] Na classificação das irreps unitárias
do grupo de Poincaré: (i) partícula massiva — little group SO(3), **compacto** ⇒ spin
**discreto**; (ii) o rótulo de momento vive na casca de massa — que é *o mesmo
hiperbolóide H³* da camada 1 — **não-compacto** ⇒ rótulo **contínuo**; (iii) partícula
sem massa — little group ISO(2), cuja parte não-compacta (translações) DEVE agir
trivialmente, senão surgem as representações de *spin contínuo*, nunca observadas; a
helicidade discreta vem do SO(2) compacto restante.

O padrão da física quântica padrão já é: **números que se fixam = invariantes da parte
compacta; números que correm contínuos (ou patologias nunca vistas) = parte não-compacta.**
E há uma coincidência estrutural exata que merece registro: o hiperbolóide H^{d−1} aparece
em Wigner como o espaço dos rótulos contínuos de momento e no Teorema da Fronteira como o
volume infinito que mata a valência. **Um único objeto geométrico, duas manifestações da
mesma não-compacidade.** A tese é a versão estatística, sobre a ordem, de um padrão que a
teoria quântica de campos já pratica.

---

## 3. N0(b) — A RG de thinning

### 3.1 Definição (e por que ela é a coarse-graining nativa da CST)

**R_p (deleção aleatória):** manter cada elemento de C independentemente com
probabilidade p ∈ (0,1); tomar a subordem induzida. Totalmente intrínseca (não usa
embedding); é a coarse-graining canônica da literatura CST (Sorkin) [literatura], aqui
lida pela primeira vez no programa como transformação de RG.

**Observação estrutural (que simplifica tudo):** em M^d a dilatação x → x/b é um
*automorfismo da estrutura causal* (conformal ⇒ preserva cones ⇒ preserva ≺) e leva
PPP(ρ) em PPP(ρ b^d). Logo, **a lei da ordem intrínseca do sprinkling em M^d é
ρ-independente** — ρ é gauge puro no nível intrínseco (é exatamente o enunciado "ρ é a
unidade externa da teoria", agora como teorema trivial). A etapa de redilatação da RG
usual age trivialmente sobre a ordem; a RG intrínseca é *só* a deleção.

### 3.2 As três proposições

**Proposição 1 (ponto fixo exato).** [teorema] R_p(PPP(ρ)) = PPP(pρ) (thinning
independente de Poisson é Poisson — teoria clássica de processos pontuais); como a lei
da ordem é ρ-independente (3.1), **a lei da ordem do sprinkling é ponto fixo EXATO da
deleção aleatória** — não fixo-aproximado, não fixo-no-limite. Pela unicidade BHS, é o
único ponto fixo Lorentz-invariante.

**Proposição 2 (atrator global, nível de lei).** [teorema, literatura] O teorema
clássico de limites de thinning (Rényi para renovação; Kallenberg em geral: iterar
thinning + contração converge para um processo de Cox) dá: **todo processo pontual
invariante ergódico de intensidade finita flui, sob iteração de R, para o Poisson** (o
limite Cox é dirigido pela intensidade amostral; ergodicidade ⇒ intensidade amostral
constante ⇒ Cox = Poisson). O ponto fixo não é só único: é o atrator de toda a classe.

**Proposição 3 (nenhuma direção relevante).** [prova-esboço] No nível dos momentos
fatoriais: thinning multiplica a densidade de k-ésimo momento por p^k; a redilatação
compensadora multiplica por b^{kd} e dilata os argumentos; com p = b^{−d} a ação líquida
é **dilatação pura dos argumentos**: ρ_k(x₁,…,x_k) → ρ_k(bx₁,…,bx_k). Logo, para
correlações truncadas g:

- g com decaimento (qualquer taxa, inclusive lei de potência): g(b^n x) → 0 —
  **irrelevante**. Não existe amplitude renormalizada que salve uma cauda: a RG não toca
  amplitudes, só dilata argumentos.
- g → c > 0 no infinito: processo não-ergódico (mistura/Cox) — não é uma direção de
  escala, é superseleção da intensidade; e pela observação 3.1, **intrinsecamente
  invisível** em M^d infinito (cada componente ρ dá a mesma lei de ordem).
- A única direção marginal é a própria intensidade ρ — **que é a unidade externa,
  gauge intrínseco**.

**Setor de regras/matéria:** toda regra invariante tem marginal q(Δτ) e ⟨z⟩ = ∞ em
qualquer ρ (camada 1) — a divergência é propriedade do ponto fixo, sem escala onde
correr; consistente com C5 [medido: dimensão espectral sem running]. O que esta campanha
NÃO constrói: a RG conjunta (substrato + campo de matéria acoplado), que é a derivação
analítica da EFT — permanece o item aberto conhecido (Perguntas I §3; Apêndice B).

### 3.3 Veredito N0(b)

**"Sem escala" É estrutura de RG** [prova-esboço + teoremas citados]: ponto fixo trivial
único, exato, globalmente atrator, sem direção relevante invariante ergódica; a única
direção marginal é a unidade da teoria. Emergência = o que sobrevive à deleção
(topologia, formas — invariantes discretos não têm como fluir); não-emergência = o que a
deleção dilata para longe (correlações, escalas, laços).

**Critério de morte (perturbação relevante = mecanismo de escala novo): NÃO DISPARA.**
A porta única que o charter deixava para reabrir a linha de escala fecha também por
dentro da RG.

---

## 4. N0(c) — O enunciado de assinatura

### 4.1 O teorema, afiado

**Teorema (a fronteira é a definitude da assinatura).** [prova-esboço] Seja um processo
de Poisson invariante sob o grupo de isometrias de (ℝ^d, g), com g de assinatura (p,q),
e uma regra de conexão invariante não-trivial. A órbita de vizinhos a separação
invariante fixa é a quádrica {x·x = c}, e:

- **assinatura definida** (p=0 ou q=0; grupo O(d), compacto): a órbita é a esfera
  S^{d−1}, volume finito ⇒ ⟨z⟩ = ρ·Vol(S^{d−1})·∫r^{d−1}q(r)dr **< ∞ para toda q
  integrável** — vizinhanças locais, grafos geométricos aleatórios, e criticalidade
  genuína existe [literatura: percolação contínua, Ising em RGG];
- **assinatura indefinida** (p,q ≥ 1; grupo O(p,q), não-compacto): TODA quádrica de
  separação é não-compacta com volume infinito ⇒ ⟨z⟩ = ∞ para **toda** regra invariante
  não-trivial — o mesmo mecanismo de Campbell–Mecke da camada 1.

**O afiamento sobre o pré-registro:** a fronteira não é "Lorentziano vs. Euclidiano" — é
**definida vs. indefinida**. Qualquer assinatura indefinida mata; a Lorentziana (q=1) é
apenas a única indefinida que possui cone convexo e portanto *ordem causal*. O substrato
do programa está, por construção, do lado indefinido: **a ordem É o dado Lorentziano; um
substrato de ordem causal não pode "Wick-rotacionar" para o lado compacto sem deixar de
ser ordem.** (A rotação de Wick é exatamente a operação que compactifica o grupo — é por
isso que métodos Euclidianos "funcionam" em matéria condensada e QFT de rede: eles vivem
do lado definido desde o início.)

### 4.2 A checagem de contraexemplo (critério de morte)

A morte exigia: um sistema Euclidiano invariante **sem** criticalidade *pela mesma razão*
(valência divergente forçada pela invariância). Isso é impossível: no lado definido
existe q de suporte compacto (r < r₀), invariante, com ⟨z⟩ finito — a divergência nunca é
*forçada*, apenas *escolhida* (caudas longas). No lado indefinido a divergência é forçada
para toda regra. **A assimetria é forçado-vs-escolhido, e é exatamente a fronteira.**
Morte NÃO dispara.

### 4.3 Consequência (destrava N3)

A conexão Wen ganha seu enunciado exato: *string-nets exigem estrutura de laços de
dimensão finita, que exige valência finita, que exige órbitas compactas, que exige
assinatura definida — e o substrato causal invariante é indefinido por definição.* Os 60
anos de emergência em matéria condensada não se transportam porque matéria condensada
vive, toda ela, do lado definido da fronteira. **N3 (paper Wen-complement) está gated em
N0(c) e fica LIBERADO por este enunciado.**

---

## 5. N0(d) — O no-go de paridade/quiralidade

> Disciplina pré-registrada: ZERO referência ao Modelo Padrão até §5.6. Só medida, ordem,
> componentes de O(d−1,1), e o tratamento da quebra espontânea.

### 5.1 Lema 1 (ação intrínseca das isometrias)

[teorema] Seja g ∈ IO(d−1,1) uma isometria de M^d.

- Se g **preserva a orientação temporal** (inclui todas as rotações, boosts, translações
  E as reflexões espaciais "tipo-P"): g preserva ≺; logo induz um isomorfismo de ordem
  (C_Φ, ≺) ≅ (C_{gΦ}, ≺). **Como estrutura intrínseca, gΦ é o MESMO objeto que Φ.**
  Toda isometria que preserva tempo age *trivialmente* sobre o espaço de configurações
  intrínsecas (C, ≺, n) — é redundância da descrição por embedding, não simetria da
  teoria intrínseca.
- Se g **reverte a orientação temporal** (tipo-T): g leva ≺ em ≻; induz um
  *anti-isomorfismo* — (C, ≺) ↦ (C, ≺^op), a ordem dual, que é genericamente um objeto
  intrínseco **distinto**. T é a única componente de O(d−1,1) que age não-trivialmente
  sobre dados intrínsecos, e age como dualidade de ordem.

### 5.2 Lema 2 (orientação espacial não tem portador)

[prova-esboço] Um funcional intrínseco P-ímpar precisaria distinguir a quiralidade de
uma configuração espacial. Pelo Lema 0, todo dado espacial intrínseco é reconstrução
estatística por contagens — invariantes **não-assinados** (estimativas de |s²|, dados de
Gram). Dados de Gram determinam uma configuração de pontos a menos de O(d−1), *incluindo
reflexões*: o sinal do determinante de qualquer d−1-upla de "direções espaciais
reconstruídas" não é função dos dados. **Não existe funcional intrínseco ímpar sob
reflexão espacial. O portador da quiralidade espacial é vazio.**

### 5.3 O teorema

**Teorema (no-go de paridade, forma forte).** Na classe intrínseca (Axiomas 1–2):

1. **Violação explícita é inexprimível.** Nenhum termo P-ímpar pode ser escrito na ação
   ou em observáveis: P age trivialmente (Lema 1) e não existe funcional P-ímpar
   (Lema 2). [Contraste instrutivo: numa rede cúbica ℤ³, termos quirais SÃO exprimíveis —
   a rede herda o frame orientado do embedding. O substrato causal não herda frame.]
2. **Violação espontânea é impossível — e este é o ponto que o pré-registro mandava
   tratar.** Quebra espontânea de uma simetria S exige um parâmetro de ordem S-ímpar
   sobre o espaço de configurações (o ferromagneto quebra SO(3)_int porque SO(3)_int age
   não-trivialmente sobre n). P age **trivialmente** sobre o espaço de configurações
   intrínseco inteiro (Lema 1) — não há órbita de vácuos trocados por P, porque P não
   troca nada. A analogia com o ferromagneto **falha no ponto exato**: quebrar exige
   agir. P é, na teoria intrínseca, o análogo de uma redundância de gauge — e
   redundâncias não quebram espontaneamente (o mesmo espírito de Elitzur).
3. **O loophole do pseudo-escalar é nominal.** Pode-se *declarar* que o campo interno
   transforma sob P (n → −n, "pseudo-escalar"). A declaração é vazia operacionalmente:
   violação de P observável = correlator ímpar entre a quiralidade interna e uma
   quiralidade **geométrica** — e o parceiro geométrico ímpar não existe (Lema 2).
   ⟨n⟩ ≠ 0 com rótulo pseudo-escalar é quebra da ℤ₂ *interna* (permitida, camada 3), não
   de P.

**Corolário (quiralidade).** Quiralidade emergente = correlação entre handedness interna
e handedness espacial. Sem portador espacial (Lema 2), **quiralidade não emerge da
classe — nem explicitamente, nem espontaneamente.** ∎

### 5.4 T: o lado honestamente mais fraco

A estrutura P-vs-T é **assimétrica**, e o teorema deve dizê-lo (é o refinamento sobre a
intuição "P,T componentes desconexas ⇒ mesmo destino", que era imprecisa):

- **P:** sem portador — exclusão **cinemática**, fecha explícito E espontâneo. [teorema]
- **T:** COM portador (a dualidade de ordem é intrínseca; funcionais T-ímpares existem —
  ex.: assimetrias passado/futuro de contagem). A lei é auto-dual (medida T-invariante)
  ⇒ ⟨O⟩ = 0 para todo O T-ímpar **no equilíbrio estatístico**; mas quebra espontânea de
  T não é cinematicamente excluída. Ela foi **medida ausente**: COLAPSO EXP2 — o eixo
  (comparabilidade, não-assinada) emerge; a seta (o bit da dualidade) não condensa e
  precisa ser input [medido]. O fechamento do lado T é empírico, não teoremático — e
  isso está correto e declarado (é a ressalva (ii) do §1).

### 5.5 CP

Defina C = involução interna c: X → X que é simetria da ação (ex.: n → −n). C age
não-trivialmente sobre configurações ⇒ **C pode quebrar espontaneamente** (camada 3 — é
uma ℤ₂ interna como outra qualquer). Como P age trivialmente (Lema 1), **CP = C∘P age
exatamente como C: na classe intrínseca, CP e C são operacionalmente indistinguíveis.**

**Enunciado para registro (previsão falsificável do princípio):** toda violação de CP
cujo conteúdo seja genuinamente P-emaranhado (i.e., que não se reduza a uma violação de
conjugação puramente interna) é **input externo** — a classe não a produz. Violações de
ℤ₂ internas (C puro) podem emergir espontaneamente. [Remark de consistência: se a EFT
emergente satisfaz CPT (assumido do contínuo, não derivado aqui — Apêndice B), então
T-par estatístico ⇔ CP-par estatístico, uma segunda rota para a mesma conclusão, com a
mesma ressalva empírica do §5.4.]

### 5.6 Aplicações (agora sim, e em seção separada, como mandava o charter)

O Modelo Padrão entra apenas aqui. Os três setores ausentes do programa são exatamente
os três setores **quirais**: neutrinos (a partícula maximamente quiral), a estrutura de
gerações (famílias definidas por reps quirais), e o setor eletrofraco (gauge quiral).
O teorema explica os três de uma vez: não faltou campanha — **falta o portador**. Anos de
campanhas nesses setores ficam estruturalmente bloqueados, que era o objetivo declarado.

**Falseador do teorema:** qualquer derivação de quiralidade a partir de um substrato
causal invariante (de qualquer grupo de pesquisa) implicaria erro em Lema 1 ou Lema 2 —
o no-go é atacável e, portanto, científico.

---

## 6. N0(e) — Geração de previsões (o teste "princípio vs. sumário")

Derivadas da tese ANTES de olhar dados, além dos quatro negativos conhecidos:

- **P1 — Quantização canônica não tem portador; quantização covariante é FORÇADA.**
  A tese proíbe toda variável fundamental sobre superfícies espaciais. Caem de uma vez:
  variáveis ADM (h_ij, K_ij em Σ), funcional de onda Ψ[h_ij] (Wheeler–DeWitt), gauge
  Hamiltoniano de rede (links espaciais), redes de spin como cinemática fundamental
  (grafos SOBRE Σ com operadores de área/volume), linhas de Wilson espaciais, e
  emaranhamento-através-de-Σ como variável fundamental. O que resta é histórias/covariante
  — Sorkin–Johnston, funcionais de decoerência. **Consequência interna: N4 deixa de ser
  "uma opção" e vira a única quantização compatível com o princípio** — upgrade
  estrutural do gate de N4.
- **P2 — Nenhuma violação de P em observáveis puros de geometria, nunca.** Nem
  espontânea (§5.3). Concreto e falsificável: um fundo de ondas gravitacionais quiral de
  origem de substrato, ou correlatores primordiais P-ímpares *do setor geométrico*, são
  impossíveis na classe; toda P-violação observada rastreia aos setores importados.
- **P3 — Sem bariogênese dinâmica.** B é carga topológica π₃ — exatamente conservada
  (camada 3 protege *demais*); os canais de criação foram medidos mortos (FL3, HE1–HE3)
  [medido]; e o conteúdo P-emaranhado de CP é externo (§5.5). A assimetria
  matéria–antimatéria é, nesta classe, **condição inicial ou input** — a classe não a
  fabrica.
- **P4 — Sem monopolos magnéticos, duplamente.** Como objeto de gauge: não há U(1)
  emergente (corolário sem-fóton). Como sóliton interno: π₂(G) = 0 para TODO grupo de
  Lie [teorema clássico] — alvos de variedade-de-grupo não têm setor de monopolo;
  monopolos exigiriam coset com π₂(G/H) ≠ 0, i.e., U(1) não-quebrado em H — a mesma
  porta fechada. A não-observação de monopolos é consistência gratuita (o problema do
  monopolo GUT não se põe).
- **P5 — Nenhuma partícula emergente estável sem índice topológico discreto; nenhuma
  carga emergente contínua.** (Camada 3 + precedente de Wigner: rótulos que se fixam são
  discretos-compactos.) Toda estabilidade emergente é um inteiro.
- **P6 — Hierarquia de quebras espaço-temporais possíveis.** Se a classe algum dia
  exibir quebra espontânea de caráter espaço-temporal, ela só pode ser do setor com
  portador: T (dualidade) ou alinhamento de frame/boost (direções tipo-tempo são
  intrínsecas — cadeias). **Nunca P.** [R1/EXP2 medem ambos ausentes até hoje; o
  princípio prevê a ordem em que poderiam aparecer, e proíbe o terceiro para sempre.]

**Sobre o que a tese NADA diz (declaração exigida pelo charter):**
(iv) **emaranhamento/causalidade quântica: nada.** O substrato é clássico-estatístico;
estrutura quântica só entra via quantização (N4). Dizê-lo é parte da honestidade do
princípio. (v) **SUSY: quase nada** — sem portador para cargas espinoriais fundamentais
(não há fibrado de spin sobre uma ordem; férmions da classe são coletivos, FR); sobre
SUSY acidental de EFT, silêncio.

**Critério de morte (o mais importante do charter):** a tese gera P1–P6 além dos quatro
negativos conhecidos — inclusive uma reorganização interna não-trivial (P1 força N4) e
proibições observacionais (P2–P4). **"Sumário organizador, não princípio" NÃO se aplica.**

---

## 7. Veredito global de N0

**O princípio existe.** Formato axiomático entregue (§1): dois axiomas → Lema 0 ("tempo
com sinal, espaço sem sinal e sem estrutura") → Teorema da Fronteira (três camadas:
órbitas não-compactas divergem; componentes desconexas não se fixam — com a assimetria
P/T enunciada; parte compacta protege índices discretos) → corolários (sem-escala,
sem-fóton, sem-quiralidade, eixo-sem-seta, matéria topológica) → aplicações (Modelo
Padrão §5.6; matéria condensada §4).

O programa muda de categoria nos termos do próprio charter: **de coleção disciplinada
para teoria com núcleo dedutivo**, com o escopo do núcleo declarado (cinemático; a
dinâmica continua sendo medida, como deve ser). A frase para os papers, quando o delta
editorial for autorizado: *"os resultados negativos do programa não são acidentes
independentes; são corolários de um único teorema de fronteira sobre a assinatura e a
topologia do grupo de isometrias — e os positivos são os invariantes discretos da sua
parte compacta."*

**Gates alterados por este resultado:**
- **N3 (Wen-complement): LIBERADO** — o enunciado de assinatura (§4) é o que o paper
  precisava.
- **N4 (SJ): LIBERADO para pré-registro próprio, com upgrade** — P1 mostra que a
  quantização covariante não é escolha, é a única compatível com o princípio.
- **N1, N2:** seguem como estavam (independentes do veredito, já autorizados).
- Linha de escala: a porta única (direção relevante sob thinning) **fechou** (§3.3).

## Apêndice A — Delimitação substrato vs. matéria (registro Q13)

Desligando o Axioma 2, sobra exatamente a CST pura (dimensão, curvatura, d'Alembertiano,
everpresent-Λ) MAIS o setor de colapso — que usou o espectro causal NU (GOE, ⟨r⟩→0.53)
[medido, COLAPSO_SR]: a convergência com a SR é propriedade do substrato, não da matéria.
Tudo no §1–§6 que usa só o Axioma 1 (camadas 1 e 2 inteiras, N0(b), N0(c), N0(d) Lemas
1–2) é física do substrato; a camada 3 é o setor de matéria condicional ao Axioma 2.

## Apêndice B — Lacunas técnicas declaradas (o que este documento NÃO prova)

1. **Hauptvermutung discreta** (§2.1): a recuperação completa "order+number ⇒ geometria"
   permanece conjectura da literatura; a tese usa apenas o Lema 0 (mais fraco e
   verificável), mas a âncora contínua completa depende dela.
2. **Proposição 3 de N0(b)** é rigorosa no nível dos momentos fatoriais; o nível de lei
   vem do teorema de limites de thinning citado (condições: intensidade finita,
   ergodicidade) — a combinação está esboçada, não redigida como prova única.
3. **RG conjunta substrato+matéria** (o fluxo de J e a derivação analítica da EFT) não
   foi construída — é o item aberto pré-existente (Perguntas I §3/§20), não desta
   campanha.
4. **CPT da EFT emergente** (§5.5) é assumido do contínuo, não derivado do substrato.
5. **Lema 2** formaliza "reconstrução espacial ⇒ dados de Gram" no nível do que as
   construções conhecidas (MRS, contagens de intervalos) de fato produzem; um teorema de
   exaustão ("TODA reconstrução intrínseca é não-assinada") está esboçado via Lema 1
   (P-invariância pontual do algebra de observáveis) — que é o argumento forte; a
   redação de livro-texto dos dois lemas como um só enunciado fica para o paper-núcleo.
6. O **teorema combinatório** (lado COMBINATÓRIA do binário: laços de dimensão finita em
   posets aleatórios/triangulações) segue pendente como registrado na síntese das sete
   mortes — não era alvo de N0.

---

## ADENDO N0′ (2026-07-01) — edições mandatórias do stress test adversarial

> N0′ executado (ver `../N0_STRESS_TEST/RESULTADO.md`): 6/6 alvos SOBREVIVEM, nenhuma
> morte pré-registrada disparou; status do princípio sobe para **"atacado e de pé"**.
> O ataque encontrou um degrau implícito real e um qualificador estrutural. Este adendo
> EDITA o documento (não apaga), como manda o charter.

**A1 — Precisão do Lema 2 (absoluto vs. relativo).** "Espaço sem sinal" significa sem
sinal ABSOLUTO. Quiralidade RELATIVA de dois aglomerados rígidos, χ(A,B) ∈ {±1}, É
intrínseca (dados de Gram conjuntos fixam a configuração a menos de UMA reflexão global;
o produto de sinais é invariante) — e é P-PAR. O Lema 2 fica intacto (nenhum funcional
P-ímpar existe); mas o corolário §5.3 pulava o caso do condensado quiral relacional.

**A2 — Lema 3 (novo; fecha o degrau).** Na classe (Axiomas 1–2) não há ordem quiral de
longo alcance: a geometria é *quenched* (o sprinkling não responde ao campo interno) e,
sob Poisson, orientações locais de regiões disjuntas são independentes e
localmente-refletíveis ⇒ ⟨χ⟩ = 0 e ⟨χχ⟩ = 0 a toda distância — exclusão por
INDEPENDÊNCIA DA MEDIDA, não por simetria. [prova-esboço] Com A1+A2 o corolário de
quiralidade fecha em forma mais forte. **Fronteira declarada:** para geometria DINÂMICA
(fora do Axioma 1), o Lema 3 não se aplica — a porta relacional vai para o flanco
combinatório/dinâmico (B.6).

**A3 — Qualificador estrutural da Prop. 2.** "Intensidade finita" é load-bearing:
processos ergódicos de intensidade infinita (clusters de cauda pesada) escapam do
teorema de thinning. **Lema δ₀:** eles são inconstruíveis na classe invariante — órbitas
não-compactas não portam medida de probabilidade invariante ⇒ a única distribuição de
deslocamento/cluster invariante é δ₀ ⇒ não há dressing invariante não-trivial. A mesma
não-compacidade da camada 1 protege a Prop. 2. [prova-esboço]

**A4 — Corolários novos (ganhos do alvo 3 de N0′):**
- **Classe GOE do espectro causal** (FS2, ⟨r⟩→0.53 [medido]): camada 2 — lei
  T-estatisticamente simétrica + sem estrutura complexa/U(1) (corolário sem-fóton) ⇒
  operadores reais simétricos ⇒ classe ortogonal, não GUE/GSE. O princípio fixa a
  CLASSE; a universalidade dentro dela é RMT. [prova-esboço]
- **Expoente frac_B ∝ H²** (E6c/E6e, R²=0.984–0.997 [medido]): frac_B é contagem
  não-assinada (T-par) e a dualização de ordem mapeia H↔−H mantendo a lei ⇒ frac_B é
  função PAR de H ⇒ termo líder H², dada analiticidade (zero exato no flat por camadas
  1+2). O expoente medido vira derivado. [prova-esboço]

**A5 — Previsão nova P7:** quiralidade emergente, em QUALQUER substrato de ordem, só
pode ser fase relacional (condensado: domínios, paredes ℤ₂, restaurável), nunca LEI —
porque a lei é P-par por uniformidade (§2.1 de N0′) em toda classe intrínseca. A
quiralidade exata e jamais restaurada do neutrino é evidência estrutural contra qualquer
origem de quiralidade em substrato causal. [falseável]
