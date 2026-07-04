# Mecanismos de geração de escala vs. o teorema binário — o que o teorema cobre, e o gap real

**Data:** 2026-06-30 · **Natureza:** documento **inteiramente analítico** (mapeamento da
física conhecida + verificação cruzada com o teorema parcial; **nenhum código, nenhum
experimento**). · **Pasta:** `003-TEORIAS/MECANISMOS_DE_ESCALA/`.

> **Disciplina declarada antes de começar.** O objetivo NÃO é "achar um jeito de a TEIC
> dar escala". É mapear honestamente os mecanismos conhecidos de geração de escala e, para
> cada um, decidir se está **coberto** pelo teorema binário (logo fechado), **fora do
> escopo** (logo incerteza genuína, não promessa), ou **reintroduz uma escala inserida**
> (logo não-emergente). Se o resultado for "o teorema cobre tudo que importa", isso é um
> resultado mais forte que o atual e deve ser registrado como tal.

---

## 1. O que o teorema binário prova, e onde ele vive (a verificação cruzada da Seção 5, primeiro)

Faço a verificação cruzada **antes** do mapeamento, porque ela define o eixo de
classificação de tudo que vem depois.

Lendo `IMPOSSIBILIDADE_PARCIAL/RESULTADO.md` (§3.1) e `SINTESE_SETE_MORTES/RESULTADO.md`
(§1–§2), o teorema binário é, com precisão, um enunciado sobre **duas quantidades de
equilíbrio estatístico da CONECTIVIDADE do grafo de substrato**:

- **⟨z⟩ (coordenação / valência)** — barreira BOOST. Rigorosamente: para regra de conexão
  Poincaré-invariante de par/k-pontos sobre o *sprinkling* de Poisson,
  `⟨z⟩ = ρ·Vol(H^{d−1})·∫Δτ^{d−1}q(Δτ)dΔτ = ∞`, por não-compacidade do hiperbolóide de
  boost (Campbell–Mecke + Slivnyak).
- **C4 (clustering / estrutura de laços)** — barreira COMBINATÓRIA. Argumentada
  empiricamente (CSG tipo-árvore; CDT 3D/4D Bethe): abandonar a medida invariante para
  escapar de ⟨z⟩=∞ destrói os laços de dimensão finita.

**O domínio do teorema é, portanto, a geração/regra do grafo de substrato e a classe de
universalidade estatística que esse grafo pode hospedar.** Ele decide se a conectividade
do chão admite um ponto crítico de 2ª ordem com ξ divergente (mecanismo 2.1, abaixo).

**Onde o teorema é MUDO.** O teorema NÃO faz nenhuma afirmação sobre a **dinâmica de um
campo quântico que se propaga sobre o substrato JÁ FIXO**. Especificamente, ele é mudo
sobre como um acoplamento efetivo depende da escala de sonda (running), sobre o traço do
tensor de energia-momento (anomalia de escala), e sobre setores topológicos de
configurações de campo. Essas são propriedades de **TQC-sobre-substrato**, governadas
pela função beta do campo e pelo espectro do d'Alembertiano causal — **não** por ⟨z⟩ ou
C4. Há, portanto, um **gap lógico genuíno** entre o que o teorema cobre (conectividade do
grafo) e onde vivem os mecanismos 2.2/2.5 (dinâmica de campo sobre conectividade fixa).

**Ressalva que estreita o gap — o princípio de não-localidade generaliza o teorema.** A
`FRONTEIRA_CONHECIDA.md` §6.bis já elevou o teorema de "regras de par dão MF" para um
princípio mais amplo: *qualquer objeto Lorentz-invariante construído sobre Minkowski herda
a não-compacidade do cone e é não-local*. Esse princípio **alcança** a dinâmica de campo —
e é exatamente por isso que a campanha `CONFINAMENTO_A2` encontrou uma **obstrução real** à
realização padrão de 2.2 no substrato invariante (ver §2.2 abaixo). O gap lógico é real,
mas o princípio de não-localidade o atravessa parcialmente.

---

## 2. Mapeamento — os mecanismos, com as três respostas

Para cada mecanismo: **(R1)** gera escala genuína ou transfere de input externo? **(R2)**
coberto pelo teorema binário? **(R3)** se fora do escopo, atuaria sobre o substrato CST
fixo via ingrediente adicional?

### 2.1 — Transmutação via criticalidade térmica (ξ divergente) · *linha-base, o já testado*

ξ diverge num ponto crítico de 2ª ordem; transmutação manufatura uma escala via o
*running* perto do ponto fixo (Wilson–Fisher). Fonte: Wilson & Kogut 1974 (RG); a campanha
`ESCALA_XI` é a instância TEIC.

- **R1 — genuína (se ocorresse).** ξ→∞ não é inserido. (Mas não ocorre — ver R2.)
- **R2 — COBERTO E FECHADO.** É exatamente o domínio do teorema: exige ponto crítico
  não-MF na conectividade do grafo, o que exige laços de dimensão finita + coordenação
  finita = as duas barreiras. ESCALA_XI mediu MF (χ_max∝N^≲0.5, sem pico em J_c).
- **R3 — n/a** (fechado). **Linha-base de comparação.**

### 2.2 — Transmutação dimensional via *running* de acoplamento SEM criticalidade térmica · *o candidato*

O mecanismo de Λ_QCD e de Coleman–Weinberg: uma teoria classicamente sem escala (acoplamento
adimensional `g`) adquire uma escala pelo fluxo de RG de `g` até um polo / acoplamento forte,
`Λ = μ·exp(−1/(b₀g²(μ)))`, **sem transição de fase termodinâmica**. Fontes reais:
Coleman & Weinberg 1973 (*Phys. Rev. D* 7, 1888); 't Hooft 1971–73 e Gross–Wilczek /
Politzer 1973 (liberdade assintótica, β<0); na rede, σa²(β) ∝ exp(−1/(2b₀β)) é o enunciado
operacional (Creutz, *Quarks, Gluons and Lattices* 1983).

- **R1 — emergência PARCIAL (genuína no que importa, mas anchored).** O conteúdo
  **adimensional** — a existência de uma escala de confinamento, o **hierarquia/razão**
  `Λ/μ_UV` — é genuinamente emergente de `g` adimensional, **não inserido**. O **âncora
  dimensional** (a escala UV, aqui a discretização `ρ^{−1/d}`) é inserido. *Mas isto é
  verdade de TODA TQC*, inclusive da QCD do mundo real (Λ_QCD em GeV exige um input
  dimensional). Logo "âncora inserido" não é um defeito específico da TEIC; é a natureza da
  transmutação. O teste anti-circularidade do programa (escala em unidades de rede =
  "scale non-derived") **registra exatamente isto** — sempre foi a razão dada, e ela é a
  razão correta.
- **R2 — NÃO COBERTO pelo teorema de conectividade.** Running de `g` é uma propriedade da
  função beta de um campo sobre o d'Alembertiano causal fixo; não é uma afirmação sobre ⟨z⟩
  ou C4. **O teorema é logicamente mudo.** Este é o gap da §1.
- **R3 — atuaria sobre o substrato fixo, MAS a realização padrão está OBSTRUÍDA no chão
  invariante.** Aqui o resultado é mais interessante (e mais honesto) do que "porta aberta":
  - A TEIC **já tem** uma instância de 2.2 — o setor SU(3) (`FL1`, `CONFINAMENTO_A2`) tem
    confinamento com `σ(β)` decrescente na direção da liberdade assintótica. **Mas:** isso é
    **SÓLIDO só no reticulado cúbico de controle** (8⁴ regular). **No substrato causal de
    Poisson** (o que o teorema cobre, Lorentz-invariante) a *string tension* é
    **NÃO-MENSURÁVEL** — só há plaquetas-diamante de área 1, zero retângulos R×T
    controlados, holonomia de patch sem palavra-de-bordo limpa (`CONFINAMENTO_A2`,
    veredito FRONTEIRA). A obstrução é a **mesma não-localidade** que dá ⟨z⟩=∞.
  - **⟹** o teorema de *conectividade* é mudo sobre 2.2, mas o **princípio de
    não-localidade** que o generaliza (§1, FRONTEIRA §6.bis) **re-fecha parcialmente** a
    realização canônica de 2.2 (lei-de-área de Wilson) no substrato invariante.
  - Onde 2.2 **funciona** (reticulado cúbico/foliado) **Lorentz já está quebrada** e uma
    escala de rede/foliação é importada — isto é a rota **Hořava–Lifshitz** já mapeada em
    `SINTESE_SETE_MORTES` (não é uma porta nova).
  - **A fresta genuinamente não-testada que sobra:** um acoplamento marginal cujo *running*
    se manifeste num observável **não obstruído pela não-localidade** (i.e., não uma
    lei-de-área de Wilson) sobre o Poisson fixo, com razão transmutada genuinamente
    emergente. Se tal observável existe, com β≠0 no d'Alembertiano causal, é **indeterminado**.

### 2.3 — Quebra espontânea de simetria de dilatação (dilaton)

Goldstone da dilatação quebrada → escala `f` (VEV do dilaton). A TEIC já faz SSB de O(3)
(ferromagneto de vácuo, Goldstone = fóton). Fonte: Salam–Strathdee 1969; Coleman 1985 (dilaton
como pseudo-Goldstone); ligação a 2.2 via Coleman–Weinberg.

- **R1 — NÃO gera escala sozinho (flat direction) ⟹ inserido OU reduz a 2.2.** SSB de
  simetria de escala **exata** tem potencial `V∝φ⁴` plano: `f` é direção plana, **degenerada
  classicamente** (todo `f` é igual). Só o potencial efetivo quântico (Coleman–Weinberg) fixa
  `f` — e isso É a anomalia/running (2.2/2.5). SSB clássico puro → `f` inserido.
- **R2 — NÃO coberto (simetria diferente).** O teorema é sobre Lorentz/conectividade, não
  dilatação. Mudo.
- **R3 — INDISPONÍVEL no substrato fixo, por um fato estrutural diferente.** O substrato CST
  **já quebra explicitamente a dilatação**: a densidade de *sprinkling* `ρ` (a escala de
  discretização) é uma escala explícita. **Não há simetria de escala exata para quebrar
  espontaneamente** — `ρ` é a quebra explícita. (O próprio guard da TEIC **proíbe dilatação
  em todo lugar** — `dilation still banned everywhere` — refletindo este fato no código.)
  ⟹ a rota do dilaton **reintroduz a escala inserida `ρ`**, ou recai em 2.2. Fechado por
  quebra explícita, não pelo teorema binário.

### 2.4 — Mecanismos topológicos / não-térmicos (sólitons, instantons, winding)

O Skyrmion da TEIC tem tamanho; instantons têm tamanho `ρ_inst`. Fonte: Derrick 1964 (teorema
de escala); Skyrme 1962; 't Hooft 1976 (instantons).

- **R1 — INSERIDO (Derrick) ou herdado de 2.2.** Por **Derrick**, uma teoria invariante de
  escala não tem sóliton estável (colapsa/expande); estabilizar exige um termo dimensional
  inserido — na TEIC, o termo de Skyrme `e_sk` **externo** (já registrado como inserção). O
  tamanho do instanton é um **módulo** (direção plana) integrado; só o running (2.2) regula a
  integral. ⟹ topologia não gera escala autônoma.
- **R2 — NÃO coberto (topologia ≠ ⟨z⟩/C4).** Mudo.
- **R3 — atuaria, mas só transferindo o termo dimensional inserido (Skyrme) ou a escala de
  2.2.** Não é emergência nova. Confirmado pelo programa (`FL1` Fase C/D: tamanho do
  Skyrmion via `e_sk` externo).

### 2.5 — Anomalia de escala / anomalia quântica

Invariância de escala clássica quebrada na quantização: `⟨T^μ_μ⟩ = (β(g)/2g)·G² ≠ 0`. Fonte:
Coleman–Jackiw 1971; Crewther 1972. **É a raiz de 2.2 e de 2.3-genuíno** (o running É a
anomalia de traço integrada).

- **R1 — genuína, MAS = 2.2 operacionalmente.** A anomalia faz a escala aparecer no nível
  quântico. No mundo real é exatamente o que dá Λ_QCD.
- **R2 — NÃO coberto (traço de T^μν ≠ conectividade).** Mudo — mesmo gap de 2.2.
- **R3 — no substrato CST, a anomalia se manifesta como a dependência em `ρ` (discretização)
  dos acoplamentos efetivos** = exatamente o running de 2.2. **Colapsa em 2.2**: mesma fresta,
  mesma obstrução de não-localidade na realização canônica, mesmo âncora inserido `ρ`.

### 2.6 — Condições de contorno globais / topologia do espaço-tempo (Casimir, compactificação)

Escala do tamanho/topologia global. Fonte: Casimir 1948; Kaluza–Klein.

- **R1 — INSERIDO por construção.** Tamanho de caixa `L`, raio de compactificação `R`, são
  externos — exatamente como `ρ` e `L` sempre foram no programa. Casimir `∝1/L⁴`: `L` inserido.
- **R2 — o teorema USA `L` como regulador IR inserido** (a caixa finita troca ⟨z⟩=∞ por
  "cresce com N"). Escalas de contorno são a inserção, não emergência.
- **R3 — não aplicável** (é a definição de escala inserida).

### 2.7 — Outros mecanismos revistos (todos recaem)

- **Ponto fixo + operador relevante / *walking* / escala de Miransky / BKT (singularidade
  essencial):** versão "fluxo de operador" de 2.1/2.2. A campanha `ESCALA_XI` procurou a
  singularidade essencial **na conectividade** e achou MF — mas a versão "fluxo de
  acoplamento de campo" é 2.2 (não coberta). Fonte: Miransky 1985; Kosterlitz–Thouless 1973.
- **Dimensão espectral correndo (CDT 4→2):** propriedade de **conectividade do substrato** →
  coberta/testada. `C5-SPECTRAL-DIMENSION` = MORTE (platô único `D_s=d`, sem running genuíno).
- **`ℏ` / escalas quânticas (Compton, de Broglie):** `ℏ` é inserido (`C5-3`: "ℏ stays
  external"). Inserido.
- **Escala cosmológica IR `a₀~cH₀` (DEV):** explicitamente externa (condição de contorno IR).
  Inserida — e o achado central do DEV é que importá-la é a **opção honesta**.
- **Energias de ligação (Rydberg, etc.):** reduzem às escalas dos constituintes (massas, `α`,
  `ℏ`) — inseridas ou de 2.2.

---

## 3. Tabela-resumo

| # | Mecanismo | R1: genuíno? | R2: coberto pelo teorema? | R3: sobre substrato fixo? | Classificação |
|---|---|---|---|---|---|
| 2.1 | Criticalidade térmica (ξ→∞) | sim, se ocorresse | **SIM — fechado** (é o domínio) | n/a | **FECHADO** (linha-base, ESCALA_XI=MF) |
| 2.2 | **Transmutação via running (Λ_QCD)** | **parcial: razão emergente, âncora inserido** | **NÃO (mudo)** — gap conectividade↔dinâmica | sim, mas realização canônica OBSTRUÍDA (não-localidade, A2) | **FORA DO ESCOPO — fresta estreita, anchored** |
| 2.3 | SSB de dilatação (dilaton) | não sozinho (flat dir.) → inserido/2.2 | NÃO (simetria diferente) | **indisponível: `ρ` já quebra dilatação explicitamente** | FECHADO por quebra explícita |
| 2.4 | Topológico (sóliton/instanton) | inserido (Derrick) ou herda 2.2 | NÃO (topologia) | só transfere termo inserido (Skyrme) | INSERIDO |
| 2.5 | Anomalia de escala | genuína, mas = 2.2 | NÃO (mudo) | colapsa em 2.2 (dependência em `ρ`) | = 2.2 |
| 2.6 | Contorno global (Casimir/KK) | inserido por construção | teorema usa `L` como regulador | n/a (é a inserção) | INSERIDO |
| 2.7 | fixo+relevante / `ℏ` / `a₀` / ligação | inserido ou = 2.1/2.2 | conectividade=coberto; campo=2.2 | recai | recai |

---

## 4. Veredito (critério pré-registrado da Seção 4 do charter)

**MECANISMO FORA DO ESCOPO IDENTIFICADO — mas com forte estreitamento, NÃO uma porta
aberta.** Concretamente:

1. **O teorema binário cobre mais do que "criticalidade térmica".** Cobre todo mecanismo que
   seja uma **propriedade de conectividade do grafo de substrato** (2.1 criticalidade; a
   dimensão espectral; e — via o princípio de não-localidade generalizado — re-fecha a
   realização canônica de 2.2). E os mecanismos que **não** são de conectividade ou (i)
   reintroduzem uma escala inserida (2.4 topológico via Derrick/Skyrme; 2.6 contorno; `ℏ`;
   `a₀`), ou (ii) recaem em 2.2 (2.3 dilaton, 2.5 anomalia), ou (iii) são **indisponíveis** no
   substrato porque a discretização `ρ` já quebra a simetria relevante (2.3). **Este é um
   fechamento mais amplo do que o que se sabia.**

2. **Resta UM gap lógico genuíno, e ele é nítido:** o teorema de **conectividade** (⟨z⟩, C4)
   é **logicamente mudo** sobre **transmutação dimensional via running de acoplamento de um
   campo** (2.2/2.5) — fenômeno de TQC-sobre-substrato, não de conectividade. Esta é a
   direção não-coberta.

3. **Mas o gap NÃO é uma promessa**, por três razões honestas, todas já presentes no
   programa:
   - **(a) Obstrução por não-localidade.** A realização canônica de 2.2 (confinamento via
     lei-de-área de Wilson) é **SÓLIDA só no reticulado cúbico** (Lorentz quebrada) e
     **NÃO-MENSURÁVEL no substrato causal de Poisson** (`CONFINAMENTO_A2`, FRONTEIRA) — pela
     **mesma** não-localidade que dá ⟨z⟩=∞. O princípio de não-localidade (FRONTEIRA §6.bis)
     atravessa o gap e re-fecha parcialmente a porta no chão invariante.
   - **(b) Rota foliada = já mapeada.** Onde 2.2 funciona (reticulado/foliado), Lorentz já
     está quebrada — é a rota **Hořava–Lifshitz** de `SINTESE_SETE_MORTES`, conhecida e sem
     promessa de escala.
   - **(c) Emergência só de razão, âncora sempre inserido.** Transmutação dá uma
     **hierarquia/razão** `Λ/ρ^{−1/d}` adimensional emergente; a escala absoluta exige um
     âncora dimensional (`ρ`), como em **toda** TQC (a própria QCD). Não entrega a "escala
     absoluta sem input" que 2.1 prometia.

**A fresta exata que permanece não-testada (registrada, sem desenho de experimento):** um
acoplamento marginal sobre o d'Alembertiano causal FIXO de Poisson, cujo *running*
(β≠0) se manifeste num observável **não obstruído pela não-localidade** (i.e., não uma
lei-de-área de Wilson), produzindo uma razão transmutada genuinamente emergente. **Estrutura
mínima do que seria necessário para testá-lo** (sem executar): (1) identificar um campo com
acoplamento classicamente marginal definível sobre o causet; (2) um observável que extraia
um acoplamento efetivo dependente de escala **sem** depender de um loop de Wilson de área
controlada (o objeto que A2 mostrou indisponível); (3) verificar se a função beta é
não-trivial no espectro do d'Alembertiano causal (vs. trivialmente nula = sem transmutação);
(4) anti-circularidade: a razão `Λ/ρ` deve sair do `g` adimensional, não de um literal de
escala inserido. Pende de autorização explícita.

**Veredito de uma linha:** o teorema binário fecha escala-por-conectividade (e, via o
princípio de não-localidade, a realização canônica de escala-por-running no chão invariante);
ele é **logicamente mudo** sobre transmutação dimensional como dinâmica de campo, mas essa
fresta é **estreita, anchored numa escala inserida, e parcialmente obstruída pela mesma
não-localidade** — incerteza genuína, não porta aberta. **Não é reabertura da busca por
substrato** (o chão fica fixo); é o reconhecimento de que a única classe de mecanismo que o
teorema não toca é a dinâmica de campo sobre o chão, e que o programa já tem a evidência
(A2) de que a não-localidade a alcança parcialmente.

---

## 5. Fontes (física conhecida)

- Wilson & Kogut, *Phys. Rep.* 12 (1974) — RG, ponto fixo de Wilson–Fisher (2.1).
- Coleman & Weinberg, *Phys. Rev. D* 7 (1973) 1888 — transmutação dimensional radiativa (2.2/2.3).
- Gross & Wilczek; Politzer, *Phys. Rev. Lett.* 30 (1973) — liberdade assintótica, β<0 (2.2).
- Creutz, *Quarks, Gluons and Lattices* (1983) — `σa²(β)∝exp(−1/2b₀β)` na rede (2.2).
- Coleman–Jackiw, *Ann. Phys.* 67 (1971); Crewther, *PRL* 28 (1972) — anomalia de traço (2.5).
- Derrick, *J. Math. Phys.* 5 (1964) — teorema de escala, sólitons (2.4).
- 't Hooft, *Phys. Rev. D* 14 (1976) — instantons, módulo de tamanho (2.4).
- Casimir (1948); Kaluza–Klein — escala de contorno/compactificação (2.6).
- Miransky (1985); Kosterlitz–Thouless, *J. Phys. C* 6 (1973) — singularidade essencial (2.7).
- Hořava, *Phys. Rev. D* 79 (2009) — escala anisotrópica de Lifshitz (rota foliada, §4b).

**Fontes internas:** `IMPOSSIBILIDADE_PARCIAL/RESULTADO.md`; `SINTESE_SETE_MORTES/RESULTADO.md`;
`REPULSAO_LORENTZ/docs/FRONTEIRA_CONHECIDA.md` §6.bis; `TEIC/.../CONFINAMENTO_A2/SYNTHESIS.md`
(FRONTEIRA: confinamento SU(3) sólido no cúbico, não-mensurável no causet); `FL1` (SU(3)
confinamento+liberdade assintótica no controle); `ESCALA_XI` (2.1=MF); `C5-SPECTRAL-DIMENSION`
(dimensão espectral sem running genuíno); guard TEIC (`dilation banned everywhere`).
