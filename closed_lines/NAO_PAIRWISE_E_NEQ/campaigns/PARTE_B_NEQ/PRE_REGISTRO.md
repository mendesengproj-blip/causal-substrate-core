# PRÉ-REGISTRO — Parte B: geometria genuinamente fora-do-equilíbrio (crescimento)

**Data:** 2026-06-30 · **Critérios travados ANTES de rodar.** O critério não-circular
está em `B2_CRITERIO.md` (congelado primeiro, conforme charter B.2).

## 1. Motor e drive

Reusa o motor CDT 3D validado (`F1b_acao/f1b_cdt3d.CDT3D`, 5 movimentos de Pachner
intactos, validador `check_manifold` como oráculo de cada configuração) — o mesmo da
NESS_GEOMETRIA. **Diferença vs NESS:** NESS atinge um NESS estacionário (e morreu por
escala MF); aqui o sistema **nunca estaciona** — o volume cresce sem teto.

**Drive de crescimento perpétuo:** remove-se o trava-volume (`eps = 0`, sem termo
`eps·(N3−Vt)²`) e fixa-se `k3` **abaixo do crítico** de modo que a aceitação líquida
dos movimentos (2,6)/(6,2) favoreça expansão (`⟨ΔN3⟩ > 0` por sweep). `k0` fixo
(fase estendida). Resultado: `N3(t)` cresce monotonicamente, sem limite.

## 2. Gates obrigatórios

1. **Gate 1 — ausência de ponto fixo PELA REGRA (formal, não empírica):** demonstrar
   da própria dinâmica que não há estado estacionário: (a) não há termo restaurador de
   volume (`eps = 0`); (b) a corrente líquida de volume é estritamente positiva e não
   decai a zero (`⟨ΔN3/sweep⟩ > 0` mantido). Sem termo restaurador + corrente positiva
   persistente ⇒ `N3 → ∞`, nenhuma medida estacionária possível. (Verificação empírica
   de `⟨ΔN3⟩>0` acompanha, mas o argumento é da regra.)
2. **Gate 2 — múltiplas escalas de tempo:** medir `(z, C4)` nas oitavas de volume
   `N3 = N₀·2^m`, `m=0..3` (B2 §3), e os expoentes por oitava `p_m` (B2 §4).
3. **Gate 3 — múltiplas seeds:** repetir com ≥4 seeds; comparar `std_seeds(p₂)` à
   deriva entre oitavas (B2 §4.2). Se a variação entre seeds ≈ variação entre oitavas:
   ruído, não estrutura.
4. **Controle de equilíbrio:** medir o expoente da curva C4(N) **de equilíbrio** (volume
   travado, mesma suíte) para o teste B2 §4.3.
5. **Manifold válido** em toda configuração medida (validador verde).

## 3. Critérios de veredito

Conforme `B2_CRITERIO.md` §4 (travado):
- **ESTRUTURA AUTO-SIMILAR ENCONTRADA:** as três condições de §4 (convergência de `p_m`
  entre oitavas + robustez entre seeds + distinção do equilíbrio).
- **MORTE (armadilha):** deriva de `p_m`, ou ruído entre seeds ≥ deriva, ou `p₂` ≡
  equilíbrio (sem estrutura nova).

## 4. Funil

Puramente estrutural/cinemático. **Ferromagneto e ξ NÃO rodam.** Só ESTRUTURA
AUTO-SIMILAR autoriza prosseguir (com report e autorização). Morte ⇒ fecha a abertura 2.
