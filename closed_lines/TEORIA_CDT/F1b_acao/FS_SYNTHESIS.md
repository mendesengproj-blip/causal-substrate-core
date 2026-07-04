# FS_SYNTHESIS — veredito VINCULANTE da semente em 3D (D1/D2)

> **Fase FS-3D.** O teste vinculante da semente da TEORIA_CDT ("a informação SOURCE o
> crescimento" — charter §0.1). Pré-registro: `../SEMENTE_PRE_REGISTRO.md` (mecanismo §1,
> critérios D1/D2 §2, prior §4 — todos congelados ANTES deste código). Motor: `f1b_cdt3d.py`
> (E0-3D VERDE). Baseline: fase ESTENDIDA do CDT 3D puro (F1b). Código: `fs_seed3d.py` (φ +
> acoplamento), `fs_run3d.py` (experimento com controles embutidos). Artefatos:
> `fs3d_result.json` (k0=1,3; κ=0.3), `fs3d_kappa06.json` (robustez κ). **Data:** 2026-06-28.
>
> **Desenho conforme escrutínio (2026-06-28):** rodado em DOIS pontos da fase estendida
> (k0=1 e k0=3), e o **controle de campo genérico (markoviano) foi construído como PARTE do
> experimento desde o início** — não como reação a um resultado "impressionante" (o erro do
> FS-2D, onde o controle veio depois e rebaixou o D1). Cada ponto roda os três modos no mesmo
> ensemble, a **volume casado** e **intensidade de modulação casada**.

---

## Veredito: **D1 PASSA — D2 a SEMENTE MORRE.** "Informação SOURCE o crescimento" **não** é distinguível de um peso de crescimento sem memória.

Este é o **desfecho mais provável declarado de antemão** no prior §4 ("passa D1, morre D2"). Não
é fracasso — é a morte limpa e falsificável que o pré-registro foi desenhado para tornar possível
(charter §6). Decide a pergunta §0: a semente, como mecanismo, **não adiciona** física sobre uma
CDT-com-peso.

| Critério | Pergunta | Resultado | Veredito |
|---|---|---|---|
| **D1** (vs CDT cega γ=0) | a informação muda a geometria? | clump 0.17→12.2; +497σ/+764σ | **PASSA** |
| **D2-geom** (vs markov) | a diferença é só "um peso"? | seed clump 12.2 vs markov 4.9 (+40σ) | difere, mas… |
| **D2-memória** (C_mem) | há memória NÃO-markoviana? | seed tail **−0.55** vs markov **+1…+8** | **MORRE** ¹ |

¹ A assinatura ÚNICA pré-registrada da semente (§2) é a **cauda de memória C_mem(τ)** acima do
controle. Ela está **ausente e REVERTIDA**: a semente é temporalmente **anti-persistente**, o
controle **memoryless é MAIS persistente**. Sem essa assinatura, a diferença D2-geom é "um peso
diferente", não "um mecanismo de memória" — o critério de SOBREVIVÊNCIA (§2) exige a cauda, e ela
não existe.

---

## 1. O mecanismo testado (port fiel de §1 para 3D)

Campo de informação φ_v ≥ 0 nos **vértices** (⟨φ⟩=1). (1) **Source (γ):** a aceitação do (2,6)
[inserção de vértice] ganha `exp(γ(φ_local − φ̄))`, φ_local = média de φ nos 3 vértices do
triângulo; γ=0 ⇒ CDT cega (= F1b, verificado). (2) **Depósito:** ao crescer, o vértice novo
recebe φ_local+δ e os 3 vértices-fonte +δ (registro). (3) **Transporte (κ):** φ_v ← (1−κ)φ_v +
κ·⟨φ vizinhos-de-aresta⟩ por sweep, renormaliza ⟨φ⟩=1. γ,κ,δ todos `[External]` (γ=2, κ=0.3,
δ=0.5; κ=0.6 p/ robustez). **Volume casado entre modos** por k3 adaptativo (trava ⟨N3⟩≈1400 —
só fixa volume, não a forma; sem isto o bias inflaria o volume e confundiria D1/D2).

**Os três modos (controles embutidos):**
- **BLIND** (γ=0): CDT cega = NULO de D1.
- **SEED** (φ memória + transporte): a semente.
- **MARKOV** (peso GEOMÉTRICO local = coordenação, SEM campo/memória, recalculado a cada passo):
  NULO de D2, com `markov_gain` calibrado p/ casar a **intensidade** (std do expoente do bias)
  com a da semente.

## 2. D1 — a informação muda a geometria (PASSA, massivo, nos 2 k0)

| | clump (cego) | clump (semente) | σ | d_H cego→semente |
|---|---|---|---|---|
| **k0=1** | 0.171 ± 0.010 | 12.214 ± 0.022 | **+497σ** | 2.16 → 1.77 |
| **k0=3** | 0.255 ± 0.014 | 12.260 ± 0.006 | **+764σ** | 2.07 → 1.75 |

A semente **aglomera** drasticamente o crescimento (algumas fatias incham, outras minguam: clump
sobe ~50–70×) e baixa d_H (a geometria fica mais filamentar). A informação **não** é decoração —
**D1 passa** sem ambiguidade, nos dois pontos. (Volume casado: N3≈1400 em todos os modos.)

## 3. D2 — a diferença NÃO é memória não-markoviana (a SEMENTE MORRE)

**D2-geometria:** a semente difere também do controle markoviano (seed clump 12.2 vs markov 4.9–6.0;
+40σ em k0=1, +12σ em k0=3). Então a geometria da semente **não** é trivialmente a do peso
geométrico. *Isso, sozinho, NÃO salva a semente* — o critério de sobrevivência (§2) exige a
assinatura de **memória**, porque qualquer peso muda a geometria e a calibração de intensidade
por std é imperfeita (o peso de coordenação é cauda-pesada — a maior aglomeração da semente é
plausivelmente **feedback efetivo mais forte**, não memória; ecoa o achado 2D Tarefa-2 = colapso
genérico c=1/branched-polymer, [[teoria-cdt-nova]]).

**D2-memória (o discriminador real, C_mem(τ) = autocorrelação temporal do padrão de crescimento
por fatia):** a assinatura está **ausente e revertida**, robustamente:

| ponto | C_mem tail SEED | C_mem tail MARKOV | seed − markov |
|---|---|---|---|
| k0=1, κ=0.3 | **−0.56 ± 0.13** | +4.37 ± 0.98 | **−5.0σ** |
| k0=3, κ=0.3 | **−0.54 ± 0.03** | +1.07 ± 0.28 | **−5.8σ** |
| k0=1, κ=0.6 | **−0.46 ± 0.04** | +7.81 ± 0.39 | **−21σ** |

A semente é temporalmente **anti-persistente** (cauda negativa: cresceu numa fatia ⇒ NÃO volta a
crescer ali tão cedo — o vínculo de volume a empurra para outro lugar). O controle **memoryless**
tem cauda **positiva** (regiões de alta coordenação atraem crescimento recorrente — a *geometria*
é a variável lenta). Ou seja: **o controle sem memória tem MAIS persistência temporal que o campo
de "memória" φ.** Estendido a **κ=0.6** (transporte forte, a direção de "mais memória"): o gap só
**aumenta** (−21σ) — mais transporte **não** dá memória à semente. **D2 é robusto a κ.**

**Por que (e a confirmação do prior §4).** No **transiente** (smoke-test curto, equil≈25) a
semente chega a mostrar cauda positiva (φ ainda construindo o padrão aglomerado). No **equilíbrio**
(equil=120, o regime que D2 sonda) a cauda **lava** e reverte — exatamente a previsão §4 ("a
memória não-markoviana pode lavar no equilíbrio"). A semente cria um padrão **aglomerado mas
estático**; a dinâmica de crescimento em torno dele não carrega memória do passado além da
geometria instantânea.

## 4. O que FS-3D estabelece

**Estabelece (decide a pergunta §0):**
1. **A semente PASSA D1** — γ>0 muda a geometria emergente vs CDT cega, massivamente e nos dois
   k0. A informação acoplada ao crescimento **faz** algo.
2. **A semente MORRE em D2** — esse "algo" **não** é a memória não-markoviana que a distinguiria
   de um peso de crescimento. A assinatura pré-registrada (cauda de C_mem acima do controle) está
   ausente e revertida, robusto a k0 e a κ. A maior aglomeração vs markov é peso/feedback, não
   memória.
3. **Consequência (charter §0.1, §6; risco [CLASSE GRANDE]):** "a informação SOURCE o crescimento"
   é, ao fim, **indistinguível de uma regra de crescimento com peso** — a única adição original
   da TEORIA_CDT sobre a CDT padrão **não sobrevive como mecanismo**. A teoria, no que reproduz
   (d_H, fases, geometria 3D — tudo `[GABARITO]`), é **CDT-com-peso**, não uma teoria nova. É a
   morte limpa que o pré-registro tornou falsificável **antes** de gastar numa F2-com-semente.

**NÃO estabelece (honestidade):**
1. **Não é um teorema de impossibilidade.** A morte é da *realização* pré-registrada (φ nos
   vértices, source no (2,6), C_mem por fatia, γ=2, κ∈{0.3,0.6}). Uma realização radicalmente
   diferente da semente poderia, em princípio, escapar — mas o ônus é dela, e o prior + 2D + este
   resultado convergem para o mesmo lugar (a memória lava no equilíbrio, como na TEIC/Campanha XI).
2. **Ressalvas registradas:** (a) o casamento de intensidade markov é por std (peso de coordenação
   cauda-pesada) — por isso o veredito repousa em C_mem (forma temporal), não em D2-geom (quantia);
   (b) C_mem a estas durações de cadeia tem sensibilidade transiente↔equilíbrio (documentada acima);
   (c) volume fixo é necessário p/ justiça mas pode suprimir persistência — porém o markov sob o
   MESMO vínculo mostra persistência, então a comparação é justa.

## 5. Decisão registrada

> **A semente, na sua forma pré-registrada, está FALSIFICADA como mecanismo distintivo (morre em
> D2).** A TEORIA_CDT mantém um motor 3D validado (F1b) e física de gravidade quântica genuína
> (curvatura dinâmica, d_H→3), mas **isso é `[GABARITO]`** — o que a tornaria *nova* (a semente)
> não passou. Não construir uma F2-que-pressupõe-a-semente como fonte de novidade: o veredito
> §0 do pré-registro deu **negativo**. Caminhos honestos a partir daqui: (i) F2 como **CDT pura**
> (validar d_s 4→2 etc., explicitamente `[GABARITO]`, sem alegar novidade); (ii) uma **nova
> semente** com mecanismo de memória que sobreviva ao equilíbrio (ônus pré-registrado);
> (iii) registrar a TEORIA_CDT como mais um membro viável da classe, sem a novidade pretendida —
> e parar, como o charter §6 autoriza.

**Resumo de uma linha:** a semente **passa D1** (informação muda a geometria) mas **morre em D2**
— a assinatura de memória não-markoviana (cauda de C_mem acima do controle) está ausente e
revertida, robusta a k0 e a κ, com o controle *memoryless* sendo até **mais** persistente; logo
"a informação SOURCE o crescimento" é **indistinguível de um peso de crescimento**, e a única
adição original da TEORIA_CDT não sobrevive ao teste vinculante — exatamente o desfecho que o
prior §4 declarou de antemão.
