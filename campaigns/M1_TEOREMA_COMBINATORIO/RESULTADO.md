# M1 — TEOREMA COMBINATÓRIO: resultado da campanha analítica

**Data:** 2026-07-02 · **Pasta:** `FRONTEIRA_COMPACTA/M1_TEOREMA_COMBINATORIO/`
**Pré-registro:** `PRE_REGISTRO.md`. Inteiramente analítico, zero código.
**Etiquetas:** [teorema] = demonstrado aqui; [teorema, literatura] = enunciado
citado; [prova-esboço]; [conjectura]; [medido] = campanha do programa.

---

## 0. Veredito em uma página

**O lado combinatório do binário deixou de ser padrão medido: virou uma
TRICOTOMIA com cada perna teoremática — e a dobradiça das sete mortes é agora
um teorema exato (T1).** Nenhuma morte pré-registrada disparou. A fresta que
resta (ciclos rank-frustrados) fica nomeada e promovida a alvo.

| Peça | Veredito |
|---|---|
| **T1 "laços forçam foliação"** | **[teorema] PROVADO** — espaço de ciclos gerado por 4-ciclos ⇒ função de rank (grading) ⇒ foliação intrínseca equivariante |
| **T2 exclusão exchangeable** | **[teorema] PROVADO** — nenhuma ordem aleatória exchangeable infinita tem diagrama de Hasse não-vazio localmente finito |
| **T3 box orders d≥2** | [prova-esboço] ⟨z⟩_Hasse = Θ((log n)^{d−1}) → ∞ |
| **T4 confinamento por posts** | [teorema, literatura] posts densos em transitive percolation + **[teorema] lema novo: aresta de Hasse não cruza post** ⇒ todo ciclo confinado a bloco finito |
| Tricotomia | FECHA com hipóteses nomeadas + flanco pentagonal DECLARADO |
| Mortes (T1 falhar; contraexemplo homogêneo) | NÃO dispararam |

**Enunciado-síntese (o teorema combinatório, forma tricotômica):** para ordens
aleatórias nas três classes de invariância conhecidas, estrutura de laços de
dimensão finita é impossível sem foliação: (i) invariância como
*exchangeability* ⇒ nem sequer há Hasse localmente finito (T2); (ii) invariância
como *covariância de crescimento* (exemplar: transitive percolation) ⇒ valência
finita mas TODOS os ciclos confinados em blocos finitos (T4); (iii) laços
quadrado-gerados percolantes com valência finita ⇒ a ordem é GRADED = carrega
foliação intrínseca (T1) = a classe CDT/folheada, que é exatamente a que quebra
a invariância de boost. O que escapa às três: ciclos ÍMPARES/rank-frustrados
(pentágonos) — flanco declarado, §6.

---

## 1. Preliminares (fixando objetos)

Poset $(P,\prec)$; diagrama de Hasse $H$ = grafo das relações de cobertura
$x \lessdot y$, visto como grafo não-dirigido com cada aresta rotulada pela
orientação "para cima". Para um passeio fechado $\gamma$ em $H$, a
**circulação** $\varphi(\gamma)$ = (nº de passos para cima) − (nº para baixo);
$\varphi$ é um funcional linear no espaço de ciclos.

**Lema 0 (trivial, conhecido).** [teorema] Diagramas de Hasse não têm
triângulos (um triângulo teria uma corda transitiva removida por definição).
O menor ciclo possível tem comprimento 4.

**Lema 1 (4-ciclos são balanceados).** [teorema] Todo 4-ciclo de $H$ tem
$\varphi = 0$.
*Prova.* Padrões possíveis de orientação num 4-ciclo: $\varphi=\pm4$ seria um
4-ciclo dirigido, impossível numa ordem (aciclicidade). $\varphi=\pm2$ = três
arestas num sentido e uma no outro = caminho dirigido
$x_1\lessdot x_2\lessdot x_3\lessdot x_4$ MAIS a cobertura $x_1\lessdot x_4$;
mas $x_2$ está estritamente entre $x_1$ e $x_4$, contradizendo a cobertura.
Restam os padrões balanceados ($\varphi=0$): o diamante (↑↑↓↓) e a cerca
(↑↓↑↓). $\blacksquare$

## 2. T1 — o teorema da dobradiça: laços quadrado-gerados forçam foliação

**Teorema T1.** [teorema] Seja $G$ um subgrafo conexo de $H$ cujo espaço de
ciclos **sobre $\mathbb{Z}$** (o $H_1(G;\mathbb{Z})$ do grafo como 1-complexo)
é gerado por 4-ciclos. Então existe $r: V(G)\to\mathbb{Z}$ com
$r(y)=r(x)+1$ para toda aresta de cobertura $x\lessdot y$ em $G$ (uma função
de rank/grading em $G$), única a menos de constante.

*Prova.* Pelo Lema 1, $\varphi$ anula os geradores, logo (por linearidade
sobre $\mathbb{Z}$) anula todo o espaço de ciclos de $G$. Então a "integral"
$r(x) := \varphi(\text{caminho } x_0\to x)$ não depende do caminho (a diferença
entre dois caminhos é um ciclo inteiro), está bem definida em $G$ conexo, e
sobe exatamente 1 em cada aresta para cima. $\blacksquare$

*Precisão de hipótese (por que $\mathbb{Z}$ e não GF(2)):* sobre GF(2) o
argumento falharia ($\varphi$ mod 2 só vê paridade de comprimento). Mas
$\mathbb{Z}$ é a noção FISICAMENTE correta e a que Wen usa: laços de Wilson
decompõem-se multiplicativamente em plaquetas ORIENTADAS — a condição "todo
laço é produto de plaquetas" é geração inteira, não mod-2. A hipótese de T1 é
exatamente o requisito 2 de string-nets, sem folga.

**Corolário T1a (foliação intrínseca).** Os níveis $\{r = k\}$ são antichains
do suborder alcançável por caminhos de Hasse DENTRO de $G$ (se $x\prec y$ via
cadeia de coberturas em $G$, todo passo sobe ⇒ $r(y)>r(x)$; comparabilidade
por cadeias fora de $G$ não é governada — escopo declarado), e
$r$ é construída SÓ da ordem ⇒ todo automorfismo de $(P,\prec)$ que preserva
$G$ preserva $r$ a menos de constante. **Um cluster macroscópico
quadrado-gerado carrega uma foliação discreta intrínseca e equivariante — um
tempo preferido legível da própria ordem.**

**Corolário T1b (a dobradiça, agora exata).** A síntese das sete mortes tinha
como dobradiça empírica "folhear o tempo arma C4" (a família CDT). T1 dá a
recíproca como teorema: **armar C4 (no sentido forte de Wen: plaquetas
quadradas gerando o espaço de ciclos) OBRIGA a foliação.** Não há substrato
com plaquetas quadradas percolantes que não seja graded. A rota
quadrado-plaqueta para um fóton emergente está portanto fechada para QUALQUER
ensemble sem foliação intrínseca — não por medida, por teorema.

**Consistência com a camada 1 [medido].** Ordens de sprinkling são
violentamente rank-frustradas: coexistem cadeias de comprimentos díspares
entre os mesmos extremos (ex.: $u\lessdot a\lessdot v$ e
$u\lessdot b\lessdot c\lessdot v$ = pentágono de Hasse, $\varphi=\pm1$),
genericamente e em toda escala. Logo, por T1-contrapositiva, clusters
quadrado-gerados de sprinklings não crescem — exatamente o que E6b mediu
(torres de diamante com cauda plana ~0.25%, não-crescente) [medido].
Retrodição nº 1.

## 3. T2 — exclusão exchangeable: sem Hasse localmente finito

**Teorema T2.** [teorema] Seja uma ordem aleatória exchangeable em ℕ (lei
invariante por permutações finitas de rótulos). Então a relação de cobertura é
um array exchangeable e, por componente ergódica, tem densidade constante
$p = \Pr(1\lessdot 2 \text{ ou } 2\lessdot 1)$:
(i) se $p>0$, todo elemento tem grau de Hasse esperado infinito
($\sum_j p = \infty$);
(ii) se $p=0$, a relação de cobertura é a.s. VAZIA (união enumerável de
eventos nulos).
**Logo nenhuma ordem exchangeable infinita tem diagrama de Hasse não-vazio e
localmente finito.**

*Prova.* A cobertura é função isomorfismo-invariante da ordem ⇒ o array
$C_{ij}=\mathbf{1}[i\lessdot j]$ é conjuntamente exchangeable (Aldous–Hoover;
para posets, Janson). Ergodicidade dá $p$ constante; (i) linearidade da
esperança; (ii) cada par é a.s. não-cobertura e há enumeráveis pares.
$\blacksquare$

**Exemplos de sanidade.** Ordem linear uniforme infinita (via $U_i$ iid):
densa em comparabilidade, mas a.s. SEM coberturas (sempre há $k$ entre dois) —
perna (ii) ✓. Sprinkling em caixa fixa com $n\to\infty$: coberturas existem em
todo $n$ finito mas $p_n\to0$ e a valência DIVERGE com $n$ (T3) — a
discretude localmente finita vive apenas em regimes de escala finita, nunca no
limite exchangeable ✓.

**Leitura.** T2 é a sombra abstrata da camada 1: invariância de rótulo pura já
proíbe a estrutura local de que string-nets precisam, antes de qualquer
geometria. A discretude local com laços precisa SAIR da exchangeability — e as
saídas conhecidas são exatamente as outras duas pernas (crescimento covariante;
gradedness).

## 4. T3 — box orders: valência log-divergente (a camada 1 sem Lorentz)

**Proposição T3.** [prova-esboço] Ordem de dominância sobre $n$ pontos iid em
$[0,1]^d$ ($x\prec y$ sse $x_i<y_i\ \forall i$; para $d=2$ é a ordem causal de
$\mathbb{M}^2$ a 45°): o nº esperado de coberturas é
$\sim \tfrac{2}{(d-1)!}\, n(\log n)^{d-1}$, logo
$\langle z\rangle_\text{Hasse} = \Theta((\log n)^{d-1}) \to\infty$.

*Esboço ($d=2$).* $\mathbb{E}[\#\text{cov}] = n(n-1)\int_{x\prec y}
(1-A)^{n-2}$, com $A$ = área da caixa entre $x,y$; com gaps $u,v$:
$\approx n^2\int_0^1\!\!\int_0^1 (1-uv)^n\,du\,dv = n^2\cdot\Theta(\log n / n)
= \Theta(n\log n)$ (o $\int(1-w)^n\log(1/w)\,dw$ dá o log). Geral $d$: o
produto de $d$ gaps dá $(\log n)^{d-1}$. $\blacksquare$
[Âncoras: box-spaces de Brightwell; e o fato conhecido da CST de que a
valência de links em $d=2$ diverge logaritmicamente com a densidade.]

**Leitura.** Mesmo SEM grupo de Lorentz, a rota exchangeable para uma ordem
"genuinamente $d\geq2$-dimensional" (dominância) reencontra a divergência de
valência — versão branda ($\log$) da camada 1. A não-compacidade do boost
torna a divergência dura (potência); a estrutura de ordem em $d\geq2$ já a
torna inevitável em forma fraca.

## 5. T4 — crescimento covariante: ciclos confinados por posts

Exemplar: transitive percolation (TP), o modelo mais simples da família
Rideout–Sorkin (cada elemento novo liga-se independentemente com prob. $p$ a
cada anterior; fecho transitivo).

**Fato [teorema, literatura].** Em TP com $p$ fixo, *posts* (elementos
comparáveis a TODOS os outros) ocorrem com densidade positiva; a ordem infinita
decompõe-se a.s. numa concatenação (soma ordinal) de blocos finitos i.i.d.
entre posts consecutivos, com caudas exponenciais de tamanho
[Alon–Bollobás–Brightwell–Janson 1994; Bollobás–Brightwell, *The structure of
random graph orders*].

**Lema 2 (novo, elementar).** [teorema] Nenhuma aresta de Hasse cruza um post:
se $w$ é post e $x\prec w\prec y$ estritamente, então $x\lessdot y$ é
impossível ($w$ está entre). Logo o diagrama de Hasse de TP é uma CADEIA de
blocos finitos unidos nos posts (vértices de corte). $\blacksquare$

**Corolário T4 (confinamento de laços).** [teorema, dadas as âncoras] Todo
ciclo do Hasse de TP está contido num único bloco, de tamanho $O_P(1)$; o nº
de ciclos independentes num raio $R$ cresce $\lesssim R$ (arranjo 1D de
blocos) — dimensão de ciclos 1, nunca 2. **Não existe escala além de
$\xi(p)$ (o tamanho típico de bloco) em que laços possam condensar.** A
topologia de larga escala é a de um caminho.

**Retrodição nº 2 [medido].** O CSG medido no programa deu exatamente isto:
$\langle z\rangle$ satura (Gatilho 1 armado) mas C4 fica sub-mean-field com um
platô intermediário (C4 ≈ 0.019 a N=16000) — **o platô são os ciclos
intra-bloco**, que existem mas nunca percolam. O padrão medido vira corolário.

**Escopo.** Para CSG geral (acoplamentos $t_n$ genéricos) a densidade positiva
de posts é [conjectura] plausível mas não-provada aqui — hipótese nomeada; TP
é o exemplar provado.

## 6. A tricotomia, o flanco declarado, e o que NÃO foi provado

**Tricotomia (síntese).** Ordem aleatória com estrutura de laços de dimensão
finita exigiria simultaneamente: valência localmente finita (contra T2/T3 nas
classes exchangeable/embutidas), ciclos não-confinados (contra T4 na classe de
crescimento com posts), e — se as plaquetas forem quadradas — nenhuma
foliação (contra T1, que a força). As três pernas cobrem as três noções de
invariância em uso; **a interseção exigida por Wen é vazia em todas**.

**O flanco pentagonal (a fresta única, declarada e promovida a alvo).**
T1 só governa geradores BALANCEADOS (4-ciclos; qualquer mistura de ciclos com
$\varphi=0$). Um espaço de ciclos 2-dimensional percolante gerado por ciclos
RANK-FRUSTRADOS (pentágonos N5, $\varphi=\pm1$), homogêneo e de valência
finita, escaparia de T1 — e não sabemos construí-lo nem proibi-lo.
Observações que estreitam a fresta: (a) toda a família folheada/CDT usa
quadrados — um substrato pentagonal seria física nova por si; (b) frustração
de rank em toda escala é exatamente o perfil dos sprinklings, onde a valência
diverge — sugerindo (não provando) que frustração percolante e valência finita
competem. **Alvo nomeado M1b:** provar "pentágono-percolante + homogêneo ⇒
valência infinita" OU construir o contraexemplo (= morte 2, descoberta maior).

**Mortes pré-registradas:** nenhuma disparou (T1 fechou sem obstrução de
Möbius — a obstrução É a circulação, e quadrados a anulam; nenhum
contraexemplo homogêneo construído).

## 7. O que muda no programa

1. **Camada 2 do Teorema da Fronteira sobe de [medido] para
   [teorema-nas-classes-nomeadas + fresta declarada]** — editar o paper Wen
   (N3) na próxima revisão: o parágrafo de layer 2 pode citar T1/T2/T4 e
   rebaixar "measured binary" para "theorem in the three named invariance
   classes, with the rank-frustrated flank open". O Apêndice B.6 de N0
   (teorema combinatório pendente) é RESOLVIDO neste nível.
2. **Duas retrodições novas** (platô C4 do CSG = ciclos intra-bloco; torres de
   diamante planas de E6b = frustração de sprinkling) — mais dois corolários
   para o paper-núcleo (M4).
3. **M1b entra na fila da Linha 1** (fresta pentagonal) atrás de M2/N5.
4. A tricotomia dá ao paper-núcleo sua seção combinatória pronta: T1 é
   provavelmente o teorema mais citável do programa depois do binário
   (enunciado de 3 linhas, prova de 10, consequência física direta).

## Literatura citada

Aldous–Hoover (arrays exchangeable); Janson, *Poset limits and exchangeable
random posets*; Alon–Bollobás–Brightwell–Janson, Ann. Appl. Probab. 4 (1994)
(posts em random graph orders); Bollobás–Brightwell, *The structure of random
graph orders* (decomposição em blocos); Brightwell, *Box-spaces and random
partial orders* + *Colouring random Hasse diagrams* arXiv:2501.12373
(box orders); Rideout–Sorkin PRD 61 024002 (CSG); Kleitman–Rothschild
(estrutura 3-camadas do poset uniforme — o extremo "denso" da perna T2).
[Volumes/páginas a conferir na redação final do paper-núcleo.]
