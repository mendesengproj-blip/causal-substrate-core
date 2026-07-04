# M5 — TEOREMA DE CLASSIFICAÇÃO: RESULTADO (o capstone da Linha 1)

**Data:** 2026-07-04 · **Pré-registro:** `PRE_REGISTRO.md` (16e8306) ·
**Gate:** `gate_m5.py` → `gate_m5.json` (bateria unificada; emenda de instrumento
documentada §4) · **Natureza:** síntese analítica + tabela de decisão empírica.

---

## 0. Veredito em uma página

**A FRONTEIRA STRING-NET COINCIDE COM A FRONTEIRA DE INVARIÂNCIA.** Um substrato
causal é string-net-admissível (SNA = valência finita + reticulado 2D-amenável +
laços percolantes) **se e somente se for NÃO-invariante** (cristal determinístico
ou foliação graduada). Toda medida Lorentz-invariante ou covariante-aleatória
falha SNA — cada uma por um mecanismo já provado. A bateria unificada põe um
representante de cada classe no MESMO eixo e o confirma: SNA=True **exatamente**
nas duas linhas não-invariantes, sem contraexemplo (D-M5-1 não disparou).

Isto formaliza o legado do programa numa frase e numa tabela: **decide-se, antes
de qualquer simulação, o que um substrato de dada simetria pode carregar.**

## 1. A tabela de decisão (gate_m5.json)

| Classe | Invariante? | ⟨z⟩ | posts | exp_rate | poly | C4/N | SNA-1 | SNA-2 | SNA-3 | **SNA** |
|---|---|---|---|---|---|---|:-:|:-:|:-:|:-:|
| Poisson M² | SIM (Lorentz) | 11 (↑N) | 0 | 0.69 | 2.70 | 29.6 | ✗ | ✗ | ✓ | **não** |
| box-order 2D | SIM (embutida) | 11 (↑N) | 0 | 0.82 | 2.81 | 29 | ✗ | ✗ | ✓ | **não** |
| CSG esparso | covariante | 3.9 | 0 | 0.66 | 3.32 | 0.02 | ✓ | ✗ | ✗ | **não** |
| CSG denso | covariante | 2.7 | 0.35 | 0.14 | 0.99 | 0.56 | ✓ | ✗ | ✓ | **não** |
| exchangeable | SIM | — | — | — | — | — | ✗ | ✗ | ✗ | **não** [T2] |
| **cristal E1 (M1b)** | **NÃO (BHS)** | 9.6 | 0 | 0.27 | 1.93 | 18.4 | ✓ | ✓ | ✓ | **SIM** |
| **reticulado foliado** | **NÃO (T1)** | 4.0 | 0 | 0.25 | 1.76 | 1.95 | ✓ | ✓ | ✓ | **SIM** |

Cada exclusão tem o mecanismo certo: Poisson/box falham **SNA-1** (valência
diverge — camada 1 / T3); CSG esparso falha **SNA-3** (C4/N≈0 — hiperbólico
tree-like, M1c); CSG denso falha **SNA-2** (poly≈1, posts — 1D-bloco, M1c/T4);
exchangeable falha **SNA-1** [T2]. Sanidade: transitividade=0 (Hasse sem
triângulos) em todas.

## 2. O teorema (montado)

**Definição (SNA).** Um poset localmente finito é *string-net-admissível* se seu
Hasse tem (1) valência finita, (2) crescimento de bola polinomial de dimensão
≈2 (amenável), (3) densidade de plaquetas Θ(N) percolante — os três requisitos
de Levin–Wen.

**Teorema de classificação.**
- **(Exclusão) SNA ⟹ ¬invariante.** Nenhum substrato Lorentz-invariante nem
  covariante-aleatório é SNA. [Montagem de peças provadas:]
  - Poisson invariante ⟹ ⟨z⟩=∞ (camada 1, Campbell–Mecke no hiperbolóide) —
    falha (1). [teorema]
  - Exchangeable ⟹ sem Hasse localmente finito (T2). [teorema]
  - Box-order/embutido ⟹ valência log-divergente (T3). [teorema]
  - CSG covariante ⟹ hiperbólico (limite Galton–Watson; falha 2/3) OU 1D-bloco
    (posts + Lema T4; falha 2). [teorema esparso ∪ denso, M1c + `HARDENING.md`]
- **(Realizabilidade) SNA é habitada na classe não-invariante.** O cristal E1
  (ℤ², M1b) e o reticulado quadrado foliado são SNA; ambos ¬invariantes (BHS:
  nenhum cristal é Lorentz-invariante; T1: quadrado-gerado ⟹ graduado ⟹
  foliação). [construção certificada, M1b + T1]

**Corolário (a fronteira de decisão).** A fronteira SNA **coincide** com a
fronteira de invariância. Equivalente: um fóton/laço-percolante emergente num
substrato causal exige quebrar a invariância — não há rota invariante.

## 3. Por que isto é o capstone (e o que é genuinamente novo)

As PEÇAS já existiam (camada 1; T1–T4; M1b; M1c). O que M5 adiciona:
1. **A definição SNA** como propriedade única de substrato (unifica os 3
   requisitos de Wen num predicado testável).
2. **O enunciado iff** — que a fronteira SNA É a fronteira de invariância —
   nenhuma peça isolada o dizia.
3. **A tabela de decisão empírica unificada** — a "uma figura que prova o
   teorema": todas as classes no mesmo eixo de medição, SNA=True só nas
   não-invariantes.

Para os papers submetidos (delta de revisão): substituir as referências
dispersas (camada 1 / T1–T4 / M1b / M1c) por **um teorema de classificação +
uma tabela**. É a frase mais citável do programa depois do binário original.

## 4. Emenda de instrumento (documentada, precedente N4/F2)

O smoke revelou (ANTES do run decisivo) que R_MAX=6 (herdado de M1c) era pequeno
demais para o `exp_rate` resolver a log-concavidade de V~R²: reticulados 2D
genuínos davam exp_rate≈0.5 em R=6 (falso negativo de SNA-2). Verificado no
sweep de R que exp_rate cai monotonicamente para reticulados (foliado
0.46→0.20; cristal 0.40→0.21 em R=6..20) e permanece >0.6 para hiperbólico em
qualquer R. **Correção:** medir amenabilidade no maior R viável (adaptativo até
R_TARGET=15) em reticulados grandes. **A janela FÍSICA (exp_rate<0.35, poly∈
[1.6,2.4]) ficou INALTERADA** — só o parâmetro de resolução mudou. Trilha no
código (comentário + `robust_ball`).

## 5. O que M5 NÃO reivindica (escopo)

- É SÍNTESE + realizabilidade; a novidade é a definição SNA + o iff + a tabela,
  não novos mecanismos (as exclusões são teoremas já provados/citados).
- A direção (⟸) é "SNA é HABITADA na classe não-invariante" (existência via E1
  e foliado), NÃO "todo não-invariante é SNA" (dust não é).
- Cobre as classes de invariância NOMEADAS. **Geometria genuinamente
  não-Markoviana** (fora do crescimento sequencial) fica fora — é o único flanco
  vivo restante (escopo: [[direcao-pos-fechamento]] item 2).
- Anti-circularidade: representantes usam só ordem/combinatória; o rótulo
  "invariante?" é fato teórico (BHS, definição, T1), não medido.

*Reprodução:* `python gate_m5.py` (~2 min). numpy; reusa `gate_m1c.py`,
`rs_trigger.py`, e o cristal E1 de M1b.
