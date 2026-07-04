# LEVANTAMENTO — existe um princípio genuinamente *pré-causal* que escape do teorema binário?

**Data:** 2026-06-30
**Natureza:** levantamento e análise teórica pura. **Nenhum código foi escrito ou
executado.** Nenhum experimento desenhado. O produto é um mapa da literatura real e um
veredito pré-registrado (§4 do charter).

**Disciplina aplicada:** nenhum candidato foi escolhido ou favorecido por "dar à TEIC o
que ela quer". A pergunta foi sempre *"este princípio é genuinamente pré-causal, e o que
ele de fato entrega quando lido sem viés de resultado?"* — nunca *"qual me dá escala /
fóton / gauge?"*.

---

## 0. Por que esta categoria estava, a priori, fora do escopo

O teorema parcial (Campbell–Mecke + invariância de Poincaré, em
`TEIC/docs/campaigns/IMPOSSIBILIDADE_PARCIAL/` e
`REPULSAO_LORENTZ/docs/FRONTEIRA_CONHECIDA.md`) e seu refinamento binário (BOOST
não-compacto / colapso COMBINATÓRIO, em `SINTESE_SETE_MORTES/`) **assumem uma medida de
pontos já definida sobre um espaço-tempo causal já dado** (hipótese (i): o *sprinkling*).
Um princípio onde a própria ordem causal **emerge** de algo mais primitivo não tem, *a
priori*, onde o Campbell–Mecke atue — não há medida-sobre-espaço-tempo-causal no passo
zero.

Isto **não é garantia de sucesso**: é só a delimitação precisa de qual classe de
candidato está fora do que já foi provado fechado. A pergunta operacional desta tarefa
foi: *algum programa real publicado realmente fica nessa classe quando destrinchado, ou
todos reintroduzem uma ordem causal / medida em algum passo intermediário?*

O teste decisivo para cada candidato é o mesmo que identificou `N(i,j)` como "Δτ
disfarçado": **localizar o passo onde a causalidade entra**. Se ela entra como axioma,
como escolha de grupo, como teoria de fundo, ou como propriedade especial assumida das
regras, então o candidato **não é pré-causal** — é uma das nove famílias com roupagem
nova, ou tem seu próprio *no-go*.

---

## 1. Candidatos investigados

| # | Candidato | Causalidade é... | Veredito §4 |
|---|---|---|---|
| 1 | Causal sets (programa Sorkin, *order + number = geometry*) | **AXIOMA** | REINTRODUZ |
| 2 | Energetic Causal Sets (Cortês–Smolin) | **PRIMITIVO fundamental** (declarado) | REINTRODUZ |
| 3 | Group Field Theory / tensor models | put-in via grupo, OU não-derivada | NO-GO CONHECIDO (mean-field) + REINTRODUZ (assinatura) |
| 4 | LQG / spin networks / spin foams | **espacial** derivada; tempo NÃO (problema do tempo) | REINTRODUZ / NO-GO (problema do tempo) |
| 4b | Causal spin foams (Markopoulou–Smolin) | **INPUT** (orientação micro-local) | REINTRODUZ |
| 5 | Espaço-tempo a partir de emaranhamento / holografia (AdS/CFT, MERA, ER=EPR) | **assumida na fronteira** (CFT Lorentziana) | REINTRODUZ + NO-GO CONHECIDO |
| 6 | Modelo de Wolfram (hipergrafo + invariância causal) | **emerge** do grafo causal de updates | REINTRODUZ (grafo causal = causal set) / depende de invariância causal assumida |

**Resultado global: NENHUM CANDIDATO GENUÍNO** (§4, último caso). Detalhamento abaixo.

---

## 2. Análise candidato a candidato (três perguntas da §3)

### 2.1 — Causal sets como "física de informação pura"

**Formulação real.** O programa de *causal set theory* (Bombelli, Lee, Meyer, Sorkin
1987; revisões de Sorkin 2003 [gr-qc/0309009], Henson 2006, Surya *Living Reviews* 2019
[arXiv:1903.11544]) define o substrato como um **conjunto parcialmente ordenado localmente
finito** `(C, ≺)`, onde `≺` é interpretada como *precedência causal*. O lema central é
*"order + number = geometry"*: a ordem dá a estrutura conforme (causal), a contagem dá o
volume.

**P1 — Causalidade é derivada ou assumida?** **ASSUMIDA, como axioma fundamental.** A
relação `≺` é a estrutura primitiva do conjunto; não emerge de nada. A correspondência com
o contínuo é o *sprinkling* de Poisson (Bombelli–Henson–Sorkin 2009 [arXiv:gr-qc/0605006])
sobre uma variedade Lorentziana **já dada** — exatamente a hipótese (i) do nosso teorema.
A linha de "derivar a ordem de máxima entropia" que a busca revelou
(arXiv:2102.03906, Sun–Schölkopf) é **teoria de informação / inferência causal**, não
física pré-geométrica — define entropia *condicionada a uma ordem causal já dada*, ou seja,
pressupõe `≺`. Não é uma derivação da ordem a partir de um princípio mais primitivo.

**P2 — Escala / criticalidade / gauge?** O programa tem dinâmica (Classical Sequential
Growth, Rideout–Sorkin 2000 [gr-qc/9904062]) e resultados fenomenológicos (predição de Λ
da ordem da flutuação de volume, Sorkin). **Mas a estrutura de escala é justamente o que
nossa própria linha já testou e matou** (CSG na fila Rideout-Sorkin: tipo-árvore, sub-MF;
ver memória `rs-trigger-csg-coordination`).

**P3 — Escapa do teorema?** **Não — é o protótipo do que o teorema fecha.** O *sprinkling*
de Poisson é literalmente a hipótese (i). Os próprios autores documentam a **não-localidade
inerente** dos causal sets (vínculos a vizinhos arbitrariamente distantes no boost — Sorkin,
"causal set ⇒ non-locality"; é a base do d'Alembertiano não-local de Sorkin–Benincasa).
Essa não-localidade **é** a não-compacidade de Lorentz do nosso §2.

**Veredito: REINTRODUZ.** Causalidade é o axioma; a medida é o Poisson. Família já testada.

---

### 2.2 — Energetic Causal Sets (Cortês–Smolin)

**Formulação real.** Cortês & Smolin, *Energetic Causal Sets*, PRD 90, 044035 (2014)
[arXiv:1308.2206]; *Quantum Energetic Causal Sets* [arXiv:1409.xxxx]; versão dimensional
superior [arXiv:2309.08694]. Eventos carregam energia-momento, transmitida ao longo de
links causais e conservada em cada evento. **O espaço-tempo emerge só no nível
semiclássico** — fundamentalmente *não há espaço-tempo*.

**P1 — Derivada ou assumida?** Aqui está a armadilha que o charter (§3.1) pede para
detectar. O programa **parece** pré-geométrico ("não há espaço-tempo fundamental"). Mas o
artigo afirma textualmente: *"nem localidade nem não-localidade são conceitos primários —
**só causalidade existe no nível fundamental**"* (1308.2206, abstract/§1). Ou seja: **a
causalidade é o primitivo declarado, não algo derivado.** É o **oposto** de pré-causal — é
causalidade-como-rocha-de-fundo, com o espaço-tempo emergindo *dela*. O substrato é um
*causal set* (com energia-momento adicionada); a ordem `≺` é dada no passo zero.

**P2 — Escala / gauge?** O resultado central é a *emergência* de espaço-tempo de Minkowski
e relações de momento; correspondência 1-para-1 com uma classe de spin foams
(arXiv:1407.0032). Não há demonstração de escala emergente / criticalidade não-trivial no
sentido que a TEIC busca; o foco é a emergência da *cinemática*, não de uma transição de
fase com expoentes.

**P3 — Escapa do teorema?** **Não.** Como a ordem causal é dada e a dinâmica é um
crescimento sequencial de eventos com pesos (energia-momento), o substrato cai na categoria
**COMBINATÓRIA** da síntese binária (crescimento sequencial = mesma família do CSG e do
CDT). A adição de energia-momento é um peso sobre os links — análogo a "peso de
crescimento", que a própria nova-teoria (`teoria-cdt-nova`, FS-3D) já mostrou ser
indistinguível de CDT-com-peso.

**Veredito: REINTRODUZ.** Não é pré-causal; é causalidade-primeiro com rótulo de
emergência aplicado ao espaço-tempo, não à ordem.

---

### 2.3 — Group Field Theory (GFT) e tensor models

**Formulação real.** GFT é uma teoria quântica de campos sobre uma variedade de grupo de
Lie (SU(2), SO(4), ou SL(2,ℂ) no caso Lorentziano), cujos diagramas de Feynman são duais a
complexos celulares interpretados como espaço-tempos discretos; a dinâmica é uma soma sobre
geometrias discretas ponderadas por amplitudes (revisões: Oriti 2011; Carrozza; Gurau
*Random Tensors* 2016; revisão recente arXiv:2404.07834). Tensor models são o esqueleto
combinatório (sem dados de grupo). **É o candidato mais genuinamente *pré-geométrico* da
gravidade quântica atual: não há espaço-tempo de fundo algum** — geometria e (em princípio)
causalidade emergem de uma transição de fase ("geometrogênese").

**P1 — Derivada ou assumida?** Aqui há **dois sub-casos, ambos desfavoráveis**:
- **(a)** A esmagadora maioria dos modelos bem-desenvolvidos é de **assinatura Euclidiana**
  (correspondência tensor↔gravidade Euclidiana em D≥3 — confirmado na busca via
  arXiv:2404.07834 e revisões). Não há causalidade/assinatura Lorentziana — não há "antes/
  depois" a derivar. O Euclidiano é genuinamente sem-causalidade, mas por *ausência*, não
  por *emergência*.
- **(b)** Para obter assinatura Lorentziana, **escolhe-se o grupo** (SL(2,ℂ) em vez de
  SO(4)) — i.e., a estrutura causal/Lorentziana é **um INPUT via a escolha do grupo de
  estrutura**, não um resultado derivado de um princípio mais primitivo. É o mesmo passo
  que em spin foams (Barrett–Crane / EPRL Lorentziano impõe SL(2,ℂ)). A causalidade entra
  pela porta do grupo.

Em nenhum dos dois a ordem causal *emerge* de algo pré-causal: ou está ausente (Euclidiano)
ou é imposta pela escolha de grupo (Lorentziano).

**P2 — Escala / criticalidade?** Esta é a parte decisiva e **diretamente análoga às nossas
próprias mortes**. A geometrogênese é uma transição de fase de condensado de GFT. A
literatura própria do programa documenta que a transição, no regime tratável, é
**campo-médio**: *"Mean-Field Phase Transitions in Tensorial Group Field Theory Quantum
Gravity"* (Pithis, Marchetti et al., ~2023, encontrado na busca; também Benedetti–Gurau,
Carrozza sobre o grupo de renormalização de GFT). A cosmologia de condensado de GFT
(Oriti, Gielen, Sindoni) é construída precisamente no regime de **aproximação de
campo-médio**. Ou seja: o ponto onde a geometria emerge é **mean-field** — exatamente a
"morte" que toda a nossa linha vem encontrando (escala-xi, CDT, NESS-B, cinemática-4D).

**P3 — Escapa do teorema / tem no-go?** O teorema parcial *literal* (§2) não se aplica
(não há *sprinkling*). **Mas o programa tem seu próprio resultado restritivo documentado e
equivalente em espírito:** o regime de emergência é mean-field (P2). A morte que a §4
chama de "no-go conhecido" não precisa ser o teorema de boost — pode ser outra obstrução
que impeça o que se busca, e a **escala mean-field do condensado de GFT é exatamente
isso**. Além disso, a assinatura Lorentziana ser um input de grupo (P1b) significa que, no
que tange à *causalidade*, GFT **reintroduz** a estrutura por escolha.

**Veredito: NO-GO CONHECIDO (mean-field) + REINTRODUZ (assinatura via grupo).** É
pré-geométrico de verdade, mas (i) não deriva causalidade — ausente ou imposta por grupo —
e (ii) sua emergência geométrica é mean-field na própria literatura. Não passa nos três
critérios da §3 favoravelmente.

---

### 2.4 — LQG / spin networks / spin foams

**Formulação real.** LQG quantiza a relatividade geral canônica; **redes de spin**
(spin networks) são autoestados dos operadores de área e volume — dão **geometria
*espacial* quântica**. Spin foams são a versão covariante (história de redes de spin),
soma sobre 2-complexos com amplitudes (Barrett–Crane, EPRL/FK). Revisões: Rovelli–Vidotto
*Covariant LQG* (2014); Perez *Living Reviews* 2013 [arXiv:1205.2019].

**P1 — Derivada ou assumida?** A **geometria espacial** emerge de uma álgebra de operadores
(genuíno). Mas a **causalidade / evolução temporal NÃO é derivada** — é o notório
**"problema do tempo"** da gravidade quântica canônica: a dinâmica é codificada na
*restrição Hamiltoniana* `Ĥ|ψ⟩ = 0` (formalismo "congelado", Wheeler–DeWitt). Não há
"antes/depois" fundamental; a ordem causal **não emerge** — ela é um problema **não
resolvido**, não um resultado. Nos spin foams padrão, a maioria dos modelos
**de-enfatiza a estrutura causal** (confirmado na busca: "most studies of spin foam models
de-emphasize the role of causal structure"; Pérez–Rovelli sobre orientação).

**P2 — Escala / gauge?** LQG entrega geometria discreta e gauge (é uma teoria de gauge
SU(2)); mas a recuperação do limite contínuo / semiclássico e a fixação da ordem das
transições são problemas abertos, novamente com sinais de comportamento mean-field nas
abordagens de GFT-renormalização (§2.3, mesma comunidade).

**P3 — Escapa do teorema?** Não há *sprinkling*, então o teorema literal não se aplica.
Mas a causalidade **não é derivada** (P1: problema do tempo) — então o candidato falha o
critério §3.1 antes mesmo de chegar à escala. O "no-go" relevante aqui é o próprio
**problema do tempo**, documentado há décadas (Kuchař, Isham 1992 [gr-qc/9210011]).

**Veredito: REINTRODUZ / problema-do-tempo.** A causalidade não emerge; é um problema
aberto, não um output.

#### 2.4b — Causal spin foams (Markopoulou–Smolin) — sub-caso explícito

A variante que *tenta* causalizar (Markopoulou–Smolin 1997; Markopoulou
[gr-qc/9704013]) define modelos de spin foam causais **assumindo uma estrutura causal
micro-local, codificada na orientação das redes de spin** (confirmado na busca direta).
Isto é **um INPUT explícito**: a orientação (= a seta causal local) é dada à mão, não
derivada. As regras de propagação satisfazem restrições causais "motivadas pela física
Lorentziana clássica" — i.e., a causalidade é importada do contínuo, não emergente.

**Veredito: REINTRODUZ.** Causalidade é input (orientação). Idêntico em estrutura à
foliação/orientação já mapeadas.

---

### 2.5 — Espaço-tempo a partir de emaranhamento / holografia (AdS/CFT, MERA, ER=EPR)

**Formulação real.** A geometria do *bulk* (incluindo sua estrutura causal) emerge da
estrutura de emaranhamento de um sistema quântico de fronteira (Van Raamsdonk 2010
[arXiv:1005.3035]; Ryu–Takayanagi 2006; Swingle MERA 2009 [arXiv:0905.1317]; Maldacena–
Susskind ER=EPR 2013 [arXiv:1306.0533]; Almheiri–Dong–Harlow código corretor de erros
2014 [arXiv:1411.7041]).

**P1 — Derivada ou assumida?** O *bulk* emerge — mas **a fronteira é uma teoria de campos
conforme (CFT) Lorentziana, com sua própria estrutura causal (microcausalidade /
localidade) já embutida.** A busca confirma: a causalidade do *bulk* deve ser **consistente
com a causalidade da fronteira** (arXiv:2504.15910, "Consistency between Bulk and Boundary
Causalities"; Gao–Wald 2000 sobre causalidade de fronteira). Ou seja, a causalidade do
*bulk* **emerge da causalidade da fronteira** — que é **assumida** (a CFT é uma QFT
relativística padrão, com cone de luz e microcausalidade no passo zero). A causalidade não
é derivada de algo pré-causal: é *transportada* da fronteira para o *bulk*. Além disso, o
programa **requer um fundo AdS** (constante cosmológica negativa) — uma teoria de fundo,
exatamente o que a §2.2 do charter exclui ("precisa de background ⇒ reintroduz o que o
teorema cobre").

**P2 — Escala / gauge?** O programa é riquíssimo (dicionário holográfico, código corretor
de erros, RT). Mas tudo isso pressupõe a CFT e o AdS — não é uma escala *emergente de algo
pré-causal*.

**P3 — Escapa / no-go?** Não escapa (P1: causalidade de fronteira assumida + fundo AdS). E
**tem no-gos documentados**: a busca confirma *"several No Go Theorems proven"* sobre
recuperar a geometria completa só da entropia de emaranhamento (HRT e generalizações;
e.g. trabalhos sobre os limites da reconstrução do *bulk*). A holografia em fundo
**não-AdS / dependente do tempo (cosmológico)** — que seria o caso de interesse para um
substrato sem causalidade prévia — é justamente onde o programa é mais frágil e sem
dicionário estabelecido.

**Veredito: REINTRODUZ (causalidade de fronteira + fundo AdS) + NO-GO CONHECIDO
(reconstrução).** Não é pré-causal: é geometria-de-bulk a partir de uma fronteira
causal-relativística dada.

---

### 2.6 — Modelo de Wolfram (hipergrafo + invariância causal)

**Formulação real.** Reescrita de hipergrafos: um hipergrafo espacial **sem métrica**
sofre reescritas locais; o **grafo causal** (ordem parcial dos eventos de update) **emerge**
da estrutura de dependência entre as reescritas. Lorentz-invariância é apresentada como
*consequência* da **invariância causal** (confluência) (Wolfram 2020; Gorard
*Some Relativistic and Gravitational Properties of the Wolfram Model* 2020; Gorard–Dehghani
*Algorithmic Causal Sets* [arXiv:2011.12174]).

**P1 — Derivada ou assumida?** **Este é o candidato mais genuinamente pré-causal da lista.**
O hipergrafo espacial não tem métrica nem ordem; o grafo causal *de fato emerge* da
dinâmica de reescrita. A causalidade não é axioma (≠ causal sets) nem input de orientação
(≠ causal spin foams) nem importada de uma fronteira (≠ holografia). **Porém**, dois
problemas:
- **(a)** A invariância de Lorentz é derivada **da invariância causal** (confluência) — que
  é uma **propriedade especial assumida das regras**, não genérica. Regras sem invariância
  causal não dão Lorentz. Então "Lorentz emerge" está condicionado a *assumir* a classe
  certa de regras. Há crítica documentada (debate confluência-vs-invariância-causal;
  Gorard, *The Last Theory* #035) sobre o status — invariância causal é uma hipótese
  selecionada, não um teorema sobre regras genéricas.
- **(b)** Crucialmente para *nós*: **o objeto emergente é um grafo causal — i.e., uma ordem
  parcial de eventos — que É um causal set** (o próprio programa chama-os "algorithmic
  causal sets", arXiv:2011.12174). Uma vez que a ordem causal emergiu, a pergunta sobre
  escala/Lorentz/coordenação **torna-se a pergunta do causal set** — e a não-compacidade de
  Lorentz volta a operar sobre o grafo causal emergente. A emergência move o problema um
  passo para trás (do espaço-tempo para o grafo causal), mas **não o dissolve**: o grafo
  causal ainda é uma ordem parcial sobre a qual a coordenação/clustering se decide.

**P2 — Escala / gauge?** O programa *alega* RG, mecânica quântica (multiway), gauge — mas
estas alegações são **contestadas quanto a rigor e falseabilidade** na literatura externa
(o programa é largamente auto-publicado; crítica recorrente de não-preditividade). Não há
demonstração revisada por pares de escala emergente não-trivial no sentido da TEIC.

**P3 — Escapa / no-go?** Não há *sprinkling* (escapa do teorema literal), mas o grafo
causal emergente **é um causal set** (P1b) — logo cai sob o mesmo guarda-chuva da §2.1 no
nível emergente. Não há um *no-go* formal único e citável (o programa é jovem e
heterodoxo), mas isto **não conta como abertura** (§"O que NÃO fazer": ausência de no-go
≠ prova de possibilidade). A dependência de invariância causal assumida (P1a) e a redução
ao causal set (P1b) são as obstruções concretas.

**Veredito: REINTRODUZ no nível emergente (grafo causal = causal set) / depende de
invariância causal assumida.** É o único genuinamente pré-causal *na construção*, mas o que
ele produz é precisamente a estrutura (ordem parcial de eventos) que a nossa linha já
mapeou — e sua Lorentz-invariância repousa numa propriedade especial assumida, não
derivada.

---

## 3. O padrão único que atravessa os seis

Os seis candidatos falham por **um de dois modos**, e os dois modos são as **duas faces da
mesma moeda** que toda a linha vem encontrando:

1. **Reintroduzem a ordem causal / a medida em algum passo** (causal sets: axioma;
   energetic CS: primitivo declarado; causal spin foams: orientação-input; holografia:
   fronteira Lorentziana + fundo AdS; Wolfram: o grafo causal emergente É um causal set;
   GFT-Lorentziano: assinatura via escolha de grupo). → **Variante das nove famílias.**

2. **São genuinamente pré-causais/pré-geométricos, mas têm uma obstrução documentada** que
   impede o que se busca (GFT: emergência **mean-field** na própria literatura; holografia:
   **no-go theorems** de reconstrução; LQG: **problema do tempo** não resolvido). → **No-go
   conhecido.**

A constatação mais forte: **mesmo quando um programa consegue ser pré-geométrico de
verdade (GFT, Wolfram), a estrutura que emerge é ou (i) mean-field na transição de
emergência, ou (ii) um causal set sobre o qual a não-compacidade de Lorentz volta a operar.**
Isto é uma confirmação *externa e independente* do mecanismo binário de
`SINTESE_SETE_MORTES`: a tensão BOOST/COMBINATÓRIA não é um artefato da nossa escolha de
substratos — ela reaparece nos programas de fronteira da gravidade quântica, do outro lado,
como "mean-field na geometrogênese" e como "non-locality dos causal sets".

---

## 4. Veredito pré-registrado (§4 do charter)

> **NENHUM CANDIDATO GENUÍNO ENCONTRADO.**

Nenhum dos programas reais investigados satisfaz **favoravelmente os três critérios da §3**
simultaneamente (causalidade provadamente derivada **E** fora do escopo do teorema por
construção **E** sem no-go equivalente documentado):

- **Causal sets, Energetic Causal Sets, Causal spin foams** → causalidade **assumida**
  (axioma / primitivo / orientação-input). Falham §3.1. **REINTRODUZEM.**
- **LQG / spin foams** → causalidade **não derivada** (problema do tempo). Falham §3.1.
- **Holografia / emaranhamento** → causalidade **importada da fronteira** + **fundo AdS** +
  **no-gos de reconstrução**. Falham §3.1 e §3.3. **REINTRODUZ + NO-GO.**
- **GFT / tensor models** → genuinamente pré-geométrico, mas causalidade **ausente
  (Euclidiano) ou imposta por grupo (Lorentziano)**, e emergência **mean-field** na própria
  literatura. Falham §3.1 e §3.3. **NO-GO CONHECIDO.**
- **Modelo de Wolfram** → genuinamente pré-causal *na construção*, **mas** o grafo causal
  emergente **é um causal set** (a não-compacidade volta a operar) e a Lorentz-invariância
  repousa em **invariância causal assumida**. Falha §3.3 no nível emergente. **REINTRODUZ.**

**Este é o fechamento mais amplo possível do mapa até aqui.** A busca por física nova via
**modificação de substrato — causal OU pré-causal — está, com a informação disponível,
esgotada nos caminhos conhecidos da literatura.** Não só as nove famílias de substrato
causal estão fechadas (boost/combinatória); os programas *pré-causais* de fronteira da
gravidade quântica, quando destrinchados, ou reintroduzem a ordem causal/medida que o
teorema cobre, ou esbarram nas suas próprias obstruções documentadas (mean-field,
problema do tempo, no-gos de reconstrução).

### Ressalva de honestidade (§"O que NÃO fazer")

- **Ausência de um no-go formal único para o modelo de Wolfram não é evidência de que ele
  funcione.** É incerteza genuína: o programa é jovem, heterodoxo e largamente
  auto-publicado. A obstrução concreta identificada (grafo causal = causal set; invariância
  causal assumida) é **argumento estrutural, não teorema**. Registrado como *incerteza*,
  não como abertura promissora.
- **Não foi lido cada artigo na íntegra.** As formulações de GFT-renormalização (caráter
  mean-field da geometrogênese) e os no-gos de reconstrução holográfica foram verificados
  via abstracts/revisões e snippets de busca, não pela leitura completa das provas. O que
  é robusto: a causalidade ser axioma/primitivo/input/fronteira nos candidatos 1,2,4,4b,5 —
  isto é estrutural e bem-estabelecido. O que é mais frágil: a caracterização *quantitativa*
  do mean-field de GFT e o escopo exato dos no-gos holográficos (verificados, não auditados).

### Nenhum experimento desenhado

Conforme o charter: **nada a executar.** Se uma decisão futura quiser reabrir, o único
candidato que *constrói* sem causalidade prévia é o modelo de Wolfram — mas o passo
seguinte honesto seria **provar (analiticamente) que o grafo causal emergente herda a
não-compacidade de Lorentz** (i.e., que ⟨z⟩ ou o clustering do grafo causal de updates cai
na dicotomia binária), **antes** de qualquer simulação. Isso é a "pendência analítica
combinatória" de `SINTESE_SETE_MORTES` aplicada a um substrato emergente — e está atrás
daquela pendência na fila, não à frente.

---

## 5. Fontes (autores, ano, identificador)

- Bombelli, Lee, Meyer, Sorkin (1987), *Space-time as a causal set*, PRL 59, 521.
- Sorkin (2003), *Causal Sets: Discrete Gravity*, gr-qc/0309009.
- Surya (2019), *The causal set approach to quantum gravity*, Living Rev. Relativ.,
  arXiv:1903.11544.
- Bombelli, Henson, Sorkin (2009), *Discreteness without symmetry breaking*,
  arXiv:gr-qc/0605006 (sprinkling + não-localidade).
- Rideout, Sorkin (2000), *Classical sequential growth*, gr-qc/9904062.
- Cortês, Smolin (2014), *Energetic Causal Sets*, PRD 90, 044035, arXiv:1308.2206; e
  *Quantum Energetic Causal Sets*; *Spin foam models as energetic causal sets*,
  arXiv:1407.0032; dimensional superior arXiv:2309.08694.
- Oriti (2011), *The microscopic dynamics of quantum space as a group field theory*;
  Gurau (2016), *Random Tensors* (OUP); revisão arXiv:2404.07834 (*Tensor models and group
  field theories*).
- Pithis, Marchetti, et al. (~2023), *Mean-Field Phase Transitions in Tensorial Group Field
  Theory Quantum Gravity* (geometrogênese mean-field).
- Perez (2013), *The Spin Foam Approach to Quantum Gravity*, Living Rev., arXiv:1205.2019.
- Isham (1992), *Canonical quantum gravity and the problem of time*, gr-qc/9210011.
- Markopoulou, Smolin (1997), *Causal evolution of spin networks*; Markopoulou
  gr-qc/9704013 (orientação como input causal).
- Van Raamsdonk (2010), *Building up spacetime with quantum entanglement*, arXiv:1005.3035.
- Swingle (2009), *Entanglement renormalization and holography*, arXiv:0905.1317 (MERA).
- Maldacena, Susskind (2013), *Cool horizons / ER=EPR*, arXiv:1306.0533.
- Almheiri, Dong, Harlow (2014), *Bulk locality and quantum error correction in AdS/CFT*,
  arXiv:1411.7041.
- Consistência causal bulk-fronteira: arXiv:2504.15910 (*Consistency between Bulk and
  Boundary Causalities in Asymptotically Anti-de Sitter Spacetimes*).
- Wolfram (2020), *A Project to Find the Fundamental Theory of Physics*; Gorard (2020),
  *Some Relativistic and Gravitational Properties of the Wolfram Model*; Gorard, Dehghani
  (2020), *Algorithmic Causal Sets and the Wolfram Model*, arXiv:2011.12174.
- (Contexto info-teórico, NÃO pré-geométrico) Sun, Schölkopf et al. (2021), *Causal
  versions of Maximum Entropy*, arXiv:2102.03906.

> **Nota de método:** afirmações sobre *o que cada programa entrega ou não entrega* foram
> ancoradas em busca à literatura real (revisões + abstracts), não em memória. Onde a
> verificação foi parcial (mean-field de GFT; escopo dos no-gos holográficos), isso está
> marcado em §4. Nenhuma formulação foi inventada para servir à TEIC.
