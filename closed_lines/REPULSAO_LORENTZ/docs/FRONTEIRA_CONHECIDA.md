# FRONTEIRA CONHECIDA — o teorema parcial e o que ele deixa aberto

Este é o **mapa de onde esta linha pode ir e onde não pode**. Reproduz o teorema
parcial de `TEIC/docs/campaigns/IMPOSSIBILIDADE_PARCIAL/RESULTADO.md` (2026-06-29) e
é **atualizado a cada resultado** que refine a fronteira.

---

## 1. A tese central (conjectura) e a parte rigorosa

**Tensão fundamental.** Toda regra de conexão definida exclusivamente em termos de
quantidades **invariantes de Lorentz** entre eventos de um *sprinkling de Poisson*
está sujeita a:

- **ou** a regra carece de informação espacial fina para cortar os "atalhos de
  boost" — e então **herda a coordenação divergente do Poisson** (campo-médio
  tipo-Bethe, valência infinita);
- **ou** introduz **dependência de referencial** — e então **viola a invariância
  estatística** que é a única razão pela qual *causal sets* são um substrato
  relativístico legítimo.

A **parte de coordenação** desta tensão é um **teorema** (não acidente empírico),
decorrente da **não-compacidade do grupo de Lorentz**. A tese geral ("nenhum
substrato de ordem causal tem escala emergente") permanece **conjectura**.

## 2. O enunciado rigoroso (parcial)

Seja Φ um *sprinkling* de Poisson de densidade ρ em M^d, e uma regra de conexão que
liga `i ≺ j` com probabilidade que é um funcional **Poincaré-invariante** de Φ.
Então a valência esperada de um evento típico é

> **⟨z⟩ = ρ · Vol(H^{d−1}) · ∫₀^∞ Δτ^{d−1} q(Δτ) dΔτ**

onde `q(Δτ)` é a probabilidade de conexão **marginalizada** (uma função só de Δτ, por
invariância) e `H^{d−1}` é o hiperbolóide unitário (a órbita de Lorentz a Δτ fixo).
Como **Vol(H^{d−1}) = ∞** (grupo de Lorentz não-compacto), **⟨z⟩ = ∞** a menos que
`q ≡ 0` (regime trivialmente esparso).

**Esboço de prova.** Campbell–Mecke (Palm) do Poisson: `⟨z⟩ = ρ ∫_{cone} h(i,x) d^d x`
com `h = E_Φ[1(conectados)]`. Invariância de Poincaré ⇒ `h` depende **apenas** de Δτ
(inclusive para regras de k pontos: a dependência de vizinhança é absorvida na média
`h`). Decompondo `d^d x = Δτ^{d−1} dΔτ dμ_{H^{d−1}}`, o fator hiperbólico
`Vol(H^{d−1})` sai como prefator infinito. ∎(esboço)

**N(i,j) não é exceção.** O nº de eventos no intervalo de Alexandrov tem
`E[N|Δτ] = ρ c_d Δτ^d` (bijeção monotônica) ⇒ é "Δτ disfarçado". Toda contagem
combinatória de par é função de `V ∝ Δτ^d` e cai em `q(Δτ)`.

## 3. As hipóteses (o que falta para fechar a tese inteira)

Rigoroso sob:
- **(i)** O substrato é um *sprinkling de Poisson* em M^d (medida de
  Bombelli–Henson–Sorkin), correspondência discreto-contínuo independente de
  referencial. **← a hipótese de INDEPENDÊNCIA dos eventos.**
- **(ii)** A regra usa **apenas** ordem causal e contagens invariantes (sem
  coordenadas de *embedding*).
- **(iii)** "Campo-médio" ≡ valência esperada divergente (Bethe).

A tese geral permanece conjectura porque: (1) caixa finita troca "∞" por "cresce com
N" (operacionalmente MF, não literalmente ∞); (2) a hipótese (i) **exclui medidas
não-Poisson / dinâmicas** (CSG, CDT), que escapam da barreira-1 — ao custo da
barreira-2; (3) §2 fecha a barreira de **coordenação**; a barreira de **clustering** é
argumentada à parte.

## 4. O que o teorema FECHA

- Regras **pairwise** (e de k pontos) **invariantes de Lorentz** sobre o **Poisson**:
  ⟨z⟩ diverge. **Empiricamente confirmado** por ESCALA_XI e PERCOLACAO_LONGO_ALCANCE.
- O candidato N(i,j) e toda contagem combinatória de par (= Δτ disfarçado).
- ⇒ Não há contraexemplo **dentro da classe par/vizinhança-invariante sobre Poisson**.

## 5. O que o teorema NÃO fecha (as aberturas)

1. **Regras não-*pairwise* sobre medidas NÃO-Poisson.** Palm estreita muito esta
   porta (fecha coordenação até para regras de k pontos **se a medida for o
   sprinkling invariante**). Sobra: regras de configuração sobre uma medida que
   **não** seja o Poisson invariante — p.ex. construída autoconsistentemente por uma
   **dinâmica**. O CSG é o representante já testado (cai na barreira-2), mas o espaço
   não foi varrido. **Abertura mais concreta.**
2. **Dinâmica genuinamente fora-do-equilíbrio para a GEOMETRIA.** O NESS testou
   *drive* paramétrico e morreu; falta um regime de relaxação transiente que **nunca
   atinge estacionariedade** (registrado em [[teoria-cdt-nova]]).

Em ambas, o ingrediente que falta é **explicitamente "além da ordem causal pura de
pares num sprinkling de equilíbrio"** — exatamente o que §2 isola como insuficiente.

---

## 6. Onde ESTA linha se encaixa, e o que ela já refinou

A linha REPULSAO_LORENTZ ataca a **hipótese (i)**: relaxa a **independência** dos
eventos (Poisson → processo repulsivo) **mantendo a invariância em distribuição**.
Como o teorema depende de (i) via Campbell–Mecke, ele **não se aplica diretamente** a
um substrato repulsivo — daí a fresta.

**Refinamento desta linha — campanha `GATILHO_REPULSAO` (2026-06-30):**

> A sub-classe **"medida repulsiva com regra de exclusão de par invariante"** (hard-core
> Matérn II no intervalo `s²`) **cai do mesmo jeito**: ⟨z⟩ diverge em todo α (a
> repulsão não reduz a coordenação) e C4 rastreia Poisson, decaindo com N. Primeiro
> teste **empírico fora da hipótese (i)** — quebrar a independência **não basta**.
>
> **Por quê (e por que estreita a abertura 1):** a região de exclusão invariante é
> uma **banda ao redor do cone de luz** (`V_excl ~ r0²·L`, não `~r0^d`) — a própria
> não-compacidade do cone. A repulsão remove pares perto do cone, mas eles se
> regeneram na densidade retida, e a divergência da órbita de boost sobrevive. A
> exclusão é Lorentz-invariante ⇒ é **cega aos atalhos de boost** (excluir em `|s²|`
> é o análogo, do lado da medida, de "decair em Δτ" do lado da regra). Corolário
> medido: **"repulsão local Lorentz-invariante" é um oximoro** — o mesmo fato que
> força ⟨z⟩=∞.
>
> **Consequência para a abertura 1:** a fresta de "medidas não-Poisson" **continua
> aberta**, mas **não** para medidas repulsivas definidas por **regra de par
> invariante** (esta sub-classe está fechada). O que resta da abertura 1 é
> estritamente **medidas dinâmicas / autoconsistentes não-pairwise** (à la CSG, mas
> com laços de dimensão finita) — não uma repulsão de par sobre Minkowski estático.

---

## 6.bis O mecanismo geral: NÃO-LOCALIDADE FORÇADA POR INVARIÂNCIA — duas confirmações independentes

O que o teorema parcial de §2 chama de "coordenação invariante ⟹ valência infinita" é
um caso de um princípio mais geral, agora apoiado em **duas confirmações
independentes** que atacam o problema por **eixos diferentes** e chegam ao **mesmo
mecanismo**: *qualquer objeto Lorentz-invariante construído sobre Minkowski herda a
não-compacidade do cone, e portanto é não-local — a localidade efetiva finita só pode
ser comprada quebrando a invariância.*

| Confirmação | Eixo atacado | Objeto invariante | Por que é não-local | Sintoma medido |
|---|---|---|---|---|
| **1ª — lado da REGRA** | a **regra de conexão** sobre a medida de Poisson | `p(Δτ)=f(Δτ)` (decai no invariante Δτ) | a órbita de boost a Δτ fixo é o hiperbolóide não-compacto `Vol(H^{d−1})=∞`; a regra conecta ao longo de todo ele | **⟨z⟩ diverge ∀σ** (ESCALA_XI + PERCOLACAO_LONGO_ALCANCE; teorema §2 é o enunciado rigoroso) |
| **2ª — lado da MEDIDA** | a **medida do processo de ponto** (relaxa a independência) | exclusão `\|s²\|<r0²` (hard-core no invariante `s²`) | a região de exclusão invariante é a **banda do cone de luz**, `V_excl~r0²·L`, não uma bola compacta `~r0^d` | **⟨z⟩ diverge ∀α** + C4≈Poisson (GATILHO_REPULSAO, 2026-06-30) |

**Por que isto é uma confirmação genuína, e não a mesma observação duas vezes.** O
teorema parcial (§2) é, por construção, um enunciado sobre **regras de conexão sobre
o sprinkling de Poisson** — ele *assume* a medida (hipótese (i)) e restringe a regra.
A 2ª confirmação ataca exatamente a peça que o teorema *assumia fixa*: troca a
**medida** (Poisson → repulsiva) e deixa a regra na forma mais canônica possível (a
cobertura causal nua). O fato de a não-localidade **reaparecer do outro lado** —
agora como propriedade geométrica da região de exclusão, não como propriedade da
integral de Campbell–Mecke — mostra que o mecanismo **não depende de qual peça é
invariante**: depende apenas de que *alguma* peça Lorentz-invariante seja construída
sobre o cone não-compacto. "Decair em Δτ" (regra) e "excluir em `s²`" (medida) são a
**mesma falha** vista por dois lados.

**Elevação de status.** Antes: "regras de par invariantes sobre Poisson dão MF"
(teorema). Agora: "**invariância de Lorentz manifesta sobre Minkowski ⟹ não-localidade
do objeto construído**", suportado independentemente na regra e na medida. Continua
sendo **conjectura** quanto à tese geral (escala emergente impossível), mas o
*mecanismo* que a sustenta saiu de "propriedade de uma classe de regras" para
"propriedade de qualquer construção invariante sobre o cone" — uma generalização que
torna as aberturas restantes (§5/§7) mais nitidamente as **únicas** saídas: elas são
precisamente as que **não** constroem um objeto invariante fixo sobre Minkowski
estático (medidas dinâmicas autoconsistentes; geometria fora-do-equilíbrio).

## 7. Estado da fronteira (resumo)

| Porta | Status |
|---|---|
| Regra par invariante **sobre Poisson** | **FECHADA** (teorema §2; ESCALA_XI, longo alcance) |
| Regra/correlação de **k-pontos sobre Poisson** | **FECHADA** (Slivnyak–Mecke; `NAO_PAIRWISE_E_NEQ/.../A2_ANALISE.md`, 2026-06-30) |
| **Repulsão de par invariante** (medida não-Poisson, regra de par) | **FECHADA** (GATILHO_REPULSAO, 2026-06-30) |
| Medida **dinâmica/autoconsistente não-pairwise** (CSG, CDT) | **FECHADA empiricamente** (categoria COMBINATÓRIA; falta teorema combinatório — ver §8) |
| Geometria **fora-do-equilíbrio genuíno** (relaxação transiente) | categoria COMBINATÓRIA; **pendência analítica separada** (§8; não executada) |
| **Foliação anisotrópica / intra-fatia** (Hořava–Lifshitz) | **única saída estrutural — mas TROCA a premissa** (quebra Lorentz); §8. Gatilho ARMOU; criticalidade = **classe de reticulado conhecida, sem física nova** (§8) |
| **Substratos PRÉ-CAUSAIS** (causalidade emerge, não é premissa) | **FECHADA por levantamento** (LEVANTAMENTO_PRE_CAUSAL, 2026-06-30; §9) — nenhum candidato real genuíno |
| **Dinâmica de CAMPO sobre o substrato fixo** (transmutação/running, 2.2/2.5) | **FORA do teorema de conectividade (mudo), mas estreitada** (MECANISMOS_DE_ESCALA, 2026-06-30; §10) — realização canônica obstruída pela não-localidade (A2), âncora inserido |

## 8. A síntese das sete mortes: a estrutura é BINÁRIA (fechamento mais forte)

`003-TEORIAS/SINTESE_SETE_MORTES/RESULTADO.md` (2026-06-30, analítico) generaliza as
sete mortes além de "uma tensão". Achado central:

- A morte tem **dois mecanismos distintos**: **BOOST** (não-compacidade do hiperbolóide,
  ⟨z⟩=∞; famílias 1/6/7 + teorema) e **COMBINATÓRIA** (laços do grafo: CSG sub-conectado
  tipo-árvore; CDT 3D/NESS/4D super-conectado Bethe). Um candidato precisa vencer **os
  dois**.
- **Dobradiça (o eixo do tempo):** a única operação que escapa do BOOST — folhear /
  discretizar o eixo tipo-tempo / capar contagem — é exatamente a que **entra** na
  COMBINATÓRIA (evidências: ESCALA_XI cap k-NN → Bethe + quebra Lorentz; CDT foliação
  → z~13 finito-mas-alto; tipo-CDT 2D arma C4≈0.145, somar o tempo lava). Boost e
  combinatória são **o mesmo obstáculo** (conectividade do eixo tipo-tempo) antes/depois
  de folhear.
- **Para a premissa do programa (Lorentz manifesta) o mapa está FECHADO** (teoria de
  grupos: órbita compacta ⟹ fatia espacial ⟹ foliação ⟹ abandona a premissa).
- **Única saída estrutural = foliação anisotrópica (Hořava–Lifshitz / shape dynamics)** —
  distância **intra-fatia** (grupo `SO(d−1)` **compacto**), distinta de tudo testado, mas
  **quebra Lorentz manifesta**, é **parcialmente testada** (tipo-CDT 2D arma / CDT 3D-4D
  morre, colchetando-a) e **sem promessa de escala** na literatura. Gatilho cinemático
  mínimo **desenhado (não executado)** no apêndice do RESULTADO; pende de autorização.
- **Pendência registrada:** a categoria COMBINATÓRIA está fechada **empiricamente**, não
  com força **analítica** (só o BOOST tem teorema). Próximo passo barato = um **teorema
  combinatório** ("cobertura de poset aleatório / triangulação dinâmica não tem dimensão
  de laço finita") **antes** de rodar mais motores (a Parte B / NESS perpétuo fica atrás
  dessa tentativa analítica).

**Desfecho da saída foliada (CRITICALIDADE_GENUINA, 2026-06-30):** o substrato foliado
(Hořava–Lifshitz discreto, **NÃO Lorentz-invariante**) não só armou o gatilho como
**sustenta criticalidade de 2ª ordem genuína** com o ferromagneto O(3) (χ_max~N^0.52,
J_c estável, ξ/L ordem-1, LRO — **não** mean-field). **MAS** a classe de universalidade é
**indistinguível de um reticulado cúbico puro** (controle obrigatório: N^0.59; Δx/σ=0.89)
⇒ **criticalidade de reticulado conhecida (3D-Heisenberg), não assinatura nova de
Hořava–Lifshitz**. Esperado e confirmado: acoplamento só ferromagnético ⇒ sem ponto de
Lifshitz ⇒ λ irrelevante no IR (varredura de λ não rodou, funil). **Conclusão do
programa:** a única saída estrutural da estrutura binária entrega, no melhor caso, a
mecânica estatística de reticulado que já se conhecia — **sem física nova e às custas da
invariância de Lorentz**. Refina (z alto ≠ MF): o foliado tem z≈11.5 e mesmo assim é
crítico-3D, confirmando que o MF das 7 mortes vinha da **não-localidade/coordenação
divergente/tree-Bethe**, não da magnitude de z.

## 9. O fechamento mais amplo: substratos PRÉ-CAUSAIS também não escapam

`003-TEORIAS/LEVANTAMENTO_PRE_CAUSAL/RESULTADO.md` (2026-06-30, **levantamento puro, sem
código**) ataca a categoria que estava, *a priori*, fora do escopo do teorema: princípios
onde a **própria ordem causal emerge** de algo mais primitivo (não há medida-sobre-
espaço-tempo-causal no passo zero ⇒ Campbell–Mecke não tem onde atuar). Seis programas
reais da literatura de gravidade quântica investigados:

| Candidato | Causalidade é... | Veredito |
|---|---|---|
| Causal sets (Sorkin) | AXIOMA | REINTRODUZ (é a hipótese (i)) |
| Energetic Causal Sets (Cortês–Smolin) | PRIMITIVO declarado | REINTRODUZ (crescimento+peso = COMBINATÓRIA) |
| Group Field Theory / tensor models | ausente (Euclid.) ou input-de-grupo (Lorentz.) | NO-GO: geometrogênese **mean-field** na própria literatura |
| LQG / spin foams | NÃO derivada (**problema do tempo**) | REINTRODUZ / no-go do tempo |
| Causal spin foams (Markopoulou–Smolin) | INPUT (orientação micro-local) | REINTRODUZ |
| Holografia / emaranhamento (AdS/CFT, MERA, ER=EPR) | importada da **fronteira CFT** + fundo AdS | REINTRODUZ + NO-GOs de reconstrução |
| Modelo de Wolfram (hipergrafo + invar. causal) | **emerge** de fato, mas → grafo causal = **causal set** | REINTRODUZ no nível emergente; Lorentz repousa em invar. causal **assumida** |

**Veredito (§4 do charter): NENHUM CANDIDATO GENUÍNO.** Padrão único — todo programa, ao ser
destrinchado, ou (1) reintroduz a ordem causal/medida que o teorema cobre, ou (2) é
genuinamente pré-geométrico mas tem **obstrução documentada** (GFT mean-field; problema do
tempo; no-gos holográficos). Confirmação **externa e independente** do mecanismo binário:
mesmo nos programas pré-geométricos de fronteira, a tensão reaparece como "mean-field na
geometrogênese" e como "non-locality dos causal sets". **A busca por física nova via
modificação de substrato — causal OU pré-causal — está esgotada nos caminhos conhecidos da
literatura.** Ressalva honesta: ausência de no-go formal único p/ Wolfram = incerteza
genuína, não abertura (a obstrução "grafo causal = causal set" é argumento estrutural, não
teorema). Único passo futuro honesto = provar que o grafo causal emergente do Wolfram herda
a não-compacidade — atrás da pendência combinatória de `SINTESE_SETE_MORTES` na fila.

## 10. O gap conectividade↔dinâmica-de-campo: os mecanismos de escala além da criticalidade

`003-TEORIAS/MECANISMOS_DE_ESCALA/RESULTADO.md` (2026-06-30, **analítico, sem código**)
mapeia **todos** os mecanismos conhecidos de geração de escala (não só a criticalidade
térmica que ESCALA_XI testou) e classifica cada um contra o teorema binário. Achado:

- **O teorema cobre mais do que se sabia.** Ele fecha tudo que é **propriedade de
  conectividade do grafo** (2.1 criticalidade térmica = MF; dimensão espectral = sem
  running). E os mecanismos não-de-conectividade ou (i) **reintroduzem escala inserida**
  (2.4 sóliton via Derrick/termo de Skyrme externo; 2.6 caixa/Casimir/KK; `ℏ`; `a₀~cH₀`),
  ou (ii) **recaem em 2.2** (2.3 dilaton, 2.5 anomalia de traço), ou (iii) são
  **indisponíveis** porque a discretização `ρ` **já quebra explicitamente a dilatação**
  (2.3; o guard TEIC `dilation banned everywhere` reflete isto). **Fechamento mais amplo.**
- **Resta UM gap lógico genuíno:** o teorema de conectividade (⟨z⟩, C4) é **mudo** sobre
  **transmutação dimensional via running de acoplamento** (2.2/2.5, à la Λ_QCD /
  Coleman–Weinberg) — isso é **dinâmica de campo sobre o substrato FIXO**, não
  conectividade.
- **Mas o gap NÃO é porta aberta**, por três razões já no programa: **(a)** a realização
  canônica de 2.2 (confinamento via lei-de-área de Wilson) é **sólida só no reticulado
  cúbico** e **NÃO-MENSURÁVEL no causet de Poisson** (`CONFINAMENTO_A2`, FRONTEIRA) — pela
  **mesma** não-localidade que dá ⟨z⟩=∞; o princípio de não-localidade (§6.bis) atravessa o
  gap e re-fecha parcialmente a porta no chão invariante. **(b)** Onde 2.2 funciona
  (foliado/cúbico) Lorentz já está quebrada = rota **Hořava–Lifshitz** já mapeada (§8).
  **(c)** Transmutação dá só uma **razão** `Λ/ρ` emergente; o âncora dimensional fica
  **inserido** (`ρ`), como em **toda** TQC (a própria QCD).
- **Fresta exata que sobra (não-testada, registrada):** um acoplamento marginal sobre o
  d'Alembertiano causal fixo cujo running se manifeste num observável **não obstruído pela
  não-localidade** (não um loop de Wilson), com razão transmutada genuína. Estrutura mínima
  do teste em `MECANISMOS_DE_ESCALA/RESULTADO.md` §4; **pende de autorização**.

---

> **Atualizar este arquivo** sempre que uma campanha mover qualquer linha da tabela §7.
