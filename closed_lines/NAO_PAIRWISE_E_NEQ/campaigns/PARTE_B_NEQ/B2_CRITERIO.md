# B.2 — Critério não-circular (TRAVADO antes de qualquer código)

**Data:** 2026-06-30. Esta é a parte de maior risco de autoengano de todo o mapa de
impossibilidade (a armadilha α=0,1 já apareceu 3× nesta linha). O critério abaixo é
definido e **congelado antes** de escrever o motor.

---

## 1. O que precisamos distinguir

- **(i) Genuinamente sem ponto fixo, com estrutura emergente** (o que se busca): a
  dinâmica nunca estaciona, mas os observáveis revelam um **atrator dinâmico
  auto-similar** — uma relação adimensional estável apesar de ⟨z⟩ e C4 evoluírem.
- **(ii) "Ainda não convergiu"** (a armadilha): a falta de convergência é só paciência
  insuficiente; não há estrutura, só transiente/deriva/ruído.

## 2. Por que GROWTH (volume → ∞) e não um drive limitado

Um sistema **finito** (volume travado) tem espaço de configurações finito ⇒ ou tem
distribuição estacionária, ou cicla (estacionário periódico = o NESS já testado e
morto), ou é absorvido numa fronteira degenerada. "Nenhuma estacionariedade de tipo
algum" exige espaço de configurações **não-limitado** ⇒ **crescimento perpétuo do
volume**. Esta é a leitura literal da abertura 2 ("relaxação transiente que nunca
atinge estacionariedade"). O drive: o volume **cresce monotonicamente sem teto** — por
construção não há distribuição estacionária (Gate 1 abaixo prova isto da regra, não da
simulação).

## 3. Observável e escalas de tempo

Mede-se, ao longo do tempo de simulação `t` (sweeps), no **1-esqueleto** da geometria
CDT 3D em crescimento:
- `z(t) = 2·n_edges/N0` (coordenação — barata, mantida pelo motor),
- `C4(t)` = square clustering médio (`rs_clustering.clustering_metrics` VERBATIM).

Medidos em **escalas de tempo geométricas** ancoradas no volume: registramos `(z, C4)`
quando o volume `N3` cruza `N₀·2^m` para `m = 0,1,2,3` (oitavas `t, 2t, 4t, 8t` em
volume). Octavas em **volume** (não sweeps brutos) garantem comparação self-similar
limpa.

## 4. O descritor adimensional e o teste (PRIMÁRIO)

Descritor self-similar = **expoente local** da relação C4–volume por oitava:
```
p_m = Δ ln C4 / Δ ln N3   na oitava [2^m → 2^{m+1}]   (m = 0,1,2)
```
Um **atrator auto-similar** ⟺ `p_m` **converge** para um valor estável: a relação
C4 ~ N3^p mantém o **mesmo expoente** por oitava (a "forma" é fixa enquanto o tamanho
cresce), mesmo com z e C4 individualmente sem limite.

**Teste (travado):**
- **ESTRUTURA AUTO-SIMILAR ENCONTRADA** sse **as três** valerem:
  1. **Convergência entre oitavas:** `|p₂ − p₁| < |p₁ − p₀|` (a variação por oitava
     **encolhe**) E `|p₂ − p₁| < 0.05`.
  2. **Robustez entre seeds:** `std_seeds(p₂) < |p₁ − p₀|` (a convergência não é ruído;
     a dispersão entre seeds na última oitava é menor que a deriva inicial).
  3. **Não é meramente o equilíbrio:** `p₂` difere do expoente da curva de **equilíbrio**
     C4(N) (controle medido na mesma suíte) por mais que `std_seeds` — i.e. é um
     atrator **dinâmico**, não a curva de equilíbrio reproduzida sob um rótulo de tempo.
- **MORTE (a armadilha de novo)** se **qualquer**:
  1. `p_m` **deriva** (`|p₂ − p₁| ≥ |p₁ − p₀|`, não encolhe) ⇒ "ainda não convergiu".
  2. `std_seeds(p₂) ≥ |p₁ − p₀|` ⇒ ruído mascarado de sinal (lição da varredura x(A)).
  3. `p₂` é indistinguível do expoente de equilíbrio ⇒ não há estrutura nova (é só a
     curva de equilíbrio traçada dinamicamente — não um atrator fora-do-equilíbrio).

**Secundário (registrado, não decisivo):** a razão literal `C4(t)/z(t)` e `C4·z`.
Espera-se que **derivem** (z cresce, C4 decai), o que NÃO é, por si, o critério —
self-similaridade é estabilidade do **expoente**, não da razão crua (charter §B.2:
"ou outra combinação adimensional"; aqui a combinação é o expoente local).

## 5. Anti-circularidade explícita

- Gate 1 prova a **ausência de ponto fixo pela regra** (volume sem termo restaurador +
  aceitação líquida de expansão > 0), não por "a simulação não convergiu".
- Critério §4.2 e §4.3 protegem contra os dois modos de autoengano já vistos: ruído
  entre seeds (x(A)) e "ainda relaxando" (α=0,1).
- Nada de escala física emergente é reivindicado; ⟨z⟩/C4 são geométricos, e a taxa de
  crescimento é `[External]`.
