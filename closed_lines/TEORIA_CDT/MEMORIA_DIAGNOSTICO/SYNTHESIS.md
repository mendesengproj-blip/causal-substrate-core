# SYNTHESIS — A memória lava por ESTRUTURA (equilíbrio), não por escolha de kernel

> **Pré-registro:** `PRE_REGISTRO.md` (critérios congelados antes de rodar). **Código:**
> `nivel0_toy.py` (modelo + estimador `c_mem` reusado de `F1b_acao/fs_seed3d.py`),
> `nivel0_decisive.py` (diagnóstico de janela). **Dados:** `nivel0_decisive.json`,
> `nivel0_toy.json`. **Data:** 2026-06-29. Diagnóstico em funil sobre a morte de D2 em FS-3D.

---

## VEREDITO NÍVEL 0: **ESTRUTURAL** — a morte de D2 generaliza a todo kernel que equilibra. **Nível 1 NÃO roda.**

A memória (C_mem) **lava em equilíbrio para qualquer kernel que de fato equilibra no horizonte
observado**, independente da forma (exponencial curto/longo, lei-de-potência α=0.3–0.5,
envelhecimento). Memória só sobrevive em kernel que **nunca equilibra** (= explicitamente
fora-do-equilíbrio). Pela regra do funil (pré-registro), **o Nível 1 (motor FS-3D, caro) NÃO é
executado** — registrar e parar é o resultado certo, e ele **fecha estruturalmente a busca por uma
semente-de-equilíbrio**.

## A descoberta que evitou um falso-positivo caro (e por que o funil funcionou)

A **primeira leitura** (estimador FS-3D, `c_mem` com max_tau=15) dizia **ESPECÍFICO_DO_KERNEL**:
K2 (power-law) e K3 (aging) davam C_mem-tail **positivo** em estacionariedade (+0.15, +1.97),
+30σ, robusto a burn-in — o que **armaria o Nível 1**. Ceticismo disciplinado (o controle exigido
pelo pré-registro) desmontou isso em três passos:

1. **Controle "exp de τ longo":** um exponencial com τ_m grande (τ=50→+1.3, τ=400→+9.5) **também**
   dá tail positivo na janela curta. Logo **não é a forma da cauda (power-law)** — é a **escala de
   tempo de memória vs a janela de medição**.
2. **Curva C_mem(τ) em janela LARGA (max_tau=200–400) com burn-in pleno (40000 >> τ):** a
   integral completa reverte para **~−0.5 (anti-persistente, idêntico ao FS-3D)** para TODOS os
   kernels que equilibram — exp(τ=5,50), power(α=0.3,0.5), aging. O "+positivo" da janela curta
   era o **bump de curto-lag** que qualquer kernel lento tem; ao capturar a decaída completa
   (incluindo a parte anti-persistente da mean-reversion), a integral é **negativa**.
3. **α=0.1 (cauda extrema):** o único "sobrevivente" — mas **falha a checagem de
   estacionariedade** (equilibrou=0%, variância não-platô) e dá valores numéricos selvagens
   (±tens) = processo que **não mistura no horizonte** = literalmente **fora-do-equilíbrio**, não
   memória estacionária.

**Tabela definitiva** (`nivel0_decisive.json`; integral de C_mem dos incrementos, regime
estacionário; janela CURTA = Σ[1..15] = estimador FS-3D; janela LARGA = Σ[1..400] = decisiva):

| kernel | CURTA (FS-3D) | LARGA (decisiva) | equilibrou? | preserva? |
|---|---|---|---|---|
| white (controle) | ~0 | ~0 | sim | — |
| **K1 exp τ=5 (FS-3D)** | −0.62 | **−0.49** | sim | não (lava) |
| exp τ=50 (longo) | **+1.32** (falso+) | **−0.51** | sim | não (lava) |
| **K2 power α=0.5** | **+0.19** (falso+) | **−0.51** | sim | não (lava) |
| K2 power α=0.3 | **+0.55** (falso+) | −0.44 | sim | não (lava) |
| power α=0.1 (extremo) | +14.6 | −4.1 (selvagem) | **NÃO (0%)** | — (fora-eq) |
| **K3 aging** | +1.97 (curto)/−0.02 | **−0.51** | sim | não (lava) |

## Por que ESTRUTURAL (o mecanismo, confirmado)

A hipótese estrutural do enunciado está **confirmada**: um processo que satisfaz balanço detalhado
e atinge medida estacionária é, por mixing/ergodicidade, **cego à própria história** nesse estado.
Concretamente: **qualquer kernel com extensão de memória finita** (qualquer kernel fisicamente
realizável e que equilibre) **mistura dado burn-in suficiente**, e então a assinatura C_mem dos
incrementos lava para o valor anti-persistente imposto pelo vínculo (mean-reversion) — o **mesmo
−0.5 do FS-3D**. A "sobrevivência" só ocorre quando a extensão de memória é **efetivamente
infinita** (α→0: o kernel truncado vira média-móvel quase-plana, mixing-time >> horizonte) — i.e.,
o processo **nunca equilibra**, que é precisamente o regime **fora-do-equilíbrio**.

## Lição metodológica (registrar — afeta qualquer teste D2 futuro)

**O estimador C_mem com max_tau=15 (o usado em FS-3D) é janela-limitado e pode dar FALSO-POSITIVO
de memória:** o bump de curto-lag de um kernel lento aparece como tail positivo, sem ser
dependência de longo alcance genuína. **A integral de janela larga (até capturar a decaída
completa) é o diagnóstico correto.** Corolário tranquilizador: **o resultado NEGATIVO de FS-3D é
robusto** (negativo na janela curta ⇒ certamente negativo/lavado na janela larga — a janela larga
só adiciona mais decaída anti-persistente); a janela curta só engana na direção de falso-POSITIVO,
que FS-3D não teve. A morte de D2 em FS-3D está **confirmada e reforçada**.

## Consequência para o programa (muda o desenho, não só o kernel)

A busca por uma **semente-de-equilíbrio** está **estruturalmente fechada**: nenhuma semente cujo
mecanismo de memória equilibre (qualquer kernel exponencial OU power-law truncado) sobreviverá a
D2 — a geometria emergente no estado estacionário é cega à história, por teorema (mixing). Portanto:

> **Qualquer semente futura com chance em D2 precisa ser explicitamente um sistema
> FORA-DO-EQUILÍBRIO** — dinâmica que nunca atinge estacionariedade no horizonte físico
> (envelhecimento/glassy genuíno, memória não-truncada, ou condução com fonte/sorvedouro
> permanente). Isso **muda o desenho de toda campanha de semente subsequente** (o eixo não é "qual
> kernel", é "equilíbrio vs não-equilíbrio") — e o ônus de pré-registrar um observável de
> não-equilíbrio bem-posto (não só C_mem, que é um diagnóstico de série temporal estacionária)
> recai sobre ela.

## O que NÃO foi feito (honestidade)
- **Nível 1 não rodou** — corretamente, pelo critério ESTRUTURAL pré-registrado. Não há "porte de
  kernel" a testar no motor caro, porque nenhum kernel-de-equilíbrio sobrevive ao Nível 0.
- O modelo de brinquedo é 1D mean-revertido; o CDT é mais rico (geometria dinâmica, alta
  coordenação). Mas o argumento é de **mixing/ergodicidade**, que é mais forte (não mais fraco) num
  substrato que mistura rápido — o CDT de z~13 (visto em CDT_TEIC_FERRO) mistura ainda melhor, o
  que **reforça** o veredito estrutural, não o enfraquece.

**Resumo de uma linha:** no Nível 0 barato (toy 1D, sem CDT), a assinatura de memória C_mem **lava
em equilíbrio para todo kernel que equilibra** (exp curto/longo, power-law α≥0.3, aging) — os
positivos eram **artefato da janela curta** do estimador FS-3D, desfeitos pela integral de janela
larga (todos → −0.5, = FS-3D); só kernels que **nunca equilibram** retêm memória, confirmando que
o problema é o **equilíbrio em si** (mixing), não a escolha de kernel — logo **D2 fecha
estruturalmente a semente-de-equilíbrio**, o **Nível 1 não roda**, e qualquer semente futura tem
de ser **explicitamente fora-do-equilíbrio**.
