# M6 — TEOREMA DE HOSPEDAGEM: RESULTADO

**Data:** 2026-07-04 · **Pré-registro:** `PRE_REGISTRO.md` (a8009a9) ·
**Gate:** `gate_m6.py` → `gate_m6.json` (estrutural, barato) ·
**Natureza:** síntese analítica + certificado estrutural. Movimento 3 de
[[direcao-pos-fechamento]].

---

## 0. Veredito em uma página

**O substrato hospeda QUALQUER grupo compacto por um mecanismo; a forma
emergente é uma função a-priori do alvo $X=G/H$, e o grupo específico é INPUT do
mundo, não seleção do substrato.** Confirmado: contagem de Goldstone = $\dim X$
em cinco alvos incluindo o **coset O(3)=S²** (a prova afiada: 2 = dim do coset,
não 3 = dim do grupo); carga $\pi_3$ inteira universal; tabela a-priori para
grupos não-simulados. "A forma deriva; o grupo postula-se" agora tem mecanismo.

## 1. O mecanismo (a tese, confirmada)

O acoplamento do Axioma 2, $E=-J\sum \tfrac1{\dim_f}\mathrm{Re}\,\mathrm{Tr}
(U_iU_j^\dagger)=-J\sum v_i\!\cdot\!v_j$, depende de $G$ **apenas através da
métrica bi-invariante (Killing)** — que todo grupo compacto tem. O substrato,
portanto, não consegue distinguir grupos além de: **dimensão, estrutura de
coset, topologia**. Logo a hospedagem é genérica *por construção*, e as três
medições prévias (SU(3)/SU(4)/G₂) concordarem não é coincidência: é a
consequência do acoplamento fatorar pela métrica universal.

## 2. O teorema de hospedagem (montado + certificado)

Para todo $G$ compacto simples e alvo $X=G/H$, o substrato hospeda $X$ com:

| Peça | Forma a-priori | Fonte | Certificado |
|---|---|---|---|
| Goldstones | $\dim X=\dim G/H$ | teorema de Goldstone | **medido, 5 alvos** |
| Carga topológica | $\pi_3(G)=\mathbb{Z}$ (Bott) | Bott | **medido (escada B)** |
| Multipletos | irreps do $H$ não-quebrado | Peter–Weyl | octeto SU(3) [N1] |
| Confinamento | $\sigma>0$ forte, **indep. de centro** | caracteres | G₂ $Z=1$ [F2] |

**Certificado de Goldstone (gate, twist estático):**

| Alvo | dim X | Goldstones medidos |
|---|---|---|
| SU(2) | 3 | **3/3** |
| SU(3) | 8 | **8/8** |
| SU(4) | 15 | **15/15** |
| G₂ | 14 | **14/14** |
| **O(3)=SU(2)/U(1)=S²** | **2** | **2/2** |

**A prova afiada (coset).** O(3)/S² dá **2** Goldstones, não **3**. Se a forma
rastreasse o GRUPO (SU(2), dim 3), seriam 3. Rastreia o COSET $X$ (S², dim 2).
Isto separa "forma = função de $X$" de "forma = função de $G$" empiricamente —
a tese passa no caso que a distingue.

**Certificado de $\pi_3$.** As escadas de carga (hedgehog) de SU(2) e SU(3) são
**idênticas** — $B=0.7947,\,0.8921,\,0.9507\to1$ em $L=15,21,31$, monótonas,
anti $=-B$. O inteiro topológico independe de $N$ (Bott: $\pi_3(G)=\mathbb{Z}$
para todo compacto simples; o log age só no bloco SU(2)) [medido].

## 3. Tabela a-priori (predição, sem simulação — respeita "SU(5+) nunca")

O teorema PREDIZ, por pura teoria de grupos, os alvos não-simulados:

| Alvo | dim (Goldstones) | $\pi_3$ |
|---|---|---|
| SU(5) | 24 | ℤ |
| SO(5) / Sp(2) | 10 | ℤ |
| F4 | 52 | ℤ |
| E6 | 78 | ℤ |

Nenhuma MC de ordenamento foi rodada (a política "SU(5+) nunca" é sobre a
campanha cara de fase; a contagem estrutural é teoria de grupos barata). As
predições são falsificáveis por quem quiser simular.

## 4. O que muda no programa

1. **Resposta ao referee "por que SU(3)?"** pronta: o substrato hospeda todo
   compacto; SU(3) é a escolha do mundo (o mínimo que dá cor); o que emerge é a
   ESTRUTURA (Goldstones dim $G/H$ + $\pi_3$ + irreps $H$ + $\sigma>0$), a-priori
   do alvo. Delta de revisão para o core_paper Sec. matéria: enunciar como
   TEOREMA (mecanismo bi-invariante) + a tabela + a prova-de-coset.
2. **A camada 3 do Teorema da Fronteira ganha seu functor:** o substrato é uma
   aplicação (grupos compactos → fenomenologia) que fatora pela métrica
   bi-invariante. O Axioma 2 é genérico de verdade — agora com mecanismo, não só
   três medições.

## 5. O que M6 NÃO reivindica (escopo)

- **Existência (ordenamento a J finito) é DINÂMICA e medida** [N1/F2], não
  derivada; M6 é sobre a FORMA quando ordena. Nenhum ordenamento novo simulado.
- Síntese de teoremas padrão (Goldstone, Bott, Peter–Weyl) + o mecanismo
  bi-invariante (novo) + a prova-de-coset (nova). Não reivindica novidade nos
  teoremas citados.
- Grupos não-compactos ou com métrica bi-invariante degenerada ficam fora.
- Anti-circularidade: contagens (dim, ℤ) são teoria de grupos; twist/hedgehog
  usam só geradores; nenhum número do mundo.

*Reprodução:* `python gate_m6.py` (~1 min). numpy; reusa `sun_core.py` (N1) e
`g2_core.py` (F2).
