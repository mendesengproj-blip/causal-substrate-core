# PRÉ-REGISTRO DA SEMENTE — "a informação SOURCE o crescimento"

> **Por que este documento existe.** A semente (charter §0.1) é, hoje, um **princípio
> evocativo** — bonito, mas sem mecanismo, forma ou tamanho. O charter só tem um *esboço* de
> critério de morte (§0.1: "a rede *sourced* tem que ser estatisticamente diferente da CDT
> cega"), não uma hipótese falsificável. Este pré-registro **converte a semente de poesia em
> mecanismo testável**, com a mesma disciplina anti-circularidade + critério de morte que toda
> outra hipótese deste pipeline recebeu (Campanha XI/XII, FX1, etc.). Congelado **antes** de
> qualquer código que a teste, e **antes** de a semente virar pressuposto arquitetural de uma
> fase cara.
>
> **Estado:** PRÉ-REGISTRADO, NÃO EXECUTADO. **Data:** 2026-06-28.
> **Posição na fila:** a semente NÃO entra em F1 nem F1b (gravidade pura, crescimento cego).
> Este teste é uma fase própria (chamada **FS**, "Fase Semente"), a rodar **depois** de F2 ter
> estabelecido que existe geometria estável de fundo sobre a qual acoplar informação — e
> **só** se este pré-registro der um observável genuíno (senão a semente morre no papel, aqui).

---

## 0. A pergunta que o pré-registro tem que responder ANTES de qualquer código

> **A semente é um mecanismo testável, ou é poesia de fundamentação?**
> Concretamente (a pergunta exata do escrutínio): *qual observável distinguiria "a informação
> SOURCE o crescimento" de uma regra de crescimento genérica que não tem esse princípio?*

Se as seções abaixo não entregarem **um observável que separe a semente de (a) CDT cega E de
(b) uma regra de crescimento puramente geométrica**, então a semente é decoração, e a
**TEORIA_CDT não é mais que a CDT padrão re-rodada** — exatamente o risco [CLASSE GRANDE] que
fechou a `NOVA TEORIA/` (invariantes genéricos não selecionam estrutura). A semente é a **única
coisa** que protege esta teoria desse destino. Por isso ela tem que passar por aqui primeiro.

---

## 1. O mecanismo (especificado o suficiente para virar equação)

Sem isto, não há o que testar. A semente fica:

**Um campo de informação φ vive na triangulação** (φ_v ≥ 0 em cada vértice v = "densidade de
informação registrada naquele nó"). A dinâmica acopla geometria e informação em **ciclo
fechado** (o "ser-evento ↔ ser-distribuição" do charter §0.1):

1. **Informação SOURCE o crescimento (o acoplamento γ).** A taxa do move de Pachner que
   *cria* volume (inserção de vértice) na vizinhança de x é **modulada pela informação local**:
   `taxa_add(x) ∝ exp(γ · φ_x)`. γ ≥ 0 é o **acoplamento semente** (`[External]`, como a
   aresta — não se afirma que γ emerge). γ=0 = crescimento cego (informação não toca a
   geometria).

2. **O crescimento re-emite informação (o ciclo).** Cada evento de crescimento **deposita**
   Δφ no nó novo (o evento é "registrado" — volta à rede), e φ **transporta** na geometria
   *atual* entre passos (difusão no Laplaciano do grafo: `φ ← (1−κ)φ + κ L̂φ`, κ
   `[External]`). Logo a informação que biasa o crescimento de amanhã foi **depositada e
   transportada** pelo crescimento de ontem. Geometria e informação **co-determinadas**.

3. **Inversão da CDT padrão (a tese):** aqui a informação/matéria é fundamental e a geometria é
   o **registro** da expansão dela — não um campo passivo numa geometria que cresce sozinha.

**Limite-controle embutido:** γ=0 (informação passiva, só difunde) reproduz a CDT cega com um
espectador escalar. Este é o **NULO** contra o qual a semente é medida.

---

## 2. Os DOIS critérios de morte empilhados (o coração da falsificação)

A semente só sobrevive se passar **ambos**. Cada um responde a uma metade da pergunta §0.

### D1 — vs CDT CEGA: a informação muda a geometria, ou é decoração?

**Hipótese:** com γ>0, a **geometria emergente** (não o campo — a geometria) é
**estatisticamente diferente** da CDT cega (γ=0).

**Observáveis (da geometria, medidos pela maquinaria já validada em F1):** d_H, dimensão
espectral d_s, distribuição do perfil de volume P(ℓ_t), distribuição de curvatura (déficit) em
3D/4D, e a **homogeneidade** (a informação deveria *agrupar* o crescimento → geometria mais
inomogênea/clumped).

> **MORTE D1:** se {d_H, d_s, P(ℓ), curvatura, homogeneidade} de γ>0 são
> **indistinguíveis** de γ=0 dentro da barra de erro por *blocking* (a lição do G5 de F1:
> erro autocorrelação-aware, não ingênuo), a informação é **decoração** → a semente é
> falsa, a TEORIA_CDT colapsa na CDT padrão. **Pré-registrado como morte definitiva.**

### D2 — vs REGRA GEOMÉTRICA GENÉRICA: "informação" é mais que uma palavra para "peso de crescimento"?

Esta é a metade que responde **diretamente** à pergunta do escrutínio. Uma regra de
crescimento genérica também modula o crescimento — mas por **geometria** (ex.: peso por
curvatura, `taxa_add(x) ∝ exp(γ·curvatura_x)`), sem campo de informação. Se a semente produz a
**mesma** geometria que essa regra geométrica, então "informação" é só um **nome chique para um
peso de crescimento** — o princípio não adiciona nada.

**Controle obrigatório:** rodar uma **regra geométrica markoviana** (peso por curvatura/volume
local, sem campo φ, sem memória) calibrada para a mesma intensidade de modulação.

**A assinatura ÚNICA da semente = MEMÓRIA NÃO-MARKOVIANA.** O que distingue φ de um peso
geométrico é que φ **carrega o passado**: onde o crescimento ocorre hoje depende da informação
**depositada e transportada por eventos passados**, não só da geometria local instantânea. O
observável que isola isto:

- **C_mem(τ):** correlação causal entre o **local** de um evento de crescimento em t e o local
  de deposição de informação em t−τ (rastreada pelo transporte de φ). Numa regra geométrica
  markoviana, C_mem(τ>0) → 0 (sem memória do passado além da geometria atual). Na semente,
  C_mem(τ) tem **cauda** (a informação transportada lembra de onde veio).

> **MORTE D2:** se a geometria de γ>0 é indistinguível da regra geométrica markoviana de
> mesma intensidade **E** C_mem(τ) não tem cauda acima do controle, então a "informação" não
> faz nada que um peso geométrico não faça → o princípio é **poesia**, mesmo que D1 tenha
> passado (geometria ≠ CDT cega, mas só porque *qualquer* peso a mudaria). **Pré-registrado
> como morte definitiva.**

**Sucesso da semente = passar D1 E D2:** a geometria com γ>0 difere da CDT cega (D1) **e** essa
diferença NÃO é reproduzível por uma regra geométrica sem memória (D2), com C_mem(τ) exibindo a
cauda de memória. Só então "a informação SOURCE o crescimento" é uma afirmação física, não uma
metáfora.

---

## 3. Anti-circularidade (não-negociável, herdado do charter §3)

1. **γ e κ são `[External]`.** A semente NÃO afirma que o acoplamento emerge. O teste é
   **estrutural** (o acoplamento muda a *classe* da geometria?), nunca "um número emergiu".
2. **Nenhuma escala emerge da semente.** Se γ>0 gera um comprimento, ele vem de γ/κ
   `[External]`, não é derivado — declarar, não maquiar (a parede de escala do programa inteiro
   continua de pé; a semente não a fura).
3. **Nada de TEIC/DEV/SR.** φ é re-derivado aqui; a palavra "informação" não importa a
   "saturação holográfica" da SR nem a "orientação" da TEIC — é o campo definido em §1, ponto.
4. **Pré-registro antes de medir; sem annealing.** D1/D2 e os observáveis estão congelados
   aqui. "Se der quase, talvez conte" é proibido.

---

## 4. Prior honesto (declarar, não pender)

- **A semente provavelmente NÃO mostra nada em 2D.** Em 2D a geometria é rígida (d_H=2 forçado
  pela folheação; curvatura topológica) — um acoplamento fraco pode não conseguir mover os
  observáveis (risco de MORTE D1 trivial/não-informativa em 2D). Logo o teste **honesto** da
  semente é **3D/4D**, onde a geometria tem liberdade (curvatura dinâmica, fases). Consistente
  com o charter pôr a semente em F2+.
- **D2 é o filtro mais provável de matar.** É fácil uma geometria com peso mudar vs CDT cega
  (D1); é **difícil** essa mudança ser irreplicável por um peso geométrico markoviano (D2). A
  memória não-markoviana pode lavar no equilíbrio (ecoa o achado B7/Campanha XI: o substrato
  tende a campo-médio sem cauda — [[escala-xi-correlation-divergence]]). **Se C_mem não tiver
  cauda, a semente morre em D2**, e isso seria o mesmo mecanismo que matou a transmutação de
  escala na TEIC.
- **Resultado mais provável (declarado de antemão):** a semente passa D1 (qualquer peso muda a
  geometria) mas **morre em D2** (a memória não sobrevive ao equilíbrio) — i.e., "informação
  fonte o crescimento" seria, ao fim, **indistinguível de uma regra de crescimento geométrica**,
  e a TEORIA_CDT seria CDT-com-peso, não uma teoria nova. **Este desfecho não é fracasso** — é
  o mesmo tipo de morte limpa e publicável que o charter §6 já abraça. O fracasso seria não
  saber qual desfecho ocorreu.

---

## 5. Por que isto tem que vir ANTES de gastar em F2-com-semente

A `NOVA TEORIA/` fechou em **[CLASSE GRANDE]** porque os invariantes compartilhados eram
**genéricos-por-teorema** — não selecionavam estrutura. O risco gêmeo aqui: **os resultados de
CDT que F1/F1b/F2 reproduzem (d_H=2, d_s 4→2, geometria estendida) são TODOS genéricos** — são
o que *qualquer* gravidade quântica 2D/4D viável dá (são `[GABARITO]`/validação, charter §3.6).
**A única coisa não-genérica que a TEORIA_CDT pode oferecer é a semente** (o Nível C: algo
adimensional que cai *por causa* da informação-source). Se a semente é decoração (morre em D1 ou
D2), então a TEORIA_CDT **é** [CLASSE GRANDE] — mais um membro da classe "gravidade quântica
viável", sem novidade. Por isso o veredito da semente (este pré-registro, executado) é
**logicamente anterior** a qualquer investimento que a pressuponha: ele decide se há teoria
nova **para** construir.

---

## 6. Entregáveis (quando executar a Fase FS, pós-F2)

`fs_seed.py` (campo φ + acoplamento γ + transporte κ sobre a maquinaria de F1b/3D),
`fs_pre_gate.json` (controles: γ=0 = CDT cega; regra geométrica markoviana), `FS_SYNTHESIS.md`
(veredito D1/D2 com barras de erro por blocking + C_mem(τ)). **Bloqueio:** não rodar antes de
F2 dar geometria de fundo estável (Nível A) — sem fundo, não há onde acoplar informação.

**Resumo de uma linha:** a semente vira física **se e somente se** uma geometria *sourced* por
informação (D1) diferir da CDT cega **e** essa diferença não for reproduzível por um peso
geométrico sem memória (D2, com C_mem de cauda); senão, "a informação SOURCE o crescimento" é
poesia e a TEORIA_CDT é CDT padrão — um veredito que este pré-registro torna **falsificável
antes** de gastar em construí-la.

---

## ADENDO FS-2D — sonda barata no motor de F1 (congelado 2026-06-28, ANTES de rodar)

**Estatuto:** indicador antecipado **EXPLORATÓRIO**, **NÃO** o teste de morte D1 (que permanece
3D — §4: em 2D a geometria é rígida, d_H=2 forçado pela folheação). Roda agora porque é
**quase grátis** no motor já validado (F1), e um **positivo** seria informativo mesmo sendo 2D.

**Mecanismo 2D (realização mínima, φ no DUAL = por triângulo):** φ_i ≥ 0 em cada triângulo
("informação registrada na 2-célula"). (1) **Source:** a aceitação do move `add` em i ganha
fator `exp(γ·(φ_i − φ̄))` — alta informação local → mais crescimento ali; γ=0 ⇒ fator 1 ⇒
**CDT cega validada**. (2) **Depósito:** ao crescer em i, os triângulos novos herdam φ_i + δ e
φ_i recebe um bump (registro) → feedback positivo (clumping). (3) **Transporte:** a cada sweep
`φ ← (1−κ)φ + κ·⟨φ_vizinhos no dual⟩`, depois renormaliza ⟨φ⟩=1 (γ controla **contraste**, não
escala absoluta). δ, κ, γ todos `[External]`.

**Observáveis (CONGELADOS):**
- **O1 = d_H(γ)** vs d_H(0): a dimensão se move?
- **O2 = R = Var(ℓ_t)/⟨ℓ_t⟩²** (clumping espacial): a informação **agrupa** o crescimento
  (algumas fatias incham, outras minguam) → R sobe com γ?
- **O3 = razão de participação de φ** (PR = ⟨φ⟩²/⟨φ²⟩, baixo = concentrado): a informação se
  **auto-concentra**?

**Regra de inferência (CONGELADA, ASSIMÉTRICA — sem annealing):**
- **POSITIVO:** O2 sobe monotonicamente e claramente com γ (além do erro por *blocking*) e/ou
  d_H se desloca → a semente tem **assinatura mesmo em 2D rígido** → indicador **DISPARA** →
  **eleva o prior** para a campanha FS-3D (o teste vinculante D1/D2).
- **NULO:** O1/O2/O3 não se movem com γ → **consistente com o prior §4** (2D rígido demais) →
  **NÃO-INFORMATIVO, NÃO é morte da semente** → o veredito vinculante fica para FS-3D. Um nulo
  aqui **não** pode ser citado como "a semente passou" nem como "a semente morreu".
- **Varredura:** γ ∈ {0, 1, 2, 4} (0 = controle = CDT cega), erro por blocking (lição G5).

---

## ADENDO TAREFA-2 — controle de campo genérico vs barreira c=1 (congelado 2026-06-28, ANTES de rodar)

**Por quê.** Gravidade 2D acoplada a matéria com carga central efetiva **c>1** colapsa numa fase
patológica **universal** (branched-polymer, d_s→≈1), **independente do conteúdo do campo** — só
pela força do acoplamento. O resultado FS-2D (clumping ×100, d_H 2.1→1.1 com γ) tem a assinatura
**exata** dessa fase. Antes que o D1 conte como evidência **pró-semente**, isto tem que ser
descartado como explicação completa.

**Método.** O que distingue a semente de "um campo escalar qualquer com feedback positivo" é o
**transporte não-markoviano** (κ — a re-emissão nó-a-nó, a parte estrutural distintiva). O
controle genérico = **mesma forma de acoplamento e depósito, SEM transporte (κ=0)**. Varre-se o
mesmo γ ∈ {0,1,2,4} para **κ ∈ {0 (controle genérico), 0.3 (semente FS-2D), 0.6 (transporte
forte)}**, mesmo ensemble/ladder; mede d_H(γ,κ) e clumping(γ,κ), erro por blocking.

**Critério (CONGELADO, sem ajuste depois):**
- **REBAIXA D1:** se o colapso (d_H(γ=4) e clumping) for **κ-independente** — Δd_H(γ=4) entre
  κ∈{0,0.3,0.6} < 0.15 **e** clumping(γ=4) dentro de fator 2× entre κ — então o colapso é
  **dirigido pelo acoplamento, não pelo transporte** ⇒ é a barreira c=1/branched-polymer
  genérica ⇒ o "positivo" do FS-2D é **rebaixado** para "consistente com fase patológica
  conhecida de gravidade-matéria 2D, **não-específico à semente**". A evidência pró-semente
  passa a depender **inteiramente de D2 (memória, C_mem) em 3D**.
- **D1 SOBREVIVE:** se κ muda o colapso qualitativamente (Δd_H(γ=4) > 0.3, ou clumping de
  assinatura distinta) ⇒ o transporte faz algo que o feedback genérico não faz ⇒ D1 sobrevive
  como evidência (prior elevado), **mas D2/3D continua sendo o discriminador real** — este
  controle protege D1 de falso-positivo, não substitui D2.
- **AMBÍGUO:** resultado intermediário ⇒ reporta como **não-decisivo**, não força direção.

### RESULTADO TAREFA-2 (executado 2026-06-28) — D1 REBAIXADO na interpretação (apesar do binário dizer "sobrevive")

`F1_acao/task2_generic_control.py`, dados `task2_generic_control.json`. Varredura γ×κ:

| γ=4 (colapso máximo) | κ=0 (GENÉRICO, sem transporte) | κ=0.3 (semente) | κ=0.6 |
|---|---|---|---|
| d_H | **1.60** | 1.07 | 1.00 |
| clumping | **11.2** | 20.0 | 17.6 |

**O que o critério binário congelado disse:** spread d_H(γ=4)=0.60 > 0.30 ⇒ ramo "**D1
SOBREVIVE**" (o transporte κ muda o colapso). **Reporto isto fielmente — sem annealing.**

**A leitura honesta que SUPERA o binário (e o critério estava mal-desenhado):** o ponto decisivo
não é "κ muda o colapso?" mas "**o colapso acontece SEM o ingrediente distintivo da semente?**".
E acontece: **em κ=0 (campo genérico, só feedback de depósito, sem transporte) o d_H já desaba
2.07→1.60 e o clumping sobe ×11**. Ou seja, **feedback positivo genérico sozinho já produz o
colapso** — é a barreira **c=1/branched-polymer**, exatamente a preocupação da Tarefa-2,
**confirmada**. O transporte κ apenas **aprofunda** o colapso (1.60→1.00), o que é plausivelmente
só um **reescalonamento do acoplamento efetivo** (mais transporte espalha φ → c efetivo maior),
**não** um efeito físico qualitativamente novo.

**Veredito honesto (supera o binário):** o "positivo" do FS-2D é **substancialmente
não-específico à semente** — é a fase patológica genérica de gravidade-matéria 2D. O critério
binário pré-registrado deu "sobrevive" por uma **tecnicalidade** (transporte muda a profundidade),
mas a conclusão prática é a do ramo de **REBAIXAMENTO**: **a evidência pró-semente NÃO pode se
apoiar em D1/FS-2D; depende inteiramente de D2 (memória/C_mem) em 3D.** Registro também a falha de
desenho do critério (deveria ter chaveado em "κ=0 colapsa sozinho?", não em "κ muda o colapso?")
— a disciplina exige admitir isto em vez de me esconder atrás do binário favorável.
