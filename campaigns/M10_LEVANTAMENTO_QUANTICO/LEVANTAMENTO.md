# M10 — LEVANTAMENTO: a fronteira quântica/não-Markoviana

**Data:** 2026-07-04 · **Pasta:** `FRONTEIRA_COMPACTA/M10_LEVANTAMENTO_QUANTICO/`
**Natureza:** levantamento analítico de escopo (precedente: LEVANTAMENTO_PRE_CAUSAL).
Zero código. **Objetivo:** filtrar os candidatos de medida não-Markoviana/quântica
sobre causets e decidir se existe UMA campanha com critério de morte — ou declarar
que não existe e por quê.
**Antecedentes:** C2 do paper de restrições declara a fronteira ("fluctuating causal
measure with memory"); N4 abriu a porta SJ e parou em ħ/colapso; M1c fechou toda
medida de crescimento Markoviana. **As duas fronteiras são o mesmo objeto** — a
dinâmica quântica de um causet é não-Markoviana por construção (interferência =
memória entre histórias).

---

## 0. Veredito em uma página

**Existe um candidato que passa no filtro inteiro, e só um: a integral de caminho
sobre ordens com a ação de Benincasa–Dowker (C3).** É bem-posta (espaço amostral
finito a N fixo), covariante (pesa classes de isomorfismo), tem critério de morte
limpo, reusa a bateria SNA de M5 verbatim — e tem a âncora de literatura decisiva:
**o peso da ação MUDA a tipicidade do ensemble** (suprime os bilayers
Kleitman–Rothschild que dominam a medida uniforme; e exibe uma fase "layered"/
cristalina a acoplamento forte, além da fase random/contínua). Ou seja: a resposta
à pergunta "pesos quânticos podem mudar QUEM domina?" já é SIM na literatura — o
que ninguém mediu é **de que lado da fronteira de invariância cada fase cai**.

**A campanha recomendada (TIPICIDADE QUÂNTICA, futura):** rodar a bateria SNA
(M5: valência, exp-rate/poly, plaqueta, posts) DENTRO das fases da integral de
caminho 2D. A pergunta central, com dois desfechos e ambos resultado:

1. **A fase random (contínua) é não-SNA e domina no regime físico** ⟹ as
   restrições C1–C8 são **quântico-robustas** (no regime analiticamente
   continuado): a primeira travessia da checklist para o lado quântico.
2. **A fase layered é SNA e domina em algum acoplamento** ⟹ a dinâmica quântica
   **escolhe espontaneamente o lado não-invariante** — o fóton torna-se possível
   ao preço de quebra espontânea de Lorentz. **E o iff de M5 sobrevive nos dois
   casos** (a fase layered É não-invariante): o que mudaria não é a classificação,
   é QUEM decide o lado — a cinemática (antes) ou a dinâmica (agora).

Dois candidatos secundários têm papel de apoio: a **TP complexa** (C2) como
aquecimento analítico (a densidade de posts tem forma fechada — a pergunta
"interferência suprime posts?" pode ter resposta no papel), e a **medida quantal
de Sorkin** (C1) como moldura interpretativa, não como campanha (sem dinâmica
canônica ⟹ sem critério de morte). Os demais (C4, C5) reprovam no filtro.

---

## 1. O filtro (aplicado a cada candidato)

| # | Critério |
|---|---|
| (a) | **Bem-posto:** a medida/amplitude é definida sem escolhas ad-hoc? |
| (b) | **Covariante/invariante:** pesa estrutura intrínseca (classes de isomorfismo), sem rótulo/embedding? |
| (c) | **Suporte vs pesos:** muda o espaço amostral ou só redistribui peso? (As C1–C8 são afirmações sobre tipicidade-no-suporte; só "pesos que movem tipicidade" ameaçam.) |
| (d) | **Critério de morte formulável:** existe medição que decide algo? |
| (e) | **Instrumento reusável:** a bateria M1c/M5 se aplica? |

## 2. Os candidatos

### C1 — Medida quantal de Sorkin (funcional de decoerência, co-eventos)
A generalização da teoria de medida para interferência (μ(A) do funcional de
decoerência D(A,A)), formulada precisamente para causets. **(a)** A MOLDURA é
bem-posta; a DINÂMICA não — qual D físico sobre causets é a pergunta em aberto há
décadas (o análogo quântico das regras Rideout–Sorkin não tem solução canônica).
**(b)** Formulável covariantemente (eventos-tronco/stem). **(c)** Muda pesos.
**(d) FALHA:** sem D canônico, qualquer morte pré-registrada testaria a NOSSA
escolha de D, não a classe — o resultado seria imune a generalização.
**Veredito: moldura de fundo, não campanha.** É a linguagem na qual C2/C3 devem
ser lidos, e a ponte com N4 (o funcional de decoerência é o mesmo objeto da porta
SJ/histórias).

### C2 — Crescimento sequencial quântico / percolação transitiva COMPLEXA
A deformação mínima: as constantes de acoplamento t_n da CSG tornadas complexas
(amplitudes de transição em vez de probabilidades); TP complexa (t_n = t^n, t ∈ ℂ)
é o exemplar. **(a)** Amplitudes bem-definidas por história rotulada; sutilezas:
covariância exige observáveis de classe (eventos-tronco) e probabilidades exigem
um D (volta a C1). **(b)** Sim, via eventos covariantes. **(c)** Pesos. **(d)**
PARCIAL — no nível da medida quantal de eventos específicos, sim: **a densidade de
posts em TP tem forma fechada (Bollobás–Brightwell, já usada em M1c); a versão
complexa é computável NO PAPEL.** A mini-pergunta analítica: *a interferência
suprime ou reforça posts?* (posts são eventos-tronco covariantes — exatamente o
objeto certo). Como M1c provou que posts ⟹ 1D, "interferência mata posts" seria o
primeiro indício de que o lado quântico foge do confinamento por blocos. **(e)**
O gerador rs_trigger generaliza. **Veredito: aquecimento analítico legítimo**
(um lema, não uma campanha): barato, com resposta possível em forma fechada, e
alimenta diretamente o desenho de C3. Risco declarado: sem D canônico, o
resultado é sobre a medida quantal de eventos-tronco, com essa qualificação.

### C3 — Integral de caminho sobre ordens com ação de Benincasa–Dowker ★
O ensemble estatístico de TODAS as ordens de N elementos (tipicamente a classe
2D-orders, computacionalmente tratável) pesado por e^{iS_BD}, estudado via
continuação analítica (β real) e MCMC — o programa de dinâmica de causets de
Surya e colaboradores. **(a)** Bem-posto: espaço amostral FINITO a N fixo; ação
intrínseca (contagens de intervalos); continuação declarada (mesma ressalva de
toda QFT de rede). **(b)** Covariante: pesa classes de isomorfismo, sem rótulo.
**(c)** **Pesos que comprovadamente MOVEM a tipicidade** — as duas âncoras:
(i) a ação BD SUPRIME os posets bilayer de Kleitman–Rothschild que dominam
entropicamente a medida uniforme (o path integral escapa da "catástrofe KR");
(ii) o diagrama de fases 2D exibe transição entre uma fase **random/contínua**
(tipo-Poisson) e uma fase **layered/cristalina** a acoplamento forte. **(d)**
LIMPO: medir a bateria SNA dentro de cada fase; janelas herdadas de M5, mortes
formuláveis nos dois sentidos. **(e)** TOTAL: a bateria M1c/M5 (valência,
exp-rate, poly, plaqueta C4/N, posts) aplica-se verbatim ao Hasse das ordens
amostradas; falta só o amostrador MCMC de 2D-orders (permutation pairs), que é
implementável e tem precedente publicado em N~50–100.
**Veredito: O CANDIDATO.** Única entrada que passa (a)–(e) inteiro.

**A leitura fina que torna C3 valioso nos dois desfechos:** a fase layered é
graduada/cristalina — pela NOSSA classificação (M5), é o lado não-invariante.
Então mesmo o desfecho "dramático" (layered domina e é SNA) não quebra o iff de
M5; ele o **completa dinamicamente**: a integral de caminho realizaria quebra
espontânea de invariância como FASE, e o custo do fóton ("quebrar Lorentz")
passaria de escolha de modelo a transição de fase. O desfecho conservador
(random domina, não-SNA) daria a primeira extensão quântica da checklist. Não
há desfecho vazio — o critério do conselho nº 4 (aposta arriscada nos dois
sentidos) é satisfeito.

### C4 — Energetic causal sets (Cortês–Smolin)
Dinâmica com momenta/energia nos eventos. **(b) FALHA:** os dados dinâmicos são
coordenadas de embedding (momenta em ℝ^d), fora da classe intrínseca — a
checklist nem se aplica sem tradução. Programa distinto, não candidato.

### C5 — Rewriting determinístico de (hiper)grafos (estilo Wolfram)
**(b)/(c) FALHAM para o nosso uso:** regras determinísticas geram estruturas
quase-cristalinas — genericamente o lado NÃO-invariante da classificação (M5 já
os localiza por inspeção: é o caso "rigid crystal" da tabela do paper de
restrições). Não é medida sobre causets; é um candidato a SER avaliado pela
checklist, não a estendê-la.

## 3. Tabela-filtro

| Candidato | (a) bem-posto | (b) covariante | (c) move tipicidade | (d) morte | (e) instrumento | Veredito |
|---|---|---|---|---|---|---|
| C1 medida quantal | moldura sim, dinâmica NÃO | sim | pesos | **não** (sem D canônico) | — | fundo interpretativo |
| C2 TP complexa | sim (com quals.) | via stem-events | pesos | parcial (forma fechada de posts) | rs_trigger | **lema analítico de aquecimento** |
| **C3 path integral BD** | **sim** | **sim** | **sim (KR + layered, literatura)** | **sim (bateria SNA por fase)** | **M5 verbatim + MCMC novo** | **★ a campanha** |
| C4 energetic CS | sim | **não** (embedding) | — | — | — | fora da classe |
| C5 rewriting | sim | **não** (determinístico) | suporte | — | — | avaliando, não estendendo |

## 4. A campanha recomendada (esboço; pré-registro SÓ após §5)

**Nome provisório:** N6_TIPICIDADE_QUANTICA. **Pergunta:** *o ensemble
quanticamente pesado (BD, continuado) fica do lado invariante da classificação
(fase random, não-SNA) ou migra espontaneamente para o lado não-invariante
(fase layered) — e a fase layered é SNA de fato?*

- **Fase 0 (analítica):** conferir âncoras NA FONTE (§5); lema C2 (posts sob t
  complexo, forma fechada); congelar a leitura BD-2D e o esquema de continuação.
- **Gate de engenharia:** amostrador MCMC de 2D-orders reproduz resultados
  publicados (localização da transição, observáveis de ação) ANTES de qualquer
  medição nova.
- **Fase 1:** bateria SNA (M5, janelas FROZEN herdadas) dentro das duas fases,
  varrendo o acoplamento pela transição; N na faixa com precedente publicado.
- **Mortes candidatas (a congelar no pré-registro):** D1 fase layered é SNA E
  domina em regime declarado-físico ⟹ escape dinâmico real (quebra espontânea);
  D2 nenhuma fase é SNA ⟹ checklist quântico-robusta (no regime continuado);
  D3 bateria inconclusiva na transição ⟹ INCONCLUSIVO-por-resolução, escalar N.
- **Custo estimado:** MCMC 2D-orders a N≲100 é barato por config; a bateria é a
  já paga. Campanha computacional MODERADA (menor que N4, maior que F2).
- **Escopo desde já:** tudo no regime analiticamente CONTINUADO (β real) — a
  versão genuinamente quântica (pesos complexos + D) fica explicitamente fora,
  com C2 como única sonda; dizer isso sem upgrade retórico.

## 5. Âncoras a conferir NA FONTE antes do pré-registro (disciplina N4-Fase-0)

Este levantamento cita literatura DE MEMÓRIA; nenhuma janela será congelada sem
conferência na fonte (precedente: N4 Fase 0, "10 âncoras conferidas"):

1. MCMC de 2D-orders com ação BD: existência/ordem da transição random↔layered,
   acoplamentos, tamanhos (Surya e colaboradores; série de papers ~2012–2019).
2. Supressão dos posets KR/bilayer pela ação BD (Loomis–Surya ~2017/18).
3. Observáveis covariantes/eventos-tronco na CSG e sua versão quântica
   (Dowker–Zalel e antecessores).
4. Forma fechada da densidade de posts em TP (Bollobás–Brightwell; já usada em
   M1c — reconferir o enunciado exato para t complexo).
5. Medida quantal/funcional de decoerência de Sorkin (formulação para causets).

## 6. O que este levantamento NÃO é

Não é pré-registro (nenhuma janela congelada aqui); não reivindica nenhum
resultado sobre a fase layered (a pergunta SNA-por-fase está ABERTA — é
exatamente por isso que é campanha); não toca os papers submetidos; e não
promove a analogia informação/computação a programa — ela permanece gesto de
discussão até ter critério de morte próprio (posição registrada em
[[direcao-pos-fechamento]]).
