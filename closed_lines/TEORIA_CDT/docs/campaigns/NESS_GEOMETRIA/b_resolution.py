"""b_resolution.py -- resolve a Pergunta B: o expoente de chi_max escala com a amplitude A do drive?

Pré-registro: B_RESOLUTION_PREREG.md (congelado). Discriminante decisivo e barato: x(A).
- ESCAPE: x(A) cresce monotonicamente com A E deriva de J_c diminui com A.
- MF: x(A) plano/disperso, J_c segue derivando -> fecha o programa de escala.
A=0 = controle de equilíbrio embutido (deve dar x~0.24 do CDT-equilíbrio).

Reusa driven_cdt (drive), cdt_substrate (1-esqueleto) e ferro_cdt.question_B (suíte O(3)) verbatim.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
FERRO = HERE.parents[3] / "TEIC" / "docs" / "campaigns" / "CDT_TEIC_FERRO"
sys.path.insert(0, str(FERRO))

from driven_cdt import build_driven, driven_run                 # noqa: E402
from cdt_substrate import cdt_skeleton_graph                    # noqa: E402
from ferro_cdt import question_B                                # noqa: E402

K0_BAR, P, T = 2.5, 8, 10


def build_ladder_A(A, volumes, n_snap, therm, burn_c, gap_c):
    """Ladder {Vt:(graphs,infos)} de snapshots estroboscópicos sob drive de amplitude A.
    A=0 -> geometria de equilíbrio (controle). Formato de ferro_cdt.question_B."""
    ladder = {}
    for Vt in volumes:
        graphs, infos = [], []
        seed = 0
        while len(graphs) < n_snap:
            seed += 1
            g, k3 = build_driven(K0_BAR, T, Vt, seed=1300 + 7 * seed + int(Vt), therm=therm)
            driven_run(g, k3, K0_BAR, A, P, Vt, burn_c * P, seed_meas=seed)   # entra no NESS
            for _ in range(3):
                if len(graphs) >= n_snap:
                    break
                driven_run(g, k3, K0_BAR, A, P, Vt, gap_c * P, seed_meas=seed)
                G, times, frac_sp = cdt_skeleton_graph(g)
                graphs.append(G)
                infos.append({"N0": int(g.N0), "z_mean": float(G.degree.mean())})
        ladder[Vt] = (graphs, infos)
        print(f"    [A={A} Vt={Vt}] N0~{np.mean([i['N0'] for i in infos]):.0f} "
              f"<z>={np.mean([i['z_mean'] for i in infos]):.1f} ({len(graphs)} snap)", flush=True)
    return ladder


def main():
    smoke = "--smoke" in sys.argv
    t0 = time.time()
    if smoke:
        As = [0.0, 1.5]
        volumes = [1200, 2400]
        n_snap, therm, burn_c, gap_c = 5, 80, 6, 3
        Js = [0.14, 0.18, 0.22, 0.27]
    else:
        # n_snap=10 (= statistics da scaling_ness principal); 4 amplitudes p/ TENDÊNCIA x(A)
        # (robusta a ruído, ao contrário de 1 expoente isolado). A=0 = controle de equilíbrio.
        As = [0.0, 0.75, 1.5, 2.25]
        volumes = [1500, 3000, 6000]
        n_snap, therm, burn_c, gap_c = 10, 140, 10, 4
        Js = [0.13, 0.16, 0.18, 0.20, 0.22, 0.25]
    out = {"config": {"K0_BAR": K0_BAR, "P": P, "T": T, "As": As, "volumes": volumes,
                      "n_snap": n_snap, "Js": Js}, "by_A": {}}
    print(f"=== B-RESOLUTION: varredura de amplitude x(A) (k0_bar={K0_BAR}, P={P}) ===", flush=True)
    for A in As:
        print(f"\n###### A = {A} {'(EQUILÍBRIO/controle)' if A==0 else ''} ######", flush=True)
        ladder = build_ladder_A(A, volumes, n_snap, therm, burn_c, gap_c)
        B = question_B(ladder, K0_BAR, Js)
        out["by_A"][str(A)] = {"x": B["chi_max_exponent"], "Jc_per_size": B["Jc_per_size"],
                               "Jc_drift": B["Jc_drift"],
                               "chi_max": [B["per_size"][str(v)]["chi_max"] for v in volumes],
                               "N0": [B["per_size"][str(v)]["N0"] for v in volumes]}
    # análise: x(A) cresce? J_c-drift diminui?
    As_arr = np.array(As)
    xs = np.array([out["by_A"][str(a)]["x"] for a in As])
    drifts = np.array([out["by_A"][str(a)]["Jc_drift"] for a in As])
    # tendência de x com A (regressão; >0 e monotônica = mecanístico)
    x_slope = float(np.polyfit(As_arr, xs, 1)[0]) if len(As) > 1 else float("nan")
    monotonic = bool(np.all(np.diff(xs) > -0.03))   # cresce (tolera ruído pequeno)
    drift_shrinks = bool(abs(drifts[-1]) < abs(drifts[0])) if len(As) > 1 else False
    out["analysis"] = {"x_vs_A": list(zip([float(a) for a in As], [float(x) for x in xs])),
                       "x_slope_per_A": x_slope, "x_monotonic_up": monotonic,
                       "Jc_drift_vs_A": list(zip([float(a) for a in As],
                                                 [float(d) for d in drifts])),
                       "Jc_drift_shrinks_with_A": drift_shrinks,
                       "x_at_equilibrium_A0": float(xs[0]),
                       "x_at_max_A": float(xs[-1])}
    # veredito pré-registrado
    escape = bool(monotonic and x_slope > 0.05 and xs[-1] > 0.55 and drift_shrinks)
    mean_field = bool((not monotonic or x_slope < 0.03) and xs.max() < 0.6)
    out["verdict"] = ("ESCAPE" if escape else ("MEAN_FIELD" if mean_field else "AINDA_AMBIGUO"))
    out["runtime_s"] = round(time.time() - t0, 1)
    name = "b_resolution_smoke.json" if smoke else "b_resolution.json"
    (HERE / name).write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(f"\n=== x(A) = {[(round(a,2),round(float(x),3)) for a,x in zip(As,xs)]} ===", flush=True)
    print(f"    x_slope/A={x_slope:+.3f} monotonic_up={monotonic}  "
          f"Jc_drift={[round(float(d),3) for d in drifts]} shrinks={drift_shrinks}", flush=True)
    print(f">>> VEREDITO B: {out['verdict']} [{out['runtime_s']:.0f}s] -> {name}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
