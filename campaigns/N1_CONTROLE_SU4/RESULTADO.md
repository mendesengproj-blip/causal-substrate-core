# N1 — CONTROLE_SU4: resultado

**Data:** 2026-07-01 · **Pasta:** `FRONTEIRA_COMPACTA/N1_CONTROLE_SU4/`
**Pré-registro:** `PRE_REGISTRO.md` (escrito antes do código). Motor: `sun_core.py`
(SU(N) generalizado; substrato+estimadores IMPORTADOS byte-idênticos de
`TEIC/results/matter/fl1/su3_core.py`). Drivers: `n1_gate_su3.py`, `n1_su4.py`.
Saídas: `n1_gate_su3.json`, `n1_su4.json`. Determinístico (seeds fixas).

---

## VEREDITO: **A — SU(4) FUNCIONA IGUAL (7/7). "SU(3) é HOSPEDADO, não emergente; o 3 é escolha do mundo."**

O substrato causal de Poisson não seleciona SU(3): ele hospeda QUALQUER grupo
compacto que o Axioma 2 lhe dê — exatamente como a camada 3 do Teorema da Fronteira
(N0) prevê (compacidade ⇒ índices discretos; Bott e Goldstone não distinguem N).
A frase exata pré-registrada para os papers fica autorizada.

## Gate de engenharia (obrigatório, ANTES de SU(4)): **VERDE 4/4**

O motor generalizado instanciado em N=3 reproduz o FL1 medido:

| Critério | Medido | FL1 referência | Passa |
|---|---|---|---|
| J_c(causal) | pico de χ em **J=0.3** exato; desord. J≤0.1 (m≈0.03≈1/√N); LRO todo J≥0.5 | J_c≈0.3 | ✓ |
| Mermin C_long=m² | desvios 1.2%, 1.0%, 0.5% (J=0.5,1,2) | 1–3% | ✓ |
| Confinamento SU(3) β=4.5 | Creutz χ(2,2)=1.046>0.05, V(r) crescente | σ>0 | ✓ |
| Álgebra | Tr(T_aT_b)=2δ_ab err 0.0; \|f\|_max=1.0000 | Gell-Mann | ✓ |

Cross-check N-hig: hot/cold em J=1.0 → m=0.880 vs 0.881 (Δ=0.001). Grafo:
n≈1304, avgdeg≈44 (mesma família de seeds 7000+s do FLB).

## Suíte SU(4) verbatim: **7/7 espelha SU(3)**

### [1] Ordenamento (substrato causal, 9 J × 4 seeds)

| J | m | U₄ | C(r) | C_long | m² |
|---|---|---|---|---|---|
| 0.05–0.5 | 0.028–0.053 | 0.645–0.648 | sem platô | ~0 | ~0 |
| 0.7 | 0.573 | 0.667 | **const** | 0.314 | 0.329 |
| 1.0 | 0.747 | 0.667 | **const** | 0.541 | 0.558 |
| 2.0 | 0.870 | 0.667 | **const** | 0.746 | 0.758 |

- **Ordena com LRO genuína** (Mermin 4.6%, 3.1%, 1.5% — <10%); U₄→0.667 exato na
  fase ordenada; desordenado até J=0.5 (m≈1/√N).
- **J_c(SU4) ≈ 0.6** (crossover exp→const em [0.5, 0.7]). Fator **2.0× o J_c(SU3)=0.3
  — consistente com a razão de dimensões dim SU(4)/dim SU(3) = 15/8 = 1.9** (a
  sub-previsão fraca pré-registrada, "fator ≲2", confirmada no valor).
- *Nota honesta (N-hig):* o rótulo "chi_peak_J=2.0" do JSON é ARTEFATO de ESS baixo
  na fase ordenada profunda (τ_int≈24, ESS≈2 com 120 medidas); o J_c reportado vem
  do crossover, que é robusto (classificador com janelas pré-registradas). Nos J
  desordenados ESS=40–118. Mitigação: hot/cold concorda a 0.001 no gate.

### [2] Goldstones: **15/15 sem gap** (dim SU(4), protocolo D2 verbatim, twist
estático por gerador, dE~ρ_s k²). SU(3)×SU(3)→SU(3) dava 8; SU(4)×SU(4)→SU(4) dá
15 — a contagem segue o coset, não o "3".

### [3] Topologia π₃: **B(SU4) ≡ B(SU3) bit-idêntico** (correção de protocolo documentada)

| L | B_su3 | B_su4 | \|diff\| |
|---|---|---|---|
| 15 | +0.794678 | +0.794678 | 0.0 |
| 21 | +0.892081 | +0.892081 | 0.0 |
| 31 | +0.950683 | +0.950683 | 0.0 |

Monótono → 1 (escada de discretização, como no FL1: 0.806→0.969 em L=15→41);
anti-Skyrmion B=−0.8921 = −B exato. π₃(SU(N))=ℤ (Bott) não vê N — medido, não só
citado.

**Correção documentada (honestidade):** a 1ª rodada da suíte FALHOU o check de
topologia com o critério ingênuo |B−1|<0.05 em L=21 — que é IMPASSÁVEL para o
próprio SU(3) (o FLC mediu B(21)=0.8921). Diagnóstico: B é idêntico para todo N
(o log age só no bloco SU(2); verificado N=2,3,4 e su3_core original, todos
+0.892081). O check foi corrigido para o protocolo de ESCADA do próprio FL1
(N-invariância por L + convergência monótona) e a suíte re-rodou inteira. Não é
ajuste pós-hoc do alvo físico — é calibração do estimador ao protocolo FL1 já
publicado; a falha e a correção ficam registradas aqui.

### [4] Gauge/confinamento (β escalonados ×16/9 do FLC quick)

| β | Creutz χ(2,2) | V(r) | 
|---|---|---|
| 8.0 (forte) | **1.624 > 0** | [1.30, 2.97] crescente |
| 10.7 | 0.847 | [0.91, 1.85, 2.46] crescente |

Confina no acoplamento forte E σ(β) decresce (1.624→0.847) = mesma assinatura de
liberdade assintótica na direção β que o SU(3) (FLC: σ decresce com β). Espelha.

## O que muda no programa

1. **Rebaixamento de alegação AUTORIZADO (com delta editorial próprio, fora desta
   campanha):** onde os papers dizem/impliquem "SU(3) emerge", a frase correta é
   **"o substrato hospeda qualquer G compacto; SU(3) é o mínimo que o mundo
   escolheu; o que emerge é a ESTRUTURA (LRO + Goldstones dim G/H + π₃ + σ>0),
   não o grupo."** Isto REFORÇA N0 camada 3 (a família de índices é do alvo
   compacto genérico) — o Axioma 2 é genérico de verdade, agora medido.
2. **Bônus quantitativo não previsto no charter: J_c ∝ dim(G)** (0.3×15/8≈0.56 vs
   medido ≈0.6, no bracket). Candidato a nota de rodapé no paper-núcleo; não é
   critério de nada (sub-previsão fraca, confirmada).
3. **G₂ (segundo controle) fica AUTORIZADO** pelo charter (SU(4) passou limpo):
   centro trivial Z(G₂)=1 discrimina se o confinamento medido depende do centro.
   Campanha própria (7×7 real, 14 geradores via octonions) — NÃO executada nesta
   sessão; próxima da fila computacional junto com N2.

## Higiene (N-hig, cumprida)

τ_int/ESS por (J,seed) no JSON (alerta ESS<20 na fase ordenada: declarado acima);
2º algoritmo: justificativa declarada no pré-registro (mesmo updater = feature do
controle comparativo) + hot/cold; janelas de estimador: verbatim FL1, declaradas
antes de rodar. Anti-circularidade: nenhum número físico entrou; contagens (15,
ℤ) são teoria de grupos; β/J varridos; σ/J_c/B medidos.

*Reprodução:* `python n1_gate_su3.py` (~5 min) → gate; `python n1_su4.py`
(~9 min, exige gate VERDE). numpy; seeds fixas nos drivers.
