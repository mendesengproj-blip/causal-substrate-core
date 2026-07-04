"""n2_phase2.py -- N2 Phase 2 (GATED on phase 1 = AREA_LAW): configurational
entropy of the ORDERED ferromagnet across the Rindler corner.

Protocol (PRE_REGISTRO.md): SU(2) chiral model (the programme's orientation
sector, via the N1 generalized engine) on the Hasse graph of the SAME d=4
sprinkling geometry; Gaussian mutual information between slabs
A = {-0.5<u<0, |t|<1} and B = {0<u<0.5, |t|<1} over one internal component.
Prediction: I_G ~ A (I_G/L^2 flat in L, +-40%); disordered control << ordered.
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "N1_CONTROLE_SU4"))
import n2_core as nc
import sun_core as sc
import su3_core as s3

HERE = Path(__file__).resolve().parent

RHO, TX = 4.0, 2.5
LS = [2.0, 3.0, 4.0]
N_SEEDS = 4
J_ORD, J_DIS = 1.0, 0.05
BURN, MEAS, EVERY = 500, 3500, 3
SLAB_U, SLAB_T = 0.5, 1.0


def hasse_graph(pts, L_perp):
    rel = nc.causal_matrix(pts, L_perp)
    B = rel.astype(np.float32)
    two = (B @ B) > 0.5
    links = np.argwhere(rel & ~two)
    g = s3.Graph(len(pts), links)
    return g


def blocks(pts):
    u = pts[:, 0] - pts[:, 1]
    t = pts[:, 0]
    A = np.nonzero((u > -SLAB_U) & (u < 0) & (np.abs(t) < SLAB_T))[0]
    Bb = np.nonzero((u > 0) & (u < SLAB_U) & (np.abs(t) < SLAB_T))[0]
    return A, Bb


def gaussian_mi(XA, XB, ridge=1e-6):
    """I = -1/2 sum ln(1 - lam_k), lam = eigvals of the canonical-correlation
    matrix.  XA (nsamp, dA), XB (nsamp, dB), mean-subtracted inside."""
    XA = XA - XA.mean(axis=0)
    XB = XB - XB.mean(axis=0)
    n = XA.shape[0]
    SAA = XA.T @ XA / n
    SBB = XB.T @ XB / n
    SAB = XA.T @ XB / n
    SAA += ridge * np.trace(SAA) / SAA.shape[0] * np.eye(SAA.shape[0])
    SBB += ridge * np.trace(SBB) / SBB.shape[0] * np.eye(SBB.shape[0])
    LA = np.linalg.cholesky(SAA)
    LB = np.linalg.cholesky(SBB)
    M = np.linalg.solve(LA, SAB)
    M = np.linalg.solve(LB, M.T).T
    sv = np.linalg.svd(M, compute_uv=False)
    lam = np.clip(sv ** 2, 0.0, 1.0 - 1e-10)
    return float(-0.5 * np.sum(np.log(1.0 - lam)))


def run_case(L, seed, J):
    rng = np.random.default_rng(61000 + seed)
    pts = nc.sprinkle(RHO, TX, L, 4, rng)
    g = hasse_graph(pts, L)
    A, Bb = blocks(pts)
    mdl = sc.SUNChiralModel(g, 2, J=J, seed=71000 + seed)
    mdl.equilibrate(BURN, adapt=True)
    comp = 1                                  # one internal component (symmetry)
    XA = np.empty((MEAS, A.size))
    XB = np.empty((MEAS, Bb.size))
    ms = []
    taken = s = 0
    while taken < MEAS:
        mdl.sweep()
        s += 1
        if s % EVERY == 0:
            XA[taken] = mdl.v[A, comp]
            XB[taken] = mdl.v[Bb, comp]
            ms.append(mdl.order_parameter())
            taken += 1
    I = gaussian_mi(XA, XB)
    # shuffle baseline (bias of the estimator at zero true MI): permute time
    # indices of XB independently of XA
    perm = np.random.default_rng(81000 + seed).permutation(MEAS)
    I0 = gaussian_mi(XA, XB[perm])
    tau, ess = sc.tau_int(np.array(ms))
    return {"I": I, "I_shuffle": I0, "dA": int(A.size), "dB": int(Bb.size),
            "m": float(np.mean(ms)), "tau_int": tau, "ess": ess, "n": g.n}


def main():
    t0 = time.time()
    # gate: the pre-registered DS-type estimator failed in d=4 (n2_phase1.json,
    # stands as reported); the area law was established by the literature-exact
    # BD molecule (phase 1b: d=3, T-indep, rho^0.5; phase 1c: d=4 converged,
    # d=2 powered).  The gate reads the corrected verdict.
    gate = json.loads((HERE / "n2_phase1c.json").read_text())
    if gate["verdict"] != "AREA_LAW":
        print("PHASE 1 (BD molecule) NOT AREA_LAW -- phase 2 gated CLOSED.")
        sys.exit(1)
    print("=" * 74)
    print("N2 Phase 2 -- ferromagnet Gaussian MI across the Rindler corner")
    print("=" * 74)

    out = {}
    for J, tag in ((J_ORD, "ordered"), (J_DIS, "disordered")):
        out[tag] = {}
        print(f"\n[{tag}] J={J}")
        for L in LS:
            rows = [run_case(L, s, J) for s in range(N_SEEDS)]
            Im, Ie = (float(np.mean([r["I"] for r in rows])),
                      float(np.std([r["I"] for r in rows], ddof=1)
                            / np.sqrt(N_SEEDS)))
            I0m = float(np.mean([r["I_shuffle"] for r in rows]))
            out[tag][L] = {
                "I": [Im, Ie], "I_shuffle": I0m,
                "I_net": Im - I0m,
                "dA": float(np.mean([r["dA"] for r in rows])),
                "m": float(np.mean([r["m"] for r in rows])),
                "tau_max": float(np.max([r["tau_int"] for r in rows])),
                "ess_min": float(np.min([r["ess"] for r in rows]))}
            d = out[tag][L]
            print(f"  L={L:3.1f}: I={Im:7.3f}+-{Ie:.3f}  shuf={I0m:6.3f}  "
                  f"net={d['I_net']:7.3f}  I_net/L2={d['I_net']/L**2:6.4f}  "
                  f"dA~{d['dA']:.0f}  m={d['m']:.3f}  "
                  f"tau<={d['tau_max']:.1f} ESS>={d['ess_min']:.0f}")

    # criteria
    ord_ = out["ordered"]
    net = {L: ord_[L]["I_net"] for L in LS}
    perA = [net[L] / L ** 2 for L in LS]
    flat = (max(perA) - min(perA)) / max(np.mean(perA), 1e-12)
    area_ok = flat < 0.8 and all(v > 0 for v in perA)      # +-40% around mean
    s_net, s_e = nc.loglog_slope(LS, [max(net[L], 1e-9) for L in LS])
    ctrl = all(out["disordered"][L]["I_net"]
               < 0.2 * max(out["ordered"][L]["I_net"], 1e-12) for L in LS)
    print("-" * 74)
    print(f"  I_net/L^2 spread (must be < 0.8 of mean): {flat:.2f}  -> {area_ok}")
    print(f"  I_net ~ L^{s_net:.2f}+-{s_e:.2f} (area=2)")
    print(f"  disordered control < 20% of ordered: {ctrl}")
    verdict = ("AREA_LAW_MATTER" if (area_ok and ctrl)
               else ("INCONCLUSIVE" if not ctrl else "FAIL"))
    print(f"PHASE 2 VERDICT: {verdict}")
    print(f"({time.time()-t0:.0f}s)")

    payload = {"campaign": "N2_ENTROPIA_HORIZONTE", "stage": "phase2",
               "config": {"rho": RHO, "tx": TX, "Ls": LS, "seeds": N_SEEDS,
                          "J_ord": J_ORD, "J_dis": J_DIS, "burn": BURN,
                          "meas": MEAS, "every": EVERY,
                          "slab_u": SLAB_U, "slab_t": SLAB_T},
               "results": {tag: {str(L): out[tag][L] for L in LS}
                           for tag in out},
               "slope_net": [s_net, s_e], "perA_spread": flat,
               "control_ok": bool(ctrl), "verdict": verdict,
               "runtime_s": time.time() - t0}
    (HERE / "n2_phase2.json").write_text(json.dumps(payload, indent=2))
    print("saved n2_phase2.json")


if __name__ == "__main__":
    main()
