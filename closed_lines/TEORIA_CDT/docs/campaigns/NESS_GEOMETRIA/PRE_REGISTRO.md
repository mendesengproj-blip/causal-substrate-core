# PRÉ-REGISTRO — Geometria FORA-DO-EQUILÍBRIO (NESS): a geometria escapa do mean-field?

> **Estado: PRÉ-REGISTRADO. Congelado ANTES de qualquer medição de física.** Data: 2026-06-29.
> Campanha **Direção 2** (geometria NESS). A Parte B (4D) é **estritamente condicional** à morte
> desta Parte A pelo critério §6 — não roda em paralelo, não "adianta".
>
> Reusa o motor `F1b_acao/f1b_cdt3d.py` (E0-3D VERDE) e os estimadores ξ_2nd/U₄/χ_max/C4 já
> validados (`ESCALA_XI/xi_suite.py`, `CDT_TEIC_FERRO/ferro_cdt.py`) **verbatim**. Nada é
> reimplementado.

---

## 0. A pergunta (afiada pela lição do MEMORIA_DIAGNOSTICO)

> A geometria do CDT 3D, quando **dirigida fora-do-equilíbrio** (NESS genuíno, não "nunca
> converge"), **escapa do mean-field** — o destino que matou Poisson, CSG e CDT-em-equilíbrio
> (`CDT_TEIC_FERRO`, Pergunta B não-resolvida, sinal limpo lean MF)?

Se sim, é o **primeiro resultado positivo** de toda a linha de investigação de escala. Se não, a
morte da escala é **robusta a equilíbrio E não-equilíbrio** na geometria — mesmo padrão que o
MEMORIA_DIAGNOSTICO estabeleceu para a *memória informacional*, agora para a *geometria*.

## 1. A armadilha central (esta campanha existe para não repeti-la)

O MEMORIA_DIAGNOSTICO mostrou que **"nunca atinge platô" (o α=0,1) não é sobrevivência — é falha
de convergência mascarada**. **"Fora do equilíbrio" aqui = Estado Estacionário de Não-Equilíbrio
(NESS)**, com definição operacional não-circular, verificada em DUAS condições **separadas e em
ordem**:

- **Condição 1 — estacionariedade estatística** (Gate 1): observáveis (d_H, ⟨z⟩, volume) atingem
  distribuição **estável no tempo** (média/variância constantes entre janelas, dentro do erro de
  blocking). É o **oposto** de "nunca converge". Se falhar → mesma armadilha do α=0,1, morte aqui.
- **Condição 2 — quebra de balanço detalhado** (Gate 2): apesar de estacionário, **não** satisfaz
  reversibilidade microscópica — há corrente de probabilidade não-nula no espaço de configurações
  (assimetria persistente entre fluxos de aceitação de um movimento e do seu inverso). Se o balanço
  detalhado **se restabelece** apesar do drive → equilíbrio disfarçado, morte.

**Só com as duas confirmadas (1 depois 2) a campanha testa escala.**

## 2. O mecanismo de condução — ESCOLHA DECLARADA (antes de rodar)

> **ESCOLHIDO: opção (c) do charter — condução PARAMÉTRICA via k₀ OSCILANTE.**
> `k₀(τ) = k̄₀ + A·cos(2π·τ / P)`, onde τ = índice de sweep, **A** = amplitude e **P** = período,
> ambos **`[External]`** (declarados, não emergem).

**Por que esta opção (razão declarada, congelada):**

1. **Integridade do motor (decisivo).** Opção (c) **não toca em nenhum dos 5 movimentos de Pachner
   validados** — só varia o parâmetro `k0` que `CDT3D.sweep(k0, k3, eps, Vt)` já recebe a cada
   sweep. Logo o validador `check_manifold` (o oráculo agnóstico-ao-movimento que sustenta a
   integridade de todo o programa) **continua guardando cada configuração**. As opções (a)
   injeção/dissipação local e (b) aceitação não-recíproca exigiriam cirurgia nos moves ou no
   balanço, reabrindo o risco de bug-density que o F1b_PHASE_GATE §5 fechou. Trocar isso por um
   drive de um parâmetro é a escolha de integridade certa.
2. **Faz os DOIS gates genuínos (não triviais).** É a propriedade que o charter mais exige
   (advertência explícita contra passe trivial / "equilíbrio disfarçado"):
   - **Gate 1** vira teste real: um sistema periodicamente dirigido **pode** atingir estado
     estacionário periódico (Floquet) **ou** disparar (volume/curvatura sem retorno). Não é dado.
   - **Gate 2** vira teste real: no limite **adiabático** (P ≫ τ_relax) o sistema segue o
     equilíbrio instantâneo → balanço detalhado **se restabelece** sobre o ciclo (histerese → 0) =
     **morte Gate 2**, exatamente o "equilíbrio disfarçado" do charter. No limite **não-adiabático**
     (P ≪ τ_relax) há atraso → histerese / produção de entropia por ciclo ≠ 0 = NESS genuíno.
3. **Fundamentação padrão.** É o NESS periodicamente-dirigido da termodinâmica estocástica
   (regime Jarzynski/Crooks): a dependência temporal do protocolo quebra DB globalmente; a
   **área da curva de histerese** (k₀ vs resposta geométrica) = produção de entropia por ciclo é o
   diagnóstico canônico de DB quebrado. Diretamente alinhado ao Gate 2 do charter ("assimetria
   entre taxa de aceitação de movimento e inverso"): a assimetria **integrada no ciclo** é a
   histerese.

**Parâmetros primários (congelados):** `k̄₀ = 2.5`, `A = 1.5` (faixa k₀ ∈ [1.0, 4.0], **dentro da
fase estendida** — não cruza a transição k₀≈5–6 para não arriscar morte de Gate 1 por degeneração
em fase crumpled). `T` (fatias) = 10, `Vt` = volume-alvo travado pelo potencial `eps·(N₃−Vt)²`
(volume globalmente conservado: o drive age na **curvatura/coordenação**, não no volume líquido).
**Varredura de P** declarada: P ∈ {2, 8, 32, 128} sweeps — para localizar τ_relax e exibir a
transição adiabático↔não-adiabático (é o que torna Gate 2 falsificável dos dois lados).

**Controle nulo embutido (obrigatório):** `A = 0` ⇒ `k₀(τ) ≡ k̄₀` ⇒ recupera o F1b de equilíbrio
**verbatim**. Histerese DEVE ser nula e a estacionariedade DEVE ser a de equilíbrio. É o nulo
contra o qual o NESS é medido (e a sanidade de que o wrapper não alterou a física).

## 3. Gate 1 — Estacionariedade (medir ANTES de tudo)

1. Rodar o sistema dirigido por horizonte longo. Medir d_H, ⟨z⟩, volume médio em janelas
   sucessivas (estroboscópico: mesma fase do ciclo entre períodos consecutivos, p/ separar a
   oscilação imposta da deriva genuína).
2. **Critério de PASSA:** média e variância **estabilizam** entre janelas (dentro do erro de
   blocking) em horizonte finito. Reportar o horizonte necessário explicitamente.
3. **Morte do Gate 1 (e da Parte A):** observáveis driftam sem estabilizar até o limite
   computacional razoável (= padrão do α=0,1, não NESS). Registrar e pular para a Parte B.

## 4. Gate 2 — Quebra de balanço detalhado (SÓ se Gate 1 passou)

1. No estado estacionário (periódico) confirmado: medir a **assimetria integrada no ciclo** entre
   o fluxo de aceitação de cada par de Pachner e seu inverso — concretamente o **fluxo líquido
   acumulado por ciclo** de (2,6)−(6,2) e (2,3)−(3,2), e a **área da curva de histerese** k₀ vs
   {d_H, ⟨z⟩} (= produção de entropia por ciclo). Varrer P.
2. **Sucesso (NESS genuíno):** assimetria/histerese estatisticamente significativa e **estável
   (não decai com mais amostragem)** em pelo menos um P não-adiabático. Reportar a curva
   histerese(P).
3. **Morte (equilíbrio disfarçado):** a assimetria/histerese **desaparece dentro do erro** em
   todos os P acessíveis (sistema sempre adiabático → DB restaura). Registrar e pular para Parte B.

## 5. Teste de escala sob NESS confirmado (SÓ se Gates 1 E 2 passaram)

Repetir **verbatim** a suíte de universalidade já usada (`ESCALA_XI`, Gatilhos, `CDT_TEIC_FERRO`
Pergunta B): **snapshots estroboscópicos** da geometria NESS (fase fixa do ciclo) → 1-esqueleto via
`cdt_substrate.cdt_skeleton_graph` → `ferro_cdt.question_B` (ferromagneto O(3) verbatim):
ξ_2nd via `xi_suite`/grafo, **U₄(J) cruzando entre tamanhos**, **χ_max(N)**.

- **ESCAPA DO MEAN-FIELD:** ξ_2nd/L com pico em J_c (cruzamento entre tamanhos), χ_max **super-MF**
  (expoente x > 0,5, rumo a ~0,66 geométrico-3D). Primeiro positivo da linha de escala.
- **MEAN-FIELD (replica tudo):** ξ_2nd/L em platô, χ_max sub-volume (x ≲ 0,5) — mesma assinatura
  de Poisson, CSG, CDT-equilíbrio.
- **Overlay obrigatório** sobre as curvas existentes (Poisson N^0,07; CSG; CDT-equilíbrio N^0,24).
- Disciplina de sempre: **resultado ambíguo = NÃO-RESOLVIDO**, nunca forçado. Muitos seeds (a
  lição de `CDT_TEIC_FERRO`: 4 seeds → χ_max noise-dominated).

## 6. Critério de morte da Parte A inteira (verbatim, pré-registrado)

> Se o Gate 1 **ou** o Gate 2 falhar — isto é, se não for possível estabelecer um NESS genuíno e
> não-ambíguo nesta classe de mecanismos de condução — **OU** se, sob NESS confirmado, o teste de
> escala ainda mostrar as assinaturas mean-field (platô de ξ_2nd/L, χ_max sub-volume), então a
> **Direção 2 está morta**: geometria fora-do-equilíbrio, nesta formulação, não escapa do mesmo
> destino das tentativas em equilíbrio. Prossiga para a Parte B.

## 7. Anti-circularidade (charter §3, mantida)

1. **A, P, k̄₀ (e qualquer escala do drive) são `[External]`.** A campanha **não** afirma que o
   relógio do drive emerge. Teste é **estrutural** (a classe de universalidade muda?), nunca "número
   emergiu".
2. **Nenhuma escala emerge.** A aresta do CDT já é `[External]` por F1b.
3. **Nada de TEIC/DEV/SR como fundação.** O ferromagneto O(3) é importado **como sonda de
   universalidade** (igual `CDT_TEIC_FERRO` faz; TEIC importa o CDT, não o contrário) — o veredito
   de escala é sobre a **geometria NESS**, medida por uma sonda padrão.
4. **Pré-registro antes de medir; sem annealing.** Mecanismo (c), parâmetros, Gates 1/2, e o
   critério de morte §6 estão congelados aqui.

## 8. Prior honesto (declarar, não pender)

A morte mais provável é a **mesma estrutural de sempre**: o 1-esqueleto do CDT 3D tem coordenação
alta (⟨z⟩~12–15) → mistura rápido → mean-field por teorema (small-world/Bethe, ver
`escala-xi-correlation-divergence`). O drive paramétrico injeta correlação **temporal** (memória de
ciclo), mas se a mistura geométrica de alta-z domina, a sonda O(3) não vê classe nova — **χ_max
sub-MF de novo**, agora robusto a não-equilíbrio. Resultado mais provável declarado: **morte por
§6** (Gate 2 adiabático, OU escala MF sob NESS). Não seria fracasso — seria fechar a porta do
não-equilíbrio **geométrico** com a mesma honestidade do MEMORIA_DIAGNOSTICO. O fracasso seria não
saber qual morte ocorreu.

## 9. Entregáveis

`driven_cdt.py` (wrapper k₀-oscilante + contadores de fluxo, reusa CDT3D), `gate1_stationarity.py`,
`gate2_detailed_balance.py`, `scaling_ness.py` (condicional, reusa ferro_cdt), `SYNTHESIS.md`
(veredito), dados (`.json`), figuras. **Bloqueios:** Gate 2 só após Gate 1 passar; escala só após
ambos; Parte B só após morte §6.
