# N5 / M2 — SKYRME_RADIATIVO: resultado

**Data:** 2026-07-02 · **Pré-registro:** `PRE_REGISTRO.md` (+ adendo de instrumento,
escrito pós-G3-vermelho e ANTES de qualquer medida de loop válida).

## VEREDITO: **D1 — MORTE TOTAL DA ROTA RADIATIVA** (pelas duas sub-condições, a ~130σ)

```
D1a  c_K^loop = −0.012961 ± 0.000097   (L=8, 8 seeds; L=6: −0.012865 ± 0.00014)
     O loop NÃO gera canal de Skyrme estabilizador: gera o canal com o
     SINAL ERRADO (anti-estabilizador), com estabilidade de volume perfeita.
D1b  α₄_loop^B = −0.1380 ± 0.0011      (quártico de loop do hedgehog < 0)

Corolário mais forte que o pré-registrado: como o termo de loop é
INDEPENDENTE DE J (ln det(J·h) = const + ln det h) e a árvore é negativa,
   Q(J) = J·e₄_tree^B + α₄_loop^B < 0  PARA TODO J ≥ 0
— não existe janela em acoplamento NENHUM, não apenas em J ≥ J_c = 0.045(5).
D2/D3 e Fase 3 (Derrick): não alcançadas (funil); a janela não existe.
```

O Skyrme permanece **[EXTERNO com prova]** — e a prova fica mais forte: a
dominância não emerge em árvore (identidade pontual, SD1–SD5) **nem em 1-loop
(medido aqui)**. A esperança Q20 ("2 axiomas secos") morre; a versão mínima da
teoria segue **2 axiomas + 2 externos com prova**.

## Números (instrumento toro+transportadores; por nó; J=1 na árvore)

| quantidade | L=6 (8 seeds) | L=8 (8 seeds) |
|---|---|---|
| árvore bare e₄^A (U≡1, cosseno SC1) | −6.295 ± 0.057 | −7.109 ± 0.061 |
| árvore bare e₄^B | −3.367 ± 0.025 | −3.956 ± 0.030 |
| razão bare B/A (âncora 5/9 = 0.5556) | 0.5349 ± 0.0011 | **0.5565 ± 0.0010** |
| árvore relaxada e₄^A / e₄^B | −6.009 / −3.444 | −6.832 / −4.039 |
| razão relaxada B/A | 0.5732 ± 0.0014 | 0.5912 ± 0.0013 |
| loop α₄^A | −0.04796 ± 0.00062 | −0.06023 ± 0.00059 |
| loop α₄^B | −0.12515 ± 0.00089 | −0.13800 ± 0.00114 |
| razão loop B/A | 2.612 ± 0.031 | **2.291 ± 0.007** |
| c_S^loop = α₄^A/9 | −0.005329 ± 0.00007 | −0.006692 ± 0.00007 |
| c_K^loop = (α₄^B−α₄^A)/6 | −0.012865 ± 0.00014 | **−0.012961 ± 0.00010** |
| loop α₂ (renorm. quadrática) | — | −0.796 (A) / −0.796 (B) |
| a_eff (comprimento espacial médio de link) | 2.027 | 2.080 |
| deslocamento de estabilidade (drop-2-g) | ≤ 2e−5 | ≤ 1.2e−4 |

**Controle cúbico periódico (L=8³):** bare A ≡ bare B = −3/384 EXATO (cegueira
da grade, máquina); relaxada ≡ bare (twist uniforme é estacionário na grade —
vestidura de meio nula); loop α₄^A = −0.03428, α₄^B = −0.02821 ⇒
c_K^loop,cúbico = **+0.00101** (fraco, estabilizador) mas α₄^B < 0 ainda.

**J_c (G5):** SU(2) quiral no MESMO substrato torus: J_c ≈ 0.045 (pico de χ
interior ao grid {0.02…0.06}; desordenado limpo em J=0.02; τ_int/ESS no JSON).

## O que foi estabelecido (e é novo)

1. **A porta radiativa está fechada — por medida, com o sinal identificado.**
   Q20 perguntava se integrar flutuações gera o termo de Skyrme com coeficiente
   efetivo. Resposta: gera um canal K radiativo, mas com o **sinal
   anti-estabilizador**, e o quártico de loop do hedgehog é ele próprio
   saturante. Combinado com a árvore (teorema SD), o quártico líquido do
   hedgehog é negativo em TODO acoplamento — a morte não depende de J_c.

2. **O loop é PIOR que a árvore no canal do hedgehog.** A razão B/A do loop é
   ≈ 2.3 (contra 5/9 ≈ 0.56 da árvore): as flutuações respondem MAIS à
   curvatura isospin-tripla do hedgehog do que ao twist abeliano — mais
   repulsão de níveis na Hessiana, mais ln det, mais saturação. A hierarquia
   K ≤ ⅔S da árvore não se transfere ao loop; o loop inverte o sentido.

3. **Contraste Poisson × grade (radiativo).** SD mostrou que a isotropia de
   Poisson é o ÓTIMO do canal K em árvore (e a grade é cega). No loop o
   contraste INVERTE: a grade gera c_K^loop fracamente POSITIVO (+0.001), o
   Poisson gera NEGATIVO (−0.013, 13× maior em módulo). A mesma isotropia que
   gera o operador em árvore é a que o mata radiativamente. (Observação
   medida; mecanismo heurístico: os links isotrópicos acoplam todas as
   direções de isospin do hedgehog em todos os eixos espaciais.)

4. **Vestidura de meio é suave no instrumento certo.** No toro sem fronteira,
   a razão de árvore relaxada (0.59) fica perto da bare (0.556) — o meio
   desordenado renormaliza sem destruir a estrutura de canais. (O instrumento
   clampado, retirado no adendo, tinha razão −1.3: artefato de fronteira, não
   física — diagnóstico preservado em `n5_phase0_clamped.json`.)

5. **Âncora 5/9 verificada em população nova de links** (Hasse min-image no
   toro, L=8): 0.5565 ± 0.0010 — terceira verificação independente da isotropia
   de SC1/SD3, convergindo com o volume (L=6: 0.535).

## Limitações honestas (declaradas)

- **1-loop apenas** (determinante gaussiano na sela restrita). Perto de J_c
  ordens superiores importam; mas árvore e loop têm o MESMO sinal no canal do
  hedgehog — não há janela a ser aberta por correções pequenas, e "loops
  maiores resgatam" exigiria inversão de sinal de uma série cujos dois
  primeiros termos são negativos e grandes.
- O coeficiente de loop foi medido na resposta a twist de fronteira
  (transportadores) do mínimo restrito — o mesmo instrumento nos dois canais e
  nas duas ordens; a decomposição c_S/c_K herda a aproximação de invariantes
  realizados (vigiada por G3-bare na máquina e razão 5/9).
- A expectativa contínua da pergunta (ChPT gera l₂ tipo-Skyrme positivo em
  4D contínuo) NÃO se reproduz aqui — o objeto desta campanha é a teoria
  estatística no substrato causal, que é o que a TEIC é. O desacordo é
  informação sobre o substrato, não erro do contínuo.

## Consequências para o programa (Linha 1 / ROADMAP V2)

- **M2 executado; a teoria congelada v1.0 fica como está:** 2 axiomas + 2
  externos com prova. O item 3 da LISTA HONESTA muda de "N5 pode derrubar"
  para "N5 executado: não derruba — reforça (árvore: teorema; loop: medido)".
- O paper-núcleo (M4) ganha a frase: *"the Skyrme stabiliser is external by
  necessity: its dominance cannot emerge at tree level (pointwise identity)
  and does not emerge radiatively (measured one-loop channel coefficient
  c_K^loop < 0 at 130σ, volume-stable), so the non-cosine core cost is a
  genuine axiom-level input of the matter sector"*.
- Morte parcial pré-registrada no charter ("emerge pequeno demais") era o
  desfecho provável; o desfecho real é MAIS limpo: nem pequeno — de sinal
  contrário. Não há razão para N5b.
- Próximo da fila (ROADMAP V2): **M4 paper-núcleo** (v0), com M1 (tricotomia)
  e agora M2/N5 prontos como seções; M1b atrás.

## Higiene N-hig (cumprida)

- Medida principal sem MC (determinante determinístico); τ_int/ESS no único
  MC (G5), janela de Sokal, por (J, seed).
- Dois algoritmos de ln det (Cholesky vs autovalores, 1e−15); Newton-CG
  verificado contra splu (4e−14); gradiente/Hessiana contra diferenças
  finitas (G0, com transportadores genéricos).
- Janelas declaradas antes de rodar; regra drop-2-g: deslocamentos ≤ 1.2e−4
  (três ordens abaixo do sinal).
- Segundo operador BD: N/A declarado.

## Artefatos

| arquivo | conteúdo |
|---|---|
| `PRE_REGISTRO.md` | pré-registro + adendo de instrumento (datado) |
| `n5_core.py` | motor: toro causal min-image, transportadores, Hessiana analítica, Newton-CG, ln det duplo |
| `n5_phase0.py` / `n5_phase0.json` | gates G0–G4 (todos verdes) |
| `n5_phase0_clamped.json` | 1º instrumento (clampado): G3 vermelho — retirado |
| `n5_phase0_jc.py` / `n5_phase0_jc.json` (+`_box`, `_run1`) | G5: J_c = 0.045 no toro (e trilha de refinamento) |
| `n5_phase1.py` / `n5_phase1.json` | medida principal: 8+8 seeds, 2 canais, controle cúbico |
| `n5_phase2.py` / `n5_phase2.json` | aritmética de morte: **D1** |
| `n5_phase3.py` | Derrick condicional — NÃO executado (funil) |

Reprodução: `python n5_phase0.py` (~10 min) → `python n5_phase0_jc.py`
(~25 min) → `python n5_phase1.py` (~45 min) → `python n5_phase2.py` (~1 s).
