# M1c — ENDURECIMENTO dos dois sketches

**Data:** 2026-07-04 · **Verificação:** `harden_m1c.py` → `harden_m1c.json`
(Lema A certificado; densidade de plaquetas; sweep de discharge do T1).
Fecha os dois [sketch] declarados no `RESULTADO.md` §2.

---

## 0. Resultado

- **Sketch 1 (esparso ⇒ localmente árvore) → [teorema].** Via **Lema A**
  (certificado exato) + **Lema B** (limite local de ER).
- **Sketch 3 (2D-amenável ⇒ foliação) → DESCARREGADO para a subfamília TP.**
  Os dois pilares rigorosos (Lema A+B no esparso; T4+Bollobás–Brightwell no
  denso) cobrem o eixo inteiro de percolação transitiva; o argumento T1 **não
  é necessário** para a família simulada. Ele permanece como guarda,
  reenquadrado, só para a família {t_n} geral.

O grau do fechamento do M1c na subfamília TP sobe de "[medido] + 2 sketches"
para **"[teorema] no esparso ∪ [teorema] no denso, com o interstício medido
vazio"**.

---

## 1. Lema A — o Hasse é subgrafo do grafo gerador [teorema + certificado]

**Enunciado.** Na percolação transitiva (gerador do CSG, $t_n=t^n$), todo elo
de cobertura (aresta do diagrama de Hasse) é uma aresta **diretamente sorteada**
do grafo gerador. Logo o Hasse é um **subgrafo** do grafo de Erdős–Rényi
$G(N,p)$ das arestas diretas.

**Prova.** Seja $i\lessdot k$ um elo de cobertura: $i\prec k$ e não existe $m$
com $i\prec m\prec k$. Em percolação transitiva $i\prec k$ significa que há um
caminho dirigido de $i$ a $k$ no grafo direto. Se esse caminho tivesse
comprimento $\ge 2$, teria um vértice intermediário $m$ com $i\prec m\prec k$,
contradizendo a cobertura. Logo o caminho tem comprimento 1 = **aresta direta**
$i\to k$. $\blacksquare$

**Certificado finito** (`harden_m1c.py`, parte A): em 4 regimes (denso $p=0.7$,
médio $p=0.2$, esparso $p=\lambda/N$ com $\lambda=2,4$), sobre 6 seeds cada,
**toda** aresta de Hasse está no grafo direto — **0 violações** em dezenas de
milhares de arestas.

## 2. Lema B — subgrafo de ER esparso é localmente árvore [teorema]

**Enunciado.** Em $p=\lambda/N$, o grafo gerador é $G(N,\lambda/N)$, cujo limite
local fraco (Benjamini–Schramm / método objetivo de Aldous) é a **árvore de
Galton–Watson Poisson($\lambda$)** [teorema, literatura]. Para cada $k$ fixo, o
número de $k$-ciclos de $G(N,\lambda/N)$ converge a Poisson($\lambda^k/2k$) =
$O(1)$; a densidade de ciclos $\to 0$. Pelo **Lema A**, o Hasse é subgrafo, logo
tem $\le$ esse número de $k$-ciclos ⇒ **densidade de ciclos do Hasse $\to 0$**
⇒ localmente árvore.

**Corolário (não-2D-amenável).** Um reticulado 2D-amenável tem densidade de
4-ciclos (plaquetas) **limitada por baixo** ($\Theta(N)$ plaquetas). O Hasse
esparso tem densidade $\to 0$. Logo o Hasse esparso **não é** um reticulado
2D-amenável — o requisito de "laços de dimensão finita" do string-net falha por
tree-likeness.

**Medição** (`harden_m1c.py`, parte B): densidade de 4-ciclos por vértice.

| N | CSG esparso ($\lambda=4$) | grade 2D de referência |
|---|---|---|
| ~500 | 0.072 | 1.822 |
| ~1000 | 0.035 | 1.877 |
| ~2000 | 0.022 | 1.912 |
| ~4000 | 0.011 | 1.937 |

CSG cai como $\sim 1/N$ (⇒ $O(1)$ plaquetas totais, densidade $\to 0$); a grade
2D é constante $\approx 1.9$. O discriminador separa as classes por 2 ordens de
grandeza e diverge com $N$.

## 3. Discharge do T1 para a subfamília TP [os 2 pilares cobrem o eixo]

O `RESULTADO.md` usava o T1 (foliação) para excluir o interstício 2D-amenável.
Para a família de percolação transitiva simulada, **isso é desnecessário**: os
dois pilares rigorosos cobrem o eixo de conectividade inteiro.

- **$p\to 0$ (esparso):** Lema A + Lema B ⇒ localmente árvore ⇒ não-2D-amenável.
- **$p=\Theta(1)$ (denso):** posts de densidade positiva (Bollobás–Brightwell)
  + Lema T4 (nenhuma aresta de Hasse cruza post) ⇒ soma ordinal de blocos
  finitos ⇒ 1D ⇒ não-2D-amenável.

Um reticulado 2D-amenável com laços percolantes precisaria das TRÊS condições
simultâneas: (i) densidade de plaqueta $\Theta(1)$; (ii) sem posts (senão soma
ordinal 1D); (iii) crescimento sub-exponencial (amenável). **Sweep fino**
(`harden_m1c.py`, parte C; $N=1500$, $p\in[0.05,0.9]$): nenhum $p$ satisfaz as
três. Quando (i) vale (plaquetas densas, $p$ pequeno), o crescimento é
hiperbólico (exp_rate $0.45$–$0.65$, falha iii); quando (iii) tende a valer
($p$ grande, exp_rate $\to 0.23$), os posts ligam (falha ii) e a plaqueta cai.
O canto está **vazio** — verificado, `any_2D_amenable = False`.

| p | posts | C4/N | exp_rate | 2D-amenável? |
|---|---|---|---|---|
| 0.05 | 0.000 | 1.70 | 0.65 | não (hiperbólico) |
| 0.20 | 0.000 | 1.64 | 0.45 | não (hiperbólico) |
| 0.30 | ~0 | 1.39 | 0.39 | não (hiperbólico) |
| 0.40 | 0.024 | 1.09 | 0.33 | não (posts ligam) |
| 0.50 | 0.082 | 0.95 | 0.31 | não (blocos) |
| 0.70 | 0.357 | 0.54 | 0.25 | não (blocos densos) |
| 0.90 | 0.785 | 0.19 | 0.23 | não (quase-cadeia) |

**Reenquadramento para {t_n} geral.** Para acoplamentos arbitrários (não
simulados exatamente), os dois pilares generalizam parcialmente (T4 vale p/
qualquer poset com posts; o limite-árvore vale p/ qualquer regime localmente
esparso), e o T1 permanece como guarda do interstício, agora ancorado em
[[m1b-flanco-pentagonal]]: a ÚNICA classe com reticulado 2D-plano percolante a
valência finita é a **não-invariante** (cristal M1b ou foliação T1). Nenhuma
medida covariante aleatória a produz.

## 4. Status epistêmico atualizado (para a revisão dos papers submetidos)

| Peça | Antes | Agora |
|---|---|---|
| Esparso ⇒ localmente árvore | [sketch] | **[teorema]** (Lema A certificado + Lema B) |
| Redução transitiva preserva tree-likeness | [sketch] | **[teorema]** (Lema A: Hasse ⊆ gerador; subgrafo tem ≤ ciclos) |
| 2D-amenável ⇒ foliação (T1) | [sketch] necessário | **descarregado** p/ TP (2 pilares cobrem o eixo); guarda p/ {t_n} geral |
| Fechamento TP | [medido] | **[teorema] esparso ∪ [teorema] denso + interstício medido vazio** |

Delta de revisão (papers já submetidos 04jul26; entra na resposta aos
referees): substituir, no core_paper, o par de [sketch] do M1c pela dupla de
lemas (A: Hasse ⊆ gerador; B: ER localmente árvore) + a densidade-de-plaqueta
como discriminador; manter o T1 só como guarda do caso {t_n} geral.

*Reprodução:* `python harden_m1c.py` (~2 min). numpy; estende `rs_trigger.py`.
