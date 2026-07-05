# -*- coding: utf-8 -*-
"""
n6_module_a.py -- Modulo A (analitico): medida quantal de POSTS na percolacao
transitiva COMPLEXA (PRE_REGISTRO par.7).

Base (A3/A4 conferidas): posts sao eventos-tronco covariantes; o nº esperado de
posts em ordem de grafo aleatorio finita tem expressao (Bombelli-Seggev-Watson
0809.2258, citando ABBJ). Formula por elemento (fechamento passado x futuro,
INDEPENDENTES por construcao da TP):
    P(k-esimo e post em n) = prod_{m=1}^{k-1}(1-q^m) * prod_{m=1}^{n-k}(1-q^m),
q = 1-p. MINI-GATE: verificar ESTA formula contra Monte Carlo (rs_trigger +
post_stats de gate_m1c) ANTES de complexificar. Se falhar, PARAR.

COMPLEXIFICACAO (o passo novo, declarado): na TP cada elemento novo liga-se a
cada anterior independentemente; amplitudes a (liga) e 1-a (nao liga) somam 1
p/ QUALQUER a em C => a medida complexa e automaticamente normalizada. A
amplitude do evento 'k e post' e a MESMA soma combinatoria da probabilidade
classica com p->a: alpha_k(a) = formula com q=1-a. Medida quantal (prescricao
declarada: medida vetorial p/ eventos de estagio finito): mu_k = |alpha_k|^2.
Diagnostico: Sigma_k mu_k(theta)/Sigma_k mu_k(0) com a = p e^{i theta} --
interferencia SUPRIME (alimenta D1) ou PRESERVA (eco quantico do T4, D2)?
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "M1C_FRONTEIRA_NAO_POISSON"))
sys.path.insert(0, os.path.join(HERE, "..", "..", "TEIC", "docs", "campaigns",
                                "RIDEOUT_SORKIN_TRIGGER"))
import rs_trigger as rs
import gate_m1c as gm


def post_prob_formula(n, q):
    """E[#posts](n) = sum_k prod_{m=1}^{k-1}(1-q^m) prod_{m=1}^{n-k}(1-q^m).
    Vale p/ q real OU complexo (retorna soma dos produtos; p/ complexo o
    chamador usa alpha_k individualmente)."""
    # prefix[t] = prod_{m=1}^{t} (1-q^m), t=0..n-1
    pref = np.ones(n, dtype=complex)
    acc = 1.0 + 0.0j
    qq = q
    for t in range(1, n):
        acc *= (1.0 - qq)
        pref[t] = acc
        qq *= q
    alphas = np.array([pref[k - 1] * pref[n - k] for k in range(1, n + 1)])
    return alphas


def mini_gate(n=100, ps=(0.5, 0.7), seeds=300):
    print(f"[mini-gate] formula de posts vs Monte Carlo (rs_trigger), n={n}")
    ok_all = True
    rows = []
    for p in ps:
        q = 1.0 - p
        exp_formula = float(np.sum(post_prob_formula(n, q).real))
        counts = []
        for s in range(seeds):
            anc, _ = rs.grow_transitive_percolation(
                n, p, np.random.default_rng(9000 + s))
            counts.append(gm.post_stats(anc, n)["n_post"])
        mc = float(np.mean(counts))
        sem = float(np.std(counts) / np.sqrt(seeds))
        ok = abs(mc - exp_formula) <= 3 * max(sem, 1e-9)
        ok_all = ok_all and ok
        print(f"   p={p}: formula={exp_formula:.3f}  MC={mc:.3f}+-{sem:.3f}"
              f"  -> {'OK' if ok else 'FALHA'}")
        rows.append({"p": p, "formula": exp_formula, "mc": mc, "sem": sem,
                     "ok": bool(ok)})
    return ok_all, rows


def log_mu_posts(n, q):
    """log Sigma_k |alpha_k|^2 em LOG-espaco (sem overflow). alpha_k =
    prod_{m=1}^{k-1}(1-q^m) prod_{m=1}^{n-k}(1-q^m)."""
    logs = np.zeros(n)          # log|prefix_t|, t=0..n-1
    acc = 0.0
    qq = q
    for t in range(1, n):
        acc += np.log(max(abs(1.0 - qq), 1e-300))
        logs[t] = acc
        qq *= q
    la = np.array([logs[k - 1] + logs[n - k] for k in range(1, n + 1)])
    m = la.max()
    return float(2 * m + np.log(np.sum(np.exp(2 * (la - m)))))


def complex_sweep(n=100, p=0.5, thetas=None):
    """mu(theta)/mu(0) via log-espaco. DOMINIO declarado: |q|=|1-a|<1 e a
    regiao de normalizabilidade das amplitudes-tronco (|q|>=1 => produtos
    divergem com n; marcado fora-do-dominio, nao e supressao/reforco)."""
    if thetas is None:
        thetas = np.linspace(0.0, np.pi / 2, 19)
    log_mu0 = None
    rows = []
    for th in thetas:
        a = p * np.exp(1j * th)
        q = 1.0 - a
        in_dom = abs(q) < 1.0
        lm = log_mu_posts(n, q)
        if log_mu0 is None:
            log_mu0 = lm
        rows.append({"theta": float(th), "abs_q": float(abs(q)),
                     "in_domain": bool(in_dom),
                     "log_ratio": float(lm - log_mu0),
                     "ratio": float(np.exp(min(lm - log_mu0, 700.0)))})
    return rows


def main():
    out = {}
    print("=" * 74)
    print("N6 MODULO A -- medida quantal de posts na TP complexa")
    print("=" * 74)
    ok, rows = mini_gate()
    out["mini_gate"] = {"ok": bool(ok), "rows": rows}
    if not ok:
        print("MINI-GATE FALHOU -- formula nao validada; modulo PARA aqui.")
        json.dump(out, open(os.path.join(HERE, "n6_module_a.json"), "w"), indent=2)
        return

    print("\n[sweep] a = p e^{i theta}, p=0.5, n=100 (log-espaco; dominio |q|<1):")
    rows = complex_sweep()
    out["sweep_p0.5_n100"] = rows
    for r in rows[::3]:
        tag = "" if r["in_domain"] else "  [FORA DO DOMINIO |q|>=1]"
        print(f"   theta={r['theta']:.3f}: |q|={r['abs_q']:.3f} "
              f"log(mu/mu0)={r['log_ratio']:+8.3f}{tag}")
    # robustez: p=0.7 e n=200
    out["sweep_p0.7_n100"] = complex_sweep(p=0.7)
    out["sweep_p0.5_n200"] = complex_sweep(n=200)

    # classificacao pre-declarada (par.7): suprime ou preserva/reforca?
    dom = [r for r in rows if r["in_domain"]]
    supp = all(dom[i]["log_ratio"] >= dom[i + 1]["log_ratio"] - 1e-12
               for i in range(len(dom) - 1)) and dom[-1]["log_ratio"] < np.log(0.5)
    if supp:
        verdict = ("SUPRIME: interferencia mata posts no dominio "
                   "(alimenta D1 -- fuga do confinamento-por-blocos possivel)")
    elif dom[-1]["log_ratio"] >= 0:
        verdict = ("REFORCA: mu_quantal(posts) >= classica em TODO o dominio "
                   "|q|<1 (cresce monotonicamente com theta e diverge na borda "
                   "de normalizabilidade) -- eco quantico FORTE do mecanismo "
                   "T4; nenhum indicio de fuga por supressao de posts "
                   "(alimenta D2)")
    else:
        verdict = "MISTO: reportar curva sem classificacao binaria"
    print(f"\n   log-ratio no fim do dominio: {dom[-1]['log_ratio']:+.3f} "
          f"(theta={dom[-1]['theta']:.3f}, |q|={dom[-1]['abs_q']:.3f})")
    print(f"   >>> {verdict}")
    out["verdict"] = verdict
    json.dump(out, open(os.path.join(HERE, "n6_module_a.json"), "w"), indent=2)
    print("   saved n6_module_a.json")


if __name__ == "__main__":
    main()
