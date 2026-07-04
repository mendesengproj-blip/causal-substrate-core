# FS2D_SYNTHESIS — sonda barata da semente em 2D (indicador antecipado)

> Pré-registro: `../SEMENTE_PRE_REGISTRO.md` + ADENDO FS-2D (critérios congelados ANTES de
> rodar). Código `fs_seed2d.py`, dados `fs2d_result.json`. **Data:** 2026-06-28.
> **Estatuto (não esquecer):** EXPLORATÓRIO. NÃO é o teste de morte D1/D2 (esses são 3D).

## Veredito de uma linha
**FS-2D = POSITIVO** pelo critério congelado: O1(d_H), O2(clumping) e O3(PR) **todos se movem**
clara e monotonicamente com γ, muito além do erro por blocking. ⇒ pela regra assimétrica
pré-registrada, **dispara FS-3D** e **eleva o prior** da semente. **Mas o positivo é D1-apenas,
e tem cara de patologia em γ grande — leitura honesta abaixo.**

## Números (γ=0 = CDT cega, controle)
| γ | d_H (band) | O2 clumping R=Var(ℓ)/⟨ℓ⟩² | O3 PR (baixo=concentrado) |
|---|---|---|---|
| 0.0 | 2.116 | 0.188 ± 0.030 | 0.926 ± 0.001 |
| 1.0 | 1.785 | 2.610 ± 0.260 | 0.620 ± 0.005 |
| 2.0 | 1.462 | 5.142 ± 0.533 | 0.671 ± 0.004 |
| 4.0 | 1.111 | 20.39 ± 0.486 | 0.760 ± 0.001 |

- **Controle OK:** γ=0 reproduz a CDT cega de F1 (d_H≈2.1, R≈0.19). A semente desligada = F1.
- **A informação demonstravelmente reformata a geometria:** clumping ×100 (0.19→20), d_H
  desaba de 2.1 para ~1.1 (geometria vira **filamento** — o crescimento concentra numa
  sub-região onde a informação se acumulou).

## As 3 ressalvas (a leitura honesta, simétrica ao resto do programa)

1. **É D1-apenas, NÃO D2.** O positivo prova que a informação **não é decoração** (D1: geometria
   ≠ CDT cega — robusto). Mas **não** prova que a semente é mais que uma **regra de crescimento
   com feedback positivo genérico**. Qualquer feedback "cresce-onde-já-cresceu" colapsa em
   clumping — e é exatamente isso que **D2** (vs regra geométrica markoviana, assinatura =
   memória não-markoviana C_mem) existe para discriminar. **D2 NÃO foi testado aqui.** O positivo
   D1 é necessário, não suficiente. A novidade da semente continua **não estabelecida**.

2. **Em γ grande, parece PATOLOGIA, não riqueza.** d_H→1 com R≈20 (uma fatia detém quase todo o
   volume) é **colapso** geométrico (filamento degenerado), não formação de estrutura rica — o
   análogo "branched-polymer" do feedback forte. O regime potencialmente físico é o
   **intermediário** (γ≈1: d_H≈1.8, R≈2.6 — geometria *modificada mas estendida*). Declarar:
   a semente forte **destrói** a geometria 2D; não a enriquece.

3. **2D é rígido e a sonda é fraca por construção (prior §4).** Que a semente consiga mover d_H
   **mesmo** em 2D (onde a folheação fixa d_H=2 na CDT cega) é o que torna o positivo digno de
   nota. Mas o teste vinculante exige 3D (geometria com liberdade) + D2 (memória). Um positivo
   2D **eleva o prior**; não fecha nada.

## O que isto muda (e o que não muda)
- **Muda:** remove a hipótese mais barata de morte da semente ("é decoração, não toca a
  geometria") — refutada. A semente **tem** efeito estrutural. Justifica gastar em FS-3D.
- **Não muda:** o veredito de novidade. A semente ainda pode morrer em **D2** (o efeito é
  replicável por um peso geométrico sem memória) — e o colapso d_H→1 sugere que o efeito 2D
  pode ser **só** feedback genérico, não a memória-informação específica. O prior §4 (morte
  provável em D2) **permanece**.

## ATUALIZAÇÃO (2026-06-28, Tarefa 2) — o positivo é REBAIXADO: colapso é genérico

Controle pré-registrado (`task2_generic_control.py`): varredura γ×κ, κ=0 = campo genérico sem
transporte (o ingrediente distintivo da semente removido). **Em κ=0, d_H já desaba 2.07→1.60 e
clumping ×11** — feedback positivo genérico **sozinho** produz o colapso ⇒ é a barreira
**c=1/branched-polymer**, não a semente. O transporte κ só **aprofunda** (1.60→1.00 em γ=4),
plausivelmente reescalonamento do acoplamento efetivo. **Conclusão honesta:** o "positivo" da
ressalva 1 acima é **substancialmente não-específico à semente**. A evidência pró-semente
**não pode se apoiar no FS-2D/D1** — depende **inteiramente de D2 (memória/C_mem) em 3D**.
(Detalhe e a falha de desenho do critério binário em `../SEMENTE_PRE_REGISTRO.md`, RESULTADO
TAREFA-2.) Isto **reforça** a ressalva 1 original e o prior §4 de morte provável em D2.

## Próximo (registrado)
FS-3D (sobre a geometria de F1b/3D, Nível A): rodar D1 **e D2** com o controle de regra
geométrica markoviana + medir C_mem(τ). Só lá a pergunta "informação ≠ peso de crescimento"
recebe resposta. Bloqueio: precisa de F1b (motor 3D) primeiro.
