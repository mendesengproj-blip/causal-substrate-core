# GLOSSÁRIO — TEORIA_CDT

> Termos definidos **do zero**, para este programa ser autocontido. Um leitor sem CDT prévia
> deve conseguir ler o `CHARTER.md` e os pré-registros só com isto ao lado. Ordem: dos blocos
> à dinâmica.

---

## Os blocos

**Simplex.** O "tijolo" de dimensão mínima. Um 0-simplex é um **ponto** (vértice); 1-simplex é
uma **aresta**; 2-simplex é um **triângulo**; 3-simplex é um **tetraedro**; 4-simplex é o
análogo em 4D. Uma triangulação de dimensão *d* é feita colando *d*-simplices pelas faces.

**Aresta de comprimento fixo.** Nesta teoria, **toda aresta tem o mesmo comprimento** (uma
unidade `[External]`, ver `CHARTER.md §3.1`). A geometria **não** está nas posições dos pontos
(não há coordenadas) — está **na combinatória de como os simplices são colados**. Curvatura,
distância, dimensão: tudo é lido da rede de colagens, não de coordenadas.

**Hinge (dobradiça).** O lugar onde a curvatura "mora" numa triangulação. Em 2D é um **vértice**;
em *d* dimensões é um (*d*−2)-simplex. A curvatura é concentrada nos hinges (curvatura de Regge),
não espalhada suavemente.

**Deficit angle (ângulo de déficit).** A medida discreta de curvatura num hinge. Some os ângulos
de todos os simplices que encostam num hinge; o quanto falta (ou sobra) para fechar o "plano"
(2π em torno de um vértice em 2D) é o ângulo de déficit δ. δ>0 = curvatura positiva (esfera);
δ<0 = negativa (sela); δ=0 = plano. **A curvatura de uma triangulação É a coleção dos δ.**

---

## A estrutura causal (o "C" de CDT)

**Folheação (foliation).** A triangulação é organizada em **fatias de tempo** (spatial slices)
empilhadas: fatia 0, fatia 1, fatia 2... Cada fatia é uma geometria espacial pura (dimensão
*d*−1); os simplices que ligam uma fatia à seguinte preenchem o "tempo" entre elas. É o que torna
a teoria **causal**: existe uma noção global de "antes/depois" embutida na construção.

**Aresta tipo-espaço / tipo-tempo.** Arestas **dentro** de uma fatia são tipo-espaço; arestas
que **ligam fatias vizinhas** são tipo-tempo. Elas podem ter comprimentos (ao quadrado)
diferentes — a razão entre eles é o parâmetro **α** (ver Rotação de Wick).

**Por que a folheação importa (a lição que motiva esta teoria).** Triangulações **sem** estrutura
causal (DT euclidiano puro) colapsam em geometrias patológicas (ver Branched-polymer). A
folheação proíbe esses colapsos — é o ingrediente que faz a CDT funcionar onde o DT falha. **Não
é opcional; é o coração da teoria** (`CHARTER.md §5`).

**Movimento de Pachner.** As "jogadas" locais que transformam uma triangulação válida em outra,
varrendo o espaço de todas as colagens possíveis. Ex. em 2D: o **flip** troca a diagonal de dois
triângulos adjacentes; a inserção **(1,3)** põe um vértice dentro de um triângulo. Um conjunto de
movimentos é **ergódico** se, repetido, alcança qualquer triangulação válida. Na CDT, os
movimentos têm que **preservar a folheação** (não podem rasgar as fatias de tempo).

---

## A dinâmica

**Ação de Regge.** A versão discreta da ação de Einstein-Hilbert (a "energia" de uma geometria).
Numa triangulação, ela tem dois termos: um de **curvatura** (soma dos ângulos de déficit nos
hinges, pesada por 1/G — a constante de Newton) e um de **volume** (número de simplices, pesado
pela constante cosmológica λ). Esquematicamente: **S = −(curvatura)/16πG + λ·(volume)**.
> **Cuidado dimensional (decisão de F1):** em **2D** o termo de curvatura é um **invariante
> topológico** (Gauss-Bonnet: a curvatura total só depende do "número de buracos" da superfície,
> não da geometria). Logo, em 2D, a ação efetiva é **só o termo de volume** — a dinâmica vem da
> **entropia** (quantas triangulações há de cada tipo), não da curvatura. Em **3D/4D** o termo de
> curvatura é dinâmico de verdade. Isto molda o que cada dimensão pode testar.

**Soma sobre geometrias (integral de caminho).** A teoria não escolhe **uma** triangulação — ela
**soma todas**, cada uma pesada por e^{−S} (após a rotação de Wick). Quantidades físicas são
**médias** sobre esse ensemble. É o análogo discreto da integral de caminho de Feynman para a
geometria do espaço-tempo.

**Rotação de Wick.** A soma com peso e^{iS} (tempo real) é oscilatória e impossível de amostrar
numericamente. Continua-se analiticamente para "tempo imaginário", virando e^{−S} (um peso de
Boltzmann, positivo, amostrável por Monte Carlo). Na CDT isso é feito **continuando o parâmetro α**
(razão tipo-tempo/tipo-espaço) para valores onde a soma converge. A estrutura causal (folheação)
é o que torna essa rotação **bem-definida** — outra razão de o "C" ser essencial.

**Monte Carlo (MCMC).** O método de amostrar o ensemble: parte-se de uma triangulação, aplicam-se
movimentos de Pachner aceitos/rejeitados com probabilidade que reproduz o peso e^{−S} (Metropolis).
Depois de "equilibrar", as configurações visitadas são amostras típicas, e médias sobre elas são
as previsões da teoria.

---

## O que se mede (os observáveis de geometria)

**Dimensão de Hausdorff (d_H).** "Quantas dimensões o espaço-tempo *tem* em larga escala." Mede-se
vendo como o **volume cresce com a distância**: numa rede *D*-dimensional, o número de pontos
dentro de raio *r* cresce como *r^D*. Se a geometria emergente é física, d_H deve dar ≈ a
dimensão alvo (ex.: 4 em 4D). Se d_H **diverge**, a geometria é patológica (ver Branched-polymer).

**Dimensão espectral (d_s).** "Quantas dimensões o espaço-tempo *parece ter* para um processo de
difusão" (uma partícula que faz random walk). Mede-se pela probabilidade de retorno do walk. O
resultado **célebre** da CDT real: d_s **corre** de ≈4 em larga escala (IR) para ≈2 em pequena
escala (UV) — o espaço-tempo "afina" de 4 para 2 dimensões no ultravioleta. Reproduzir isso é um
alvo de validação (Nível A do charter), não descoberta.

**Branched-polymer / crumpled (as patologias a evitar).** As duas fases doentes. **Branched-
polymer:** a geometria vira uma "árvore de galhos" ramificada, com d_H → ∞ (toda direção foge
para um galho novo) — o que o DT euclidiano sem folheação produz. **Crumpled:** o oposto, tudo
colapsa num ponto de coordenação infinita, d_H → ∞ também. A CDT existe **porque** a folheação
abre uma **terceira fase** (estendida, geometria física) entre essas duas. **Morte A** do charter
= não achar essa terceira fase.

---

## Os parâmetros e o que conta como resultado

| Símbolo | É | Estatuto |
|---|---|---|
| comprimento da aresta | a unidade de tamanho | **`[External]`** — inserido, nunca "emergente" |
| α | razão (comprimento tipo-tempo)²/(tipo-espaço)² | parâmetro de Wick; escolhido |
| G (Newton) / κ | peso do termo de curvatura | acoplamento (varre-se o diagrama de fases) |
| λ (cosmológica) | peso do termo de volume | acoplamento (ajustado para volume-alvo) |
| **d_H, d_s** | dimensões emergentes | **RESULTADO** (medido, não inserido) |
| **expoentes críticos** | no ponto de 2ª ordem | **RESULTADO** — a ponte para o contínuo (Nível B) |

**Regra de leitura (anti-auto-engano, `CHARTER.md §3`):** os acoplamentos G, λ, α são **entradas**
que varremos; a aresta é **externa**. Só contam como **emergentes/resultado** as **dimensões**
(d_H, d_s) e os **expoentes adimensionais** no ponto crítico. Nada que dependa do tamanho da
aresta pode ser chamado de "escala que emergiu".

---

**Próximo:** `F1_acao/PRE_REGISTRO.md` — define o ensemble causal concreto + a ação de Regge + o
gate de validação (em 2D, reproduzir resultados de CDT exatamente conhecidos), tudo congelado
antes de qualquer código.
