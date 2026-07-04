# N0′ — STRESS TEST DO PRINCÍPIO: resultado da campanha adversarial

**Data:** 2026-07-01 · **Pasta:** `FRONTEIRA_COMPACTA/N0_STRESS_TEST/`
**Mandato (pré-registrado no CHARTER §N0′):** DESTRUIR N0, não confirmá-lo. Sessão
dedicada, iniciada pelo `N0_PRINCIPIO/RESULTADO.md` *procurando o erro*; 6 alvos
pré-registrados em ordem de letalidade; literatura varrida onde o alvo exigia (alvos 1,
4, 6). **Zero código** (nenhum toy foi necessário — todo candidato a contraexemplo foi
resolvido no papel).
**Etiquetas:** [teorema], [prova-esboço], [literatura], [medido] — como em N0.

---

## 0. Veredito em uma página

**N0 SOBREVIVE AOS 6 ATAQUES. Nenhuma morte pré-registrada disparou.** O status do
princípio sobe, nos termos do charter, de "argumento excelente" para **"atacado e de
pé"**. O ataque não saiu vazio: o alvo 2 encontrou um **degrau implícito real** na prova
do corolário de quiralidade (absoluto vs. relativo — §2), cujo fechamento exige um **Lema
3 novo**; o alvo 4 encontrou um **qualificador obrigatório** na Prop. 2; o alvo 3 rendeu
**dois ganhos oportunistas** (a classe GOE do colapso e o expoente H² do frac_B passam a
ser cobertos pelo princípio) e uma **previsão nova (P7)**. Edições mandatórias aplicadas
como Adendo N0′ em `N0_PRINCIPIO/RESULTADO.md` (editado, não apagado, como manda o
charter).

| # | Alvo | Veredito | Morte disparou? |
|---|---|---|---|
| 1 | Lema 2 vs. férmions na CST | **SOBREVIVE** — nenhum Weyl-da-ordem existe; toda construção importa frame/vierbein/contínuo (tabela §1) | NÃO |
| 2 | Loophole pseudo-escalar composto | **SOBREVIVE COM PATCH OBRIGATÓRIO** — funcional P-ímpar continua impossível (confirmado); mas quiralidade RELACIONAL é intrínseca e P-par, e o corolário original não a tratava; fechada pelo Lema 3 novo (independência do Poisson quenched) | NÃO (a morte exigia funcional P-ímpar explícito; não existe) |
| 3 | Inventário de campanhas vs. 3 camadas | **SOBREVIVE** — nenhum resultado da classe fica descoberto; 2 ganhos: GOE (camada 2) e expoente frac_B∝H² (paridade-T) | NÃO |
| 4 | Costura nível-de-lei da Prop. 3 | **SOBREVIVE COM QUALIFICADOR** — processos ergódicos de intensidade infinita escapam do teorema citado, mas são inconstruíveis na classe invariante (lema δ₀); condições do teorema conferidas na literatura | NÃO |
| 5 | Contraexemplo Euclidiano | **SOBREVIVE (rápido, como previsto)** — divergência nunca é forçada no lado definido; assimetria forçado-vs-escolhido confirmada | NÃO |
| 6 | Orientação via reconstrução do contínuo | **SOBREVIVE** — Malament/HKM dá classe conforme com orientação TEMPORAL como input; orientação espacial é impossível por P-equivariância | NÃO |

**Gates:** N3 (Wen-complement) **LIBERADO DE FATO** (gated por N0(c) ✓ e agora N0′ ✓).
N4 liberado para pré-registro próprio (N0 ✓ + N0′ ✓ + upgrade P1).

---

## 1. Alvo 1 — Lema 2 vs. férmions na literatura CST

**Morte exigida:** um campo de Weyl construído sobre a ordem SEM importar
vielbein/frame/orientação externa.

**Núcleo analítico do ataque** (independente da literatura): um espinor exige estrutura
de spin = levantamento pelo recobrimento duplo de uma redução do fibrado de frames a
SO⁺(d−1,1). Pelo Lema 0, a ordem fornece dados espaciais apenas módulo O(d−1) — nenhuma
redução orientada canônica. Weyl exige ainda mais: a projeção quiral γ⁵ é exatamente o
sinal que o Lema 2 mostra não ter portador. Logo qualquer Dirac/Weyl sobre causet TEM de
importar ≥ frame/orientação — e a varredura confirma que todos importam:

| Construção | O que importa além da ordem | Fonte |
|---|---|---|
| Johnston, propagador spin-½ (a): checkerboard de Feynman | direções nulas/frame do Minkowski 1+1 ambiente; amplitude por "esquina" definida no embedding | tese de Johnston; cap. handbook [literatura] |
| Johnston (b): "raiz quadrada" do Green de KG, S=(iγ^μ∂_μ+m)G | matrizes γ^μ e ∂_μ do contínuo — o fibrado de frames inteiro do Minkowski ambiente | idem |
| Sverdlov (arXiv:0808.2956); Sverdlov–Bombelli (Lagrangiano) | vierbeins definidos via holonomias de 4 campos vetoriais ADICIONADOS + campos escalares extras + medida com sinal (Grassmann); o handbook chama de "top-down... starts from the continuum" | [literatura] |
| "Free fermions on causal sets" / SJ fermiônico | extensão linear p/ ordenamento temporal + espaço espinorial do contínuo (família raiz-de-KG); nenhuma estrutura espinorial nativa | [literatura; detalhe atrás de paywall — consistente com a família (b)] |
| Causal fermion systems (Finster) | férmions são FUNDAMENTAIS (a medida sobre operadores é o ponto de partida; o espaço-tempo emerge deles) — direção oposta, não é férmion-da-ordem | [literatura] |

O próprio capítulo do handbook (Nomaan X/Surya) declara que **não existe descrição
análoga de espinores sobre um causal set** e que o objetivo realista é modelo de
*partícula* spin-½, não de campo espinorial — "might require a complete reformulation of
standard continuum-based spinor theory".

**Veredito: SOBREVIVE.** Bônus previsto no pré-registro entregue: a tabela acima é a
tabela "o que falta para quiralidade" do paper-núcleo — a estrutura importada é sempre
uma redução orientada do fibrado de frames, i.e., exatamente o portador cuja
inexistência o Lema 2 demonstra.

---

## 2. Alvo 2 — Reabrir o loophole do pseudo-escalar por construção composta

**Morte exigida:** um funcional intrínseco P-ímpar explícito.

### 2.1 O ataque direto falha por uniformidade (confirmação forte do Lema 2)

P preserva cones e orientação temporal ⇒ P: Φ → PΦ é isomorfismo de ordem, e
(C_Φ,≺,n) ≅ (C_PΦ,≺,n∘P⁻¹) *pela identidade nos rótulos*. Todo funcional intrínseco F
satisfaz F(PΦ)=F(Φ); P-ímpar ⇒ F ≡ 0. **A prova é uniforme sobre os ingredientes**:
não importa a engenhosidade da composição (tríades internas × cadeias × contagens de
intervalos), o resultado é automático. Não há loophole composto. [teorema]

### 2.2 MAS o ataque encontrou o degrau implícito da prova original

O Lema 2 diz "dados de Gram determinam configurações a menos de O(d−1), incluindo
reflexões" — isso é o grupo **global**. Consequência não tratada em N0:

> **Quiralidade RELATIVA é intrínseca.** Para dois aglomerados rígidos A, B, os dados de
> Gram de A∪B determinam a configuração conjunta a menos de UMA reflexão global; o
> produto dos sinais de orientação locais (a handedness relativa χ(A,B) ∈ {±1}) é
> invariante sob essa ambiguidade ⇒ é função dos dados intrínsecos. [prova-esboço]
> Precedente químico exato: a matriz de distâncias não distingue enantiômeros
> (handedness absoluta), mas distingue (A,B) de (A, espelho-de-B) (handedness relativa).

χ(A,B) é P-PAR (reflexão global troca os dois sinais), então o Lema 2 fica intacto. Mas
o **corolário** de N0 §5.3 ("quiralidade não emerge — nem espontaneamente") pulava um
degrau: um **condensado quiral relacional** (ordem de longo alcance de χ) mimetizaria
quiralidade emergente *referenciada ao condensado* — o padrão dos modelos left-right
simétricos, e o que toda medição real de violação-P faz (helicidade é sempre medida
relativa ao aparato; a violação-P do MP é, operacionalmente, correlação quiral universal
e rígida entre todos os processos). Isso NÃO é excluído pelos Lemas 1–2, que só
controlam funcionais P-ímpares.

### 2.3 O fechamento — Lema 3 (novo, obrigatório em N0)

**Lema 3 (sem ordem quiral de longo alcance na classe).** [prova-esboço] Na classe
(Axiomas 1–2): (i) a geometria é *quenched* — o sprinkling não é dinâmico; o campo
interno não pode alinhar handedness geométrica porque a geometria não responde. (ii) Sob
a lei de Poisson, as orientações locais de aglomerados em regiões disjuntas são
independentes e, pela simetria de reflexão local da lei, moedas justas ⇒
⟨χ(A,B)⟩ = 0 e ⟨χ(A,B)χ(C,D)⟩ = 0 para pares disjuntos, **em toda distância**. Não há
condensado quiral relacional a formar — a exclusão é por *independência da medida*, não
por simetria. ∎

Com o Lema 3, o corolário de quiralidade fecha de novo, **em forma mais forte e com a
fronteira honesta declarada**: para substratos de geometria DINÂMICA (fora do Axioma 1 —
CDT-likes etc.), o Lema 3 não se aplica e a porta relacional não está fechada por estes
argumentos (vai para o flanco combinatório/dinâmico já aberto, Apêndice B.6 de N0).

### 2.4 Previsão nova que o ataque rendeu (P7)

**P7 — Toda quiralidade emergente, em QUALQUER substrato de ordem, só pode ser fase
relacional, nunca lei:** exigiria condensado (domínios, paredes de ℤ₂, restauração
térmica/de volume finito), porque a lei é P-par por §2.1 em qualquer classe intrínseca.
A quiralidade do neutrino ser exata, universal e jamais restaurada é, portanto,
evidência estrutural contra QUALQUER origem de quiralidade em substrato causal — não só
contra a nossa classe. [falseável: achar quiralidade-lei emergente de ordem]

**Veredito: SOBREVIVE** (morte não disparou), **com patch obrigatório** — foi o achado
mais valioso da campanha: a prova ficou mais precisa (absoluto vs. relativo), ganhou um
lema, uma fronteira declarada e uma previsão.

---

## 3. Alvo 3 — Inventário de campanhas vs. as 3 camadas

**Morte parcial exigida:** um resultado medido que a fronteira deveria cobrir e não cobre.

Varredura do inventário (TEIC/DEV/SR/CDT + colapso) contra as camadas. Os três
candidatos pré-registrados:

1. **Fase FR — por que ℤ₂?** COBERTO (já estava): camada 3 — π₁(Conf₁) ≅ π₄(SU(2)) = ℤ₂
   é homotopia do alvo compacto; a tabela §2.4 de N0 já o lista. O "por que não outra
   coisa" é respondido pela própria homotopia do alvo do Axioma 2.
2. **Convergência GOE do colapso (⟨r⟩→0.53, FS2).** NÃO estava coberto em N0 — e a
   análise mostra que **é corolário da camada 2**: a via tripla de Dyson associa GOE à
   classe com simetria anti-unitária T²=+1. A lei da classe é T-estatisticamente
   simétrica (auto-dual, camada 2 lado T) e não há estrutura complexa disponível — sem
   U(1) emergente (corolário sem-fóton) não há fluxo magnético para quebrar T no
   operador ⇒ operadores reais simétricos ⇒ **classe ortogonal (GOE), não GUE/GSE**.
   O princípio pós-diz a CLASSE do ensemble; a universalidade dentro da classe é RMT,
   não o princípio (declarado). **GANHO: novo corolário para N0.** [prova-esboço]
3. **frac_B ∝ H² — a camada 1 explica o low-curvature, mas explica o EXPOENTE?**
   AGORA SIM: o protocolo E6c usa dS₄ via hiperbolóide 5D, **simétrico sob reversão
   temporal** (X0→−X0); frac_B é contagem não-assinada (T-par, Lema 0). A dualização de
   ordem mapeia a família de deformação H↔−H mantendo a lei ⇒ frac_B(H) = frac_B(−H) ⇒
   função PAR ⇒ termo líder H², dado analiticidade em torno do flat (o flat é zero
   exato por teorema — camadas 1+2). O fit quadrático medido (R²=0.984–0.997)
   [medido, E6c/E6e] deixa de ser empírico e vira expoente derivado. Formulação
   equivalente: resposta escalar analítica em invariantes de curvatura só contém
   potências pares de H (R_scal ∝ H²). **GANHO: expoente coberto.** [prova-esboço]

**Resíduo correto (fora do escopo, declarado, não é morte):** as mortes COMBINATÓRIAS
(CSG, CDT empilhado, foliado) estão fora do Axioma 1 — o teorema é sobre a classe; esse
flanco é o item B.6 já aberto. Valores dinâmicos (J_c≈0.3, 1ª ordem do SU(3), σ(β)) e o
padrão "forma emerge/escala externa" das pontes SR são dinâmica — fora do escopo
cinemático declarado em §1 de N0. Setor DEV/MOND: outra teoria. **Nenhum resultado DA
CLASSE fica descoberto. Morte parcial NÃO dispara.**

---

## 4. Alvo 4 — Costura de nível-de-lei da Prop. 3 (Kallenberg/Last–Penrose)

**Morte exigida:** uma perturbação invariante que não flui para Poisson.

**Condições do teorema citadas conferidas** [literatura: Kallenberg; Daley–Vere-Jones;
Møller–Schoenberg "Thinning spatial point processes into Poisson processes"; e a recente
"law of thin processes" (arXiv:2502.14839)]: thinning p→0 + contração compensadora →
Cox em geral; → Poisson exatamente quando a intensidade amostral é determinística
(ergodicidade) e **finita**. Não-ergódico → Cox = superseleção de intensidade,
intrinsecamente invisível (já tratado em N0 §3.2). Exóticos de nível de momento
(correlações log-periódicas = ciclos-limite de RG à la Efimov) ficam excluídos DENTRO da
classe ergódica de intensidade finita pelo próprio teorema de nível de lei — a costura
protege contra eles; é o valor dela.

**O escape encontrado (real, e fechado pela própria camada 1):** existem processos
estacionários ergódicos **localmente finitos com intensidade infinita** (ex.: clusters
com E[K]=∞ e cauda pesada — thinning preserva o índice de cauda; nunca fluem para
Poisson). Escapam do teorema. MAS são inconstruíveis na classe invariante:

> **Lema δ₀.** [prova-esboço] Um kernel de deslocamento/cluster Lorentz-invariante
> exigiria uma medida de PROBABILIDADE invariante sobre órbitas de O(d−1,1)†; as órbitas
> não-triviais são não-compactas (H^{d−1} etc.) e não portam probabilidade invariante ⇒
> a única distribuição de deslocamento invariante é δ₀ ⇒ não existe dressing/cluster
> invariante não-trivial. A mesma não-compacidade que mata a valência (camada 1) protege
> a Prop. 2 de seus próprios patológicos. †(no sentido de Palm, como em
> IMPOSSIBILIDADE_PARCIAL)

**Veredito: SOBREVIVE COM QUALIFICADOR** — a Prop. 2 já dizia "intensidade finita", mas
o qualificador é estrutural (load-bearing) e o lema δ₀ deve entrar no Adendo de N0. A
lacuna de redação B.2 (costura como prova única) permanece declarada — nada encontrado
que a inverta.

---

## 5. Alvo 5 — Contraexemplo Euclidiano do afiamento

**Morte exigida:** construção Euclidiana invariante onde a valência diverge POR FORÇA da
invariância.

Impossível, em duas linhas: todo subgrupo fechado de O(d) é compacto; toda órbita de
separação invariante é esfera de volume finito; para qualquer processo invariante
(Poisson ou não), a regra q de suporte compacto é invariante e dá ⟨z⟩ < ∞. A divergência
no lado definido é sempre *escolhida* (cauda longa), nunca *forçada*. A literatura de
matéria condensada confirma o lado positivo (percolação contínua, Ising em RGG —
criticalidade genuína existe no lado definido). **A assimetria forçado-vs-escolhido de
N0 §4.2 fica confirmada. SOBREVIVE.** (Checagem rápida, como o pré-registro previa.)

---

## 6. Alvo 6 — Orientação via teoremas de reconstrução do contínuo

**Morte exigida (do Lema 0/2):** a ordem determinando orientação espacial em qualquer
regime.

[literatura] Malament (1977)/HKM (1976)/KPHM: a ordem causal de espaço-tempos
distinguishing determina topologia, estrutura diferenciável e métrica **a menos de fator
conforme** — e o enunciado PRESSUPÕE a orientação temporal como input do setup. Nenhum
teorema da linha (incl. topologia de causets, antichains engrossadas MRS, Parrikar–Surya)
recupera orientação ESPACIAL. E não poderia: argumento de P-equivariância — P é
automorfismo causal de Minkowski, logo os dados de ordem são invariantes sob P; qualquer
funtor de reconstrução leva dados P-invariantes em outputs P-invariantes; uma orientação
não é P-invariante ⇒ nenhuma reconstrução a produz. Em espaço-tempo genérico: (M,g,or) e
(M,g,or′) têm a MESMA ordem causal (o mapa identidade é isomorfismo causal) ⇒ orientação
é estrutura extra sobre a classe conforme, indeterminável pela ordem em qualquer regime.
**SOBREVIVE.** [teorema]

---

## 7. O que muda em N0 (edições mandatórias, aplicadas como Adendo N0′)

1. **Lema 2 — precisão absoluto/relativo** (§2.2 acima): "espaço sem sinal" = sem sinal
   ABSOLUTO; quiralidade relativa é intrínseca e P-par.
2. **Lema 3 — novo** (§2.3): sem ordem quiral de longo alcance na classe (geometria
   quenched + independência de Poisson + reflexão local); fecha o degrau do corolário de
   quiralidade; fronteira dinâmica declarada.
3. **Prop. 2 — qualificador estrutural** (§4): "intensidade finita" é load-bearing; lema
   δ₀ mostra que os patológicos de intensidade infinita são inconstruíveis na classe
   invariante.
4. **Corolários novos:** classe GOE do espectro causal (camada 2); expoente frac_B ∝ H²
   (paridade-T + analiticidade).
5. **P7 nova** (§2.4): quiralidade emergente só como fase relacional, nunca lei — em
   qualquer substrato de ordem.

## 8. Critério de encerramento e gates

Cada alvo tem veredito escrito (acima): 6/6 SOBREVIVE (2 com edição obrigatória).
Pelo charter: **N3 LIBERADO DE FATO** (N0(c) ✓ + N0′ ✓); **N4 liberado para
pré-registro** (N0 ✓ + N0′ ✓); N1/N2 seguem independentes. Ordem recomendada do charter
continua: **N1 (gate SU(3) primeiro) → N2 → N3**.

## Literatura consultada (alvos 1, 4, 6)

- Sverdlov, "Spinor fields in Causal Set Theory", arXiv:0808.2956 (vierbeins via
  holonomias de campos adicionados).
- Sverdlov–Bombelli, "Dynamics for causal sets with matter fields", J.Phys.Conf.Ser. 174
  (Lagrangiano top-down).
- Nomaan X, "Quantum Field Theory on Causal Sets", arXiv:2306.04800 / handbook Springer
  (estado da arte; espinores inexistentes sobre a ordem; Johnston checkerboard e
  raiz-de-KG).
- Johnston, "Feynman Propagator for a Free Scalar Field on a Causal Set",
  arXiv:0909.0944 (+ tese, cap. spin-½).
- Finster, causal fermion systems (férmions fundamentais, direção oposta).
- Malament 1977 / HKM 1976 (classe conforme; orientação temporal como input); survey
  Surya, "The causal set approach to quantum gravity", arXiv:1903.11544.
- Møller–Schoenberg, "Thinning spatial point processes into Poisson processes";
  Kallenberg (limites de thinning → Cox/Poisson); "The law of thin processes",
  arXiv:2502.14839.
