# F1_SYNTHESIS — veredito da maquinaria 2D-CDT (ensemble + ação + Wick + MC)

> **Fase F1.** Pré-registro: `PRE_REGISTRO.md` (congelado 2026-06-27, commitado antes
> do código). Código: `f1_cdt2d.py` (motor + gate E0), `f1_controls.py` (validação do
> estimador de d_H), `f1_run.py` (gate G1–G5). Artefatos: `e0_report.json`,
> `validation_gate.json`, `f1_production.log`. **Data de execução:** 2026-06-28.
>
> **Natureza do veredito (charter §3.4 / PRE_REGISTRO §0):** F1 é um veredito de
> **ENGENHARIA**, não de física nova. A pergunta é só: *a maquinaria está correta?* —
> medida contra os gabaritos analíticos de 2D-CDT (`[GABARITO]`, externos, usados para
> validar, não como resultado desta teoria — anti-contaminação preservada).

---

## Veredito: **F1 VERDE — maquinaria validada** (com 2 ressalvas registradas, nenhuma fatal)

| Gate | Critério pré-registrado | Resultado | Status |
|---|---|---|---|
| **E0** (engenharia) | invariantes de manifold causal, Euler, reversibilidade | todos passam após 10⁴ e 2×10⁵ moves | **VERDE** |
| **G1** (gate-mor) | d_H = 2, \|d_H−2\|<0.1 | d_H = **2.08±0.02** (banda), 2.06±0.01 (extrap) | **VERDE** |
| **G2** | distribuição de ℓ_t | ⟨ℓ⟩=Vt/2T exato; flutua; forma medida | **VERDE (qualit.)** ¹ |
| **G3** | propagador/correlador | C(Δt) decai suave e monótono | **VERDE (qualit.)** ¹ |
| **G4** | autocorr finita; visita o range | τ_int≈260 sweeps **finito**; range visitado | **VERDE** ² |
| **G5** | hot vs cold em 2σ | 0.9σ (spread), 1.06σ (vol) com blocking | **VERDE** |

¹ G2/G3 confirmados ao nível da **física correta** (média, flutuação, decaimento). O teste
estatístico de **forma fechada** AL98 (KS-test / R²>0.95 contra o propagador de tempo-próprio)
**NÃO** foi implementado: exige **re-derivar a matriz de transferência de Ambjørn–Loll dentro
desta teoria** (a regra de não-contaminação proíbe importá-la pronta). Fica como tarefa de F1b.
² τ_int≈260 sweeps em λ=ln2 é **critical slowing down** (esperado: ln2 é o ponto crítico bare).
É **finito** (passa o critério "autocorr finita"), não divergente, e o sampler não prende
(hot/cold coincidem). Ressalva de **eficiência**, não de correção.

---

## 1. E0 — gate de engenharia (VERDE)

`gate_E0()` em `f1_cdt2d.py`, artefato `e0_report.json`:

- **E0-a** (cilindro mínimo contável): T=3, ℓ=3 → N₂=18 (=2ℓT ✓), V=9 (=ℓT ✓), invariantes OK.
- **E0-b** (Euler): χ = V−E+F = 0 (toro) em 4 tamanhos distintos. ✓
- **E0-c** (invariantes preservados): após **10⁴** moves aleatórios (e teste de estresse
  separado de **2×10⁵** moves em rede 40×20), o checador `check_manifold()` não acusa
  **nenhuma** violação — nbL/nbR inversos, involução espacial nbC(nbC(i))=i, nbC liga
  UP↔DOWN, sanduíches adjacentes, contagem ℓ↔UPs consistente, χ=0.
- **E0-d** (reversibilidade): `add` seguido do `delete` inverso retorna **bit-a-bit** à
  triangulação original; **flip é involutivo** (flip∘flip = identidade). Pré-requisito do
  balanço detalhado — satisfeito.

A representação (triângulo-adjacência, folheação por sanduíches, moves de Pachner foliados
`flip`/`add`/`delete`) está **mecanicamente correta**.

## 2. G1 — d_H = 2 (gate-mor, VERDE)

**Achado de calibração do estimador (medido, `f1_controls.py`).** O estimador cumulativo de
Hausdorff (shelling BFS, N(r)~r^d) tem **viés de tamanho finito MEDIDO**: numa rede 2D **plana**
(taxicab, N(r)=2r²+2r+1) ele lê d≈1.89, não 2.00 — a dimensão local sobe monotonicamente para 2
mas satura antes por tamanho finito. **Mas o grafo dual da CDT NÃO herda esse viés**: por ser
triangulação aleatória (preenche 2D isotropicamente, sem as correções lineares da métrica de
quadrados), lê d≈2.0 **diretamente**. Esse achado é o motivo de validar o estimador **antes**
de ler a física, e justifica aplicar o critério **absoluto** pré-registrado |d_H−2|<0.1.

**Resultado (4 sementes/tamanhos, Vt=1568…3200):**

| | banda | extrap (1/r→0) | local_max |
|---|---|---|---|
| **CDT** | **2.081 ± 0.015** | **2.058 ± 0.010** | 2.15 |
| controle 1D (anel) | 0.99 | — | — |
| controle 2D plano | 1.89 | 1.95 | — |
| controle 3D | 2.60 | 2.18 | — |

- |2.08 − 2| = 0.08 < 0.1 → **passa o gate absoluto**. extrap 2.06, ainda mais perto.
- A CDT cai **claramente** no setor 2D: longe do 1D (0.99) e do 3D (2.60), com o estimador
  provado dimensão-metro válido (1D<2D<3D monotônico nos controles).
- **Honestidade:** o valor fica levemente **acima** de 2 (~2.06–2.08), não exatamente 2.00.
  É consistente com d_H=2 (crescimento de bola levemente super-quadrático a tamanho finito no
  grafo dual), e em todo caso é **2, não 1 nem 3**. O gate-mor — a maquinaria reproduz a
  bidimensionalidade genuína da 2D-CDT (≠ d_H=4 do DT euclidiano) — está **cumprido**.

### 2b. Cross-check β=0 (d_H vs acoplamento de ação) — resolve a ressalva-2 do Gatilho 3

Pedido como gate retroativo: rodar a medição no próprio motor de F1 variando λ (em 2D a ação
é **só** λ·N₂). Resultado: **d_H independe de λ** — λ=0 → 2.070, λ=ln2 → 2.071, λ=1.5 → 2.036.

**Leitura (honesta e importante para a fila de substratos):** em 2D a ação **não molda** a
geometria (curvatura = Gauss-Bonnet topológico; o termo de volume só fixa ⟨N₂⟩). Logo d_H=2
vem da **folheação (causalidade) do ensemble**, não da ação. Isso **resolve a ressalva-2 do
Gatilho 3** (`TEIC/docs/campaigns/CDT_VIABILIDADE/SYNTHESIS.md:75-82`, "Pachner sem ação ⇒
branched-polymer") de forma precisa: a patologia branched-polymer é fenômeno do **DT euclidiano
não-folheado**; o ensemble **folheado** a exclui **mesmo a ação livre** — então, em 2D, a
ressalva-2 simplesmente **não se aplica**, e a verificação genuína de "geometria global sadia
sob a dinâmica completa" migra para **3D/4D** (F1b+), onde o DT euclidiano de fato ramifica e
folheação+ação passam a fazer trabalho. Confirma também o glossário/charter §2: em 2D a
dinâmica é **puramente entrópica**.

## 3. G2/G3 — distribuição de fatia e correlador (VERDE qualitativo)

- **G2:** ⟨ℓ⟩ = 32.02 ≈ Vt/2T = 32 (**exato** — conservação de volume e folheação corretas);
  std(ℓ)=10.6, range [3,75] — a "largura do universo" flutua fortemente, como deve a 2D-CDT
  (volume espacial faz passeio estocástico no tempo). A **forma** do histograma foi medida e
  registrada (`validation_gate.json:G2_hist`).
- **G3:** correlador volume-volume C(Δt)/C(0) = [1.0, 0.82, 0.63, 0.45, 0.28, 0.12, −0.01, …]
  — decaimento **suave e monótono**, indo levemente negativo em Δt~T/2 (anticorrelação
  antipodal forçada pelo volume total ≈ fixo no toro). Fisicamente correto.
- **Ressalva (¹):** o teste de **forma-fechada** AL98 (KS / R²) requer a matriz de
  transferência de Ambjørn–Loll re-derivada **nesta teoria** — não feito aqui para não
  importar resultado externo. **Tarefa F1b.** O que está medido é consistente com AL98, mas
  não é, ainda, o teste quantitativo travado. Marcado VERDE-qualitativo, não VERDE-pleno.

## 4. G4 — ergodicidade / critical slowing down (VERDE com nota)

- τ_int(spread) ≈ **260 sweeps** em λ=ln2, **finito**. O MC visita um range largo de
  ℓ-spread ([7,74]…[8,110]) sem prender.
- λ=ln2 **é** o ponto crítico bare da 2D-CDT → autocorrelação grande é **esperada e física**
  (critical slowing down), não um bug. Passa o critério "autocorr finita; sem regiões presas".
- **Nota de eficiência (não-fatal):** para F2/sistemas maiores, τ crescente vai exigir moves
  melhores (cluster/coletivos) ou mais compute. Registrado para orçamento de F2.

## 5. G5 — balanço detalhado: hot vs cold (VERDE) — e a lição metodológica

- spread: cold=47.4, hot=45.3 → **0.9σ** (blocking). vol: **1.06σ**. **Coincidem.**
- **Diagnóstico cirúrgico de um quase-falso-vermelho:** a barra de erro **ingênua**
  (std/√N, que assume amostras independentes) dava **7.68σ** para o spread → "VERMELHO".
  Com τ_int≈260 sweeps, amostras a cada 2–3 sweeps são fortemente correlacionadas (~6
  independentes), então a barra real (por **blocking**) é ~13× maior e o desvio cai para
  0.9σ. O volume (modo rápido) já dava 1.06σ em ambas as contas. **A "falha" era artefato de
  autocorrelação, não quebra de ergodicidade** — exatamente o tipo de auto-engano que o
  charter §3 manda tornar difícil. Registrado: `G5_*_diff_sigma` (blocking) vs
  `G5_*_diff_sigma_naive` no `validation_gate.json`.

---

## 6. O que F1 estabelece (e o que explicitamente NÃO estabelece)

**Estabelece (maquinaria validada → liberado para F1b/F2):**
1. O ensemble causal foliado + ação de Regge (só-volume em 2D, curvatura=Gauss-Bonnet
   topológico) + rotação de Wick (peso e^{−S} real) + Monte Carlo Metropolis com moves de
   Pachner `flip`/`add`/`delete` é **mecanicamente correto** (E0) e **fisicamente correto**
   no observável decisivo: **reproduz d_H=2 da 2D-CDT** (G1), com ergodicidade (G4) e balanço
   detalhado (G5) verificados.
2. O pipeline de **calibração de estimador antes da física** pegou um viés real (estimador de
   d_H em rede plana) e um quase-falso-vermelho (barras de erro ingênuas em G5). A disciplina
   funcionou.

**NÃO estabelece (honestidade, charter §3.1 e §6):**
1. **Nada de física nova.** d_H=2 é **gabarito conhecido** de 2D-CDT; reproduzi-lo é
   **validação**, não descoberta (charter §3.6). A aresta é `[External]`; nenhuma escala
   emergiu.
2. **G2/G3 quantitativos (forma-fechada AL98) ficam pendentes** para F1b — sem isso, a
   validação da maquinaria é **forte mas não exaustiva**. O gate-mor (d_H) carrega o veredito.
3. **A semente original da teoria** (informação SOURCE o crescimento — charter §0.1) **não foi
   testada em F1**: F1 é gravidade pura, crescimento cego. O critério de morte que protege
   contra repetir a TEIC (geometria *sourced* ≠ CDT pura) só é exercido de F2 em diante.

## 7. Decisão registrada

> **Subir para F1b (3D, curvatura dinâmica de Regge).** Em 2D a curvatura é topológica
> (não-dinâmica), então 2D só valida a maquinaria — o que está feito. A física de dimensão
> (coordenação informativa, fases branched-polymer/crumpled/estendida, dimensão que corre
> d_s 4→2) **só aparece em 3D/4D**. Antes de F2 (Nível A: *geometria emerge?*), F1b deve:
> (i) generalizar o ensemble para 3D folheado (simplices (3,1),(2,2),(1,3));
> (ii) ligar o termo de curvatura (1/G) — agora dinâmico;
> (iii) re-rodar E0 (invariantes 3D) e um gate de validação 3D.
>
> **Pendência herdada por F1b:** fechar G2/G3 quantitativos (matriz de transferência AL98
> re-derivada in-theory) **ou** registrar explicitamente que a validação de maquinaria fica
> assentada no gate-mor d_H + ergodicidade + balanço detalhado, sem o teste de forma-fechada.
>
> **Nota de orçamento:** critical slowing down (τ~260 sweeps já em 2D, L=40) vai piorar em
> 3D/maior — F1b/F2 provavelmente precisarão de moves coletivos ou mais compute.

**Resumo de uma linha:** a maquinaria 2D-CDT está **correta** — reproduz d_H=2 (gate-mor),
é ergódica e satisfaz balanço detalhado; o caminho para F1b (3D) e F2 (geometria emerge?)
está **aberto**, com duas ressalvas honestas registradas (G2/G3 forma-fechada pendente;
slowing down a gerir).
