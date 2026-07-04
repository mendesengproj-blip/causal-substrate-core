"""n2_core.py -- N2_ENTROPIA_HORIZONTE: d-dimensional Poisson sprinkling with a
Rindler-horizon corner, and the pre-registered crossing counts.

Geometry (PRE_REGISTRO.md): box in M^d with coords (t, x, y_perp...); horizon =
null plane u = t - x = 0; cut = slice t = 0; entropy surface = the codim-2 corner
{t=0, x=0} of transverse extent L^{d-2}.  Transverse directions are PERIODIC
(min-image), so an area law shows as a count strictly proportional to L^{d-2}.

Counts:
  N_link  -- Hasse links i->j with i in W_p = {u<0, t<0}, j in B_f = {u>0, t>0}
             (crosses both the null plane and the slice => corner-localized).
  N_mol   -- same, with i MAXIMAL in W_p and j MINIMAL in B_f (Dou-Sorkin-style
             horizon molecule; the area-law object).
  N_rel   -- all causal pairs (relations) crossing the corner (comparison).
"""

from __future__ import annotations

import numpy as np


def sprinkle(rho, tx_half, L_perp, d, rng):
    """Poisson sprinkle in t,x in [-tx_half, tx_half], y_perp in [0, L_perp]^(d-2).
    Returns (n, d) array, columns (t, x, y...)."""
    vol = (2 * tx_half) ** 2 * L_perp ** (d - 2)
    n = rng.poisson(rho * vol)
    pts = np.empty((n, d))
    pts[:, 0] = rng.uniform(-tx_half, tx_half, n)
    pts[:, 1] = rng.uniform(-tx_half, tx_half, n)
    for k in range(2, d):
        pts[:, k] = rng.uniform(0.0, L_perp, n)
    return pts


def causal_matrix(pts, L_perp):
    """rel[i,j] = True iff i strictly precedes j (timelike, future-directed),
    with PERIODIC min-image transverse distances."""
    t = pts[:, 0]
    dt = t[None, :] - t[:, None]
    dx2 = (pts[None, :, 1] - pts[:, None, 1]) ** 2
    for k in range(2, pts.shape[1]):
        dperp = np.abs(pts[None, :, k] - pts[:, None, k])
        dperp = np.minimum(dperp, L_perp - dperp)          # min-image
        dx2 = dx2 + dperp ** 2
    return (dt > 0) & (dt * dt > dx2)


def corner_counts(pts, rel):
    """The three pre-registered counts for the corner {t=0, x=0}."""
    t = pts[:, 0]
    u = pts[:, 0] - pts[:, 1]
    Wp = np.nonzero((u < 0) & (t < 0))[0]                  # outside, past of cut
    Bf = np.nonzero((u > 0) & (t > 0))[0]                  # inside, future of cut

    sub = rel[np.ix_(Wp, Bf)]                              # causal crossing pairs
    n_rel = int(sub.sum())
    if n_rel == 0:
        return {"N_rel": 0, "N_link": 0, "N_mol": 0}

    # linkness: no k (anywhere) strictly between i and j
    B = rel.astype(np.float32)
    two_step = (B[Wp] @ B[:, Bf]) > 0.5                    # exists k: i<k<j
    links = sub & ~two_step
    n_link = int(links.sum())

    # Dou-Sorkin molecule: i maximal in W_p, j minimal in B_f
    has_succ_in_Wp = rel[np.ix_(Wp, Wp)].any(axis=1)
    has_pred_in_Bf = rel[np.ix_(Bf, Bf)].any(axis=0)
    mol = links & ~has_succ_in_Wp[:, None] & ~has_pred_in_Bf[None, :]
    return {"N_rel": n_rel, "N_link": n_link, "N_mol": int(mol.sum())}


def run_point(rho, tx_half, L_perp, d, seed):
    rng = np.random.default_rng(31000 + seed)
    pts = sprinkle(rho, tx_half, L_perp, d, rng)
    rel = causal_matrix(pts, L_perp)
    out = corner_counts(pts, rel)
    out["n"] = int(len(pts))
    return out


def loglog_slope(xs, ys, errs=None):
    """Weighted OLS slope of log y vs log x (+ its std error)."""
    xs = np.asarray(xs, float)
    ys = np.asarray(ys, float)
    keep = ys > 0
    x, y = np.log(xs[keep]), np.log(ys[keep])
    if errs is not None:
        w = (np.asarray(ys)[keep] / np.maximum(np.asarray(errs)[keep], 1e-12)) ** 2
    else:
        w = np.ones_like(x)
    W = np.sum(w)
    xb, yb = np.sum(w * x) / W, np.sum(w * y) / W
    sxx = np.sum(w * (x - xb) ** 2)
    slope = np.sum(w * (x - xb) * (y - yb)) / sxx
    resid = y - yb - slope * (x - xb)
    dof = max(len(x) - 2, 1)
    s2 = np.sum(w * resid ** 2) / dof
    return float(slope), float(np.sqrt(s2 / sxx))
