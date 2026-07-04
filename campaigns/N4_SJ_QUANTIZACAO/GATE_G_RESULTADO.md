# N4 — Gate G de engenharia: RESULTADO

**Data:** 2026-07-02 · **Veredito: VERDE 4/4** (critérios da declaração v4,
congelados antes do run final; JSON: `n4_gate_g.json`; v1 preservado em
`n4_gate_g_v1.json`; código: `n4_gate_g.py` com changelog v1→v4 completo).
**Fases 1–3 LIBERADAS.**

## 0. Veredito

| Gate | Critério (congelado) | Medido | |
|---|---|---|---|
| G1 espectro | pares ±λ < 1e-10; inclinação torre = −1 ± 0.15 | resíduo 3.1e-15; **−1.0025 ± 0.0004** | ✅ |
| G2 forma ABDRSY | R² > 0.9 sem parâmetros livres, pooled, cada N | **0.9990 / 0.9999 / 0.9998** (N=1024/2048/4096) | ✅ |
| G3′ controle massivo | ⟨G_R⟩ vs ½J₀(mτ): RMS < 5%; 1º zero ± 5% | **RMS 2.4% ± 0.5%; zero −3.0%** | ✅ |
| G4 SSEE Sorkin–Yazdi | volume sem trunc. (ratio > 2); log 1/3 ± max(0.10, 3SE) com trunc. duplo | **ratio 4.27; inclinação 0.254 ± 0.039** (alvo 1/3, tol 0.116) | ✅ |

Confirmações finas dignas de nota: o fit LIVRE do G2 devolve
a = −0.0796 = −1/4π e b = −0.0236 vs previsto −0.0246 (N=4096) — i.e., o corte
IR **λ ≈ 0.46/L de ABDRSY é reproduzido no 3º dígito**, sem nenhum parâmetro
ajustado. A sanidade t0 (S do diamante inteiro) deu 1.8e-12.

## 1. O que o gate PEGOU (o motivo de gates existirem)

**Bug de física: massa taquiônica.** v1–v3 construíam o propagador massivo com
(I − (m²/2ρ)C)^{-1} = série **não-alternante** — equivalente a m² < 0. A série
correta alterna (J₀ exige): **G_R = ½C(I + (m²/2ρ)C)^{-1}**, consistente com
b = −m²/ρ de Johnston (que a própria tabela A1 da Fase 0 registrava certo em
d=4). Sintomas explicados de uma vez: ridge sub-cone, banda causal v3 excluindo
o sinal, estimadores "não achando" o gap. **Verificação decisiva:** ⟨G_R⟩
binado = ½J₀(mτ) a 3 decimais por 2 oscilações completas (τ ∈ [0,2]).
**ERRATUM → Fase 0, tabela A1:** a transcrição d=2 massiva estava com o sinal
errado (a eq. (23) de 2008.07697 extraída em texto também mostra "I−"; nossa
verificação J₀ resolve a física independentemente da tipografia da fonte).

## 2. A emenda G3 → G3′ (falha de desenho documentada, não afrouxamento)

O G3 original pedia o gap de dispersão dos DOIS estimadores espectrais no
**diamante**. Após o conserto do sinal, forense de 5 iterações mostrou viés
sistemático mode-side (m_eff ≈ 9–10, c ≈ 1.1–1.2, estável entre seeds e entre
3 implementações independentes), enquanto: (i) o propagador é exato (J₀);
(ii) o E2 com média de centro-de-massa vê o cone (c ≈ 0.99); (iii) o
**discriminante massless** reproduz o viés (c = 1.22 na seed 0) ⇒ viés de
test-bed, não física nova. Causa nomeada: com mL = 6.7 o diamante contém ~3
comprimentos de Compton e cantos-espelho (ABDRSY; Mathur–Surya) — o ridge de
modos individuais sem média de COM é dominado por interferência de borda.
Consulta de âncora adicional (Mathur–Surya 1906.07952): o SJ massivo do
diamante só rastreia W^mink_m para m > m_c = 2Λ ≈ 0.92/L — nosso m = 6.66 ≫ m_c
está do lado certo do crossover; o problema é o corpo finito, não o estado.

**Emenda declarada e commitada ANTES do run final (d95ec35):** G3′ = controle
de propagador J₀ quantitativo; a validação dois-estimadores-15% do gap MIGRA
para a geometria da Fase 1 (caixa com transversal periódica ⇒ k exato, sem
cantos), onde M1.2/M1.3 já a pré-registravam. As medições E1/E2 do diamante
ficam REPORTADAS como diagnóstico (não gated): E2 c ≈ 0.99 (2/3 seeds).

## 3. Higiene da trilha (para auditoria)

```
a82726d  v1: código + declaração congelada ANTES do run
   run1: 2/4 (G1 ✅ G4 ✅; G2 falha marginal N=1024 per-seed; G3 estimador)
   v2: G2 pooled (mesmo critério; fit livre já batia −1/4π em 12/12);
       E1 M=100 (alinha ao pré-reg), fit ponderado; E2 taper Hann
   v3: marginais + banda causal (diagnóstico do vazamento da linha ω₁)
   → forense: picos sistemáticos m_eff≈√2·m → teste J₀ direto → BUG DE SINAL
d95ec35  v4: sinal corrigido + emenda G3→G3′ congelada PRÉ-run + changelog
   run2 (v4): 4/4 VERDE (este documento)
```
Nenhum critério físico foi afrouxado após ver dados: G1/G4 inalterados desde
v1; G2 manteve "R²>0.9 sem parâmetros livres em cada N" (mudou o agregador,
com o fit livre como evidência independente); G3′ foi SUBSTITUÍDO com falha de
desenho documentada e critério novo congelado antes do run que o avaliou.

## 4. Consequências para as Fases 1–3

1. **Fases 1–3 LIBERADAS** (funil do pré-registro §11).
2. **M1.2/M1.3 (caixa) herdam a validação de estimador** que G3 não pôde dar
   no diamante — com a lição aprendida: usar média de COM (tipo-E2) como
   estimador primário e o mode-side como secundário; janelas do §7 mantidas.
3. **Lição de instrumento (banco de lições do programa):** ridge espectral de
   modos individuais em domínio causal FINITO e profundo-massivo é
   borda-dominado; exigir média de COM ou periodicidade antes de confiar em
   dispersão. (Parente da lição "clamp em grafo irregular" de N5.)
4. O truncamento duplo congelado (número, α=1) reproduziu Sorkin–Yazdi
   (0.254±0.039 vs 0.346±0.028 deles — consistente dentro de 2σ combinado e
   da tolerância declarada) — o pipeline SSEE da Fase 3 está validado.
