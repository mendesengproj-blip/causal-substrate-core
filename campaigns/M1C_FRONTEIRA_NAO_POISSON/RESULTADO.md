# M1c — FRONTEIRA NÃO-POISSON: RESULTADO

**Data:** 2026-07-04 · **Pré-registro:** `PRE_REGISTRO.md` (e9a3fa3, com
declaração de não-cegueira §2) · **Gate:** `gate_m1c.py` → `gate_m1c.json`
(gerador VALIDADO por formas fechadas de TP; 9 famílias de acoplamento) ·
**Natureza:** medição (sweep) + teorema (o entregável).

---

## 0. Veredito em uma página

**A FRONTEIRA NÃO-POISSON FECHA. Nenhum substrato de crescimento sequencial
covariante (CSG) oferece valência finita + laços percolantes de dimensão
finita.** O sweep é CLOSURE-consistent em todas as 9 famílias, e revela que o
fechamento NÃO é por divergência de valência (a valência de Hasse frequentemente
SATURA na CSG) mas por uma **dicotomia geométrica** ao longo do eixo de
conectividade:

| Regime | Mecanismo de fechamento | Assinatura medida |
|---|---|---|
| **Denso** (p≳0.5) | posts densos ⇒ soma ordinal de blocos finitos (Lema T4) | poly≈1 (crescimento 1D), max-block-frac → 0 |
| **Esparso / valência finita** (p=λ/N, p≲0.3) | limite local = árvore de Galton–Watson ⇒ **hiperbólico** | exp-rate ≥ 0.35 (crescimento exponencial de bola) |

Os dois regimes se encontram num crossover (p≈0.3–0.4) e cobrem o eixo. O
**reticulado 2D-plano amenável** que um string-net exige (crescimento polinomial
de dimensão 2 + laços percolantes) **nunca aparece** — `amenable_2d = False` em
TODAS as famílias. Ele é o fio-da-navalha folheado (T1), medida-zero na família
covariante, porque exige uma grade global que o crescimento covariante — onde
cada nascimento vê só o passado NÃO-rotulado — não pode alinhar.

**Ponte com [[m1b-flanco-pentagonal]]:** o reticulado 2D-plano com laços
percolantes a valência finita existe SÓ na classe **não-invariante**
(o cristal E1 de M1b, ou a foliação de T1) — **nunca em qualquer medida
invariante/covariante aleatória.** O flanco nº 1 da [[rs-trigger-csg-coordination]]
está fechado; resta só o flanco nº 2 (geometria genuinamente não-Markoviana).

---

## 1. O sweep (gate_m1c.json; N=1000 nas medições pesadas)

| Família | p | ⟨z⟩_Hasse | post_dens | max_blk_frac | rank/N | exp_rate | poly | veredito |
|---|---|---|---|---|---|---|---|---|
| A_dense_p0.70 | 0.70 | 2.63 (finita) | **0.383** | 0.052 (N2k) | 0.31 | 0.25 | 0.94 | posts ⇒ **1D blocos** |
| A_dense_p0.50 | 0.50 | 3.19 (finita) | 0.089 | 0.092 | 0.60 | 0.29 | 1.08 | posts ⇒ **1D blocos** |
| K_edge_p0.40 | 0.40 | 3.60 (finita) | 0.020 | 0.225→0.111 | 0.80 | 0.33 | 1.23 | crossover → 1D (borderline) |
| K_edge_p0.30 | 0.30 | 4.07 (finita) | ~0.002 | 0.702 | 1.04 | 0.39 | 1.46 | **hiperbólico** (onset) |
| M_fixed_p0.10 | 0.10 | 5.96 (satura) | 0 | 1.0 | 1.93 | 0.55 | 2.09* | **hiperbólico** |
| B_scaled_lam2 | λ/N | 1.97 (finita) | 0 | 1.0 | 0.15 | 0.69 | 2.49* | **hiperbólico/frag.** |
| B_scaled_lam4 | λ/N | 3.92 (finita) | 0 | 1.0 | 0.98 | 0.95 | 3.52* | **hiperbólico** |
| B_scaled_lam8 | λ/N | 7.09 (cresce) | 0 | 1.0 | 2.34 | 0.76 | 2.96* | hiperbólico/divergente |
| C_dust | →0 | 0.01 | 0 | — | 0 | — | — | antichain trivial |

`*` poly > 2 nas famílias esparsas é **artefato do crescimento exponencial**
na janela pequena de R (não é dimensão): sob bola exponencial o ajuste log-log
infla. O discriminador correto é **exp_rate**: ≥ 0.35 ⇒ hiperbólico (não
amenável). O teste `amenable_2d` exige exp_rate < 0.35 **E** poly ∈ [1.6, 2.4]
simultaneamente — as únicas famílias com exp_rate baixo (0.25–0.33) têm poly ≈ 1
(blocos 1D), e as com poly ≈ 2 têm exp_rate alto (hiperbólico). **A interseção
é vazia.**

**Sanidade (Lema 0 de M1):** transitividade = 0.0000 em todas — o Hasse não tem
triângulos, confirmado. **Âncora de retrodição:** C4 sub-mean-field / árvore-like
no regime esparso reproduz o platô medido da campanha CSG anterior.

## 2. O teorema (o entregável) — fechamento por dicotomia geométrica

**Enunciado (CSG covariante, subfamília de percolação transitiva + escala
λ/N).** O diagrama de Hasse de uma CSG de Rideout–Sorkin nunca realiza um
reticulado 2D-amenável com laços percolantes de dimensão finita. Ao longo do
eixo de conectividade:

**(1) Regime denso — 1D por posts.** [teorema, dado o anexo]
Densidade positiva de posts (Bollobás–Brightwell, para a ordem de grafo
aleatório = TP) + o **Lema T4** (nenhuma aresta de Hasse cruza um post;
[teorema], M1) ⇒ o Hasse é soma ordinal de blocos finitos ⇒ crescimento
polinomial de dimensão 1 e ciclos block-locais (não percolam). Medido:
poly ≈ 0.9–1.1, max-block-frac → 0 (0.13→0.09→0.05 em p=0.5).

**(2) Regime esparso / valência finita — hiperbólico por árvore.** [sketch;
2 pilares citados]
Em p = λ/N o grafo de relações diretas é Erdős–Rényi G(N, λ/N), cujo limite
local fraco (Benjamini–Schramm / método objetivo de Aldous) é a **árvore de
Galton–Watson Poisson(λ)** [teorema, literatura]. A redução transitiva (Hasse)
remove apenas cordas sobre caminhos de comprimento ≥ 2, preservando a
tree-likeness local (girth → ∞) [sketch]. Logo o crescimento de bola é
exponencial (hiperbólico), não polinomial-de-dimensão-2. Medido: exp_rate
0.55–0.95, fragmentação em componentes no subcrítico.

**(3) O canto proibido — 2D-amenável exige foliação.** [sketch]
Um reticulado 2D-amenável com laços percolantes é gerado por plaquetas
(quadrados) ⇒ por **T1** (M1) carrega uma graduação ⇒ foliação intrínseca ⇒
quebra a covariância (cada nascimento veria uma grade global rotulada). A CSG
covariante não pode alinhar-se a ela. O canto é medida-zero na família.

**Conclusão.** (1)∪(2) cobrem o eixo; (3) exclui o interstício. A fronteira
não-Poisson fecha na sua realização canônica.

**Grau epistêmico honesto (ATUALIZADO 04jul26 — ver `HARDENING.md`):** os dois
sketches foram ENDURECIDOS. O sketch (2) virou **[teorema]** via o **Lema A**
(certificado: o Hasse é subgrafo do grafo gerador ER — 0 violações) + **Lema B**
(subgrafo de ER esparso é localmente árvore; densidade de plaqueta → 0 vs grade
2D constante). O sketch (3)/T1 foi **descarregado para a subfamília TP**: os dois
pilares rigorosos (Lema A+B no esparso; T4+Bollobás–Brightwell no denso) cobrem
o eixo inteiro, e o sweep fino confirma o interstício 2D-amenável VAZIO — o T1 só
permanece como guarda do caso {t_n} geral. **Fechamento TP = [teorema] esparso ∪
[teorema] denso + interstício medido vazio.**

## 3. O que a conjectura pré-registrada acertou e errou (honestidade)

- **Prior de fechamento: CONFIRMADO.** Nenhuma descoberta; o canto post-suprimido
  é vazio (de laços 2D), como suspeitado na §2 do pré-registro.
- **D-M1c-2 DISPAROU parcialmente (previsto):** no regime de valência finita os
  **posts DESAPARECEM** (post_dens = 0 em todo λ/N e p ≤ 0.1) — a conjectura
  "posts de densidade positiva para toda CSG de valência finita" é **FALSA**.
  T4 é o mecanismo do regime DENSO, não do de valência finita. MAS o fechamento
  é resgatado pela **hiperbolicidade** (limite-árvore) — exatamente o mecanismo
  (b) da declaração de não-cegueira. Consequência: o texto de T4 no core_paper
  precisa da ressalva "posts = mecanismo do regime denso; o regime de valência
  finita fecha por tree-likeness local".
- **Refinamento não-antecipado:** a valência de Hasse SATURA numa faixa ampla
  (p=0.1–0.2, λ/N pequeno) — a "divergência de boost" NÃO é a barreira dominante
  na CSG (ela satura). O peso todo recai no requisito 2 (laços de dimensão
  finita), e é aí que a covariância morde: hiperbólico ou 1D, nunca 2D-plano.

## 4. O que muda no programa

1. **Flanco não-Poisson (nº 1) FECHADO** na realização canônica CSG. O
   core_paper "How to break" rota (ii) e a Table item — o único flanco genuíno
   restante passa a ser **geometria genuinamente não-Markoviana / fora-do-
   -equilíbrio** (flanco nº 2), estritamente mais estreito.
2. **Unificação com M1b e T1** (delta conceitual forte para a revisão): laços
   2D-planos percolantes a valência finita ⟺ classe NÃO-invariante (cristal
   M1b **ou** foliação T1). Toda medida invariante/covariante é: divergente
   (Poisson, camada 1) **ou** hiperbólica/1D-bloco (CSG, M1c). Uma frase fecha
   as três classes.
3. **Ressalva no T4:** posts governam o regime denso; o regime de valência
   finita fecha por tree-likeness (não por posts).

## 5. O que M1c NÃO reivindica (escopo)

- Simulei a subfamília de **percolação transitiva** ($t_n=t^n$) + a escala
  $p=\lambda/N$ — que já cobre valência-finita, denso, e o crossover. A
  família {t_n} GERAL (acoplamentos arbitrários) NÃO foi simulada exatamente
  (amostrador exato é exponencial); a extensão a todo {t_n} repousa nos DOIS
  pilares gerais (Lema T4 vale p/ qualquer poset com posts; limite-árvore vale
  p/ qualquer regime localmente esparso), não em medição. Declarado.
- **Geometria genuinamente não-Markoviana** (integral de caminho CDT com
  métrica flutuante; medidas com memória) permanece flanco SEPARADO (core_paper
  itens 9–10; flanco nº 2).
- Nada sobre condensação dinâmica de string-net mesmo se o substrato existisse.
- Anti-circularidade: só p adimensional + ordem de nascimento; nenhuma métrica.

*Reprodução:* `python gate_m1c.py` (~90 s). numpy; estende
`rs_trigger.py` (gerador+estimador byte-idênticos); seeds fixas.
