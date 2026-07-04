# TEORIA CDT — Charter fundacional

> **Documento independente e autocontido.** Esta teoria começa do zero. Ela **não herda**
> resultados, suposições, código ou vereditos de TEIC, DEV ou SR. Aquelas teorias são
> mencionadas aqui **apenas** como contexto histórico (de onde veio a motivação) e como
> **anti-padrões a evitar** — nunca como fundação. Se em qualquer ponto futuro esta teoria
> precisar de um resultado de TEIC/DEV/SR, ele deve ser **re-derivado dentro desta teoria**,
> não importado. **Regra de não-contaminação: nada entra sem ser construído aqui.**
>
> **Data de fundação:** 2026-06-27.
> **Estado:** FUNDAÇÃO — nenhuma física construída ainda. Este charter define o que vamos
> fazer, o que buscamos, e como saberemos se falhamos.

---

## 0. Por que esta teoria existe (a única frase)

Partir da mesma semente que gerou a TEIC — **a realidade é informação que se expande**, em que
cada evento é registrado numa rede que cresce e re-emite essa informação nó a nó — mas agora
hospedada no substrato **CDT (Causal Dynamical Triangulations)**, o único da "fila de
substratos" que tem laços, criticalidade e dimensão que corre; e usar a **TEIC como mapa** (ver
`MAPA_TEIC_BENCHMARK.md`): reproduzir o que ela explicou e **furar as paredes onde ela parou** —
porque essas paredes (mean-field, dimensão que não corre, escala não-derivada) foram causadas
pelo substrato mean-field da TEIC, e a CDT é justamente o substrato que não as tem.

## 0.1 A semente (o ingrediente original — o análogo da "orientação" da TEIC)

A TEIC nasceu de uma intuição — **centros de informação que se expandem**: um evento gera um
fóton → a informação é registrada na rede → a rede cresce → a informação atualiza a cada nó,
alternando entre **ser evento** (volta à realidade) e **ser distribuição** (volta à rede). O
espaço-tempo é o **rastro** desse ciclo. Quando a TEIC formalizou isso como "rede causal que
cresce", colapsou na CST (e, como medimos, num **grafo tipo-árvore mean-field**) — o ciclo vivo
evaporou. **A adição original desta teoria** é o que se perdeu lá: **o centro de informação
SOURCE o crescimento** — a propagação da informação é o que dispara o crescimento local da rede
(um movimento de Pachner *sourced* pela informação), em vez de um campo passivo numa geometria
que cresce sozinha. Geometria e informação são **co-determinadas**. Inverte a CDT padrão: aqui
a informação/matéria é fundamental e o espaço-tempo é o registro da expansão dela.

**O critério de morte que protege contra repetir a TEIC:** a rede gerada por crescimento
*sourced* por informação tem que ser **estatisticamente diferente** da CDT pura (crescimento
cego). Se a geometria emergente sair idêntica à CDT sem informação, a informação é decoração —
e morremos do mesmo jeito que a TEIC. Isto é pré-registrado em cada fase.

---

## 1. De onde viemos (contexto, NÃO fundação)

Três teorias anteriores (TEIC, DEV, SR) foram exploradas a fundo. O aprendizado que **motiva**
esta nova teoria — e que é a única coisa que carregamos adiante (como lição, não como
resultado) — foi:

1. **O padrão forma/escala.** Repetidamente, aquelas teorias **reproduziam as formas** da
   física (padrões, estatísticas, comportamentos-limite) mas **nunca forçavam as escalas**
   (os números absolutos: G, ℏ, a₀). A escala vinha sempre de fora.
2. **A fila de substratos.** Testamos, com filtros baratos, quais "tecidos" discretos de
   espaço-tempo escapam de virar mean-field trivial (uma "multidão sem estrutura"). Duas
   barreiras baratas:
   - **Barreira 1 — coordenação:** o número de vizinhos por ponto não pode divergir.
   - **Barreira 2 — laços:** a malha precisa de laços locais (não pode ser uma árvore).
3. **O resultado que aponta para cá.** Sprinkling de Poisson morreu na barreira 1; o
   crescimento sequencial (CSG) passou a 1 mas morreu na 2 (é uma árvore disfarçada);
   **a classe tipo-CDT foi a única a passar as duas barreiras** (teste cinemático,
   `TEIC/docs/campaigns/CDT_VIABILIDADE/`).

> **Atenção honesta sobre o item 3.** Aquele "passou" foi **fraco e cinemático**: em 2D, ter
> o número certo de vizinhos é uma trivialidade geométrica (identidade de Euler, ⟨z⟩→6 para
> qualquer triangulação), e os laços vêm "de graça" de uma superfície ser feita de triângulos.
> Aquele teste **não tinha ação dinâmica** — e é exatamente a ação que separa CDT real de
> geometrias patológicas (branched-polymer). Portanto o ponto de partida desta teoria **não
> é** "CDT já venceu"; é "CDT é a única candidata que sobrou, e agora temos que construí-la
> de verdade e ver se ela vale alguma coisa".

**Tudo o que segue é construído nesta teoria. Os itens acima são por que começamos, não o que assumimos.**

---

## 2. O que estamos buscando (os alvos, em ordem de ambição)

Três níveis. Não pular níveis. Cada um tem critério de sucesso e de morte.

### Nível A — Geometria emerge (o piso; sem isso, nada feito)
**Pergunta:** a soma sobre triangulações com a ação de Regge, após rotação de Wick, produz um
espaço-tempo de **dimensão correta e estável** em grande escala (dimensão de Hausdorff ≈ 4 no
IR; dimensão espectral correndo de ~4 no IR para ~2 no UV), ou colapsa numa fase patológica
(branched-polymer com dimensão divergente / fase "crumpled" com dimensão infinita)?

- **Sucesso A:** existe uma fase (uma janela dos acoplamentos) onde a dimensão é estável e
  física, reproduzindo o achado central da CDT real (Ambjørn–Jurkiewicz–Loll).
- **Morte A:** só há fases patológicas; nenhuma janela com geometria estendida. → a classe
  tipo-CDT não funciona nem como gravidade pura; teoria encerrada.

### Nível B — Há criticalidade não-trivial (a ponte para escala)
**Pergunta:** existe um **ponto crítico de 2ª ordem** (transição contínua) na fronteira entre
fases, onde um comprimento de correlação **diverge**? É a única forma conhecida de um sistema
discreto "esquecer" o tamanho do bloco e gerar uma escala contínua (limite do contínuo).

- **Sucesso B:** ponto crítico de 2ª ordem identificado, com expoentes medidos. → existe um
  limite do contínuo candidato.
- **Morte B:** todas as transições são de 1ª ordem (descontínuas) → sem limite do contínuo →
  a teoria fica presa na escala do bloco (a mesma parede de escala das teorias anteriores,
  agora confirmada para CDT). **Este é o desfecho que as teorias anteriores tornam mais
  provável — e é por isso que é o teste decisivo.**

### Nível C — Algo cai de graça (o sonho, só se A e B passarem)
**Pergunta:** no ponto crítico, alguma quantidade **adimensional** (uma razão, um expoente, um
número) sai **forçada** pela estrutura — algo que não foi inserido e que a teoria **prevê**?

- **Sucesso C:** uma previsão adimensional falsificável que nenhuma entrada fixou. → a teoria
  diz algo novo sobre o mundo.
- **Resultado honesto esperado:** mesmo com A e B, **a escala absoluta provavelmente continua
  externa** (o bloco é `[External]` por construção). O ganho realista do Nível C é uma
  **razão** ou um **expoente**, não G ou ℏ. Declarar isso desde já evita auto-engano.

---

## 3. A linha vermelha anti-contaminação (a regra que protege a honestidade)

Esta teoria foi criada **porque** as anteriores tinham um padrão perigoso: era fácil confundir
"a forma emergiu" com "a teoria funciona". Para não repetir isso:

1. **Aresta = `[External]`, sempre.** O tamanho do bloco é inserido. **Nenhuma frase, em
   nenhum documento desta teoria, pode dizer "uma escala emergiu" se ela vier do tamanho da
   aresta.** Escala só conta como emergente se vier de criticalidade (Nível B), e mesmo aí
   é uma razão adimensional, não o bloco.
2. **Nada de TEIC/DEV/SR entra como dado.** Se precisarmos de um resultado deles, re-derivamos
   aqui ou marcamos `[EXTERNO NÃO RE-DERIVADO]` e não construímos em cima.
2b. **A TEIC entra como MAPA, não como dado** (ver `MAPA_TEIC_BENCHMARK.md`). Os fenômenos que
   ela explicou e as paredes onde ela parou são **alvos** (`[ALVO-TEIC]`), não premissas — como
   a TEIC usou Lorentz/Myrheim-Meyer da CST para validar, não como axiomas. **Proibido** usar um
   resultado da TEIC como passo de uma derivação aqui; **exigido** medir-se contra o mapa dela
   ("reproduzimos qual S#? furamos qual W#?"). Reproduzir um sucesso da TEIC é **validação**;
   furar uma parede dela é **o produto**.
3. **Pré-registro antes de medir.** Todo experimento congela predições + critério de morte
   **antes** de rodar (a disciplina que funcionou nas campanhas anteriores). Morte
   pré-registrada é definitiva; sem annealing depois de ver a curva.
4. **Gate de engenharia antes de física.** Todo código passa por validação contra casos
   conhecidos (geometrias calculáveis à mão) antes de qualquer leitura física.
5. **Distinguir cinemática de dinâmica.** O teste anterior (Gatilho 3) foi só cinemático e
   por isso fraco. Aqui, **nenhum veredito de viabilidade é dado sem a ação dinâmica** rodando.
6. **Forma ≠ função.** Reproduzir o que a CDT real já mostra é **validação**, não descoberta.
   Descoberta é só o que cai a mais (Nível C).

---

## 4. Plano mínimo de construção (sem executar nada ainda — só o mapa)

Fases sequenciais. Cada fase é uma campanha com pré-registro próprio, dentro de `TEORIA_CDT/`.

| Fase | O que constrói | Pergunta-gate | Entrega |
|---|---|---|---|
| **F0 — Fundação** | este charter + glossário + decisões de escopo | escopo claro, anti-contaminação travada | `CHARTER.md` (este), `GLOSSARIO.md` |
| **F1 — Ensemble + ação** | triangulações causais (folheadas no tempo) + ação de Regge discreta + peso e^{-S} | a ação está correta (limites conhecidos)? | `F1_acao/` (pré-registro + gate) |
| **F2 — Geometria (Nível A)** | Monte Carlo sobre triangulações + medição de dimensão de Hausdorff e espectral | existe fase de geometria estável? | `F2_geometria/` |
| **F3 — Fases & criticalidade (Nível B)** | diagrama de fases + busca de transição de 2ª ordem | há ponto crítico contínuo? | `F3_criticalidade/` |
| **F4 — O que cai de graça (Nível C)** | medir quantidades adimensionais no ponto crítico | alguma previsão forçada não-inserida? | `F4_previsao/` |

> **F1 é o primeiro passo real.** Nada de F2+ roda antes de F1 passar seu gate (a ação tem que
> reproduzir limites conhecidos — ex.: deficit angular de Regge → curvatura no limite suave).
> A separação tempo-tipo/espaço-tipo (a parte "causal" e "dynamical" do CDT, a folheação que
> evita as patologias do DT euclidiano puro) é decisão de F1 e deve ser **explícita**.

---

## 5. Decisões de escopo a travar em F0 (registrar a escolha, não deixar implícito)

- **Dimensão de trabalho:** começar em **2D** (barato, mas lembrar que ⟨z⟩=6 é trivial lá — a
  física interessante de dimensão só aparece em 3D/4D) e **só then** subir. Decidir em F1 se o
  alvo é 3D (onde a coordenação volta a ser informativa) ou 4D (onde está a física real e o
  resultado célebre da CDT). **Recomendação inicial:** prototipar em 2D para validar a
  maquinaria, mirar 3D para o primeiro resultado de geometria não-trivial.
- **Causal vs Euclidiano:** **causal** (com folheação temporal) — é o ingrediente que faz a CDT
  funcionar onde o DT euclidiano falha (branched-polymer). Não negociável; é o "C" de CDT.
- **Movimentos:** conjunto ergódico mínimo de movimentos de Pachner que preserva a folheação.
- **Sem matéria, no início.** Gravidade pura primeiro. Matéria (campos sobre a triangulação) é
  fase posterior, só se Níveis A–B passarem.

---

## 6. Como saberemos que falhamos (a honestidade que define a teoria)

Esta teoria se compromete, desde a fundação, com três mortes possíveis e igualmente válidas:

1. **Morte em A:** sem geometria estável → a classe tipo-CDT não serve nem como gravidade.
2. **Morte em B:** só 1ª ordem, sem limite do contínuo → a parede de escala vale para CDT
   também; o sonho dos números fundamentais morre aqui, de forma limpa e publicável.
3. **Sucesso A+B mas vazio em C:** geometria e contínuo existem, mas nada adimensional cai de
   graça → a teoria é "mais uma gravidade quântica viável", não uma que prevê o inesperado.

**Nenhum desses desfechos é fracasso.** O fracasso seria nos enganarmos sobre qual deles
ocorreu. O charter existe para tornar o auto-engano difícil.

---

## 7. O que esta teoria NÃO é (para o leitor futuro)

- Não é uma extensão de TEIC, nem uma versão de DEV, nem uma releitura de SR.
- Não é uma promessa de derivar G, ℏ ou a₀ (a aresta é externa; ver §3.1).
- Não é nova física até o Nível C entregar algo — até lá, é a re-execução honesta e
  autocontida de um programa conhecido (CDT) com a disciplina de pré-registro do nosso pipeline.

**Próximo documento a escrever:** `GLOSSARIO.md` (termos: simplex, Pachner, Regge, folheação,
dimensão de Hausdorff/espectral, rotação de Wick — definidos do zero) e depois o pré-registro
de **F1**. Nenhum código antes de F1 estar travado por escrito.
