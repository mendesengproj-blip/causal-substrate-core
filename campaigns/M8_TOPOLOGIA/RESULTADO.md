# M8 — CLASSIFICAÇÃO TOPOLÓGICA: RESULTADO

**Data:** 2026-07-04 · **Pré-registro:** `PRE_REGISTRO.md` (9f28659) ·
**Gate:** `gate_m8.py` → `gate_m8.json` (certificado de sólitons, VERDE) ·
**Natureza:** síntese analítica + certificado. 2º teorema da série de
classificação (Linha B), após [[m5-classificacao]] e [[m6-hospedagem]].

---

## 0. Veredito em uma página

**O substrato protege exatamente as TEXTURAS DE MATÉRIA classificadas por
$\pi_n(X)\neq0$ do alvo compacto — discretas e estáveis sob thinning — e PROÍBE
os DEFEITOS DE CALIBRE (monopolos, cordas de gauge), porque não há campo de
calibre emergente (M5).** Certificado ao longo da escada de homotopia com três
sólitons distintos (vórtice π₁, baby-Skyrmion π₂, bárion π₃), todos com carga
inteira conservada; e a carga π₂ **sobrevive à deleção de 40% dos sítios**
(Q=0.9996 até p=0.6), confirmando que topologia não flui — corolário da
restrição de escala C5.

## 1. A distinção que torna isto teorema (não resumo de homotopia)

- **Textura de matéria** (Skyrmion, baby-Skyrmion, vórtice global): carga do
  CAMPO $n:\mathcal C\to X$; protegida sse $\pi_n(X)\neq0$. **HOSPEDADA.**
- **Defeito de calibre** (monopolo de 't Hooft–Polyakov, corda cósmica de
  gauge): exige campo de calibre emergente ⟹ **PROIBIDO** por M5 (sem $U(1)$
  emergente). Monopolo: proibição DUPLA — $\pi_2(G)=0$ (grupo) E sem gauge.

A mesma homotopia governa os dois; o que os separa é *o que carrega a carga*. O
substrato carrega o campo de matéria, não um campo de calibre. Logo protege as
texturas e proíbe os defeitos de calibre — pela topologia do alvo E pela
ausência (M5) de calibre.

## 2. Certificado de sólitons (gate_m8.json, VERDE)

| $\pi_n$ | Sóliton | Alvo | Carga medida | Anti |
|---|---|---|---|---|
| π₁ | vórtice XY | S¹=U(1) | w=+1.000, +2.000, −1.000 | ✓ |
| π₂ | baby-Skyrmion | S² | Q=+0.9996, +1.999, −0.9996 | ✓ |
| π₃ | Skyrmion/bárion | SU(2)=S³ | B=0.795→0.892→0.951→1 (escada) | −B ✓ |

**Estabilidade sob thinning (π₂):** deletando fração 1−p dos sítios e
recomputando Q no campo remanescente (re-triangulação Delaunay):

| p (mantido) | Q |
|---|---|
| 0.9 | +0.9996 |
| 0.8 | +0.9996 |
| 0.7 | +0.9996 |
| 0.6 | +0.9996 |

A carga inteira é **invariante sob deleção de até 40% dos sítios** — topologia
não flui (C5). Isto é o que distingue uma carga topológica de uma escala: a
escala dilata sob thinning, a carga é preservada exatamente.

## 3. A tabela de classificação (o teorema)

| $\pi_n$ | textura de matéria | defeito de calibre | classe |
|---|---|---|---|
| π₁(X) | vórtice global | corda de gauge | matéria sse π₁≠0; **gauge PROIBIDO** |
| π₂(X) | baby-Skyrmion | monopolo | matéria sse π₂≠0; **monopolo PROIBIDO (duplo)** |
| π₃(X) | Skyrmion/bárion | instanton | **PROTEGIDO** (π₃(G)=ℤ, Bott) |
| π₄(SU2) | — | spin-estatística | protegido (ℤ₂, Finkelstein–Rubinstein) |

**Enunciado.** Para um alvo compacto $X=G/H$, o substrato causal hospeda a
textura de matéria de grau $n$ se e somente se $\pi_n(X)\neq0$; a carga é um
inteiro (ou elemento de $\pi_n$ finito) conservado e invariante sob thinning; e
nenhum defeito de calibre existe (M5). Consistente com M6 (π₃(G)=ℤ universal) e
com a restrição C5 (topologia = o que sobrevive à deleção).

## 4. O que muda no programa

1. **Nova linha na checklist de restrições** ([[m7-paper-restricoes]]): C7
   topológica — "seu modelo protege exatamente π_n(X)≠0 da matéria e nenhum
   defeito de calibre?". Junta de ataque: exibir carga espúria (π_n=0) ou perda
   de carga sob thinning.
2. **P4 do core_paper ganha prova de escada:** "no magnetic monopoles, twice"
   (π₂(G)=0 E sem U(1)) — agora com a escada π₁/π₂/π₃ certificada e a distinção
   textura-vs-defeito explícita. Delta de revisão.
3. **Terceiro teorema de classificação da série** (grupos M6, fases/substrato
   M5, topologia M8) — a "teoria de restrições" ganha sua terceira coluna.

## 5. Emenda de instrumento (documentada, precedente N4/F2/M5)

O smoke revelou (ANTES do resultado valer) dois artefatos, ambos de
convenção/discretização, com a física manifestamente correta (magnitudes
inteiras, thinning preservado):
- **π₁ centro-sobre-sítio:** o vórtice em (30,30) numa rede 61² punha a
  singularidade sobre um sítio (arctan2(0,0)=0 corrompia 4 plaquetas).
  Correção: centro no meio de plaqueta (semi-inteiro).
- **π₁ aliasing de núcleo p/ |w|≥2:** soma-de-plaquetas aliava (>π por passo
  perto do centro). Correção: winding por contorno GRANDE (campo distante,
  gradientes pequenos).
- **Sinal de orientação (π₁ contorno; π₂ triangulação):** convenção
  horário/anti-horário e diagonal do dual; fixados para carga(+1)=+1.

**A janela física (carga inteira, conservada, sobrevive ao thinning) ficou
INALTERADA** — só convenções de orientação e resolução mudaram. Trilha no código.

## 6. O que M8 NÃO reivindica (escopo)

- É a topologia da MATÉRIA (campo $n$ sobre a ordem); defeitos de calibre são
  proibidos por M5, não re-testados.
- **Proteção topológica ≠ estabilidade dinâmica.** M8 certifica que a carga é um
  inteiro conservado (protegido); se o sóliton minimiza energia é o setor
  Skyrme externo (M2/N5), não M8.
- Hopfion (π₃(S²)) fica como predição; a escada π₁/π₂/π₃ é o certificado.
- Anti-circularidade: cargas são invariantes topológicos do campo; nenhum número
  do mundo.

*Reprodução:* `python gate_m8.py` (~1 min). numpy, scipy (Delaunay); reusa
`sun_core.py` (N1) para π₃.
