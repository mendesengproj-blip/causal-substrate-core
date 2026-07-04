# PRÉ-REGISTRO — Gatilho do substrato foliado anisotrópico (Hořava–Lifshitz discreto)

> # ⚠️ **ESTE SUBSTRATO NÃO É MAIS LORENTZ-INVARIANTE MANIFESTO.**
> Ele adota uma **foliação preferida** (uma noção de "agora") e usa **distância
> intra-fatia** — exatamente a troca de premissa que `SINTESE_SETE_MORTES/RESULTADO.md`
> identificou como a única saída estrutural da estrutura binária das sete mortes. Esta
> linha é a **gravidade de Hořava–Lifshitz discreta**. Qualquer resultado futuro desta
> linha DEVE carregar este rótulo em negrito no topo (condição do autorizador).

**Data:** 2026-06-30 · **Critérios travados ANTES de rodar.** Autorizado a partir do
apêndice do RESULTADO da síntese.

## 1. Substrato

Pilha de `T` fatias espaciais (tempo periódico, S¹), cada fatia = processo de Poisson de
`N_slice` pontos em `[0,L]²` (espaço d−1 = 2D). A conexão **não** usa ordem causal nem
invariante de par (`Δτ`, `s²`) — usa **distância espacial**, definida sobre a foliação:

- **Intra-fatia:** pontos `i,j` na mesma fatia conectam se `|Δx| < r_s`. A órbita
  relevante é a esfera espacial (grupo `SO(2)` **compacto**) ⇒ coordenação intra-fatia
  **finita por construção**. `r_s` escalado p/ grau-alvo `k_intra` fixo:
  `r_s = √(k_intra / (π ρ_s))`, `ρ_s = N_slice/L²`.
- **Inter-fatia (tipo-tempo):** pontos em fatias **adjacentes** (`t`,`t±1`) conectam se
  `|Δx_proj| < r_t`, com `r_t = λ·r_s`. **Parâmetro de Lifshitz `λ`** = anisotropia
  espaço×tempo. `λ→0`: fatias desacopladas; `λ~1`: ≈ isotrópico (≈ CDT).

Grafo não-direcionado; estimadores `⟨z⟩` e `C4` = `rs_clustering.clustering_metrics`
**VERBATIM**. Ladder de N (refino espacial `N_slice`, `T` fixo); varredura de `λ`.

## 2. Gates

1. **Cross-check do estimador:** `⟨z⟩ = 2E/N` (clustering_metrics VERBATIM).
2. **Frame-dependência DEMONSTRADA (não é um bug — é a premissa):** sob boost η=0.8 +
   re-foliação, `⟨z⟩`/`C4` **mudam** (Δ ≠ 0). Isto confirma honestamente que o substrato
   **não** é Lorentz-invariante — o oposto do gate das campanhas anteriores. Informativo,
   não aborta.
3. **Espaço-tempo genuíno (anti-reclassificação):** para `λ>0` a pilha deve **percolar
   no tempo** (componente gigante atravessa as `T` fatias). Se a estrutura só existir
   dentro de fatias desconexas, não é um espaço-tempo (ver §4 morte simétrica).

## 3. Medição central

Para cada `λ` e cada N do ladder: construir a pilha, medir `⟨z⟩(N)`, `C4(N)`,
transitividade (agora há triângulos, ao contrário do grafo de Hasse). Expoentes locais
`d⟨z⟩/dlnN`, `dC4/dlnN`.

## 4. Critérios de veredito (TRAVADOS)

`z_rel_thresh = 0.05`, `c4_sat_thresh = 0.02`, `c4_decay_ratio = 0.5`.

- **GATILHO ARMA:** existe `λ > 0` (espaço-tempo genuíno, gate 3) com `⟨z⟩` saturando
  (finito) **E** `C4` saturando positivo. ⇒ primeiro substrato do programa a passar as
  **duas** barreiras — **mas explicitamente às custas da invariância de Lorentz** (não é
  vitória do programa Lorentz-invariante; é a confirmação concreta de que Lorentz era a
  única obstrução).
- **MORTE SIMÉTRICA / RECLASSIFICAÇÃO:** se `C4` positivo **só** ocorre em `λ=0` (fatias
  desconexas) e colapsa para **todo** `λ>0` ⇒ não é um espaço-tempo, é uma pilha de redes
  desconexas ⇒ candidato **não** é genuíno.
- **MORTE TIPO-CDT:** se para todo `λ>0` o acoplamento tipo-tempo leva a `⟨z⟩` divergente
  ou `C4→0` (small-world/MF como CDT) ⇒ folhear não bastou.
- **AMBÍGUO:** reportar não-resolvido + N estimado. Sem forçar.

## 5. Funil

Puramente cinemático. **Ferromagneto e ξ NÃO rodam.** Se ARMAR, o passo seguinte
(testar criticalidade/ξ genuína) é o que importa de verdade — mas **pende de nova
autorização** e, novamente, sob o rótulo em negrito. Armar o gatilho cinemático aqui é
**esperado** (um grafo geométrico euclidiano de grau fixo trivialmente tem laços de
dimensão finita) — o valor está em (a) confirmar a tese da síntese e (b) mapear a
dependência em `λ` (onde o acoplamento tipo-tempo destrói, ou não, a estrutura da fatia).
