# SÍNTESE — Gatilho cinemático da repulsão Lorentz-invariante

**Data:** 2026-06-30 · **Diretório:** `REPULSAO_LORENTZ/campaigns/GATILHO_REPULSAO/`
**Natureza:** gatilho cinemático barato (⟨z⟩ + C4), sem ferromagneto, sem ξ.
**VEREDITO: `MORTE_LIMPA`** — em ambas as barreiras, com a invariância de Lorentz
verificada explicitamente como bit-idêntica.

---

## 1. O que foi testado

A 3ª família autônoma (ver `../../README.md`): substituir o sprinkling de Poisson
**independente** por um processo de ponto **repulsivo** Lorentz-invariante, e
perguntar se o grafo de cobertura causal escapa das duas barreiras cinemáticas
(`⟨z⟩` saturar **e** `C4` saturar positivo) que mataram as seis famílias anteriores.

A motivação precisa: o teorema parcial de `IMPOSSIBILIDADE_PARCIAL` prova `⟨z⟩=∞`
para qualquer regra de par invariante de Lorentz **sobre um sprinkling de Poisson**.
A hipótese crucial (i) é a **independência dos eventos** (medida de Poisson).
Quebrá-la com correlação **negativa** (repulsão) remove a aplicabilidade direta de
Campbell–Mecke. Esta é a única abertura na classe de substratos *discretos* que o
teorema não fecha (ver `../../docs/FRONTEIRA_CONHECIDA.md`, abertura 1).

**Substrato:** afinamento tipo **Matérn II** no intervalo invariante
`s²_ij = Δt² − |Δx|²` (a única quantidade Lorentz-invariante de um par). Exclusão
`{|s²_ij| < r0²}`, `r0 = α·ρ_cand^(−1/d)`; marcas chaveadas por identidade ⇒
invariante por construção. `α ∈ {0, 0.1, 0.2, 0.3}` (`α=0` = Poisson puro =
baseline interna). Grafo = cobertura causal (Hasse); estimador
`rs_clustering.clustering_metrics` **VERBATIM**; ladder de N **retido**
`{400, 800, 1500, 2500}` (2+1D, caixa T=1, L=3 — idêntica à percolação).

---

## 2. Gates — VERDE (8/8) · `validation_gate.json`

| Item | Resultado |
|---|---|
| Matérn II afina (repulsão ativa) | p_ret(α=0.3)=0.26 ✓ |
| **Hard-core invariante** (nenhum par retido com \|s²\|<r0²) | min\|s²\|=r0² exato ✓ |
| **g(Δτ)<1 curto alcance** (repulsão real, charter §2.3) | g_curto=0.74 ✓ |
| g(Δτ)→1 longo alcance (independência assintótica) | g_longo=0.95 ✓ |
| cross-check ⟨z⟩=2E/N (estimador VERBATIM) | bit-idêntico (1e-9) ✓ |
| **Invariância Lorentz: conjunto RETIDO idêntico sob boost η=0.8** | n_ret iguais ✓ |
| **Invariância Lorentz: arestas de cobertura BIT-idênticas** | simdif=0 ✓ |
| Invariância Lorentz: ⟨z⟩/C4 idênticos sob boost | iguais a 1e-9 ✓ |

A correlação de par é **genuinamente negativa** (g<1 em curto, →1 em longo) e a
invariância de Lorentz passa **por construção e verificada** (a regra depende só de
`|s²|` e de marcas por identidade). As duas precondições do charter (§2.2, §2.3)
estão satisfeitas: o que segue é uma leitura física legítima.

---

## 3. Resultado central (`repulsion.json`, `verdict_final.json`)

**Barreira 1 — coordenação ⟨z⟩(N): DIVERGE em TODO α.** O expoente local relativo
`(d⟨z⟩/dlnN)/z_top` é **+0.43, +0.42, +0.44, +0.36** para α = 0, 0.1, 0.2, 0.3 —
sempre ≫ o limiar de saturação 0.05. A repulsão **não reduz** o crescimento da
coordenação. No N casado (controle interno), `⟨z⟩(α)/⟨z⟩(Poisson) ≈ 1` (0.99–1.16):
a repulsão é essencialmente invisível para ⟨z⟩.

**Barreira 2 — clustering C4(N): DECAI e rastreia Poisson em TODO α.** C4 cai
0.10→0.05 com N em todos os α, **junto** da baseline de Poisson (α=0). No N casado,
`C4(α)/C4(Poisson) ≈ 1` (0.94–1.10 para α≤0.2). C4 fica entre o CSG (0.019) e bem
**abaixo** do tipo-CDT 2D (0.145, o único que arma C4): nenhum laço de dimensão
finita é criado.

| α | ⟨z⟩ (slope rel.) | C4 topo | C4/Poisson @N casado |
|----|---|---|---|
| 0.0 | +0.43 **div** | 0.0475 | 1.000 (baseline) |
| 0.1 | +0.42 **div** | 0.0478 | 1.007 |
| 0.2 | +0.44 **div** | 0.0513 | 1.081 |
| 0.3 | +0.36 **div** | 0.0614 | 1.293* |

\* O `1.293` (e as flags per-α "C4>0" de α=0.2/0.3 no `verdict()`) são **artefato
de truncamento do ladder**: α=0.3 bate no teto de candidatos (NCAND_CAP=6500) e o
rung do topo retém só N≈1545 em vez de 2500 — e C4 **decresce** com N, então um N
menor "infla" C4. A correção matched-N (`finalize.py`) mostra que a N genuinamente
casado C4(α)≈C4(Poisson) e **decai com N** em todos os α. **Barreira 2 falha.**

⇒ `{α : ⟨z⟩ satura} = ∅` e `{α : C4 não-trivial acima de Poisson} = ∅`. **JANELA = ∅.**

---

## 4. Mecanismo (por que morre, e o achado estrutural extra)

**A repulsão invariante é estruturalmente NÃO-LOCAL.** A região de exclusão
`{|s²|<r0²}` não é uma bola compacta: é uma **banda ao redor do cone de luz** de
volume `V_excl ~ r0²·L` (não `~r0^d`), porque o cone é não-compacto. Consequências
medidas:
- `p_ret` colapsa rápido com α (α=0.1→0.84; 0.3→0.26; 0.5→0.12; 1.0→0.03) e
  **decresce com a densidade** a α fixo (a banda captura mais candidatos quando há
  mais perto do cone) ⇒ acima de α≈0.3 o processo é degenerado (teto de densidade
  retida). **Que "repulsão local Lorentz-invariante" seja um oximoro** é o mesmo
  fato que mata a coordenação no lado de Poisson — agora visto pelo lado da medida.
- Mesmo onde o substrato é bem-definido (α≤0.3), a exclusão remove pares **perto do
  cone**, mas eles **se regeneram** na nova densidade retida, e a divergência da
  **órbita de boost (não-compacta)** sobrevive intacta. Exatamente como a percolação
  de longo alcance falhou por "decair na variável errada", o hard-core falha por
  **excluir na variável errada**: `|s²|` é cego aos atalhos de boost que ele mesmo
  cria ao manter a densidade uniforme em larga escala.

**O dado novo para a conjectura:** este é o **primeiro teste empírico fora da
hipótese (i) do teorema** (medida não-Poisson, eventos correlacionados). O resultado
estende a fenomenologia das barreiras **além de Poisson**: quebrar a independência
com repulsão de par invariante **não basta**. A abertura 1 de §3.4 da
`IMPOSSIBILIDADE_PARCIAL` (regras/medidas não-Poisson) fica **estreitada** — a
sub-classe "medida repulsiva invariante de par" cai do mesmo jeito.

---

## 5. Ressalvas honestas

- **Faixa de α limitada por estrutura, não por orçamento:** α>0.3 não é varrido
  porque o substrato **deixa de existir** (p_ret→0, densidade retida no teto) — e
  isso é registrado como achado (§4), não como buraco. Dentro de α∈[0,0.3] o
  substrato é bem-definido e a repulsão é real (gate §2.3).
- **Hard-core vs DPP soft:** usou-se Matérn II (sancionado pelo charter §2.1) em vez
  do DPP determinantal completo. Ambos têm a **mesma assinatura** g(Δτ)<1; o que o
  gatilho testa (escapar das barreiras) depende da existência da repulsão, não da
  forma hard/soft. Um DPP soft com kernel f(|s²|) teria a **mesma** não-localidade
  da banda do cone (kernel função de `s²` ⇒ correlação ao longo do cone) ⇒ mesma
  expectativa. Não há indício de cruzamento que justifique o custo do DPP.
- **Truncamento do ladder em α=0.3:** corrigido pela análise matched-N; não afeta o
  veredito (JANELA exige ambas, e ⟨z⟩ nunca satura).

---

## 6. Posição na fila de substratos

| Família | Barreira 1 (⟨z⟩) | Barreira 2 (C4) | Status |
|---|---|---|---|
| Poisson | FALHA (diverge) | — | MORTA |
| CSG | passa | FALHA (sub-MF, árvore) | ENCERRADA |
| Tipo-CDT 2D | passa (trivial, Euler) | PASSA (rede 2D) | ARMADO fraco |
| CDT 3D completo | z alto | passa | A=reproduz / B=não-resolvido |
| Longo alcance | FALHA (diverge ∀σ) | FALHA (<controle ∀σ) | SEM JANELA |
| **Repulsão Lorentz (Matérn II)** | **FALHA (diverge ∀α)** | **FALHA (≈Poisson ∀α)** | **MORTE_LIMPA** |

Segunda família (após longo alcance) a falhar as **duas** barreiras simultaneamente,
e a **primeira a testar fora da hipótese de independência** (medida não-Poisson).
A repulsão de par invariante não é a abertura que se esperava.

---

## 7. Funil (o que NÃO foi feito, por disciplina)

Não se rodou ferromagneto nem ξ — gatilho cinemático puro (charter §2.4, PRE_REGISTRO
§6). Como o veredito é MORTE_LIMPA, nenhuma campanha completa sobre esta família se
justifica. **Aberturas remanescentes** (ver `../../docs/FRONTEIRA_CONHECIDA.md`):
medidas **dinâmicas/autoconsistentes** não-pairwise (não testadas aqui), e o regime
**fora-do-equilíbrio genuíno da geometria** (registrado em [[teoria-cdt-nova]]). A
sub-classe "repulsão de par invariante" está fechada.

## Arquivos
`PRE_REGISTRO.md` (critérios travados antes) · `repulsion_trigger.py` (substrato +
gate + scan + veredito) · `finalize.py` (análise matched-N, corrige o artefato de
truncamento) · `make_figure.py` · `validation_gate.json` · `repulsion.json` ·
`verdict_final.json` · `repulsion.png` (⟨z⟩(N) e C4(N) por α com referências).
