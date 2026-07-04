# TEORIA_CDT

Teoria de gravidade quântica do tipo **Causal Dynamical Triangulations**, construída do zero
e **independente** de TEIC, DEV e SR (as três teorias nas pastas vizinhas).

## Regra de ouro
**Nada das outras teorias entra como dado.** TEIC/DEV/SR são contexto e anti-padrão, nunca
fundação. Ver `CHARTER.md §3` (linha vermelha anti-contaminação).

## A semente (em uma frase)
A realidade é **informação que se expande**: um evento gera um centro de informação (ex.: um
fóton) que é registrado numa rede que cresce e re-emite essa informação nó a nó. O espaço-tempo
é o **rastro** desse ciclo. A adição original: **a informação SOURCE o crescimento** (não é campo
passivo numa geometria que cresce sozinha). Mesma semente da TEIC — mas hospedada na CDT, o único
substrato com laços e criticalidade (a TEIC colapsou num grafo tipo-árvore mean-field).

## Por onde começar
1. **`CHARTER.md`** — o documento fundacional: a semente (§0.1), o que buscamos em 3 níveis, as
   regras de honestidade, como saberemos se falhamos.
2. **`MAPA_TEIC_BENCHMARK.md`** — a **bússola**: o que reproduzir (sucessos da TEIC) e o que furar
   (paredes da TEIC), com prognóstico honesto por parede. ✅ escrito.
3. **`GLOSSARIO.md`** — termos do zero. ✅ escrito.
4. **`F1_acao/PRE_REGISTRO.md`** — 1º passo real: validar o motor CDT (que é, ao mesmo tempo, a 1ª
   tentativa de furar a parede W1 — a dimensão espectral que corre, que a TEIC não conseguiu). ✅
   travado, **não executado**.

## Estado atual
**NESS_GEOMETRIA — geometria CDT 3D fora-do-equilíbrio: NESS genuíno alcançado, escala NÃO-RESOLVIDA (1º sinal não-limpamente-MF).** (2026-06-29)
`docs/campaigns/NESS_GEOMETRIA/` — Direção 2 (geometria NESS). Veredito completo em
**`docs/campaigns/NESS_GEOMETRIA/SYNTHESIS.md`**. Reusa o motor F1b (`f1b_cdt3d.py`) e a sonda O(3)
(`ferro_cdt`/`cdt_substrate`) intactos; drive paramétrico k₀(τ)=2,5+1,5·cos(2πτ/P).
- **Gate 1 (estacionariedade) PASSA:** o sistema dirigido atinge estado estatisticamente estacionário
  (N₃/z/d_H blocked-stable, 2 seeds, manifold sempre válido, d_H≈2.43 platô) — **não** a armadilha
  α=0,1. Horizonte de relaxação medido (~350–450 sweeps a Vt=1500; therm=140 inicial media na subida).
- **Gate 2 (balanço detalhado) PASSA:** histerese (entropia/ciclo) 8–14σ, sinal-consistente em
  P∈{4,12,32,96}×2 seeds, + **corrente de Pachner fase-resolvida** circulante → DB quebrado. NESS genuíno.
- **Escala (sob NESS): A REPRODUZ** (m/floor 16→30, U₄=0.667, plateau — geometria é fundo sadio);
  **B NÃO-RESOLVIDO: χ_max~N^0.53** — o **dobro** do equilíbrio-CDT (0.24) e o **1º sinal de escala
  não-limpamente-mean-field** do programa, **mas no limiar MF (0.5) com J_c derivando ↓ (MF-like) e
  só 3 tamanhos** → ambíguo, não forçado.
- **RESOLUÇÃO de B (varredura x(A), `b_resolution.py`): MEAN-FIELD — o 0.53 era RUÍDO.** x(A)=
  [0.30, 0.63, 0.38, 0.50] disperso, **sem tendência** com a amplitude (slope +0.05); J_c deriva em
  todo A. **Prova decisiva: A=1.5 deu x=0.53 (1º run) vs 0.38 (este run) a parâmetros idênticos** —
  irreprodutível ⇒ o expoente é noise-dominated, o "realce" era flutuação. A barreira de alta-
  coordenação (z~13) é robusta a equilíbrio **E** não-equilíbrio.
- **Veredito §6: Direção 2 MORTA** (escala sob NESS = mean-field) → **Parte B (gatilho 4D)
  AUTORIZADA e EXECUTADA.**
- **Parte B (`docs/campaigns/CDT_4D_VIABILIDADE/`, gatilho cinemático 4D barato, stacked (1,5),
  gate verde): NÃO ARMADO.** z satura finito (~10, não Poisson) mas o **clustering DECAI rumo ao
  MF** (C4~N^−0.33, transitividade~N^−0.45) — oposto do 3D flipped (saturava em 0.145). Como
  stacked é o regime MAIS aglomerado, o negativo é robusto → **não construir o motor dinâmico 4D**.
- **SALDO: a linha de criticalidade/escala está FECHADA** — equilíbrio (CDT_TEIC_FERRO),
  não-equilíbrio (NESS, 3D) e cinemática 4D, todos mean-field. Somado à semente morta (FS-3D), não
  resta contribuição original viva. Caminho honesto: **F2 como CDT pura [GABARITO] ou PARAR.**

**MEMORIA_DIAGNOSTICO — a morte de D2 é ESTRUTURAL (equilíbrio), não escolha de kernel.** (2026-06-29)
`MEMORIA_DIAGNOSTICO/` (Nível 0 barato: toy 1D Langevin generalizado, SEM CDT, reusa `c_mem`).
Veredito completo em **`MEMORIA_DIAGNOSTICO/SYNTHESIS.md`**. Funil: o Nível 1 (motor FS-3D, caro)
só rodaria se o Nível 0 armasse — **não armou**.
- **Pergunta:** a memória C_mem lava por **equilíbrio** (mixing) ou por escolha do kernel
  exponencial-rápido de FS-3D? Se estrutural, nenhuma semente-de-equilíbrio sobrevive a D2.
- **1ª leitura deu falso-positivo:** com o estimador FS-3D (max_tau=15), power-law/aging davam
  C_mem+ em estacionariedade (+30σ, burn-stable) → "ESPECÍFICO_DO_KERNEL". Ceticismo desmontou:
  (1) exp de τ longo **também** dá +na janela curta → é escala-de-tempo, não forma-da-cauda; (2)
  curva C_mem(τ) em **janela larga** (burn≫τ) → integral reverte p/ **~−0.5 (=FS-3D) para TODO
  kernel que equilibra**; (3) só α=0.1 "sobrevive", mas **não equilibra** (= fora-do-equilíbrio).
- **Veredito ESTRUTURAL:** mixing torna o estado estacionário cego à história p/ qualquer kernel de
  extensão finita. **Lição metodológica:** o C_mem max_tau=15 é janela-limitado (falso-POSITIVO
  possível); a integral de janela larga é correta — mas o resultado **negativo** de FS-3D é robusto.
- **Consequência (muda o desenho do programa):** a busca por **semente-de-equilíbrio** está
  estruturalmente fechada; qualquer semente futura com chance em D2 precisa ser **explicitamente
  fora-do-equilíbrio** (nunca atinge estacionariedade) — o eixo é equilíbrio vs não-equilíbrio,
  não "qual kernel".

## Próximo passo PRÉ-REGISTRADO (não executado)
**`SEMENTE_NEQ_PRE_REGISTRO.md`** — a semente FORA-DO-EQUILÍBRIO, a única classe que o
MEMORIA_DIAGNOSTICO deixou viva. Mecanismo: transporte com **envelhecimento** (κ(s)=κ₀/(1+s/s_age)
→ 0, φ nunca equilibra). Observável bem-posto: **correlação de dois tempos C(t_w+τ,t_w)
t_w-dependente** (aging) — **não** o C_mem-janela-curta que dá falso-positivo (lição do
MEMORIA_DIAGNOSTICO incorporada). **Três** mortes empilhadas: D1 (geometria muda), D2-NEQ (aging
genuíno vs controle estacionário **e** vs κ(s)-sem-campo) e **D3 NOVO (a geometria sobrevive como
fundo p/ F2 — a tensão central, morte mais provável)**. Prior honesto: a morte mais provável é a
**geometria de alta-coordenação do CDT (z~13) equilibrar φ apesar do aging** → fecharia a semente
robusta a equilíbrio E não-equilíbrio. Funil: Nível 0 (toy, estende `MEMORIA_DIAGNOSTICO`) arma o
Nível 1 (motor FS-3D). **Bloqueado até alguém decidir executar.**

### FS-3D (a semente — falsificada, base deste diagnóstico)
**FS-3D EXECUTADO — a SEMENTE foi FALSIFICADA (morre em D2).** (2026-06-28)
`F1b_acao/fs_seed3d.py` (campo φ + acoplamento), `fs_run3d.py` (experimento c/ controles
embutidos). Veredito completo em **`F1b_acao/FS_SYNTHESIS.md`**. O teste vinculante da única
adição original da teoria ("a informação SOURCE o crescimento"), em 2 pontos da fase estendida
(k0=1,3) com o controle markoviano construído desde o início:
- **D1 PASSA** (massivo, +497σ/+764σ): γ>0 muda a geometria vs CDT cega (clump 0.17→12.2).
- **D2 — a semente MORRE:** a assinatura de memória não-markoviana (cauda de C_mem acima do
  controle) está **ausente e revertida** — a semente é anti-persistente (tail −0.55), o controle
  *memoryless* é MAIS persistente (+1…+8); robusto a k0 e a κ (κ=0.6: −21σ). A memória **lava no
  equilíbrio**, exatamente o prior §4 do pré-registro.
- **Consequência:** "informação SOURCE o crescimento" é **indistinguível de um peso de
  crescimento** → a TEORIA_CDT, no que reproduz (d_H, fases), é **CDT-com-peso, não teoria nova**.
  Morte limpa e falsificável (charter §6), decidida ANTES de gastar numa F2-com-semente.

### F1b (motor 3D — base sobre a qual FS-3D rodou)
**F1b EXECUTADO — motor CDT 3D VALIDADO + curvatura dinâmica.** (2026-06-28)
`F1b_acao/f1b_cdt3d.py` (motor 3D: complexo simplicial explícito, 5 Pachner foliados, ação
dinâmica S=−k0N0+k3N3, MC, gate E0-3D), `f1b_phase.py` (scan de fases), `f1b_dH.py` (d_H).
Veredito completo em **`F1b_acao/F1b_SYNTHESIS.md`**.
- **E0-3D VERDE:** invariantes de manifold causal 3D (link-S², fatia-S², Euler χ=0) preservados
  após 10⁴ moves; 5 movimentos reversíveis bit-a-bit; balanço detalhado por *apply-then-undo*.
  Um validador agnóstico-ao-movimento pegou e matou um bug do (2,3)/(3,2) (aresta nova precisa
  ser tipo-tempo). **Resolve o bloqueio "não há motor 3D no repo".**
- **Fases emergem:** estendida (k0≲5) ↔ degenerada/branched-polymer (k0≳6), transição nítida em
  k0≈5–6 (maxcoord/méd salta ~3→13; IPR cai ~19→9).
- **Gate-mor d_H (curvatura DINÂMICA):** d_H **corre com k0** (2.68→1.87) — ao contrário do 2D
  onde era constante (folheação só). Na fase estendida d_H **sobe com o volume** (2.45→2.87,
  **45σ por blocking**; ref. fina=2.06; extrap. física 3.1–3.3) = **geometria 3D genuína emerge**.
- **Divulgação de transparência:** o gate fechou por **critério SUBSTITUTO** (d_H), não pelo
  perfil de-Sitter cos² pré-registrado (R²≤0.41, limite de volume) — declarado em FS/F1b_SYNTHESIS.

### Histórico
**F1 EXECUTADO E VERDE — maquinaria 2D-CDT validada.** (2026-06-28)
`F1_acao/f1_cdt2d.py` (motor + gate E0), `f1_controls.py` (validação do estimador de d_H),
`f1_run.py` (gate G1–G5). Veredito completo em **`F1_acao/F1_SYNTHESIS.md`**.
- **E0 VERDE:** invariantes de manifold causal, Euler χ=0, reversibilidade add↔delete, flip
  involutivo — todos OK após 10⁴ e 2×10⁵ moves.
- **G1 VERDE (gate-mor):** d_H = **2.08±0.02**, reproduz a bidimensionalidade da 2D-CDT
  (≠ d_H=4 do DT euclidiano); separado de controles 1D (0.99) e 3D (2.60). Estimador
  calibrado contra geometrias conhecidas antes de ler a física.
- **G4 VERDE (c/ nota):** τ_int≈260 sweeps finito — *critical slowing down* em λ=ln2 (esperado).
- **G5 VERDE:** hot vs cold coincidem (0.9σ com blocking; o 7.68σ ingênuo era artefato de
  autocorrelação — pego pela disciplina de erro).
- **Ressalva honesta:** G2/G3 confirmados qualitativamente (⟨ℓ⟩=Vt/2T exato, correlador suave),
  mas o teste de **forma-fechada AL98** (KS/R²) fica para F1b (exige re-derivar a matriz de
  transferência *in-theory* — anti-contaminação).

### Escrutínio pré-F1b (3 tarefas, 2026-06-28) — feitas
- **Tarefa 1 (gatilho cinemático fechado no substrato certo):** ⟨z⟩ e C4 do 1-esqueleto do CDT
  foliado de F1, estimadores VERBATIM dos Gatilhos 1/2. ⟨z⟩=6 (Euler-trivial); **C4=0.103 ≠
  genérico 0.149 a ~18σ** → C4 não-trivial, discrimina CDT de mean-field. ARMADO confirmado.
  (`TEIC/docs/campaigns/CDT_VIABILIDADE/SYNTHESIS.md`, atualização datada.)
- **Tarefa 2 (controle c=1 → D1 REBAIXADO):** varredura γ×κ. Em κ=0 (campo genérico sem
  transporte) o colapso d_H 2.07→1.60 + clumping ×11 **já acontece** → é a barreira
  c=1/branched-polymer genérica, não a semente. O "positivo" FS-2D é **não-específico à
  semente**; evidência pró-semente depende **inteiramente de D2/C_mem em 3D**.
- **Tarefa 3 (gate de fases 3D):** **NÃO-VERDE — NÃO EXECUTADO.** Rodá-lo = construir+validar o
  motor CDT 3D (= F1b inteira), não validável com integridade numa sessão. Pré-registro
  shovel-ready em **`F1b_PHASE_GATE.md`**. ⇒ **FS-3D (semente em 3D) BLOQUEADO** até motor 3D
  validado na fase de-Sitter.

**Próximo passo:** **F1b — construir e validar o motor CDT 3D PURO** (E0-3D + gate de fases de
`F1b_PHASE_GATE.md`), pré-requisito de tudo: do teste vinculante da semente (FS-3D: D2/C_mem) e
de F2. A semente (informação SOURCE o crescimento) está pré-registrada (`SEMENTE_PRE_REGISTRO.md`)
mas **bloqueada** até o motor 3D existir e passar o gate.

## A frase de uma linha
Construir CDT de verdade (com ação dinâmica, não só cinemática) e descobrir, sem auto-engano,
se a geometria do espaço-tempo emerge dela — sabendo de antemão que a escala absoluta
provavelmente continua externa, e que o ganho realista é uma razão ou expoente, não G/ℏ/a₀.

## Origem
Esta teoria nasce do único sobrevivente da "fila de substratos" investigada no pipeline TEIC
(`TEIC/docs/campaigns/CDT_VIABILIDADE/`): a classe tipo-CDT foi a única a passar os dois filtros
cinemáticos baratos — mas passou **fraco** (em 2D as barreiras são triviais por construção), e
o teste não tinha dinâmica. Daí esta teoria: fazer o trabalho de verdade, com ação.
