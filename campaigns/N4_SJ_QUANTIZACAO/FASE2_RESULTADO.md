# N4 — FASE 2: RESULTADO (setor Goldstone quantizado sobre o vácuo MC real)

**Data:** 2026-07-03 · **Runner:** `n4_fase2.py` (declaração v1 f5718ec +
guarda v2, ambas pré-run) · **Dados:** `n4_fase2.json` + `n4_fase2_rows.jsonl`
(48 configs + 12 robustez ×4; L ∈ {2,3} × 4 seeds × 3 configs × {J=1.0, 0.05})
· **Custo:** 1684 s.

## 0. Veredito em uma página

**D3 NÃO disparou. P-N4-4 CONFIRMADA nas duas metades: o multipleto de
Goldstone SOBREVIVE à quantização SJ (splitting quântico ~ clássico, razão
1.1–1.3, longe do limiar 3×) E a forma relativística IR sobrevive ao fundo
térmico real (c_s = 0.843 vs c_scalar = 0.806 no MESMO substrato, Δ = 0.037
≤ 0.10). Q2-forte: nenhuma degenerescência além de flutuação — SJ NÃO cria
fibra compacta; Axioma 2 permanece postulado [DELIMITAÇÃO, como declarado].**

| Medição | Critério (congelado) | Medido | Veredito |
|---|---|---|---|
| M2.2 splitting L=2 | Δ_q > 3Δ_cl + 2σ? | Δ_q=0.285±0.030 vs Δ_cl=0.263±0.066 (razão 1.08) | NÃO excede ✅ |
| M2.2 splitting L=3 | idem | Δ_q=0.313±0.028 vs Δ_cl=0.232±0.065 (razão 1.35) | NÃO excede ✅ |
| M2.2 robustez M→4M | classificação não troca | Δ_q(×4)=0.423 < 3Δ_cl=0.70 | consistente ✅ |
| **D3** | excede em AMBOS + não-decresce | falha o "excede" nos dois L | **NÃO dispara** |
| M2.1 forma IR | \|c_s−c_scalar\| ≤ 0.10 E \|c_E2−c_E1′\| ≤ 0.10 | **0.037 e 0.029** | ✅ PASSA |
| Q2-forte | degenerescência exata? | min gap relativo 8.7e-4 (>0 sempre) | NENHUMA ✅ |
| Higiene | pares ±λ | max 1.7e-15 (60 diagonalizações) | ✅ |

## 1. A rota R-A executada (e a derivação que a corrigiu no papel)

Achado pré-run (commitado antes de rodar): para SU(2) quiral a massa
escalar-por-direção do pré-registro é IDENTICAMENTE NULA (a energia de cada
link depende só de U_xU_y†, invariante sob rotação comum dos extremos ⇒ toda
soma-de-linha escalar = 0 config a config). O objeto Gaussiano que sobrevive
é a **matriz 3×3 por sítio** — a projeção nas 3 direções de Goldstone COM a
mistura entre elas (Hessiana O(4) exata da carta transversal; fórmulas no
cabeçalho do runner). Vácuo ideal ⇒ M ≡ 0 exato ⇒ tripleto = 3 cópias da
Fase 1 — **verificado à máquina no smoke (5.2e-14)**, fechando a afirmação
analítica do pré-registro. Guarda de carta |c| ≥ 0.2: clip 0.0% no ordenado
(24/24 configs), ~25% no desordenado (o controle é assim por construção).

## 2. M2.2 — o multipleto sobrevive (D3 não dispara)

O funcional (frame-free): ocupação de direção dos K=12 modos IR do tripleto
SJ, Δ = spread dos autovalores de Λ; régua = MESMO funcional na Hessiana
clássica das MESMAS configs. Autovalores de Λ tipicamente {3.5, 4.0, 4.5}
em torno do valor degenerado 4 = K/3 — anisotropia térmica moderada, e o
quântico rastreia o clássico (razões 1.08/1.35). O limiar de morte 3× nunca
é aproximado (gaps −0.50/−0.38, ambos negativos); a robustez M→4M mantém a
classificação. Controle J=0.05: razões 1.60/1.74 e Δ_q maior — o estimador
VÊ a desordem; a ordem é o que mantém o multipleto coeso.

## 3. M2.1 — a forma relativística IR sobre o fundo real

Emenda de janela (achada NO PAPEL, pré-run): a janela da Fase 1 literal é
VAZIA em ρ=4 (4π/L = 4.19 > k_max = 2.22) ⇒ n=1 admitido com piso k_res
mantido ⇒ single-k em L=3 (k₁=2.094). Com a régua ABSOLUTA da lição Fase 1:

- c_goldstone(E2) = **0.8429 ± 0.0053** (12 configs); E1′ = 0.8141 ± 0.0056.
- c_scalar(E2) no MESMO substrato = **0.8062 ± 0.0059** (4 seeds).
- |c_s − c_scalar| = 0.037 ≤ 0.10 ✓; |E2 − E1′| = 0.029 ≤ 0.10 ✓.

O Goldstone térmico propaga como o escalar livre no mesmo substrato (leve
excesso +0.04). Nota de régua: c_scalar = 0.81 aqui vs 0.90 na Fase 1 —
substrato mais grosso (ρ=4 vs 8; discretude ρ^{−1/4} = 0.71 vs 0.59), mesma
direção do viés IR já documentado; a comparação VÁLIDA é no mesmo substrato,
que é a que o critério usa. **Contraste do controle: no desordenado
c_E2 = 0.41–0.52 — sem ordem a forma relativística DEGRADA; o vácuo ordenado
é o portador do ramo** (eco quântico do Verdict A clássico de E2/TEIC).

## 4. Q2-forte — SJ não cria estrutura interna (delimitação)

Gaps espectrais do escalar massless nos 4 substratos: min gap relativo
8.7e-4, nenhuma degenerescência exata (tol 1e-10). Como previsto na Fase 0
§3 (espectro não-degenerado q.c. ⇒ estabilizador = U(1)^K abeliano): **a
construção SJ sobre (C, ≺) puro não cria fibra compacta não-abeliana; o
multipleto vem do G interno postulado — Axioma 2 permanece postulado.**
[DELIMITAÇÃO declarada, não morte.] D-Q0 quieta em toda a campanha (nenhum
observável ímpar-sob-conjugação fixável apareceu).

## 5. Higiene MC e notas de instrumento

- τ_int(m) máx 16.6 sweeps; espaçamento 200 sweeps ⇒ configs separadas por
  ~12 τ — descorrelacionadas (N-hig 1 ✓). m = 0.94–0.97 (J=1, ordenado
  profundo); 0.03–0.09 (J=0.05).
- Correção fina à declaração (sem efeito em critério): esperávamos ~6
  zero-modos exatos de o(4) na Hessiana térmica; n_zeros = 0 medido, e a
  razão é exata — em ponto NÃO-crítico o termo (∇E)·(curvatura da órbita)
  não some, então órbitas de simetria não são zero-modos de H. A regra de
  exclusão declarada fica (apenas não dispara).
- R-B (Hessiana de Hasse nativa): NÃO rodada, como declarado (pré-reg:
  diagnóstico opcional, não critério).

## 6. Estado do funil — CAMPANHA N4 COMPLETA

```
Fase 0 ✅ (Q0 teorema) → Gate G ✅ 4/4 → Fase 1 ✅ (Q1: D1/D2 não)
  → Fase 3 ✅ (Q3: SUB_AREA, localização resgatada/expoente do corte)
  → Fase 2 ✅ ESTA SESSÃO (Q2-fraca: multipleto sobrevive, D3 não;
     Q2-forte: sem fibra = delimitação)
```

Q0–Q3 todas respondidas. NENHUMA das 6 mortes pré-registradas disparou.
Consolidação da campanha: `RESULTADO.md`; deltas do paper-núcleo lá.
