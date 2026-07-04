# N4 — FASE 1: RESULTADO (vácuo SJ do escalar livre no substrato-caixa)

**Data:** 2026-07-03 · **Runner:** `n4_fase1.py` (declaração v1 55821d7 → emendas
55821d7‥79f28f4, todas pré-run do trecho que avaliaram) · **Dados:**
`n4_fase1.json` + `n4_fase1_rows.jsonl` (110 runs) · **Custo:** ~20h de parede
(interrompido 4× por kills de sessão; checkpoint preservou tudo).

## 0. Veredito em uma página

**D1 NÃO disparou. D2 NÃO disparou. P-N4-1 (forma IR relativística do vácuo SJ
no substrato do programa) CONFIRMADA em d=2 e d=4.** O flag composto
`PASSA_FASE1=false` do JSON é LITERAL e explicado em §2: um único sub-critério
(concordância E1/E2 a 2σ *estatístico*) revelou-se mal-posto após os dados —
os dois estimadores diferem por sistemática pura de +0.6% (vs. tolerância
física de 15%); nenhum critério FÍSICO falhou. Não reescrevemos o critério
post-hoc: registramos a falha do critério, com a causa, aqui.

| Medição | Critério físico | Medido | Veredito |
|---|---|---|---|
| M1.1 estabilidade (D1) | pares ±λ < 1e-10; deriva torre ≤ 0.10/0.20 | 1.9e-15; derivas 0.001–0.022 | ✅ (D1 não) |
| M1.2 d=2 (D2) | \|c−1\| ≤ 0.15 nos 2 estimadores | **c_E2 = 0.9585 ± 0.0002; c_E1′ = 0.9647 ± 0.0002** (36 runs) | ✅ físico (D2 não); ⚠️ 2σ-formal (§2) |
| M1.2 d=4 | \|c−1\| ≤ 0.20 | **c = 0.904** (2 pontos k; 7+7 runs) | ✅ |
| M1.3 d=2 (validação migrada do Gate G) | \|m/m_in − 1\| ≤ 0.15 nos 2 + 2σ | **−1.9% (E2) / −1.7% (E1′), consistentes** | ✅ |
| M1.3 d=4 | reportado (resolução) | m_fit=1.16 vs m_in=2.37; shift +0.290±0.002 (sinal 60σ, 28% da magnitude) | **INCONCLUSIVO-por-resolução** (declarado; §4) |
| M1.4 espectro | reportado | torre d=2 −1.036 / d=4 −0.31…−0.36; kernel ~0 | §5 |
| BD cross-check | robustez (não morte) | c_BD = 0.797 ± 0.038; 2σ-inconsistente com Johnston | ⚠️ parcial (§6) |

**Fases 2 e 3 LIBERADAS** (gate do funil = "Fase 1 sem D1/D2" — satisfeito).

## 1. M1.1 — o vácuo SJ é estável no substrato-caixa (D1 não dispara)

Pareamento ±λ a 1.9e-15 em TODOS os 110 runs (cilindro d=2 três tamanhos,
laje-toro d=4 três tamanhos, massivo, BD, Lanczos/denso 12000–16000).
Deriva da torre: d=2 0.0007–0.0015 (tol. 0.10); d=4 0.020–0.022 (tol. 0.20).
Fração de kernel numérico ≤ 0.5% (d=2), 0 (d=4). O objeto Pos(iΔ) existe e é
estável em N e ρ no substrato do programa — a porta-ℏ abre.

## 2. M1.2 — o ramo relativístico EMERGE (D2 não dispara); e a lição do 2σ

**d=2 (36 runs, 3 tamanhos, ρ varrida ×4):** ridge presente em TODOS os runs
nos DOIS estimadores. c_E2 = 0.9585, c_E1′ = 0.9647 — ambos a ≤4.2% de c=1
(tolerância 15%). O desvio −4% é **constante em ρ** (0.9579/0.9588/0.9588 com
ρ ×4) ⇒ NÃO é dispersão UV de rede; é viés comum de leitura IR (binning +
Hann + laje finita) e/ou física IR da laje — registrado como observação,
irrelevante para D2.

**A falha formal declarada:** o pré-registro pedia |c_E1 − c_E2| ≤ 2σ
*estatístico combinado*. Medido: diferença pareada +0.00621 ± 0.00113
(sistemática pura de estimador, 0.6%) contra SEMs de 0.0002 ⇒ ~18σ
estatístico. O critério era MAL-POSTO: dois estimadores que compartilham o
binning (caveat declarado na emenda E1′) têm erro relativo sistemático, não
estatístico; com 36 runs o SEM colapsa e qualquer sistemática não-nula
"falha". A régua correta teria sido tolerância absoluta (ex.: |Δc| ≤ 0.05).
**Não a adotamos post-hoc**: reportamos `M1_2_d2.passa=false` literal +
esta análise. Para D2 (a morte), o que importa: os dois estimadores veem o
ridge e ambos passam o critério físico com folga — **D2 não dispara**.

**d=4:** c = 0.904 (pontos: ω=2.157±0.002 em k=2.370, N=16000, 6 seeds; e
ω=2.288 em k=2.547, N=12000, 1 seed). |c−1| = 0.096 ≤ 0.20 ✓ com a ressalva
de janela declarada (poucos k — o vínculo sem-enrolamento 2T=L/2 come a
janela IR; conta no papel na declaração).

## 3. M1.3 d=2 — validação de estimadores (migrada do Gate G) VERDE

m = 3·(2π/L_x) = 4.712 inserido; medido 4.623 ± 0.009 (E2) e 4.633 ± 0.008
(E1′): desvios −1.9%/−1.7% (tol. 15%), concordância 2σ ✓ (aqui os SEMs são
maiores e a régua 2σ funciona). A validação dois-estimadores que o diamante
do Gate G não podia dar, a caixa deu — a emenda G3→G3′ fecha o ciclo.

## 4. M1.3 d=4 — INCONCLUSIVO-por-resolução (saída declarada)

Shift massless→massivo pareado por seed: **+0.2901 ± 0.0018** (sinal
inequívoco, ~60σ estatístico, sinal POSITIVO correto) mas 28% do esperado
(+1.05 para ω=√(c²k²+m²)). Causa nomeada: m·(espaçamento de rede) =
2.37·ρ^{−1/4} = **1.41** — a massa de controle em d=4 é PESADA em unidades de
rede (λ_Compton ≈ 2.7 espaçamentos), regime onde correções de rede à relação
de dispersão são O(1); em d=2 o controle tinha m/√ρ = 0.21 (leve) e deu −2%.
O pré-registro declarou exatamente esta saída ("resolução comparável ao gap —
INCONCLUSIVO-por-resolução, não morte"). Registro adicional: o run massivo
N=12000 herdou m_in=2.3702 do binding do loop no fallback (não recalculado);
inofensivo — o m_in efetivamente inserido é o registrado no row e TODOS os
runs massivos d=4 usaram o mesmo 2.3702 (consistentes entre si).

## 5. M1.4 — densidade espectral (reportado)

Torre d=2: inclinação −1.036 (vs −1 exata do diamante — a laje-toro tem a
mesma lei com correção de geometria); estável em ρ. d=4: −0.31…−0.36
(deriva lenta com N — dimensão maior enche a torre de degenerescências do
toro; reportado). Joelho: detectável só em N=1024 d=2 (~n=300) e N=2000 d=4
(~n=190); nos N maiores o detector (dobra de inclinação) não acha joelho na
janela n≤400 — consistente com o joelho escalando com N (Fase 0 A7/A8).
Kernel numérico ~0. Nada aqui alimenta morte; alimenta a Fase 3 (truncamento).

## 6. BD cross-check (N-hig 2) — robustez PARCIAL

O 2º operador (d'Alembertiano BD suavizado ε=0.25, kernel C5 validado,
G_BD = (−½I + εK_ret)^{-1}) exibe o ridge relativístico (12/12 runs) com
**c_BD = 0.797 ± 0.038** — 2σ-inconsistente com o Johnston (0.958). Leitura:
a escala de suavização do BD em ρ=341 é ℓ_smear ~ √(1/(ε·ρ)) ≈ 0.11,
comparável aos comprimentos de onda do topo da janela (2π/k_max ≈ 0.22) — a
janela pré-registrada morde a região onde o BD é deliberadamente não-local.
FORMA relativística: robusta nos dois operadores. VALOR de c: dependente de
operador na janela usada. Era robustez-não-morte declarada; fica como caveat
quantitativo para a Fase 2 (que usa Johnston).

## 7. Trilha de emendas e incidentes (auditoria completa)

```
55821d7  v1 declaração congelada + commit pré-run
  smoke → ENROLAMENTO: no cilindro G_R=½C só vale sem wrap (T=1.5, L_x=2
  tinha wrap; modos fora da shell). EMENDA pré-run: L_x=4, T=1 (fronteira
  sem-enrolamento 2T ≤ L_x/2; N_img é não-intrínseco = proibido).
  + eigenproblema da laje resolvido no papel (modos on-shell exatos;
  λ=√(CS)/k; zero-modo 2ρ/√3 e n=1 ρ/k BATEM os λ medidos) ⇒ desvio do
  smoke era JANELAMENTO ⇒ PISO k ≥ k_res = 2π/(1.4T) nos fits.
  + E1 mode-side: 0/30 modos aceitos (misturas elípticas + hibridização UV;
  3ª ocorrência da lição mode-side do programa) ⇒ SUBSTITUÍDO por E1′ =
  inclinação de fase da MESMA projeção binada (caveat: compartilha binning
  com E2 — a lição do §2 nasce deste caveat declarado).
  + d=4 pequenos sub-resolução (conta: resolver n=3 exige N>8500) ⇒
  dispersão em N=16000 Lanczos top-200 (cláusula Lanczos do pré-reg).
run 02jul 17:55 → checkpoint 96: d=2 completo; d=4 M1.1 completo;
  MemoryError no Lanczos 16000 → FALLBACK DECLARADO N=12000 (2 runs, 1.6h/run)
  → ARPACK NÃO CONVERGE na seed 1 (>5h34, tol=0 default = precisão de máquina)
194ce10  tol=1e-7 (tolerância numérica ~10⁷× mais fina que σ_ω; não é janela)
  → seed 1 AINDA >1h54
74c3f20  plano B: seed 1 excluída (cláusula de orçamento §9; seed de
  instrumento, não física; lista [0,2,3,4,5,6] mantém 6 seeds)
  → seed 2 idem >3h ⇒ padrão SISTEMÁTICO do ARPACK neste operador
  (espectro aglomerado do iΔ), não seeds ruins
79f28f4  ARPACK → diagonalização DENSA parcial (LAPACK evr top-200,
  complex64): 20–22 min/run DETERMINÍSTICO, e voltou a N=16000 (o limite
  de memória era do perfil ARPACK). Runs N=12000 s=0 mantidos como dados.
  Operacional: 4 kills de sessão → processo DESACOPLADO (Start-Process,
  prioridade BelowNormal) + retomada por checkpoint JSONL em todos.
FIM 03jul 17:48 — 110 rows, n4_fase1.json
```

**Lições de instrumento (banco do programa):** (i) substrato compacto +
propagador de série causal: trabalhar na fronteira sem-enrolamento, nunca
somar imagens; (ii) mode-side de novo não (agora com mecanismo: mistura
elíptica + hibridização); (iii) critério de consistência entre estimadores
correlacionados exige régua ABSOLUTA, não 2σ estatístico (§2); (iv) ARPACK
em iΔ de causet grande é armadilha (espectro aglomerado) — diagonalização
densa parcial é determinística e cabe em RAM com complex64; (v) massa de
controle deve ser LEVE em unidades de rede (m·a ≲ 0.3) — em d=4 com ρ=8 e
caixa sem-enrolamento isso é impossível dentro da janela IR (m mínimo =
3·2π/L com L preso a T — tensão declarada; resolver exigiria ρ maior).

## 8. Consequências

1. **Fases 2 e 3 LIBERADAS** (sem D1/D2).
2. P-N4-1 do pré-registro: **confirmada** (prior ALTO honrado): o vácuo SJ
   existe, é estável e carrega o ramo relativístico no substrato do programa.
3. Para o paper-núcleo (delta próprio, só após campanha completa): "a
   quantização covariante forçada por P1 é REALIZÁVEL sobre o substrato — a
   porta-ℏ abre com forma relativística" [medido].
4. Fase 2 usa Johnston (BD caveat §6); Fase 3 usa o pipeline SSEE já validado
   no Gate G4 + joelho/truncamento congelado da Fase 0.
```
Fase 0 ✅ → Gate G ✅ (4/4) → Fase 1 ✅ (D1/D2 não; P-N4-1 confirmada)
  → Fase 2 (Goldstone/multipleto)  ∥  Fase 3 (SSEE canto de Rindler)
```
