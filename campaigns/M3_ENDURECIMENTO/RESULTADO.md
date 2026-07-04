# M3 — ENDURECIMENTO DO APÊNDICE B: resultado

**Data:** 2026-07-02 · **Pasta:** `FRONTEIRA_COMPACTA/M3_ENDURECIMENTO/`
**Roadmap:** `../ROADMAP_V2.md` item M3 ("analítico: costura Prop. 3
(nível-de-lei), redação livro-texto Lemas 0/2 (+Lema 3, δ₀)"). Zero código.
**Efeito:** os [sketch] do paper-núcleo (M4) sobem de grau onde a prova fecha;
o paper ganha o Apêndice A (provas); onde NÃO fecha, o resíduo é declarado.

---

## Quadro de vereditos

| Peça (Apêndice B de N0) | Antes | Depois | Resíduo declarado |
|---|---|---|---|
| E1. Lema do par (Lema 0) | [sketch] | **[teorema]** nas duas metades | constante m_d: existência por Kingman, valor [literatura/medido] |
| E2. Exaustão de reconstruções (B.5) | [sketch] | **[teorema]** (pushforward, 5 linhas) | nenhum — o argumento forte fecha |
| E3. Lema 3 quenched (N0′-A2) | [sketch] | **[teorema] p/ estimadores locais** | estimadores com moldura comum (frame-cluster): permanece [sketch] |
| E4. Lema δ₀ (N0′-A3) | [sketch] | **[teorema]** (Weil, unicidade de medida invariante) | nenhum |
| E5. Prop. 3 thinning (B.2) | [sketch] | **[teorema]** (funcionais de Laplace + Kallenberg; autovalores p^{α/d}) | direções crescentes: excluídas por existência, não classificadas |
| E6. Bibliografia | "a conferir" | conferida + 3 entradas novas | — |

O que M3 NÃO toca (fora de escopo, permanecem abertos): Hauptvermutung (B.1),
RG conjunta substrato+matéria (B.3), CPT (B.4), teorema combinatório (B.6 —
resolvido por M1 em outro nível).

---

## E1. Lema do par — redação livro-texto

**Setup.** Φ = processo de Poisson de densidade ρ em M^d; P↑ = grupo de
Poincaré ortócrono (preserva orientação temporal; inclui reflexões espaciais).

**(a) Par tipo-tempo: o invariante completo é Δτ, com sinal.** [teorema]
P↑ age transitivamente sobre pares ordenados tipo-tempo de mesmo tempo próprio:
translade x à origem; um boost leva y−x à forma (Δτ, 0⃗); rotações conectam
quaisquer dois desses. O estabilizador do par ordenado é SO(d−1) (rotações em
torno do eixo). Logo toda função intrínseca de um par causal ordenado é função
de Δτ; e a ordem (quem precede) é ela própria um dado intrínseco — o SINAL.

**(b) O intervalo é estruturado.** [teorema + literatura] O intervalo de
Alexandrov I(x,y) tem volume V_d = c_d Δτ^d (constante de dimensão; Surya
Living Rev.) ⇒ N(x,y) ~ Poisson(ρ c_d Δτ^d) — estimador do módulo. O
comprimento da cadeia máxima satisfaz L(x,y)/(ρ^{1/d}Δτ) → m_d q.c. e em L¹:
existência do limite pelo teorema ergódico subaditivo de Kingman (a cadeia
máxima é superaditiva sob concatenação de intervalos); cotas e valor de m_d:
Brightwell–Gregory, PRL 66, 260 (1991); em d=2, m_2 = 2 exatamente (problema
de Ulam, Vershik–Kerov/Logan–Shepp).

**(c) Par tipo-espaço: um bit, e o entorno é não-assinado.** [teorema]
A única relação intrínseca q.c.-definida do par é a incomparabilidade (1 bit).
Para o entorno: coloque o par em (0, (0,s,0⃗)). O estabilizador linear do
vetor tipo-espaço é o grupo ortogonal do complemento Lorentziano
O(d−2,1)-tipo, que CONTÉM reflexões transversais R: (t, s-eixo, u⃗) ↦
(t, s-eixo, Ru⃗), R ∈ O(d−2), det R = −1 — elementos de determinante espacial
−1 que preservam a orientação temporal. Cada um é um isomorfismo de ordem de
toda realização (preserva cones e orientação temporal) e preserva a lei de Φ.
Logo toda estatística intrínseca do par-mais-entorno é R-invariante: nenhuma
"orientação transversal" do entorno de um par tipo-espaço é dado intrínseco.
Combinado com (a): reconstruções espaciais produzem apenas estimativas de
|s²| (ex.: o estimador de distância tipo-espaço de Rideout–Wallden, CQG 26,
155013 (2009), que é função simétrica de contagens) — e uma configuração
determinada por distâncias mútuas está fixada a menos do grupo ortogonal
completo, reflexões incluídas (rigidez de Gram/Schoenberg, clássica). ∎

**Slogan provado:** tempo com sinal e estrutura; espaço sem sinal e sem
estrutura (além de |s²| estatístico).

## E2. Teorema de exaustão (o Lema 2 forte — fecha B.5)

A versão [sketch] de N0 enumerava reconstruções conhecidas (MRS, contagens)
e verificava que todas produzem dados de Gram. A versão forte dispensa a
enumeração:

**Teorema (exaustão por pushforward).** [teorema] Seja O qualquer observável
intrínseco — função mensurável da classe de isomorfismo de (C, ≺, n). Seja g
qualquer isometria de M^d que preserva a orientação temporal, INCLUSIVE as de
determinante espacial −1 ("tipo-P"). Então O(gΦ) = O(Φ) para TODA realização
Φ, e a ação induzida de P sobre os dados intrínsecos é a identidade.
Consequentemente, um observável "P-ímpar" (O∘P = −O) satisfaz O = −O ⇒ O ≡ 0.

*Prova.* g preserva cones e orientação temporal ⇒ x ≺ y ⇔ gx ≺ gy ⇒ g realiza
um isomorfismo (C_Φ, ≺, n) ≅ (C_{gΦ}, ≺, n∘g⁻¹). O depende só da classe de
isomorfismo ⇒ O(gΦ) = O(Φ). A ação de P no espaço de classes é trivial; ser
ímpar sob a identidade força O ≡ 0. ∎

*Escopo.* O teorema fecha TODA reconstrução (passada, presente ou futura) de
uma quiralidade absoluta: não há o que enumerar. O que ele NÃO fecha (e A1 de
N0′ já apontava): a quiralidade RELATIVA χ(A,B) de dois aglomerados, que é
P-PAR — objeto do E3.

## E3. Lema 3 (quenched) — teorema condicional + resíduo declarado

**Definição.** Regiões limitadas disjuntas A, B ⊂ M^d. Um *estimador local de
quiralidade em A* é um funcional χ_A de Φ∩A com valores em {−1, 0, +1}, ímpar
sob alguma isometria r_A de A que reverte orientação espacial e preserva o
tempo (ex.: A = cilindro D×I, r_A = reflexão espacial diametral):
χ_A(r_A Φ_A) = −χ_A(Φ_A).

**Teorema (sem LRO quiral para estimadores locais).** [teorema] Para o
sprinkling de Poisson e quaisquer A, B limitados disjuntos:
E[χ_A χ_B] = E[χ_A]·E[χ_B] = 0 — em TODA separação, não só assintoticamente.

*Prova.* (i) Independência completa do PPP: Φ∩A e Φ∩B são independentes para
A∩B = ∅ ⇒ E[χ_Aχ_B] = E[χ_A]E[χ_B]. (ii) r_A preserva Lebesgue em A ⇒
Φ_A ~ r_AΦ_A em lei ⇒ E[χ_A] = E[χ_A(r_AΦ_A)] = −E[χ_A] ⇒ E[χ_A] = 0. ∎

**Resíduo declarado (o que permanece [sketch]).** Estimadores de quiralidade
relativa que usam uma moldura comum F (dados causais de terceiros ligando A a
B) não são funcionais de regiões disjuntas: condicionado em F, a reflexão
local de A altera as relações A–F e o argumento (ii) não passa. Para esses, o
fechamento continua o de N0′-A2 ([sketch] por independência-da-medida), e a
fronteira para geometria DINÂMICA (fora do Axioma 1) segue declarada. O
teorema acima cobre todos os estimadores locais — que é a classe fisicamente
mensurável padrão.

## E4. Lema δ₀ — redação livro-texto (fecha o qualificador da Prop. 2)

**Teorema.** [teorema] A única medida de probabilidade sobre M^d invariante
sob o grupo de Lorentz ortócrono L↑ = SO⁺(d−1,1) é δ₀. Consequentemente não
existe "dressing" invariante não-trivial (deslocamentos de cluster,
offspring): a distribuição de deslocamento invariante é δ₀ e processos de
cluster invariantes de intensidade infinita são inconstruíveis na classe.

*Prova.* As órbitas de L↑ em M^d são: {0}; as folhas de massa H±; as
componentes do cone de luz; os hiperbolóides de uma folha S_s. Cada órbita
não-trivial é um espaço homogêneo G/H com G = SO⁺(d−1,1) unimodular
(semissimples) e H unimodular (SO(d−1) compacto nas folhas de massa;
SO⁺(d−2,1) nas tipo-espaço; ISO(d−2)-tipo no cone). Pelo teorema de Weil
(unicidade da medida relativamente invariante; Folland, *A Course in Abstract
Harmonic Analysis*, Thm. 2.49), cada órbita carrega medida G-invariante única
a menos de escala — a medida de Lorentz padrão — que é INFINITA (órbitas
não-compactas). Logo nenhuma órbita não-trivial porta probabilidade
invariante. Desintegrando μ invariante sobre o espaço de órbitas (ação suave,
órbitas localmente fechadas), toda a massa cai na única órbita compacta {0}:
μ = δ₀. ∎

## E5. Prop. 3 — a costura de nível-de-lei (thinning RG)

Operadores sobre processos pontuais em M^d: R_p = thinning independente
(retém com prob. p); S_a = escala x ↦ ax. O passo de RG compensado é
T_p := S_{p^{1/d}} ∘ R_p (contração restaura a intensidade).

**(i) Ponto fixo exato.** [teorema] Em funcionais de Laplace,
L_{R_pΦ}[f] = L_Φ[−log(1 − p(1−e^{−f}))]; para o PPP(ρ),
L[f] = exp(−ρ∫(1−e^{−f})): o thinning dá exp(−pρ∫(1−e^{−f})) e a contração
S_{p^{1/d}} multiplica ∫ por p⁻¹ ⇒ T_p PPP(ρ) = PPP(ρ), exatamente, para todo
p. Com BHS, é o único ponto fixo Lorentz-invariante.

**(ii) Atrator no nível de LEI.** [teorema, literatura] O teorema de limites
de thinning (Kallenberg, *Random Measures* 2017; Mecke) é enunciado em
convergência em distribuição: thinning iterado com compensação converge para
um processo de Cox dirigido pelo limite da intensidade amostral. Para Φ
invariante ERGÓDICO de intensidade finita λ, o teorema ergódico espacial dá
intensidade amostral → λ constante ⇒ Cox(λ·Leb) = PPP(λ). A costura que
faltava é só esta observação: a hipótese de ergodicidade converte o Cox do
teorema em Poisson, e a convergência já é de lei (funcionais de Laplace), não
de momentos. Intensidade infinita: excluída na classe invariante pelo E4.

**(iii) Classificação de direções com autovalores.** [teorema] Densidades de
momento fatorial transformam como (T_p ρ)_k(x) = p^k a^{−kd} ρ_k(x/a) =
ρ_k(x/a) com a = p^{1/d} (compensação exata) ⇒ correlações truncadas g_k
sofrem dilatação PURA de argumentos: g_k ↦ g_k(·/a), 1/a = p^{−1/d} > 1.
Autofunções homogêneas g(x) = |x|^{−α}: autovalor p^{α/d} < 1 para todo
α > 0 — **toda cauda decrescente é irrelevante, com autovalor explícito**;
α = 0 (constante) é a superseleção de intensidade (mistura de Cox,
não-ergódica; e intrinsecamente invisível em M^d pela ρ-independência da lei
da ordem); o nível k=1 (a própria ρ) é a direção marginal = a unidade.
Correlações crescentes (α<0): não correspondem a processo pontual invariante
de momentos localmente finitos — excluídas por existência (declarado; não
classificadas).

## E6. Bibliografia conferida (para o paper-núcleo)

Confirmadas: Malament JMP 18, 1399 (1977); HKM JMP 17, 174 (1976); BHS MPLA
24, 2579 (2009); Surya LRR 22, 5 (2019); Levin–Wen PRB 71, 045110 (2005);
Wigner Ann. Math. 40, 149 (1939); Janson Combinatorica 31, 529 (2011);
Brightwell in *Surveys in Combinatorics 1993* (LMS LNS 187); Rideout–Sorkin
PRD 61, 024002 (2000); ABBJ Ann. Appl. Probab. 4, 108 (1994);
Bollobás–Brightwell SIAM J. Discrete Math. 10, 318 (1997); Kallenberg
*Random Measures* (2017); Elitzur PRD 12, 3978 (1975).

Adicionadas (usadas pelas provas novas): Brightwell–Gregory PRL 66, 260
(1991) — cadeia máxima; Rideout–Wallden CQG 26, 155013 (2009) — distância
tipo-espaço; Folland *AHA* (1995) — Weil/medidas invariantes.

## O que muda no paper-núcleo (edições executadas nesta sessão)

1. **Apêndice A (provas)** com as versões concisas de E1(c), E2, E3, E4 e
   E5(i,iii) — o paper ganha autossuficiência matemática nos lemas de base.
2. Upgrades de grau: Lema do par → [theorem] (m_d citado); Lema de Gram →
   reescrito com o teorema de exaustão; Lema quenched → [theorem, estimadores
   locais] com resíduo declarado; Props. de thinning → [theorem] com
   autovalores p^{α/d}.
3. Bibliografia: 3 entradas novas.
4. O Teorema da Fronteira permanece "assembled from cited components" — a
   montagem das camadas como enunciado único é honesta como está; o que
   mudou é que os componentes agora têm prova no apêndice ou citação exata.

**Pendências que M3 deixa (para a lista honesta, sem mudança):** B.1
Hauptvermutung; B.3 RG conjunta; B.4 CPT; resíduo frame-cluster do E3.
