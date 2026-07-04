"""sun_core.py -- generalized SU(N) engine for the N1_CONTROLE_SU4 campaign.

Generalizes su3_core.py (FL1) to arbitrary N >= 2 via the generalized Gell-Mann
basis, normalised Tr(T_a T_b) = 2 delta_ab (identical convention to FL1).  The
SUBSTRATE parts (Poisson sprinkling, Hasse graph, longest-chain distances,
correlation accumulator, C(r) classifier) are IMPORTED from su3_core verbatim, so
SU(3) and SU(4) are tested on byte-identical causal networks and with the
byte-identical estimator windows (pre-registered in PRE_REGISTRO.md).

Anti-circularity: the generators ARE the definition of su(N) (mathematics, not a
physics input); no QCD number enters anywhere.  The gate instantiates N=3 and must
reproduce the FL1 measurements before N=4 runs (PRE_REGISTRO gate).
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]          # 003-TEORIAS/
FL1 = ROOT / "TEIC" / "results" / "matter" / "fl1"
sys.path.insert(0, str(FL1))
sys.path.insert(0, str(ROOT / "TEIC" / "src"))

import su3_core as s3  # noqa: E402  -- substrate + estimators, reused verbatim

# re-exported substrate/estimator primitives (byte-identical to FL1)
sprinkle_box = s3.sprinkle_box
causal_link_graph = s3.causal_link_graph
lattice_periodic = s3.lattice_periodic
longest_chain_from = s3.longest_chain_from
CorrelationAccumulator = s3.CorrelationAccumulator
fit_forms = s3.fit_forms
dagger = s3.dagger

PI = np.pi


# =========================================================================== #
# PART 0 -- generalized Gell-Mann generators of su(N), Tr(T_a T_b) = 2 delta_ab
# =========================================================================== #
def generators(N):
    """The N^2-1 generalized Gell-Mann matrices: for each pair i<j the symmetric
    (E_ij + E_ji) and antisymmetric -i(E_ij - E_ji); for each l=1..N-1 the diagonal
    sqrt(2/(l(l+1))) diag(1,..,1,-l,0,..).  All Hermitian, traceless, and
    Tr(T_a T_b) = 2 delta_ab -- the exact su3_core convention at N=3."""
    T = []
    for i in range(N):
        for j in range(i + 1, N):
            S = np.zeros((N, N), dtype=complex)
            S[i, j] = S[j, i] = 1.0
            T.append(S)
            A = np.zeros((N, N), dtype=complex)
            # GROUP-DEF COMPLEX -- the -i/+i entries define the antisymmetric
            # generators of su(N); group theory, not an injected phase.
            A[i, j] = -1j
            A[j, i] = 1j
            # END GROUP-DEF COMPLEX
            T.append(A)
    for l in range(1, N):
        D = np.zeros((N, N), dtype=complex)
        for k in range(l):
            D[k, k] = 1.0
        D[l, l] = -l
        T.append(D * np.sqrt(2.0 / (l * (l + 1))))
    return np.array(T)


def structure_f(T):
    """f^{abc} = (1/4i) Tr([T_a,T_b] T_c) for a generator stack T."""
    n = T.shape[0]
    f = np.zeros((n, n, n))
    for a in range(n):
        for b in range(n):
            comm = T[a] @ T[b] - T[b] @ T[a]
            for c in range(n):
                f[a, b, c] = (np.trace(comm @ T[c]) / 4j).real
    return f


# =========================================================================== #
# PART 1 -- the group SU(N): exponential, Haar sampling, projection
# =========================================================================== #
def sun_exp(X):
    """U = exp(i X) for Hermitian X (single or stack), via eigendecomposition."""
    w, V = np.linalg.eigh(X)
    # GROUP-DEF COMPLEX -- exp(i w) is the Lie exponential su(N)->SU(N).
    phase = np.exp(1j * w)
    # END GROUP-DEF COMPLEX
    return (V * phase[..., None, :]) @ np.conjugate(np.swapaxes(V, -1, -2))


def sun_from_coords(T, phi):
    """U = exp(i phi_a T_a) from real coordinates phi (..., N^2-1)."""
    X = np.tensordot(np.asarray(phi, float), T, axes=([-1], [0]))
    return sun_exp(X)


def sun_random(N, n, rng):
    """n Haar-distributed SU(N) matrices (QR of complex Gaussian, phase-fixed,
    det projected)."""
    # GROUP-DEF COMPLEX -- complex Gaussian carries the Haar measure of U(N).
    Z = (rng.standard_normal((n, N, N)) + 1j * rng.standard_normal((n, N, N))) / np.sqrt(2.0)
    # END GROUP-DEF COMPLEX
    Q, R = np.linalg.qr(Z)
    ph = np.diagonal(R, axis1=-2, axis2=-1)
    ph = ph / np.abs(ph)
    Q = Q * ph[:, None, :]
    det = np.linalg.det(Q)
    Q = Q * (det ** (-1.0 / N))[:, None, None]
    return Q


def sun_log(U):
    """Anti-Hermitian su(N) logarithm (eigenphases in (-pi, pi])."""
    w, V = np.linalg.eig(U)
    theta = np.angle(w)
    Vinv = np.linalg.inv(V)
    # GROUP-DEF COMPLEX -- diag(i theta) is the su(N) logarithm.
    return (V * (1j * theta)[..., None, :]) @ Vinv
    # END GROUP-DEF COMPLEX


def project_to_sun(M):
    """Nearest SU(N) matrix (unitary polar factor, det fixed to 1)."""
    N = M.shape[-1]
    Uu, _, Vh = np.linalg.svd(M)
    W = Uu @ Vh
    det = np.linalg.det(W)
    return W * (det ** (-1.0 / N))[..., None, None]


def is_sun(U, ):
    eye = np.broadcast_to(np.eye(U.shape[-1]), U.shape)
    unit = np.max(np.abs(U @ dagger(U) - eye))
    det = np.max(np.abs(np.linalg.det(U) - 1.0))
    return float(unit), float(det)


# =========================================================================== #
# PART 2 -- the SU(N) principal-chiral spin model (verbatim FL1 Phase B, N free)
# =========================================================================== #
# E = -J sum_<ij> (1/N) Re Tr(U_i U_j^dag).  v = (1/sqrtN)[ReU, ImU] is a unit
# 2N^2-vector with v_i.v_j = (1/N)Re Tr(U_i U_j^dag) -- same Mermin identity.

def u_to_vec(U):
    N = U.shape[-1]
    flat = U.reshape(U.shape[:-2] + (N * N,))
    return np.concatenate([flat.real, flat.imag], axis=-1) / np.sqrt(N)


class SUNChiralModel:
    """Vectorised colour-Metropolis for the SU(N) principal-chiral field --
    line-for-line the FL1 SU3ChiralModel with N a parameter."""

    def __init__(self, graph, N, J, seed=0, step=0.4, init=None):
        self.g = graph
        self.N = int(N)
        self.T = generators(N)
        self.dimA = N * N - 1
        self.dimV = 2 * N * N
        self.J = float(J)
        self.rng = np.random.default_rng(seed)
        self.step = float(step)
        if init == "ordered":
            self.U = np.broadcast_to(np.eye(N, dtype=complex),
                                     (graph.n, N, N)).copy()
        else:
            self.U = sun_random(N, graph.n, self.rng)
        self.v = u_to_vec(self.U)

    def _color_field(self, c):
        nbr, seg, m = self.g._nbr[c], self.g._seg[c], self.g.groups[c].size
        H = np.empty((m, self.dimV))
        for k in range(self.dimV):
            H[:, k] = np.bincount(seg, weights=self.v[nbr, k], minlength=m)
        return H

    def _propose_accept(self, c, H):
        nodes = self.g.groups[c]
        m = nodes.size
        phi = self.step * self.rng.standard_normal((m, self.dimA))
        R = sun_from_coords(self.T, phi)
        Uprop = R @ self.U[nodes]
        vprop = u_to_vec(Uprop)
        dE = -self.J * np.sum((vprop - self.v[nodes]) * H, axis=1)
        p = np.exp(-np.clip(dE, 0.0, 50.0))
        acc = self.rng.random(m) < p
        self.U[nodes[acc]] = Uprop[acc]
        self.v[nodes[acc]] = vprop[acc]
        return int(acc.sum())

    def sweep(self):
        acc = 0
        for c in range(self.g.n_colors):
            if self.g.groups[c].size == 0:
                continue
            acc += self._propose_accept(c, self._color_field(c))
        return acc / max(self.g.n, 1)

    def equilibrate(self, n_burn, adapt=True, target=0.4):
        for s in range(n_burn):
            a = self.sweep()
            if adapt and (s + 1) % 25 == 0:
                if a > target + 0.1:
                    self.step *= 1.15
                elif a < target - 0.1:
                    self.step *= 0.87
                self.step = float(np.clip(self.step, 1e-3, 3.0))

    def order_parameter(self):
        return float(np.linalg.norm(self.v.mean(axis=0)))

    def energy_per_link(self):
        e = self.g.edges
        if e.shape[0] == 0:
            return 0.0
        overlap = np.sum(self.v[e[:, 0]] * self.v[e[:, 1]], axis=1)
        return float(-self.J * np.mean(overlap))

    def corr_arrays(self):
        return [self.v[:, k] for k in range(self.dimV)]


# ---- tau_int / ESS (N-hig, Sokal automatic window) -------------------------- #
def tau_int(series):
    """Integrated autocorrelation time with the standard positive-window rule:
    sum rho(t) from t=1 while rho(t) > 0.  Returns (tau, ESS)."""
    x = np.asarray(series, float)
    n = x.size
    if n < 8 or np.std(x) == 0:
        return 0.5, float(n)
    x = x - x.mean()
    var = float(np.dot(x, x) / n)
    tau = 0.5
    for t in range(1, n // 2):
        rho = float(np.dot(x[:-t], x[t:]) / ((n - t) * var))
        if rho <= 0:
            break
        tau += rho
    return float(tau), float(n / (2.0 * tau))


# =========================================================================== #
# PART 3 -- Goldstone twist test (verbatim FLD d2, N free)
# =========================================================================== #
def chiral_energy_grad(U, dx):
    """E2 = (2/dx^2) sum_x sum_i [1 - (1/N) Re Tr(U_x^dag U_{x+i})] * dx^3."""
    N = U.shape[-1]
    Ud = dagger(U)
    e2 = 0.0
    for ax in range(3):
        R = Ud @ np.roll(U, -1, axis=ax)
        tr = np.real(np.trace(R, axis1=-2, axis2=-1))
        e2 += np.sum(1.0 - tr / N)
    return float((2.0 / dx ** 2) * e2 * dx ** 3)


def goldstone_twists(N, L=14):
    """Static twist test: aligned vacuum U0; per generator T_a, twist
    U = exp(i k x T_a) U0; dE(k) -> 0 with dE ~ rho_s k^2 => gapless mode.
    Expected count = N^2 - 1 broken generators of SU(N)xSU(N) -> SU(N)_diag."""
    rng = np.random.default_rng(0)
    T = generators(N)
    U0 = sun_random(N, 1, rng)[0]
    base = np.broadcast_to(U0, (L, L, L, N, N)).copy()
    E0 = chiral_energy_grad(base, 1.0)
    x = np.arange(L)
    ks = [2 * PI * nk / L for nk in (1, 2, 3)]
    modes = {}
    n_gapless = 0
    for a in range(N * N - 1):
        dEs, stiff = [], []
        for k in ks:
            Xtw = sun_exp((k * x)[:, None, None] * T[a][None])
            U = np.einsum("aij,jk->aik", Xtw, U0)
            field = np.broadcast_to(U[:, None, None], (L, L, L, N, N)).copy()
            Et = chiral_energy_grad(field, 1.0)
            dEs.append(float(Et - E0))
            stiff.append(float((Et - E0) / k ** 2))
        gapless = (dEs[0] > 0) and (dEs[0] < dEs[-1]) and (stiff[0] > 1e-6)
        n_gapless += int(gapless)
        modes[f"gen_{a}"] = {"k": ks, "dE": dEs, "dE_over_k2": stiff,
                             "gapless": bool(gapless)}
    return {"expected": N * N - 1, "found": n_gapless, "vacuum_E0": E0,
            "modes": modes}


# =========================================================================== #
# PART 4 -- topology: embedded hedgehog, baryon number (N free)
# =========================================================================== #
def embedded_hedgehog(N, L, half_width=2.6, charge=+1, w_core=0.8):
    """B=+-1 Skyrmion: SU(2) hedgehog in the upper-left 2x2 block of SU(N)
    (rest = identity).  The inclusion SU(2)->SU(N) is an iso on pi_3 (Bott)."""
    x = np.linspace(-half_width, half_width, L)
    dx = float(x[1] - x[0])
    X, Y, Z = np.meshgrid(x, x, x, indexing="ij")
    r = np.sqrt(X ** 2 + Y ** 2 + Z ** 2)
    rs = np.where(r > 0, r, 1.0)
    rx, ry, rz = X / rs, Y / rs, Z / rs
    rx[r == 0] = ry[r == 0] = rz[r == 0] = 0.0
    if charge < 0:
        rz = -rz
    F = PI * np.exp(-r / w_core)
    a0 = np.cos(F)
    s = np.sin(F)
    a1, a2, a3 = s * rx, s * ry, s * rz
    U = np.zeros(X.shape + (N, N), dtype=complex)
    # GROUP-DEF COMPLEX -- the SU(2) hedgehog block embedded in SU(N).
    U[..., 0, 0] = a0 + 1j * a3
    U[..., 0, 1] = a2 + 1j * a1
    U[..., 1, 0] = -a2 + 1j * a1
    U[..., 1, 1] = a0 - 1j * a3
    # END GROUP-DEF COMPLEX
    for k in range(2, N):
        U[..., k, k] = 1.0
    return U, dx


_B_PREF = -1.0 / (24.0 * PI ** 2)


def baryon_number(U, dx):
    """Pontryagin index of U: S^3 -> SU(N) (same formula, N free)."""
    Ud = dagger(U)
    a = [sun_log(Ud @ np.roll(U, -1, axis=ax)) for ax in range(3)]
    ax_, ay_, az_ = a
    comm = ay_ @ az_ - az_ @ ay_
    dens = 3.0 * np.real(np.trace(ax_ @ comm, axis1=-2, axis2=-1))
    return _B_PREF * float(np.sum(dens))


# =========================================================================== #
# PART 5 -- gauge sector: SU(N) Wilson action, loops, Creutz (verbatim, N free)
# =========================================================================== #
def gauge_init(N, L, rng, hot=True):
    shape = (4, L, L, L, L)
    if hot:
        return sun_random(N, int(np.prod(shape)), rng).reshape(shape + (N, N))
    return np.broadcast_to(np.eye(N, dtype=complex), shape + (N, N)).copy()


def _shift(A, mu, sign):
    return np.roll(A, -sign, axis=mu)


def staple_sum(U, mu):
    Umu = U[mu]
    A = np.zeros_like(Umu)
    for nu in range(4):
        if nu == mu:
            continue
        Unu = U[nu]
        upper = Unu @ _shift(Umu, nu, +1) @ dagger(_shift(Unu, mu, +1))
        Unu_mnu = _shift(Unu, nu, -1)
        lower = (dagger(Unu_mnu) @ _shift(Umu, nu, -1)
                 @ _shift(Unu_mnu, mu, +1))
        A = A + upper + lower
    return A


def gauge_metropolis_sweep(U, beta, rng, step, T, n_hit=2):
    """Metropolis over links; dS = -(beta/N) Re Tr((U' - U) A^dag)."""
    N = U.shape[-1]
    L = U.shape[1]
    g = np.arange(L)
    I, J, K, Tt = np.meshgrid(g, g, g, g, indexing="ij")
    parity = (I + J + K + Tt) % 2
    acc_tot = cnt_tot = 0
    for mu in range(4):
        A = staple_sum(U, mu)
        for par in (0, 1):
            mask = parity == par
            for _ in range(n_hit):
                Uold = U[mu][mask]
                Amask = A[mask]
                R = sun_from_coords(T, step * rng.standard_normal(
                    (Uold.shape[0], N * N - 1)))
                Uprop = R @ Uold
                dtr = np.real(np.trace((Uprop - Uold) @ dagger(Amask),
                                       axis1=-2, axis2=-1))
                dS = -(beta / N) * dtr
                p = np.exp(-np.clip(dS, 0.0, 50.0))
                a = rng.random(Uold.shape[0]) < p
                blk = U[mu][mask]
                blk[a] = Uprop[a]
                U[mu][mask] = blk
                acc_tot += int(a.sum())
                cnt_tot += a.size
    return acc_tot / max(cnt_tot, 1)


def _roll_n(field, axis, n):
    return np.roll(field, -n, axis=axis) if n else field


def wilson_loop(U, mu, nu, r, t):
    N = U.shape[-1]
    Umu, Unu = U[mu], U[nu]
    Pmu = np.broadcast_to(np.eye(N, dtype=complex), Umu.shape).copy()
    for k in range(r):
        Pmu = Pmu @ _roll_n(Umu, mu, k)
    Pnu = np.broadcast_to(np.eye(N, dtype=complex), Unu.shape).copy()
    base_nu = _roll_n(Unu, mu, r)
    for k in range(t):
        Pnu = Pnu @ _roll_n(base_nu, nu, k)
    Pmu_top = np.broadcast_to(np.eye(N, dtype=complex), Umu.shape).copy()
    base_mu_top = _roll_n(Umu, nu, t)
    for k in range(r):
        Pmu_top = Pmu_top @ _roll_n(base_mu_top, mu, k)
    Pnu_left = np.broadcast_to(np.eye(N, dtype=complex), Unu.shape).copy()
    for k in range(t):
        Pnu_left = Pnu_left @ _roll_n(Unu, nu, k)
    W = Pmu @ Pnu @ dagger(Pmu_top) @ dagger(Pnu_left)
    return float(np.mean(np.real(np.trace(W, axis1=-2, axis2=-1)) / N))


def measure_wilson_loops(U, r_max, t_max):
    out = {}
    nu = 3
    for r in range(1, r_max + 1):
        for t in range(1, t_max + 1):
            vals = [wilson_loop(U, mu, nu, r, t) for mu in range(3)]
            out[(r, t)] = float(np.mean(vals))
    return out


def static_potential(loops, r_max, t_max, w_floor=2e-3):
    rs, Vs = [], []
    for r in range(1, r_max + 1):
        ts, lw = [], []
        for t in range(1, t_max + 1):
            w = loops.get((r, t))
            if w is not None and w > w_floor:
                ts.append(t)
                lw.append(-np.log(w))
        if len(ts) >= 2:
            rs.append(r)
            Vs.append(float(np.polyfit(ts, lw, 1)[0]))
    return np.array(rs, float), np.array(Vs, float)


def creutz_ratio(loops, r):
    try:
        val = (loops[(r, r)] * loops[(r - 1, r - 1)]) / \
              (loops[(r, r - 1)] * loops[(r - 1, r)])
        if val <= 0:
            return float("nan")
        return float(-np.log(val))
    except (KeyError, ZeroDivisionError):
        return float("nan")


if __name__ == "__main__":
    rng = np.random.default_rng(0)
    print("sun_core smoke tests")
    for N in (2, 3, 4):
        T = generators(N)
        G = np.einsum("aij,bji->ab", T, T).real
        err = np.max(np.abs(G - 2 * np.eye(N * N - 1)))
        U = sun_random(N, 500, rng)
        ue, de = is_sun(U)
        print(f"  N={N}: {N*N-1} gens, Tr-norm err {err:.1e}, "
              f"Haar unit {ue:.1e} det {de:.1e}")
    # N=3 cross-check against su3_core structure constants
    T3 = generators(3)
    f3 = structure_f(T3)
    # find the |f|=1 entry (f_123 analogue)
    mx = np.unravel_index(np.argmax(np.abs(f3)), f3.shape)
    print(f"  N=3 f max |f|={np.abs(f3[mx]):.4f} at {mx} (expect 1.0)")
