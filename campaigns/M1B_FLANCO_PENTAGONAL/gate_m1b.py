# -*- coding: utf-8 -*-
"""
M1b — gate de certificados finitos (declarado no PRE_REGISTRO.md par.5 ANTES de rodar).

G-E1: Z^2, geradores V={(3,0),(0,3),(1,1),(3,1),(1,3)} — verificacao EXAUSTIVA
      em bola de peso h<=24 (aritmetica inteira exata) + rank de ciclos em bolas.
G-E2: Gamma_3 = <a,b,c | aba = bc>   — certificados por quociente de permutacao.
G-E3: Gamma_5 = <a,b,c,d,e | abc = ed> — idem.

Logica do certificado (par.5): imagem != 1 num quociente finito PROVA a
desigualdade no grupo; nao-separacao nao prova nada.
"""
import itertools, json, math, random, sys
from collections import deque

OUT = {}

# ---------------------------------------------------------------- G-E1 (Z^2)
V1 = [(3, 0), (0, 3), (1, 1), (3, 1), (1, 3)]
H_MAX = 24

def h(p):
    return p[0] + p[1]

def e1_gate():
    res = {}
    # (a) cone pontiagudo: h>0 em todos os geradores => combinacao N nao-trivial tem h>0
    res["a_pointed"] = all(h(v) > 0 for v in V1)

    # conjunto do cone ate h<=H_MAX (BFS exato)
    cone = {(0, 0)}
    frontier = deque([(0, 0)])
    while frontier:
        x = frontier.popleft()
        for v in V1:
            y = (x[0] + v[0], x[1] + v[1])
            if h(y) <= H_MAX and y not in cone:
                cone.add(y)
                frontier.append(y)
    conenz = cone - {(0, 0)}

    # (b) elementos minimais do cone (=coberturas de 0) == exatamente V1
    def in_cone_nz(p):
        return p in conenz
    minimals = set()
    for x in conenz:
        strictly_below = False
        for y in conenz:
            if y != x:
                d = (x[0] - y[0], x[1] - y[1])
                if d != (0, 0) and in_cone_nz(d):
                    strictly_below = True
                    break
        if not strictly_below:
            minimals.add(x)
    res["b_minimals_eq_generators"] = (minimals == set(V1))
    res["b_minimals_found"] = sorted(minimals)

    # (c) nenhum gerador e soma-N dos demais (redundante com (b); explicito)
    ok_c = True
    for i, v in enumerate(V1):
        others = [u for j, u in enumerate(V1) if j != i]
        sub = {(0, 0)}
        fr = deque([(0, 0)])
        while fr:
            x = fr.popleft()
            for u in others:
                y = (x[0] + u[0], x[1] + u[1])
                if h(y) <= h(v) and y not in sub:
                    sub.add(y)
                    fr.append(y)
        if v in sub:
            ok_c = False
    res["c_generators_irreducible"] = ok_c

    # (d) pentagono embutido feito de coberturas; phi = +1
    P = [(0, 0), (3, 0), (3, 3), (4, 4), (3, 1)]
    res["d_pentagon_vertices_distinct"] = (len(set(P)) == 5)
    edges = [((0, 0), (3, 0)), ((3, 0), (3, 3)), ((3, 3), (4, 4)),
             ((3, 1), (4, 4)), ((0, 0), (3, 1))]  # 3 subidas + 2 descidas na volta
    ok_d = True
    for (u, w) in edges:
        d = (w[0] - u[0], w[1] - u[1])
        if d not in set(V1) or d not in minimals:
            ok_d = False
    res["d_pentagon_edges_are_covers"] = ok_d
    res["d_phi"] = 3 - 2

    # (e) sem graduacao unitaria: lambda.v=1 para os 5 geradores e inconsistente (exato)
    # v1: 3*l1=1 -> l1=1/3 ; v2: 3*l2=1 -> l2=1/3 ; v3 exige l1+l2=1 -> 2/3=1 falso.
    from fractions import Fraction
    l1 = Fraction(1, 3); l2 = Fraction(1, 3)
    res["e_no_unit_grading"] = (l1 * 1 + l2 * 1 != 1)

    # (e') os geradores geram Z^2 (grafo de Cayley conexo)
    zspan_has_units = ((1, 0) == (V1[3][0] - V1[2][0] - (V1[0][0] - (V1[3][0] - V1[2][0])), 0)) # ilustrativo
    # verificacao honesta: (2,0)=v4-v3; (1,0)=v1-(2,0); (0,1)=v3-(1,0)
    p20 = (V1[3][0] - V1[2][0], V1[3][1] - V1[2][1])          # (2,0)
    p10 = (V1[0][0] - p20[0], V1[0][1] - p20[1])              # (1,0)
    p01 = (V1[2][0] - p10[0], V1[2][1] - p10[1])              # (0,1)
    res["e2_generates_Z2"] = (p20 == (2, 0) and p10 == (1, 0) and p01 == (0, 1))

    # (f) rank do espaco de ciclos em bolas de raio-grafo R=4..12 ~ R^2
    moves = V1 + [(-v[0], -v[1]) for v in V1]
    dist = {(0, 0): 0}
    q = deque([(0, 0)])
    R_MAX = 12
    while q:
        x = q.popleft()
        if dist[x] == R_MAX:
            continue
        for m in moves:
            y = (x[0] + m[0], x[1] + m[1])
            if y not in dist:
                dist[y] = dist[x] + 1
                q.append(y)
    ranks = {}
    for R in range(4, R_MAX + 1):
        ball = {p for p, d in dist.items() if d <= R}
        E = 0
        for p in ball:
            for v in V1:
                w = (p[0] + v[0], p[1] + v[1])
                if w in ball:
                    E += 1
        Vn = len(ball)
        ranks[R] = E - Vn + 1  # bola conexa
    xs = [math.log(R) for R in ranks]
    ys = [math.log(r) for r in ranks.values()]
    n = len(xs)
    sx, sy = sum(xs), sum(ys)
    sxx = sum(x * x for x in xs)
    sxy = sum(x * y for x, y in zip(xs, ys))
    slope = (n * sxy - sx * sy) / (n * sxx - sx * sx)
    res["f_cycle_rank_by_R"] = ranks
    res["f_fit_exponent"] = round(slope, 3)
    res["f_exponent_in_window"] = (1.7 <= slope <= 2.3)

    res["PASS"] = all([res["a_pointed"], res["b_minimals_eq_generators"],
                       res["c_generators_irreducible"],
                       res["d_pentagon_vertices_distinct"],
                       res["d_pentagon_edges_are_covers"],
                       res["e_no_unit_grading"], res["e2_generates_Z2"],
                       res["f_exponent_in_window"]])
    return res

# --------------------------------------------- quocientes de permutacao (E2/E3)
N_PERM = 8
MAX_TRIALS = 5000
SEED = 20260704

def pmul(p, q):  # (p o q)[i] = p[q[i]]
    return tuple(p[q[i]] for i in range(len(q)))

def pinv(p):
    r = [0] * len(p)
    for i, v in enumerate(p):
        r[v] = i
    return tuple(r)

def pid(n):
    return tuple(range(n))

def reduced_words(letters, max_len):
    """palavras livremente reduzidas ate max_len; letters = lista de simbolos;
    inverso de s e s.swapcase()."""
    words = []
    def rec(w):
        if 0 < len(w) <= max_len:
            words.append("".join(w))
        if len(w) == max_len:
            return
        for s in letters:
            if w and w[-1] == s.swapcase():
                continue
            rec(w + [s])
    rec([])
    return words

def cyclically_reduced(w):
    return not (len(w) >= 2 and w[0] == w[-1].swapcase())

def eval_word(w, gens):
    n = len(next(iter(gens.values())))
    acc = pid(n)
    for s in w:
        g = gens[s.lower()]
        acc = pmul(acc, g if s.islower() else pinv(g))
    return acc

def quotient_gate(name, base_letters, solve_dependent, relation_check,
                  pentagon_vertex_words):
    """base_letters: geradores livres sorteados; solve_dependent(dict)->dict
    completa o(s) gerador(es) dependente(s). Certifica: palavras ciclicamente
    reduzidas |w|<=4 != 1 (girth>=5, cobre distincao de geradores e casos de
    cobertura) + vertices do pentagono distintos."""
    rng = random.Random(SEED)
    all_letters = None
    targets = None
    uncertified = None
    quotients_used = 0
    for trial in range(MAX_TRIALS):
        gens = {s: tuple(rng.sample(range(N_PERM), N_PERM)) for s in base_letters}
        gens = solve_dependent(gens)
        if not relation_check(gens):
            return {"PASS": False, "error": "relation violated in quotient (bug)"}
        if all_letters is None:
            all_letters = sorted(gens.keys())
            lets = [c for s in all_letters for c in (s, s.upper())]
            words = [w for w in reduced_words(lets, 4) if cyclically_reduced(w)]
            pv = []
            for i in range(len(pentagon_vertex_words)):
                for j in range(i + 1, len(pentagon_vertex_words)):
                    pv.append((pentagon_vertex_words[i], pentagon_vertex_words[j]))
            targets = {"girth": set(words), "penta": set(pv)}
            uncertified = {"girth": set(words), "penta": set(pv)}
        quotients_used += 1
        ident = pid(N_PERM)
        for w in list(uncertified["girth"]):
            if eval_word(w, gens) != ident:
                uncertified["girth"].discard(w)
        for (w1, w2) in list(uncertified["penta"]):
            if eval_word(w1, gens) != eval_word(w2, gens):
                uncertified["penta"].discard((w1, w2))
        if not uncertified["girth"] and not uncertified["penta"]:
            break
    res = {
        "quotients_used": quotients_used,
        "n_perm": N_PERM, "seed": SEED,
        "girth_words_total": len(targets["girth"]),
        "girth_uncertified": sorted(uncertified["girth"]),
        "pentagon_pairs_total": len(targets["penta"]),
        "pentagon_uncertified": [list(p) for p in uncertified["penta"]],
    }
    res["PASS"] = (not uncertified["girth"]) and (not uncertified["penta"])
    return res

def e2_gate():
    # Gamma_3 = <a,b,c | a b a c^-1 b^-1> ; c := b^-1 a b a
    def solve(g):
        a, b = g["a"], g["b"]
        g = dict(g)
        g["c"] = pmul(pmul(pmul(pinv(b), a), b), a)
        return g
    def relcheck(g):
        a, b, c = g["a"], g["b"], g["c"]
        lhs = pmul(pmul(a, b), a)          # aba
        rhs = pmul(b, c)                   # bc
        return lhs == rhs
    # vertices do pentagono: 1, a, ab, aba, b
    pv = ["", "a", "ab", "aba", "b"]
    return quotient_gate("E2", ["a", "b"], solve, relcheck, pv)

def e3_gate():
    # Gamma_5 = <a,b,c,d,e | abc = ed> ; e := a b c d^-1
    def solve(g):
        a, b, c, d = g["a"], g["b"], g["c"], g["d"]
        g = dict(g)
        g["e"] = pmul(pmul(pmul(a, b), c), pinv(d))
        return g
    def relcheck(g):
        lhs = pmul(pmul(g["a"], g["b"]), g["c"])   # abc
        rhs = pmul(g["e"], g["d"])                 # ed
        return lhs == rhs
    # vertices do pentagono: 1, a, ab, abc, e
    pv = ["", "a", "ab", "abc", "e"]
    return quotient_gate("E3", ["a", "b", "c", "d"], solve, relcheck, pv)

def main():
    OUT["E1"] = e1_gate()
    OUT["E2"] = e2_gate()
    OUT["E3"] = e3_gate()
    OUT["ALL_PASS"] = all(OUT[k]["PASS"] for k in ("E1", "E2", "E3"))
    with open("gate_m1b.json", "w", encoding="utf-8") as f:
        json.dump(OUT, f, indent=2, ensure_ascii=False)
    for k in ("E1", "E2", "E3"):
        print(k, "PASS" if OUT[k]["PASS"] else "FAIL")
        for kk, vv in OUT[k].items():
            if kk not in ("PASS",):
                print("   ", kk, "=", vv if not isinstance(vv, dict) else vv)
    print("GATE:", "VERDE" if OUT["ALL_PASS"] else "NAO-VERDE")

if __name__ == "__main__":
    main()
