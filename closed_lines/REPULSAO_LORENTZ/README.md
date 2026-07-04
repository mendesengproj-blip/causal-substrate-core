# REPULSAO_LORENTZ — Processos de ponto com repulsão Lorentz-invariante

> Linha de pesquisa **autônoma e independente** da TEIC e da TEORIA_CDT. Não é
> continuação delas: é uma **terceira família** de substrato causal, motivada pelos
> resultados (sobretudo pelas *mortes*) das duas anteriores. Esta pasta é
> **autocontida** — tudo o que se precisa para entender de onde a linha vem e o que
> ela busca está aqui e em `docs/`.

---

## O que é esta linha

Uma investigação sobre se existe uma **terceira família de substrato causal** —
diferente de **CST** (causal sets / sprinkling de Poisson) e de **CDT**
(triangulações dinâmicas causais) — capaz de produzir física não-trivial emergente,
incluindo potencialmente **criticalidade genuína** (comprimento de correlação
divergente) e **escala**, sobre um fundo **Lorentz-invariante**.

A família proposta: **processos de ponto com repulsão Lorentz-invariante**. Em vez
de eventos distribuídos independentemente (Poisson), os eventos do substrato têm
**correlação negativa** de curto alcance — repelem-se localmente, de forma
invariante sob Lorentz **em média**. A motivação vem diretamente das duas linhas
anteriores, abaixo.

---

## De onde vem — as descobertas que motivam esta linha

**Da linha TEIC (CST com Poisson).** Validou que um campo de orientação O(3) produz
ordem de longo alcance (LRO), Goldstones escalares, octeto de mésons degenerado,
spin-½ bariônico — tudo sobre o substrato de Poisson. Mas **não entrega escalas**
(G, a₀, fπ), nem *gauge*, nem o fóton como setor dinâmico. A razão do fóton foi
estabelecida (os diamantes causais são 100% "elétricos"; o setor magnético é
estruturalmente vazio). A razão da ausência de escala emergente foi estabelecida em
seguida.

**Do programa de busca por escala (seis campanhas + análise).** Testou-se
sistematicamente se *qualquer* variação de substrato causal consegue produzir
criticalidade genuína em vez de campo-médio (mean-field). **Seis famílias morreram
pelo mesmo mecanismo:**

1. **Poisson modificado** (ESCALA_XI): a coordenação diverge ⇒ mean-field de Bethe.
2. **Crescimento sequencial** (CSG, Gatilhos 1–2): coordenação finita, mas
   *clustering* → 0 ⇒ tipo-árvore.
3. **CDT 3D em equilíbrio** (CDT×TEIC): indício de mean-field, inconclusivo por custo.
4. **CDT 3D fora-do-equilíbrio / NESS** (NESS_GEOMETRIA): mean-field mesmo com *drive*.
5. **CDT 4D cinemático** (CDT_4D_VIABILIDADE): *clustering* decai ⇒ mean-field.
6. **Percolação de longo alcance por Δτ** (PERCOLACAO_LONGO_ALCANCE): falha nas duas
   barreiras; Δτ é cego à geometria espacial (decai na variável errada).

**Da análise analítica (IMPOSSIBILIDADE_PARCIAL).** O mecanismo comum das seis
mortes foi formalizado como **teorema parcial** (Campbell–Mecke / Palm + invariância
de Poincaré):

> Para qualquer regra de conexão *pairwise* mensurável e invariante de Poincaré
> sobre um *sprinkling de Poisson*, a valência esperada é
> **⟨z⟩ = ρ · Vol(H^{d−1}) · ∫ Δτ^{d−1} q(Δτ) dΔτ**, e como
> **Vol(H^{d−1}) = ∞** (a órbita de boost é o hiperbolóide não-compacto),
> **⟨z⟩ = ∞** salvo `q ≡ 0`.

O candidato mais próximo de exceção — N(i,j), o número de eventos no intervalo
causal — foi provado ser "Δτ disfarçado" (`E[N|Δτ] = ρ c_d Δτ^d`, bijeção
monotônica): não carrega informação espacial nova além de Δτ.

**O ponto-chave que abre esta linha.** O teorema fecha o espaço de regras *pairwise*
**sobre Poisson**. A hipótese central de que ele depende é: **a medida do *sprinkling*
é Poincaré-invariante (independência dos eventos)**. Se essa hipótese for relaxada —
se os eventos **não** forem independentes, mas correlacionados **negativamente**
(repulsão) de forma que preserve Lorentz **em média** mas não ponto-a-ponto — o
argumento de Campbell–Mecke **não se aplica diretamente**, e a divergência de ⟨z⟩
**deixa de estar garantida**. É exatamente essa fresta que esta linha testa.

---

## O que esta linha busca

**A pergunta central:** um processo de ponto com repulsão Lorentz-invariante produz
um grafo de cobertura com

- coordenação **⟨z⟩(N) que satura** (não diverge com N)? **e**
- *clustering* **C4 que satura em valor positivo** (não decai a zero)?

Se **ambas**: seria o primeiro substrato causal a passar as duas barreiras
cinemáticas simultaneamente — e justificaria rodar o ferromagneto da TEIC em cima e,
depois, o teste de criticalidade completo.

- **Sucesso:** as duas condições satisfeitas por algum regime do parâmetro de
  repulsão, com o **mesmo estimador e ladder de N** das campanhas anteriores
  (comparabilidade direta).
- **Morte:** repulsão reproduz mean-field (⟨z⟩ diverge apesar da repulsão, ou C4
  decai a zero), ou o único regime que satisfaz ambas introduz **dependência de
  referencial** (violação de Lorentz medida explicitamente).
- **Resultado mais valioso mesmo sendo morte:** se a repulsão funciona para uma
  barreira mas não para a outra, isso é um **dado concreto** que estreita a
  conjectura de impossibilidade.

---

## O que NÃO estamos fazendo

- **Não** estamos "construindo para dar certo". O gatilho tem critério de morte
  **simétrico** — é tão fácil morrer quanto sobreviver.
- **Não** estamos tentando encaixar a TEIC neste substrato. A TEIC é um **mapa de
  referência**, não o objetivo.
- **Não** estamos derivando escalas (G, a₀). Escala emergente é uma consequência
  *posterior*, condicional a sobreviver as barreiras cinemáticas primeiro.

---

## Estado atual

| Campanha | Veredito | Diretório |
|---|---|---|
| Gatilho cinemático da repulsão (Matérn II em s²) | **`MORTE_LIMPA`** (ambas as barreiras falham) | `campaigns/GATILHO_REPULSAO/` |

**Resumo do gatilho (2026-06-30):** com um processo de ponto **genuinamente
repulsivo** (afinamento Matérn II no intervalo invariante `s²`, `g(Δτ)<1` verificado;
invariância de Lorentz **bit-idêntica** sob boost), o grafo de cobertura causal
**diverge em ⟨z⟩ em todo α** e **rastreia o C4 de Poisson, decaindo com N**. Quebrar
a independência do *sprinkling* com **repulsão de par invariante não basta** para
escapar das barreiras: a exclusão remove pares perto do cone, mas eles se regeneram
na nova densidade e a divergência da órbita de boost sobrevive. Achado estrutural
extra: a repulsão Lorentz-invariante é **não-local** (banda do cone, `V_excl~r0²L`),
o que limita o regime acessível — o mesmo fato que mata a coordenação, visto pelo
lado da medida. Detalhes em `campaigns/GATILHO_REPULSAO/SYNTHESIS.md`.

**Aberturas que permanecem** (`docs/FRONTEIRA_CONHECIDA.md`): medidas
**dinâmicas/autoconsistentes não-pairwise** (a abertura mais concreta do teorema
parcial), e a geometria **fora-do-equilíbrio genuíno**. A sub-classe "repulsão de
par invariante sobre o espaço de Minkowski" está fechada.

---

## Mapa da pasta

```
REPULSAO_LORENTZ/
├── README.md                  ← este arquivo (contexto completo)
├── docs/
│   ├── MOTIVACAO.md           ← por que esta família especificamente
│   ├── O_QUE_BUSCAMOS.md      ← prioridades: o que é sucesso/morte e a sequência
│   └── FRONTEIRA_CONHECIDA.md ← o teorema parcial: o que fecha, o que deixa aberto
└── campaigns/
    └── GATILHO_REPULSAO/      ← a campanha (gatilho cinemático barato)
        ├── PRE_REGISTRO.md    ← critérios travados ANTES de rodar
        ├── SYNTHESIS.md       ← resultado e veredito
        ├── repulsion_trigger.py · finalize.py · make_figure.py
        └── *.json · repulsion.png
```

**Reuso VERBATIM da linhagem** (para comparabilidade): `causal_core.sprinkle_box`,
`causal_core.causal_matrix` e `rs_clustering.clustering_metrics` são importados de
`../TEIC/` sem modificação. A **única novidade** desta linha é o *processo de ponto*
(a medida repulsiva); o substrato causal, o grafo e os estimadores são os mesmos das
campanhas anteriores.
