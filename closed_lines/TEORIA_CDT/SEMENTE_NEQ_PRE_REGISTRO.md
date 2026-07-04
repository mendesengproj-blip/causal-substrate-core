# PRÉ-REGISTRO — Semente FORA-DO-EQUILÍBRIO (a única classe que o MEMORIA_DIAGNOSTICO deixou viva)

> **Estado: PRÉ-REGISTRADO, NÃO EXECUTADO.** Data: 2026-06-29. Congelado ANTES de qualquer código
> que o teste. Este documento é a **consequência direta** do veredito ESTRUTURAL de
> `MEMORIA_DIAGNOSTICO/SYNTHESIS.md`: a morte de D2 em FS-3D (`F1b_acao/FS_SYNTHESIS.md`) **não** é
> escolha do kernel exponencial — é o **equilíbrio em si** (mixing/ergodicidade torna o estado
> estacionário cego à história, para qualquer kernel de extensão finita). Logo:
>
> > **A busca por uma semente-de-EQUILÍBRIO está estruturalmente FECHADA.** A única classe de
> > semente que ainda pode sobreviver a D2 é a **explicitamente fora-do-equilíbrio**: uma dinâmica
> > de informação que **nunca atinge estacionariedade** no horizonte físico. Este pré-registro
> > define essa semente, seu observável bem-posto, e — honestamente — por que ela provavelmente
> > também morre, mas por um motivo **diferente e informativo**.
>
> **Substitui** o eixo de desenho: não é mais "qual kernel de memória", é **"equilíbrio vs
> não-equilíbrio"**. Nada aqui é "uma escala emergiu" (aresta `[External]` por F1b; anti-circ §3 do
> charter mantida). Não construir F2-com-esta-semente antes deste pré-registro dar observável genuíno.

---

## 0. A pergunta (afiada pelo MEMORIA_DIAGNOSTICO)

> Existe uma realização **fora-do-equilíbrio** da semente ("a informação SOURCE o crescimento")
> que (D1) muda a geometria, (D2-NEQ) carrega uma assinatura de **envelhecimento** (memória de
> não-equilíbrio) irreproduzível por um controle estacionário, **E** (D3) **deixa a geometria
> utilizável como fundo** (d_H→~3, fase estendida, não branched-polymer)?

Se sim, há teoria nova. Se não, sabe-se **qual das três mortes** ocorreu — e isso fecha (ou redobra)
a linha da semente com a mesma honestidade do resto do programa.

## 1. O mecanismo (especificado o suficiente para virar equação)

Mesma espinha de FS-3D (campo φ ≥ 0 nos vértices; source do (2,6) por `exp(γ(φ_local − φ̄))`;
depósito Δφ no vértice novo + fontes) — **muda APENAS o transporte**, que em FS-3D era relaxação de
escala FIXA (`φ ← (1−κ)φ + κ⟨φ_viz⟩`, κ constante ⇒ equilibra ⇒ lava). A semente fora-do-equilíbrio
substitui a escala fixa por uma que **nunca para de crescer**:

**PRIMÁRIA — transporte com ENVELHECIMENTO (glassy/aging):**
> κ(s) = κ₀ / (1 + s / s_age),  onde s = idade do run (nº de sweeps desde o início).
A taxa de esquecimento κ(s) → 0 com a idade ⇒ depósitos antigos são esquecidos **cada vez mais
devagar** ⇒ a escala de memória do campo **cresce sem limite** com a idade ⇒ φ **nunca atinge medida
estacionária** no horizonte. `κ₀, s_age` são `[External]` (declarados, não emergem). É a realização
"aging genuíno" nomeada na §Consequência do `MEMORIA_DIAGNOSTICO`. **Limite-controle embutido:**
s_age → 0 recupera κ→0 (congela) e s_age → ∞ recupera FS-3D (κ fixo, equilibra, lava) — os dois
nulos contra os quais o aging é medido.

**ALTERNATIVA (registrada, secundária) — NESS dirigido (fonte-sorvedouro):** corrente permanente de
informação (injeta φ em eventos de alta-curvatura, remove em baixa) ⇒ estado estacionário de
não-equilíbrio com corrente. Secundária porque um NESS **ainda é estacionário** (a geometria pode
equilibrar em torno dele, reduzindo o risco D3) MAS a "memória" vira **corrente**, que D2-NEQ
(aging, abaixo) **não** detecta — exigiria um observável de **produção de entropia / corrente de
probabilidade** distinto. Só se a PRIMÁRIA falhar por D3 (geometria destruída), a ALTERNATIVA passa
a valer (troca risco-de-geometria por observável-de-corrente).

## 2. O observável BEM-POSTO (a lição do MEMORIA_DIAGNOSTICO incorporada)

O `MEMORIA_DIAGNOSTICO` provou que o **C_mem com janela curta (max_tau=15)** dá **falso-positivo** de
memória (o bump de curto-lag de qualquer kernel lento). **Este pré-registro NÃO usa C_mem-de-janela-
fixa como discriminante.** O observável de não-equilíbrio correto é a **correlação de dois tempos
com dependência explícita do tempo de espera** (a definição-padrão de envelhecimento):

> **C(t_w+τ, t_w)** = correlação do padrão de crescimento por fatia entre a idade t_w e a idade
> t_w+τ. Num processo **estacionário** (qualquer semente de equilíbrio, o controle markoviano, um
> NESS) C(t_w+τ, t_w) = C(τ) — **independe de t_w** (invariância de translação temporal). Em
> **envelhecimento**, C depende **explicitamente de t_w** (tipicamente colapsa numa função de
> τ/t_w). **A assinatura = dependência de t_w**, medida em ≥2 tempos de espera bem separados
> (ex.: t_w ∈ {N_sweeps/4, N_sweeps}), com a **disciplina de janela larga** (integral até capturar
> a decaída completa — nunca um max_tau fixo curto).

## 3. Os critérios de morte EMPILHADOS (pré-registrados, sem ajuste depois)

A semente só sobrevive se passar **os três**.

### D1 — vs CDT cega (informação muda a geometria?)
Inalterado de FS-3D. Já se sabe que **passa** (qualquer peso muda a geometria; FS-3D deu +500σ).
Mantido só como gate de sanidade, não carrega evidência pró-semente.

### D2-NEQ — vs controle ESTACIONÁRIO (há envelhecimento genuíno?)
> A correlação de dois tempos C(t_w+τ, t_w) **depende de t_w** (curvas de t_w distintos NÃO
> colapsam numa C(τ) única) acima do que o **controle estacionário** de mesma intensidade produz —
> medido com janela larga, robusto a k₀. **Controle obrigatório embutido (a lição do FS-3D/2D):**
> um peso markoviano/estacionário de mesma intensidade de modulação **deve** dar curvas de t_w
> **colapsando** (t_w-independentes). Se a semente também colapsa ⇒ **MORTE D2-NEQ** (sem
> envelhecimento; a "memória" lava como no equilíbrio). 3º controle (anti-trivialidade): o
> envelhecimento **não** pode ser só o relógio externo κ(s) impondo a escala — comparar com um
> κ(s) **idêntico mas SEM o campo φ informacional** (aging geométrico cego); se este reproduzir a
> assinatura, então "informação" é de novo só nome para um agendamento `[External]` ⇒ **MORTE
> D2-NEQ por trivialidade** (o mesmo destino estrutural da semente de equilíbrio, recolocado).

### D3 — NOVO: a geometria SOBREVIVE como fundo? (a tensão central, morte mais provável)
> Ir fora-do-equilíbrio na informação **não pode destruir a geometria**. A geometria precisa
> permanecer um **fundo utilizável**: d_H ainda corre rumo a ~3, a fase estendida não colapsa em
> branched-polymer/degenerada, o volume permanece controlável (k₃ adaptativo ainda trava ⟨N₃⟩).
> **MORTE D3:** se o setor informacional fora-do-equilíbrio arrasta a geometria para fora da fase
> estendida (d_H degenera, maxcoord explode, sem quasi-estacionariedade geométrica), a semente é
> **incompatível com F2** (que exige fundo estável p/ medir geometria emergente) — morre por D3
> **mesmo que D2-NEQ passe**. Esta é a tensão que o equilíbrio "de graça" resolvia e o
> não-equilíbrio reabre.

**Sucesso = D1 ∧ D2-NEQ ∧ D3:** geometria muda (D1), exibe envelhecimento genuíno e não-trivial
(D2-NEQ), **e** continua um fundo geométrico sadio (D3). Só então "informação SOURCE o crescimento"
é física nova **e** compatível com o resto do programa.

## 4. Anti-circularidade (charter §3, mantida)
1. **κ₀, s_age (e qualquer escala do drive) são `[External]`.** A semente não afirma que o relógio
   de envelhecimento emerge. Teste é **estrutural** (a classe da dinâmica muda?), nunca "número emergiu".
2. **Nenhuma escala emerge.** Se o aging gera um tempo, ele vem de s_age `[External]` — declarar.
3. **Nada de TEIC/DEV/SR.** φ re-derivado aqui; "informação" = o campo de §1, ponto.
4. **Pré-registro antes de medir; sem annealing.** D1/D2-NEQ/D3 e os observáveis estão congelados
   aqui. A disciplina de **janela larga** (não C_mem-curto) é parte do congelamento.

## 5. Prior honesto (declarar, não pender) — as TRÊS mortes prováveis

- **Morte 1 (a mais provável): a GEOMETRIA equilibra e arrasta φ.** O 1-esqueleto do CDT 3D tem
  coordenação alta (z~13–15, visto em `TEIC/CDT_TEIC_FERRO`) ⇒ o grafo **mistura rápido**. Mesmo com
  κ(s)→0, a difusão de φ no grafo que mistura rápido pode equilibrar φ apesar do agendamento de
  esquecimento lento — a mistura **geométrica** vence o envelhecimento **informacional**, e D2-NEQ
  colapsa (curvas de t_w juntam). Seria o mesmo mecanismo estrutural do MEMORIA_DIAGNOSTICO, agora
  imposto pela geometria, não pelo kernel.
- **Morte 2: o aging sobrevive MAS destrói a geometria (D3).** Um φ que nunca relaxa biasa o
  crescimento de forma cada vez mais inomogênea ⇒ filamenta a geometria (d_H→1, branched-polymer) ⇒
  sem fundo ⇒ incompatível com F2. Trocaria-se "memória que lava" por "geometria que quebra".
- **Morte 3 (trivialidade): o aging é só o relógio `[External]` κ(s).** Se o controle "κ(s) sem φ"
  (D2-NEQ, 3º controle) reproduz a assinatura, "informação" é de novo nome para um agendamento
  imposto — o mesmo veredito que matou a semente de equilíbrio, recolocado um nível acima.
- **Resultado mais provável declarado de antemão:** **Morte 1** (a geometria de alta-coordenação
  equilibra φ apesar do aging). Isso **não é fracasso** — seria a confirmação de que o substrato CDT
  específico (z alto, mistura rápida) fecha **também** a porta do não-equilíbrio, tornando a morte
  da semente **robusta a equilíbrio E não-equilíbrio**. O fracasso seria não saber qual morte ocorreu.

## 6. Estrutura de FUNIL (mesma disciplina dos gatilhos; obrigatória)

- **NÍVEL 0 (barato, sem CDT) — primeiro:** estender o toy de `MEMORIA_DIAGNOSTICO/nivel0_toy.py`
  com o kernel de envelhecimento (κ(s)→0) e medir a **correlação de dois tempos C(t_w+τ, t_w)** em
  ≥2 tempos de espera, com janela larga. **Pergunta de armação:** o aging produz t_w-dependência
  genuína que um processo estacionário (controle) **não** consegue forjar, e que **não** é só o
  agendamento κ(s) (3º controle, sem o campo)? Critério: t_w-dependência > 3σ acima do controle
  estacionário **E** acima do controle κ(s)-sem-campo. Só se **armar**, vai ao Nível 1.
- **NÍVEL 1 (caro, motor FS-3D) — condicional:** porta o kernel de aging para a semente em
  `fs_seed3d.py`/`fs_run3d.py`, roda D1 + D2-NEQ + **D3** (gate de geometria) em k₀=1,3 com os
  controles embutidos (estacionário + κ(s)-sem-campo). Critério binário, sem ajuste posterior.
- **Se o Nível 0 não armar** (aging não sobrevive nem no toy), **não rodar o Nível 1** — registrar
  que **nem o não-equilíbrio salva a semente** e que a linha da semente está **definitivamente
  fechada** (equilíbrio E não-equilíbrio mortos), o que é um veredito de programa, não um fracasso.

## 7. Entregáveis (quando/se executar)
`fs_neq_toy.py` (Nível 0: aging + C(t_w+τ,t_w), reusa o toy e `c_mem` verbatim),
`fs_neq_seed.py`/`fs_neq_run.py` (Nível 1: kernel aging no motor FS-3D, D1/D2-NEQ/D3),
`SYNTHESIS.md` (veredito das três mortes), dados. **Bloqueio:** Nível 1 só após Nível 0 armar.

**Resumo de uma linha:** o MEMORIA_DIAGNOSTICO fechou a semente-de-equilíbrio por estrutura
(mixing), deixando viva só a semente **fora-do-equilíbrio**; este pré-registro a define
(transporte com envelhecimento κ(s)→0), dá-lhe um observável bem-posto (**correlação de dois tempos
t_w-dependente**, não o C_mem-curto que dá falso-positivo) e **três** mortes empilhadas — D1
(geometria muda), D2-NEQ (aging genuíno e não-trivial vs controles estacionário e κ(s)-sem-campo) e
**D3 (a geometria sobrevive como fundo)** — com o prior honesto de que a morte mais provável é a
**geometria de alta-coordenação do CDT equilibrar o campo apesar do envelhecimento**, o que
tornaria a morte da semente robusta a equilíbrio **e** não-equilíbrio; tudo em funil (toy barato
arma o motor caro), aresta `[External]`, nada "escala emergiu".
