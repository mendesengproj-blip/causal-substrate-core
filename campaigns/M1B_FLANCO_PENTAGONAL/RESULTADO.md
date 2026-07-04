# M1b — FLANCO PENTAGONAL: RESULTADO

**Data:** 2026-07-04 · **Pré-registro:** `PRE_REGISTRO.md` (mesmo dia, com
declaração de não-cegueira §2) · **Gate:** `gate_m1b.py` → `gate_m1b.json`,
**VERDE** nos 3 exemplares · **Natureza:** analítica + certificados finitos.

---

## 0. Veredito em uma página

**O FLANCO PENTAGONAL É CONSTRUTÍVEL.** A "morte 2 / descoberta maior"
antecipada em M1 §6 disparou: existem ordens parciais **homogêneas
(vértice-transitivas), localmente finitas (axioma de causal set), de valência
de Hasse finita, NÃO-graduadas**, cujo espaço de ciclos é gerado por ciclos
locais **rank-frustrados** (pentágonos, $\varphi=\pm1$) e **percola**
($\#$ciclos independentes $\sim R^2$ ou mais). Três exemplares elementares,
com provas completas e gate de certificados finitos VERDE.

| Peça | Veredito |
|---|---|
| Conjectura-forte M1 §6(b) "frustração percolante + homogêneo ⇒ valência ∞" | **MORTA** (contraexemplo explícito, 3×) |
| T1–T4 (tricotomia) | **INTACTOS** — a classe cristalina nunca esteve nas 3 pernas; agora sabemos que ela é HABITADA |
| Teorema físico (no-photon em substrato Lorentz-invariante) | **INTACTO e mais apertado** — a rota de ataque via flanco exige tornar o cristal invariante, exatamente o que camada 1 + BHS proíbem |
| Lição estrutural | a competição real nunca foi "frustração vs. valência finita"; é **frustração vs. INVARIÂNCIA ESTATÍSTICA** |

A construção é elementar (o valor está no fechamento do alvo nomeado e na
delimitação, não em profundidade matemática). O alvo foi nomeado em 02jul26 e
fechado em 04jul26.

---

## 1. Os três exemplares e o enunciado

**Teorema (existência; K1–K7 do pré-registro).** Existem ordens parciais
$(P,\prec)$ com TODAS as propriedades: (i) vértice-transitivas; (ii)
localmente finitas (intervalos finitos = causal set); (iii) diagrama de Hasse
de valência finita; (iv) não-graduadas (nenhuma $r$ com $r(y)=r(x){+}1$ em
coberturas — a conclusão de T1 falha genuinamente); (v) espaço de ciclos do
Hasse gerado por translados de ciclos locais com $\varphi$-imagem
$=\mathbb{Z}$ (frustrados); (vi) percolante ($\mathrm{rank}$ de ciclos em bola
de raio $R$ cresce $\gtrsim R^2$).

| | E1 (cristal abeliano) | E2 ($\Gamma_3$) | E3 ($\Gamma_5$) |
|---|---|---|---|
| Grupo | $\mathbb{Z}^2$ | $\langle a,b,c \mid aba{=}bc\rangle$ | $\langle a,b,c,d,e \mid abc{=}ed\rangle$ |
| Geradores (up) | $(3,0),(0,3),(1,1),(3,1),(1,3)$ | $a,b,c$ | $a,b,c,d,e$ |
| Peso $h$ | $x{+}y$: $3,3,2,4,4$ | $1,1,2$ | $2,2,2,3,3$ |
| Valência | 10 | 6 | 10 |
| Crescimento | polinomial ($R^2$) | exponencial | exponencial |
| Girth | 4 (quadrados existem) | 5 | 5 |
| Geradores do esp. de ciclos | quadrados ($\varphi{=}0$) + 3 ciclos frustrados | **pentágonos SÓ** | **pentágonos SÓ** |
| Arestas por pentágono | — | $a,b$-arestas em 2 | cada aresta em 1 ("cacto") |
| Pentágono | $v_1{+}v_2{+}v_3=v_4{+}v_5$ | $1,a,ab,aba,b$ | $1,a,ab,abc,e$ |

E1 fecha a leitura "não-graduado + Wen-requisitos + crescimento de dimensão de
variedade"; E2/E3 fecham a leitura literal do flanco ("espaço de ciclos gerado
por pentágonos frustrados"); E2 adicionalmente tem plaquetas compartilhando
arestas (responde a objeção de que E3 é um cacto de pentágonos colados por
vértices).

## 2. Provas

Em todos: ordem $u \preceq v \iff u^{-1}v$ (resp. $v-u$) pertence ao
semigrupo positivo gerado pelos geradores "up".

**K1 (ordem parcial).** $h$ é um homomorfismo ao $\mathbb{Z}$ (o relator é
$h$-balanceado: E1 $3{+}3{+}2=4{+}4$; E2 $1{+}1{+}1=1{+}2$; E3 $2{+}2{+}2=3{+}3$)
com $h>0$ em todo gerador. Elemento positivo não-trivial tem $h\ge$ peso
mínimo $>0$ ⇒ aciclicidade e antissimetria. $\blacksquare$

**K2 (local finitude).** Elementos de $[u,v]$ correspondem a positivos $p$ com
$h(p)\le h(u^{-1}v)$; palavra positiva de peso $\le W$ tem comprimento
$\le W/\min h$ ⇒ finitos. É um causal set. $\blacksquare$

**K3 (Hasse = grafo de Cayley).** $u \lessdot v \iff u^{-1}v$ é positivo
IRREDUTÍVEL no semigrupo. (a) Todo gerador é irredutível: produto de 2
positivos tem $h \ge 2\min h$; em E1 e E3, $2\min h = 4 > \max h(\text{gen})=3$
— aritmética pura. Em E2, $c$ tem $h=2=1{+}1$: os positivos de peso 1 são
exatamente $\{a,b\}$ (palavra positiva de peso 1 tem comprimento 1), logo o
único risco é $c\in\{a^2,ab,ba,b^2\}$ — **certificado no gate** (palavras
$c^{-1}a^2$ etc. separadas em quociente finito ⇒ desigualdade provada em
$\Gamma_3$). Em E1, exaustivo no gate: minimais do cone $=$ exatamente os 5
geradores. (b) Nenhum irredutível além dos geradores: todo positivo é imagem
de palavra positiva; comprimento $\ge2$ ⇒ fatora em positivos não-triviais ⇒
redutível. $\blacksquare$

**K4 (valência e transitividade).** Multiplicação à esquerda (translação) é
automorfismo de ordem ⇒ vértice-transitiva. Valência $= 2\times\#$geradores,
com geradores 2-a-2 distintos [E1: coordenadas; E2/E3: certificado em
quociente]. $\blacksquare$

**K5 (pentágono embutido, frustrado).** Os 5 vértices têm pesos 2-a-2
distintos OU distinção certificada em quociente (gate: 10/10 pares nos dois
grupos); as 5 arestas são coberturas (K3); padrão ↑↑↑↓↓ ⇒ $\varphi=+1$.
$\blacksquare$

**K6 (não-graduação).** Graduação unitária exigiria funcional com valor 1 em
todo gerador; o relator dá $3=2$, contradição. (E1 exato:
$\lambda=(\tfrac13,\tfrac13)$ dos dois primeiros geradores força
$\lambda\cdot(1,1)=\tfrac23\neq1$.) A conclusão de T1 falha genuinamente — e
DEVE falhar: os geradores do espaço de ciclos não são balanceados, então T1
simplesmente não governa. $\blacksquare$

**K7 (espaço de ciclos e percolação).** Teorema do complexo de apresentação:
para $\langle S\mid R\rangle$ com $R$ gerando normalmente o núcleo, o espaço de
ciclos do grafo de Cayley é gerado (como $\mathbb{Z}$-módulo) pelos translados
dos ciclos dos relatores (o recobrimento universal do complexo é simplesmente
conexo). E2/E3: um relator (pentágono, $\varphi=1$), girth 5 **certificada por
máquina** (nenhuma palavra ciclicamente reduzida $\le4$ é trivial: 792 e 7400
certificados) ⇒ ciclo mínimo é o pentágono e o espaço é pentagon-gerado.
E1: núcleo $K=\ker(\mathbb{Z}^5\!\to\!\mathbb{Z}^2)$ tem posto 3; com
$r_1=(1,1,1,-1,-1)$ (pentágono, $\varphi{=}1$), $r_2=(1,1,-3,0,0)$ (5-ciclo,
$\varphi{=}{-}1$), $r_3=(-3,-1,0,3,0)$ (7-ciclo, $\varphi{=}{-}1$): na base
$k_1=(2,0,-9,0,3)$, $k_2=r_2$, $k_3=(0,0,-4,1,1)$ de $K$ tem-se $r_1=k_2-k_3$,
$r_3=-k_1-k_2+3k_3$, determinante $-1$ ⇒ $\{r_1,r_2,r_3\}$ é
$\mathbb{Z}$-BASE de $K$ ⇒ espaço de ciclos $=$ quadrados de comutação
($\varphi{=}0$) $+$ translados de $r_1,r_2,r_3$; $\varphi$-imagem
$=\mathbb{Z}$. Percolação: translados em todo vértice; E1 medido no gate:
rank de ciclos em bolas $R{=}4..12$ com expoente $2.24\in[1.7,2.3]$.
$\blacksquare$

## 3. Gate (VERDE)

`gate_m1b.json` (seed 20260704, $S_8$): **E1** exaustivo em bola $h\le24$ —
minimais $=$ os 5 geradores, pentágono de coberturas, sem graduação (exato),
expoente 2.237; **E2** 792 palavras + 10 pares certificados em 3 quocientes;
**E3** 7400 palavras + 10 pares em 2 quocientes. Nenhum item AMARELO: as
únicas citações analíticas restantes são o teorema do complexo de apresentação
[literatura, padrão] e aritmética de pesos [exata]. Freiheitssatz tornou-se
DESNECESSÁRIO (os certificados de quociente cobrem tudo que ele cobria aqui).

## 4. O que morre e o que fica

**MORRE — a conjectura-forte do flanco.** M1 §6(b) sugeria que "frustração de
rank em toda escala é o perfil dos sprinklings, onde a valência diverge —
sugerindo que frustração percolante e valência finita competem". FALSO no
nível combinatório: competem apenas quando se exige **invariância
estatística**. Homogeneidade determinística (cristal) hospeda frustração
percolante com valência 6–10 sem esforço.

**FICA — T1–T4, sem emenda.** Nenhum dos quatro é tocado: T1 governa geradores
balanceados (aqui não-balanceados de propósito); T2 governa exchangeability
(cristal não é); T3 ordens embutidas iid (não é); T4 growth models (não é).
A tricotomia era exata sobre o que afirmava; o que muda é o STATUS da 4ª
classe: de "não sabemos construí-la" para "habitada, com exemplares de 3
linhas".

**FICA — o teorema físico, mais apertado.** O no-photon do programa é sobre
substratos **Lorentz-invariantes**: camada 1 (Campbell–Mecke sobre ensembles
invariantes embutidos) mata valência finita; BHS mata cristais (nenhuma
estrutura discreta determinística é boost-invariante). O flanco construído
vive EXATAMENTE no complemento: determinístico, rígido, não-invariante. A
junta de ataque do core paper ("an emergent photon must break T1–T4 through
the pentagonal flank") fica MAIS estreita: o atacante agora tem o cristal de
graça, mas precisa torná-lo invariante — e isso é a porta que camada 1/BHS
fecham. Resta, como sempre, a fronteira declarada das medidas
não-Poisson/dinâmicas (IMPOSSIBILIDADE_PARCIAL).

## 5. Leituras estruturais (com sobriedade)

1. **Lorentz pode ser quebrada sem foliação.** A família foliada/CDT
   (GATILHO_ARMA) passava as duas barreiras (valência finita + laços
   percolantes) ao preço de um tempo preferido graduado. O cristal pentagonal
   é o **segundo** substrato a passar as duas — ao preço de rigidez
   cristalina, SEM graduação unitária. (Sobriedade: ele ainda carrega funções
   de altura equivariantes de passos desiguais — um cone de $h$'s, nenhum
   canônico — e toda a anisotropia de um cristal; "sem foliação" = a conclusão
   específica de T1 falha, não "isótropo".)
2. **A obstrução a string-nets é a invariância, não a ordem causal.** E1 é
   realizável como cristal causal em $\mathbb{M}^2$ (5 vetores dentro de um
   cone convexo apontado); um string-net kinematicamente tem tudo que pede
   (valência finita, plaquetas locais gerando ciclos percolantes) sobre uma
   ordem causal legítima. O que não existe é versão INVARIANTE disso. Refina a
   tese do paper Wen com um witness construtivo do outro lado da fronteira.
3. **E3 não é manifoldlike:** intervalos crescem exponencialmente
   ($\sim 5^{h/2}$ elementos abaixo de peso $h$) vs. polinomial em qualquer
   $\mathbb{M}^d$ — o exemplar de pentágonos puros mais simples é
   intrinsecamente hiperbólico. E1 é manifold-compatível ($\mathbb{Z}^2$) mas
   mistura quadrados. **Pergunta nova nomeada (aberta, baixa prioridade):
   existe cristal de pentágonos PUROS com crescimento polinomial?**

## 6. Deltas para os papers (NA REVISÃO — nenhum PDF submetido é tocado agora)

- **core_paper Sec. IV ("The declared flank"):** "We can neither construct nor
  forbid it" → construído; enunciar o teorema de existência (1 parágrafo + o
  exemplar E1 ou E3) e a delimitação: o flanco vive na classe cristalina,
  fora de toda classe de invariância e fora de Lorentz (BHS); a observação
  (b) ("frustration and finite valence compete") deve ser REMOVIDA ou
  reescrita como "compete with statistical invariance".
- **core_paper Table open frontiers, item 1:** de "named target" para
  "resolved: constructible, strictly crystalline; invariant version excluded
  by layer 1/BHS; non-Poisson-measure frontier unchanged".
- **core_paper Sec. "How to break this theory":** a rota do flanco se reduz à
  rota das medidas não-Poisson — fusão de duas juntas em uma.
- **Wen paper (CQG), na revisão:** parágrafo-witness: requisitos de Wen são
  satisfazíveis sobre ordem causal cristalina; a fronteira é invariância — 
  fortalece a tese central (era "signature/invariance boundary").

## 7. Custo e disciplina

Analítico + gate de ~1 s de execução. Pré-registro com declaração de
não-cegueira (§2) ANTES do código; kill-list integralmente executada; nenhuma
janela movida pós-dado (expoente 2.237 dentro da janela declarada [1.7,2.3]).

## 8. O que M1b NÃO reivindica

Nada sobre dinâmica (se string-net CONDENSA no cristal é outra campanha, hoje
sem gatilho); nada sobre substratos invariantes (fronteira não-Poisson
inalterada); nenhuma novidade matemática profunda reivindicada (objetos
elementares; não fizemos busca de literatura por eles — se um referee apontar
precedente, o valor para o programa não muda: o alvo nomeado fecha igual);
a pergunta "pentágonos puros + crescimento polinomial" fica aberta e nomeada.
