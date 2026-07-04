# F1b_PHASE_GATE — gate de fases do CDT 3D PURO (pré-registro + veredito de estado)

> **Tarefa 3 do escrutínio pré-FS-3D.** Antes de injetar a semente em 3D (o teste vinculante
> D2/C_mem), o motor 3D **puro** (γ=0, sem semente) tem que reproduzir o diagrama de fases
> conhecido do CDT, em particular uma **fase estendida** com perfil de volume tipo-de-Sitter.
> Sem esse gate VERDE, qualquer efeito da semente em 3D é não-interpretável (pode ser só uma
> fase patológica conhecida do CDT puro — o mesmo risco da Tarefa 2).
>
> **Data:** 2026-06-28. **Estado: ~~NÃO-VERDE (NÃO EXECUTADO)~~ → EXECUTADO.** O motor 3D foi
> construído e validado (E0-3D VERDE) e o gate de física rodou. **Veredito completo e atualizado
> em `F1_acao/F1b_SYNTHESIS.md`.** Resumo: E0-3D VERDE; diagrama de fases emerge (estendida ↔
> degenerada, transição k0≈5–6); **gate-mor d_H corre com k0 (2.68→1.87)** e sobe com o volume na
> fase estendida (2.41→2.55→2.69, rumo a 3) = curvatura DINÂMICA + geometria 3D emergente; só o
> perfil de-Sitter cos² fica **deferido** por volume. **FS-3D DESBLOQUEADO.** O §5 abaixo é o
> registro histórico do veredito ANTERIOR (pré-execução).

---

## 1. O ensemble 3D (especificação, re-derivada aqui)

- **Folheação:** T fatias de tempo (periódicas). Cada fatia é uma **triangulação 2D** de
  topologia espacial fixa (começar com **S²**; o mínimo é o bordo do tetraedro = 4 triângulos).
- **Tetraedros entre fatias** (3 tipos, o análogo 3D dos (2,1)/(1,2)):
  - **(3,1):** 3 vértices na fatia *t*, 1 na *t*+1 (base 2D embaixo, ápice em cima).
  - **(1,3):** 1 na *t*, 3 na *t*+1 (espelho).
  - **(2,2):** 2 na *t*, 2 na *t*+1 (aresta-tipo-espaço embaixo, aresta-tipo-espaço em cima).
  - N₃ = #tetraedros; N₀ = #vértices; N₃^{(3,1)} = #tetraedros (3,1) (proporcional ao volume
    espacial de cada fatia).
- **Vínculo causal:** nenhuma aresta pula fatias; as fatias 2D não se rasgam (topologia S² fixa
  em todo *t*). O "C" de CDT.

## 2. A ação (3D — agora a curvatura é DINÂMICA, ≠ 2D)

Diferente de 2D (curvatura topológica), em 3D a ação de Regge é dinâmica:
- Forma padrão (após Wick): **S = −k₀·N₀ + k₃·N₃** (k₀ ∝ 1/G inverso de Newton; k₃ ∝ constante
  cosmológica, ajustado p/ fixar ⟨N₃⟩). Opcionalmente o parâmetro de assimetria Δ
  (tipo-tempo/tipo-espaço) como 2º eixo do diagrama de fases.
- Peso e^{−S} (Metropolis), volume fixado por potencial quadrático (como em F1).

## 3. Os movimentos de Pachner 3D (preservando a folheação)

Conjunto ergódico mínimo (o análogo 3D do flip/add/delete de F1), **muito** mais intrincado:
- **(2,6) / (6,2):** insere/remove um vértice numa fatia (muda volume espacial local).
- **(4,4):** move tipo-espaço dentro de um sanduíche (preserva N₃).
- **(2,3) / (3,2):** rearranjo de tetraedros (preserva folheação).
Cada um exige bookkeeping de vizinhança de tetraedros (4 vizinhos por tetraedro) + invariante de
manifold causal — a fonte principal de bugs, motivo do gate E0-3D abaixo ser não-negociável.

## 4. Os gates (congelados)

### E0-3D (engenharia — ANTES de qualquer física)
- contagem manual do menor slab causal (2 fatias = bordos de tetraedro) confere N₃,N₂,N₁,N₀;
- característica de Euler 3D (χ=0 p/ S²×S¹) preservada após 10⁴ movimentos;
- invariante de manifold (cada triângulo em exatamente 2 tetraedros; links de vértice = discos)
  preservado por **todos** os movimentos;
- reversibilidade (move∘inverso = id) e ergodicidade (autocorr finita).

### Gate de FÍSICA (o veredito de F1b — a lógica do gate de d_H 1D/2D/3D de F1)
Varrer k₀ (e Δ) e localizar as fases por seus diagnósticos conhecidos (Ambjørn–Jurkiewicz–Loll):
- **Fase "crumpled"** (k₀ pequeno): volume espacial concentrado, dimensão alta/degenerada.
- **Fase "branched-polymer"** (k₀ grande): rede ramificada, d_H degenerada.
- **Fase ESTENDIDA / "de-Sitter"** (janela intermediária): a física — o perfil de volume
  espacial médio ⟨N₃^{(3,1)}(t)⟩ tem a **forma de-Sitter** conhecida (um "blob" suave,
  ∝ cos^a(t/B), **não** uma reta nem um colapso).
- **VERDE:** as três fases aparecem E a fase estendida exibe o perfil de-Sitter (ajuste à forma
  conhecida com R² alto) E registra-se **em qual fase** (k₀,Δ) o baseline de F1b vai operar.
- **NÃO-VERDE:** falta a fase estendida, ou o perfil não bate de-Sitter → não prosseguir para a
  semente em 3D (resultado da semente sobre motor não-validado = não-interpretável).

## 5. VEREDITO DE ESTADO (honesto, 2026-06-28): **NÃO-VERDE — NÃO EXECUTADO**

**Por quê (sem maquiar).** Executar este gate = **construir e validar o motor CDT 3D completo**
(estrutura folheada de tetraedros + os 5 movimentos de Pachner 3D com bookkeeping correto +
ação dinâmica + MC + varredura de fases + ajuste de-Sitter). **Isto É a campanha F1b inteira** —
um trabalho de pesquisa de porte (as simulações AJL originais são códigos sofisticados rodados em
cluster), **não validável com confiança numa única sessão.** As Tarefas 1 e 2 foram executáveis
porque **reusaram o motor 2D já validado de F1**; a Tarefa 3 exige um motor **novo**, e não há
motor 3D no repositório (verificado).

**A disciplina deste projeto proíbe o atalho.** Produzir um motor 3D não-validado e ler "fases"
dele seria exatamente o auto-engano que o charter §3 e toda esta linha de trabalho existem para
impedir (a mesma razão pela qual a Tarefa 2 rebaixou um "positivo" que parecia bom). **Forjar um
resultado de fase 3D que eu não consiga validar é pior que declarar o gate não-executado.**

**Consequência (a lógica de decisão, respeitada):**
> Gate de fases 3D **NÃO-VERDE** ⇒ **FS-3D (o teste vinculante D2/C_mem da semente) está
> BLOQUEADO.** A construção+validação do motor 3D (F1b) é o **pré-requisito** e é a próxima
> campanha real — com seu próprio E0-3D e este gate de física, executados de verdade, antes de
> qualquer semente.

**O que esta tarefa entrega de concreto:** o **pré-registro shovel-ready** do gate (ensemble,
ação, movimentos, E0-3D, critério de-Sitter VERDE/NÃO-VERDE) — para que F1b seja executado com a
mesma disciplina de F1 (pré-registro → E0 → gate de física → síntese), e **não** uma reclamação
de fase 3D não-fundamentada.

## 6. Orçamento e riscos registrados (herdados de F1)
- **Critical slowing down:** já τ~260 sweeps em 2D (L=40); em 3D piora → F1b provavelmente
  precisa de movimentos coletivos ou mais compute para ver a fase estendida em volume suficiente.
- **Bug-density dos movimentos 3D:** os 5 Pachner 3D são a parte mais frágil → E0-3D é o filtro.
- **Volume mínimo p/ ver de-Sitter:** o "blob" só aparece em N₃ grande; sub-volume pode mascarar
  a fase estendida (risco de falso NÃO-VERDE por tamanho — registrar tamanhos testados).

---

**Resumo de uma linha:** o gate de fases 3D está **especificado e pré-registrado**, mas
**não-verde porque não-executado** — rodá-lo é construir+validar o motor CDT 3D (a campanha F1b),
que não se faz com integridade numa sessão; portanto **FS-3D (a semente em 3D) permanece
BLOQUEADO** até F1b entregar um motor 3D validado operando na fase de-Sitter.
