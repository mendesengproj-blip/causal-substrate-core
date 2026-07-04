# A.2 — Releitura analítica: o que Palm já fecha, e o candidato que sobra

**Data:** 2026-06-30 · **Antes de qualquer código** (charter A.2).
**Fonte relida:** `TEIC/docs/campaigns/IMPOSSIBILIDADE_PARCIAL/RESULTADO.md`, §3.1
(esboço de prova) e §3.4 (aberturas), e `REPULSAO_LORENTZ/docs/FRONTEIRA_CONHECIDA.md`.

---

## 1. O que o argumento de Palm já fecha — e por quê isto inclui ordem superior SOBRE POISSON

A fórmula de Campbell–Mecke usada no teorema parcial dá, para a valência de um evento
típico de um *sprinkling de Poisson* Φ:

> ⟨z⟩ = ρ ∫_{cone futuro} h(i, x_j) d^d x_j ,  com  h(i, x_j) = E_Φ[ 1(i, x_j conectados) ].

O ponto crucial (§3.1 do RESULTADO): **`h` é a probabilidade de conexão
MARGINALIZADA sobre o resto do processo.** Mesmo que a regra de conexão dependa de
**trios ou k-tuplas** (i, x_j e mais um/vários eventos), ao tomar a esperança `E_Φ`
sobre os demais pontos a dependência de ordem superior é **absorvida na média** `h`.
E por invariância de Poincaré, `h` só pode depender do invariante de par `Δτ_ij`.
Logo o argumento — fator hiperbólico `Vol(H^{d−1}) = ∞` — **reaparece idêntico**, e
⟨z⟩ diverge.

**Por que a marginalização é limpa exatamente sobre Poisson (Slivnyak–Mecke).** A
propriedade de Slivnyak–Mecke diz que a distribuição de Palm reduzida de um processo
de Poisson é **o próprio Poisson** (condicionar a ter pontos em i, x_j não muda a lei
dos outros pontos — eles permanecem Poisson independente). Por isso a esperança sobre
"o resto" que define `h` é uma integral contra a medida de Poisson **não-condicionada**,
e a fórmula de Campbell–Mecke de ordem k **fatoriza** da mesma maneira. Conclusão:

> **Correlações/regras de conexão de QUALQUER ordem finita, definidas sobre o
> *sprinkling de Poisson*, caem sob o mesmo teorema parcial.** A "porta não-pairwise"
> está fechada **enquanto a medida de base for Poisson**.

Isto é a generalização natural antecipada no charter A.2: *higher-order over Poisson
also falls*. **Registrado como fechamento adicional do mapa** (atualiza
`FRONTEIRA_CONHECIDA.md`).

## 2. O que NÃO está fechado — o único candidato genuíno

O fechamento de §1 usa Slivnyak–Mecke, que é uma **propriedade exclusiva do Poisson**.
Se a medida de base **não** for Poisson, condicionar a ter pontos em i, x_j **muda** a
lei do resto (há correlação), `h` deixa de fatorizar trivialmente, e o argumento não se
aplica diretamente. Essa é precisamente a abertura 1 residual da
`REPULSAO_LORENTZ/FRONTEIRA_CONHECIDA.md`:

- A campanha REPULSAO_LORENTZ já testou um caso **não-Poisson de ordem 2** (Matérn II,
  repulsão de par) → **morreu** (a região de exclusão invariante é a banda não-compacta
  do cone). Mas isso cobre só a **estrutura de par** da medida.
- **Sobra**: uma medida de base **não-Poisson com estrutura genuína de ordem ≥3**
  (correlação de tripla não-redutível a pares), invariante de Lorentz. Não coberta nem
  por Palm/Slivnyak (não-Poisson) nem pela campanha de repulsão (que era ordem 2).

## 3. DECISÃO (charter A.2)

> O fechamento analítico de §1 cobre **ordem superior sobre Poisson** — ali **não há
> experimento a fazer**. Mas o candidato de §2 — **Gibbs com potencial de tripla
> genuíno sobre medida não-Poisson** — **não está coberto**. O charter A.2 manda
> prosseguir a A.3 exatamente neste caso. **DECISÃO: prosseguir para A.3**, com um
> potencial de tripla `V₃` que (gate obrigatório) seja comprovadamente **não-fatorável**
> em um `V₂` efetivo — senão a "morte" é reclassificação (não era genuinamente
> não-pairwise).

**Expectativa honesta (prior, não conclusão):** o mecanismo geral já confirmado duas
vezes (não-localidade forçada por invariância) prevê que um `V₃` construído dos
invariantes da tripla aja sobre **órbitas de configuração não-compactas** (a tripla
pode ser deslizada/boosted ao longo do cone), repetindo a falha. Mas isto é conjectura
quanto à tese geral — por isso **medimos**.
