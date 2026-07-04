# M9 — CLASSIFICAÇÃO DAS QUEBRAS DE SIMETRIA DISCRETA: pré-registro

**Data:** 2026-07-04 · **Pasta:** `FRONTEIRA_COMPACTA/M9_SIMETRIAS_DISCRETAS/`
**Natureza:** síntese analítica (teorema) + certificado de ação de simetria.
**Movimento:** 3º teorema da série de classificação (Linha B), após
[[m5-classificacao]] (substratos), [[m6-hospedagem]] (grupos), M8 (topologias).
Adiciona a linha C8 à checklist de [[m7-paper-restricoes]].

---

## 1. A pergunta

Quais quebras de simetria de espaço-tempo discreta (P, T, C, e combinações) a
classe permite, e por qual mecanismo? O core_paper tem as peças dispersas (no-go
de paridade forte; lado T empírico). M9 as unifica num TEOREMA de classificação
com a hierarquia decidida por um único critério.

## 2. A tese (o critério do carrier)

> **Uma simetria discreta pode ser quebrada (mesmo espontaneamente) SE E SOMENTE
> SE ela tem um CARRIER intrínseco** — um observável de $(\mathcal C,\prec,n)$
> sobre o qual ela age não-trivialmente. Sem carrier: a quebra é inexprimível
> (não há funcional ímpar a escrever) e impossível mesmo espontaneamente (uma
> redundância não quebra — mecanismo de Elitzur).

Aplicado às três simetrias:

| Simetria | Ação intrínseca | Carrier? | Quebra |
|---|---|---|---|
| **P** (paridade) | reflexão espacial preserva $\prec$ ⟹ age como IDENTIDADE | **NÃO** | inexprimível E espontânea impossível [teorema, cinemático] |
| **T** (reversão) | dualidade de ordem $\prec\leftrightarrow\succ$ ⟹ age NÃO-trivialmente | **SIM** | funcionais T-ímpares existem; lei auto-dual ⟹ ⟨T-ímpar⟩=0 em equilíbrio; espontânea NÃO excluída cinematicamente — medida ausente [empírico] |
| **C** (conjugação) | involução interna do alvo | **SIM** (interno) | pode quebrar dinamicamente (camada 3) |

**Corolário CP:** como P age trivialmente, $CP\equiv C$ operacionalmente;
qualquer violação de CP com conteúdo genuinamente P-emaranhado é input externo.

## 3. O que torna isto teorema (não resumo)

O critério do carrier UNIFICA os três casos sob um mecanismo (existência de
observável ímpar) e PREDIZ a assimetria P-vs-T que o core_paper afirma: P e T
são AMBAS simetrias de espaço-tempo discretas, mas têm destinos OPOSTOS, e a
razão não é "P é especial" — é que P não tem carrier (reflexão = isomorfismo de
ordem) e T tem (dualidade de ordem = objeto intrínseco distinto). A física do
Modelo Padrão alinha: os 3 setores quirais (neutrinos, gerações, eletrofraco)
são os 3 sem carrier geométrico.

## 4. O gate (certificado de ação de simetria — barato, exato)

`gate_m9.py`. Verifica, num causal set explícito (sprinkling de M², exato), COMO
cada simetria age nos dados intrínsecos:

- **(P) age como identidade:** reflexão espacial $x\to-x$ de um sprinkling ⟹ a
  ordem $\prec$ e a classe de isomorfismo do causet são PRESERVADAS ⟹ todo
  funcional intrínseco é invariante ⟹ funcional P-ímpar $\equiv0$. Congelado:
  para observáveis-teste (assimetria espacial esquerda-direita), valor no causet
  original = valor no refletido (a menos de relabeling), a 1e-12.
- **(T) age não-trivialmente:** reversão temporal $t\to-t$ ⟹ $\prec\to\succ$
  (dual) ⟹ a ordem MUDA (causet ≠ seu dual genericamente). Congelado:
  observável T-ímpar (ex.: assimetria passado-futuro do número de intervalo)
  MUDA de sinal sob dualidade; ⟨T-ímpar⟩→0 na média sobre sprinklings (auto-dual
  em lei).
- **(C) carrier interno:** involução no alvo (ex.: conjugação SU(2)) age
  não-trivialmente no campo $n$. Congelado: funcional C-ímpar existe e é não-nulo
  numa config genérica.

## 5. Mortes pré-registradas

- **D-M9-1 (P tem carrier):** algum funcional intrínseco P-ímpar não-nulo (valor
  DIFERE entre causet e seu refletido, além de relabeling) ⟹ a paridade É
  quebrável ⟹ o no-go de paridade cai. (Prior: NÃO — reflexão preserva ordem.)
- **D-M9-2 (T sem carrier):** dualidade de ordem age trivialmente (causet ≡ dual
  sempre) ⟹ T também é redundância ⟹ a assimetria P-vs-T do core_paper cai.
- **D-M9-3 (critério falha):** alguma simetria com carrier que NÃO pode quebrar,
  ou sem carrier que PODE ⟹ o critério do carrier não classifica.
- Regra: ações de simetria exatas (tolerância 1e-10 no relabeling); nenhuma
  janela pós-dado.

## 6. O que M9 NÃO reivindica (escopo)

- É a ação CINEMÁTICA das simetrias (o que a ordem permite); a quebra dinâmica
  efetiva (C condensar; T-arrow como input) é medida/dinâmica, não derivada —
  mesma ressalva do core_paper (lado T empírico).
- Não re-deriva o octeto nem os setores quirais do MP; observa que o critério
  do carrier os alinha (P sem carrier ⟷ 3 setores quirais sem carrier
  geométrico).
- CPT do EFT emergente é assumido do contínuo (item de escopo do core_paper),
  não testado aqui.
- Anti-circularidade: ações de simetria em causet explícito; nenhum número do
  mundo.
