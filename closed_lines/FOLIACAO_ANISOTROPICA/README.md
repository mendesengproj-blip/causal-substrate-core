# FOLIACAO_ANISOTROPICA — substrato foliado anisotrópico (Hořava–Lifshitz discreto)

> # ⚠️ **ESTE PROGRAMA NÃO É MAIS LORENTZ-INVARIANTE MANIFESTO.**
> Toda esta linha adota uma **foliação preferida** (uma noção de "agora") e usa
> **distância intra-fatia**. Isto **quebra a invariância de Lorentz local** (recuperável
> só dinamicamente no IR, em tese — frágil). É a **gravidade de Hořava–Lifshitz
> discreta** / *shape dynamics*. **Condição do autorizador:** qualquer resultado futuro
> desta linha DEVE carregar este rótulo em negrito no topo. Não é uma vitória do programa
> Lorentz-invariante (TEIC/causal sets) — é a confirmação de que aquele programa estava
> bloqueado **pela** invariância de Lorentz.

---

## De onde vem

`SINTESE_SETE_MORTES/RESULTADO.md` (2026-06-30) mostrou que as sete mortes do programa de
escala emergente têm **estrutura binária**: ou **BOOST** (não-compacidade do hiperbolóide
⇒ ⟨z⟩=∞) ou **COMBINATÓRIA** (laços: árvore/Bethe), ligadas pela **dobradiça do eixo do
tempo**. A teoria de grupos prova: escapar do BOOST exige **órbita compacta** ⇒ quantidade
definida numa **fatia espacial** (grupo `SO(d−1)` compacto) ⇒ **foliação preferida** ⇒
abandona a premissa de Lorentz. Essa é a **única saída estrutural** — e leva diretamente à
gravidade de Hořava–Lifshitz. Esta linha testa esse candidato (o apêndice da síntese),
autorizado explicitamente.

## O que esta linha busca

Primeiro: o **gatilho cinemático** — ⟨z⟩(N) finito **E** C4(N) positivo saturando, para
um espaço-tempo foliado genuíno (λ>0, percolando no tempo). Depois (só com autorização):
se há **criticalidade/escala genuína** ou se é apenas um grafo geométrico trivial.

## Estado atual

| Campanha | Veredito | Diretório |
|---|---|---|
| Gatilho foliado (λ ajustável) | **`GATILHO_ARMA`** (ambas as barreiras; NÃO Lorentz-inv.) | `campaigns/GATILHO_FOLIADO/` |
| Criticalidade genuína (ferromagneto O(3) vs controle reticulado) | **`CRITICALIDADE DE RETICULADO CONHECIDA`** (classe = reticulado puro; não é física nova) | `campaigns/CRITICALIDADE_GENUINA/` |

**Criticalidade (2026-06-30):** com o ferromagneto O(3) da TEIC, o substrato foliado em
λ=0.75 sustenta **criticalidade de 2ª ordem genuína** (χ_max~N^0.52, J_c estável, ξ/L
ordem-1, LRO — claramente **não** mean-field, ao contrário das 7 mortes causais), MAS o
expoente é **indistinguível** do controle de reticulado cúbico puro (N^0.59; Δx/σ=0.89).
⇒ **criticalidade de reticulado conhecida (3D-Heisenberg), não assinatura nova de
Hořava–Lifshitz.** Esperado: acoplamento só ferromagnético ⇒ sem ponto de Lifshitz ⇒ λ
irrelevante no IR. A varredura de λ não rodou (funil: classe idêntica ⇒ nada a mapear).
É um Heisenberg 3D empilhado com rótulo de espaço-tempo — sem física nova, e às custas de
Lorentz.

**Resumo (2026-06-30):** com foliação + distância intra-fatia (RGG 2D por fatia,
acoplamento tipo-tempo anisotrópico `λ=r_t/r_s`), o substrato **arma as duas barreiras**:
⟨z⟩ finito (órbita compacta, `≈k_intra(1+2λ²)`) e C4≈0.19 saturando em todo λ (acima do
tipo-CDT 2D 0.145), com o espaço-tempo percolando as 8 fatias. **Primeiro substrato do
programa a passar ambas** — exatamente por **quebrar Lorentz**, confirmando a tese da
síntese. **Ressalvas (no SYNTHESIS):** armar é quase tautológico (RGG euclidiano clusteriza
— C4 é geometria de entrada, não emergência); a morte tipo-CDT prevista no apêndice (C4
colapsar a λ>λ*) **não** ocorreu (a morte da CDT era da colagem dinâmica, não de "3D
foliado"); **criticalidade/ξ NÃO foi testada** (funil; pende autorização).

## Mapa da pasta

```
FOLIACAO_ANISOTROPICA/
├── README.md                       ← este arquivo (com o rótulo obrigatório)
└── campaigns/GATILHO_FOLIADO/
    ├── PRE_REGISTRO.md             ← critérios + rótulo, travados antes de rodar
    ├── SYNTHESIS.md                ← resultado e veredito (rótulo no topo)
    ├── foliated_trigger.py · make_figure.py
    └── validation_gate.json · foliated.json · foliated.png
```

Reuso VERBATIM: `rs_clustering.clustering_metrics` (de `../TEIC/`). A novidade é o
**processo foliado** (a quebra de Lorentz); o estimador é o mesmo da linhagem, para
comparabilidade direta com as sete mortes.
