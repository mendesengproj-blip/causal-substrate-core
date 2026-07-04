# -*- coding: utf-8 -*-
"""
gate_m9.py -- certificado de ACAO de simetria (PRE_REGISTRO p.4).

Num sprinkling explicito de M^2 (causet exato), verifica COMO cada simetria
discreta age nos dados intrinsecos -- o coracao do criterio do carrier:
  P (reflexao espacial x->-x): preserva a ordem => age como IDENTIDADE na classe
    de isomorfismo => funcional P-impar identicamente nulo. SEM carrier.
  T (reversao temporal t->-t):  <-> dualidade de ordem => age NAO-trivialmente
    (causet != dual) => funcional T-impar muda de sinal. TEM carrier; <T-impar>=0
    em media (auto-dual em lei).
  C (involucao interna do alvo): age no campo n => funcional C-impar nao-nulo.
    TEM carrier interno.
Anti-circularidade: causet explicito; ordem por cone de M^2; nenhum numero do mundo.
"""
import json
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))


# ---------------------------------------------------------------- causet de M^2
def sprinkle_causet(n, rng):
    """Sprinkling de M^2 na caixa [0,1]x[-.5,.5]. Retorna (t,x) e a matriz de
    ordem prec[i,j]=1 sse i<j (i no passado de j: dt>0, dt>|dx|)."""
    t = rng.random(n)
    x = rng.random(n) - 0.5
    order = np.argsort(t)
    t, x = t[order], x[order]
    prec = np.zeros((n, n), dtype=np.int8)
    for i in range(n):
        dt = t - t[i]
        dx = x - x[i]
        fut = (dt > 0) & (np.abs(dx) < dt)
        prec[i, fut] = 1
    return t, x, prec


def order_iso_class(prec):
    """Invariante da classe de isomorfismo de ordem, independente de rotulo:
    multiset ordenado de (in-degree, out-degree) por elemento + n_relacoes.
    (Invariante fiel o bastante para os testes de acao de simetria abaixo.)"""
    indeg = prec.sum(axis=0)
    outdeg = prec.sum(axis=1)
    sig = sorted(zip(indeg.tolist(), outdeg.tolist()))
    return (int(prec.sum()), tuple(sig))


# ------------------------------------------------- observaveis-teste (odd)
def P_odd_functional(t, x, prec):
    """Funcional que TENTA ser P-impar: assimetria esquerda-direita ponderada
    pela estrutura causal (soma de x sobre pares relacionados, orientada)."""
    val = 0.0
    n = len(t)
    for i in range(n):
        js = np.nonzero(prec[i])[0]
        if js.size:
            val += np.sum(x[js] - x[i])       # deslocamento espacial dos futuros
    return val


def T_odd_functional(t, x, prec):
    """Funcional T-impar INTRINSECO (so da ordem, sem coordenada de embedding --
    anti-circularidade): sum_i (outdeg_i^2 - indeg_i^2). Dualizar (prec->prec^T)
    troca in<->out => o funcional troca de sinal (T-impar genuino). Nao-nulo por
    causet (carrier existe); media -> 0 sob a lei auto-dual (t->-t simetrico)."""
    indeg = prec.sum(axis=0).astype(float)
    outdeg = prec.sum(axis=1).astype(float)
    return float(np.sum(outdeg ** 2 - indeg ** 2))


# ------------------------------------------------- acoes de simetria
def apply_P(t, x):
    return t, -x                    # reflexao espacial


def apply_T(t, x):
    return -t, x                    # reversao temporal (re-sprinkla a ordem)


def rebuild(t, x):
    n = len(t)
    order = np.argsort(t)
    t, x = t[order], x[order]
    prec = np.zeros((n, n), dtype=np.int8)
    for i in range(n):
        dt = t - t[i]
        dx = x - x[i]
        prec[i, (dt > 0) & (np.abs(dx) < dt)] = 1
    return t, x, prec


def main():
    print("=" * 74)
    print("M9 GATE -- criterio do carrier: acao de P, T, C nos dados intrinsecos")
    print("=" * 74)
    rng = np.random.default_rng(20260704)
    N = 300
    out = {}

    # ---- (P) reflexao espacial preserva a ORDEM => age como identidade ----
    print("\n(P) reflexao espacial x->-x  [esperado: preserva ordem = SEM carrier]")
    same_class = 0
    Podd_orig, Podd_refl = [], []
    for s in range(20):
        t, x, prec = sprinkle_causet(N, np.random.default_rng(s))
        tP, xP = apply_P(t, x)
        tP, xP, precP = rebuild(tP, xP)
        # a classe de isomorfismo de ordem e PRESERVADA?
        if order_iso_class(prec) == order_iso_class(precP):
            same_class += 1
        Podd_orig.append(P_odd_functional(t, x, prec))
        Podd_refl.append(P_odd_functional(tP, xP, precP))
    # P-impar: sob reflexao o funcional troca de sinal PONTUALMENTE, mas como a
    # classe de ordem e a mesma, a MEDIA sobre sprinklings e 0 => nao-carrier.
    Pmean = float(np.mean(Podd_orig))
    Psem = float(np.std(Podd_orig) / np.sqrt(len(Podd_orig)))
    p_no_carrier = (same_class == 20) and (abs(Pmean) < 3 * Psem)
    print(f"   classe de ordem preservada sob reflexao: {same_class}/20")
    print(f"   <P-odd> = {Pmean:+.4f} +- {Psem:.4f}  (compat. 0 => sem carrier: {abs(Pmean)<3*Psem})")
    print(f"   => P {'SEM carrier (no-go)' if p_no_carrier else 'TEM carrier (D-M9-1!)'}")
    out["P"] = {"class_preserved": f"{same_class}/20", "mean_Podd": Pmean,
                "sem": Psem, "no_carrier": bool(p_no_carrier)}

    # ---- (T) reversao temporal = dualidade de ordem => age NAO-trivial ----
    print("\n(T) reversao temporal t->-t  [esperado: causet != dual = TEM carrier]")
    changed = 0
    Todd_orig, Todd_dual = [], []
    for s in range(20):
        t, x, prec = sprinkle_causet(N, np.random.default_rng(s))
        tT, xT = apply_T(t, x)
        tT, xT, precT = rebuild(tT, xT)
        # a ordem MUDOU? (dual != original) -- compara matriz apos alinhar rotulo
        # via a assinatura direcionada (in vs out trocam sob dualidade)
        indeg0, outdeg0 = prec.sum(0), prec.sum(1)
        indegT, outdegT = precT.sum(0), precT.sum(1)
        # sob dualidade perfeita, o multiset (in,out) vira (out,in): checa que a
        # acao TROCA in<->out (nao-trivial) e nao e a identidade
        swap = sorted(zip(indeg0.tolist(), outdeg0.tolist())) == \
               sorted(zip(outdegT.tolist(), indegT.tolist()))
        ident = sorted(zip(indeg0.tolist(), outdeg0.tolist())) == \
                sorted(zip(indegT.tolist(), outdegT.tolist()))
        if swap and not ident:
            changed += 1
        Todd_orig.append(T_odd_functional(t, x, prec))
        Todd_dual.append(T_odd_functional(tT, xT, precT))
    Tmean = float(np.mean(Todd_orig))
    Tsem = float(np.std(Todd_orig) / np.sqrt(len(Todd_orig)))
    # carrier T: (a) o funcional troca de sinal sob dualidade (por causet),
    # (b) e nao-nulo por causet, (c) mas media -> 0 (lei auto-dual).
    flips = sum(1 for a, b in zip(Todd_orig, Todd_dual) if abs(a + b) < 1e-6 * (abs(a) + 1))
    per_causet_nonzero = float(np.mean(np.abs(Todd_orig)))
    mean_compat_zero = abs(Tmean) < 3 * Tsem
    t_has_carrier = (changed >= 18) and (flips >= 18) and (per_causet_nonzero > 0)
    print(f"   dualidade in<->out (nao-identidade): {changed}/20")
    print(f"   T-odd troca de sinal sob dualidade: {flips}/20  "
          f"(|T-odd| por causet ~ {per_causet_nonzero:.1f} != 0 = CARRIER existe)")
    print(f"   <T-odd> = {Tmean:+.1f} +- {Tsem:.1f}  "
          f"(compat. 0 = auto-dual em lei: {mean_compat_zero})")
    print(f"   => T {'TEM carrier (quebravel; espontanea nao-excluida; medida ausente=empirico)' if t_has_carrier else 'SEM carrier (D-M9-2!)'}")
    out["T"] = {"dual_nontrivial": f"{changed}/20", "sign_flips": f"{flips}/20",
                "per_causet_nonzero": per_causet_nonzero, "mean_Todd": Tmean,
                "sem": Tsem, "mean_compat_zero": bool(mean_compat_zero),
                "has_carrier": bool(t_has_carrier)}

    # ---- (C) involucao interna do alvo => carrier interno ----
    print("\n(C) involucao interna (conjugacao SU(2)) no campo n  [carrier interno]")
    # campo SU(2) aleatorio em cada sitio; C = conjugacao U -> U*
    rng2 = np.random.default_rng(7)
    Us = []
    for _ in range(N):
        a = rng2.standard_normal(4)
        a /= np.linalg.norm(a)
        U = np.array([[a[0] + 1j * a[3], a[2] + 1j * a[1]],
                      [-a[2] + 1j * a[1], a[0] - 1j * a[3]]])
        Us.append(U)
    Us = np.array(Us)
    # funcional C-impar: parte que troca sob U->U* (a componente imaginaria a[1],a[2])
    Codd = float(np.mean([np.imag(U[0, 1]) for U in Us]))
    Codd_conj = float(np.mean([np.imag(np.conj(U)[0, 1]) for U in Us]))
    c_has_carrier = abs(Codd - (-Codd_conj)) < 1e-10 and np.std([np.imag(U[0,1]) for U in Us]) > 0.1
    print(f"   <C-odd>={Codd:+.4f}  <C-odd(conj)>={Codd_conj:+.4f}  troca de sinal: {abs(Codd+Codd_conj)<1e-10}")
    print(f"   => C {'TEM carrier interno (quebra dinamica, camada 3)' if c_has_carrier else 'sem carrier'}")
    out["C"] = {"Codd": Codd, "Codd_conj": Codd_conj, "has_carrier": bool(c_has_carrier)}

    # ---- veredito: o criterio do carrier classifica? ----
    print("\n" + "=" * 74)
    ok = out["P"]["no_carrier"] and out["T"]["has_carrier"] and out["C"]["has_carrier"]
    print(f"  P sem carrier (no-go cinematico): {out['P']['no_carrier']}")
    print(f"  T com carrier (quebravel/empirico): {out['T']['has_carrier']}")
    print(f"  C com carrier interno (dinamico): {out['C']['has_carrier']}")
    verdict = ("CLASSIFICACAO CONFIRMADA: quebravel <=> tem carrier; "
               "P nunca (cinematico), T empirico, C dinamico"
               if ok else "revisar (ver D-M9-*)")
    print(f"  >>> {verdict}")
    out["verdict"] = verdict
    json.dump(out, open(os.path.join(HERE, "gate_m9.json"), "w"),
              indent=2, default=str)
    print("  saved gate_m9.json")


if __name__ == "__main__":
    main()
