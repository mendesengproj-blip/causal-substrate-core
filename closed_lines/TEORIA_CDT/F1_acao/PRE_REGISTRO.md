# PRÉ-REGISTRO — F1: ensemble causal + ação de Regge (a fundação dinâmica)

> **Congelado ANTES de qualquer código.** Charter: `../CHARTER.md` (Fase F1). Glossário:
> `../GLOSSARIO.md`. Disciplina herdada do pipeline (a mesma que organizou TEIC): predições +
> critério de morte travados aqui; gate de engenharia antes de física; sem annealing depois de
> ver os números. **Regra de não-contaminação ativa:** nada de TEIC/DEV/SR entra como dado.
>
> **Data de congelamento:** 2026-06-27. **Estado:** PRÉ-REGISTRADO, NÃO EXECUTADO.

---

## 0. O que F1 decide (e o que NÃO decide)

F1 **não** testa se a geometria emerge (isso é F2) nem se há criticalidade (F3). F1 constrói e
**valida a maquinaria**: o ensemble de triangulações causais + a ação de Regge + a rotação de
Wick + o Monte Carlo. O veredito de F1 é **de engenharia**, não de física:

> **A maquinaria está correta?** Ou seja: o gerador produz triangulações causais válidas
> (manifold, folheação preservada, ergódico), a ação avalia certo, e — o teste decisivo — em 2D
> ela **reproduz resultados de CDT exatamente conhecidos** (que existem analiticamente).

Sem F1 VERDE, **nenhum número de F2+ é confiável**. Esta é a porta de engenharia do charter §3.4.

---

## 1. O ensemble causal concreto (decisão travada: começar em 2D)

**Dimensão de trabalho de F1: 2D** (decisão de escopo, `CHARTER.md §5`). Razão: 2D-CDT é
**exatamente solúvel** (Ambjørn–Loll 1998), então existe **gabarito analítico** contra o qual
validar a maquinaria. Subir para 3D só depois de F1 VERDE em 2D (F1 não mira física nova — mira
correção de maquinaria; 2D é onde isso é verificável sem ambiguidade).

**Construção (2D-CDT padrão, re-derivada aqui, não importada):**
- O espaço-tempo é um **cilindro** (ou toro no tempo): T fatias de tempo, cada fatia é um círculo
  de ℓ_t vértices (geometria espacial = anel 1D).
- Entre a fatia *t* e *t*+1, o "sanduíche" é preenchido por triângulos de dois tipos:
  **(2,1)** = base de 2 vértices na fatia *t*, ápice de 1 na fatia *t*+1; **(1,2)** = o inverso.
  Cada triângulo tem 1 aresta tipo-espaço + 2 tipo-tempo.
- **Vínculo causal (a folheação):** nenhuma aresta pula fatias; cada sanduíche é uma tira de
  triângulos (2,1)/(1,2) alternados; as fatias **não** se rasgam nem se ramificam. Topologia
  espacial fixa (círculo) em todo *t*.

**Movimentos de Pachner (preservando a folheação):** o conjunto mínimo ergódico para 2D-CDF —
inserção/remoção de vértice numa fatia (muda ℓ_t) + flip de aresta tipo-tempo dentro de um
sanduíche. **Ergodicidade é um gate (§4), não uma suposição.**

---

## 2. A ação (travada, com o cuidado dimensional explícito)

Ação de Regge em 2D (ver `GLOSSARIO.md`):
- **Termo de curvatura = TOPOLÓGICO** (Gauss-Bonnet): ∑ deficit = 2π·χ, com χ = característica
  de Euler **fixa** pela topologia (cilindro/toro). ⇒ **não contribui para a dinâmica** (é
  constante no ensemble de topologia fixa). Registrar isto explicitamente: em 2D a única
  dinâmica é **entrópica**.
- **Termo de volume:** S = **λ · N₂**, onde N₂ = número de triângulos. λ = constante cosmológica
  (acoplamento, varre-se). Em 2D-CDT com volume fixo, λ é apenas o multiplicador de Lagrange que
  fixa ⟨N₂⟩.
- **Rotação de Wick:** parâmetro α (razão tipo-tempo/tipo-espaço ao quadrado). Para F1, usar a
  continuação padrão α → −α (Lorentziano → Euclidiano) onde o peso vira e^{−S} real positivo.
  A α-dependência das áreas/ângulos entra explicitamente; em 2D o efeito é controlado e
  verificável.

> **Por que 2D mesmo sendo a curvatura trivial:** o objetivo de F1 é **validar a maquinaria**, e
> 2D-CDT tem observáveis **analíticos** (próximo §3) que só a maquinaria correta reproduz. A
> trivialidade da curvatura em 2D é uma feature (menos partes móveis), não um bug — a curvatura
> dinâmica entra em F1b/3D, depois do gate VERDE.

---

## 3. O gate de validação (o teste DECISIVO de F1 — gabaritos analíticos de 2D-CDT)

A maquinaria só é aceita se reproduzir, **dentro do erro estatístico**, resultados de 2D-CDT que
são **conhecidos exatamente** (re-derivados/conferidos aqui, não importados como fé):

| # | Observável analítico de 2D-CDT | Valor-alvo (gabarito) | Tolerância |
|---|---|---|---|
| G1 | **Dimensão de Hausdorff** d_H da geometria 2D-CDT | **d_H = 2** (exato; 2D-CDT é, ao contrário do DT euclidiano d_H=4, genuinamente bidimensional) | \|d_H − 2\| < 0.1 |
| G2 | **Distribuição de comprimento da fatia** ℓ_t no estado estacionário | bate a forma conhecida do propagador de tempo-próprio de Ambjørn–Loll (largura ∝ √⟨N₂⟩) | KS-test não rejeita a 5% |
| G3 | **Função de 2 pontos / propagador de tempo-próprio** | decaimento conhecido em T (forma fechada AL98) | R² > 0.95 no ajuste à forma |
| G4 | **Ergodicidade dos movimentos** | autocorrelação de N₂ e ℓ finita; o MC visita todo o range de ℓ | autocorr-time finito; sem regiões presas |
| G5 | **Balanço detalhado / acceptance** | ⟨N₂⟩ estável e independente da condição inicial (quente vs fria) | 2 inits coincidem em 2σ |

**G1 é o gate-mor:** se a maquinaria não der d_H = 2 para 2D-CDT, ela está **errada** — porque
esse número é conhecido e não-negociável. (Nota anti-contaminação: d_H=2 aqui é o **gabarito
externo de CDT**, usado para **validar a maquinaria**, não um resultado desta teoria; marcado
`[GABARITO]`.)

---

## 4. Critérios de F1 (congelados — engenharia, não física)

- **F1 VERDE (maquinaria aceita):** G1–G5 **todos** passam. ⇒ o ensemble + ação + Wick + MC estão
  corretos; a teoria pode subir para F1b (3D, curvatura dinâmica) e depois F2 (geometria emerge).
- **F1 VERMELHO (maquinaria quebrada):** qualquer G1–G3 falha (d_H≠2, propagador errado). ⇒ há bug
  na ação, na rotação de Wick ou nos movimentos. **Não é morte da teoria** — é morte da
  implementação; corrige e re-roda. (Distinção crucial: F1 vermelho ≠ Morte A do charter.)
- **F1 AMARELO (ergodicidade/MC):** G1–G3 passam mas G4/G5 falham (MC preso, autocorr divergente).
  ⇒ a física está certa mas o amostrador é ineficiente; precisa de movimentos melhores ou mais
  estatística antes de F2. Registrar o orçamento de passos necessário.

**SEM ANNEALING:** os gabaritos G1–G5 e os alvos são fixados aqui, antes de qualquer dado. d_H=2
não é renegociável "se der 2.3, talvez conte" — dá 2 ou a maquinaria está errada.

---

## 5. Gate de engenharia ANTES da física (charter §3.4)

Antes de medir d_H, validar o gerador em casos pequenos **conferíveis à mão**:
- E0-a: o menor cilindro causal (T=2, ℓ=3) tem N₂, N₁, N₀ contáveis manualmente; conferir.
- E0-b: característica de Euler χ medida = χ topológica esperada (0 para toro, etc.) — confirma
  que a folheação não rasgou nada.
- E0-c: cada aresta tipo-espaço em exatamente 2 triângulos do mesmo sanduíche; cada aresta
  tipo-tempo idem — invariante de manifold causal preservado por **todos** os movimentos
  (testar após 10⁴ movimentos aleatórios: o invariante nunca quebra).
- E0-d: um movimento seguido do seu inverso retorna à triangulação original (reversibilidade,
  pré-requisito do balanço detalhado).

Sem E0 VERDE, o gate de física (§3) não roda.

---

## 6. Prior honesto (declarar, não pender)

F1 é a fase **menos** arriscada cientificamente e a **mais** arriscada em engenharia: 2D-CDT é
território conhecido, então o resultado físico (d_H=2) é **esperado** — o risco real é **bug de
implementação** (rotação de Wick errada, movimentos não-ergódicos, balanço detalhado quebrado).
Por isso F1 é, deliberadamente, um **teste da maquinaria contra gabarito**, não uma busca por
novidade. **Expectativa honesta:** F1 deve dar VERDE; se der VERMELHO, é bug nosso, não física —
e o valor de pré-registrar é justamente não confundir um bug com uma descoberta nem o contrário.
A novidade só é possível de F3 em diante (criticalidade) e, no melhor caso, em F4.

---

## 7. O que NÃO fazer em F1

- **Não rodar 3D/4D ainda.** F1 é 2D para ter gabarito analítico. 3D é F1b, após VERDE.
- **Não medir "emergência de geometria" como descoberta** — em 2D ela é gabarito conhecido (§3).
- **Não chamar nada de "escala emergente"** — a aresta é `[External]` (charter §3.1).
- **Não importar código/resultado de TEIC/DEV/SR.** Re-derivar aqui; marcar `[GABARITO]` o que
  vier da literatura de CDT como referência de validação.
- **Não escrever código antes deste pré-registro estar commitado.** (Próximo passo após commit:
  `f1_cdt2d.py` + gate E0 + gate G1–G5, nesta ordem.)

---

## 8. Entregáveis de F1 (quando executar)

`f1_cdt2d.py` (gerador + ação + MC), `validation_gate.json` (E0 + G1–G5), `F1_SYNTHESIS.md`
(veredito VERDE/VERMELHO/AMARELO com os números), figura (d_H fit + distribuição de ℓ). Depois:
decisão registrada de subir para **F1b (3D, curvatura dinâmica)** ou corrigir.
