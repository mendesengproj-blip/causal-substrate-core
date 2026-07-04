"""Aggregate the phase-2b JSONL rows and apply the verbatim phase-2 criteria."""
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import n2_core as nc

HERE = Path(__file__).resolve().parent
LS = [2.0, 3.0, 4.0]

rows = [json.loads(l) for l in
        (HERE / "n2_phase2b_rows.jsonl").read_text().splitlines()]
out = {}
for tag, J in (("ordered", 1.0), ("disordered", 0.005)):
    out[tag] = {}
    for L in LS:
        rs = [r for r in rows if r["J"] == J and r["L"] == L]
        Is = [r["I"] for r in rs]
        I0s = [r["I_shuffle"] for r in rs]
        nets = [i - i0 for i, i0 in zip(Is, I0s)]
        Im, Ie = float(np.mean(Is)), float(np.std(Is, ddof=1) / np.sqrt(len(Is)))
        net_m = float(np.mean(nets))
        net_e = float(np.std(nets, ddof=1) / np.sqrt(len(nets)))
        out[tag][L] = {"I": [Im, Ie], "I_shuffle": float(np.mean(I0s)),
                       "I_net": net_m, "I_net_err": net_e, "n_seeds": len(rs),
                       "m": float(np.mean([r["m"] for r in rs])),
                       "ess_min": float(np.min([r["ess"] for r in rs]))}
        d = out[tag][L]
        print(f"{tag:10s} L={L:3.1f}: net={net_m:7.4f}+-{net_e:.4f}  "
              f"net/L2={net_m/L**2:7.5f}  m={d['m']:.3f}  ESS>={d['ess_min']:.0f}")

ord_ = out["ordered"]
net = {L: ord_[L]["I_net"] for L in LS}
perA = [net[L] / L ** 2 for L in LS]
flat = (max(perA) - min(perA)) / max(np.mean(perA), 1e-12)
area_ok = flat < 0.8 and all(v > 0 for v in perA)
s_net, s_e = nc.loglog_slope(LS, [max(net[L], 1e-9) for L in LS],
                             [ord_[L]["I_net_err"] for L in LS])
ctrl = all(out["disordered"][L]["I_net"]
           < 0.2 * max(out["ordered"][L]["I_net"], 1e-12) for L in LS)
print("-" * 66)
print(f"I_net/L^2 spread (< 0.8): {flat:.2f} -> {area_ok}")
print(f"I_net ~ L^{s_net:.2f}+-{s_e:.2f} (area=2)")
print(f"control < 20%: {ctrl}")
verdict = ("AREA_LAW_MATTER" if (area_ok and ctrl)
           else ("INCONCLUSIVE" if not ctrl else "FAIL"))
print(f"PHASE 2b VERDICT: {verdict}")

payload = {"campaign": "N2_ENTROPIA_HORIZONTE", "stage": "phase2b_repair",
           "repairs": ["global zero-mode projection", "control J=0.005"],
           "note": "run in foreground chunks (background tasks were killed)",
           "results": {tag: {str(L): out[tag][L] for L in LS} for tag in out},
           "slope_net": [s_net, s_e], "perA_spread": flat,
           "control_ok": bool(ctrl), "verdict": verdict}
(HERE / "n2_phase2b.json").write_text(json.dumps(payload, indent=2))
print("saved n2_phase2b.json")
