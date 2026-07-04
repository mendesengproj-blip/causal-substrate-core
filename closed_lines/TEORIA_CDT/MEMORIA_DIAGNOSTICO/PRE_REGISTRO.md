# PRÉ-REGISTRO — A memória lava por ESTRUTURA (equilíbrio) ou por ESCOLHA de kernel?

> **Congelado ANTES de rodar.** Data: 2026-06-29. Diagnóstico em funil sobre a morte de D2 em
> FS-3D (`F1b_acao/FS_SYNTHESIS.md`): a assinatura de memória C_mem estava ausente/revertida no
> equilíbrio, robusta a k₀ e κ. Pergunta: isso é **estrutural** (qualquer kernel que equilibre
> mata a memória — mixing/ergodicidade cega o estado estacionário à história) ou **específico do
> kernel exponencial-rápido** usado (e um kernel de cauda longa / medição transiente escaparia)?
>
> **Funil (mesma disciplina dos gatilhos):** Nível 0 = modelo de brinquedo 1D, sem CDT, custo de
> minutos. Nível 1 (motor FS-3D, caro) **só roda se o Nível 0 armar** ("ESPECÍFICO DO KERNEL" ou
> "transiente preserva"). Se Nível 0 der "ESTRUTURAL" em todas as variantes, **não rodar Nível 1**
> — registrar e parar fecha a busca por semente-de-equilíbrio.

---

## NÍVEL 0 — modelo de brinquedo (pré-registrado)

### Processo
Processo escalar 1D mean-revertido com **memória** (Langevin generalizado discreto, overdamped):
> x_t = x_{t-1} − θ·dt·Σ_{j=1..W} K(j)·x_{t−j} + σ√dt·ξ_t,  Σ_j K(j)=1, ξ_t ~ N(0,1) iid.

O termo de restauração mean-reverte (análogo do **vínculo de volume fixo** do FS-3D, que torna o
crescimento anti-persistente). O sinal medido = **incrementos** dx_t = x_t − x_{t−1} (o análogo do
"growth_by_slice" de FS-3D, um fluxo/incremento), agregado sobre `n_real` realizações
independentes (as "colunas/fatias" do estimador). **C_mem é medido pela MESMA função `c_mem` de
`F1b_acao/fs_seed3d.py`** (reusada, não reimplementada); cauda + erro por `cmem_tail_with_error`.

### Os três kernels (eixo 1 — FORMA do kernel)
- **K1 — exponencial** (o de FS-3D): K(j) ∝ e^{−j/τ_m}, τ_m curto → memória decai rápido, mixing
  garantido. É o NULO-de-referência (deve reproduzir a morte de FS-3D: cauda ausente/revertida).
- **K2 — lei de potência** (cauda longa): K(j) ∝ j^{−α}, 0<α<1 (α=0.5) → memória decai lento,
  candidato a NÃO-mixing em horizonte finito.
- **K3 — envelhecimento/glassy** (não-estacionário): escala de memória CRESCE com o tempo,
  τ_m(t)=τ_m0·(1+t/t_age) → nunca atinge kernel estacionário fixo no horizonte simulado.

### Os dois regimes (eixo 2 — REGIME de medição, NÃO confundir com eixo 1)
- **(a) estacionário:** após relaxar até estacionariedade declarada (mesmo critério-tipo do FS-3D:
  burn longo + checagem de platô de variância 1ª-metade vs 2ª-metade da janela).
- **(b) transiente:** medido a partir de t=0, ANTES de qualquer declaração de equilíbrio.

### Controle (baseline)
Processo puramente markoviano = **ruído branco** (ξ_t iid, sem força de memória). Por construção,
C_mem dos incrementos ≈ 0 (sem persistência) em AMBOS os regimes. Valida o estimador/zero.

### Entregável: TABELA ÚNICA 3 kernels × 2 regimes (+ controle) de C_mem-tail ± erro (blocking).

## CRITÉRIOS (congelados, sem ajuste depois)
- **ESTRUTURAL (a morte de D2 generaliza):** K1, K2 e K3 — TODOS medidos em **estacionariedade** —
  dão C_mem-tail ausente ou revertido (≈0 ou <0, dentro de ~3σ do controle / abaixo dele),
  **independente da forma do kernel**. ⇒ o problema é o **equilíbrio em si**, não a escolha de K1.
  Qualquer semente futura precisaria operar **fora do equilíbrio**. ⇒ **NÃO rodar Nível 1; parar.**
- **ESPECÍFICO DO KERNEL (há caminho):** algum kernel (esp. K2/K3) preserva C_mem-tail **positivo
  e > 3σ acima do controle** em estacionariedade declarada; OU o **regime transiente (b)** preserva
  C_mem positivo para K1 mesmo que o estacionário (a) não. ⇒ **arma o Nível 1** (portar SÓ esse
  kernel/regime à semente).
- **PARCIAL/NÃO RESOLVIDO:** kernel ambíguo (nem claramente preserva nem claramente lava, p.ex.
  cauda positiva mas <3σ, ou dependente do horizonte) ⇒ registrar como **não resolvido** + qual
  extensão de horizonte temporal resolveria. **NÃO** tratar como decisivo, **NÃO** armar Nível 1.

## NÍVEL 1 — confirmação no motor FS-3D (CONDICIONAL)
Só se Nível 0 armar. Porta **apenas** o kernel/regime sobrevivente para a semente (mantendo
exp(γ(φ−φ̄)) + depósito idênticos), repete o teste D2 vinculante de FS-3D **com o controle
markoviano embutido**, aplica o MESMO critério binário (C_mem acima do controle = sobrevive;
ausente/revertido = morre), sem ajuste posterior.

## Anti-circularidade / disciplina
Nada "escala emergiu" (não há escala em teste). Estimador C_mem reusado verbatim. Eixos FORMA e
REGIME testados **separados** (a tabela existe para não misturá-los). Resultado parcial ≠ decisivo.

**Resumo de uma linha:** decidir, barato e fora da CDT, se C_mem-tipo sobrevive em estado
estacionário para **algum** kernel (cauda longa K2 / envelhecimento K3) ou no **transiente** — ou
se é estruturalmente nulo para todo kernel que equilibra; só o segundo arma o caro Nível 1.
