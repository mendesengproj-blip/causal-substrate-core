"""
f1b_cdt3d.py — TEORIA_CDT, Fase F1b: ensemble causal 3D + ação de Regge DINÂMICA + Wick + MC.

Documento de referência (CONGELADO antes deste código): ../F1b_PHASE_GATE.md
Charter: ../CHARTER.md   Glossário: ../GLOSSARIO.md   Síntese 2D: ../F1_acao/F1_SYNTHESIS.md

OBJETIVO DE F1b (engenharia, não física nova ainda): construir e VALIDAR o motor CDT 3D
PURO (γ=0, sem semente). Em 3D a curvatura de Regge é DINÂMICA (≠ 2D topológico), então
a ação S = −k0·N0 + k3·N3 molda a geometria. Gate-mor desta fase: o diagrama de fases
conhecido (crumpled / branched-polymer / ESTENDIDA-de-Sitter) emerge. E0-3D é o FILTRO.

ESTRATÉGIA DE INTEGRIDADE (a lição do F1b_PHASE_GATE §5):
  O risco de F1b é bug-density dos 5 movimentos de Pachner 3D. A defesa é a REPRESENTAÇÃO:
  usamos um COMPLEXO SIMPLICIAL EXPLÍCITO (conjunto de tetraedros = tuplas de vértices,
  mapas triângulo→tetraedro e vértice→tetraedro derivados). O validador de manifold
  (check_manifold) opera DIRETO sobre o complexo e é AGNÓSTICO ao movimento: qualquer
  movimento incorreto produz uma violação detectável (triângulo não-compartilhado-por-2,
  link de vértice ≠ S², folheação quebrada). Logo é IMPOSSÍVEL um movimento bugado passar
  como verde. Trocamos velocidade por validabilidade — a escolha certa dado o charter §3.

REPRESENTAÇÃO (re-derivada aqui, sem importar AJL):
  - Espaço-tempo = S²×S¹: T fatias de tempo (periódicas em t∈0..T-1). Cada fatia t é uma
    triangulação 2D fechada de topologia S² (genus 0). Vértices carregam rótulo de tempo vt[v].
  - Entre fatias t e t+1 (um "sanduíche") há tetraedros de 3 tipos:
      (3,1): 3 vértices em t, 1 em t+1   (base 2D embaixo, ápice em cima)
      (1,3): 1 em t, 3 em t+1            (espelho)
      (2,2): 2 em t, 2 em t+1           (aresta-tipo-espaço embaixo e em cima)
  - Vínculo causal (o "C" do CDT): toda aresta liga vértices com |Δt|≤1 (mod T); fatias S²
    não rasgam (topologia fixa). Nenhuma aresta pula fatia.

AÇÃO (3D, DINÂMICA — re-derivada):
  Após Wick, a ação de Einstein-Regge 3D toma a forma combinatória padrão
      S = −k0·N0 + k3·N3        (k0 ∝ 1/G inverso de Newton; k3 ∝ const. cosmológica)
  N0 = #vértices, N3 = #tetraedros. (Opcional: assimetria Δ tipo-tempo/tipo-espaço como
  2º eixo; aqui Δ=0 — fatiamento isotrópico — fixado no pré-registro.) Volume fixado por
  potencial quadrático ε(N3−Vt)². Peso e^{−S} real positivo (Metropolis).

MOVES de Pachner 3D foliados (o conjunto ergódico mínimo, re-derivado):
  (2,6)/(6,2): insere/remove vértice numa fatia (muda volume espacial local) — ±4 tetra.
  (4,4):       flip de aresta tipo-espaço num sanduíche (preserva N3).
  (2,3)/(3,2): rearranjo de tetraedros em torno de triângulo/aresta tipo-tempo (±1 tetra).

Autor: TEORIA_CDT / F1b. Sem importação de TEIC/DEV/SR (regra de não-contaminação).
"""

import json
import math
import os
import sys
import time
from collections import defaultdict

import numpy as np


def tri_faces(tet):
    """As 4 faces (triângulos, frozenset de 3 vértices) de um tetraedro (tupla de 4)."""
    a, b, c, d = tet
    return (frozenset((a, b, c)), frozenset((a, b, d)),
            frozenset((a, c, d)), frozenset((b, c, d)))


class IndexedSet:
    """Conjunto com amostragem uniforme O(1) (lista + mapa de posição, swap-remove)."""

    __slots__ = ("items", "pos")

    def __init__(self):
        self.items = []
        self.pos = {}

    def add(self, x):
        if x in self.pos:
            return
        self.pos[x] = len(self.items)
        self.items.append(x)

    def discard(self, x):
        i = self.pos.pop(x, None)
        if i is None:
            return
        last = self.items.pop()
        if i < len(self.items):
            self.items[i] = last
            self.pos[last] = i

    def sample(self, rng):
        return self.items[rng.integers(len(self.items))]

    def __len__(self):
        return len(self.items)

    def __contains__(self, x):
        return x in self.pos


class CDT3D:
    """Triangulação causal 3D (S²×S¹) como complexo simplicial explícito."""

    def __init__(self, T, seed=0):
        assert T >= 3, "T>=3 para S^1 temporal não-degenerado"
        self.T = T
        self.rng = np.random.default_rng(seed)
        self.vt = {}                       # vid -> tempo (0..T-1)
        self._next_vid = 0
        self.tets = {}                     # tid -> tupla ORDENADA de 4 vids
        self._next_tid = 0
        self.tri2tet = defaultdict(set)    # frozenset(3 vids) -> {tids}
        self.vert2tet = defaultdict(set)   # vid -> {tids}
        # estruturas indexadas (p/ amostragem uniforme O(1) e balanço detalhado)
        self.spatial_set = IndexedSet()    # triângulos espaciais distintos
        self.timelike_set = IndexedSet()   # triângulos tipo-tempo distintos
        self.edge_set = IndexedSet()       # arestas distintas
        self.vertex_set = IndexedSet()     # vértices
        self._edge_mult = defaultdict(int) # aresta -> #tetra que a contêm
        self._build_regular()

    # contagens via len() das estruturas indexadas
    @property
    def n_tri_spatial(self):
        return len(self.spatial_set)

    @property
    def n_tri_timelike(self):
        return len(self.timelike_set)

    @property
    def n_edges(self):
        return len(self.edge_set)

    # ------------------------------------------------------------------
    # primitivas de complexo
    # ------------------------------------------------------------------
    def _new_vertex(self, t):
        v = self._next_vid
        self._next_vid += 1
        self.vt[v] = t % self.T
        self.vertex_set.add(v)
        return v

    def _add_tet(self, verts):
        """Registra um tetraedro. verts: iterável de 4 vids distintos."""
        tet = tuple(sorted(verts))
        assert len(set(tet)) == 4, f"tetraedro degenerado {tet}"
        tid = self._next_tid
        self._next_tid += 1
        self.tets[tid] = tet
        for f in tri_faces(tet):
            s = self.tri2tet[f]
            if not s:  # triângulo novo (0 -> 1)
                if self._tri_is_spatial(f):
                    self.spatial_set.add(f)
                else:
                    self.timelike_set.add(f)
            s.add(tid)
        for v in tet:
            self.vert2tet[v].add(tid)
        for e in self._tet_edges(tet):
            if self._edge_mult[e] == 0:
                self.edge_set.add(e)
            self._edge_mult[e] += 1
        return tid

    def _del_tet(self, tid):
        tet = self.tets.pop(tid)
        for f in tri_faces(tet):
            s = self.tri2tet[f]
            s.discard(tid)
            if not s:  # triângulo sumiu (1 -> 0)
                if self._tri_is_spatial(f):
                    self.spatial_set.discard(f)
                else:
                    self.timelike_set.discard(f)
                del self.tri2tet[f]
        for v in tet:
            self.vert2tet[v].discard(tid)
        for e in self._tet_edges(tet):
            self._edge_mult[e] -= 1
            if self._edge_mult[e] == 0:
                self.edge_set.discard(e)
                del self._edge_mult[e]
        return tet

    @staticmethod
    def _tet_edges(tet):
        a, b, c, d = tet
        return (frozenset((a, b)), frozenset((a, c)), frozenset((a, d)),
                frozenset((b, c)), frozenset((b, d)), frozenset((c, d)))

    def _tri_is_spatial(self, f):
        it = iter(f)
        t0 = self.vt[next(it)]
        return all(self.vt[u] == t0 for u in f)

    def _del_vertex(self, v):
        assert not self.vert2tet.get(v), f"vértice {v} ainda em tetraedros"
        self.vert2tet.pop(v, None)
        self.vt.pop(v, None)
        self.vertex_set.discard(v)

    # ------------------------------------------------------------------
    # tempos / tipos
    # ------------------------------------------------------------------
    def _bottom_top(self, tet):
        """Para um tetraedro, retorna (t_bottom, t_top) com (t_top-t_bottom)%T==1."""
        ts = set(self.vt[v] for v in tet)
        assert len(ts) == 2, f"tetraedro {tet} com tempos {ts} (deveria ter 2)"
        a, b = sorted(ts)
        # consecutivos no círculo: ou (a,b) com b=a+1, ou (a,b)=(0,T-1) wrap
        if (b - a) % self.T == 1:
            return a, b
        if (a - b) % self.T == 1:
            return b, a
        raise AssertionError(f"tempos não-consecutivos {ts} em {tet}")

    def tet_type(self, tet):
        """Retorna (n_bot, n_top) p.ex. (3,1),(1,3),(2,2); n_bot = #verts na fatia inferior."""
        tb, tt = self._bottom_top(tet)
        n_bot = sum(1 for v in tet if self.vt[v] == tb)
        return (n_bot, 4 - n_bot)

    def base_slice_of_31(self, tet):
        """Para um (3,1), a fatia (inferior) onde está sua base espacial."""
        tb, _ = self._bottom_top(tet)
        return tb

    # ------------------------------------------------------------------
    # construção regular (cold start) — S²×S¹ com (3,1),(2,2),(1,3)
    # ------------------------------------------------------------------
    def _build_regular(self):
        """Cada fatia = ∂Δ³ (4 vértices, 4 triângulos espaciais, S² mínimo).
        Sanduíche = 4 prismas (1 por triângulo espacial), cada prisma → 3 tetra
        ((3,1)+(2,2)+(1,3)) via ordenação local 'fundo<topo' (diagonais consistentes).
        """
        T = self.T
        # vértices: 4 por fatia
        V = {}  # (t,k) -> vid
        for t in range(T):
            for k in range(4):
                V[(t, k)] = self._new_vertex(t)
        # triângulos espaciais de cada fatia: as 4 faces de Δ³ sobre {0,1,2,3}
        spatial_tris = [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
        for t in range(T):
            tn = (t + 1) % T
            for (k0, k1, k2) in spatial_tris:  # já ordenados k0<k1<k2
                b0, b1, b2 = V[(t, k0)], V[(t, k1)], V[(t, k2)]      # fundo (fatia t)
                a0, a1, a2 = V[(tn, k0)], V[(tn, k1)], V[(tn, k2)]   # topo (fatia t+1)
                # prisma fundo(b0<b1<b2) topo(a*): diagonais b_lo–a_hi (consistente)
                self._add_tet((b0, b1, b2, a2))   # (3,1): 3 fundo, 1 topo
                self._add_tet((b0, b1, a1, a2))   # (2,2): 2 fundo, 2 topo
                self._add_tet((b0, a0, a1, a2))   # (1,3): 1 fundo, 3 topo

    # ------------------------------------------------------------------
    # contagens
    # ------------------------------------------------------------------
    @property
    def N3(self):
        return len(self.tets)

    @property
    def N0(self):
        return len(self.vt)

    def edges(self):
        """Conjunto de arestas (frozenset de 2) derivado dos tetraedros."""
        E = set()
        for tet in self.tets.values():
            a, b, c, d = tet
            E.update((frozenset((a, b)), frozenset((a, c)), frozenset((a, d)),
                      frozenset((b, c)), frozenset((b, d)), frozenset((c, d))))
        return E

    def count_types(self):
        c = {(3, 1): 0, (1, 3): 0, (2, 2): 0}
        for tet in self.tets.values():
            c[self.tet_type(tet)] += 1
        return c

    def spatial_volume_profile(self):
        """N31(t) = #tetraedros (3,1) com base na fatia t  (∝ volume espacial da fatia)."""
        prof = np.zeros(self.T, dtype=np.int64)
        for tet in self.tets.values():
            if self.tet_type(tet) == (3, 1):
                prof[self.base_slice_of_31(tet)] += 1
        return prof

    # ------------------------------------------------------------------
    # dimensão de Hausdorff (grafo dual: tetra vizinhos por triângulo compartilhado)
    # ------------------------------------------------------------------
    def dual_neighbors(self):
        """tid -> lista de até 4 tids vizinhos (compartilham um triângulo)."""
        nb = {tid: [] for tid in self.tets}
        for f, tset in self.tri2tet.items():
            if len(tset) == 2:
                a, b = tuple(tset)
                nb[a].append(b)
                nb[b].append(a)
        return nb

    def measure_dH(self, n_sources=30, seed=None):
        """d_H pela inclinação de log N(r) vs log r (shelling BFS no grafo dual)."""
        nb = self.dual_neighbors()
        tids = list(self.tets.keys())
        N = len(tids)
        if N < 8:
            return float('nan')
        rng = self.rng if seed is None else np.random.default_rng(seed)
        srcs = rng.choice(N, size=min(n_sources, N), replace=False)
        maxlen = 0
        profiles = []
        for si in srcs:
            s = tids[si]
            dist = {s: 0}
            frontier = [s]
            counts = [1]
            d = 0
            while frontier:
                nxt = []
                for u in frontier:
                    for v in nb[u]:
                        if v not in dist:
                            dist[v] = d + 1
                            nxt.append(v)
                if nxt:
                    counts.append(len(nxt))
                frontier = nxt
                d += 1
            cum = np.cumsum(counts)
            profiles.append(cum)
            maxlen = max(maxlen, len(cum))
        M = np.full((len(profiles), maxlen), N, dtype=np.float64)
        for k, p in enumerate(profiles):
            M[k, :len(p)] = p
        Nbar = M.mean(axis=0)
        r = np.arange(maxlen)
        mask = (r >= 2) & (Nbar < 0.5 * N) & (r < len(r))
        if mask.sum() < 3:
            return float('nan')
        x = np.log(r[mask])
        y = np.log(Nbar[mask])
        A = np.vstack([x, np.ones_like(x)]).T
        slope = np.linalg.lstsq(A, y, rcond=None)[0][0]
        return float(slope)

    # ==================================================================
    # VALIDADOR DE MANIFOLD (gate E0-3D) — o oráculo agnóstico-ao-movimento
    # ==================================================================
    def check_manifold(self, max_errs=40):
        errs = []

        def add(msg):
            if len(errs) < max_errs:
                errs.append(msg)

        # (1) pseudomanifold: todo triângulo em EXATAMENTE 2 tetraedros
        for f, tset in self.tri2tet.items():
            if len(tset) != 2:
                add(f"triângulo {set(f)} em {len(tset)} tetra (≠2)")

        # (2) folheação: toda aresta com |Δt|∈{0,1} mod T
        for e in self.edges():
            u, w = tuple(e)
            dt = (self.vt[u] - self.vt[w]) % self.T
            if dt not in (0, 1, self.T - 1):
                add(f"aresta {set(e)} com Δt={dt} (folheação quebrada)")

        # (3) tipos válidos: todo tetraedro é (3,1),(1,3) ou (2,2)
        for tid, tet in self.tets.items():
            try:
                typ = self.tet_type(tet)
            except AssertionError as ex:
                add(f"tet {tid} {tet}: {ex}")
                continue
            if typ not in ((3, 1), (1, 3), (2, 2)):
                add(f"tet {tid} {tet}: tipo inválido {typ}")

        # (4) link de cada vértice é S² (variedade): superfície fechada conexa χ=2
        for v in list(self.vt.keys()):
            ok, why = self._vertex_link_is_sphere(v)
            if not ok:
                add(f"link do vértice {v} (t={self.vt[v]}) não é S²: {why}")

        # (5) cada fatia espacial é S² (genus 0): superfície fechada conexa χ=2
        for t in range(self.T):
            ok, why = self._spatial_slice_is_sphere(t)
            if not ok:
                add(f"fatia espacial t={t} não é S²: {why}")

        # (6) Euler do complexo 3D fechado: χ = N0 - N1 + N2 - N3 = 0
        N1 = len(self.edges())
        N2 = len(self.tri2tet)
        chi = self.N0 - N1 + N2 - self.N3
        if chi != 0:
            add(f"Euler χ={chi} ≠ 0 (3-variedade fechada)")

        return errs

    def _surface_is_sphere(self, triangles):
        """triangles: iterável de frozenset(3). Verdade se forma S² (fechada, conexa, χ=2)."""
        tris = list(triangles)
        if not tris:
            return False, "vazio"
        # toda aresta da superfície em exatamente 2 triângulos
        edge_count = defaultdict(int)
        verts = set()
        for tri in tris:
            a, b, c = tuple(tri)
            verts.update((a, b, c))
            for e in (frozenset((a, b)), frozenset((a, c)), frozenset((b, c))):
                edge_count[e] += 1
        for e, n in edge_count.items():
            if n != 2:
                return False, f"aresta {set(e)} em {n} faces da superfície (≠2)"
        # conexidade (via grafo dual das faces que compartilham aresta)
        adj = defaultdict(set)
        edge2face = defaultdict(list)
        for idx, tri in enumerate(tris):
            a, b, c = tuple(tri)
            for e in (frozenset((a, b)), frozenset((a, c)), frozenset((b, c))):
                edge2face[e].append(idx)
        for e, fl in edge2face.items():
            if len(fl) == 2:
                adj[fl[0]].add(fl[1])
                adj[fl[1]].add(fl[0])
        seen = {0}
        stack = [0]
        while stack:
            x = stack.pop()
            for y in adj[x]:
                if y not in seen:
                    seen.add(y)
                    stack.append(y)
        if len(seen) != len(tris):
            return False, f"desconexo ({len(seen)}/{len(tris)} faces)"
        # Euler χ = V - E + F = 2
        chi = len(verts) - len(edge_count) + len(tris)
        if chi != 2:
            return False, f"χ={chi} (≠2)"
        return True, "ok"

    def _vertex_link_is_sphere(self, v):
        """Link de v = faces opostas a v nos tetraedros que contêm v (triângulos sem v)."""
        link = []
        for tid in self.vert2tet[v]:
            tet = self.tets[tid]
            link.append(frozenset(u for u in tet if u != v))
        return self._surface_is_sphere(link)

    def _spatial_slice_is_sphere(self, t):
        """Fatia espacial t = triângulos com os 3 vértices na fatia t."""
        tris = set()
        for f in self.tri2tet:
            if all(self.vt[u] == t for u in f):
                tris.add(f)
        return self._surface_is_sphere(tris)

    # ------------------------------------------------------------------
    # snapshot p/ teste de reversibilidade (combinatória pura)
    # ------------------------------------------------------------------
    def snapshot(self):
        return (frozenset(self.tets.values()),
                frozenset((v, self.vt[v]) for v in self.vt))

    # ==================================================================
    # MOVIMENTOS DE PACHNER 3D FOLIADOS
    # ==================================================================
    # Cada método de move retorna True (aplicado) ou False (precondição falhou).
    # Convenção: o validador check_manifold é o oráculo; aqui só checamos as
    # precondições estruturais suficientes p/ a combinatória ser bem-definida.

    def _apex(self, tid, tri):
        """O vértice do tetraedro tid que não está no triângulo tri."""
        for u in self.tets[tid]:
            if u not in tri:
                return u
        return None

    def spatial_triangles(self):
        """Triângulos espaciais (3 vértices na mesma fatia)."""
        out = []
        for f in self.tri2tet:
            it = iter(f)
            t0 = self.vt[next(it)]
            if all(self.vt[u] == t0 for u in f):
                out.append(f)
        return out

    # ---- (2,6): insere vértice numa fatia (na face espacial) -----------
    def move_26(self, tri):
        """tri: frozenset(3) espacial. Insere vértice central; 2 tetra → 6. ±4 tetra."""
        tset = self.tri2tet.get(tri)
        if not tset or len(tset) != 2:
            return False
        a, b, c = tuple(tri)
        if not (self.vt[a] == self.vt[b] == self.vt[c]):
            return False
        t = self.vt[a]
        t1, t2 = tuple(tset)
        p = self._apex(t1, tri)
        q = self._apex(t2, tri)
        # p,q em fatias t+1 e t-1 (ordem qualquer)
        tp = (t + 1) % self.T
        tm = (t - 1) % self.T
        if {self.vt[p], self.vt[q]} != {tp, tm}:
            return False
        up = p if self.vt[p] == tp else q
        dn = q if up is p else p
        # aplica
        self._del_tet(t1)
        self._del_tet(t2)
        x = self._new_vertex(t)
        for (i, j) in ((a, b), (b, c), (a, c)):
            self._add_tet((i, j, x, up))   # (3,1) p/ cima
            self._add_tet((i, j, x, dn))   # (1,3) p/ baixo
        return True

    # ---- (6,2): remove vértice de coordenação espacial 3 (inverso de 2,6) --
    def find_62(self, x):
        """Retorna (a,b,c,p,q) se x é removível por (6,2), senão None."""
        tets_x = self.vert2tet.get(x)
        if not tets_x or len(tets_x) != 6:
            return None
        t = self.vt[x]
        tp = (t + 1) % self.T
        tm = (t - 1) % self.T
        ups, downs = [], []
        neigh_t = set()
        for tid in tets_x:
            others = [u for u in self.tets[tid] if u != x]
            apex = [u for u in others if self.vt[u] != t]
            if len(apex) != 1:
                return None
            ap = apex[0]
            tneigh = [u for u in others if self.vt[u] == t]
            neigh_t.update(tneigh)
            if self.vt[ap] == tp:
                ups.append(ap)
            elif self.vt[ap] == tm:
                downs.append(ap)
            else:
                return None
        if len(ups) != 3 or len(downs) != 3:
            return None
        if len(set(ups)) != 1 or len(set(downs)) != 1:
            return None
        if len(neigh_t) != 3:
            return None
        a, b, c = tuple(neigh_t)
        if frozenset((a, b, c)) in self.tri2tet:
            return None  # {a,b,c} já existe → duplicação
        return (a, b, c, ups[0], downs[0])

    def move_62(self, x):
        info = self.find_62(x)
        if info is None:
            return False
        a, b, c, p, q = info
        for tid in list(self.vert2tet[x]):
            self._del_tet(tid)
        self._del_vertex(x)
        self._add_tet((a, b, c, p))
        self._add_tet((a, b, c, q))
        return True

    # ---- (4,4): flip de aresta espacial dentro de um sanduíche ---------
    def move_44(self, edge):
        """edge: frozenset(2) espacial. Flipa aresta {a,b}→{c,d}. Preserva N3."""
        a, b = tuple(edge)
        if self.vt[a] != self.vt[b]:
            return False
        # triângulos espaciais que contêm a aresta
        sp = [f for f in self.tri2tet if edge <= f and
              all(self.vt[u] == self.vt[a] for u in f)]
        if len(sp) != 2:
            return False
        c = next(iter(sp[0] - edge))
        d = next(iter(sp[1] - edge))
        if c == d:
            return False
        if frozenset((c, d)) in self.edge_set:
            return False  # aresta nova já existe → não-flippável
        # apices (cima/baixo) dos 2 triângulos espaciais
        t = self.vt[a]
        tp = (t + 1) % self.T
        tm = (t - 1) % self.T
        up_c = self._apices_dir(sp[0], tp)
        up_d = self._apices_dir(sp[1], tp)
        dn_c = self._apices_dir(sp[0], tm)
        dn_d = self._apices_dir(sp[1], tm)
        if None in (up_c, up_d, dn_c, dn_d):
            return False
        if up_c != up_d or dn_c != dn_d:
            return False  # apices não compartilhados → não é config (4,4)
        p, q = up_c, dn_c
        # remove os 4 tetra antigos, adiciona 4 novos
        old = [frozenset((a, b, c, p)), frozenset((a, b, d, p)),
               frozenset((a, b, c, q)), frozenset((a, b, d, q))]
        oldtids = []
        for ot in old:
            tid = self._tid_of(ot)
            if tid is None:
                return False
            oldtids.append(tid)
        for tid in oldtids:
            self._del_tet(tid)
        self._add_tet((a, c, d, p))
        self._add_tet((b, c, d, p))
        self._add_tet((a, c, d, q))
        self._add_tet((b, c, d, q))
        return True

    def _apices_dir(self, tri, t_target):
        """Apex (na direção t_target) do tetra que estende o triângulo espacial tri."""
        for tid in self.tri2tet.get(tri, ()):
            ap = self._apex(tid, tri)
            if self.vt[ap] == t_target:
                return ap
        return None

    def _tid_of(self, tet_frozen):
        """tid do tetraedro cujos vértices = tet_frozen (frozenset de 4), ou None."""
        tet = tuple(sorted(tet_frozen))
        # via interseção dos vert2tet
        vs = list(tet)
        cand = set(self.vert2tet.get(vs[0], ()))
        for v in vs[1:]:
            cand &= self.vert2tet.get(v, set())
        for tid in cand:
            if self.tets[tid] == tet:
                return tid
        return None

    # ---- (2,3): rearranjo em torno de triângulo tipo-tempo -------------
    def move_23(self, tri):
        """tri: frozenset(3) tipo-tempo (2+1). 2 tetra → 3 (em torno de nova aresta u-w)."""
        tset = self.tri2tet.get(tri)
        if not tset or len(tset) != 2:
            return False
        times = set(self.vt[u] for u in tri)
        if len(times) != 2:
            return False  # precisa ser tipo-tempo
        t1, t2 = tuple(tset)
        u = self._apex(t1, tri)
        w = self._apex(t2, tri)
        if u == w:
            return False
        # CDT: a aresta nova {u,w} deve ser TIPO-TEMPO (ápices em fatias distintas),
        # para NÃO modificar nenhuma fatia espacial (essas só mudam por (2,6)/(4,4)).
        if (self.vt[u] - self.vt[w]) % self.T not in (1, self.T - 1):
            return False
        if frozenset((u, w)) in self.edge_set:
            return False  # aresta u-w já existe
        x, y, z = tuple(tri)
        # nova triangulação da bipirâmide: 3 tetra compartilhando aresta {u,w}
        new = [(u, w, x, y), (u, w, y, z), (u, w, x, z)]
        # cada novo tetra deve ter exatamente 2 tempos consecutivos (folheação)
        for nt in new:
            ts = set(self.vt[v] for v in nt)
            if len(ts) != 2:
                return False
            aa, bb = sorted(ts)
            if (bb - aa) % self.T != 1 and (aa - bb) % self.T != 1:
                return False
        self._del_tet(t1)
        self._del_tet(t2)
        for nt in new:
            self._add_tet(nt)
        return True

    # ---- (3,2): inverso — colapsa aresta com anel de 3 tetra -----------
    def find_32(self, edge):
        """Retorna (u,w,x,y,z) se a aresta {u,w} tem o anel de 3 tetra, senão None."""
        u, w = tuple(edge)
        # CDT: só colapsa aresta TIPO-TEMPO (inverso do (2,3); arestas espaciais
        # são geridas por (6,2)/(4,4), não por (3,2)).
        if (self.vt[u] - self.vt[w]) % self.T not in (1, self.T - 1):
            return None
        ring = list(self.vert2tet.get(u, set()) & self.vert2tet.get(w, set()))
        if len(ring) != 3:
            return None
        opp = set()
        for tid in ring:
            others = [v for v in self.tets[tid] if v not in (u, w)]
            if len(others) != 2:
                return None
            opp.update(others)
        if len(opp) != 3:
            return None
        x, y, z = tuple(opp)
        if frozenset((x, y, z)) in self.tri2tet:
            return None  # triângulo {x,y,z} já existe → duplicação
        return (u, w, x, y, z)

    def move_32(self, edge):
        info = self.find_32(edge)
        if info is None:
            return False
        u, w, x, y, z = info
        # checa folheação dos 2 novos tetra
        for ap in (u, w):
            ts = set(self.vt[v] for v in (x, y, z, ap))
            if len(ts) != 2:
                return False
            aa, bb = sorted(ts)
            if (bb - aa) % self.T != 1 and (aa - bb) % self.T != 1:
                return False
        ring = list(self.vert2tet[u] & self.vert2tet[w])
        for tid in ring:
            self._del_tet(tid)
        self._add_tet((x, y, z, u))
        self._add_tet((x, y, z, w))
        return True

    # ==================================================================
    # MONTE CARLO (Metropolis, balanço detalhado via apply-then-undo)
    # ==================================================================
    # Ação 3D DINÂMICA: S = -k0*N0 + k3*N3 + eps*(N3-Vt)^2 (potencial de volume).
    # Proposta: 1 dos 5 tipos com prob 1/5; objeto uniforme entre os candidatos.
    # Razão de proposta q = T_reverso/T_forward calculada com contagens exatas
    # (antes/depois). Se rejeitado, desfaz com o movimento inverso VALIDADO —
    # zero derivação manual de deltas (o motor mantém as contagens sozinho).

    def _dS(self, dN0, dN3, k0, k3, eps, Vt):
        N3 = self.N3  # estado ATUAL (antes de aplicar) quando chamado nesse ponto
        dS_act = -k0 * dN0 + k3 * dN3
        dS_vol = eps * ((N3 + dN3 - Vt) ** 2 - (N3 - Vt) ** 2)
        return dS_act + dS_vol

    def mc_step(self, k0, k3, eps, Vt, stats=None):
        """Uma tentativa de movimento. Retorna o tipo tentado (str)."""
        rng = self.rng
        m = int(rng.integers(5))
        if m == 0:      # (2,6)
            return self._try_26(k0, k3, eps, Vt, stats)
        elif m == 1:    # (6,2)
            return self._try_62(k0, k3, eps, Vt, stats)
        elif m == 2:    # (4,4)
            return self._try_44(stats)
        elif m == 3:    # (2,3)
            return self._try_23(k0, k3, eps, Vt, stats)
        else:           # (3,2)
            return self._try_32(k0, k3, eps, Vt, stats)

    def _accept(self, q, dS):
        if q <= 0:
            return False
        a = q * math.exp(-dS)
        return a >= 1.0 or self.rng.random() < a

    def _bump(self, stats, key):
        if stats is not None:
            stats[key] = stats.get(key, 0) + 1

    def _try_26(self, k0, k3, eps, Vt, stats):
        self._bump(stats, 'try_26')
        if self.n_tri_spatial == 0:
            return '26'
        tri = self.spatial_set.sample(self.rng)
        n_st_before = self.n_tri_spatial
        dS = self._dS(+1, +4, k0, k3, eps, Vt)
        if not self.move_26(tri):
            return '26'
        # forward escolheu 1/n_st_before ; reverso (6,2) escolhe 1/N0_after
        q = n_st_before / self.N0          # N0 já é N0_after (vértice criado)
        if self._accept(q, dS):
            self._bump(stats, 'acc_26')
        else:
            x = self._next_vid - 1         # vértice recém-criado
            assert self.move_62(x), "undo (2,6) falhou"
        return '26'

    def _try_62(self, k0, k3, eps, Vt, stats):
        self._bump(stats, 'try_62')
        if self.N0 == 0:
            return '62'
        v = self.vertex_set.sample(self.rng)
        N0_before = self.N0
        info = self.find_62(v)
        if info is None:
            return '62'
        a, b, c, p, q_apex = info
        dS = self._dS(-1, -4, k0, k3, eps, Vt)
        assert self.move_62(v)
        # forward 1/N0_before ; reverso (2,6) escolhe 1/n_st_after
        q = N0_before / self.n_tri_spatial
        if self._accept(q, dS):
            self._bump(stats, 'acc_62')
        else:
            assert self.move_26(frozenset((a, b, c))), "undo (6,2) falhou"
        return '62'

    def _try_44(self, stats):
        self._bump(stats, 'try_44')
        if self.n_tri_spatial == 0:
            return '44'
        f = self.spatial_set.sample(self.rng)
        a, b, c = tuple(f)
        e = (frozenset((a, b)), frozenset((a, c)), frozenset((b, c)))[int(self.rng.integers(3))]
        # (4,4): dS=0, q=1 (n_st invariante) -> aceita sempre que aplicável
        if self.move_44(e):
            self._bump(stats, 'acc_44')
        return '44'

    def _try_23(self, k0, k3, eps, Vt, stats):
        self._bump(stats, 'try_23')
        if self.n_tri_timelike == 0:
            return '23'
        tri = self.timelike_set.sample(self.rng)
        n_tlt_before = self.n_tri_timelike
        dS = self._dS(0, +1, k0, k3, eps, Vt)
        # apexes p/ undo
        tset = self.tri2tet.get(tri)
        if not tset or len(tset) != 2:
            return '23'
        t1, t2 = tuple(tset)
        u = self._apex(t1, tri)
        w = self._apex(t2, tri)
        if not self.move_23(tri):
            return '23'
        # forward 1/n_tlt_before ; reverso (3,2) escolhe 1/n_edges_after
        q = n_tlt_before / self.n_edges
        if self._accept(q, dS):
            self._bump(stats, 'acc_23')
        else:
            assert self.move_32(frozenset((u, w))), "undo (2,3) falhou"
        return '23'

    def _try_32(self, k0, k3, eps, Vt, stats):
        self._bump(stats, 'try_32')
        if self.n_edges == 0:
            return '32'
        e = self.edge_set.sample(self.rng)
        n_edges_before = self.n_edges
        info = self.find_32(e)
        if info is None:
            return '32'
        u, w, x, y, z = info
        dS = self._dS(0, -1, k0, k3, eps, Vt)
        if not self.move_32(e):
            return '32'
        # forward 1/n_edges_before ; reverso (2,3) escolhe 1/n_tlt_after
        q = n_edges_before / self.n_tri_timelike
        if self._accept(q, dS):
            self._bump(stats, 'acc_32')
        else:
            assert self.move_23(frozenset((x, y, z))), "undo (3,2) falhou"
        return '32'

    def sweep(self, k0, k3, eps, Vt, n_steps=None, stats=None):
        """Um sweep = n_steps tentativas (default N3)."""
        if n_steps is None:
            n_steps = max(1, self.N3)
        for _ in range(n_steps):
            self.mc_step(k0, k3, eps, Vt, stats)


# ======================================================================
# GATE E0-3D (engenharia — ANTES de qualquer física)
# ======================================================================
def gate_E0_3d(verbose=True):
    """Filtro de engenharia do motor CDT 3D (F1b_PHASE_GATE §4). Ver síntese."""
    report = {}

    # E0a: configuração mínima contável (T=3) + invariantes
    g = CDT3D(3, seed=1)
    report['E0a_N3'] = g.N3
    report['E0a_N3_expected'] = 12 * 3
    report['E0a_N0'] = g.N0
    report['E0a_N0_expected'] = 4 * 3
    report['E0a_types'] = {str(k): v for k, v in g.count_types().items()}
    e = g.check_manifold()
    report['E0a_manifold_ok'] = (len(e) == 0)
    report['E0a_errs'] = e[:5]

    # E0b: manifold válido (link S², fatias S², Euler χ=0) em vários T
    ok_b = True
    for T in (3, 4, 5, 7):
        gg = CDT3D(T, seed=2)
        if gg.check_manifold():
            ok_b = False
    report['E0b_manifold_multi_T_ok'] = ok_b

    # E0c: invariantes preservados após 10^4 movimentos aleatórios (5 tipos)
    g2 = CDT3D(8, seed=3)
    rng = g2.rng
    for _ in range(200):  # cresce
        g2.move_26(g2.spatial_set.sample(rng))
    stats = {}
    NMOVES = 10000
    for _ in range(NMOVES):
        g2.mc_step(k0=1.0, k3=0.85, eps=0.0008, Vt=g2.N3, stats=stats)
    e2 = g2.check_manifold()
    report['E0c_moves'] = NMOVES
    report['E0c_manifold_ok'] = (len(e2) == 0)
    report['E0c_errs'] = e2[:5]
    report['E0c_types_balanced'] = (g2.count_types()[(3, 1)] == g2.count_types()[(1, 3)])

    # E0d: contadores incrementais == força-bruta (após os 10^4 moves)
    sp_bf = len(g2.spatial_triangles())
    tl_bf = sum(1 for f in g2.tri2tet if len(set(g2.vt[u] for u in f)) == 2)
    e_bf = len(g2.edges())
    report['E0d_counters_ok'] = (g2.n_tri_spatial == sp_bf and
                                 g2.n_tri_timelike == tl_bf and
                                 g2.n_edges == e_bf and
                                 len(g2.vertex_set) == g2.N0)

    # E0e: REVERSIBILIDADE de cada par de movimentos (combinatória bit-a-bit)
    rev = {}
    # (2,6)+(6,2)
    g3 = CDT3D(5, seed=4)
    for _ in range(20):
        g3.move_26(g3.spatial_set.sample(g3.rng))
    snap = g3.snapshot()
    tri = g3.spatial_set.sample(g3.rng)
    if g3.move_26(tri):
        x = g3._next_vid - 1
        rev['26_62'] = bool(g3.move_62(x) and g3.snapshot() == snap)
    # (4,4) auto-inverso
    g4 = CDT3D(5, seed=5)
    for _ in range(40):
        g4.move_26(g4.spatial_set.sample(g4.rng))
    rev['44'] = False
    for f in list(g4.spatial_set.items):
        a, b, c = tuple(f)
        for ed in (frozenset((a, b)), frozenset((a, c)), frozenset((b, c))):
            sp = [ff for ff in g4.tri2tet if ed <= ff and
                  all(g4.vt[u] == g4.vt[a] for u in ff)]
            if len(sp) != 2:
                continue
            cc = next(iter(sp[0] - ed))
            dd = next(iter(sp[1] - ed))
            snap4 = g4.snapshot()
            if g4.move_44(ed):
                rev['44'] = bool(g4.move_44(frozenset((cc, dd))) and g4.snapshot() == snap4)
                break
        if rev['44']:
            break
    # (2,3)+(3,2)
    g5 = CDT3D(5, seed=6)
    for _ in range(40):
        g5.move_26(g5.spatial_set.sample(g5.rng))
    rev['23_32'] = False
    for tri in list(g5.timelike_set.items):
        tset = g5.tri2tet.get(tri)
        if not tset or len(tset) != 2:
            continue
        t1, t2 = tuple(tset)
        u = g5._apex(t1, tri)
        w = g5._apex(t2, tri)
        snap5 = g5.snapshot()
        if g5.move_23(tri):
            rev['23_32'] = bool(g5.move_32(frozenset((u, w))) and g5.snapshot() == snap5)
            break
    report['E0e_reversibility'] = rev
    report['E0e_all_reversible'] = all(rev.get(k, False) for k in ('26_62', '44', '23_32'))

    # E0f: ergodicidade-sanity — todos os 5 tipos são aceitos; range de volume visitado
    report['E0f_accept_rates'] = {
        t: round(stats.get('acc_' + t, 0) / max(1, stats.get('try_' + t, 1)), 3)
        for t in ('26', '62', '44', '23', '32')}
    report['E0f_all_moves_fire'] = all(stats.get('acc_' + t, 0) > 0
                                       for t in ('26', '62', '44', '23', '32'))

    all_ok = (report['E0a_manifold_ok'] and report['E0b_manifold_multi_T_ok'] and
              report['E0c_manifold_ok'] and report['E0c_types_balanced'] and
              report['E0d_counters_ok'] and report['E0e_all_reversible'] and
              report['E0f_all_moves_fire'])
    report['E0_3D_GREEN'] = bool(all_ok)

    if verbose:
        print("=== GATE E0-3D (engenharia do motor CDT 3D) ===")
        for k, v in report.items():
            if k.endswith('errs') and not v:
                continue
            print(f"  {k}: {v}")
        print(f"  >>> E0-3D {'VERDE' if all_ok else 'VERMELHO'}")
    return report


if __name__ == "__main__":
    t0 = time.time()
    rep = gate_E0_3d(verbose=True)
    print(f"\n[tempo E0-3D: {time.time()-t0:.1f}s]")
    out = os.path.join(os.path.dirname(__file__), "e0_3d_report.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(rep, f, indent=2, default=str, ensure_ascii=False)
    print(f"[escrito: {out}]")
    sys.exit(0 if rep['E0_3D_GREEN'] else 1)
