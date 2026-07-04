# M1c — FRONTEIRA NÃO-POISSON: pré-registro (congelado ANTES de qualquer código)

**Data:** 2026-07-04 · **Pasta:** `FRONTEIRA_COMPACTA/M1C_FRONTEIRA_NAO_POISSON/`
**Antecedentes:** M1 (tricotomia; T4 confinamento por posts) · core_paper
Sec. "How to break" rota (ii) e Table item 1 · [[rs-trigger-csg-coordination]]
(flanco aberto nº 1: regras sobre medidas não-Poisson/dinâmicas) ·
[[m1b-flanco-pentagonal]] (o outro flanco, já fechado por construção).
**Natureza:** analítica (o entregável é um teorema) com gate computacional de
sweep + medição.

---

## 1. A pergunta (a fronteira não-Poisson, tornada precisa)

O resultado central do programa — **sem fóton, sem escala, sem laços
percolantes de dimensão finita** — é teorema no caso Poisson (camada 1) e no
caso folheado (T1). Na **família de crescimento sequencial covariante de
Rideout–Sorkin (CSG)** — a única medida invariante NÃO-Poisson genuína — ele
está apenas **parcialmente** fechado:

- **T4 (provado)** governa só a **percolação transitiva** (acoplamento
  $t_n=t^n$): posts têm densidade positiva ⇒ (Lema T4: nenhuma aresta de Hasse
  cruza um post) ⇒ soma ordinal de blocos finitos ⇒ **todo ciclo confinado a um
  bloco** ⇒ dimensão do espaço de ciclos = 1.
- **Para {t_n} GERAL** a densidade positiva de posts é **[conjectura]** (escopo
  declarado em M1 §5); e "sem laços percolantes na CSG completa" é **[medido]**
  (o platô sub-mean-field C4≈0.019), não provado.

> **A pergunta M1c:** o mecanismo do T4 (posts ⇒ confinamento ⇒ laços 1D)
> sobrevive a TODA a família CSG Bell-causal e geralmente-covariante, ou existe
> uma escolha de acoplamentos {t_n} que mantém **valência finita** mas
> **suprime os posts** o suficiente para os laços **percolarem em 2D**?

Uma CSG com valência finita + posts de densidade nula + espaço de ciclos 2D
percolante seria um substrato invariante-não-Poisson capaz de hospedar um
string-net: a **"morte 2 / descoberta maior"** da fronteira não-Poisson, e a
realização (não apenas declaração) da rota (ii) do "How to break" do core_paper.

**Redução central (torna a pergunta decidível):** pelo Lema T4 (geral, não só
TP), *laços percolantes 2D* ⟹ *ausência de posts de densidade positiva*. Logo a
fronteira inteira pivota sobre a **densidade de posts em CSG como função de
{t_n}** — objeto estudado (mas incompleto) na literatura.

## 2. DECLARAÇÃO DE NÃO-CEGUEIRA

O scoping analítico (antes deste documento, sem código) já produziu um **prior
forte de FECHAMENTO** (a impossibilidade estende-se à CSG) e três mecanismos
candidatos de prova, cada um também indicando ONDE um contraexemplo teria de
viver. Este pré-registro não é cego quanto à direção; ele congela o
**protocolo**: a kill-list, o gate e as janelas de decisão, antes do código.

**Mecanismos candidatos de FECHAMENTO (prior):**
- **(a) Tensão valência-finita ↔ posts.** Manter ⟨z⟩ finito exige anexar cada
  novo elemento a O(1) ancestrais em média; anexação esparsa em ordem crescente
  tende a produzir posts densos (Barak–Erdős / random graph orders têm posts de
  densidade positiva para todo p>0 — Bollobás–Brightwell). Suprimir posts
  parece exigir anexar a um NÚMERO crescente de ancestrais ⇒ ⟨z⟩ diverge.
- **(b) Argumento covariante "sem-grade".** Espaço de ciclos 2D percolante é,
  por T1, essencialmente uma grade graduada; a covariância da CSG faz cada
  nascimento ver só o passado como poset NÃO-rotulado ⇒ não pode alinhar-se a
  uma grade 2D global sem uma graduação (foliação, T1) que a medida covariante
  não fornece. O 2D-plano-percolante é o fio-da-navalha folheado, medida-zero
  na família covariante.
- **(c) Conexão com T3.** Laços 2D percolantes exigem estrutura de
  dominância/box-order, que (T3) tem valência log-divergente.

**Onde um contraexemplo teria de viver (o canto a varrer):** acoplamentos que
suprimem posts a valência finita e SEM graduação — o canto que campanhas
anteriores (geradores "genéricos") NÃO sondaram. Suspeito que é vazio (um lado
dá árvore/posts, o outro dá valência divergente), mas não sei provar — daí o
gate varre exatamente esse canto.

## 3. O que já está estabelecido (para não reivindicar redundância)

Trabalho CSG anterior do programa ([[rs-trigger-csg-coordination]]) mediu, em
acoplamentos **genéricos**: (i) ⟨z⟩ SATURA (escapa do boost) e (ii) C4
sub-mean-field / árvore-like. M1c NÃO re-mede isso. O conteúdo NOVO é:
1. **Analítico:** a conjectura de densidade de posts para a família {t_n}
   COMPLETA (a lacuna do T4), OU sua caracterização exata.
2. **Sonda do canto post-suprimido**, que os acoplamentos genéricos não
   atingiram — onde a valência-finita e a percolação 2D teriam de coexistir.

## 4. Objetos (fixando a definição)

CSG de Rideout–Sorkin: causet crescido elemento a elemento; a probabilidade de
o novo elemento nascer com um dado passado (order-ideal do causet atual) é
fixada por Bell-causalidade + covariância geral discreta via uma sequência de
constantes de acoplamento não-negativas $\{t_n\}_{n\ge0}$ (Rideout–Sorkin 2000).
$t_n=t^n$ = percolação transitiva. **Post** = elemento comparável a todos os
outros. **Espaço de ciclos** do diagrama de Hasse; **dimensão** $d$ = expoente
de rank($H_1$ em bola de raio-grafo $R$) $\sim R^d$ (1 = confinado/1D;
2 = percolante). Anti-circularidade: só $\{t_n\}$ (adimensional) e a ordem de
nascimento entram no gerador — nenhuma métrica, coordenada ou expressão
relativística.

## 5. Kill-list (o que um contraexemplo/prova deve satisfazer)

| # | Exigência | Instrumento |
|---|---|---|
| K1 | Gerador é CSG Bell-causal + covariante (não um reticulado disfarçado) | forma $\propto t_{|S|}$ das transições; teste de covariância (invariância por relabeling do passado) |
| K2 | Valência de Hasse FINITA (⟨z⟩ limitada, estável em N) | fit de ⟨z⟩(N); slope em log N ≈ 0 |
| K3 | Densidade de posts → 0 (posts suprimidos) | ρ_post(N) = posts/N decrescente < 0.005 |
| K4 | Blocos entre posts CRESCEM sem limite | max-block/N não → 0; ou nº de posts sublinear |
| K5 | Espaço de ciclos PERCOLA em 2D | expoente $d$ ∈ [1.7, 2.3] em janela R declarada |
| K6 | Laços de fato existem e interligam (não só rank) | C4 acima do platô MF; transitividade não → 0 |
| K7 | (escopo) não-graduado: nenhuma foliação intrínseca ⇒ não recai em T1 | ausência de função de rank consistente (checar circulação φ dos ciclos) |

**Prova de FECHAMENTO** (a alternativa, o entregável preferido) deve
estabelecer UMA de: (A) CSG Bell-causal com ⟨z⟩ finita ⇒ posts de densidade
positiva (estende Bollobás–Brightwell além de TP) ⇒ fecha por T4; (B)
covariância + valência finita ⇒ dimensão de ciclos ≤ 1 (análogo covariante de
T1/T3); (C) impossibilidade direta do canto K2∧K3∧K5.

## 6. Gate computacional G (declarado ANTES de rodar)

`gate_m1c.py` (estende `TEIC/docs/campaigns/RIDEOUT_SORKIN_TRIGGER/rs_trigger.py`:
fecho transitivo com bitsets uint64 de ancestrais; generalizar o gerador de
$t_n=t^n$ para $\{t_n\}$ arbitrário). Saída `gate_m1c.json`.

**Famílias de acoplamento varridas (congeladas):**
1. Percolação transitiva $t_n=t^n$, $t\in\{0.05,0.1,0.2,0.5\}$ — CONTROLE
   (posts provados densos; T4 aplica).
2. Dust-like ($t_0\gg$ resto) — CONTROLE trivial (antichain, sem laços).
3. Lei de potência $t_n=(n{+}1)^{-a}$, $a\in\{0,0.5,1,2\}$ — sintoniza peso
   para anexar-a-muitos ($a$ pequeno) vs anexar-a-poucos ($a$ grande).
4. Crescente $t_n=c^n$ normalizado, $c>1$ — CANDIDATO a supressão de posts
   (testa se a valência diverge ou abre janela).
5. **Sonda do fio-da-navalha:** {t_n} sintonizado p/ grau-de-entrada médio fixo
   moderado (∈[4,8]) com dispersão máxima — o canto onde K2∧K5 teriam de
   coexistir.

**Medições** por (acoplamento, N), $N\in\{500,1000,2000,4000\}$, seeds ≥ 8:
- ⟨z⟩_Hasse(N) [K2]; ρ_post(N) [K3]; max/mean-block-size / N [K4];
- expoente $d$ do espaço de ciclos (rank $H_1$ em bolas $R\in[3,R_{\max}]$) [K5];
- densidade C4 e transitividade (âncora de retrodição: platô ≈0.019) [K6].

**Janelas de decisão (FROZEN):**
- **FECHAMENTO-consistente (esperado):** todo acoplamento dá OU [⟨z⟩ cresce com
  N, slope>0 robusto = boost-like] OU [ρ_post ≥ 0.02 assintótico E $d$ ≤ 1.3 E
  C4 sub-MF]. → fronteira permanece fechada (medição; o TEOREMA é o entregável).
- **DESCOBERTA (kill do fechamento):** algum {t_n} Bell-causal covariante com
  ⟨z⟩ limitada (≤30, plana em N) E ρ_post<0.005 decrescente E $d$≥1.7 E C4 acima
  do platô MF. → escape não-Poisson encontrado (substrato string-net).
- **Meio ambíguo ($1.3<d<1.7$):** INCONCLUSIVO-por-resolução declarado; escalar
  N ou refinar, NÃO reivindicar nenhum lado.
- Proibido: mover janela ou redefinir "post/covariante" pós-dado.

## 7. Desfechos pré-declarados (mortes)

- **D-M1c-1 (a descoberta):** gate sinaliza DESCOBERTA ⇒ o binário central tem
  escape não-Poisson; rota (ii) do core_paper "How to break" é REALIZADA;
  revisão maior do no-photon (torna-se Poisson-específico + foliação-específico,
  com uma TERCEIRA saída viva). Maior resultado possível do programa em 2026.
- **D-M1c-2 (fechamento parcial):** a conjectura de posts é FALSA com
  contraexemplo limpo (posts→0 a valência finita) MAS os laços não percolam
  ($d$≤1.3) ⇒ T4 não estende como enunciado, a fronteira estreita mas não abre;
  T4 no core_paper precisa da ressalva "TP + família com posts", e o
  fechamento passa a depender de (B)/(C).
- **FECHAMENTO (prior):** nenhuma morte dispara; entregar o teorema (A/B/C) e
  rebaixar o "[measured]" da CSG no core_paper para "[theorem] na família CSG,
  com a fronteira de geometria genuinamente dinâmica ainda declarada".
- Emendas só pré-run com trilha git (precedente N4/M1b/F2).

## 8. O que M1c NÃO reivindica (escopo honesto)

- CSG é UMA família invariante não-Poisson (crescimento sequencial, Markoviano,
  Bell-causal). **Geometria genuinamente fora-de-equilíbrio / não-Markoviana**
  (integral de caminho CDT com métrica flutuante; medidas com memória) permanece
  flanco SEPARADO e declarado (core_paper itens 9–10; flanco nº 2 de
  [[rs-trigger-csg-coordination]]). M1c fecha/testa o flanco nº 1 (medida
  dinâmica sobre causets) na sua realização canônica.
- Nada sobre se um string-net CONDENSA dinamicamente mesmo que o substrato
  cinemático exista (campanha futura, sem gatilho hoje).
- Nenhuma novidade matemática profunda reivindicada a priori; se (A) reduzir-se
  a Bollobás–Brightwell + um passo, o valor para o programa é fechar o flanco
  nomeado, não a profundidade.
