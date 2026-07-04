"""n5_core.py -- engine for N5/M2 SKYRME_RADIATIVO (see PRE_REGISTRO.md).

Measures the ONE-LOOP (Gaussian) quartic coefficients of the SU(2) chiral
model on the Poisson causal Hasse substrate, by the clamped-twist method:

    F(g) = J * E[Ubar*(g)]  +  (1/2) ln det' h[Ubar*(g)]  + O(1/J)

with Ubar*(g) the constrained minimum (spatial boundary clamped to the
channel-A / channel-B backgrounds of SC2) and h the J-independent Hessian
of E = sum_links (1 - (1/2)Tr(U_i^dag U_j)) with respect to left rotations
U_i -> exp_q(pi_i) U_i.

Conventions (real quaternion arithmetic, NO complex numbers):
  * q = (w, x, y, z) unit quaternion <-> U = w*I - i (x,y,z).sigma, so the
    Hamilton product realises matrix product and (1/2)Tr(U_i^dag U_j) =
    dot4(q_i, q_j)  (the chiral SU(2) model IS the O(4) model).
  * link quaternion W = q_j (x) conj(q_i) = (w0, wvec); per-link expansion in
    left-rotation coords (alpha on i, beta on j):
      E^(1) = (1/2)(alpha - beta).wvec
      E^(2) = (w0/8)(|alpha|^2+|beta|^2) - (w0/4) alpha.beta
              + (1/4) alpha^T [wvec]_x beta
    (signs pinned by the finite-difference gate G0 in n5_phase0.py).

Anti-circularity: the Skyrme operator is never a fit target; fits are even
polynomials in the twist g of scalar energies / log-determinants.
"""

from __future__ import annotations

import json
import platform
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]                      # 003-TEORIAS/
FL1 = ROOT / "TEIC" / "results" / "matter" / "fl1"
N1 = ROOT / "FRONTEIRA_COMPACTA" / "N1_CONTROLE_SU4"
for p in (str(FL1), str(N1)):
    if p not in sys.path:
        sys.path.insert(0, p)

import su3_core as s3  # noqa: E402  (causal_links, causal_link_graph, Graph)

OUTDIR = HERE


# ============================================================================ #
# quaternions (vectorised, real)
# ============================================================================ #
def qmul(a, b):
    """Hamilton product of (...,4) stacks."""
    aw, av = a[..., :1], a[..., 1:]
    bw, bv = b[..., :1], b[..., 1:]
    w = aw * bw - np.sum(av * bv, axis=-1, keepdims=True)
    v = aw * bv + bw * av + np.cross(av, bv)
    return np.concatenate([w, v], axis=-1)


def qconj(a):
    out = a.copy()
    out[..., 1:] *= -1.0
    return out


def qexp(v):
    """exp map: 3-vector v (rotation angle |v|) -> unit quaternion
    (cos(|v|/2), sin(|v|/2) vhat), series-safe at 0."""
    v = np.asarray(v, float)
    th = np.linalg.norm(v, axis=-1, keepdims=True)
    half = 0.5 * th
    w = np.cos(half)
    small = th < 1e-8
    with np.errstate(invalid="ignore", divide="ignore"):
        s = np.where(small, 0.5 - th * th / 48.0, np.sin(half) / np.where(th == 0, 1.0, th))
    return np.concatenate([w, s * v], axis=-1)


def qnormalize(q):
    return q / np.linalg.norm(q, axis=-1, keepdims=True)


# ============================================================================ #
# substrates
# ============================================================================ #
def sprinkle(rng, rho, tmax, L):
    """Poisson sprinkling in [0,tmax] x [0,L]^3. Returns pts (N,4)."""
    vol = tmax * L ** 3
    n = rng.poisson(rho * vol)
    pts = np.empty((n, 4))
    pts[:, 0] = rng.uniform(0.0, tmax, n)
    pts[:, 1:] = rng.uniform(0.0, L, (n, 3))
    return pts[np.argsort(pts[:, 0])]


def hasse_edges(pts):
    """Covering relations (Hasse links) -- same substrate code as FL1/N1."""
    return s3.causal_links(pts)


def cubic_grid(L):
    """Open 3D cubic grid, spacing 1: coords (N,3) and nearest-neighbour
    edges (E,2).  Static control with the same clamped-twist pipeline."""
    idx = np.arange(L ** 3).reshape(L, L, L)
    coords = np.stack(np.meshgrid(np.arange(L), np.arange(L), np.arange(L),
                                  indexing="ij"), axis=-1).reshape(-1, 3).astype(float)
    edges = []
    for ax in range(3):
        a = np.take(idx, np.arange(L - 1), axis=ax).ravel()
        b = np.take(idx, np.arange(1, L), axis=ax).ravel()
        edges.append(np.stack([a, b], axis=1))
    return coords, np.concatenate(edges, axis=0)


def spatial_link_length(pts, edges):
    """Mean spatial length of links (a_eff of the pre-registration)."""
    d = pts[edges[:, 1], 1:] - pts[edges[:, 0], 1:]
    return float(np.mean(np.linalg.norm(d, axis=1)))


def free_mask_spatial(xyz, L, b):
    """Free = further than b from every spatial face of [0,L]^3."""
    return np.all((xyz > b) & (xyz < L - b), axis=1)


# ============================================================================ #
# backgrounds (channels of SC2, centred on the spatial box centre)
# ============================================================================ #
def background(xyz, g, channel, L):
    """channel 'A': v = g*(x+y+z)*e1 (abelian, K=0, S=9g^4);
    channel 'B': v = g*(x,y,z)      (hedgehog frame, K=6g^4, S=9g^4);
    channel 'A2': as A but along e2 (null test G4).  Coords from box centre."""
    r = xyz - 0.5 * L
    if channel == "A":
        v = np.zeros_like(r)
        v[:, 0] = g * r.sum(axis=1)
    elif channel == "A2":
        v = np.zeros_like(r)
        v[:, 1] = g * r.sum(axis=1)
    elif channel == "B":
        v = g * r
    else:
        raise ValueError(channel)
    return qexp(v)


# ============================================================================ #
# energy / gradient / Hessian of E = sum_links (1 - dot4(q_i,q_j))
# ============================================================================ #
def energy(q, edges):
    return float(np.sum(1.0 - np.sum(q[edges[:, 0]] * q[edges[:, 1]], axis=1)))


def link_W(q, edges):
    return qmul(q[edges[:, 1]], qconj(q[edges[:, 0]]))


def gradient(q, edges, n):
    """dE/d(left-rotation) per node, (n,3).  Per link: -wvec/2 on i, +wvec/2 on j
    (sign convention of qexp pinned by the finite-difference gate G0)."""
    W = link_W(q, edges)
    wv = W[:, 1:]
    g = np.zeros((n, 3))
    np.add.at(g, edges[:, 0], -0.5 * wv)
    np.add.at(g, edges[:, 1], 0.5 * wv)
    return g


def _cross_mat(wv):
    """[w]_x stack: (E,3,3) with M v = w x v."""
    E = wv.shape[0]
    M = np.zeros((E, 3, 3))
    M[:, 0, 1] = -wv[:, 2]
    M[:, 0, 2] = wv[:, 1]
    M[:, 1, 0] = wv[:, 2]
    M[:, 1, 2] = -wv[:, 0]
    M[:, 2, 0] = -wv[:, 1]
    M[:, 2, 1] = wv[:, 0]
    return M


def hessian_free(q, edges, free):
    """Dense Hessian restricted to free nodes (3F,3F).

    Per link (i,j), W=(w0,wvec):
      H_ii += (w0/4) I ; H_jj += (w0/4) I
      H_ij += -(w0/4) I + (1/4)[wvec]_x ;  H_ji = H_ij^T.
    Links with a clamped endpoint contribute only their free diagonal block."""
    n = q.shape[0]
    fidx = np.full(n, -1, dtype=np.int64)
    ff = np.nonzero(free)[0]
    fidx[ff] = np.arange(ff.size)
    F = ff.size
    H = np.zeros((3 * F, 3 * F))

    W = link_W(q, edges)
    w0, wv = W[:, 0], W[:, 1:]
    i, j = edges[:, 0], edges[:, 1]
    fi, fj = fidx[i], fidx[j]

    # diagonal blocks (w0/4) I
    diag = np.zeros(F)
    m = fi >= 0
    np.add.at(diag, fi[m], 0.25 * w0[m])
    m = fj >= 0
    np.add.at(diag, fj[m], 0.25 * w0[m])
    di = np.arange(F)
    for c in range(3):
        H[3 * di + c, 3 * di + c] += diag

    # off-diagonal blocks for free-free links
    m = (fi >= 0) & (fj >= 0)
    if np.any(m):
        blocks = -0.25 * w0[m, None, None] * np.eye(3) + 0.25 * _cross_mat(wv[m])
        bi, bj = fi[m], fj[m]
        # scatter (duplicate (bi,bj) pairs impossible: Hasse links are unique)
        for a in range(3):
            for b in range(3):
                H[3 * bi + a, 3 * bj + b] += blocks[:, a, b]
                H[3 * bj + b, 3 * bi + a] += blocks[:, a, b]
    return H


# ============================================================================ #
# constrained relaxation (Newton, clamped boundary)
# ============================================================================ #
def relax(q0, edges, free, tol=1e-10, max_iter=60):
    """Damped Newton to the constrained minimum; returns (q, info).
    Uses the same analytic gradient/Hessian as the loop measurement."""
    q = q0.copy()
    n = q.shape[0]
    ff = np.nonzero(free)[0]
    e_prev = energy(q, edges)
    lam = 0.0
    for it in range(max_iter):
        gr = gradient(q, edges, n)[ff]
        gmax = float(np.max(np.abs(gr))) if gr.size else 0.0
        if gmax < tol:
            return q, {"iters": it, "grad_inf": gmax, "energy": e_prev, "converged": True}
        H = hessian_free(q, edges, free)
        if lam > 0.0:
            H[np.diag_indices_from(H)] += lam
        try:
            L = np.linalg.cholesky(H)
            step = -np.linalg.solve(H, gr.ravel()).reshape(-1, 3)
        except np.linalg.LinAlgError:
            lam = max(10.0 * lam, 1e-6)
            continue
        # backtracking line search on E
        t = 1.0
        for _ in range(30):
            qt = q.copy()
            qt[ff] = qnormalize(qmul(qexp(t * step), q[ff]))
            e_new = energy(qt, edges)
            if e_new <= e_prev + 1e-14 * abs(e_prev):
                break
            t *= 0.5
        q, e_prev = qt, e_new
        lam *= 0.1
    gr = gradient(q, edges, n)[ff]
    return q, {"iters": max_iter, "grad_inf": float(np.max(np.abs(gr))),
               "energy": e_prev, "converged": False}


# ============================================================================ #
# log-determinants (two algorithms -- N-hig)
# ============================================================================ #
def logdet_chol(H):
    L = np.linalg.cholesky(H)
    return 2.0 * float(np.sum(np.log(np.diag(L))))


def logdet_eig(H):
    w = np.linalg.eigvalsh(H)
    if np.any(w <= 0):
        raise np.linalg.LinAlgError("non-positive eigenvalue in logdet_eig")
    return float(np.sum(np.log(w)))


# ============================================================================ #
# tree-level interior energy (free-free links only, pre-registered comparator)
# ============================================================================ #
def interior_energy(q, edges, free):
    m = free[edges[:, 0]] & free[edges[:, 1]]
    e = edges[m]
    return float(np.sum(1.0 - np.sum(q[e[:, 0]] * q[e[:, 1]], axis=1)))


# ============================================================================ #
# even-polynomial fit in g (declared estimator)
# ============================================================================ #
def fit_even(gs, ys, degree=6):
    """Least-squares fit y = a2 g^2 + a4 g^4 (+ a6 g^6). Returns dict."""
    gs = np.asarray(gs, float)
    ys = np.asarray(ys, float)
    cols = [gs ** 2, gs ** 4]
    if degree >= 6:
        cols.append(gs ** 6)
    A = np.stack(cols, axis=1)
    coef, res, *_ = np.linalg.lstsq(A, ys, rcond=None)
    out = {"a2": float(coef[0]), "a4": float(coef[1])}
    out["a6"] = float(coef[2]) if degree >= 6 else 0.0
    pred = A @ coef
    out["rms_resid"] = float(np.sqrt(np.mean((ys - pred) ** 2)))
    return out


# ============================================================================ #
# one full channel measurement on one substrate
# ============================================================================ #
def _bg_vec(xyz, g, channel, L):
    """The exp-map 3-vector field of `background` (linear in g)."""
    r = xyz - 0.5 * L
    if channel == "A":
        v = np.zeros_like(r); v[:, 0] = g * r.sum(axis=1)
    elif channel == "A2":
        v = np.zeros_like(r); v[:, 1] = g * r.sum(axis=1)
    elif channel == "B":
        v = g * r.copy()
    else:
        raise ValueError(channel)
    return v


def measure_channel(pts_xyz, edges, L, b, gs, channel, q_vac_logdet=None,
                    logdet_fn=logdet_chol, warm=True):
    """Returns per-g tree interior energies and loop 1/2*delta-logdet,
    both per free node, plus diagnostics.  gs iterated ascending with warm
    starts (previous relaxed interior + incremental twist)."""
    n = pts_xyz.shape[0]
    free = free_mask_spatial(pts_xyz, L, b)
    F = int(free.sum())
    q_vac = background(pts_xyz, 0.0, "A", L)          # uniform identity
    if q_vac_logdet is None:
        q_vac_logdet = logdet_fn(hessian_free(q_vac, edges, free))
    e_vac = interior_energy(q_vac, edges, free)        # = 0
    rows = []
    gs_sorted = sorted(float(g) for g in gs)
    q_prev, g_prev = None, 0.0
    for g in gs_sorted:
        q0 = background(pts_xyz, g, channel, L)
        if warm and q_prev is not None:
            dv = _bg_vec(pts_xyz, g - g_prev, channel, L)
            q0w = qnormalize(qmul(qexp(dv), q_prev))
            q0w[~free] = q0[~free]                     # clamps exact
            q0 = q0w
        q, info = relax(q0, edges, free)
        if not info["converged"]:
            raise RuntimeError(f"relaxation failed: channel {channel}, g={g}, {info}")
        q_prev, g_prev = q, g
        ld = logdet_fn(hessian_free(q, edges, free))
        rows.append({
            "g": float(g),
            "tree_per_node": (interior_energy(q, edges, free) - e_vac) / F,
            "loop_per_node": 0.5 * (ld - q_vac_logdet) / F,
            "relax_iters": info["iters"],
            "grad_inf": info["grad_inf"],
        })
    return {"channel": channel, "F": F, "rows": rows,
            "vac_logdet": float(q_vac_logdet)}


# ============================================================================ #
# TORUS + LINK-TRANSPORTER instrument (engineering change after G3-red on the
# clamped instrument; documented in PRE_REGISTRO.md addendum and RESULTADO.md).
#
# Substrate: spatial 3-torus (minimum-image causal relation), time open.
# Twist: per-link transporters Omega_ij = qexp(g * C . delta_ij) -- realises
# the SC1 constant-current link statistics EXACTLY at U == 1 (bare tree =
# sum of 1 - cos(|v|/2), the SC1 cosine).  Node 0 pinned for the determinant.
#
# E_link = 1 - (1/2)Tr(U_i^dag Omega U_j) = 1 - dot4(q_i, om (x) q_j).
# With X = q_j (x) conj(q_i), P = om (x) X, R = X (x) om:
#   grad_i = -pvec/2 ; grad_j = +rvec/2       (G0-pinned)
#   H_ii = H_jj = (p0/4) I  (p0 = r0)
#   H_ij[a,b] = -T_ab/8,  T_ab = -2 * w( e_a (x) om (x) e_b (x) X )
# (reduces to the untwisted blocks at Omega = 1; re-pinned by G0.)
# ============================================================================ #
def causal_links_torus(pts, L):
    """Hasse links of a sprinkling on [0,T] x (R/L)^3 (min-image spatial
    distance).  Same transitive-reduction algorithm as su3_core.causal_links."""
    n = pts.shape[0]
    t = pts[:, 0]
    dt = t[None, :] - t[:, None]
    dx2 = np.zeros((n, n), dtype=np.float32)
    for c in range(3):
        d = pts[None, :, 1 + c] - pts[:, None, 1 + c]
        d -= L * np.round(d / L)
        dx2 += (d * d).astype(np.float32)
    rel = (dt > 0) & ((dt * dt).astype(np.float32) > dx2)
    relf = rel.astype(np.float32)
    two_step = (relf @ relf) > 0.5
    link = rel & ~two_step
    return np.argwhere(link)


def link_deltas_torus(pts, edges, L):
    """Min-image spatial displacements delta_ij (E,3) of the links."""
    d = pts[edges[:, 1], 1:] - pts[edges[:, 0], 1:]
    return d - L * np.round(d / L)


def transporters(deltas, g, channel):
    """Omega_ij = qexp(v), v from the SC2 channel currents:
    A : v = g*(dx+dy+dz) e1   (abelian, K=0, S=9g^4)
    A2: idem along e2         (null test)
    B : v = g*delta           (hedgehog frame, K=6g^4, S=9g^4)."""
    E = deltas.shape[0]
    if channel == "A":
        v = np.zeros((E, 3)); v[:, 0] = g * deltas.sum(axis=1)
    elif channel == "A2":
        v = np.zeros((E, 3)); v[:, 1] = g * deltas.sum(axis=1)
    elif channel == "B":
        v = g * deltas
    else:
        raise ValueError(channel)
    return qexp(v)


def energy_tw(q, edges, om):
    return float(np.sum(1.0 - np.sum(q[edges[:, 0]] * qmul(om, q[edges[:, 1]]),
                                     axis=1)))


def _link_PRX(q, edges, om):
    X = qmul(q[edges[:, 1]], qconj(q[edges[:, 0]]))
    P = qmul(om, X)
    R = qmul(X, om)
    return P, R, X


def gradient_tw(q, edges, om, n):
    P, R, _ = _link_PRX(q, edges, om)
    g = np.zeros((n, 3))
    np.add.at(g, edges[:, 0], -0.5 * P[:, 1:])
    np.add.at(g, edges[:, 1], 0.5 * R[:, 1:])
    return g


_EBASIS = np.zeros((3, 4))
_EBASIS[:, 1:] = np.eye(3)


def _link_blocks_tw(q, edges, om):
    """Per-link (p0, cross-block) with cross[a,b] = -T_ab/8."""
    P, R, X = _link_PRX(q, edges, om)
    p0 = P[:, 0]
    E = X.shape[0]
    T = np.empty((E, 3, 3))
    ea_om = [qmul(np.broadcast_to(_EBASIS[a], om.shape), om) for a in range(3)]
    eb_X = [qmul(np.broadcast_to(_EBASIS[b], X.shape), X) for b in range(3)]
    for a in range(3):
        for b in range(3):
            prod_w = (ea_om[a][:, 0] * eb_X[b][:, 0]
                      - np.sum(ea_om[a][:, 1:] * eb_X[b][:, 1:], axis=1))
            T[:, a, b] = -2.0 * prod_w
    return p0, -T / 8.0


def hessian_tw_dense(q, edges, om, free):
    """Dense pinned Hessian (3F,3F) of energy_tw."""
    n = q.shape[0]
    fidx = np.full(n, -1, dtype=np.int64)
    ff = np.nonzero(free)[0]
    fidx[ff] = np.arange(ff.size)
    F = ff.size
    H = np.zeros((3 * F, 3 * F))
    p0, cross = _link_blocks_tw(q, edges, om)
    i, j = edges[:, 0], edges[:, 1]
    fi, fj = fidx[i], fidx[j]
    diag = np.zeros(F)
    m = fi >= 0
    np.add.at(diag, fi[m], 0.25 * p0[m])
    m = fj >= 0
    np.add.at(diag, fj[m], 0.25 * p0[m])
    di = np.arange(F)
    for c in range(3):
        H[3 * di + c, 3 * di + c] += diag
    m = (fi >= 0) & (fj >= 0)
    if np.any(m):
        bi, bj, blocks = fi[m], fj[m], cross[m]
        for a in range(3):
            for b in range(3):
                H[3 * bi + a, 3 * bj + b] += blocks[:, a, b]
                H[3 * bj + b, 3 * bi + a] += blocks[:, a, b]
    return H


def hessian_tw_sparse(q, edges, om, free):
    """CSR pinned Hessian (for Newton solves)."""
    from scipy import sparse
    n = q.shape[0]
    fidx = np.full(n, -1, dtype=np.int64)
    ff = np.nonzero(free)[0]
    fidx[ff] = np.arange(ff.size)
    F = ff.size
    p0, cross = _link_blocks_tw(q, edges, om)
    i, j = edges[:, 0], edges[:, 1]
    fi, fj = fidx[i], fidx[j]
    rows, cols, vals = [], [], []
    diag = np.zeros(F)
    m = fi >= 0
    np.add.at(diag, fi[m], 0.25 * p0[m])
    m = fj >= 0
    np.add.at(diag, fj[m], 0.25 * p0[m])
    di = np.arange(F)
    for c in range(3):
        rows.append(3 * di + c); cols.append(3 * di + c); vals.append(diag)
    m = (fi >= 0) & (fj >= 0)
    bi, bj, blocks = fi[m], fj[m], cross[m]
    for a in range(3):
        for b in range(3):
            rows.append(3 * bi + a); cols.append(3 * bj + b); vals.append(blocks[:, a, b])
            rows.append(3 * bj + b); cols.append(3 * bi + a); vals.append(blocks[:, a, b])
    H = sparse.coo_matrix((np.concatenate(vals),
                           (np.concatenate(rows), np.concatenate(cols))),
                          shape=(3 * F, 3 * F)).tocsr()
    return H


def relax_tw(q0, edges, om, free, tol=1e-10, max_iter=60):
    """Damped Newton with Jacobi-preconditioned CG solves (pinned node
    fixed; CG vs splu agreement 4e-14 checked -- splu is the fallback)."""
    from scipy import sparse
    from scipy.sparse.linalg import LinearOperator, cg, splu
    q = q0.copy()
    n = q.shape[0]
    ff = np.nonzero(free)[0]
    e_prev = energy_tw(q, edges, om)
    lam = 0.0
    for it in range(max_iter):
        gr = gradient_tw(q, edges, om, n)[ff]
        gmax = float(np.max(np.abs(gr))) if gr.size else 0.0
        if gmax < tol:
            return q, {"iters": it, "grad_inf": gmax, "energy": e_prev,
                       "converged": True}
        H = hessian_tw_sparse(q, edges, om, free).tocsr()
        if lam > 0.0:
            H = H + lam * sparse.identity(H.shape[0], format="csr")
        d = H.diagonal()
        M = LinearOperator(H.shape, matvec=lambda v: v / d)
        sol, info = cg(H, gr.ravel(), rtol=1e-12, atol=0.0, maxiter=5000, M=M)
        if info != 0:
            try:
                sol = splu(H.tocsc()).solve(gr.ravel())
            except RuntimeError:
                lam = max(10.0 * lam, 1e-6)
                continue
        step = -sol.reshape(-1, 3)
        t = 1.0
        for _ in range(30):
            qt = q.copy()
            qt[ff] = qnormalize(qmul(qexp(t * step), q[ff]))
            e_new = energy_tw(qt, edges, om)
            if e_new <= e_prev + 1e-14 * abs(e_prev):
                break
            t *= 0.5
        q, e_prev = qt, e_new
        lam *= 0.1
    gr = gradient_tw(q, edges, om, n)[ff]
    return q, {"iters": max_iter, "grad_inf": float(np.max(np.abs(gr))),
               "energy": e_prev, "converged": False}


def measure_channel_tw(pts, edges, deltas, L, gs, channel, vac_logdet=None,
                       logdet_fn=logdet_chol):
    """Torus instrument: per-g bare tree (U==1), relaxed tree, loop
    1/2*delta-logdet at the relaxed config; all per node."""
    n = pts.shape[0]
    free = np.ones(n, dtype=bool)
    free[0] = False                                    # pin
    om0 = transporters(deltas, 0.0, channel)
    q_vac = np.zeros((n, 4)); q_vac[:, 0] = 1.0
    if vac_logdet is None:
        vac_logdet = logdet_fn(hessian_tw_dense(q_vac, edges, om0, free))
    rows = []
    q_prev, g_prev = None, 0.0
    for g in sorted(float(x) for x in gs):
        om = transporters(deltas, g, channel)
        q0 = q_vac if q_prev is None else q_prev
        q, info = relax_tw(q0, edges, om, free)
        if not info["converged"]:
            raise RuntimeError(f"relax_tw failed: {channel}, g={g}, {info}")
        q_prev, g_prev = q, g
        ld = logdet_fn(hessian_tw_dense(q, edges, om, free))
        rows.append({
            "g": float(g),
            "tree_bare_per_node": energy_tw(q_vac, edges, om) / n,
            "tree_per_node": info["energy"] / n,
            "loop_per_node": 0.5 * (ld - vac_logdet) / n,
            "relax_iters": info["iters"],
            "grad_inf": info["grad_inf"],
        })
    return {"channel": channel, "n": n, "rows": rows,
            "vac_logdet": float(vac_logdet)}


def cubic_grid_torus(L):
    """Periodic cubic lattice, spacing 1: coords, edges, deltas (all +e_ax)."""
    idx = np.arange(L ** 3).reshape(L, L, L)
    edges, deltas = [], []
    for ax in range(3):
        a = idx.ravel()
        b = np.roll(idx, -1, axis=ax).ravel()
        edges.append(np.stack([a, b], axis=1))
        d = np.zeros((L ** 3, 3)); d[:, ax] = 1.0
        deltas.append(d)
    return np.concatenate(edges, axis=0), np.concatenate(deltas, axis=0)


# ============================================================================ #
# bookkeeping
# ============================================================================ #
def save_json(name, payload):
    payload = dict(payload)
    payload["_meta"] = {
        "campaign": "N5_SKYRME_RADIATIVO",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "python": sys.version.split()[0],
        "numpy": np.__version__,
        "platform": platform.platform(),
    }
    path = OUTDIR / name
    path.write_text(json.dumps(payload, indent=2))
    return path
