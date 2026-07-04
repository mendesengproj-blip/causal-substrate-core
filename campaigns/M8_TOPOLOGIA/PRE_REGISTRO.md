# M8 — CLASSIFICAÇÃO TOPOLÓGICA: pré-registro (congelado ANTES do código)

**Data:** 2026-07-04 · **Pasta:** `FRONTEIRA_COMPACTA/M8_TOPOLOGIA/`
**Natureza:** síntese analítica (teorema) + certificado de sólitons.
**Movimento:** o 2º da série de classificação (Linha B), após [[m5-classificacao]]
(SNA) e [[m6-hospedagem]]. Adiciona uma linha à checklist de [[m7-paper-restricoes]].

---

## 1. A pergunta

Dado um alvo compacto $X=G/H$ para o campo de matéria $n:\mathcal C\to X$, **quais
cargas topológicas o substrato causal protege, e quais proíbe?**

## 2. A tese (a classificação)

Os defeitos/texturas em $d$ dimensões espaciais são classificados pelos grupos de
homotopia $\pi_n(X)$. A tese:

> **O substrato protege exatamente as TEXTURAS DE MATÉRIA classificadas por
> $\pi_n(X)\neq0$** — discretas (compacidade ⟹ $\pi_n$ finitamente gerado) e
> **estáveis sob thinning** (topologia não flui sob deleção; corolário da
> restrição de escala C5). **E PROÍBE os DEFEITOS DE CALIBRE** (monopolos,
> cordas de gauge) — porque não há campo de calibre emergente (M5 / no-photon).

Distinção central (o que torna isto teorema, não resumo de homotopia):
- **Textura de matéria** (Skyrmion, baby-Skyrmion, Hopfion, vórtice global):
  carga do CAMPO $n$; protegida sse $\pi_n(X)\neq0$. HOSPEDADA.
- **Defeito de calibre** (monopolo de 't Hooft–Polyakov, corda cósmica de
  gauge): exige campo de calibre emergente ⟹ PROIBIDO. Para o monopolo,
  proibição DUPLA: $\pi_2(G)=0$ (grupo) E sem $U(1)$ emergente.

## 3. A tabela de classificação (predição congelada)

| $\pi_n$ | textura de matéria | defeito de calibre | veredito na classe |
|---|---|---|---|
| $\pi_1(X)$ | vórtice global | corda de gauge | matéria: sse $\pi_1\neq0$; gauge: PROIBIDO |
| $\pi_2(X)$ | baby-Skyrmion | monopolo | matéria: sse $\pi_2\neq0$; monopolo: PROIBIDO (duplo) |
| $\pi_3(X)$ | Skyrmion/bárion | instanton | PROTEGIDO ($\pi_3(G)=\mathbb Z$, Bott) |
| $\pi_4(SU2)$ | — | spin-estatística | protegido ($\mathbb Z_2$, Finkelstein–Rubinstein) |

Valores de homotopia (teoria de grupos, congelados): $S^1{=}U(1)$: $\pi_1{=}\mathbb Z$;
$S^2$: $\pi_2{=}\mathbb Z,\pi_3{=}\mathbb Z$(Hopf); $S^3{=}SU(2)$: $\pi_3{=}\mathbb Z,
\pi_4{=}\mathbb Z_2$; $SU(3),G_2$: $\pi_3{=}\mathbb Z$.

## 4. O gate (certificado de sólitons — barato, estrutural)

`gate_m8.py`. Verifica que as texturas de matéria PROTEGIDAS têm carga INTEIRA
conservada, ao longo da escada de homotopia, com sólitons distintos:
- **$\pi_1$ — vórtice XY** (alvo $S^1$, 2D): campo $\theta(x,y)$; winding
  $w=\tfrac1{2\pi}\oint\nabla\theta\cdot d\ell$. Congelado: $w\in\mathbb Z$ p/
  $w=1,2$; anti $=-w$.
- **$\pi_2$ — baby-Skyrmion** (alvo $S^2$, 2D): $n(r,\varphi)$ hedgehog-2D;
  carga $Q=\tfrac1{4\pi}\int n\cdot(\partial_x n\times\partial_y n)$. Congelado:
  $Q\to\mathbb Z$ p/ $Q=1,2$; anti $=-Q$.
- **$\pi_3$ — Skyrmion/bárion** (alvo $SU(2){=}S^3$, 3D): reusa
  `sun_core.embedded_hedgehog` + `baryon_number` (já em M6/N1). Congelado:
  $B\to\mathbb Z$ escada, anti $=-B$.
- **Estabilidade sob thinning** ($\pi_2$): deletar fração $1{-}p$ dos sítios e
  reconstruir $Q$ no campo remanescente — a carga inteira SOBREVIVE (topologia
  não flui, C5). Congelado: $Q$ preservado (desvio < 0.15) até $p=0.6$.

## 5. Mortes pré-registradas

- **D-M8-1 (substrato NÃO protege):** alguma textura de matéria com
  $\pi_n(X)\neq0$ cuja carga medida é NÃO-inteira, NÃO-conservada, ou NÃO
  sobrevive ao thinning ⟹ a classificação falha; a proteção topológica não é
  genérica.
- **D-M8-2 (substrato ADICIONA topologia):** carga espúria num alvo com
  $\pi_n(X)=0$ ⟹ o substrato cria estrutura topológica não do alvo.
- Regra: cargas com tolerância declarada (inteiro ± 0.1 na escada de
  discretização; anti $=-$carga a 1e-6); nenhuma janela movida pós-dado.

## 6. O que M8 NÃO reivindica (escopo)

- É a topologia da MATÉRIA (campo $n$ sobre a ordem); os defeitos de calibre
  ficam proibidos por M5 (sem campo emergente), não re-testados aqui.
- Existência dinâmica (se o sóliton é estável energeticamente / minimiza) é
  outra questão; M8 é sobre a PROTEÇÃO topológica (carga discreta conservada),
  não sobre dinâmica de estabilização (isso é o setor Skyrme externo).
- Hopfion ($\pi_3(S^2)$) fica como predição (carga de Hopf cara de medir);
  a escada $\pi_1/\pi_2/\pi_3$ é o certificado.
- Anti-circularidade: cargas são invariantes topológicos (teoria de grupos +
  o campo); nenhum número do mundo.
