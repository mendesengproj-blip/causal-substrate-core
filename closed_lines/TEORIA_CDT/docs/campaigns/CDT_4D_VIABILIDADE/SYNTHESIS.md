# SYNTHESIS — CDT_4D_VIABILIDADE: gatilho cinemático 4D (Parte B)

> **Autorizada pela morte §6 da Parte A** (`../NESS_GEOMETRIA/SYNTHESIS.md`: a geometria NESS
> reproduz a ordem mas a escala é mean-field — resolvido pela varredura x(A)). **Código:**
> `fourd_kinematic.py` (ensemble 4D stacked (1,5), reusa `rs_clustering.clustering_metrics`
> verbatim). **Dados:** `fourd_kinematic.json`, `fourd.log`. **Data:** 2026-06-29.
>
> Gatilho CINEMÁTICO BARATO (prompt Parte B §2), **não** o motor dinâmico 4D completo (esse é a
> campanha F1b-4D separada, que esta tarefa **não** constrói).

## O que foi feito (e por que é barato e correto)
Generalização do gatilho 3D (`TEIC/CDT_VIABILIDADE/cdt_kinematics.py`) para **4-simplexos
(pentatopes)**. Ensemble = **stacked (1,5)**: o move adiciona um vértice central que subdivide UM
4-simplexo em 5. Escolha deliberada: (1,5) **preserva trivialmente a 4-variedade fechada** (S⁴),
então **não precisa de validador de link-S³** — é a única classe 4D provavelmente-correta sem
construir o validador completo (a disciplina de integridade do programa: nunca forjar engine
não-validado). **Gate VERDE:** seed = ∂(5-simplex) = K6 (z=5, C_tri=1); pseudomanifold (todo
tetraedro em 2 pentatopes) + Euler χ(S⁴)=2 preservados após 200 moves; z bate a fórmula analítica
stacked z=(30+10k)/(6+k)→10.

## Resultado (1-esqueleto, ladder N=50→3200)

| N | z | C_trans | C4 |
|---|---|---|---|
| 50 | 9.40 | 0.388 | 0.273 |
| 400 | 9.93 | 0.152 | 0.119 |
| 1600 | 9.98 | 0.075 | 0.077 |
| 3200 | 9.99 | 0.065 | 0.073 |

- **Coordenação z: SATURA em ~10** (finito) — **não** diverge tipo-Poisson. ✓ (passa no eixo z)
- **Clustering: DECAI rumo ao mean-field** — C4 ~ N^**−0.33**, transitividade ~ N^**−0.45**. É o
  **oposto** do gatilho 3D flipped/DT (que SATURAVA em C4≈0.145, transitividade≈0.30, ~5× o piso
  MF, ver memória `rs-trigger-csg-coordination`). O discriminador de clustering **replica
  mean-field**.

## Veredito: **NÃO ARMADO**
Critério pré-registrado (mesma régua do Gatilho 3 3D): arma só se **z satura E o clustering satura
num valor não-trivial** (não decai). Aqui z satura mas o **clustering decai para o piso MF** → pela
regra do prompt ("se o discriminador de clustering for trivial/replicar mean-field — gatilho não
armado, registre e pare, **não construa o motor dinâmico 4D completo**") → **PARE.**

**Por que o negativo é robusto (não fraco):** stacked é o regime **Apolloniano = o MAIS
aglomerado** (cada vértice novo se cola a um K5 local). Se **até o regime mais clusterizado decai
para MF**, o regime genérico (flipped/DT) decairia **ao menos tão rápido**. Logo o NÃO ARMADO do
stacked é um limite **superior** otimista — o caso genérico é pior. Combinado com a morte MF limpa
da Parte A (3D, equilíbrio E não-equilíbrio), o padrão é consistente: **a barreira de
alta-coordenação derrota a criticalidade em 3D e 4D**.

**Ressalva honesta (registrada):** este é o regime stacked; o discriminante genérico (flipped/DT)
exige os moves (3,3)/(2,4)+(4,2) **e** o validador de link-S³ = a campanha F1b-4D completa, **não
construída aqui** (e, dado este resultado + Parte A, **não justificada**). O gatilho cinemático fez
seu trabalho: **não autoriza o investimento no motor dinâmico 4D**.

**Resumo de uma linha:** o gatilho cinemático 4D barato (ensemble stacked (1,5), provavelmente
correto, gate verde) mostra **z saturando finito (~10) mas o clustering decaindo para o mean-field**
(C4~N^−0.33, vs o 3D flipped que saturava) → **NÃO ARMADO**, e como stacked é o regime mais
aglomerado o negativo é robusto → **não construir o motor dinâmico 4D**, fechando a Parte B de
acordo com o critério do prompt.
