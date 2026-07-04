# SYNTHESIS — NESS_GEOMETRIA: geometria CDT 3D fora-do-equilíbrio escapa do mean-field?

> **Pré-registro:** `PRE_REGISTRO.md` (mecanismo, Gates 1/2 e critério de morte §6 congelados
> ANTES de medir). **Código:** `driven_cdt.py` (drive paramétrico k₀(τ), reusa F1b intacto),
> `gate1_stationarity.py`, `gate2_detailed_balance.py`, `scaling_ness.py` (reusa
> `ferro_cdt.question_A/B` + `cdt_substrate` verbatim). **Dados:** `gate1.json`, `gate2.json`,
> `scaling_ness.json`, `ness_figures.png`. **Data:** 2026-06-29.
>
> **Direção 2** do prompt (geometria NESS). Pergunta: a geometria do CDT 3D, **dirigida
> fora-do-equilíbrio** (NESS genuíno), escapa do **mean-field** que matou Poisson, CSG e
> CDT-em-equilíbrio (`CDT_TEIC_FERRO` Pergunta B não-resolvida, lean-MF)?

---

## VEREDITOS (na ordem pré-registrada: Gate 1 → Gate 2 → escala)

### Gate 1 — Estacionariedade: **PASSA** (NESS, não a armadilha α=0,1)
O sistema dirigido (k₀(τ)=2,5+1,5·cos(2πτ/8), Vt=1500, T=10) atinge **estado estacionário
estatístico genuíno** — o oposto de "nunca converge":

| run | manifold | N₃ estac. | z estac. | d_H estac. | d_H (platô) | veredito |
|---|---|---|---|---|---|---|
| NULO (A=0, equilíbrio) | ✓ | ✓ | (✓)* | ✓ | 2.42±0.02 | controle |
| DRIVE s201 | ✓ | ✓ | ✓ | ✓ | 2.43±0.03 | **PASS** |
| DRIVE s202 | ✓ | ✓ | ✓ | ✓ | 2.44±0.03 | **PASS** |

Critério faithful do PRE-REGISTRO §3 ("média E variância constantes ENTRE janelas, dentro do
erro de blocking"): teste de duas-metades com SEM-bloqueado (half_z<3) + F-test de variância +
guarda lenta contra deriva monotônica não-limitada (t_slope). **Horizonte de relaxação medido
explicitamente** (~350–450 sweeps a Vt=1500): a 1ª tentativa (therm=140) media ainda na subida e
deu deriva espúria — corrigido para therm=450 (medição no platô). *O NULO de equilíbrio passa em
média; o único sub-teste que ele trip é o F-ratio de variância de z (artefato de pequena amostra/
autocorrelação), não não-estacionariedade física — daí a calibração do estimador.

**A armadilha central foi evitada:** o estado é estacionário e bem-definido, não um relaxamento
lento mascarado.

### Gate 2 — Quebra de balanço detalhado: **PASSA** (NESS genuíno)
No estado estacionário, o sistema **não satisfaz reversibilidade microscópica** — há corrente de
probabilidade no espaço de configurações, manifesta como **histerese** (área do laço k₀ vs resposta
geométrica = produção de entropia/ciclo) e como **fluxo circulante fase-resolvido** dos pares de
Pachner:

| P (sweeps/ciclo) | área histerese ⟨k₀,z⟩ | sig. (\|a\|/sem) | sinal | frac_envelope |
|---|---|---|---|---|
| 4 | −0.21 | 13–15σ | − | 0.056 |
| 12 | −0.40 | 8σ | − | 0.091 |
| 32 | −0.23 | 2σ | − | 0.055 |
| 96 | −1.36 | 9–13σ | − | 0.242 |

Histerese **grande, significativa e sinal-consistente (negativa) em todos os P, robusta a 2 seeds**
→ balanço detalhado quebrado. O **fluxo fase-resolvido** de (2,6)/(6,2) circula com a fase do drive
(swing −→+ ao longo do ciclo, integrando ≈0 net mas com lag claro) — a assinatura mecanística da
corrente de NESS, além da área. **Honestidade:** a Vt=800 a área NÃO decai até P=96 (cresce) ⇒ τ_relax
> 96 sweeps, **não bracketei o limite adiabático** nesse volume; mas o smoke a Vt=600 mostrou a
decaída a P=32 (limite adiabático existe e é alcançável). O critério §4 ("histerese significativa e
estável em ao menos um P não-adiabático") é satisfeito **decisivamente**.

### Escala sob NESS confirmado: Pergunta A **REPRODUZ** / Pergunta B **NÃO-RESOLVIDO (ambíguo)**
Suíte de universalidade verbatim (`ferro_cdt.question_A/B`) sobre **snapshots estroboscópicos** da
geometria NESS (k̄₀=2.5, A=1.5, P=8), 3 volumes × 10 snapshots, comparada às curvas conhecidas.

**Pergunta A (reprodução) — REPRODUZ_LRO, limpo:**

| N₀ | m | m/floor | U₄ | C(r) |
|---|---|---|---|---|
| 282 | 0.937 | 15.7 | 0.667 | plateau (C_long 0.86) |
| 530 | 0.936 | 21.5 | 0.667 | plateau (0.87) |
| 1053 | 0.925 | **30.0** | 0.667 | plateau (0.86) |

m estabiliza (trend dlnm/dlnN=−0.01), m/floor **cresce** com N (LRO real), U₄ no valor O(3) ordenado
(2/3) — **a geometria NESS é um fundo geométrico sadio**, igual ao equilíbrio. (Equivalente ao
veredito A de `CDT_TEIC_FERRO`.)

**Pergunta B (universalidade) — NÃO-RESOLVIDO, no limiar do mean-field com sinais mistos:**

| N₀ | χ_max | J_c | U₄@J_c |
|---|---|---|---|
| 282 | 1.39 | 0.22 | 0.611 |
| 530 | 1.69 | 0.20 | 0.612 |
| 1053 | 2.78 | **0.18** | 0.585 |

→ **χ_max ~ N^0.53** (MF≤0.5, geom-3D~0.66). **Overlay:** Poisson N^0.07, CDT-equilíbrio N^0.24.

**Por que NÃO-RESOLVIDO (disciplina §5, não forçar o ambíguo):**
1. **A favor de algo novo:** χ(J) agora tem **picos limpos e únicos** (1.39→1.69→2.78, monotônico —
   não o serrilhado de ruído dos 4 seeds de `CDT_TEIC_FERRO`); o expoente **0.53 é mais do DOBRO**
   do equilíbrio-CDT limpo (0.24) e muito acima do Poisson (0.07). Algo **mudou** sob o NESS.
2. **Contra um escape limpo:** **x=0.53 ≈ 0.5 (o teto MF)**, não convincentemente rumo a 0.66
   geométrico; **J_c DERIVA para baixo** (0.22→0.20→0.18) — a assinatura canônica Poisson/MF (sem
   ponto-fixo de cruzamento, cf. `baseline_3p1` Jc_drifts_down=True); U₄ não cruza em J_c fixo. A
   própria deriva de J_c **contamina** a estimativa do expoente de χ_max (mede-se χ a distâncias
   efetivas distintas da transição em cada tamanho). Só **3 tamanhos** — não distingue 0.53 de 0.5.
3. **ξ:** o ξ_g/L medido (10.7→8.9→7.2) é o **platô da fase ordenada** (winner='const', C_long~0.86),
   não o ξ_2nd crítico em J_c — **não-informativo** para classe aqui (registrado, não usado).

**Leitura honesta (deste run isolado, DEPOIS SUPERADA pela resolução abaixo):** o expoente χ_max
**parecia** subir vs equilíbrio (0.24→0.53), sugerindo realce do não-equilíbrio — mas era **3
tamanhos, 10 snapshots, sem barra de erro no expoente**, no regime k₀~2,5 que `CDT_TEIC_FERRO` já
flagara como noise-dominated. Por isso NÃO foi tratado como decisivo aqui, e disparou o follow-up
x(A) — que **resolveu para mean-field** (o 0,53 era ruído; ver seção "RESOLUÇÃO da Pergunta B").

---

## O que esta campanha estabelece (e o que não)

**Estabelece:**
1. **É possível dirigir a geometria CDT 3D para um NESS genuíno** (Gates 1 **e** 2 passam) sem
   quebrar o manifold (validador verde em toda configuração) — o mecanismo paramétrico (c) funciona
   e os dois gates são testes **reais** (a estacionariedade não é o trap α=0,1; o balanço detalhado
   é de fato quebrado, com corrente fase-resolvida). **Primeira realização de geometria CDT
   fora-do-equilíbrio bem-posta do programa.**
2. **Pergunta A: a geometria NESS permanece um fundo geométrico sadio** (LRO reproduzido, d_H≈2.4
   no platô, U₄ ordenado, m/floor crescente) — dirigir fora-do-equilíbrio **não destrói** a
   geometria (a "Morte 2" prevista no prior NÃO ocorreu).

**NÃO estabelece (honestidade, anti-forçar §5):**
1. **Não há escape do mean-field.** A Pergunta B, depois RESOLVIDA pela varredura x(A) (abaixo),
   é **mean-field/noise-limited**: o aparente 0.53 era flutuação (irreprodutível a parâmetros
   idênticos). A geometria NESS **não** muda a classe de universalidade.
2. **Nada "escala emergiu"** (A, P, k̄₀ `[External]`; B é sobre classe).

## RESOLUÇÃO da Pergunta B (follow-up `B_RESOLUTION_PREREG.md`, executado 29jun26) — **MEAN-FIELD (o 0.53 era RUÍDO)**

A varredura de amplitude **x(A)** (`b_resolution.py`, 4 amplitudes × 3 volumes × 10 snapshots) —
o teste pré-registrado para decidir se o realce 0.24→0.53 é mecanístico (NESS) ou flutuação —
**resolveu B para mean-field/noise-limited**:

| A (intensidade do drive) | x (χ_max~N^x) | χ_max(N~1050) | J_c drift |
|---|---|---|---|
| 0,0 (equilíbrio, controle) | 0,30 | 2,11 | −0,04 |
| 0,75 | 0,63 | 3,36 | −0,02 |
| 1,5 | **0,38** | 1,86 | −0,04 |
| 2,25 | 0,50 | 2,33 | −0,06 |

**x(A) é DISPERSO, NÃO monotônico** (0,30→0,63→0,38→0,50; slope ≈ +0,05, plano) — **nenhuma
dependência da intensidade do não-equilíbrio**. A assinatura pré-registrada de MF está satisfeita
("x(A) disperso ~0,3–0,5 sem tendência **E** J_c segue derivando em todo A" — drift não encolhe:
−0,04,−0,02,−0,04,−0,06, o mais forte em A=2,25).

**A prova decisiva — irreprodutibilidade a parâmetros idênticos:** o run principal e este run usam
**exatamente os mesmos parâmetros em A=1,5**, e deram **x=0,53 vs x=0,38** (χ_max no maior volume:
**2,78 vs 1,86**, ~50% de diferença). Mesma física, realizações de snapshot diferentes → **o
expoente é noise-dominated nesses volumes; o "0,53" foi uma flutuação alta**, não um sinal estável.
Confirma exatamente a advertência de `CDT_TEIC_FERRO` (em k₀~2,5–3, χ_max é noise-dominated).

> **Pergunta B RESOLVIDA → MEAN-FIELD.** O não-equilíbrio **não** realça o expoente de forma
> mecanística; o aparente realce era ruído. A barreira estrutural de alta-coordenação (z~13,
> small-world/Bethe ⇒ MF por teorema) é **robusta a equilíbrio E a não-equilíbrio**.

## Veredito da Direção 2 (PRE-REGISTRO §6) e decisão sobre a Parte B

> §6 mata a Direção 2 se Gate 1/2 falhar **OU** se a escala sob NESS mostrar assinaturas
> mean-field. Gates 1 e 2 PASSARAM, mas a **Pergunta B foi RESOLVIDA → mean-field** (varredura
> x(A): expoente disperso sem tendência, J_c derivando em todo A, e o 0.53 irreprodutível a
> parâmetros idênticos = ruído). **A condição de morte É satisfeita: a escala sob NESS é
> mean-field.**
>
> **A Direção 2 está MORTA por §6:** geometria fora-do-equilíbrio, nesta formulação, **não escapa
> do mesmo destino das tentativas em equilíbrio**. A barreira estrutural de alta-coordenação (z~13)
> é robusta a equilíbrio **E** a não-equilíbrio. **O prompt manda prosseguir para a Parte B.**

## Decisão sobre a Parte B (gatilho cinemático 4D)
A morte §6 dispara → a Parte B fica **autorizada**. **Recomendação honesta antes de gastar nela:**
o que a Parte A mostrou é que o **mecanismo do mean-field é a alta coordenação do 1-esqueleto**
(z~13, small-world/Bethe ⇒ MF por teorema — [[escala-xi-correlation-divergence]]), e isso é
**estrutural do CDT em qualquer dimensão**. Em **4D a coordenação é AINDA MAIOR** (4-simplexos
compartilham mais), então o prior para o gatilho 4D é **MF mais forte, não mais fraco** — o gatilho
cinemático 4D provavelmente também não arma (⟨z⟩ alto, discriminador de clustering dominado pela
coordenação). A Parte B é **barata** (combinatória, sem motor dinâmico), então **vale rodar como
gate barato** para confirmar/refutar esse prior — mas com expectativa baixa, e SEM construir o
motor dinâmico 4D completo (decisão separada, só se o gatilho armar surpreendentemente).

## O que faltaria para reabrir a escala (registrado, não o caminho recomendado)
- Reduzir a coordenação z do substrato (cap k-NN, como em `ESCALA_XI`) — mas isso já foi testado e
  **viola Lorentz/folheação** (a coordenação métrica não pode ser cortada sem quebrar a causalidade);
  o cap de contagem dá transição contínua mas **platô-LRO, não pico** (mean-field por teorema). Ou
  seja: o caminho de fugir do MF reduzindo z **já está fechado** em campanha anterior.
- Volumes ordens de magnitude maiores (N₀≥10⁴) com ≥24 snapshots — só para cravar x com barra de
  erro; mas o veredito x(A) já mostra que não há tendência a explorar (não é questão de precisão).

**Resumo de uma linha:** dirigir a geometria CDT 3D para um **NESS genuíno** (Gate 1 + Gate 2 ambos
PASSAM, manifold sempre válido) é **possível e não destrói a geometria** (Pergunta A REPRODUZ LRO),
**mas o teste de escala — resolvido pela varredura de amplitude x(A) — é MEAN-FIELD**: o expoente é
disperso e sem tendência com a intensidade do drive (0,30/0,63/0,38/0,50), J_c deriva em todo A, e o
"χ_max~N^0,53" do 1º run era **ruído** (irreprodutível: 0,53 vs 0,38 a parâmetros idênticos) — logo
**a Direção 2 MORRE por §6** (a barreira de alta-coordenação z~13 é robusta a equilíbrio **e**
não-equilíbrio), o que **autoriza a Parte B (gatilho 4D)** com prior honesto de MF ainda mais forte
em 4D (z maior), a rodar só como **gate combinatório barato**, sem o motor dinâmico completo.

**Anti-circularidade (charter §3):** A, P, k̄₀ são `[External]` (drive não emerge); nada "escala
emergiu"; o ferromagneto O(3) é sonda de **classe de universalidade** sobre a geometria NESS.
