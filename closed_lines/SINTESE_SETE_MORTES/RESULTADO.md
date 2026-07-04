# Síntese das sete mortes — a estrutura é binária, e o eixo do tempo é a dobradiça

**Data:** 2026-06-30 · **Natureza:** documento **inteiramente analítico** (lê e
sintetiza as sete campanhas + o teorema parcial; nenhum experimento novo). · **Pasta:**
`003-TEORIAS/SINTESE_SETE_MORTES/`.

> **Disciplina declarada antes de começar.** A pergunta NÃO é "que estrutura me dá
> escala". É "que estrutura as sete mortes me *obrigam* a considerar". O candidato que
> emergir abaixo é, de fato, **desconfortável para a TEIC** (ele exige abandonar a
> invariância de Lorentz manifesta — a própria premissa da TEIC). Isso é evidência de
> que a análise não foi torcida para servir ao programa.

---

## 1. As sete mortes, lado a lado — com a coluna que faltava

A coluna nova (4ª) é **qual propriedade do grupo de Lorentz, ou da sua ação sobre o
espaço de configurações, é especificamente responsável pela morte** — não o resultado,
o *mecanismo*.

| # | Família | Quantidade usada | Mecanismo Lorentz-específico da morte |
|---|---|---|---|
| 1 | **Poisson / coordenação** (ESCALA_XI) | ordem causal pura (cobertura) | Os "vizinhos de link" jazem junto ao cone; o conjunto deles a Δτ fixo é o **hiperbolóide de boost**, **não-compacto** ⇒ ⟨z⟩=∞. Verificado: cortar por janela métrica de Δτ **não** localiza (o slab `{0<τ²<ℓ²}` tem volume crescente com a caixa). **Não-compacidade do BOOST.** |
| 2 | **CSG** (Rideout–Sorkin) | regra de crescimento sequencial; **sem embedding** | Nenhum grupo de Lorentz age (não há embedding). Morte = a redução transitiva do poset aleatório é **tipo-árvore** (transitividade ≡0 por teorema, C4 sub-MF). **COMBINATÓRIA (sub-conectada: sem laços).** |
| 3 | **CDT 3D equilíbrio** | colagem livre de simplexos, soma sobre geometrias | Cada colagem quebra Lorentz local; restaurada estatisticamente. O 1-esqueleto tem **coordenação alta** (z~13) ⇒ small-world/Bethe ⇒ MF por teorema. **COMBINATÓRIA (super-conectada).** |
| 4 | **CDT 3D NESS** | idem + condução fora-do-equilíbrio | A condução quebra balanço detalhado mas **não muda a classe de coordenação** (z~13). **COMBINATÓRIA (idêntica a #3).** |
| 5 | **CDT 4D cinemático** | idem, dimensão maior | Em 4D simplexos compartilham **mais** ⇒ coordenação ainda maior, clustering decai (C4~N^−0.33). **COMBINATÓRIA (super-conectada, pior).** |
| 6 | **Percolação longo alcance** | Δτ_ij (tempo-próprio invariante) | A regra `p(Δτ)` é invariante de boost ⇒ **conecta ao longo da órbita de boost**: atalhos (grande separação espacial, pequeno Δτ) sobrevivem ⇒ ⟨z⟩=∞ ∀σ. **Não-compacidade do BOOST (lado da regra).** |
| 7 | **Repulsão Lorentz-inv.** (Matérn/DPP) | s²_ij (invariante de par completo) | A região de exclusão `{\|s²\|<r0²}` é uma **banda ao redor do cone**, volume `~r0²·L` (cresce com o sistema) — a própria não-compacidade do cone ⇒ não reduz ⟨z⟩. **Não-compacidade do BOOST (lado da medida).** |
| — | **Teorema parcial** (analítico) | qualquer q(Δτ) invariante, via Campbell–Mecke | ⟨z⟩ = ρ·**Vol(H^{d−1})**·∫Δτ^{d−1}q dΔτ = ∞ porque **Vol(H^{d−1})=∞**. **Não-compacidade do BOOST (enunciado rigoroso).** |
| — | **(adendo) k-pontos sobre Poisson** | qualquer correlação de ordem finita sobre Poisson | Slivnyak–Mecke: a Palm reduzida do Poisson é Poisson ⇒ a média sobre o resto fatoriza ⇒ `h` recai em função de Δτ ⇒ mesmo BOOST. (Fecha a porta "não-pairwise sobre Poisson"; ver `NAO_PAIRWISE_E_NEQ/.../A2_ANALISE.md`.) |

---

## 2. A generalização

### 2.1 — O denominador comum NÃO é único: a estrutura é binária

Preenchida a coluna 4, as mortes se separam **limpa e genuinamente** em duas categorias
com mecanismos **distintos**:

- **Categoria BOOST** — {1, 6, 7, teorema, adendo k-pontos}. A morte é **diretamente** a
  não-compacidade do subgrupo de boost: qualquer quantidade de conexão/correlação que
  seja função de um **invariante de par** (Δτ, s², ou contagem ∝ Δτ^d) tem como "órbita
  de vizinhos" o hiperbolóide de boost `H^{d−1}`, que tem volume infinito. **Falha a
  barreira 1** (⟨z⟩ diverge). Estas famílias **mantêm** a medida/embedding invariante de
  Lorentz.

- **Categoria COMBINATÓRIA** — {2; 3, 4, 5}. A morte **não** é boost: é a estrutura de
  laços do grafo combinatório que resta quando se **abandona** o embedding invariante
  para escapar da barreira 1. Tem **dois sub-modos opostos**:
  - **sub-conectado** (CSG): sem embedding nenhum, o poset aleatório é tipo-árvore,
    C4→0 (poucos laços).
  - **super-conectado** (CDT 3D/NESS/4D): a colagem livre dá coordenação alta z~13,
    small-world/Bethe, C4 decai (laços, mas em grafo de dimensão-de-grafo ∞).
  Ambos **passam a barreira 1** (z finito) mas **falham a barreira 2** (sem laços de
  dimensão **finita**).

> **Este é o achado central da síntese, e é mais forte do que "duas faces de uma
> tensão" (IMPOSSIBILIDADE_PARCIAL):** há **dois mecanismos de morte distintos**, e um
> substrato candidato precisa escapar **dos dois simultaneamente** — uma barra mais alta
> do que qualquer das sete enfrentou (cada uma morreu por *um* dos dois).

### 2.1-bis — A dobradiça: o eixo do tempo (a foliação) converte um mecanismo no outro

As duas categorias não são paredes independentes entre as quais se poderia escorregar.
**A única operação conhecida que escapa do BOOST é a que entra na COMBINATÓRIA**, e a
operação é sempre a mesma: **regularizar/discretizar o eixo do tempo (introduzir uma
foliação ou um corte de contagem), o que troca a órbita não-compacta de boost por uma
conectividade finita — mas combinatória.** Três evidências independentes, já nos dados:

1. **ESCALA_XI, alavanca A (cap k-NN):** capar a *contagem* de vizinhos é a única
   alavanca que torna z finito — e ela **(i) quebra Lorentz** (contagem não é invariante)
   **e (ii) cai em Bethe** (mean-field combinatório). Boost→combinatória num só passo.
2. **CDT:** a foliação ("C" de Causal) torna a coordenação **finita** (z~13, não ∞) — mas
   alta ⇒ Bethe. A foliação **converteu** ⟨z⟩=∞ (boost) em ⟨z⟩=alto-finito (combinatória).
3. **tipo-CDT 2D vs CDT 3D/4D:** a *fatia espacial* 2D **arma** C4 (≈0.145, laços de
   dimensão finita!); somar o eixo do tempo (links tipo-tempo) **lava** o C4 (3D/4D MF).
   O eixo do tempo é, literalmente, o que destrói a estrutura de laços da fatia.

⇒ Reframe: há **um** obstáculo subjacente — **a conectividade injetada pelo eixo
tipo-tempo** — que se manifesta como **∞ (boost)** se você mantém Lorentz manifesta, e
como **alto-finito (Bethe)** se você folheia para domá-la. CSG é o caso-limite oposto
(remove o eixo tempo *inteiro*, sobra árvore).

### 2.2 — Que classe de objeto escaparia da categoria BOOST?

Pergunta de teoria de grupos, não de física. ⟨z⟩ é finito ⟺ a **órbita dos "vizinhos"**
tem **volume finito** ⟺ o grupo cujo estabilizador define a órbita é **compacto**.

- O grupo de Lorentz `SO(d−1,1)` é **não-compacto** — e a não-compacidade está
  **inteiramente no subgrupo de boost**; o subgrupo de **rotações `SO(d−1)` é compacto**.
- Uma quantidade invariante sob o grupo **inteiro**, definida sobre um **par** de eventos,
  é necessariamente função de `s²` ⇒ órbita = hiperbolóide inteiro (inclui boosts) ⇒ ∞.
  (Tensores não salvam: para extrair um número você contrai ⇒ invariante ⇒ função de s².
  É por isso que a opção "representação tensorial de dimensão finita" do charter **não**
  escapa enquanto a quantidade final for um invariante de par.)
- **A única forma de ter órbita compacta é restringir a quantidade a uma subvariedade
  cujo grupo de isometria seja compacto: uma fatia espacial (superfície de Cauchy), onde
  age apenas `SO(d−1)⋉ℝ^{d−1}` (rotações+translações espaciais, compacto nas direções
  angulares).** Uma "distância induzida **na fatia**" tem como órbita uma **esfera na
  fatia** — compacta ⇒ coordenação finita.

**O preço, inescapável e exato:** uma quantidade definida na fatia **não é invariante de
Lorentz** — ela exige uma **foliação preferida** (uma noção de "agora"). Escapar do BOOST
**força** abandonar a invariância de Lorentz manifesta. Isto não é uma escolha de
engenharia; é o conteúdo da pergunta 2.2.

E note: isso é **exatamente** entrar na categoria COMBINATÓRIA (2.1-bis) — a fatia
espacial é uma estrutura discreta combinatória. A diferença em relação às mortes #3–5 é
**qual** estrutura combinatória: CDT usa a **colagem isotrópica do espaço-tempo** (o eixo
tempo entra em pé de igualdade, super-conecta); o candidato usa a **distância
intra-fatia** com o acoplamento inter-fatia (tipo-tempo) **suprimido/anisotrópico**, para
preservar os laços de dimensão finita da fatia (os mesmos que o tipo-CDT 2D já exibiu).

### 2.3 — Esse candidato já existe na matemática/física?

Sim, e com nome. "Folheação preferida + distância intra-fatia + escala anisotrópica
espaço×tempo para suprimir a conectividade tipo-tempo" é precisamente a estrutura de:

- **Gravidade de Hořava–Lifshitz** — escala anisotrópica `t→b^z t, x→b x` (expoente de
  Lifshitz `z`≠1), foliação preferida, **renormalizável por contagem de potências**
  justamente porque a estrutura espacial domina (a não-compacidade de boost é removida
  pela quebra UV de Lorentz; Lorentz é recuperada no **IR**).
- **Shape dynamics** (Barbour–Gomes–Koslowski) — troca invariância de re-folheação por
  invariância **conforme espacial** na fatia; dual à RG, recupera Lorentz só no nível
  dinâmico global.
- **CDT** — a foliação é a própria definição ("Causal"); e a literatura (Hořava 2009;
  Ambjørn–Görlich–Jurkiewicz–Loll) **já conecta** o fluxo de dimensão espectral 4→2 da
  CDT à gravidade de Hořava.

**Já foi tentado em causal sets / CDT, e com qual resultado?**
- **Causal sets:** deliberadamente **rejeitam** foliação (invariância de Lorentz é o
  axioma fundador) — então esta classe está **fora** do programa de causal sets por
  construção. É por isso que nenhuma das sete (que vivem na lógica de causal-set/Lorentz)
  a tocou de forma limpa.
- **CDT:** **é** a versão foliada e **funciona** geometricamente (d_s: 4→2 é um resultado
  real, não-trivial), mas suas transições são **transições de fase geométricas**
  (1ª/2ª ordem), e — nos nossos próprios testes #3–5 — a coordenação isotrópica do
  espaço-tempo lava os laços (MF). O ingrediente que a CADT padrão **não** isola é a
  **anisotropia de Lifshitz explícita** que suprimiria o acoplamento tipo-tempo,
  preservando os laços da fatia (tipo-CDT 2D, C4≈0.145).
- **Hořava–Lifshitz:** entrega renormalizabilidade, mas tem problemas conhecidos no IR
  (modo escalar extra do gráviton / acoplamento forte) — i.e., a recuperação de Lorentz
  no IR é **frágil**. Não há, na literatura, demonstração de que esta rota entregue a
  **criticalidade de escala emergente** que o programa procura.

---

## 3. Veredito (critério pré-registrado da Seção 3 do charter)

**Resultado primário — GENERALIZAÇÃO ENCONTRADA; o mapa Lorentz-invariante está
FECHADO de forma BINÁRIA.** As perguntas 2.1–2.3 estabelecem:

1. A morte não tem **um** mecanismo, tem **dois** distintos (BOOST não-compacto;
   COMBINATÓRIA de laços), e eles são **ligados pela dobradiça da foliação** (2.1-bis): a
   única operação que escapa de um entra no outro. Um candidato teria de vencer **ambos**.
2. **Dentro da premissa do programa (substrato com invariância de Lorentz manifesta) não
   existe candidato novo** — 2.2 prova que escapar do BOOST exige órbita compacta, o que
   exige fatia espacial, o que exige **foliação**, o que **abandona a premissa**. Logo,
   **para a classe Lorentz-invariante, o mapa está fechado** — não por sete instâncias,
   mas pela demonstração de que toda quantidade de par invariante recai no BOOST e toda
   fuga recai na COMBINATÓRIA.

**Resultado secundário — existe UM candidato estruturalmente distinto, mas ele troca a
premissa, e está apenas parcialmente coberto.** O candidato é o **substrato discreto
foliado com distância intra-fatia e escala anisotrópica (Hořava–Lifshitz) que suprime o
acoplamento tipo-tempo**. Ele é distinto das sete (nenhuma usou distância intra-fatia com
anisotropia controlada) e **não é "Δτ disfarçado"** (a distância é na fatia, não no
espaço-tempo; o grupo relevante é compacto — uma quantidade genuinamente diferente).
**Ressalvas que rebaixam o status de "novo":**
- (a) **abandona a invariância de Lorentz manifesta** (premissa do programa/TEIC) —
  recupera-a só dinamicamente no IR, fragilmente;
- (b) **parcialmente testado**: tipo-CDT 2D (fatia pura) **armou** C4≈0.145; CDT 3D/4D e o
  *stacked* 4D (fatia + tempo isotrópico/cinemático) **morreram** — os dois pontos já
  **colchetam** o candidato. O que falta é exatamente o regime intermediário: anisotropia
  de Lifshitz **ajustável** entre "só fatia" (arma) e "tempo isotrópico" (morre);
- (c) a literatura (Hořava, shape dynamics, CDT) **já percorre** essa rota sem ter
  entregue criticalidade de escala emergente.

Classificação final segundo o charter: **entre "GENERALIZAÇÃO ENCONTRADA, MAS SEM
CANDIDATO NOVO (mapa confirmado fechado)" e "...COM CANDIDATO NOVO".** Honestamente:
**fechado para a premissa do programa; aberto apenas se a premissa for trocada (foliação
anisotrópica), caso em que o candidato existe mas é Hořava–Lifshitz — conhecido,
parcialmente testado, e sem promessa de escala na literatura.** O gatilho cinemático
mínimo está desenhado no Apêndice **mas NÃO executado** (pende de autorização explícita).

### Sobre a Parte B do prompt anterior (NESS genuíno / geometria fora-do-equilíbrio)
Reclassificada, como o charter pediu: pertence à **categoria COMBINATÓRIA** (MF por
liberdade combinatória, não por boost). **Não executada.** Status: a categoria
COMBINATÓRIA está fechada **empiricamente** (CSG + CDT #3–5) mas **não** com a mesma força
**analítica** que o teorema parcial dá ao BOOST. **Pendência registrada e separada:** um
teorema combinatório (do tipo "grafo de cobertura de poset aleatório / triangulação
dinâmica não tem dimensão de laço finita") seria o análogo, no lado combinatório, do
teorema de não-compacidade — mais barato de atacar analiticamente do que rodar mais
motores. A re-execução da Parte B (crescimento perpétuo) só faz sentido **depois** dessa
tentativa analítica, não antes.

---

## Apêndice — gatilho cinemático mínimo do candidato (DESENHADO, NÃO EXECUTADO)

Pende de autorização explícita antes de qualquer código (charter §"O que NÃO fazer").

**Substrato:** pilha de `T` fatias espaciais; cada fatia = processo de ponto em `ℝ^{d−1}`
(Poisson **ou** rede), com grafo intra-fatia por **distância espacial** `|Δx|<r_s`
(órbita = esfera **compacta** ⇒ coordenação intra-fatia finita por construção). Links
inter-fatia (tipo-tempo) só entre fatias adjacentes, com **alcance anisotrópico**
`|Δx|<r_t` e um **parâmetro de Lifshitz** `λ = r_t/r_s` (λ→0: só fatia; λ~1: isotrópico
≈ CDT). Lorentz **não** é imposta (é o ponto); a folheação é explícita.

**Medições (mesma suíte VERBATIM):** ⟨z⟩(N), C4(N) vs `λ`, ladder de N idêntico.

**Predição falsificável (do mecanismo 2.1-bis):** existe `λ*`>0 tal que para `λ<λ*` o
substrato **arma** (⟨z⟩ finito, C4 satura positivo, herdando os laços da fatia ≈0.145) e
para `λ>λ*` ele **morre** (MF, como CDT). **Critério de morte simétrico:** se o C4 só
sobrevive em `λ=0` (fatias **desacopladas**, que não é um espaço-tempo) e colapsa para
**qualquer** `λ>0`, o candidato **não** é um substrato genuíno (é uma pilha de redes
desconexas) ⇒ morte por reclassificação. **Só** uma janela `0<λ<λ*` com C4 positivo **e**
conexão tipo-tempo genuína armaria — e mesmo então o resultado seria **Hořava–Lifshitz
discreto, com Lorentz quebrada**, a ser reportado como tal, não como vitória do programa
Lorentz-invariante.

---

## Resumo de uma linha

As sete mortes não são sete acidentes nem "uma tensão": são **duas** mortes distintas
(BOOST não-compacto; COMBINATÓRIA de laços) **dobradas pelo eixo do tempo** — folhear
para matar o boost ressuscita a combinatória. Dentro da premissa de Lorentz manifesta o
mapa está **fechado**; a única saída estrutural (distância intra-fatia, órbita compacta)
**é** abandonar a premissa, e leva direto à **gravidade de Hořava–Lifshitz** — conhecida,
parcialmente testada (tipo-CDT 2D arma / CDT 3D-4D morre), e sem promessa de escala.
