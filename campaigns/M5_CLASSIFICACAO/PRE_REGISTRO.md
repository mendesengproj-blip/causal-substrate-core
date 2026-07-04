# M5 — TEOREMA DE CLASSIFICAÇÃO: pré-registro (congelado ANTES do código)

**Data:** 2026-07-04 · **Pasta:** `FRONTEIRA_COMPACTA/M5_CLASSIFICACAO/`
**Natureza:** SÍNTESE analítica (o entregável é um teorema de decisão) + gate =
bateria computacional unificada. **O capstone da Linha 1.**
**Antecedentes:** camada 1 (core_paper), T1–T4 (M1), M1b (flanco pentagonal
construído), M1c (fronteira não-Poisson), BHS.

---

## 1. A pergunta

M1b, M1c e T1 provaram peças separadas. Juntas elas implicam uma frase que
nenhuma prova sozinha, e que é o legado formal do programa:

> **Um substrato causal pode ser "string-net-admissível" (SNA) — valência
> finita + reticulado 2D-amenável + laços percolantes de dimensão finita — se e
> somente se for NÃO-invariante** (cristal determinístico ou foliação graduada).
> Toda medida Lorentz-invariante OU covariante-aleatória falha SNA: é divergente
> (Poisson, camada 1), hiperbólica, ou 1D-confinada por blocos.

A tese central é que **a fronteira SNA coincide exatamente com a fronteira de
invariância.** Isto formaliza "decidir, antes de simular, o que um substrato de
dada simetria pode carregar" — numa TABELA DE DECISÃO (classe × estrutura →
permitido/proibido) com backing de teorema.

## 2. A propriedade SNA (definição congelada)

Um substrato (poset localmente finito com diagrama de Hasse $H$) é
**string-net-admissível** se satisfaz as TRÊS (os requisitos de Wen/Levin-Wen,
[[m1b-flanco-pentagonal]] §1):
- **(SNA-1) valência finita:** ⟨z⟩_Hasse limitada (não cresce com N).
- **(SNA-2) reticulado 2D-amenável:** crescimento de bola polinomial de
  dimensão ≈2 (exp_rate → 0, poly ≈ 2) — laços de DIMENSÃO FINITA, não
  hiperbólicos.
- **(SNA-3) laços percolantes:** densidade de plaquetas (4-ciclos) limitada por
  baixo (Θ(N), não → 0) e cobertura do espaço de ciclos.

## 3. A tese (dois enunciados)

- **(T-exclusão) SNA ⟹ ¬invariante.** Nenhum substrato Lorentz-invariante nem
  covariante-aleatório é SNA. Montagem:
  - Poisson invariante (camada 1): ⟨z⟩=∞ — falha SNA-1 [teorema].
  - CSG covariante (M1c): valência finita possível, mas hiperbólico OU 1D-bloco
    — falha SNA-2 ou SNA-3 [teorema esparso ∪ denso].
  - Exchangeable (T2) / box-order embutido (T3): sem Hasse localmente finito /
    valência log-divergente — falha SNA-1 [teorema].
  - Foliado quadrado-gerado (T1): SNA possível MAS graduado ⇒ foliação ⇒
    ¬invariante [teorema].
- **(T-realizabilidade) SNA é habitada na classe não-invariante.** O cristal
  E1 de M1b (ℤ², 5 geradores) é SNA e determinístico (¬invariante por BHS)
  [construção certificada].

## 4. Kill-criteria (o que derrubaria a classificação)

- **D-M5-1 (a descoberta):** um substrato Lorentz-invariante OU covariante-
  aleatório que passe SNA-1∧SNA-2∧SNA-3 na bateria ⇒ a fronteira SNA NÃO
  coincide com a de invariância ⇒ o teorema-bandeira do programa (no-photon) tem
  contraexemplo. Reabriria todo o edifício. (Prior: NÃO existe — é a soma dos
  fechamentos já provados.)
- **D-M5-2 (montagem falha):** alguma classe de invariância NÃO coberta pelas
  peças (camada1/T1–T4/M1c) ⇒ a classificação tem buraco; declarar a classe
  faltante como fronteira, não reivindicar iff.
- Regra: SNA-1/2/3 com janelas FROZEN (§6); nenhuma redefinição pós-dado.

## 5. O gate = bateria unificada (a "uma figura que prova a tabela")

`gate_m5.py`: a MESMA bateria de medições (reusada de M1c: ⟨z⟩, exp_rate, poly,
plaqueta C4/N, densidade de posts, componentes) aplicada a UM representante de
CADA classe de substrato, mais o rótulo de invariância (input teórico, não
medido):

| Classe | Representante | Invariante? |
|---|---|---|
| Poisson (camada 1) | sprinkling M² (ou proxy de valência) | SIM |
| CSG esparso | percolação transitiva p=λ/N | covariante |
| CSG denso | percolação transitiva p=0.7 | covariante |
| exchangeable | ordem aleatória uniforme (proxy) | SIM |
| box-order | dominância 2D iid | SIM (embutido) |
| **cristal M1b E1** | ℤ² 5-geradores (reusa gate_m1b) | **NÃO** |
| **foliado** | reticulado quadrado graduado | **NÃO** |

**Saída:** tabela (classe → SNA-1?, SNA-2?, SNA-3?, SNA global, invariante?).
**Predição congelada:** SNA=True **somente** nas duas linhas não-invariantes
(cristal E1; foliado). Todas as linhas invariantes/covariantes: SNA=False.

## 6. Janelas FROZEN (herdadas de M1c, para comparabilidade)

- SNA-1 (valência finita): ⟨z⟩ estável em N (slope d⟨z⟩/dlnN < 0.3) e ≤ 30.
- SNA-2 (2D-amenável): exp_rate < 0.35 **E** poly ∈ [1.6, 2.4].
- SNA-3 (plaquetas percolantes): C4/N não-decrescente em N e > 0.3.
- SNA global = SNA-1 ∧ SNA-2 ∧ SNA-3.

## 7. Desfechos pré-declarados

- **Predição confirmada** (prior): SNA ⟺ ¬invariante na bateria ⇒ escrever o
  teorema de classificação; a tabela de decisão vira o resultado central do
  capstone. Delta de revisão para o core_paper (unifica M1b+M1c+T1 numa frase).
- **D-M5-1** dispara: contraexemplo invariante SNA — a maior reviravolta
  possível; investigar antes de qualquer reivindicação.
- **D-M5-2** dispara: classe não coberta — declarar como fronteira.

## 8. O que M5 NÃO reivindica (escopo)

- É uma SÍNTESE das peças já provadas + realizabilidade; a novidade é a
  DEFINIÇÃO de SNA e o enunciado iff, não novos mecanismos.
- A direção (⟸) é "SNA é habitada na classe não-invariante" (existência via
  E1), NÃO "todo substrato não-invariante é SNA" (dust não é).
- Cobre as classes de invariância NOMEADAS (Poisson/exchangeable/growth/box +
  não-invariante crística/foliada); geometria genuinamente não-Markoviana fica
  fora (flanco vivo separado, item de escopo).
- Anti-circularidade: os representantes usam só combinatória/ordem; o rótulo
  "invariante?" é fato teórico (BHS, definição), não medido.
