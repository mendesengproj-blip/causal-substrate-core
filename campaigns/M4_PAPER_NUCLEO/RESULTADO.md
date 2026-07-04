# M4 — PAPER-NÚCLEO: resultado (v0)

**Data:** 2026-07-02 · **Pasta:** `FRONTEIRA_COMPACTA/M4_PAPER_NUCLEO/`
**Roadmap:** `../ROADMAP_V2.md` item M4 ("axiomas → teoremas → corolários →
LIMITES; v0 pode nascer JÁ de N0+N0′; endurece conforme M1–M3").

## ENTREGÁVEL: `core_paper.tex` / `core_paper.pdf` — 7 pp, revtex4-2, compila limpo

*"What a Lorentz-invariant discrete order can carry: an axiomatic core for
emergence on causal substrates"* — o paper-núcleo v0, com a arquitetura
axiomática completa:

| Seção | Conteúdo | Fonte |
|---|---|---|
| §2 Axiomas | Axioma 1 (Poisson FORÇADO por BHS) + Axioma 2 (campo compacto genérico) + classe intrínseca + **Lema do par** ("tempo com sinal, espaço sem sinal e sem estrutura") + âncoras Malament/antichain | N0 §1–2 |
| §3 Teorema da Fronteira | 3 camadas (órbitas não-compactas ⇒ divergência; componentes desconexas ⇒ bits não-fixáveis; parte compacta ⇒ índices discretos) + tabela de corolários + escopo cinemático declarado + precedente de Wigner | N0 §1–2 |
| §4 Tricotomia combinatória | **T1 dobradiça (prova completa no paper)**, T2 exchangeable, T3 box orders, T4 posts/TP; 2 retrodições; flanco pentagonal declarado | M1 |
| §5 Fronteira de assinatura | definida-vs-indefinida; Wick = a operação que cruza; ponte ao paper Wen (companion) | N0(c) |
| §6 RG de thinning | ponto fixo exato + atrator global (+ lema δ₀ de N0′) + sem direção relevante; ρ = unidade única | N0(b)+N0′ |
| §7 No-go de paridade | Lemas 1–3 (isometrias, Gram, quenched de N0′-A2) + teorema P forte + assimetria P/T honesta + CP≡C | N0(d)+N0′ |
| §8 Setor de matéria | família de índices {π₃, π₄, reps H, dim G/H}, raiz única = compacidade; "hospedado, não selecionado" (N1); existência = medida | N0 §2.4 + N1 |
| §9 **Os 2 externos com prova** | Skyrme: operador derivado (SC) + dominância impossível em árvore (SD teorema) **+ 1-loop medido c_K^loop=−0.01296±0.0001 (~130σ)** ⇒ input de nível-axioma localizado por impossibilidade nas duas ordens; unidade única (ρ marginal ⇒ 1 número importado) | SD + **M2/N5** |
| §10 Vacina | onde o princípio NÃO entrega: entropia de matéria super-área (N2-F2, exibida como falha da lei de área), dinâmica, estrutura quântica | N2 + charter regra 2 |
| §11 Previsões | P1–P7 (+2 bônus: classe GOE, frac_B∝H² de N0′-A4) | N0(e)+N0′ |
| §12 LISTA HONESTA | as 10 fronteiras da ROADMAP_V2, como tabela | ROADMAP_V2 |
| §13 Como quebrar | juntas nomeadas de ataque (falseabilidade estrutural) | — |

## Decisões editoriais (registradas)

1. **Título pela pergunta-mestra** ("o que é permitido emergir?" → "what … can
   carry"), não pelo programa — o paper é o núcleo dedutivo, não um review.
2. **Disciplina de alegação do charter no §1:** tudo é sobre a CLASSE; graus
   epistêmicos explícitos [theorem]/[sketch]/[measured]; a vacina é SEÇÃO.
3. **T1 com prova completa dentro do paper** (3 linhas de enunciado, 4 de
   prova) — é o teorema mais citável; os demais citados com esboço.
4. **M2/N5 entrou como metade radiativa da prova de necessidade do Skyrme**
   (§9.1) — o paper já nasce com o resultado desta sessão integrado.
5. **Não duplica o paper Wen (N3):** a conexão string-net aparece como 1 linha
   da tabela de corolários + §5 curto com \cite{WenComplement}.
6. Bibliografia mínima real (Malament, HKM, BHS, Surya, Levin–Wen, Wigner,
   Janson, Brightwell, Rideout–Sorkin, ABBJ, Bollobás–Brightwell, Kallenberg,
   Elitzur) + 3 companions. Volumes conferidos na redação final (M3).

## M3 — ENDURECIMENTO + DELTAS N4 (EXECUTADO 03jul26)

**Compila limpo:** 8 pp, 3 passes pdflatex, zero refs indefinidas, 1 overfull
residual de 4.8pt (tabela das fronteiras, pré-existente, inalterado).

**Os 3 deltas da campanha N4 (RESULTADO.md §3) escritos no paper, SEM upgrade
retórico:**
1. **Δ1 porta-ℏ (§10 "Quantum structure" + P1 + fronteira 4):** a quantização
   covariante/SJ forçada (canônica sem carregador) é MEDIDA a abrir — vácuo
   estável, ramo IR relativístico c=0.96 (d2)/0.90 (d4), controle massivo ~2%;
   custo estrutural = 1 bit-T [teorema] carregando a estrutura complexa
   (consistente com GOE). Aberto: valor de ℏ, colapso.
2. **Δ2 camada-3-no-quântico (§8 matéria + fronteira 2):** multipleto Goldstone
   SOBREVIVE à quantização SJ sobre o vácuo ordenado MEDIDO (splittings q~cl,
   limiar 3× não aproximado; degrada no desordenado ⇒ vácuo ordenado = portador);
   espectro não-degenerado (gap ~1e-3) ⇒ estabilizador U(1)^K abeliano, NENHUMA
   fibra criada ⇒ Axioma 2 postulado [delimitação, agora medido]. "Formas
   derivam, grupos postulam-se" sobrevive no setor quântico.
3. **Δ3 face-entrópica-refinada (§10 "Horizon entropy"):** corte UV declarado
   LOCALIZA a SSEE na fronteira (razão 0.93 vs 4.0 volume = resgate QUALITATIVO
   da área) MAS a escala é do corte, não da geometria (κ=1.57, n∝N_O^{3/4});
   entre resgate-total e 4ª-face-bruta; fronteira L={4,6} declarada aberta.

**Endurecimento do Apêndice B:** Lemas 0/2/δ₀ e a Prop. dos autovalores do
thinning JÁ estavam com prova livro-texto no Apêndice A do v0 (par timelike/
spacelike, δ₀ via Weil + desintegração de órbita, exhaustão P-ímpar, quenched
local, ponto-fixo+autovalores); resíduos honestos (quenched com cluster de
frame comum) mantidos como [sketch] — endurecê-los seria upgrade retórico.
Única melhoria de grau: Prop. box-orders (T3) [sketch]→[theorem, cited anchor]
(é teorema de Brightwell 1993, alinhado à convenção de T4).

**Bibliografia CONFERIDA na fonte (03jul26):** as 3 entradas de combinatória
mais propensas a erro verificadas online — ABBJ1994 Ann. Appl. Probab. **4**,
108 (1994) ✓; Bollobás–Brightwell1997 SIAM J. Discrete Math. **10**, 318
(1997) ✓; Janson2011 Combinatorica **31**, 529 (2011) ✓; demais entradas
(BHS, Malament, HKM, Levin–Wen, Wigner, Elitzur, Brightwell–Gregory,
Rideout–Sorkin, Surya, Rideout–Wallden, Folland, Kallenberg) conferidas
contra registro-padrão, todas corretas.

**Estado:** Linha 1 COMPLETA (M1–M4) + M3-endurecimento + deltas N4 integrados.
Decisão humana pendente: venue (junto com o paper Wen).

## O que v0 ainda NÃO é (endurecimento pendente = M3) — SUPERADO acima

- Referências bibliográficas com volume/página a conferir (M1 §Literatura).
  — FEITO (ver acima).
- Decisão humana pendente: venue (junto com a do paper Wen) e se o
  paper-núcleo espera M3 ou submete como perspective/axiomatic v0. — M3 FEITO;
  resta só a decisão de venue.

## Estado da Linha 1 após esta sessão

```
M1 ✅ (tricotomia)   M2 ✅ (D1 morte radiativa)   M4 ✅ v0 (este paper)
M3 = próximo analítico (endurecer Apêndice B → sobe os [sketch] do paper)
M1b = fila (flanco pentagonal)
```

Reprodução: `pdflatex core_paper.tex` ×2 (bibliografia embutida em
`thebibliography`; sem bibtex necessário). 7 pp; 1 overfull residual de 4.8pt
(tabela das fronteiras); zero referências indefinidas.
