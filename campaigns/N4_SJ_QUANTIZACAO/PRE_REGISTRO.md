# N4 — SJ_QUANTIZACAO: pré-registro (= F1 do ROADMAP_V2)

**Data:** 2026-07-02 · **Pasta:** `FRONTEIRA_COMPACTA/N4_SJ_QUANTIZACAO/`
**Linha:** ROADMAP_V2, Linha 2 (física), item F1 — "o centro da linha".
**Gates satisfeitos:** N0 ✓ (LIBERADO com upgrade P1) + N0′ ✓ ("atacado e de pé").
**Escrito ANTES de qualquer código da campanha** (disciplina padrão; esta é a
campanha mais cara da linha e por isso exigiu sessão de pré-registro própria).

**O upgrade de P1 (por que esta campanha não é "uma opção"):** N0 §6 provou que a
tese proíbe toda variável fundamental sobre superfícies espaciais — cai a
quantização canônica inteira (ADM, Wheeler–DeWitt, gauge Hamiltoniano, redes de
spin como cinemática). O que resta é histórias/covariante, e a construção
covariante nativa da CST é Sorkin–Johnston. **N4 não testa "uma quantização";
testa A quantização que o princípio força.** Se ela falhar em ter forma, o
setor-ℏ da classe fica sem porta conhecida — resultado de prioridade máxima.

---

## 1. A pergunta e sua decomposição

**Pergunta-mestra (charter §N4):** o que o campo de orientação faz quantizado à
la Sorkin–Johnston? Única porta do setor-ℏ nunca aberta (C5 fechou dimensão
espectral; SJ é outra coisa). Decomposição pré-registrada:

- **Q0 (analítica — o preço da porta):** de que inputs a construção SJ depende
  além de (C, ≺)? Candidato a lema: SJ exige a ESCOLHA retardado-vs-avançado =
  exatamente 1 bit de seta temporal — o mesmo bit que EXP2 mediu como input, e o
  portador da estrutura complexa que o corolário GOE diz não emergir. A porta-ℏ
  custaria o T-bit; consistência interna do princípio em jogo.
- **Q1 (a forma — porta-ℏ):** o vácuo SJ do escalar livre sobre o NOSSO substrato
  (caixa de Poisson, não só o diamante da literatura) existe, é estável em
  volume/densidade, e tem forma relativística no IR (ω = c|k|)?
- **Q2 (Axioma 2 de lado):** o vácuo SJ define estrutura interna natural?
  Versão fraca (mensurável): o multipleto de Goldstones do campo de orientação
  SOBREVIVE à quantização SJ sobre o vácuo ordenado REAL (fundo MC com desordem
  térmica)? Versão forte (analítica): a construção SJ sobre o substrato puro
  CRIA alguma fibra compacta além do U(1)-por-modo padrão de QFT?
- **Q3 (a face entrópica — liga N4 a N2):** a entropia de emaranhamento de
  espaço-tempo de Sorkin (SSEE) através do horizonte de N2 obedece lei de área
  com o truncamento declarado da literatura — ou a não-localidade da camada 1
  quebra a área também no setor QUÂNTICO, como quebrou a MI clássica (N2-F2,
  super-área L^{3.36})? **É a medição de maior informação da campanha** (as duas
  saídas refinam o Teorema da Fronteira; prior honesto ~50/50).

## 2. O objeto matemático (definições a CONGELAR na Fase 0)

Construção SJ padrão, congelada nesta forma (coeficientes exatos conferidos e
fixados na Fase 0, antes de código):

1. **Propagador retardado K_R** sobre o sprinkling: família de Johnston
   (hop-stop). d=2: K_R ∝ matriz causal C (série de massa em C); d=4: K_R ∝
   matriz de links L (série de massa em L). Coeficientes (a, b) por dimensão =
   valores da literatura, rederivados na Fase 0. **Segundo operador (N-hig 2):**
   inversa retardada do d'Alembertiano BD suavizado (validado em C5/TEIC) como
   cross-check em d=2 no mínimo.
2. **Função de Pauli–Jordan:** iΔ = K_R − K_A, com K_A = K_R^T. Propriedade de
   engenharia (checada sempre): iΔ é Hermitiana com espectro em pares ±λ.
3. **Vácuo SJ:** W_SJ = parte espectral positiva de iΔ (Pos(iΔ)). Estado de
   região — a dependência-de-região do SJ é caveat DECLARADO, não surpresa.
4. **SSEE de Sorkin:** problema generalizado W v = μ (iΔ) v restrito à
   sub-região; S = Σ μ ln|μ|. Truncamento do espectro de iΔ no "joelho"
   (critério da literatura) — **o critério numérico do joelho é congelado na
   Fase 0 a partir da reprodução d=2, ANTES de qualquer run d=4** (lição
   max_tau=15: janela de estimador não se ajusta depois de ver o dado).

## 3. Fase 0 — analítica + literatura (zero código)

Entregáveis:

- **Tabela de âncoras conferidas** (cada uma com enunciado exato + o que nossa
  reprodução deve bater): (i) Johnston — propagadores d=2/d=4, coeficientes;
  (ii) Sorkin–Johnston — definição do estado, unicidade; (iii) Afshordi–
  Aslanbeigi–Sorkin — SJ no diamante 2D ≈ vácuo de Minkowski no centro
  [constante exata: conferir]; (iv) Fewster–Verch — SJ não-Hadamard + versão
  suavizada; (v) Surya–Nomaan X–Yazdi — vácuo SJ em causets d=2/d=4, achados
  exatos [conferir: onde o causet DIFERE do contínuo em d=4]; (vi) Sorkin/
  Sorkin–Yazdi — SSEE, lei de VOLUME sem truncamento no diamante 2D + área com
  truncamento no joelho [conferir critério exato do joelho]. Se a literatura já
  responder alguma sub-pergunta, registrar e ESTREITAR o escopo (honest scoping).
- **Lema Q0 (candidato):** toda saída SJ é função de (C, ≺) + 1 bit (K_R vs
  K_A); trocar o bit conjuga W_SJ (anti-unitário); observáveis PARES sob
  conjugação (espectros |λ|, entropias, |W|) independem do bit; fases/distinção
  partícula–antipartícula dependem. *Consequências:* (a) a porta-ℏ é compatível
  com EXP2 (seta = input) e com o corolário GOE (a estrutura complexa é
  CARREGADA pelo bit, não emergente — "dualidade carregada" da camada 2);
  (b) **morte embutida:** se algum observável ímpar-sob-conjugação for fixável
  intrinsecamente, isso ataca a camada 2 de N0 → reportar imediatamente.
- **Q2-forte (analítica):** enunciar com precisão o que seria "SJ cria estrutura
  interna" (uma fibra compacta não-inserida agindo no espaço de modos) e por que
  o esperado é NÃO (prior declarado: Axioma 2 permanece postulado; esse desfecho
  é DELIMITAÇÃO, não morte).
- Congelar: coeficientes, janelas (§7), critério do joelho, rota da Fase 2 (§5).

> **ADENDO 02jul26 (emenda de gate, declarada antes do run final — trilha
> completa em `GATE_G_RESULTADO.md`):** G3-diamante tinha FALHA DE DESENHO
> contra a literatura (mL=6.7 ⇒ ~3 λ_Compton + cantos-espelho ⇒ ridge de modos
> sem média de COM contaminado por borda; discriminante massless reproduz o
> viés ⇒ test-bed, não física). G3 substituído por **G3′ = controle de
> propagador ⟨G_R⟩ = ½J₀(mτ)** (RMS < 5% + 1º zero ± 5%); a validação
> dois-estimadores-15% do gap MIGRA para a caixa da Fase 1 (M1.2/M1.3, onde
> já estava pré-registrada). O processo do gate pegou e corrigiu um bug de
> sinal taquiônico no propagador massivo (ver GATE_G_RESULTADO §2).

## 4. Gate de engenharia (Fase G) — reproduzir a literatura ANTES de medir

Diamante causal 2D, escalar sem massa, N ∈ {1024, 2048, 4096}, 12 seeds:

- **G1:** espectro de iΔ em pares ±λ (máquina-precisão) e escala do espectro
  compatível com a literatura d=2.
- **G2:** W_SJ na região central vs. Wightman contínuo 2D massless (forma log +
  constante AAS): concordância declarada R² > 0.9 na janela de bulk (§7).
- **G3:** controle massivo (m dentro da janela IR): gap detectado pelos DOIS
  estimadores de dispersão (§7) dentro de 15% — anti-bug do estimador.
- **G4 (SSEE):** reproduzir Sorkin–Yazdi no diamante 2D: volume sem truncamento;
  área com truncamento no joelho congelado.

**Gate VERDE (4/4) obrigatório antes da Fase 1.** Falha após esgotamento de
diagnóstico = parada de ENGENHARIA (campanha inválida, não morte da teoria).

## 5. Fases de medição

### Fase 1 — vácuo SJ do escalar livre no NOSSO substrato

Caixa causal em M^d (t ∈ [−T,T], x⃗ ∈ [−L,L]^{d−1}), sprinkling de Poisson —
o substrato do programa, não o diamante da literatura (o diamante fica como
âncora). Grades: d=2 N ∈ {1024, 2048, 4096} (ρ varrida ×4); d=4 ρ=8,
N ∈ {2000, 4000, 8000}, 12 seeds; Lanczos parcial (top-200 modos) até N=2×10⁴
só para dispersão. Medições:

- **M1.1:** estabilidade do vácuo (split ±λ limpo; Pos(iΔ) estável sob N, ρ).
- **M1.2:** dispersão IR pelos dois estimadores (§7): existe ramo ω = c|k| na
  janela IR? c medido (unidades de rede; a velocidade causal é 1 por construção
  do sprinkling — o TESTE é |c−1| ≤ 0.15 em d=2, ≤ 0.20 em d=4).
- **M1.3:** controle massivo (gap ω² = c²k² + m² dentro de 15%).
- **M1.4:** densidade espectral de iΔ vs. contínuo; onde o UV se desvia
  (esperado: escala de discretude ρ^{−1/d} — camada 1 pode aparecer aqui;
  reportar a forma do desvio, sem critério de morte no UV).

### Fase 2 — o setor Goldstone (o campo de orientação) [gated pela Fase 1]

Vácuo ordenado do motor N1 (SUNChiralModel N=2 = setor de orientação), d=4,
ρ=4, L ∈ {2, 3}, J=1.0 (mesma configuração de N2 fase 2), 4 seeds MC × 3
configurações descorrelacionadas cada (burn 500; τ_int/ESS reportados — N-hig 1).

**Rota congelada (R-A, critério):** vácuo ideal uniforme ⇒ setor Goldstone =
N_G cópias exatas da Fase 1 (afirmação analítica, não se mede). O que se MEDE é
o vácuo REAL: a desordem térmica do fundo MC entra como termo de massa local
m²(x) nas direções de Goldstone (Hessiana da ação na configuração, projetada),
acoplado à série massiva de Johnston com b dependente de sítio. **Rota R-B
(nativa, Hessiana de Hasse com fatoração causal): diagnóstico exploratório
apenas, NÃO critério** — lição C5: o Laplaciano de grafo já falhou um gate de
contínuo uma vez.

- **M2.1:** a forma relativística IR sobrevive ao fundo real? (mesmos
  estimadores/janelas da Fase 1; c_s comparado ao magnon clássico E2 dentro de
  erros combinados.)
- **M2.2 (Q2-fraca):** degenerescência do multipleto: espectros SJ das N_G
  componentes de Goldstone sobre o MESMO fundo — splitting relativo na janela
  IR. Calibração declarada: o splitting térmico CLÁSSICO medido nas mesmas
  configurações é a régua; morte só se o splitting quântico ≫ clássico E não
  decresce com o tamanho.

### Fase 3 — SSEE pelo horizonte (liga N4 a N2) [gated por Gate G + Fase 1;
independente da Fase 2]

Geometria de N2: canto de Rindler H ∩ Σ em caixa d=4 (ρ=8, L ∈ {1.5, 2, 3}),
sub-região = laje interna junto ao canto (janela declarada como em N2 fase 2);
âncora d=2 no diamante (G4). Medições:

- **M3.1:** SSEE SEM truncamento vs. L — expoente (prior de literatura+N2:
  NÃO-área; super-área/volume compatível com a 3ª face).
- **M3.2:** SSEE COM truncamento no joelho congelado vs. L — **a pergunta de
  maior informação:** expoente compatível com d−2 (área) ou não?
  - Se ÁREA: a quantização covariante + corte UV declarado RESGATA a lei de área
    que a MI clássica de matéria perdeu → refina o escopo do princípio ("a
    entropia quântica de campo é da ordem; a clássica é do grafo") — upgrade
    do Teorema da Fronteira, vai ao paper-núcleo com delta próprio.
  - Se NÃO-ÁREA: a tensão binária tem a 4ª face, agora quântica → N2-F2 sobe de
    "face medida" para "estrutural, sobrevive à quantização" — prioridade máxima.
  - Nenhuma das duas é morte; INCONCLUSIVO só se o joelho for instável
    (critério congelado deixa de identificar um joelho único — reportar como
    falha de estimador, não de física).

## 6. Previsões pré-registradas (com priors honestos)

| # | Previsão | Prior declarado |
|---|---|---|
| P-N4-1 | Vácuo SJ existe e é estável no substrato-caixa; ramo IR relativístico ω=c|k|, c≈1 | ALTO (E2 clássico Verdict A; C5 gate BD verde) |
| P-N4-2 | Lema Q0: porta-ℏ custa exatamente 1 bit (a seta); observáveis pares independem dele | ALTO (analítico; consistência EXP2+GOE) |
| P-N4-3 | SSEE sem truncamento: não-área. Com truncamento: **50/50 declarado** (área = resgate; não-área = 4ª face) | INCERTO — por isso é a medição central |
| P-N4-4 | Q2-fraca: multipleto sobrevive (splitting quântico ~ clássico). Q2-forte: SJ NÃO cria fibra compacta (Axioma 2 fica postulado) | ALTO / ALTO (positivo da forte = descoberta) |

## 7. Janelas de estimador (N-hig 3 — congeladas AGORA)

- **Janela IR de dispersão:** |k| ∈ [2·(2π/L_x), 0.25·2πρ^{1/d}]; fit OLS
  log-log no ridge; tolerância de c em §5.
- **Dois estimadores de dispersão (obrigatórios, concordância 2σ):**
  E1 = potência espectral (NUFFT) dos top-M modos SJ (M=100) com ridge ω(k);
  E2 = FT de W_SJ(x,y) em bins (Δt, Δx⃗) sobre pares de bulk.
- **Janela de bulk:** pontos a mais de 15% do lado da caixa de qualquer borda
  (SJ é estado de região; bordas descartadas por construção declarada).
- **Massa de controle:** m = 3·(2π/L_x) (dentro da janela IR por construção).
- **Joelho do SSEE:** critério único congelado na Fase 0 a partir do d=2
  (G4) e NUNCA reajustado após runs d=4.
- **Fase 2 MC:** burn 500, medidas a cada 2 sweeps, τ_int/ESS reportados;
  controle desordenado (J=0.05) para a régua de splitting.

## 8. Mortes pré-registradas

1. **D-G (engenharia):** Gate G < 4/4 após diagnóstico → campanha INVÁLIDA
   (parada de engenharia; não é morte da teoria; reportar como tal).
2. **D1 (porta-ℏ estrutural):** vácuo SJ mal-definido no substrato (split ±λ
   não-limpo, Pos(iΔ) instável em N/ρ) COM gate G verde → a única quantização
   compatível com o princípio não se define sobre o substrato do programa →
   **prioridade máxima** (o setor-ℏ fica sem porta conhecida).
3. **D2 (forma quântica):** os DOIS estimadores concordam que não há ramo IR
   relativístico (|c−1| fora de tolerância ou sem ridge) → primeira falha de
   "formas derivam" no setor quântico → prioridade máxima.
4. **D3 (multipleto, Fase 2):** splitting quântico ≫ régua clássica E
   não-decrescente com tamanho → a forma da camada 3 não sobrevive à
   quantização (morde o paper-núcleo; delta próprio).
5. **D-Q0 (ataque a N0):** observável ímpar-sob-conjugação fixável
   intrinsecamente → contradiz camada 2 → reportar imediatamente (edita N0,
   como manda o protocolo N0′).
6. **Q2-forte negativa e M3 (qualquer saída): NÃO são mortes** — delimitação e
   refinamento, respectivamente (declarado antes para não haver upgrade
   retórico depois).

## 9. Higiene e anti-circularidade

- Coordenadas de embedding usadas SÓ como leitura diagnóstica de observador
  (FT/janelas), nunca como ingrediente de regra — precedente E2/C5, declarado.
- Nenhum número físico inserido (nem ℏ, nem 1/4, nem c além da unidade do
  sprinkling); tudo medido em unidades de rede; ℏ entra como NORMALIZAÇÃO da
  construção SJ (declarado: N4 testa FORMA do setor quântico, não valor de ℏ —
  escala externa como todas as do programa).
- Seeds fixas; JSON com meta por run; erros = SEM sobre seeds; fits OLS
  ponderados em log-log.
- Custo declarado (a campanha mais cara): diagonalização densa O(N³) até
  N=8000 (~1 GB, minutos–dezenas de minutos por config), ×12 seeds × grades ≈
  1–3 CPU-dias; Lanczos parcial além disso. Orçamento estourando ×3 → parar e
  reavaliar grades (não afrouxar janelas).

## 10. O que N4 NÃO reivindica

- Setor LIVRE/Gaussiano apenas — nenhuma interação, nenhum loop (o loop do
  programa vive em N5, já executado e morto na rota radiativa).
- Nenhum valor de ℏ; nenhuma afirmação sobre colapso/medida (setor SR é outra
  linha); nada sobre gravidade dinâmica (substrato quenched — escopo do Lema 3).
- Não reabre o fóton: Goldstones são do setor interno; nenhum portador de
  2-forma aparece aqui (se aparecer, isso é ataque a N0, não vitória — ver D-Q0).
- Não testa P1 em si (a impossibilidade canônica é argumento de N0 §6); N4
  testa se a alternativa FORÇADA funciona.
- A dependência-de-região do estado SJ é caveat estrutural declarado, não bug.

## 11. Funil e critério de encerramento

```
Fase 0 (analítica: âncoras + lema Q0 + congelamentos)   ← zero código
  → Gate G (diamante d=2: G1–G4, VERDE 4/4 obrigatório)
    → Fase 1 (escalar no substrato; D1/D2 vivem aqui)
      → Fase 2 (Goldstone/multipleto)      [gated: Fase 1 sem D1/D2]
      → Fase 3 (SSEE horizonte)            [gated: G4 + Fase 1; ∥ à Fase 2]
```

**Encerramento:** veredito escrito por fase (Q0–Q3 respondidas, mortas ou
declaradas inconclusivas com causa) em `RESULTADO.md`; qualquer morte reportada
como resultado; upgrades de alegação nos papers só com delta próprio (regra 3
do ROADMAP_V2).
