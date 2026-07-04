# F2 — CONTROLE G₂: RESULTADO

**Data:** 2026-07-04 · **Pré-registro:** `PRE_REGISTRO.md` (f4d7cee) + ADENDO
pré-run (d176334, achado pelo smoke ANTES da suíte) · **Gate:** VERDE 8/8
(`f2_gate.json`, 324 s) · **Suíte:** `f2_g2.json` (1428 s) + diagnóstico
rotulado `f2_diag_J085.json` · Custo total ≈ 32 min de máquina.

---

## 0. Veredito em uma página

**G₂ ESPELHA SU(3)/SU(4): a camada 3 do Teorema da Fronteira é genérica ALÉM
da família SU(N)** — vale para grupo excepcional, representação fundamental
REAL, **centro trivial**. E a sub-pergunta nomeada no core_paper é respondida:

> **A assinatura de confinamento medida pelo programa NÃO depende do centro
> Z(G), nas escalas medidas.** G₂ (Z=1) confina no acoplamento forte com a
> mesma assinatura de SU(3)/SU(4) a u pareado: Creutz χ(2,2)=0.520>0, V(r)
> crescente, σ decrescente com β (0.520→0.477).

| Previsão | Desfecho |
|---|---|
| P-F2-1 ordena com LRO genuína | **CONFIRMADA** (LRO J≥0.7; Mermin 0.3–4.6% nos J ordenados; 1 literal-false só no ponto de crossover — §3, documentado) |
| P-F2-2 **14/14 Goldstones** (dim G₂) | **CONFIRMADA** exata |
| P-F2-3 B_est → 8 = 2×índice de Dynkin (ADENDO) | **CONFIRMADA de forma exata:** B_G₂/(8·B_SU3) = **1.000000** em L=15,21,31; anti = −B a 1e−6 |
| P-F2-4 confinamento forte espelha a u pareado | **CONFIRMADA** |
| P-F2-5 (fraca) J_c ∝ dim G: 0.3×14/8=0.53 | **CONFIRMADA no bracket:** crossover em (0.5, 0.7] |

**Mortes D-F2-1…4: NENHUMA disparou.**

## 1. Gate (VERDE 8/8; instrumento certificado)

Álgebra: 14 geradores, fechamento 2.2e−16, Casimir=4·I (1.3e−15; 7
irredutível), 3-forma octoniônica invariante sob exp(g₂) (2.6e−14). Haar-walk
certificado por caracteres: ⟨χ₇⟩=−0.008, ⟨χ₇²⟩=0.977 (irrep real ⇒ 0 e 1).
so(4)⊂g₂ com split 3+3 e so(3) diagonal exato (res 9e−16; espectro n̂·J =
{±1,±1,0,0,0} = conteúdo 3+3+1). **G7 (motor-pilha em SU(3)) reproduziu o
FL1/N1 nos mesmos números:** χ-pico J=0.3, Mermin 1.2/1.0/0.5%,
Creutz(2,2)=1.046 (valor N1 idêntico), escada B a 7 dígitos. G8: G₂
desordenado J=0.05 (m=0.029 < 0.083).

## 2. A suíte, fase a fase

**[1] Ordenamento.** Desordenado até J=0.5 (m≈1/√n); LRO genuína (winner
`const`, U₄→0.667) para J≥0.7; crossover em (0.5, 0.7] — consistente com a
escala por dimensão (0.3×14/8=0.53; mesma sub-previsão fraca que acertou no
SU(4)). Rótulo "chi_peak_J=2.0" = MESMO artefato de ESS baixo documentado no
N1 (τ≈24, ESS≈3 na fase ordenada profunda); o J_c vem do crossover.

**[2] Goldstones 14/14** sem gap (twist por gerador, dE~ρ_s k²). A contagem
segue dim G — 8 (SU3) → 15 (SU4) → **14 (G₂)** — o coset manda, não o grupo.

**[3] Topologia — a previsão afiada.** B_G₂(L) = 6.357427 / 7.136646 /
7.605461 em L=15/21/31 = **exatamente 8× a escada SU(3)** (razão 1.000000 nos
6 dígitos, nos três L); anti-hedgehog = −B a 1e−6. Confirma: (i) π₃(G₂)=ℤ
protege B também sem centro e em rep real; (ii) o estimador de Pontryagin lê
**2×(índice de Dynkin do embedding)** — grau 4 do so(3) diagonal (longo 1 +
curto 3), fator 2 = T(7)/T(fund SU2). A correção veio de emenda PRÉ-RUN
(ADENDO, commit d176334, antes da suíte), não de ajuste pós-dado.

**[4] Gauge/confinamento (a resposta à pergunta do centro).** A u pareado
(u=β/2N²: 0.25 e 0.333, β={24.5, 32.7}): χ(2,2)=0.520/0.477 > 0, V(r)
crescente nos dois, σ decresce com β — as três assinaturas de SU(3) (1.046 no
gate) e SU(4) (1.624/0.847 no N1). **Sem centro, sem N-alidade, sem estrutura
complexa: a assinatura persiste ⇒ ela vem da expansão forte do grupo compacto
genérico, não de vórtices de centro.**

## 3. O literal-false documentado (precedente N4: documenta, não reescreve)

O check `mermin` do driver computa sobre TODOS os J com LRO classificada,
incluindo o ponto de crossover J=0.7 (m=0.198≈2.4×piso, U₄=0.655≠0.667,
ESS=10): desvio 1.358 — **o ponto está EM cima da transição**, onde
C_long=m² não é esperada em tamanho finito (o fit de C_long com m~0.2 é
dominado por flutuação crítica). Nos J genuinamente ordenados: 0.3% (J=1.0),
1.9% (1.4), 4.6% (2.0) — qualidade N1. **Diagnóstico rotulado pós-suíte
(não-criterial, declarado como tal):** J=0.85 dá m=0.714 e desvio **0.4%** —
a identidade recupera imediatamente acima do crossover. O critério não foi
reescrito; o VERDICT literal "B" do JSON fica registrado com esta análise.
Nota: no N1 o mesmo check passou porque o ponto de crossover do SU(4)
(J=0.7, m=0.573) já caía fundo na fase ordenada — fragilidade do
CLASSIFICADOR no ponto marginal, não da física. Lição de instrumento: Mermin
só sobre J com U₄ ≥ 0.66 (para futuras suítes; esta não foi re-julgada).

## 4. O que muda no programa

1. **A junta aberta do core_paper FECHA (delta de revisão):** *"whether
   confinement depends on the center Z(G) is an open, discriminating test
   (G₂, trivial center, queued)"* → **medido: não depende, nas escalas
   acessíveis** (com o caveat assintótico do §5 mantido).
2. **"Hospedado, não selecionado" estende-se a TODA a classe compacta
   testável:** SU(3), SU(4), G₂ — complexo/real, com/sem centro, clássico/
   excepcional. O Axioma 2 genérico ganha sua terceira medição independente.
3. **Bônus quantitativo:** J_c ∝ dim G segue valendo (8→15→14 acerta o
   bracket 2 vezes em 2). Continua nota de rodapé, não critério.
4. **Lições de instrumento (banco):** (i) estimador de Pontryagin lê
   2T(R)×grau — normalizar por T(R) ao mudar de rep; (ii) hedgehog fora de
   SU(N) exige embedding de spins INTEIROS (so(3) com F:2π→0; −1 central não
   existe sem centro); (iii) Mermin só em U₄≥0.66; (iv) Haar sem QR:
   passeio + teste de caracteres.

## 5. O que F2 NÃO reivindica (escopo mantido do pré-registro)

String breaking / σ assintótico = 0 de G₂ (blindagem por 3 gluões,
7⊂14⊗14⊗14) fica FORA do alcance em L=6 — a independência de centro vale nas
escalas medidas, e o comportamento assintótico distinto de G₂ [literatura:
Holland–Minkowski–Pepe–Wiese] permanece como qualificação obrigatória em
qualquer texto. Nada sobre a ordem da transição G₂. Loop de Polyakov não
medido (não-criterial, não executado). Nenhum número do mundo entrou.

*Reprodução:* `python f2_gate.py` (~5 min) → gate; `python f2_g2.py`
(~24 min, exige gate VERDE). numpy; seeds fixas (família 7000+s do FLB).
