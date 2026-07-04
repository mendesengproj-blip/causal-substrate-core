# F2 — CONTROLE G₂: pré-registro (congelado ANTES de qualquer código)

**Data:** 2026-07-04 · **Pasta:** `FRONTEIRA_COMPACTA/F2_CONTROLE_G2/`
**Autorização:** N1 §"O que muda" item 3 (SU(4) passou limpo ⇒ G₂ liberado).
**Papel no programa:** validação intercalada da Linha 1 (ROADMAP_V2 item 7);
a "aposta computacional única" pós-submissão.

---

## 1. A pergunta

N1 estabeleceu que o substrato hospeda SU(4) igual a SU(3) ("SU(3) é hospedado,
não emergente"). Mas SU(3) e SU(4) são a MESMA família: complexos, com centro
não-trivial (ℤ₃, ℤ₄), N-alidade, e π₃ testado só via bloco SU(2). **G₂ quebra
as três muletas de uma vez:** grupo excepcional, representação fundamental
**7 REAL**, centro **TRIVIAL** Z(G₂)=1, sem N-alidade. A pergunta central:

> **A camada 3 do Teorema da Fronteira é genérica de verdade (qualquer G
> compacto), ou a fenomenologia medida depende secretamente da família SU(N)
> — da estrutura complexa, do centro, ou do embedding SU(2) do estimador?**

Sub-pergunta nomeada no core_paper (Sec. matter): *"whether confinement
depends on the center Z(G) is an open, discriminating test"* — respondida
AQUI **nas escalas medidas** (ver §7 para o que fica fora do alcance).

## 2. Instrumento (declarado)

`g2_core.py`: substrato + estimadores IMPORTADOS byte-idênticos de
`sun_core.py`/`su3_core.py` (mesma família de seeds, mesmas janelas). Motor
parametrizado por PILHA DE GERADORES (não por N): as classes recebem a pilha
T e dimA=len(T), de modo que **SU(3) = pilha Gell-Mann reproduz FL1 (gate) e
G₂ = pilha nova, mesmo código**.

**Geradores de g₂:** base de so(7) (21 antissimétricas reais), 3-forma
octoniônica φ com linhas de Fano (123),(145),(176),(246),(257),(347),(365);
g₂ = núcleo das 7 restrições φ_ijk A_jk = 0; Hermitianos T_a = −i·A_a,
ortonormalizados a Tr(T_aT_b)=2δ_ab (convenção FL1). U = exp(iφ_aT_a) ∈
SO(7) real, e ∈ G₂ por construção (exp de g₂).

**Haar em G₂** (não há QR): passeio aleatório U = Π_{k=1..60} exp(iφ_a^{(k)}T_a),
φ~N(0,1). **Teste quantitativo pré-declarado (teoria de caracteres):**
⟨χ₇(U)⟩ = 0 ± 0.03 e ⟨|χ₇(U)|²⟩ = 1 ± 0.06 sobre ≥ 4000 amostras (7 é irrep
não-trivial real ⇒ ∫χ=0, ∫χ²=1).

**Topologia — a correção que o pré-registro fixa ANTES do código:** o
hedgehog do FL1 usa o bloco SU(2) com U(0)=−1 central. **G₂ não tem −1.**
O embedding correto: SO(4) ⊂ G₂ = estabilizador do split 𝕆 = ℍ ⊕ ℍe
(numericamente: S = {A ∈ g₂ : A preserva span(e₁,e₂,e₃)}, dim 6, dois ideais
su(2)); tomar o **so(3) DIAGONAL** (conteúdo no 7: **3+3+1**, só spins
inteiros ⇒ exp(2πi n̂·J)=1, hedgehog bem-definido com perfil F: 2π→0).
Triple {J_k} com [J₁,J₂]=iJ₃; U(x) = exp(iF(r) n̂·J), F(r)=2π e^{−r/w}.
**Previsão afiada: B_∞ = índice de Dynkin do embedding = T(1)+T(1)+T(0) =
2+2+0 = 4** (= longo 1 + curto 3). O estimador `baryon_number` é o mesmo.

**Gauge:** ação de Wilson (β/7)ReTr, staples/Creutz/V(r) verbatim (fórmulas
N-livres). **Matching de acoplamento declarado:** coeficiente líder da
expansão de caracteres u = β/(2N²); os dois pontos do N1 (u=0.25, 0.333)
dão **β_G₂ ∈ {24.5, 32.7}**. Lattice L=6, T=4 (verbatim FLC quick/N1).

## 3. Gate de engenharia (obrigatório VERDE antes da suíte; qualquer falha = parar)

| # | Check | Critério |
|---|---|---|
| G1 | dim do núcleo das restrições | exatamente 14 |
| G2 | fechamento [g₂,g₂] ⊂ g₂ | resíduo fora do span < 1e−10 |
| G3 | Casimir Σ_aT_a² na 7 | = 4·I (escalar ⇒ 7 irredutível; 28/7=4) < 1e−10 |
| G4 | invariância da 3-forma por exp(g₂) | ‖φ∘U − φ‖ < 1e−10 (20 amostras) |
| G5 | Haar-walk | ⟨χ₇⟩=0±0.03; ⟨χ₇²⟩=1±0.06 |
| G6 | so(4)-split | dim S = 6; dois ideais su(2); {J_k} fecha [J₁,J₂]=iJ₃ (res < 1e−10); conteúdo espectral de n̂·J = {±1,±1,0,0,0} (3+3+1) |
| G7 | motor-pilha em SU(3) reproduz N1-gate | J_c=0.3 (pico de χ), Mermin <3% em J≥0.5, Creutz χ(2,2)>0.05 em β=4.5, B-ladder FL1 (0.795/0.892 em L=15/21 a <1e−3) |
| G8 | G₂ desordenado J=0.05 | m ≈ O(1/√n) (< 3/√n) |

## 4. Previsões pré-registradas

| # | Previsão | Prior |
|---|---|---|
| P-F2-1 | G₂ ORDENA com LRO genuína (crossover C(r) exp→const; U₄→2/3; Mermin C_long=m² a <10%) em algum J ≤ 2 | ALTO |
| P-F2-2 | **14/14 Goldstones** sem gap (dim G₂; twist por gerador, dE~ρ_s k², protocolo D2 verbatim) | ALTO |
| P-F2-3 | **B → 4 = índice de Dynkin** (inteiro topológico; escada monótona em L=15,21,31; anti-hedgehog = −B exato) | ALTO (a previsão AFIADA nova: o estimador π₃ vê o índice do embedding, não "1") |
| P-F2-4 | Confinamento no acoplamento forte espelha SU(3)/SU(4) a u pareado: Creutz χ(2,2)>0, V(r) crescente, σ(u=0.25) > σ(u=0.333) | MÉDIO-ALTO |
| P-F2-5 (fraca) | J_c ∝ dim G: 0.3×14/8 ≈ 0.53, bracket [0.4, 0.8] (mesmo estilo da sub-previsão N1) | MÉDIO |

**Leitura pré-declarada de P-F2-4:** se G₂ (centro trivial) espelha SU(N) nas
MESMAS escalas, então o σ>0 medido pelo programa é **independente de centro
nas escalas acessíveis** — a assinatura vem da expansão forte do grupo
compacto genérico, não de vórtices de centro. (O oposto — D4 — seria a
descoberta: confinamento medido = propriedade da família com centro.)

## 5. Mortes pré-registradas

- **D-F2-1:** G₂ NÃO ordena em nenhum J ≤ 4 (m < 3/√n em todo o grid) ⇒ a
  genericidade da camada 3 falha na primeira saída da família SU(N) —
  atinge o Axioma 2 "genérico" do core_paper (delta de revisão obrigatório).
- **D-F2-2:** contagem de Goldstones ≠ 14 (≥ 1 gerador com gap, robusto) ⇒
  contagem não segue dim G ⇒ camada 3 quebra.
- **D-F2-3:** B não converge para 4 (não-inteiro estável, ou não-monótono,
  ou anti ≠ −B) ⇒ ou o estimador π₃ era SU(N)-dependente (instrumento) ou
  π₃-proteção falha fora de SU(N) (física) — desambiguar ANTES de reportar:
  rodar o MESMO estimador no controle SU(3) do gate (G7 inclui a escada).
- **D-F2-4:** Creutz ≤ 0 / V(r) não-crescente em AMBOS os β com o gate G7
  verde ⇒ assinatura de confinamento depende do centro ⇒ **descoberta**
  (rebaixa "confinement" do paper-núcleo a "center-family confinement").
- Regra: NENHUMA janela/critério se move pós-dado; emendas só pré-run com
  trilha git (precedente N4).

## 6. Protocolo e custo

Fases: (0) gate (≈10 min); (1) ordenamento G₂ 9 J × 4 seeds verbatim N1
(J = 0.05, 0.1, 0.3, 0.5, 0.7, 1.0, 1.4, 2.0 + refino se crossover cair
entre pontos; mesmos sweeps/medidas/τ_int do N1); (2) Goldstones 14 twists
L=14; (3) topologia B em L=15,21,31 + anti em L=21; (4) gauge β={24.5,32.7},
L=6,T=4, mesmos sweeps do N1. Custo estimado total ≤ 1–2 h (7×7 real ≈
2–4× SU(4)); seeds fixas nos drivers; JSON por fase; τ_int/ESS reportados
(N-hig verbatim, alerta ESS<20 declarado).

## ADENDO PRÉ-RUN (04jul26, achado pelo SMOKE do instrumento, antes da suíte)

O smoke do hedgehog (L=15,21, ~1 s) revelou **erro de normalização na
previsão P-F2-3, corrigido aqui ANTES de qualquer run da suíte** (precedente
N4: emendas pré-run com trilha git):

O estimador `baryon_number` está calibrado no bloco-SU(2) da fundamental de
SU(N), cujo índice de Dynkin é T(fund)=1/2. A 7 de G₂ tem T(7)=1, então o
traço na 7 lê **2× o grau de π₃**. O grau do hedgehog so(3)-diagonal continua
= índice do embedding = 4 (longo 1 + curto 3 = T(1)+T(1)+T(0) em unidades
2T); a LEITURA do estimador é **B_est → 2×4 = 8**.

**P-F2-3 corrigida: B_est → 8** (escada monótona; anti = −B exato).
Verificação independente da correção: o smoke deu B(15)=6.3574 = 0.794678×8
e B(21)=7.1366 = 0.892081×8 — a MESMA escada de discretização do FL1
(0.794678/0.892081), medida, na razão exata ×8. **D-F2-3 corrigida
verbatim** (substituir "4" por "8" = 2×índice; a lógica de desambiguação
instrumento-vs-física fica inalterada). Nenhum outro número do pré-registro
muda; a suíte ainda não rodou.

## 7. O que esta campanha NÃO reivindica (escopo honesto)

- **String breaking / σ assintótico = 0 de G₂ está FORA do alcance** (L=6;
  a blindagem por 3 gluões, 7 ⊂ 14⊗14⊗14, opera a distâncias inatingíveis
  aqui — literatura: Holland–Minkowski–Pepe–Wiese). A resposta sobre centro
  vale NAS ESCALAS MEDIDAS, e isso será dito com essa qualificação.
- Loop de Polyakov: NÃO é critério (piso de ruído desconhecido para o sinal
  minúsculo sem centro); se medido, entra como diagnóstico rotulado.
- Nada sobre 1ª/2ª ordem da transição G₂ (fora do orçamento; OT foi campanha
  própria no SU(3)).
- Nenhum número do mundo entra; contagens (14, 4, ℤ) são teoria de grupos.
