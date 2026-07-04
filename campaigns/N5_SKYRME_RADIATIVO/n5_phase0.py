"""n5_phase0.py -- N5/M2 engineering gates G0-G4, TORUS + TRANSPORTER
instrument (see PRE_REGISTRO.md addendum; the clamped instrument failed its
G3 and was retired -- first run preserved in n5_phase0_clamped.json).

G0: analytic gradient/Hessian vs finite differences, GENERIC transporters.
G1: vacuum Hessian unpinned: PSD, exactly 3 zero modes; pinned: lambda_min>0.
G2: logdet Cholesky vs eigenvalues < 1e-8 relative (one relaxed case/channel).
G3: BARE tree quartic (U==1): fit a4 == direct -sum|v|^4/384 per node
    (machine, tests the fit machinery) AND ratio B/A = 5/9 +- 15% (isotropy
    of the real causal links); periodic cubic control ratio == 1 (blindness).
G4: abelian null: loop alpha4 for A(e1) vs A(e2), compatible with 0.

Red gate => fix engineering, never proceed.
"""

from __future__ import annotations

import numpy as np

import n5_core as core

RHO, TMAX = 2.0, 4.0
L_GATE = 6.0                    # gates run at L=6 (cheap); phase 1 adds L=8
GS = [0.04, 0.06, 0.08, 0.12, 0.16, 0.20, 0.24]


def build(seed, L):
    rng = np.random.default_rng(seed)
    pts = core.sprinkle(rng, RHO, TMAX, L)
    edges = core.causal_links_torus(pts, L)
    deltas = core.link_deltas_torus(pts, edges, L)
    return pts, edges, deltas


def gate_g0(rng):
    n = 50
    pts = core.sprinkle(rng, 2.0, 2.0, 3.0)[:n]
    edges = core.causal_links_torus(pts, 3.0)
    om = core.qexp(0.3 * rng.standard_normal((len(edges), 3)))   # generic
    q = core.qnormalize(rng.standard_normal((n, 4)))
    grad = core.gradient_tw(q, edges, om, n)
    H = core.hessian_tw_dense(q, edges, om, np.ones(n, bool))
    Hs = core.hessian_tw_sparse(q, edges, om, np.ones(n, bool)).toarray()
    sparse_dense = float(np.max(np.abs(H - Hs)))

    eps = 1e-6
    errs_g = []
    for node in rng.choice(n, 8, replace=False):
        for c in range(3):
            v = np.zeros(3); v[c] = eps
            qp = q.copy(); qp[node] = core.qmul(core.qexp(v), q[node])
            qm = q.copy(); qm[node] = core.qmul(core.qexp(-v), q[node])
            fd = (core.energy_tw(qp, edges, om)
                  - core.energy_tw(qm, edges, om)) / (2 * eps)
            errs_g.append(abs(fd - grad[node, c]))

    def en(delta):
        qq = core.qnormalize(core.qmul(core.qexp(delta), q))
        return core.energy_tw(qq, edges, om)

    eh = 1e-4
    errs_h = []
    se = edges[rng.choice(len(edges), 6, replace=False)]
    pairs = []
    for (i, j) in se:
        pairs += [(int(i), 0, int(i), 1), (int(i), 0, int(j), 0),
                  (int(i), 1, int(j), 2), (int(i), 2, int(i), 2)]
    z = np.zeros((n, 3))
    for (na, ca, nb, cb) in pairs:
        if na == nb and ca == cb:
            d1 = z.copy(); d1[na, ca] = 2 * eh
            d2 = z.copy(); d2[na, ca] = -2 * eh
            fd = (en(d1) - 2 * en(z) + en(d2)) / (4 * eh * eh)
        else:
            dpp = z.copy(); dpp[na, ca] = eh; dpp[nb, cb] += eh
            dpm = z.copy(); dpm[na, ca] = eh; dpm[nb, cb] -= eh
            dmp = z.copy(); dmp[na, ca] = -eh; dmp[nb, cb] += eh
            dmm = z.copy(); dmm[na, ca] = -eh; dmm[nb, cb] -= eh
            fd = (en(dpp) - en(dpm) - en(dmp) + en(dmm)) / (4 * eh * eh)
        errs_h.append(abs(fd - H[3 * na + ca, 3 * nb + cb]))
    ge = float(np.max(errs_g)) / max(1.0, float(np.max(np.abs(grad))))
    he = float(np.max(errs_h)) / max(1.0, float(np.max(np.abs(H))))
    return {"grad_relerr": ge, "hess_relerr": he, "sparse_dense": sparse_dense,
            "pass": bool(ge < 1e-6 and he < 1e-6 and sparse_dense == 0.0)}


def gate_g1():
    pts, edges, deltas = build(11, L_GATE)
    n = pts.shape[0]
    om0 = core.transporters(deltas, 0.0, "A")
    q = np.zeros((n, 4)); q[:, 0] = 1.0
    H = core.hessian_tw_dense(q, edges, om0, np.ones(n, bool))
    w = np.linalg.eigvalsh(H)
    med = float(np.median(w))
    nz = int(np.sum(np.abs(w) < 1e-10 * max(med, 1.0)))
    psd = bool(w.min() > -1e-10 * max(med, 1.0))
    free = np.ones(n, bool); free[0] = False
    wp = np.linalg.eigvalsh(core.hessian_tw_dense(q, edges, om0, free))
    return {"n_zero_unpinned": nz, "psd": psd,
            "lambda_min_pinned": float(wp.min()),
            "pass": bool(nz == 3 and psd and wp.min() > 0)}


def gate_g2():
    pts, edges, deltas = build(12, L_GATE)
    n = pts.shape[0]
    free = np.ones(n, bool); free[0] = False
    diffs = []
    for ch in ("A", "B"):
        om = core.transporters(deltas, 0.12, ch)
        q0 = np.zeros((n, 4)); q0[:, 0] = 1.0
        q, info = core.relax_tw(q0, edges, om, free)
        H = core.hessian_tw_dense(q, edges, om, free)
        lc, le = core.logdet_chol(H), core.logdet_eig(H)
        diffs.append(abs(lc - le) / abs(le))
    return {"rel_diffs": [float(d) for d in diffs],
            "pass": bool(max(diffs) < 1e-8)}


def bare_direct_a4(deltas, channel, n):
    """-sum_links |v(g=1)|^4 / 384 per node (the SC1 cosine quartic)."""
    if channel == "A":
        v4 = (deltas.sum(axis=1)) ** 4
    elif channel == "B":
        v4 = (np.sum(deltas ** 2, axis=1)) ** 2
    else:
        raise ValueError(channel)
    return float(-np.sum(v4) / 384.0 / n)


def gate_g3():
    """Bare tree: fit vs direct (machine) + ratio 5/9 (Poisson) / 1 (cubic)."""
    out = {"seeds": []}
    ratios, fit_errs = [], []
    for seed in (1001, 1002, 1003):
        pts, edges, deltas = build(seed, L_GATE)
        n = pts.shape[0]
        row = {"seed": seed}
        for ch in ("A", "B"):
            ys = []
            for g in GS:
                om = core.transporters(deltas, g, ch)
                q_vac = np.zeros((n, 4)); q_vac[:, 0] = 1.0
                ys.append(core.energy_tw(q_vac, edges, om) / n)
            fit = core.fit_even(GS, ys)
            direct = bare_direct_a4(deltas, ch, n)
            row[ch] = {"a4_fit": fit["a4"], "a4_direct": direct,
                       "relerr": abs(fit["a4"] - direct) / abs(direct)}
            fit_errs.append(row[ch]["relerr"])
        row["ratio_BA"] = row["B"]["a4_fit"] / row["A"]["a4_fit"]
        ratios.append(row["ratio_BA"])
        out["seeds"].append(row)
    out["poisson_mean_ratio"] = float(np.mean(ratios))
    # periodic cubic control: exact blindness (identical |v| per link)
    cedges, cdeltas = core.cubic_grid_torus(8)
    ncub = 8 ** 3
    a4A = bare_direct_a4(cdeltas, "A", ncub)
    a4B = bare_direct_a4(cdeltas, "B", ncub)
    out["cubic_ratio"] = float(a4B / a4A)
    out["max_fit_relerr"] = float(max(fit_errs))
    ok = (abs(out["poisson_mean_ratio"] - 5.0 / 9.0) < 0.15 * (5.0 / 9.0)
          and abs(out["cubic_ratio"] - 1.0) < 1e-12
          and out["max_fit_relerr"] < 1e-3)
    out["pass"] = bool(ok)
    return out


def gate_g4():
    d4 = []
    for seed in (2001, 2002, 2003):
        pts, edges, deltas = build(seed, L_GATE)
        a4 = {}
        for ch in ("A", "A2"):
            res = core.measure_channel_tw(pts, edges, deltas, L_GATE, GS, ch)
            ys = [r["loop_per_node"] for r in res["rows"]]
            a4[ch] = core.fit_even(GS, ys)["a4"]
        d4.append(a4["A2"] - a4["A"])
    d4 = np.asarray(d4)
    mean = float(d4.mean())
    sem = float(d4.std(ddof=1) / np.sqrt(len(d4)))
    return {"delta_a4": [float(x) for x in d4], "mean": mean, "sem": sem,
            "pass": bool(abs(mean) < 2 * max(sem, 1e-12))}


def main():
    rng = np.random.default_rng(42)
    out = {}
    out["G0"] = gate_g0(rng); print("G0:", out["G0"], flush=True)
    out["G1"] = gate_g1();    print("G1:", out["G1"], flush=True)
    out["G2"] = gate_g2();    print("G2:", out["G2"], flush=True)
    out["G3"] = gate_g3()
    print("G3:", {k: out["G3"][k] for k in
                  ("poisson_mean_ratio", "cubic_ratio", "max_fit_relerr", "pass")},
          flush=True)
    out["G4"] = gate_g4();    print("G4:", out["G4"], flush=True)
    out["all_pass"] = all(out[k]["pass"] for k in ("G0", "G1", "G2", "G3", "G4"))
    core.save_json("n5_phase0.json", out)
    print("ALL GATES PASS" if out["all_pass"] else "GATE RED -- STOP")


if __name__ == "__main__":
    main()
