"""n5_phase1.py -- N5/M2 main measurement, TORUS + TRANSPORTER instrument
(PRE_REGISTRO.md + addendum).

Per seed: channels A and B on the spatial-torus Hasse substrate with
per-link transporters; fits of BARE tree (U==1, the SC1 cosine), RELAXED
tree (medium-dressed classical response -- used by Q(J)), and loop
(1/2 delta-logdet at the relaxed config); a4 per channel.

Aggregation: s4 = a4_loop per node; c_S_loop = s4_A/9; c_K_loop =
(s4_B - s4_A)/6; tree comparators (bare and relaxed); stability rule
(drop two largest g); a_eff.  Sizes L in {6, 8}, 8 seeds each; periodic
cubic control.  Death arithmetic lives in n5_phase2.py.
"""

from __future__ import annotations

import time

import numpy as np

import n5_core as core

RHO, TMAX = 2.0, 4.0
GS = [0.04, 0.06, 0.08, 0.12, 0.16, 0.20, 0.24]
SIZES = [(6.0, 8), (8.0, 8)]
CUBIC_L = 8


def fits_from_rows(rows, gs):
    out = {}
    for key, name in (("tree_bare_per_node", "tree_bare"),
                      ("tree_per_node", "tree"),
                      ("loop_per_node", "loop")):
        ys = [r[key] for r in rows]
        out[name] = core.fit_even(gs, ys)
        out[f"{name}_stab_a4"] = core.fit_even(gs[:-2], ys[:-2])["a4"]
    return out


def run_seed(seed, L):
    rng = np.random.default_rng(seed)
    pts = core.sprinkle(rng, RHO, TMAX, L)
    edges = core.causal_links_torus(pts, L)
    deltas = core.link_deltas_torus(pts, edges, L)
    out = {"seed": int(seed), "L": float(L), "n": int(pts.shape[0]),
           "n_links": int(edges.shape[0]),
           "a_eff": float(np.mean(np.linalg.norm(deltas, axis=1)))}
    t0 = time.time()
    vac_ld = None
    for ch in ("A", "B"):
        res = core.measure_channel_tw(pts, edges, deltas, L, GS, ch,
                                      vac_logdet=vac_ld)
        vac_ld = res["vac_logdet"]
        out[f"rows_{ch}"] = res["rows"]
        out[f"fits_{ch}"] = fits_from_rows(res["rows"], GS)
    out["seconds"] = time.time() - t0
    return out


def run_cubic():
    edges, deltas = core.cubic_grid_torus(CUBIC_L)
    n = CUBIC_L ** 3
    pts = np.zeros((n, 4))                    # placeholder (not used by _tw)
    out = {"L": CUBIC_L, "n": n, "n_links": int(edges.shape[0]), "a_eff": 1.0}
    vac_ld = None
    for ch in ("A", "B"):
        res = core.measure_channel_tw(pts, edges, deltas, float(CUBIC_L), GS,
                                      ch, vac_logdet=vac_ld)
        vac_ld = res["vac_logdet"]
        out[f"rows_{ch}"] = res["rows"]
        out[f"fits_{ch}"] = fits_from_rows(res["rows"], GS)
    return out


def aggregate(seed_rows):
    a4A = np.array([s["fits_A"]["loop"]["a4"] for s in seed_rows])
    a4B = np.array([s["fits_B"]["loop"]["a4"] for s in seed_rows])
    e4A = np.array([s["fits_A"]["tree"]["a4"] for s in seed_rows])
    e4B = np.array([s["fits_B"]["tree"]["a4"] for s in seed_rows])
    b4A = np.array([s["fits_A"]["tree_bare"]["a4"] for s in seed_rows])
    b4B = np.array([s["fits_B"]["tree_bare"]["a4"] for s in seed_rows])
    a4A_s = np.array([s["fits_A"]["loop_stab_a4"] for s in seed_rows])
    a4B_s = np.array([s["fits_B"]["loop_stab_a4"] for s in seed_rows])

    def stats(v):
        return {"mean": float(v.mean()),
                "sem": float(v.std(ddof=1) / np.sqrt(len(v))) if len(v) > 1 else 0.0}

    return {
        "n_seeds": len(seed_rows),
        "loop_a4_A": stats(a4A), "loop_a4_B": stats(a4B),
        "tree_e4_A": stats(e4A), "tree_e4_B": stats(e4B),
        "bare_e4_A": stats(b4A), "bare_e4_B": stats(b4B),
        "bare_ratio_BA": stats(b4B / b4A),
        "tree_ratio_BA": stats(e4B / e4A),
        "loop_ratio_BA": stats(a4B / a4A),
        "c_S_loop": stats(a4A / 9.0),
        "c_K_loop": stats((a4B - a4A) / 6.0),
        "stability_shift_A": stats(a4A_s - a4A),
        "stability_shift_B": stats(a4B_s - a4B),
        "a_eff": stats(np.array([s["a_eff"] for s in seed_rows])),
    }


def main():
    payload = {"gs": GS, "rho": RHO, "tmax": TMAX, "instrument": "torus+transporters"}
    for L, n_seeds in SIZES:
        rows = []
        for k in range(n_seeds):
            seed = 31_000 + 100 * int(L) + k
            print(f"L={L} seed {seed} ...", flush=True)
            r = run_seed(seed, L)
            print(f"  n={r['n']} links={r['n_links']} {r['seconds']:.0f}s "
                  f"loop_a4 A={r['fits_A']['loop']['a4']:.5g} "
                  f"B={r['fits_B']['loop']['a4']:.5g} "
                  f"tree_a4 A={r['fits_A']['tree']['a4']:.5g} "
                  f"B={r['fits_B']['tree']['a4']:.5g}", flush=True)
            rows.append(r)
        payload[f"seeds_L{int(L)}"] = rows
        payload[f"agg_L{int(L)}"] = aggregate(rows)
        agg = payload[f"agg_L{int(L)}"]
        print(f"AGG L={L}: cK_loop={agg['c_K_loop']} cS_loop={agg['c_S_loop']} "
              f"bare_BA={agg['bare_ratio_BA']['mean']:.4f} "
              f"tree_BA={agg['tree_ratio_BA']['mean']:.4f}", flush=True)
    print("cubic control ...", flush=True)
    cub = run_cubic()
    payload["cubic"] = cub
    print("cubic loop a4 A/B:", cub["fits_A"]["loop"]["a4"],
          cub["fits_B"]["loop"]["a4"], flush=True)
    core.save_json("n5_phase1.json", payload)
    print("saved n5_phase1.json")


if __name__ == "__main__":
    main()
