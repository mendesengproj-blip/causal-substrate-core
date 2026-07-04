# PRÉ-REGISTRO — Gatilho cinemático da repulsão Lorentz-invariante

**Data:** 2026-06-30 · **Diretório:** `REPULSAO_LORENTZ/campaigns/GATILHO_REPULSAO/`
**Natureza:** gatilho cinemático barato (⟨z⟩ + C4), sem ferromagneto, sem ξ.
**Critérios travados ANTES de rodar a medição central** (o gate pode rodar antes; ele
não decide o veredito). Não se ajustam critérios após ver os dados.

---

## 1. O substrato (a única novidade)

Processo de ponto **repulsivo** sobre Minkowski 2+1D, em vez do sprinkling de
Poisson independente. Afinamento tipo **Matérn II** no único invariante de par de
Lorentz, o intervalo `s²_ij = Δt² − |Δx|²`:

- Candidatos: Poisson `sprinkle_box(ρ_cand)` (VERBATIM).
- Marca `u_i ~ U(0,1)` por candidato (chaveada por **identidade**).
- Região de exclusão invariante: `{j : |s²_ij| < r0²}`, `r0 = α · ρ_cand^(−1/d)`.
- Retém `i` sse `u_i` é a menor marca em sua região de exclusão (hard-core: dois
  retidos nunca a `|s²| < r0²` ⇒ `g(Δτ)=0` em curto alcance ⇒ correlação negativa).
- Grafo medido: **cobertura causal (Hasse)** sobre o conjunto **retido** — o mesmo
  observável do controle de Poisson da `RIDEOUT_SORKIN_CLUSTERING`.

Parâmetro de repulsão `α` (= raio do hard-core em unidades de discretude),
varrido em **`{0.0, 0.1, 0.2, 0.3}`**. `α=0` ⇒ sem exclusão ⇒ **Poisson puro**
(a baseline mean-field conhecida, embutida como controle interno).

> **Limite estrutural de α (registrado, não ajuste pós-hoc):** a região de exclusão
> invariante é uma **banda ao redor do cone de luz**, de volume `V_excl ~ r0²·L`
> (não `~r0^d`) — a não-compacidade do cone. Logo `p_ret` colapsa rápido (`α=0.3`
> ⇒ `p_ret≈0.26`; `α=0.5` ⇒ `≈0.12`; `α=1.0` ⇒ `≈0.03`) e a densidade retida
> atinge teto. Acima de `α≈0.3` o processo é degenerado (retém quase nada / domínio
> de borda). **Que a repulsão Lorentz-invariante seja estruturalmente não-local é,
> ele próprio, um resultado** — registrado aqui antes da medição, não inferido dela.
> O scan de `α` cobre a faixa em que o substrato é bem-definido.

Estimadores `⟨z⟩` e `C4` = `rs_clustering.clustering_metrics` importado **VERBATIM**.
Ladder sobre **N retido** `{400, 800, 1500, 2500}` (densidade de candidatos ajustada
por `α` para atingir o N retido alvo; N retido **real** é medido e reportado, e os
expoentes locais usam `N_mean`).

## 2. Gates (precondições, não opcionais) — todos devem passar

1. **Repulsão ativa:** `0.05 < p_ret < 0.99` (o afinamento de fato remove eventos).
2. **Hard-core invariante:** nenhum par retido com `|s²| < r0²`.
3. **Correlação negativa:** `g(Δτ) < 0.8` em curto alcance **e** `→1` (0.7–1.4) em
   longo alcance. Se `g ≥ 1` em toda parte: não é repulsão, aborta (charter §2.3).
4. **Cross-check do estimador:** `⟨z⟩ = 2E/N` (clustering_metrics VERBATIM).
5. **Invariância de Lorentz (charter §2.2):** sob boost `η=0.8`, o conjunto retido,
   as arestas de cobertura, e `⟨z⟩`/`C4` devem ser **bit-idênticos**. Se não:
   dependência de referencial ⇒ a campanha para.

> **Status (rodado 2026-06-30): GATE VERDE (8/8).** p_ret=0.26; min|s²|=r0² (hard-core
> exato); g_curto=0.74, g_longo=0.95; ⟨z⟩=2E/N a 1e-9; sob boost simdif=0, ⟨z⟩/C4
> idênticos. (`validation_gate.json`.)

## 3. Medição central

Para cada `α` e cada N retido do ladder: gerar o conjunto repulsivo, o grafo de
cobertura, medir `⟨z⟩(N)` e `C4(N)` (média sobre seeds, SEM). Expoentes locais
`d⟨z⟩/d ln N` e `d C4/d ln N` entre rungs consecutivos, foco no topo.

## 4. Comparabilidade

Mesmo estimador, mesma família de ladder, mesma dimensão (2+1D) e caixa
(`T=1, L=3`) da campanha de percolação de longo alcance. Sobreposição direta com
as referências das campanhas anteriores (Poisson, CSG, CDT-2D) no mesmo gráfico.

## 5. Critérios de veredito (TRAVADOS — idênticos à linhagem)

Limiares: `z_rel_thresh = 0.05` (saturação relativa de ⟨z⟩), `c4_sat_thresh = 0.02`
(C4 positivo), `c4_decay_ratio = 0.5` (não-decaimento de C4).

- **GATILHO ARMADO** — existe `α` com **ambas**:
  - ⟨z⟩ satura: `|d⟨z⟩/dlnN| / z_top < 0.05` **e** expoente local não-crescente; **E**
  - C4 satura positivo: `C4_top > 0.02` **e** `C4_top ≥ 0.5 · C4_first` (não decai).
  ⇒ Primeiro substrato causal a passar as **duas** barreiras cinemáticas. Justifica
  rodar o ferromagneto da TEIC em cima (tarefa FUTURA, não esta).

- **MORTE LIMPA** — em **todo** `α`: ⟨z⟩ diverge como Poisson (a repulsão não reduz a
  coordenação efetiva) **OU** C4 decai a zero (a repulsão não cria clustering real).

- **RESULTADO INFORMATIVO (mesmo sendo morte)** — se ⟨z⟩ satura mas C4 não, ou
  vice-versa: registrar **qual** barreira falhou e por quê, como dado novo que
  estreita a conjectura de impossibilidade.

- **AMBÍGUO** — reportar como não resolvido, com o N necessário estimado para
  resolver. **Sem forçar veredito.**

## 6. Funil (trava de disciplina)

Esta tarefa é **puramente cinemática**. Ferromagneto e ξ **não** rodam aqui. Só se
o veredito for GATILHO ARMADO uma campanha completa se justifica (ver
`../../O_QUE_BUSCAMOS.md`). Se for MORTE, a linha fecha como as anteriores.
