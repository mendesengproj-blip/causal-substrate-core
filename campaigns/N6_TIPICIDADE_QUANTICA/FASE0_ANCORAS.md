# N6 — FASE 0: âncoras conferidas NA FONTE

**Data:** 2026-07-04 · **Pasta:** `FRONTEIRA_COMPACTA/N6_TIPICIDADE_QUANTICA/`
**Antecedente:** M10 (levantamento; bloqueio deliberado em 5 âncoras citadas de
memória). **Método:** busca e leitura das fontes primárias (disciplina N4-Fase-0).
**Desfecho: 5/5 CONFIRMADAS + 1 revisão de prior achada na fonte (§3).**

---

## 1. As âncoras, conferidas

**A1 — Transição de fase no MCMC de 2D-orders com ação BD. ✅ CONFIRMADA.**
Surya, *Evidence for a Phase Transition in 2D Causal Set Quantum Gravity*
(arXiv:1110.6244, 2011): transição entre **fase contínua** e **fase cristalina**,
caracterizada por observáveis covariantes; parâmetro de não-localidade
ε ∈ (0,1]; β_c^{-1} decresce com ε; *"the continuum phase survives the analytic
continuation"*. Review de Glaser, *Computer Simulations of Causal Sets*
(arXiv:2306.09904, 2023), consolida: **fase random** (ordering fraction ~0.5,
altura ~10, manifold-like) vs **fase cristalina** (of ~0.6, **altura ~3**,
layered); transição de **1ª ordem** (coexistência em histogramas + coeficiente
de Binder); **β_c(N,ε) = 1.66(±0.03)/(N ε²)**; N simulados 30–90 (até 120 com
Ising); continuação analítica **e^{iβS} → e^{−β̃S}** (β→iβ̃). Também confirmado
o objeto: **2D-order = interseção de DUAS ordens lineares (par de permutações
U,V; e_i ≺ e_j ⟺ u_i<u_j E v_i<v_j)** — o exemplar canônico é o sprinkling de
uma caixa de M².

**A2 — Supressão dos posets Kleitman–Rothschild pela ação. ✅ CONFIRMADA.**
O review (2306.09904) afirma: os KR orders (3 camadas, N/4–N/2–N/4) **dominam
entropicamente** a medida uniforme ("the most likely partial orders of the size
of the universe are clearly KR orders"), MAS *"the integral over KR orders is
suppressed by actions for which the number of links is the leading term, as is
the case for most causal set actions"*. O fato central do levantamento — **o
peso da ação MOVE a tipicidade** — está na fonte. (Atribuição exata do teorema
de supressão [Loomis–Surya] a reconferir no full-text na execução; o FATO está
ancorado no review.)

**A3 — Observáveis covariantes / stem sets na CSG. ✅ CONFIRMADA.**
Os observáveis covariantes dos modelos de percolação generalizada são
completamente caracterizados por **stem sets** (Brightwell–Dowker–García–
Henson–Sorkin, *Observables in causal set cosmology* gr-qc/0210061 +
*extended percolation* gr-qc/0504069); dinâmica manifestamente covariante via
**covtree** (Dowker–Zalel, arXiv:2008.02607; capítulo *Covariant Growth
Dynamics*, Springer Handbook, Zalel). Posts são eventos-tronco — covariantes,
como o lema C2 precisa.

**A4 — Número esperado de posts em ordem de grafo aleatório. ✅ CONFIRMADA.**
Bombelli–Seggev–Watson, *A Computation of the Expected Number of Posts in a
Finite Random Graph Order* (arXiv:0809.2258, 2008): expressão para o número
médio de posts, **assintoticamente linear em n** (densidade positiva), erro
decrescente; cita Alon et al. [ABBJ 1994] — consistente com o que M1c usou. A
COMPLEXIFICAÇÃO (t ∈ ℂ na medida quantal) é o passo NOVO do lema C2, não
coberto pela literatura conferida — como esperado.

**A5 — Medida quantal / funcional de decoerência de Sorkin. ✅ CONFIRMADA.**
Framework padrão: μ(A) = D(A,A) do funcional de decoerência; não-aditiva
(termo de interferência); em CST *"one quantises the classical covariant
probability space by simply replacing the classical probability with a quantum
measure"* (linha de QFT-em-causet em forma de histórias; Sorkin e sucessores).
Confirma o papel de C1 no levantamento: moldura, sem dinâmica canônica.

## 2. O que as fontes acrescentaram ao desenho (instrumento)

- **Amostrador:** par de permutações (U,V) com moves locais; ação BD-2D com
  smearing ε; pesos e^{−β̃S} (continuação declarada).
- **Gate de engenharia OBJETIVO:** reproduzir **β_c(N,ε)=1.66(3)/(Nε²)** e as
  assinaturas de 1ª ordem (coexistência bimodal; Binder), mais os valores-
  -de-fase do review (of ~0.5 vs ~0.6; altura ~10 vs ~3) nos N publicados.
- **Custo:** N=30–120 tem precedente publicado; sweeps O(N²). Campanha MODERADA.

## 3. REVISÃO DE PRIOR (achada na fonte; honestidade pré-congelamento)

Duas constatações mudam o prior do levantamento:

1. **A fase cristalina tem ALTURA ~3** (nos parâmetros do review) — é um
   layered ACHATADO tipo-KR (camadas densas com ~N/altura elementos), NÃO um
   reticulado graduado alto. Camadas densas ⟹ valência de Hasse ~O(N) entre
   camadas consecutivas ⟹ **a fase cristalina provavelmente FALHA SNA-1
   (valência finita)** — não é o cristal-E1 de M1b.
2. **A fase random é essencialmente o box-order** (2D-order de caixa de M²) —
   que a bateria M5 JÁ mediu: valência cresce, não-SNA (falha SNA-1 por T3).

**Prior atualizado (era ~"aberto" no levantamento): D2 (nenhuma fase é SNA ⟹
checklist quântico-robusta no regime continuado) sobe para ~75%; D1 (fase
cristalina SNA = escape dinâmico) cai para ~15%; inconclusivo ~10%.** A
medição DECISIVA e genuinamente nova é a bateria dentro da fase CRISTALINA
(e através da transição); a fase random entra como controle ancorado em M5.
Registrado ANTES do pré-registro congelar (precedente N4: update de prior da
Fase 0, 50/50 → 60/40, declarado e nunca pós-ajustado).

## 4. Ressalva de instrumento (declarada antes do congelamento)

Os N com precedente (30–120) são PEQUENOS para os expoentes de bola da bateria
M5 (que usou N~10³–10⁴). O pré-registro portanto congela: discriminadores
PRIMÁRIOS em N pequeno = **escala da valência de Hasse com N** (série
N∈{30,50,70,90,120}), **densidade de plaquetas C4/N**, **perfil de
altura/camadas** e **posts**; os expoentes de crescimento de bola (SNA-2) só
como secundários com R adaptativo, INCONCLUSIVO-por-resolução declarável.

## Fontes

- arXiv:1110.6244 (Surya 2011) · arXiv:2306.09904 (Glaser 2023, review)
- gr-qc/0210061, gr-qc/0504069 (observáveis/stem sets) · arXiv:2008.02607
  (covtree, Dowker–Zalel) · Springer Handbook, *Covariant Growth Dynamics* (Zalel)
- arXiv:0809.2258 (Bombelli–Seggev–Watson 2008, posts)
- Sorkin, quantum measure theory (linha de histórias; múltiplas fontes
  secundárias conferidas, e.g. arXiv:2306.04800 §histories)
