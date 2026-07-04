# PRÉ-REGISTRO — Parte A: correlações não-pairwise genuínas (Gibbs com V₃)

**Data:** 2026-06-30 · **Critérios travados ANTES de rodar.** Não se ajustam após ver dados.
**Pré-condição analítica:** `A2_ANALISE.md` — decisão = prosseguir (candidato não-Poisson
de ordem ≥3 não coberto por Palm/Slivnyak).

## 1. Substrato (a novidade)

Processo de ponto de **Gibbs** sobre Minkowski 2+1D (caixa T=1, L=3 — idêntica à
linhagem), amostrado por **Metropolis-Hastings nas posições dos pontos** (não na
conexão). Energia Lorentz-invariante (só invariantes `s²`):

```
U = β₂ Σ_{i<j} V₂(s²_ij)  +  β₃ Σ_{i<j<k} V₃(s²_ij, s²_jk, s²_ik)
V₂(s²) = exp(−|s²| / (2 w²))                          (par, suave)
V₃ = V₂(s²_ij)·V₂(s²_jk)·V₂(s²_ik)                    (tripla: PRODUTO, não soma)
```

`V₃` é **produto** das três funções de par do trio ⇒ ativa só quando os **três** pares
estão simultaneamente próximos ⇒ não é uma soma de termos de par (não-fatorável por
construção; confirmado pelo gate 2). `β₃ > 0` penaliza trios mutuamente próximos.
Grafo medido: **cobertura causal (Hasse)** sobre os pontos de Gibbs; estimador
`rs_clustering.clustering_metrics` **VERBATIM**. Ladder de N; varredura de `β₃`.

## 2. Gates (precondições, todos devem passar)

1. **Equilíbrio do MC:** energia e estatísticas estabilizam (cheque de convergência da
   cadeia: duas metades concordam dentro do erro).
2. **V₃ genuinamente NÃO-FATORÁVEL (charter gate 2):** comparar β₃=0 vs β₃>0. Um `V₃`
   genuíno suprime a estatística de **trios** muito mais do que a de **pares**:
   exigir `|ΔT₃|/T₃  >  3 · |ΔP₂|/P₂` (a mudança fracionária de trios excede em ≥3× a
   de pares). **Teste forte adicional (matched-pairs):** re-tunar `β₂` no run com `β₃>0`
   para casar `P₂` com o baseline; se `T₃` ainda difere → não-redutível confirmado.
   Se só a estatística de pares muda (`|ΔT₃|/T₃ ≈ |ΔP₂|/P₂`): `V₃` é redutível a `V₂`
   efetivo ⇒ candidato **não é genuíno** (morte = reclassificação, não escape).
3. **Invariância de Lorentz:** boost η=0.8 da configuração; ⟨z⟩/C4 do grafo idênticos
   (o grafo é função invariante das posições; a medida é função só de `s²`).
4. **Cross-check do estimador:** ⟨z⟩ = 2E/N (clustering_metrics VERBATIM).

## 3. Medição central

Para cada `β₃` e cada N do ladder: equilibrar o Gibbs, construir a cobertura causal,
medir ⟨z⟩(N) e C4(N) (média sobre seeds, SEM). Expoentes locais `d⟨z⟩/dlnN`,
`dC4/dlnN`. Sobreposição com Poisson / referências da linhagem.

## 4. Critérios de veredito (TRAVADOS — idênticos à linhagem)

`z_rel_thresh = 0.05`, `c4_sat_thresh = 0.02`, `c4_decay_ratio = 0.5`.

- **JANELA ENCONTRADA:** existe `β₃` com ⟨z⟩ saturando (`|d⟨z⟩/dlnN|/z_top < 0.05` e
  não-crescente) **E** C4 saturando positivo (`C4_top > 0.02` e `≥ 0.5·C4_first`),
  **E** o gate 2 confirma `V₃` genuinamente não-fatorável nesse `β₃`.
- **MORTE:** em todo `β₃`, ⟨z⟩ diverge **ou** C4 → 0 (mesma assinatura das 7 anteriores)
  — **ou** `V₃` reclassificado como redutível a `V₂` (gate 2 falha) ⇒ não era genuíno.
- **AMBÍGUO:** reportar não-resolvido + N necessário estimado. Sem forçar.

## 5. Funil

Puramente cinemático. **Ferromagneto e ξ NÃO rodam.** Só JANELA autoriza campanha
completa (com report e autorização antes). Morte ⇒ fecha a porta não-pairwise genuína.
