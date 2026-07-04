# M6 — TEOREMA DE HOSPEDAGEM: pré-registro (congelado ANTES do código)

**Data:** 2026-07-04 · **Pasta:** `FRONTEIRA_COMPACTA/M6_HOSPEDAGEM/`
**Natureza:** síntese analítica (o entregável é um teorema) + gate estrutural
barato. **Movimento 3 de [[direcao-pos-fechamento]].**
**Antecedentes:** N1 (SU(4) espelha SU(3)), F2 ([[f2-controle-g2]]: G₂ espelha),
core_paper Sec. matéria ("hosted, not selected"; camada 3 do Teorema da Fronteira).

---

## 1. A pergunta (e a resposta ao referee "por que SU(3)?")

O programa mediu SU(3), SU(4) e G₂ produzirem a MESMA forma fenomenológica
(ordenamento a J finito; Goldstones; carga topológica inteira; confinamento
σ>0). A pergunta:

> **Isto é coincidência de três casos, ou o substrato hospeda QUALQUER grupo
> compacto por um mecanismo — de modo que a forma emergente é uma função
> a-priori da teoria de representação/topologia de G, e o grupo específico é
> INPUT do mundo, não seleção do substrato?**

## 2. O mecanismo proposto (a tese)

**Tese central.** O acoplamento do Axioma 2 é um funcional invariante de
$n_i\cdot n_j$ que depende de $G$ **apenas através da métrica bi-invariante
(Killing)** do grupo compacto — a energia é $E=-J\sum_{\langle ij\rangle}
\tfrac1{\dim_f}\mathrm{Re}\,\mathrm{Tr}(U_iU_j^\dagger)=-J\sum v_i\!\cdot\!v_j$
com $v$ na métrica bi-invariante. Todo grupo compacto tem uma (única a menos de
escala por fator simples). Logo o substrato **não consegue distinguir** grupos
além de: dimensão, estrutura de coset, e topologia. Consequência:

**Teorema de hospedagem (a provar/montar).** Para todo $G$ compacto (simples) e
alvo $X=G/H$, o substrato hospeda $X$ com a forma:
1. **Contagem de Goldstone $=\dim(X)=\dim G/H$** (geradores quebrados; teorema
   de Goldstone) — mede-se dim, não "N".
2. **Carga topológica em $\pi_3(X)$**; para $G$ simples compacto $\pi_3(G)=
   \mathbb{Z}$ (Bott) — inteiro protegido, universal.
3. **Multipletos $=$ irreps do $H$ não-quebrado** (Peter–Weyl: $H$ compacto ⟹
   irreps discretas de dim finita).
4. **Confinamento σ>0 no acoplamento forte**, do desenvolvimento de caracteres
   do grupo compacto, **independente do centro** (medido em F2 p/ $Z(G_2)=1$).

O grupo é INPUT; 1–4 são OUTPUT a-priori. "A forma deriva; o grupo postula-se."

## 3. O gate (barato, estrutural — NÃO é campanha de ordenamento)

`gate_m6.py`. Reusa os motores existentes; mede só invariantes ESTRUTURAIS
(baratos: contagem de Goldstone por twist estático + carga π₃ por hedgehog),
NUNCA a MC de ordenamento/transição (respeitando "SU(5+) nunca" = a política é
sobre a MC cara de fase, não sobre teoria de grupos barata).

- **(G-count) Goldstone = dim X**, por twist estático (protocolo D2, reusado de
  F2/N1), para os alvos com motor pronto:
  - SU(2) → 3, SU(3) → 8, SU(4) → 15 (Gell-Mann, `sun_core`);
  - G₂ → 14 (`g2_core`);
  - **COSET O(3)=SU(2)/U(1)=S² → 2** — a PROVA AFIADA: se a contagem é 2 (=dim
    G/H) e NÃO 3 (=dim SU(2)), a forma rastreia o COSET $X$, não o grupo $G$.
- **(π₃) carga inteira** por hedgehog (reusa `baryon_number`): $B\in\mathbb{Z}$,
  escada monótona, anti $=-B$, p/ SU(N) e G₂ (já em N1/F2; reconfirmar barato).
- **(tabela a-priori)** predição de dim G/H e π₃ para grupos NÃO simulados
  (SU(5), SO(5), Sp(2), F4, E6) — pura teoria de grupos, sem MC.

## 4. Previsões congeladas

| Alvo | dim G/H (Goldstones) | π₃ | fonte |
|---|---|---|---|
| SU(2) | 3 | ℤ | motor |
| SU(3) | 8 | ℤ | motor (N1) |
| SU(4) | 15 | ℤ | motor (N1) |
| G₂ | 14 | ℤ | motor (F2) |
| **O(3)=S²** | **2** | ℤ (Hopf) | motor (coset) |
| SU(5) | 24 | ℤ | a-priori |
| SO(5)/Sp(2) | 10 | ℤ | a-priori |
| F4 | 52 | ℤ | a-priori |
| E6 | 78 | ℤ | a-priori |

## 5. Mortes pré-registradas

- **D-M6-1 (substrato ADICIONA/SUBTRAI estrutura):** algum alvo com motor cujo
  Goldstone medido ≠ dim X (robusto), ou carga não-inteira/não-π₃ ⟹ o substrato
  NÃO é fiel/genérico; a camada 3 seleciona ⟹ revisão do "hosted, not selected".
- **D-M6-2 (coset falha):** O(3)/S² dá 3 (não 2) ⟹ a forma rastreia o GRUPO, não
  o coset ⟹ a tese "forma = função de X" cai; reformular.
- Regra: contagem de Goldstone com critério de F2 (dE>0, dE~k², robusto);
  nenhuma janela movida pós-dado.

## 6. O que M6 NÃO reivindica

- **Existência (ordenamento a J finito) é DINÂMICA e medida**, não derivada
  (mesma ressalva de N1/F2); M6 é sobre a FORMA quando ordena, não sobre SE
  ordena. Não simula ordenamento novo (respeita "SU(5+) nunca").
- A síntese usa teoremas padrão (Goldstone, Bott $\pi_3$, Peter–Weyl); a
  novidade é o MECANISMO (acoplamento fatora pela métrica bi-invariante ⟹
  genérico) + a moldura de functor + a prova-de-coset.
- Grupos não-compactos, ou com métrica bi-invariante degenerada, ficam fora.
- Anti-circularidade: nenhum número do mundo; contagens (dim, ℤ) são teoria de
  grupos; o twist/hedgehog usa só os geradores.
