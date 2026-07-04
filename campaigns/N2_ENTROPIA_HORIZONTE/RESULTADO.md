# N2 — ENTROPIA_HORIZONTE: resultado

**Data:** 2026-07-02 · **Pasta:** `FRONTEIRA_COMPACTA/N2_ENTROPIA_HORIZONTE/`
**Pré-registro:** `PRE_REGISTRO.md` (antes do código). Motor: `n2_core.py` (+
`sun_core`/`su3_core` de N1/FL1 na fase 2). Drivers: `n2_phase1.py` (pré-reg.),
`n2_phase1b.py` (pós-hoc declarado, molécula da literatura), `n2_phase1c.py`
(convergência), `n2_phase2.py`/`n2_phase2b*.py` (matéria). JSONs respectivos.

---

## VEREDITO EM DUAS LINHAS

1. **Fase 1 (geometria): S ∝ A EMERGE** — com a molécula de horizonte correta da
   literatura (Barton et al.), a lei de área fecha em d=2, 3 e 4, com
   independência-T e escala ρ^{1/2}; o coeficiente é medido e fica EXTERNO,
   exatamente como a previsão pré-registrada ("forma emerge, coeficiente
   externo"). A tese "formas derivam" NÃO sofreu sua primeira falha.
2. **Fase 2 (matéria): MORTE PRÉ-REGISTRADA DISPARA** — a informação mútua do
   ferromagneto através do mesmo horizonte é SUPER-ÁREA (I ~ L^3.4, compatível
   com ∝L³): a entropia de MATÉRIA não obedece lei de área neste substrato. O
   mecanismo é a não-localidade da camada 1 (os links do grafo que cruzam o
   canto crescem ~L^4.2, medido) — a mesma tensão binária, agora no setor
   térmico/entrópico.

---

## Fase 1 — geometria (3 rodadas, com lição de estimador documentada)

### 1a. Estimador pré-registrado (tipo Dou–Sorkin por quadrante): FALHA em d=4

| Check | d=2 | d=3 | d=4 |
|---|---|---|---|
| Expoente vs área | ✓ (−0.11±0.04, constante) | ✓ (1.065±0.089) | **✗ 2.928±0.125** (área=2) |
| Independência-T | — | (não testada em 1a) | **✗ 6.0σ** |
| ρ^{(d−2)/d} | — | — | **✗ 0.827 vs 0.5** |

**Fica reportado como medido.** E a falha é INFORMATIVA: é a patologia CONHECIDA
da definição original de Dou–Sorkin em d≥3 — "count unbounded even at nonzero
discreteness scale" por links longe do canto (a não-localidade dos links CST).
Reproduzimos a doença da literatura sem saber que ela estava lá. Lição de
estimador análoga ao max_tau=15 (MEMORIA_DIAGNOSTICO): janela/condição de
localização errada dá falso sinal — aqui, falso NEGATIVO da lei de área.

### 1b. Molécula da literatura (Barton–Counsell–Dowker–Padia–Wingham–Zalel,
PRD 100, 126008 (2019)) — pós-hoc DECLARADO, estimador exato, mesmos seeds

Molécula: par p−≺p+, AMBOS em J⁻(Σ), p− fora do horizonte (u<0), p+ dentro
(u>0), e p+ é o ÚNICO elemento de J⁺(p−) dentro de J⁻(Σ).

| Check | resultado |
|---|---|
| d=3 lei de área | ✓ 0.907±0.175 |
| Independência-T d=4 / d=3 | ✓ 0.57σ / 1.61σ |
| ρ^{1/2} em d=4 | ✓ 0.456±0.079 |
| d=4 expoente (4 pontos, L=1.5–4) | 2.44±0.09 — transiente: densidade por área SUBINDO (0.30→0.53) |
| d=2 (16 seeds) | subpotenciado |

### 1c. Convergência (L maiores, seeds ×8 em d=2; critérios declarados no header)

| Check | resultado |
|---|---|
| d=4, L∈{4,5,6}: expoente | **✓ 1.845±0.082** (2±0.3); por-área converge (0.496, 0.498, 0.469; L=5 vs 6: 0.59σ) |
| d=2, 128 seeds | **✓ −0.080±0.052** (constante, com potência) |

**Coeficientes medidos (números de rede; o 1/4 fica externo, como declarado):**
a₄ ≈ 0.17, a₃ ≈ 0.23, a₂ ≈ 0.31 — fator O(1) dependente de dimensão, como o
teorema de Barton et al. prevê.

**Veredito fase 1: LEI DE ÁREA (forma) EMERGE.** Previsão do charter confirmada
nos dois lados: a FORMA deriva da contagem causal; o COEFICIENTE é externo.

## Fase 2 — matéria (gated aberto pela 1c; morte própria dispara)

Protocolo: SU(2) (setor de orientação, motor N1) no grafo de Hasse do MESMO
sprinkling d=4; MI Gaussiana entre lajes junto ao canto; controle desordenado.

### 2a. Primeira rodada: INCONCLUSIVO por dois vícios diagnosticados
(i) modo-zero de Goldstone compartilhado domina a MI (satura, slope 0.65);
(ii) controle J=0.05 deixa de ser desordenado em L=4 (m=0.45) porque o grau
médio do grafo cresce com o volume (não-localidade) ⇒ J_c(L) deriva.

### 2b. Reparo único declarado (projeção do modo-zero global + controle J=0.005)
— estimador fica VÁLIDO e o resultado é limpo:

| L | I_net (ordenado) | I_net/L² | controle |
|---|---|---|---|
| 2 | 0.0513±0.0058 | 0.0128 | 0.005±0.003 (~0) |
| 3 | 0.1983±0.0084 | 0.0220 | 0.004±0.002 (~0) |
| 4 | 0.5330±0.0761 | 0.0333 | −0.004±0.006 (~0) |

Controle < 20% em todo L ✓ (estimador válido); ESS 568–3500 ✓;
**I_net ~ L^{3.36±0.04} — SUPER-ÁREA, compatível com ∝L³ ⇒ o critério de morte
pré-registrado da fase 2 dispara.**

*Caveat declarado:* com 3 tamanhos não se exclui um transiente lento (como o da
1b→1c geométrica); mas o crescimento é forte (por-área ×2.6 de L=2→4, sem sinal
de saturação) e o mecanismo é o esperado: os links de Hasse cruzando a região
crescem ~L^{4.2} (medido na fase 1a) — a MI clássica de matéria herda a
não-localidade do grafo. Follow-up possível (L≥6, ~horas): registrado, não
executado.

## Leitura para o programa

1. **A dicotomia é nova e afiada:** GEOMETRIA (contagem de moléculas, localizada
   por relações de ordem) obedece S∝A; MATÉRIA (campo sobre os links, que são
   não-locais) NÃO obedece. No contínuo, a entropia de emaranhamento de matéria
   através de um horizonte É lei de área (com corte UV) — aqui falha PELA MESMA
   não-localidade da camada 1 do Teorema da Fronteira (⟨z⟩=∞) que já matou
   escala/criticalidade. **A tensão binária tem agora uma terceira face medida:
   conectividade (N0), dinâmica de escala (campanhas XI/B7) e AGORA entropia.**
2. **"Formas derivam" sobrevive onde a forma é da ORDEM; falha onde a forma
   exige LOCALIDADE de matéria.** Refina o escopo do princípio de N0 sem
   contradizê-lo (o princípio é cinemático sobre a ordem; a EFT de matéria sobre
   os links herda a patologia conhecida).
3. **Q10 (dualidade espaço-informação, gated por N2):** o gate abre SÓ para o
   setor geométrico (S∝A por contagem é teorema empírico interno agora); para
   matéria, fecha.
4. Lição de estimador (1a→1b) documentada; contagens ingênuas de links de
   horizonte dão falso resultado em d≥3 — usar SEMPRE moléculas BD.

## Higiene

Seeds fixas; erros SEM; fits log-log ponderados declarados; τ_int/ESS na fase 2
(reportados; ESS≥568); controle desordenado como cross-check de algoritmo
(justificativa N1 declarada no pré-registro); janelas/critérios de 1c e 2b
declarados nos headers ANTES de rodar; correções pós-hoc rotuladas como tais.
Anti-circularidade: nenhum número físico inserido (nem 1/4, nem ℓ_P); a₂,a₃,a₄
medidos. Nota operacional: fase 2b rodou em chunks foreground
(`n2_phase2b_chunk.py` + `n2_phase2b_finalize.py`) porque tarefas background
foram mortas pelo ambiente; dados idênticos (mesmos seeds).

*Reprodução:* `python n2_phase1.py` (~1 min); `python n2_phase1b.py` (~1 min);
`python n2_phase1c.py` (~1 min); fase 2: chunks + finalize (~30 min).
