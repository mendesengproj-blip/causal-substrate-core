# M1b — FLANCO PENTAGONAL: pré-registro

**Data:** 2026-07-04 · **Pasta:** `FRONTEIRA_COMPACTA/M1B_FLANCO_PENTAGONAL/`
**Antecedente:** M1 §6 (alvo nomeado) + core_paper Sec. IV ("declared flank") +
Table de fronteiras item 1.
**Natureza:** analítica com gate computacional de certificados finitos.

---

## 1. A pergunta (herdada de M1, verbatim)

> **Alvo nomeado M1b:** provar "pentágono-percolante + homogêneo ⇒ valência
> infinita" OU construir o contraexemplo (= morte 2, descoberta maior).

Objeto: ordem parcial $(P,\prec)$ **homogênea** (transitiva por automorfismos),
com diagrama de Hasse de **valência finita**, cujo espaço de ciclos sobre
$\mathbb{Z}$ é gerado por ciclos **rank-frustrados** (pentágonos, $\varphi=\pm1$)
e **percola** (nº de ciclos independentes em bola de raio $R$ cresce ≥ ordem
$R^2$; não confinado à la T4). T1 não a governa (geradores não-balanceados);
T2/T3/T4 não a governam (não é exchangeable, não é growth-model, não é
sprinkling embutido). A questão é se a interseção é habitada.

## 2. DECLARAÇÃO DE NÃO-CEGUEIRA (honestidade estrutural)

Durante o scoping analítico DESTA campanha (antes deste documento, sem código),
**três candidatos a contraexemplo foram encontrados no papel**. Este
pré-registro portanto NÃO é cego quanto à direção do desfecho — ele congela o
**protocolo de verificação**: a kill-list K1–K7 que cada candidato deve passar
integralmente, e o gate computacional G (certificados finitos), ANTES de rodar
qualquer código. Cada item da kill-list é uma morte possível da construção; se
todos os candidatos morrerem, a conjectura-forte volta a aberta e isso será
registrado como tal.

## 3. Os candidatos (congelados)

**E1 (cristal abeliano, crescimento polinomial).** $P=\mathbb{Z}^2$; geradores
$V=\{v_1{=}(3,0),\,v_2{=}(0,3),\,v_3{=}(1,1),\,v_4{=}(3,1),\,v_5{=}(1,3)\}$;
ordem $u\preceq w \iff w-u\in\mathbb{N}\text{-span}(V)$; Hasse candidato = grafo
de Cayley não-dirigido com arestas $V$. Relação pentagonal:
$v_1+v_2+v_3=v_4+v_5=(4,4)$, $\varphi=+1$. Funcional-peso $h(x,y)=x+y$
(valores $3,3,2,4,4$ nos geradores).

**E2 (one-relator, pentágonos puros com arestas compartilhadas).**
$\Gamma_3=\langle a,b,c \mid a\,b\,a\,c^{-1}b^{-1}\rangle$ (i.e. $aba=bc$);
ordem $g\preceq g w$ para $w$ palavra positiva; pesos $h=(1,1,2)$.

**E3 (one-relator, pentágonos puros, girth 5, 5 geradores).**
$\Gamma_5=\langle a,b,c,d,e \mid a\,b\,c\,d^{-1}e^{-1}\rangle$ (i.e. $abc=ed$);
pesos $h=(2,2,2,3,3)$.

## 4. Kill-list (cada item mata o candidato se falhar)

| # | Exigência | Instrumento |
|---|---|---|
| K1 | Ordem parcial genuína: aciclicidade + antissimetria | $h$ homomorfismo com $h>0$ nos geradores (prova); E1 também exaustivo no gate |
| K2 | Localmente finita (intervalos $[u,v]$ finitos) = axioma de causal set | contagem por peso (prova); E1 exaustivo |
| K3 | Coberturas = exatamente as arestas de Cayley (Hasse = Cayley) | argumento de peso + verificação direta dos casos-limite; E1 exaustivo em bola |
| K4 | Valência finita e transitividade por vértices | multiplicação à esquerda; distinção dos geradores (abelianização / Freiheitssatz / quociente finito) |
| K5 | Pentágono = 5-ciclo EMBUTIDO do grafo de Hasse com $\varphi=\pm1$ | pesos distintos dos 5 vértices; certificado em quociente |
| K6 | NÃO-graduada (nenhum $r$ com $r(y)=r(x)+1$ em toda cobertura) | relação desbalanceada 3≠2 (prova exata) |
| K7 | Espaço de ciclos gerado por ciclos locais incluindo frustrados ($\varphi$-imagem $\neq 0$) e percolante: rank de ciclos em bola ~ $\geq R^2$ (E1: expoente do fit em $[1.7,2.3]$ na janela $R\in[4,12]$) | teorema do complexo de apresentação (prova); E1 medição no gate |
| K8 | (escopo, não mata) Delimitação: a construção não toca o teorema invariante — camada 1 (Campbell–Mecke sobre ensembles invariantes) e BHS (nenhum cristal é Lorentz-invariante) permanecem aplicáveis | analítico, seção própria do RESULTADO |

**Extra E3:** girth = 5 (nenhum 3-/4-ciclo) ⇒ espaço de ciclos gerado por
pentágonos SOMENTE. **Extra E2:** cada aresta-$a$ pertence a 2 pentágonos
(plaquetas compartilham arestas — responde à objeção "cacto" de E3, onde cada
aresta está em exatamente 1 pentágono).

## 5. Gate computacional G (declarado antes de rodar)

`gate_m1b.py`, saída `gate_m1b.json`:

- **G-E1 (exaustivo, aritmética inteira exata):** bola de peso $h\le 24$:
  (a) cone pontiagudo (nenhuma combinação ℕ não-trivial = 0); (b) elementos
  mínimos do cone = exatamente $V$ (coberturas de 0); (c) nenhum $v_i$ é
  soma-ℕ dos demais; (d) pentágono: 5 vértices distintos, 5 arestas todas
  coberturas; (e) sistema $\lambda\cdot v_i=1$ ($i=1..5$) inconsistente sobre
  $\mathbb{Q}$; (f) rank do espaço de ciclos $E-V+1$ em bolas de raio-grafo
  $R=4..12$: expoente de fit $\in[1.7,2.3]$.
- **G-E2/E3 (certificados por quociente):** quocientes de permutação
  ($S_n$, $n\le 10$, ≤ 5000 tentativas): relação resolvida explicitamente
  ($c:=b^{-1}aba$ em E2; $e:=abcd^{-1}$ em E3 — todo sorteio É um quociente).
  Certificar: geradores 2-a-2 distintos; todos os $w$ reduzidos $1\le|w|\le4$
  têm imagem $\neq 1$ em algum quociente (⇒ girth ≥ 5); vértices do pentágono
  distintos. **Lógica do certificado:** quociente separa ⇒ desigualdade PROVADA
  em $\Gamma$; quociente que não separa não prova nada (igualdade só por
  derivação analítica). VERDE = todos certificados; AMARELO = item coberto só
  pela prova analítica (Freiheitssatz/Magnus, citada); VERMELHO = derivação
  analítica de uma igualdade proibida (mata o candidato).

## 6. Desfechos pré-declarados

- **K1–K7 passam para ≥ 1 candidato** ⇒ conjectura-forte de M1 §6(b)
  ("frustração percolante e valência finita competem") **MORRE**; flanco
  pentagonal = **CONSTRUTÍVEL** (a "morte 2/descoberta maior" antecipada em
  M1). Consequências vão ao RESULTADO com K8 obrigatório (delimitação física:
  o que isso NÃO quebra), e os deltas de paper ficam para a REVISÃO dos
  submetidos — nenhum PDF submetido é tocado agora.
- **Todos os candidatos morrem em algum Ki** ⇒ registrar as mortes, a fresta
  continua aberta, e o lado "provar impossibilidade" herda os mecanismos das
  mortes como lemas candidatos.
- Proibido: afrouxar K7 (percolação) ou redefinir "homogêneo" pós-dado.

## 7. O que esta campanha NÃO reivindica

Nada sobre substratos Lorentz-invariantes (o teorema físico da camada 1 não
está em teste); nada sobre dinâmica (se string-net CONDENSA sobre o cristal é
campanha futura); nenhuma reivindicação de novidade matemática profunda — o
valor é o fechamento do alvo nomeado do programa e a delimitação.
