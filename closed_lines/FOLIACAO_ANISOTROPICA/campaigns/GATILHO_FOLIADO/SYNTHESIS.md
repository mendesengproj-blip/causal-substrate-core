# SÍNTESE — Gatilho do substrato foliado anisotrópico

> # ⚠️ **ESTE SUBSTRATO NÃO É MAIS LORENTZ-INVARIANTE MANIFESTO.**
> Adota foliação preferida + distância intra-fatia (gravidade de Hořava–Lifshitz
> discreta). O resultado abaixo **não é uma vitória do programa Lorentz-invariante** —
> é a confirmação concreta de que a invariância de Lorentz era a **única** obstrução.

**Data:** 2026-06-30 · `FOLIACAO_ANISOTROPICA/campaigns/GATILHO_FOLIADO/`
**VEREDITO: `GATILHO_ARMA`** (espaço-tempo foliado genuíno; ambas as barreiras passam).

---

## 1. O que foi testado

O apêndice de `SINTESE_SETE_MORTES/RESULTADO.md` identificou a **única saída estrutural**
da estrutura binária das sete mortes: uma quantidade de conexão com **órbita compacta**,
o que força **distância intra-fatia** sobre uma **foliação preferida** (grupo espacial
`SO(2)` compacto, em vez do boost não-compacto). Substrato:

- `T=8` fatias 2D (tempo S¹), cada uma Poisson em `[0,L]²` (`L=4`).
- **Intra-fatia:** `|Δx| < r_s`, `r_s` escalado a grau-alvo `k_intra=6` fixo (RGG 2D).
- **Inter-fatia** (adjacente): `|Δx| < r_t = λ·r_s`. `λ` = anisotropia de Lifshitz.

Estimadores `⟨z⟩`, `C4` = `clustering_metrics` VERBATIM. Ladder N=400…3200; `λ∈[0,2]`.

## 2. Gates — VERDE (`validation_gate.json`)

| Item | Resultado |
|---|---|
| cross-check ⟨z⟩=2E/N (VERBATIM) | bit-idêntico ✓ |
| **frame-dependência DEMONSTRADA** (boost η=0.8 + refoliação) | ⟨z⟩ 12.2→9.6, C4 0.198→0.243 **MUDAM** ✓ |
| espaço-tempo genuíno (percola as 8 fatias, λ>0) | 8/8 ✓ |

O gate 2 é o **oposto** do das campanhas anteriores: aqui confirmamos honestamente que o
substrato **muda** sob boost — ele é **frame-dependente por construção** (a premissa).

## 3. Resultado central (`foliated.json`)

| λ | ⟨z⟩ (topo) | satura? | C4 (topo) | percola | arma? |
|----|---|---|---|---|---|
| 0.0 | 5.7 | ~sim | 0.286 | (fatias soltas) | — (não é espaço-tempo) |
| 0.25 | 6.5 | quase | 0.194 | 1.00 | quase |
| **0.5** | **8.6** | **SAT** | **0.174** | **1.00** | **ARMA** |
| **0.75** | **11.8** | **SAT** | **0.196** | **1.00** | **ARMA** |
| 1.0 | 17.0 | ~MF-limiar | 0.197 | 1.00 | quase |
| **1.5** | **30.1** | **SAT** | **0.185** | **1.00** | **ARMA** |
| 2.0 | 48.3 | cresce | 0.189 | 1.00 | quase (z↑) |

- **Barreira 1 (⟨z⟩):** **finita em todo λ** (órbita espacial compacta) — `⟨z⟩ ≈
  k_intra·(1+2λ²)`. Satura com N a λ moderado; a λ≥1 o expoente local fica no limiar
  (efeito de tamanho finito do raio que encolhe), mas **nunca diverge como o boost**
  (que ia a ∞). Contraste direto: Poisson/percolação/repulsão tinham ⟨z⟩→∞.
- **Barreira 2 (C4):** **satura positivo (~0.17–0.20) em TODO λ** — bem acima do tipo-CDT
  2D (0.145, o único da linhagem Lorentz que armou C4) e ~10× o limiar de morte.
- **Espaço-tempo genuíno:** percola as 8 fatias para todo λ>0 ⇒ **não** é reclassificação
  (não é pilha de fatias desconexas).

⇒ Existe `λ>0` genuíno com ⟨z⟩ finito **E** C4 positivo saturando ⇒ **ARMA**.

## 4. Leitura honesta — o que isto significa e o que NÃO significa

**O que significa:** é o **primeiro substrato de todo o programa a passar as duas
barreiras cinemáticas simultaneamente** — e ele o faz **exatamente** abandonando a
invariância de Lorentz manifesta (foliação + distância intra-fatia). Isto **confirma
concretamente** a tese central da síntese: a obstrução binária (boost ∞ / combinatória
MF) tinha a invariância de Lorentz como raiz; removida a premissa, ambas as barreiras
caem de uma vez.

**O que NÃO significa (anti-hype, disciplina):**
1. **Não é emergência de escala.** Armar este gatilho é **quase tautológico**: um grafo
   geométrico euclidiano de grau fixo (RGG) tem, por construção, laços de dimensão finita
   e coordenação finita. O C4≈0.19 é **geometria de entrada** (clustering de RGG), não
   algo emergente. Saber se há **criticalidade genuína** (ξ divergindo, classe não-MF) é
   a pergunta seguinte — **NÃO rodada** (funil; pende de nova autorização, sob o rótulo).
2. **Não é vitória do programa Lorentz-invariante.** É o contrário: a prova de que aquele
   programa não podia armar **porque** era Lorentz-invariante.
3. **Refina o "death tipo-CDT" do apêndice:** a predição tentativa de que existiria `λ*`
   além do qual C4 colapsaria (vira MF como CDT) **NÃO se confirmou** — C4 persiste até
   λ=2. Ou seja, a morte da CDT (#3–5) era específica da **colagem dinâmica de alta
   coordenação** da CDT, **não** de "3D foliado" em geral. Um acoplamento tipo-tempo de
   **alcance espacial fixo** (Lifshitz) dilui os triângulos (transitividade cai
   0.62→0.25 com λ) mas **preserva** os quadrados (C4). A coordenação ⟨z⟩ cresce com λ
   (rumo a small-world a λ grande), o sinal de que λ→∞ reencontraria a MF — mas no regime
   anisotrópico (λ≲1) o substrato é genuinamente de dimensão finita.

## 5. Posição na fila de substratos

| Família | Barreira 1 | Barreira 2 | Lorentz | Status |
|---|---|---|---|---|
| Poisson / percolação-Δτ / repulsão-s² | FALHA (∞) | — | invariante | MORTAS (boost) |
| CSG | passa | FALHA (árvore) | (sem embedding) | combinatória |
| CDT 3D/NESS/4D | z alto | FALHA (MF) | foliada (isotrópica) | combinatória |
| **Foliado anisotrópico (este)** | **finito** | **PASSA (~0.19)** | **QUEBRADA (premissa)** | **ARMA** |

Primeiro a armar — **fora** da premissa Lorentz-invariante. Confirma a síntese.

## 6. Funil

Puramente cinemático. **Ferromagneto e ξ NÃO rodaram.** O passo que importa de verdade
(criticalidade/ξ genuína vs. RGG trivial) **pende de nova autorização** e deverá, como
esta, carregar o rótulo em negrito de quebra de Lorentz no topo.

## Arquivos
`PRE_REGISTRO.md` · `foliated_trigger.py` (substrato+gate+scan+veredito) ·
`make_figure.py` · `validation_gate.json` · `foliated.json` · `foliated.png`.
