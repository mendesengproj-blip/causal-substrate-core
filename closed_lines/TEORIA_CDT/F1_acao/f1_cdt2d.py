"""
f1_cdt2d.py — TEORIA_CDT, Fase F1: ensemble causal 2D + ação de Regge + Wick + MC.

Documento de referência (CONGELADO antes deste código): ../PRE_REGISTRO.md
Charter: ../CHARTER.md   Glossário: ../GLOSSARIO.md

OBJETIVO DE F1 (engenharia, não física nova): validar a maquinaria contra os
gabaritos analíticos de 2D-CDT. d_H = 2 é o gate-mor (G1).

REPRESENTAÇÃO (re-derivada aqui, não importada):
  - Espaço-tempo = toro: T fatias de tempo (periódicas), cada fatia = círculo de
    ell_t arestas tipo-espaço. Entre fatia s e s+1 = "sanduíche" s, uma tira de
    triângulos (2,1)=UP (base na fatia s, ápice na s+1) e (1,2)=DOWN (base na
    fatia s+1, ápice na s). #UP no sanduíche s = ell_s ; #DOWN = ell_{s+1}.
  - Cada triângulo i guarda: typ[i] (+1 UP / -1 DOWN), sand[i] (índice do sanduíche
    0..T-1), e 3 vizinhos: nbL/nbR (através das arestas tipo-tempo, dentro do
    sanduíche — a tira é um ciclo via nbR) e nbC (através da aresta tipo-espaço,
    para o sanduíche vizinho; nbC liga sempre UP<->DOWN).

AÇÃO (2D): curvatura = Gauss-Bonnet = topológica (constante no toro) => não-dinâmica.
  Dinâmica = só volume:  S = lambda * N2  (+ potencial de fixação de volume).
  Rotação de Wick: peso e^{-S} real positivo (Metropolis). Em 2D o parâmetro alpha
  de Wick não altera a combinatória do ensemble de volume (curvatura trivial), então
  a continuação é o peso de Boltzmann padrão — registrado no PRE_REGISTRO §2.

MOVES (preservam folheação; ergódicos para topologia fixa — gate G4):
  - flip:   troca um par UP-DOWN adjacente na tira (preserva N2 e todos os ell).
  - add:    insere um vértice numa fatia (divide uma aresta tipo-espaço): +2 triâng.
  - delete: inverso do add (remove vértice de coordenação-4): -2 triâng.

Autor: TEORIA_CDT / F1.  Sem importação de TEIC/DEV/SR (regra de não-contaminação).
"""

import json
import math
import os
import sys
import time

import numpy as np

UP = 1
DOWN = -1


class CDT2D:
    """Triangulação causal 2D (toro) com moves de Pachner foliados."""

    def __init__(self, T, ell0, seed=0, cap=None):
        assert T >= 3, "T>=3 para toro temporal não-degenerado"
        assert ell0 >= 3, "ell0>=3 para fatia circular válida"
        self.T = T
        self.rng = np.random.default_rng(seed)
        # capacidade inicial dos arrays (cresce se necessário)
        n0 = 2 * ell0 * T
        if cap is None:
            cap = max(64, 8 * n0)
        self.cap = cap
        self.typ = np.zeros(cap, dtype=np.int8)
        self.sand = np.zeros(cap, dtype=np.int32)
        self.nbL = np.full(cap, -1, dtype=np.int32)
        self.nbR = np.full(cap, -1, dtype=np.int32)
        self.nbC = np.full(cap, -1, dtype=np.int32)
        self.N = 0  # número de triângulos vivos (ocupam slots 0..N-1)
        self.ell = np.zeros(T, dtype=np.int64)  # comprimento de cada fatia
        self._build_regular(ell0)

    # ------------------------------------------------------------------
    # construção regular (cold start)
    # ------------------------------------------------------------------
    def _new_slot(self):
        if self.N >= self.cap:
            self._grow()
        k = self.N
        self.N += 1
        return k

    def _grow(self):
        newcap = self.cap * 2
        for name in ("typ", "sand", "nbL", "nbR", "nbC"):
            old = getattr(self, name)
            arr = np.full(newcap, -1, dtype=old.dtype)
            arr[: self.cap] = old
            setattr(self, name, arr)
        self.cap = newcap

    def _build_regular(self, ell0):
        """Toro regular: cada sanduíche = U,D,U,D,... (ell0 UP, ell0 DOWN).

        Layout dos slots: sanduíche s ocupa slots [s*2*ell0 : (s+1)*2*ell0].
        Dentro do sanduíche, posição 2k = UP_k (base = aresta-espaço k da fatia s),
        posição 2k+1 = DOWN_k (topo = aresta-espaço k da fatia s+1).
        nbR avança a posição (mod 2*ell0). nbC liga UP_k(sand s) <-> DOWN_k(sand s-1).
        """
        T, m = self.T, ell0
        W = 2 * m  # triângulos por sanduíche
        self.N = W * T
        for s in range(T):
            base = s * W
            for p in range(W):
                i = base + p
                self.sand[i] = s
                self.typ[i] = UP if (p % 2 == 0) else DOWN
                self.nbR[i] = base + (p + 1) % W
                self.nbL[i] = base + (p - 1) % W
        # nbC: UP_k(s) base = aresta k da fatia s; o vizinho espacial é o DOWN_k
        # do sanduíche s-1, cujo topo = aresta k da fatia s.
        for s in range(T):
            base = s * W
            prev = ((s - 1) % T) * W
            for k in range(m):
                up = base + 2 * k       # UP_k no sanduíche s
                down_prev = prev + 2 * k + 1  # DOWN_k no sanduíche s-1
                self.nbC[up] = down_prev
                self.nbC[down_prev] = up
        self.ell[:] = ell0

    # ------------------------------------------------------------------
    # utilidades de geometria
    # ------------------------------------------------------------------
    def slice_of_spatial(self, i):
        """Fatia onde mora a aresta tipo-espaço (base/topo) do triângulo i."""
        if self.typ[i] == UP:
            return int(self.sand[i])           # base na fatia inferior = sand
        return (int(self.sand[i]) + 1) % self.T  # topo na fatia superior

    @property
    def N2(self):
        return self.N

    # ------------------------------------------------------------------
    # MOVES
    # ------------------------------------------------------------------
    def can_flip(self, i):
        j = self.nbR[i]
        if j == i or j < 0:
            return False
        if self.typ[i] == self.typ[j]:
            return False
        L = self.nbL[i]
        RR = self.nbR[j]
        # degenerescências em tiras curtas
        if L == j or RR == i or L == i or RR == j:
            return False
        if self.nbC[i] == self.nbC[j]:
            return False
        return True

    def do_flip(self, i):
        """Troca i (esq) e j=nbR[i] (dir) de ordem na tira. Tipos preservados,
        ápices/diagonais re-conectados. Involutivo."""
        j = self.nbR[i]
        L = self.nbL[i]
        RR = self.nbR[j]
        # rewire: ...L, i, j, RR...  ->  ...L, j, i, RR...
        self.nbR[i] = RR
        self.nbL[i] = j
        self.nbR[j] = i
        self.nbL[j] = L
        self.nbR[L] = j
        self.nbL[RR] = i
        # nbC[i], nbC[j] inalterados (arestas espaciais externas do quad)

    def can_delete(self, i, ell_min):
        """Vértice no extremo-direito da aresta-espaço de i é coordenação-4?"""
        ip = self.nbR[i]              # i' à direita de i
        if ip == i or ip < 0:
            return False
        if self.typ[ip] != self.typ[i]:
            return False              # precisa par mesmo-tipo (criado por add)
        j = self.nbC[i]
        jp = self.nbC[ip]
        if j < 0 or jp < 0:
            return False
        if self.typ[j] != self.typ[jp]:
            return False
        if self.nbR[j] != jp:
            return False              # j,j' devem ser adjacentes (compartilham ápice q)
        # não colapsar slots coincidentes
        if len({int(i), int(ip), int(j), int(jp)}) != 4:
            return False
        s = self.slice_of_spatial(i)
        if self.ell[s] - 1 < ell_min:
            return False
        # evitar degenerescência: após remover ip,jp, tira não pode virar auto-laço
        if self.nbR[ip] == i or self.nbR[jp] == j:
            return False
        return True

    def do_delete(self, i):
        """Remove i'=nbR[i] e j'=nbC[i'] (o vértice de coordenação-4)."""
        ip = self.nbR[i]
        j = self.nbC[i]
        jp = self.nbC[ip]
        RU = self.nbR[ip]
        RD = self.nbR[jp]
        # i absorve o lado direito de i'
        self.nbR[i] = RU
        self.nbL[RU] = i
        # j absorve o lado direito de j'
        self.nbR[j] = RD
        self.nbL[RD] = j
        # nbC[i]=j permanece
        s = self.slice_of_spatial(i)
        self.ell[s] -= 1
        # remover slots ip e jp (swap-remove)
        self._remove_slots(ip, jp)

    def do_add(self, i):
        """Divide a aresta-espaço de i: cria i' (à dir de i) e j' (à dir de j=nbC[i])."""
        j = self.nbC[i]
        RU = self.nbR[i]
        RD = self.nbR[j]
        ip = self._new_slot()
        jp = self._new_slot()
        # tipos/sanduíches herdados
        self.typ[ip] = self.typ[i]
        self.sand[ip] = self.sand[i]
        self.typ[jp] = self.typ[j]
        self.sand[jp] = self.sand[j]
        # inserir i' entre i e RU
        self.nbL[ip] = i
        self.nbR[ip] = RU
        self.nbR[i] = ip
        self.nbL[RU] = ip
        # inserir j' entre j e RD
        self.nbL[jp] = j
        self.nbR[jp] = RD
        self.nbR[j] = jp
        self.nbL[RD] = jp
        # arestas espaciais: i<->j (metade esq), i'<->j' (metade dir)
        self.nbC[i] = j
        self.nbC[j] = i
        self.nbC[ip] = jp
        self.nbC[jp] = ip
        s = self.slice_of_spatial(i)
        self.ell[s] += 1

    def _remove_slots(self, a, b):
        """Swap-remove de dois slots, corrigindo referências dos vizinhos."""
        for slot in sorted((int(a), int(b)), reverse=True):
            last = self.N - 1
            if slot != last:
                self._move_slot(last, slot)
            self.N -= 1

    def _move_slot(self, src, dst):
        """Move triângulo do slot src para dst e corrige todas as referências."""
        self.typ[dst] = self.typ[src]
        self.sand[dst] = self.sand[src]
        L = self.nbL[src]
        R = self.nbR[src]
        C = self.nbC[src]
        self.nbL[dst] = L
        self.nbR[dst] = R
        self.nbC[dst] = C
        # vizinhos de src agora apontam para dst
        if self.nbR[L] == src:
            self.nbR[L] = dst
        if self.nbL[L] == src:
            self.nbL[L] = dst
        if self.nbR[R] == src:
            self.nbR[R] = dst
        if self.nbL[R] == src:
            self.nbL[R] = dst
        if C >= 0 and self.nbC[C] == src:
            self.nbC[C] = dst

    # ------------------------------------------------------------------
    # MONTE CARLO (Metropolis, grand-canônico com potencial de volume)
    # ------------------------------------------------------------------
    def sweep(self, lam, eps, Vtarget, ell_min=3, n_moves=None,
              p_flip=0.5, accept_stats=None):
        """Um 'sweep' = n_moves tentativas (default N2). Retorna nada; atualiza estado."""
        if n_moves is None:
            n_moves = self.N
        rng = self.rng
        for _ in range(n_moves):
            i = int(rng.integers(self.N))
            u = rng.random()
            if u < p_flip:
                if self.can_flip(i):
                    self.do_flip(i)
                    if accept_stats is not None:
                        accept_stats['flip_acc'] += 1
                if accept_stats is not None:
                    accept_stats['flip_try'] += 1
            elif u < p_flip + 0.5 * (1 - p_flip):
                # ADD
                N2 = self.N
                dS = 2 * lam + 0.5 * eps * ((N2 + 2 - Vtarget) ** 2 - (N2 - Vtarget) ** 2)
                A = math.exp(-dS) * N2 / (N2 + 2)
                if rng.random() < A:
                    self.do_add(i)
                    if accept_stats is not None:
                        accept_stats['add_acc'] += 1
                if accept_stats is not None:
                    accept_stats['add_try'] += 1
            else:
                # DELETE
                if self.can_delete(i, ell_min):
                    N2 = self.N
                    dS = -2 * lam + 0.5 * eps * ((N2 - 2 - Vtarget) ** 2 - (N2 - Vtarget) ** 2)
                    A = math.exp(-dS) * N2 / (N2 - 2)
                    if rng.random() < A:
                        self.do_delete(i)
                        if accept_stats is not None:
                            accept_stats['del_acc'] += 1
                if accept_stats is not None:
                    accept_stats['del_try'] += 1

    # ------------------------------------------------------------------
    # CHECADOR DE INVARIANTES (gate E0)
    # ------------------------------------------------------------------
    def check_manifold(self):
        """Retorna lista de violações (vazia = OK)."""
        errs = []
        N = self.N
        for i in range(N):
            L, R, C = int(self.nbL[i]), int(self.nbR[i]), int(self.nbC[i])
            if not (0 <= L < N and 0 <= R < N and 0 <= C < N):
                errs.append(f"i={i}: vizinho fora de [0,N) L={L} R={R} C={C}")
                continue
            if self.nbL[R] != i:
                errs.append(f"i={i}: nbL[nbR[i]]={int(self.nbL[R])}!=i")
            if self.nbR[L] != i:
                errs.append(f"i={i}: nbR[nbL[i]]={int(self.nbR[L])}!=i")
            if self.nbC[C] != i:
                errs.append(f"i={i}: nbC[nbC[i]]={int(self.nbC[C])}!=i (involução espacial)")
            # tipo de nbR/nbL: mesmo sanduíche
            if self.sand[R] != self.sand[i] or self.sand[L] != self.sand[i]:
                errs.append(f"i={i}: vizinho tipo-tempo em sanduíche diferente")
            # nbC liga UP<->DOWN
            if self.typ[C] == self.typ[i]:
                errs.append(f"i={i}: nbC mesmo tipo (deveria UP<->DOWN)")
            # sanduíches adjacentes via nbC
            si, sc = int(self.sand[i]), int(self.sand[C])
            if self.typ[i] == UP:
                if sc != (si - 1) % self.T:
                    errs.append(f"i={i} UP: nbC sand {sc} != sand-1")
            else:
                if sc != (si + 1) % self.T:
                    errs.append(f"i={i} DOWN: nbC sand {sc} != sand+1")
            if len(errs) > 50:
                break
        # contagem ell vs UPs por sanduíche
        ell_check = np.zeros(self.T, dtype=np.int64)
        for i in range(N):
            if self.typ[i] == UP:
                ell_check[int(self.sand[i])] += 1
        if not np.array_equal(ell_check, self.ell):
            errs.append(f"ell inconsistente: contado(UPs)={ell_check.tolist()} vs ell={self.ell.tolist()}")
        # DOWNs por sanduíche s devem = ell[s+1]
        down_check = np.zeros(self.T, dtype=np.int64)
        for i in range(N):
            if self.typ[i] == DOWN:
                down_check[int(self.sand[i])] += 1
        ell_roll = np.roll(self.ell, -1)
        if not np.array_equal(down_check, ell_roll):
            errs.append(f"DOWNs por sanduíche {down_check.tolist()} != ell[s+1] {ell_roll.tolist()}")
        # Euler (toro): V-E+F=0
        F = N
        V = int(self.ell.sum())          # vértices = soma das fatias
        E_space = int(self.ell.sum())    # arestas espaço = soma das fatias
        E_time = N                       # arestas tempo = #triângulos
        chi = V - (E_space + E_time) + F
        if chi != 0:
            errs.append(f"Euler chi={chi} != 0 (toro)")
        return errs

    # ------------------------------------------------------------------
    # OBSERVÁVEIS
    # ------------------------------------------------------------------
    def dual_adjacency(self):
        """Lista de adjacência do grafo dual (cada triângulo: 3 vizinhos)."""
        N = self.N
        adj = np.empty((N, 3), dtype=np.int64)
        adj[:, 0] = self.nbL[:N]
        adj[:, 1] = self.nbR[:N]
        adj[:, 2] = self.nbC[:N]
        return adj

    def hausdorff_profile(self, n_sources=40, rmax=None):
        """N(r) cumulativo médio no grafo dual (BFS). Retorna (r, Nbar)."""
        adj = self.dual_adjacency()
        N = self.N
        if rmax is None:
            rmax = N  # corta na saturação naturalmente
        rng = self.rng
        srcs = rng.choice(N, size=min(n_sources, N), replace=False)
        maxlen = 0
        profiles = []
        for s in srcs:
            dist = np.full(N, -1, dtype=np.int64)
            dist[s] = 0
            frontier = [int(s)]
            counts = [1]  # nós a distância 0,1,2,...
            d = 0
            while frontier:
                nxt = []
                for u in frontier:
                    for v in adj[u]:
                        if dist[v] < 0:
                            dist[v] = d + 1
                            nxt.append(int(v))
                if nxt:
                    counts.append(len(nxt))
                frontier = nxt
                d += 1
            cum = np.cumsum(counts)
            profiles.append(cum)
            maxlen = max(maxlen, len(cum))
        # média alinhada (preenche caudas com o valor final = N)
        M = np.full((len(profiles), maxlen), N, dtype=np.float64)
        for k, p in enumerate(profiles):
            M[k, : len(p)] = p
        Nbar = M.mean(axis=0)
        r = np.arange(maxlen)
        return r, Nbar

    def measure_dH(self, n_sources=40):
        """Ajusta d_H pela inclinação de log N(r) vs log r na janela linear."""
        r, Nbar = self.hausdorff_profile(n_sources=n_sources)
        # janela: r de 2 até onde N(r) < 0.5*Nmax (antes da saturação)
        Nmax = self.N
        mask = (r >= 2) & (Nbar < 0.5 * Nmax) & (r < len(r))
        if mask.sum() < 3:
            return float('nan'), (r, Nbar)
        x = np.log(r[mask])
        y = np.log(Nbar[mask])
        A = np.vstack([x, np.ones_like(x)]).T
        slope, _ = np.linalg.lstsq(A, y, rcond=None)[0]
        return float(slope), (r, Nbar)


# ======================================================================
# GATES
# ======================================================================
def gate_E0(verbose=True):
    """Gate de engenharia: invariantes, contagem, reversibilidade."""
    report = {}
    # E0-a: cilindro/toro mínimo contável
    T, ell0 = 3, 3
    g = CDT2D(T, ell0, seed=1)
    report['E0a_N2'] = int(g.N)
    report['E0a_N2_expected'] = 2 * ell0 * T
    report['E0a_V'] = int(g.ell.sum())
    report['E0a_V_expected'] = ell0 * T
    errs0 = g.check_manifold()
    report['E0a_invariants_ok'] = (len(errs0) == 0)
    report['E0a_errs'] = errs0[:10]

    # E0-b: Euler em vários tamanhos
    chi_ok = True
    for (T_, e_) in [(4, 3), (5, 6), (8, 4)]:
        gg = CDT2D(T_, e_, seed=2)
        if gg.check_manifold():
            chi_ok = False
    report['E0b_euler_ok'] = chi_ok

    # E0-c: invariantes preservados após 10^4 moves aleatórios
    g2 = CDT2D(6, 6, seed=3)
    lam, eps, Vt = math.log(2), 0.02, g2.N
    stats = dict(flip_try=0, flip_acc=0, add_try=0, add_acc=0, del_try=0, del_acc=0)
    for _ in range(200):
        g2.sweep(lam, eps, Vt, ell_min=3, n_moves=50, accept_stats=stats)
    errsc = g2.check_manifold()
    report['E0c_moves'] = 200 * 50
    report['E0c_invariants_ok'] = (len(errsc) == 0)
    report['E0c_errs'] = errsc[:10]
    report['E0c_accept'] = stats
    report['E0c_N2_after'] = int(g2.N)

    # E0-d: reversibilidade — add seguido do delete inverso retorna ao original
    g3 = CDT2D(5, 5, seed=4)
    snap0 = _snapshot(g3)
    # escolhe um triângulo, add nele, depois delete no mesmo i
    i = 7
    g3.do_add(i)
    ok_mid = (len(g3.check_manifold()) == 0)
    # o delete inverso é em i (remove i'=nbR[i] recém-criado)
    can = g3.can_delete(i, ell_min=2)
    if can:
        g3.do_delete(i)
    snap1 = _snapshot(g3)
    report['E0d_mid_ok'] = ok_mid
    report['E0d_can_delete'] = bool(can)
    report['E0d_reversible'] = _snapshots_equal(snap0, snap1)

    # E0-d2: flip é involutivo
    g4 = CDT2D(6, 6, seed=5)
    snapf0 = _snapshot(g4)
    # acha um i flipável
    fi = None
    for i in range(g4.N):
        if g4.can_flip(i):
            fi = i
            break
    rev_flip = None
    if fi is not None:
        g4.do_flip(fi)
        ok_f = (len(g4.check_manifold()) == 0)
        # inverso: agora nbR[j]=i com j o antigo nbR; flip em j desfaz
        # após do_flip(fi): nbL[fi]=j (antigo nbR). j = nbL[fi].
        jj = int(g4.nbL[fi])
        if g4.can_flip(jj):
            g4.do_flip(jj)
        snapf1 = _snapshot(g4)
        rev_flip = _snapshots_equal(snapf0, snapf1)
        report['E0d_flip_mid_ok'] = ok_f
    report['E0d_flip_involutive'] = rev_flip

    all_ok = (report['E0a_invariants_ok'] and report['E0b_euler_ok']
              and report['E0c_invariants_ok'] and report['E0d_mid_ok']
              and report['E0d_reversible'] and report.get('E0d_flip_involutive'))
    report['E0_GREEN'] = bool(all_ok)
    if verbose:
        print("=== GATE E0 (engenharia) ===")
        for k, v in report.items():
            if k.endswith('errs') and not v:
                continue
            print(f"  {k}: {v}")
        print(f"  >>> E0 {'VERDE' if all_ok else 'VERMELHO'}")
    return report


def _snapshot(g):
    N = g.N
    return (N, g.typ[:N].copy(), g.sand[:N].copy(),
            g.nbL[:N].copy(), g.nbR[:N].copy(), g.nbC[:N].copy(),
            g.ell.copy())


def _snapshots_equal(a, b):
    if a[0] != b[0]:
        return False
    for x, y in zip(a[1:], b[1:]):
        if not np.array_equal(x, y):
            return False
    return True


if __name__ == "__main__":
    t0 = time.time()
    rep = gate_E0(verbose=True)
    print(f"\n[tempo E0: {time.time()-t0:.2f}s]")
    out = os.path.join(os.path.dirname(__file__), "e0_report.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump({k: (v if not isinstance(v, dict) else v) for k, v in rep.items()},
                  f, indent=2, default=str, ensure_ascii=False)
    print(f"[escrito: {out}]")
    sys.exit(0 if rep['E0_GREEN'] else 1)
