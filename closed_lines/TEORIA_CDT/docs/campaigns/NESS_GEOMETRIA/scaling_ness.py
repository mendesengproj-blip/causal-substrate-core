"""scaling_ness.py -- NESS_GEOMETRIA: teste de escala sob NESS confirmado.

SÓ roda se Gates 1 E 2 passaram (PRE_REGISTRO §5). Pergunta: a geometria NESS escapa do
mean-field que matou Poisson, CSG e CDT-equilíbrio (CDT_TEIC_FERRO Pergunta B)?

Reusa VERBATIM: ferro_cdt.question_A/question_B (sonda O(3), χ_max~N^x, U4 crossing,
ξ_g/L) e cdt_substrate.cdt_skeleton_graph (1-esqueleto -> Graph do TEIC). A ÚNICA mudança
vs CDT_TEIC_FERRO é o SUBSTRATO: snapshots ESTROBOSCÓPICOS de geometria DIRIGIDA (NESS) em
vez de geometria de equilíbrio. Overlay direto sobre a curva CDT-equilíbrio (N^0.24).

Disciplina (lição CDT_TEIC_FERRO): MUITOS snapshots p/ média de desordem (4 seeds ->
noise-dominated). Ambíguo = NÃO-RESOLVIDO.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
# CDT_TEIC_FERRO p/ ferro_cdt + cdt_substrate (sonda O(3) verbatim)
FERRO = HERE.parents[3] / "TEIC" / "docs" / "campaigns" / "CDT_TEIC_FERRO"
sys.path.insert(0, str(FERRO))

from driven_cdt import build_driven, driven_run                              # noqa: E402
from cdt_substrate import cdt_skeleton_graph                                 # noqa: E402
from ferro_cdt import question_A, question_B                                 # noqa: E402

K0_BAR, A, P = 2.5, 1.5, 8          # NESS confirmado (Gate 2 smoke: histerese máx ~P=12; P=8 não-adiab.)
T = 10


def build_ness_ladder(volumes, n_snapshots, therm, drive_burn_cycles, snap_gap_cycles):
    """Para cada volume, gera n_snapshots grafos = 1-esqueletos de snapshots
    ESTROBOSCÓPICOS (fase 0) de geometria DIRIGIDA em NESS, espaçados por snap_gap_cycles
    ciclos (decorrelação). Retorna ladder {Vt: (graphs, infos)} no formato de ferro_cdt."""
    ladder = {}
    for Vt in volumes:
        graphs, infos = [], []
        seed = 0
        while len(graphs) < n_snapshots:
            seed += 1
            g, k3 = build_driven(K0_BAR, T, Vt, seed=900 + 7 * seed + int(Vt), therm=therm)
            # burn do transiente sob drive (entra no NESS)
            driven_run(g, k3, K0_BAR, A, P, Vt, drive_burn_cycles * P, seed_meas=seed)
            # coleta alguns snapshots estroboscópicos desta corrida (decorrelados)
            n_per_run = 3
            for _ in range(n_per_run):
                if len(graphs) >= n_snapshots:
                    break
                # avança snap_gap_cycles ciclos e fotografa na fase 0 (fim de ciclo completo)
                driven_run(g, k3, K0_BAR, A, P, Vt, snap_gap_cycles * P, seed_meas=seed)
                G, times, frac_sp = cdt_skeleton_graph(g)
                graphs.append(G)
                infos.append({"N0": int(g.N0), "N3": int(g.N3),
                              "z_mean": float(G.degree.mean()),
                              "frac_links_spatial": float(frac_sp), "k0_bar": K0_BAR})
        ladder[Vt] = (graphs, infos)
        print(f"    [NESS Vt={Vt}] N0~{np.mean([i['N0'] for i in infos]):.0f} "
              f"<z>={np.mean([i['z_mean'] for i in infos]):.1f} "
              f"frac_sp={np.mean([i['frac_links_spatial'] for i in infos]):.2f} "
              f"({len(graphs)} snapshots)", flush=True)
    return ladder


def main():
    smoke = "--smoke" in sys.argv
    t0 = time.time()
    if smoke:
        volumes = [1500, 3000]
        n_snap, therm, burn_c, gap_c = 6, 60, 6, 3
        Js = [0.12, 0.18, 0.22, 0.30]
    else:
        # therm=140 MATCHED ao baseline de equilíbrio (CDT_TEIC_FERRO/cdt_substrate) p/ overlay
        # JUSTO: só o drive NESS difere; a classe de universalidade é governada pela estrutura
        # de alto-z do grafo, estabelecida cedo. burn_c sob drive entra no NESS. n_snap=10 (>4
        # do baseline, lição do ruído de χ).
        volumes = [1500, 3000, 6000]
        n_snap, therm, burn_c, gap_c = 10, 140, 12, 4
        Js = [0.10, 0.13, 0.16, 0.18, 0.20, 0.22, 0.25, 0.28]
    out = {"config": {"K0_BAR": K0_BAR, "A": A, "P": P, "T": T, "volumes": volumes,
                      "n_snapshots": n_snap, "Js": Js, "substrate": "NESS-driven stroboscopic"}}
    print(f"=== ESCALA sob NESS (k0_bar={K0_BAR}, A={A}, P={P}) ===", flush=True)
    print("  overlay alvo: CDT-equilíbrio chi_max~N^0.24 (lean MF); Poisson N^0.07; geom-3D ~0.66",
          flush=True)
    ladder = build_ness_ladder(volumes, n_snap, therm, burn_c, gap_c)
    out["A_reproduction"] = question_A(ladder, K0_BAR)
    out["B_universality"] = question_B(ladder, K0_BAR, Js)
    out["runtime_s"] = round(time.time() - t0, 1)
    # veredito de escala (mesma régua de CDT_TEIC_FERRO)
    x = out["B_universality"]["chi_max_exponent"]
    out["escapes_mean_field"] = bool(x > 0.55)
    out["mean_field_like"] = bool(x <= 0.5)
    name = "scaling_ness_smoke.json" if smoke else "scaling_ness.json"
    (HERE / name).write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(f"\n>>> ESCALA NESS: chi_max~N^{x:.2f} "
          f"(escapa_MF={out['escapes_mean_field']}, MF-like={out['mean_field_like']}) "
          f"[{out['runtime_s']:.0f}s] -> {name}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
