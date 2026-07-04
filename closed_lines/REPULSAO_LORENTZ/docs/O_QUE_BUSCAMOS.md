# O QUE BUSCAMOS — prioridades e sequência

Em ordem de prioridade. Cada degrau é **condicional** a sobreviver o anterior — é um
funil, não uma lista de desejos.

## 1. Primeiro: passar as duas barreiras cinemáticas  ← **o gatilho desta tarefa**

Sobre o substrato repulsivo, medir no grafo de cobertura causal:
- **Barreira 1:** ⟨z⟩(N) **satura** (coordenação finita no limite N→∞)?
- **Barreira 2:** C4(N) **satura em valor positivo** (laço de dimensão finita)?

**Ambas** precisam passar, com o **mesmo estimador e ladder de N** das campanhas
anteriores. Critérios de morte simétricos travados em
`../campaigns/GATILHO_REPULSAO/PRE_REGISTRO.md`.

> **Status (2026-06-30): MORTE_LIMPA.** ⟨z⟩ diverge em todo α; C4 rastreia Poisson e
> decai. Ambas falham. Detalhes: `../campaigns/GATILHO_REPULSAO/SYNTHESIS.md`.
> ⇒ Os degraus 2 e 3 **não são autorizados** por esta família. O funil fecha no
> degrau 1, como nas campanhas anteriores.

## 2. Se o gatilho armar: ferromagneto da TEIC sobre este substrato

Rodar o ferromagneto O(3) e medir **LRO (Pergunta A)** e **universalidade
(Pergunta B)**, com os **mesmos estimadores e critérios** das campanhas anteriores
(CDT_TEIC_FERRO como referência de protocolo). **Não executar nesta tarefa.**

## 3. Se LRO e universalidade sobreviverem: criticalidade genuína

E **só então**, testar se criticalidade genuína aparece — **comprimento de
correlação ξ divergindo** — usando o **controle positivo 3D** como referência (a
suíte que certifica que a criticalidade é visível quando existe). **Não executar
nesta tarefa.**

## 4. O que NUNCA fazemos nesta linha

- **Nunca ajustar o substrato para obter o resultado que queremos.** Qualquer
  modificação do processo de ponto deve ser motivada por uma **razão física externa
  ao resultado desejado** (p.ex. a forma do kernel vir da literatura de DPP, a
  invariância impor a dependência só em `s²`), nunca "porque assim a barreira passa".
- **Nunca tratar resultado ambíguo como decisivo.** Ambíguo → reportar como
  não-resolvido, com o N estimado para resolver.
- **Nunca alterar critérios depois de ver os dados.** Eles vivem no `PRE_REGISTRO.md`.
