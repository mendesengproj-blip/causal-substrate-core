"""n2_phase1.py -- N2 Phase 1: does the horizon-molecule count obey the area law?

Pre-registered grids, counts and criteria: PRE_REGISTRO.md.  No MC here -- the
counts are deterministic per seed; errors are SEM over seeds.
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import n2_core as nc

HERE = Path(__file__).resolve().parent

D4 = {"rho": 8.0, "tx": 2.5, "Ls": [1.5, 2.0, 3.0, 4.0], "seeds": 12}
D4_TCHECK = {"L": 3.0, "txs": [2.0, 2.5, 3.5]}
D3 = {"rho": 10.0, "tx": 3.0, "Ls": [2.0, 3.0, 4.0, 6.0, 8.0], "seeds": 12}
D2 = {"rhos": [10.0, 20.0, 40.0, 80.0], "tx": 4.0, "seeds": 16}


def stats(vals):
    v = np.asarray(vals, float)
    sem = float(v.std(ddof=1) / np.sqrt(len(v))) if len(v) > 1 else 0.0
    return float(v.mean()), sem


def scan_L(d, cfg, tag):
    print(f"\n[{tag}] d={d}, rho={cfg['rho']}, tx=+-{cfg['tx']}")
    out = {}
    for L in cfg["Ls"]:
        res = [nc.run_point(cfg["rho"], cfg["tx"], L, d, s)
               for s in range(cfg["seeds"])]
        row = {}
        for key in ("N_rel", "N_link", "N_mol"):
            row[key] = stats([r[key] for r in res])
        row["n"] = float(np.mean([r["n"] for r in res]))
        out[L] = row
        print(f"  L={L:4.1f} (n~{row['n']:6.0f}): "
              f"N_mol={row['N_mol'][0]:8.2f}+-{row['N_mol'][1]:.2f}  "
              f"N_link={row['N_link'][0]:9.1f}+-{row['N_link'][1]:.1f}  "
              f"N_rel={row['N_rel'][0]:10.0f}")
    return out


def main():
    t0 = time.time()
    print("=" * 74)
    print("N2 Phase 1 -- Rindler corner counts vs area (pre-registered grids)")
    print("=" * 74)
    payload = {"campaign": "N2_ENTROPIA_HORIZONTE", "stage": "phase1"}

    # ---- d=4 ---- #
    r4 = scan_L(4, D4, "1")
    Ls = D4["Ls"]
    mol_m = [r4[L]["N_mol"][0] for L in Ls]
    mol_e = [r4[L]["N_mol"][1] for L in Ls]
    s4, s4e = nc.loglog_slope(Ls, mol_m, mol_e)
    l4, l4e = nc.loglog_slope(Ls, [r4[L]["N_link"][0] for L in Ls],
                              [r4[L]["N_link"][1] for L in Ls])
    rel4, _ = nc.loglog_slope(Ls, [r4[L]["N_rel"][0] for L in Ls])
    print(f"  -> slopes vs L: N_mol {s4:.3f}+-{s4e:.3f} (area=2)  "
          f"N_link {l4:.3f}+-{l4e:.3f}  N_rel {rel4:.3f}")

    # T-independence check at L=3
    print(f"\n[2] d=4 T-check at L={D4_TCHECK['L']}")
    tvals = {}
    for tx in D4_TCHECK["txs"]:
        res = [nc.run_point(D4["rho"], tx, D4_TCHECK["L"], 4, 500 + s)
               for s in range(D4["seeds"])]
        tvals[tx] = {k: stats([r[k] for r in res])
                     for k in ("N_mol", "N_link", "N_rel")}
        d_ = tvals[tx]
        print(f"  tx=+-{tx}: N_mol={d_['N_mol'][0]:.2f}+-{d_['N_mol'][1]:.2f}  "
              f"N_link={d_['N_link'][0]:.1f}+-{d_['N_link'][1]:.1f}  "
              f"N_rel={d_['N_rel'][0]:.0f}")
    m_lo, e_lo = tvals[min(D4_TCHECK["txs"])]["N_mol"]
    m_hi, e_hi = tvals[max(D4_TCHECK["txs"])]["N_mol"]
    t_sig = abs(m_hi - m_lo) / np.sqrt(e_lo ** 2 + e_hi ** 2 + 1e-12)
    t_ok = t_sig < 3.0
    print(f"  -> N_mol T-drift: {t_sig:.2f} sigma (must be < 3)")

    # rho-scaling (secondary) at L=3, d=4: rho in {4, 8, 16}
    print("\n[3] d=4 rho-scaling at L=3 (secondary)")
    rho_rows = {}
    for rho in (4.0, 8.0, 16.0):
        res = [nc.run_point(rho, 2.5, 3.0, 4, 900 + s) for s in range(12)]
        rho_rows[rho] = stats([r["N_mol"] for r in res])
        print(f"  rho={rho:5.1f}: N_mol={rho_rows[rho][0]:.2f}+-{rho_rows[rho][1]:.2f}")
    srho, srho_e = nc.loglog_slope(list(rho_rows), [v[0] for v in rho_rows.values()],
                                   [v[1] for v in rho_rows.values()])
    print(f"  -> N_mol ~ rho^{srho:.3f}+-{srho_e:.3f} (predicted 0.5)")

    # ---- d=3 ---- #
    r3 = scan_L(3, D3, "4")
    Ls3 = D3["Ls"]
    s3, s3e = nc.loglog_slope(Ls3, [r3[L]["N_mol"][0] for L in Ls3],
                              [r3[L]["N_mol"][1] for L in Ls3])
    l3, l3e = nc.loglog_slope(Ls3, [r3[L]["N_link"][0] for L in Ls3],
                              [r3[L]["N_link"][1] for L in Ls3])
    print(f"  -> slopes vs L: N_mol {s3:.3f}+-{s3e:.3f} (area=1)  "
          f"N_link {l3:.3f}+-{l3e:.3f}")

    # ---- d=2: pure-number prediction ---- #
    print(f"\n[5] d=2, tx=+-{D2['tx']}: N_mol must be rho-independent")
    r2 = {}
    for rho in D2["rhos"]:
        res = [nc.run_point(rho, D2["tx"], 1.0, 2, 200 + s)
               for s in range(D2["seeds"])]
        r2[rho] = {k: stats([r[k] for r in res])
                   for k in ("N_mol", "N_link", "N_rel")}
        d_ = r2[rho]
        print(f"  rho={rho:5.1f}: N_mol={d_['N_mol'][0]:.3f}+-{d_['N_mol'][1]:.3f}  "
              f"N_link={d_['N_link'][0]:.2f}  N_rel={d_['N_rel'][0]:.0f}")
    s2, s2e = nc.loglog_slope(D2["rhos"], [r2[r]["N_mol"][0] for r in D2["rhos"]],
                              [r2[r]["N_mol"][1] for r in D2["rhos"]])
    print(f"  -> N_mol ~ rho^{s2:.3f}+-{s2e:.3f} (predicted 0, |.|<=0.15)")

    # ---- coefficient a_d = N_mol / (L^{d-2} rho^{(d-2)/d}) ---- #
    a4 = np.mean([r4[L]["N_mol"][0] / (L ** 2 * D4["rho"] ** 0.5) for L in Ls])
    a3 = np.mean([r3[L]["N_mol"][0] / (L * D3["rho"] ** (1 / 3)) for L in Ls3])
    a2 = np.mean([r2[r]["N_mol"][0] for r in D2["rhos"]])
    print(f"\n[6] coefficients (lattice numbers, coefficient EXTERNAL as declared):")
    print(f"  a_4={a4:.3f}  a_3={a3:.3f}  a_2={a2:.3f}")

    # ---- verdict ---- #
    area4 = abs(s4 - 2.0) <= 0.3
    area3 = abs(s3 - 1.0) <= 0.3
    const2 = abs(s2) <= 0.15
    rho_ok = abs(srho - 0.5) <= 0.15
    phase1 = area4 and area3 and const2 and t_ok
    print("-" * 74)
    print(f"  d=4 area law (slope 2+-0.3):   {area4}  [{s4:.3f}+-{s4e:.3f}]")
    print(f"  d=3 area law (slope 1+-0.3):   {area3}  [{s3:.3f}+-{s3e:.3f}]")
    print(f"  d=2 pure number (|s|<=0.15):   {const2}  [{s2:.3f}+-{s2e:.3f}]")
    print(f"  T-independence (<3 sigma):     {t_ok}  [{t_sig:.2f} sigma]")
    print(f"  rho-scaling 0.5+-0.15 (2ndry): {rho_ok}  [{srho:.3f}+-{srho_e:.3f}]")
    print(f"PHASE 1 VERDICT: {'AREA LAW -- phase 2 gated OPEN' if phase1 else 'DEATH/FAIL -- report with max priority'}")
    print(f"({time.time()-t0:.0f}s)")

    payload.update({
        "d4": {str(L): r4[L] for L in Ls}, "d4_slopes": {
            "mol": [s4, s4e], "link": [l4, l4e], "rel": rel4},
        "d4_tcheck": {str(k): v for k, v in tvals.items()}, "t_sigma": t_sig,
        "d4_rho": {str(k): v for k, v in rho_rows.items()},
        "rho_slope": [srho, srho_e],
        "d3": {str(L): r3[L] for L in Ls3}, "d3_slopes": {
            "mol": [s3, s3e], "link": [l3, l3e]},
        "d2": {str(k): v for k, v in r2.items()}, "d2_slope": [s2, s2e],
        "coefficients": {"a4": float(a4), "a3": float(a3), "a2": float(a2)},
        "checks": {"area4": bool(area4), "area3": bool(area3),
                   "const2": bool(const2), "t_ok": bool(t_ok),
                   "rho_ok": bool(rho_ok)},
        "verdict": "AREA_LAW" if phase1 else "FAIL",
        "runtime_s": time.time() - t0,
    })
    (HERE / "n2_phase1.json").write_text(json.dumps(payload, indent=2))
    print("saved n2_phase1.json")


if __name__ == "__main__":
    main()
