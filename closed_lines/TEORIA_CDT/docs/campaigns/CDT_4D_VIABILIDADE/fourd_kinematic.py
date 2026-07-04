"""fourd_kinematic.py -- PARTE B: gatilho cinemático 4D (pentatopes), SEM ação.

Autorizado pela morte §6 da Parte A (NESS_GEOMETRIA: escala=MF, resolvida por x(A)).
Pré-registro: ../NESS_GEOMETRIA/B_RESOLUTION_PREREG.md + prompt Parte B. Generaliza o
gatilho 3D (TEIC/CDT_VIABILIDADE/cdt_kinematics.py) para 4-simplexos (pentatopes), reusando
rs_clustering.clustering_metrics VERBATIM para transitividade + C4.

ENSEMBLE: stacked (1,5) -- a ÚNICA classe 4D PROVAVELMENTE-CORRETA SEM validador de
manifold S^3: o move (1,5) subdivide UM 4-simplexo em 5 (adiciona vértice central), o que
preserva trivialmente a 4-variedade fechada. Logo NÃO há risco de move bugado (a disciplina
de integridade do programa: nunca forjar engine não-validado). Sanidade barata: todo
tetraedro (3-face) em EXATAMENTE 2 pentatopes (pseudomanifold) + Euler χ(S^4)=2.

PERGUNTA (prompt Parte B §2): ⟨z⟩(N) diverge como Poisson, ou satura (finito)? o
discriminador de clustering é trivial/MF ou não?
  - NÃO ARMADO: z diverge tipo-Poisson OU clustering trivial/MF.
  - ARMADO (autoriza, NÃO executa, o motor dinâmico 4D): z finito + clustering não-trivial.

ANTI-CIRCULARIDADE: aresta FIXA por construção; só contagens combinatórias adimensionais.
RESSALVA pré-declarada: stacked é o regime APOLLONIANO/não-genérico (em 2D o Gatilho 3
distinguiu stacked de flipped/DT; o flipped exige (3,3)/(2,4)+validador S^3 = a campanha
F1b-4D separada, NÃO construída aqui). Logo clustering alto no stacked é NECESSÁRIO, não
suficiente -- a mesma ressalva do Gatilho 3 3D.
"""
from __future__ import annotations

import itertools
import json
import sys
import time
from collections import defaultdict
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RS = HERE.parents[3] / "TEIC" / "docs" / "campaigns" / "RIDEOUT_SORKIN_CLUSTERING"
sys.path.insert(0, str(RS))
import rs_clustering as rc            # noqa: E402  (clustering_metrics: transitivity + C4)


class Triangulation4D:
    """Triangulação 4D fechada (S^4) por stacking (1,5). Pentatopo = frozenset de 5 vids.
    1-esqueleto = vértices + arestas. Seed = ∂(5-simplex) = K6 (6 pentatopes, S^4)."""

    def __init__(self):
        self.nverts = 6
        self.pents = {}                       # pid -> frozenset(5 vids)
        self.tet_pents = defaultdict(set)     # frozenset(4 vids) -> {pids}
        self.edge_set = set()                 # frozenset(2 vids)
        self._next = 0
        # ∂(5-simplex on {0..5}) = 6 facets, cada um omite 1 vértice
        for omit in range(6):
            self._add_pent(frozenset(v for v in range(6) if v != omit))

    def _add_pent(self, verts):
        pid = self._next; self._next += 1
        fs = frozenset(verts)
        self.pents[pid] = fs
        for tet in itertools.combinations(sorted(fs), 4):
            self.tet_pents[frozenset(tet)].add(pid)
        for e in itertools.combinations(sorted(fs), 2):
            self.edge_set.add(frozenset(e))
        return pid

    def _del_pent(self, pid):
        fs = self.pents.pop(pid)
        for tet in itertools.combinations(sorted(fs), 4):
            s = self.tet_pents[frozenset(tet)]; s.discard(pid)
            if not s:
                del self.tet_pents[frozenset(tet)]

    def move_15(self, rng):
        """(1,5): adiciona vértice central w num pentatopo {a,b,c,d,e} -> 5 pentatopes."""
        pid = int(rng.integers(self._next)) if False else rng.choice(list(self.pents.keys()))
        verts = sorted(self.pents[pid])
        w = self.nverts; self.nverts += 1
        self._del_pent(pid)
        for i in range(5):
            new = [verts[j] for j in range(5) if j != i] + [w]
            self._add_pent(frozenset(new))
        # arestas w-vi (as faces internas reconstroem o resto; edge_set é set global)
        for v in verts:
            self.edge_set.add(frozenset((w, v)))

    def one_skeleton_edges(self):
        return [tuple(e) for e in self.edge_set]

    def z(self):
        return 2.0 * len(self.edge_set) / self.nverts

    # --- sanidade barata (pseudomanifold + Euler), SEM link-S^3 (não necessário p/ stacked) ---
    def pseudomanifold_ok(self):
        return all(len(s) == 2 for s in self.tet_pents.values())

    def euler_chi(self):
        """χ(S^4)=2: V - E + F2 - F3 + F4. Conta i-faces distintas dos pentatopes."""
        faces = [set() for _ in range(5)]
        for fs in self.pents.values():
            sv = sorted(fs)
            for k in range(1, 6):
                for c in itertools.combinations(sv, k):
                    faces[k - 1].add(c)
        V, E, F2, F3, F4 = (len(f) for f in faces)
        return V - E + F2 - F3 + F4


def grow_to(n, rng):
    T = Triangulation4D()
    while T.nverts < n:
        T.move_15(rng)
    return T


def validation_gate(verbose=True):
    rep = {"checks": [], "passed": True}

    def chk(name, ok, detail):
        rep["checks"].append({"name": name, "ok": bool(ok), "detail": detail})
        rep["passed"] = rep["passed"] and ok
        if verbose:
            print(f"  [{'OK' if ok else 'FAIL'}] {name}: {detail}")

    # (1) seed = K6: z=5, transitivity=1, C4=1
    T = Triangulation4D()
    m = rc.clustering_metrics(T.nverts, T.one_skeleton_edges())
    chk("seed ∂(5-simplex)=K6 (z=5, C_tri=1, C4=1)",
        abs(T.z() - 5) < 1e-9 and abs(m["transitivity"] - 1) < 1e-9,
        f"z={T.z():.2f} C_tri={m['transitivity']:.4f} C4={m['mean_local_square']:.4f}")
    chk("seed pseudomanifold (todo tet em 2 pentatopes) + χ=2",
        T.pseudomanifold_ok() and T.euler_chi() == 2,
        f"pmf={T.pseudomanifold_ok()} χ={T.euler_chi()}")
    # (2) após 200 moves (1,5): pseudomanifold + χ=2 preservados (S^4)
    rng = np.random.default_rng(7)
    T = grow_to(206, rng)
    chk("após (1,5)×200: pseudomanifold + χ(S^4)=2",
        T.pseudomanifold_ok() and T.euler_chi() == 2,
        f"N={T.nverts} pmf={T.pseudomanifold_ok()} χ={T.euler_chi()}")
    # (3) z analítico: stacked (1,5) tem z=(30+10k)/(6+k) -> 10
    k = T.nverts - 6
    z_pred = (30 + 10 * k) / (6 + k)
    chk("z bate fórmula stacked (30+10k)/(6+k)", abs(T.z() - z_pred) < 1e-9,
        f"z={T.z():.4f} pred={z_pred:.4f}")
    return rep


LADDER = [50, 100, 200, 400, 800, 1600, 3200]
N_SEEDS = 4
POISSON_C4 = 0.029     # piso mean-field (ref. Gatilho 1/2, prompt Parte B)


def run_measurement():
    out = {"observable": "z + (transitivity,C4) no 1-esqueleto de ensemble (1,5) 4D stacked",
           "edge": "FIXA [External]", "ladder": LADDER, "rows": []}
    for n in LADDER:
        zs, tr, c4 = [], [], []
        t0 = time.perf_counter()
        ns = N_SEEDS if n <= 400 else 2
        for s in range(ns):
            rng = np.random.default_rng(900 + s + n)
            T = grow_to(n, rng)
            m = rc.clustering_metrics(T.nverts, T.one_skeleton_edges())
            zs.append(T.z()); tr.append(m["transitivity"]); c4.append(m["mean_local_square"])
        dt = time.perf_counter() - t0
        out["rows"].append({"N": n, "n_seeds": ns,
                            "z": float(np.mean(zs)), "z_sem": float(np.std(zs) / np.sqrt(ns)),
                            "C_trans": float(np.mean(tr)), "C4": float(np.mean(c4)),
                            "runtime_s": round(dt, 1)})
        print(f"  N={n:>4}: z={np.mean(zs):.3f} C_tri={np.mean(tr):.4f} C4={np.mean(c4):.4f} "
              f"[{dt:.1f}s]", flush=True)
    rows = out["rows"]
    z = np.array([r["z"] for r in rows]); Nv = np.array([r["N"] for r in rows], float)
    C4 = np.array([r["C4"] for r in rows]); Ct = np.array([r["C_trans"] for r in rows])
    out["z_slope_top"] = float(np.diff(z)[-1] / np.diff(np.log(Nv))[-1])
    out["z_saturates"] = bool(abs(out["z_slope_top"]) / z[-1] < 0.05)
    out["z_diverges_poisson_like"] = bool(out["z_slope_top"] / z[-1] > 0.10)
    out["C4_first"] = float(C4[0]); out["C4_top"] = float(C4[-1])
    out["C_trans_first"] = float(Ct[0]); out["C_trans_top"] = float(Ct[-1])
    out["C4_above_MF"] = bool(C4[-1] > 1.5 * POISSON_C4)
    # expoente de decaimento do clustering: C4 ~ N^p (p<0 = DECAI rumo ao MF; ~0 = SATURA)
    out["C4_exponent"] = float(np.polyfit(np.log(Nv), np.log(C4), 1)[0])
    out["Ctrans_exponent"] = float(np.polyfit(np.log(Nv), np.log(Ct), 1)[0])
    # clustering "vivo" = NÃO decaindo (satura num valor não-trivial, como o 3D flipped C4~0.145)
    out["clustering_saturates"] = bool(out["C4_exponent"] > -0.1)
    out["clustering_decays_to_MF"] = bool(out["C4_exponent"] < -0.1)
    return out


def main():
    t0 = time.time()
    print("=" * 64 + "\nGATE DE VALIDAÇÃO (4D kinematic, stacked (1,5))\n" + "=" * 64)
    g = validation_gate()
    print(f"  GATE {'VERDE' if g['passed'] else 'VERMELHO'}")
    out = {"gate": g}
    if not g["passed"]:
        (HERE / "fourd_kinematic.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
        print("ABORTA (gate vermelho)."); return 1
    print("\n" + "=" * 64 + "\nMEDIÇÃO: z e clustering no 1-esqueleto 4D\n" + "=" * 64)
    meas = run_measurement()
    out["measurement"] = meas
    # veredito pré-registrado (mesma régua do Gatilho 3 3D): ARMA só se z satura E o clustering
    # SATURA num valor não-trivial (não basta C4_top>MF num ponto; tem que NÃO decair, como o
    # 3D flipped que saturou em C4~0.145). Clustering decaindo rumo ao MF = NÃO ARMADO.
    armed = bool(meas["z_saturates"] and meas["clustering_saturates"] and meas["C4_above_MF"])
    out["verdict"] = "ARMADO" if armed else "NAO_ARMADO"
    out["caveat"] = ("stacked é o regime APOLLONIANO não-genérico; clustering alto é NECESSÁRIO "
                     "não suficiente. O discriminante real (flipped/DT) exige (3,3)/(2,4)+validador "
                     "S^3 = campanha F1b-4D separada, NÃO construída aqui.")
    out["runtime_s"] = round(time.time() - t0, 1)
    (HERE / "fourd_kinematic.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
    print("\n" + "=" * 64)
    print(f"  z: {meas['rows'][0]['z']:.2f}->{meas['rows'][-1]['z']:.2f} "
          f"(satura={meas['z_saturates']}, diverge-Poisson={meas['z_diverges_poisson_like']})")
    print(f"  C4: {meas['C4_first']:.3f}->{meas['C4_top']:.3f} (expoente N^{meas['C4_exponent']:.2f}; "
          f"satura={meas['clustering_saturates']}, decai-p/-MF={meas['clustering_decays_to_MF']})")
    print(f"  C_trans: {meas['C_trans_first']:.3f}->{meas['C_trans_top']:.3f} "
          f"(N^{meas['Ctrans_exponent']:.2f})")
    print(f"  >>> GATILHO 4D: {out['verdict']}  [{out['runtime_s']:.0f}s]")
    print(f"  RESSALVA: {out['caveat']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
