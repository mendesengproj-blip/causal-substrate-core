# -*- coding: utf-8 -*-
"""
N4 — FASE 2: o setor Goldstone (campo de orientação) quantizado à la SJ sobre
o vácuo MC REAL. Pré-registro §5 (Fase 2) + Fase 0 §4.3 (rota R-A; R-B NÃO
rodada, declarado) + lições Fase 1 (régua ABSOLUTA p/ estimadores
correlacionados) e Fase 3 (sub-regiões em unidades de ρ^{−1/d}).
Gate do funil: Fase 1 sem D1/D2 — satisfeito. D3 vive aqui.

DECLARAÇÃO PRÉ-RUN (commitada antes de executar; nenhum critério muda depois):

SUBSTRATO (pré-reg: "mesma configuração de N2 fase 2"): caixa M⁴
  (t,x) ∈ [−2.5, 2.5]², (y,z) ∈ [0,L)² periódico min-imagem, ρ=4,
  L ∈ {2, 3}; grafo de Hasse (links) = n2_phase2.hasse_graph verbatim.
  MC: SUNChiralModel(N=2) do motor N1 — E = −J Σ_links v_i·v_j com
  v_i·v_j = (1/2)Re Tr(U_iU_j†) = a_i·a_j (quaternion O(4) unitário; o
  modelo É o ferromagneto O(4)). J_ORD=1.0, J_DIS=0.05 (controle p/ régua),
  burn 500 (adapt), 4 seeds × 3 configs espaçadas 200 sweeps
  (τ_int/ESS da série m reportados — N-hig 1).

ROTA R-A — DERIVAÇÃO NO PAPEL (precedente: eigenproblem da Fase 1 no papel):
  O pré-reg descreve "massa local m²(x) nas direções de Goldstone (Hessiana
  projetada)". A derivação exata para SU(2) quiral mostra que a versão
  ESCALAR-por-direção é IDENTICAMENTE NULA: a energia de cada link depende só
  de U_xU_y† ⇒ invariante sob rotação COMUM dos extremos ⇒ toda soma-de-linha
  escalar por direção = 0, config a config (não só no vácuo ideal). O objeto
  que sobrevive no nível Gaussiano é a MATRIZ 3×3 por sítio (a projeção nas
  3 direções de Goldstone INCLUINDO a mistura entre elas):
    carta transversal em torno da ordem global e (unit 4-vetor, por config):
    a_x = c_x·e + π_x^i f_i, frame {e,f_1,f_2,f_3} (Gram-Schmidt canônico,
    determinístico); c_x = a_x·e SINALIZADO; r_i = π_i/c.
    Hessiana exata da carta: H_{xi,yj} = −J(δ_ij + r_i(x)r_j(y)) por link;
    H_{xi,xj} = +J·S_ij(x)·B(x), S_ij = δ_ij/c + π_iπ_j/c³,
    B(x) = e·Σ_{y~x}a_y.
    Massa projetada (soma-de-linha em blocos): M_ij(x) = Σ_y H_{xi,yj}
      = J[S_ij(x)B(x) − z_x δ_ij − r_i(x)·Σ_{y~x} r_j(y)].
    Vácuo ideal (π≡0): M ≡ 0 EXATO ⇒ tripleto = 3 cópias exatas da Fase 1
    (a afirmação analítica do pré-reg; verificada no smoke à máquina).
  GUARDA DE CARTA (instrumento): |c| < 0.2 ⇒ c → sign(c)·0.2 (a carta
  transversal diverge no equador); fração de sítios clipados REPORTADA
  (ordenado: ~0; desordenado: muitos — o controle é assim mesmo).
  CAVEAT DE ESCALA (declarado): a identificação M(x) ↔ m²(x) da série de
  Johnston é a naive (unidades do sprinkling, sem constante de conversão) —
  a MESMA fronteira de escala externa de todo o programa; o splitting (M2.2)
  é adimensional e primeiro-ordem insensível; robustez declarada: M → 4M na
  célula decisiva (L=3, J=1) NÃO pode trocar a classificação.

CONSTRUÇÃO SJ DO TRIPLETO (Johnston d=4 com inserção matricial):
  L̃ = LT ⊗ I₃ (índice (x,i) = 3x+i); M̃ = blkdiag{M(x)};
  G_R = a·L̃·(I + (a/ρ)M̃L̃)^{-1}, a = (1/2π)√(ρ/6)  [inserção no sítio
  intermediário, expansão conferida; LT nilpotente ⇒ sempre invertível];
  iΔ = i(G_R − G_R^T), Hermitiana, pares ±λ (higiene checada por run).

MEDIÇÕES E CRITÉRIOS (congelados):
  M2.2 (Q2-fraca — o núcleo; D3 vive aqui):
    Observable por config: matriz de ocupação de direção dos K=12 modos IR
    (top-λ) do tripleto SJ: Λ_ij = Σ_{k≤K} Σ_x u_k[x,i]·ū_k[x,j]
    (K múltiplo de 3: no vácuo ideal shells completas ⇒ Λ ∝ I ⇒ split 0).
    Δ_q = (max−min)/mean dos autovalores de Λ (frame-free).
    RÉGUA CLÁSSICA (mesmo funcional, mesmas configs): Δ_cl idem sobre os
    K=12 modos MAIS MOLES da Hessiana clássica H (3N×3N), excluídos os
    zero-modos exatos de simetria (|eig| < 1e-8·max; esperados ~6 = dim o(4)
    em config térmica; contagem reportada).
    D3 (pré-reg §8.4, "≫ E não-decresce" congelado em números):
      D3 ⟺ [Δ_q > 3·Δ_cl além de 2σ combinado] em AMBOS os L
           E [Δ_q(L=3) ≥ Δ_q(L=2) − 2σ].
    Controle J=0.05: mesmos números reportados (calibra splitting sem ordem;
    esperado Δ(ordenado) ≪ Δ(desordenado)).
  M2.1 (forma IR sobre fundo real — reportada, sem morte):
    >> EMENDA DE JANELA (conflito achado NO PAPEL, antes de rodar): a janela
    da Fase 1 transplantada literalmente é VAZIA aqui — piso n≥2 dá
    k = 4π/L ≥ 4.19 > k_max = 0.25·2πρ^{1/4} = 2.221 (ρ=4). Amendada:
    modos n≥1 admitidos com o piso k_res = 2π/(1.4·T) = 1.795 mantido
    (T=2.5). Resultado: SÓ L=3, n=1 (k=2.094) — UM ponto k; L=2 sem janela
    (declarado; M2.1 é single-point, como o d=4 da Fase 1).
    c_s = ω(k₁)/k₁ pelos DOIS estimadores (E2 pico-Hann primário; E1′ fase),
    sobre W_tr(x,y) = (1/3)Σ_i W[(x,i),(y,i)] (traço de direção), bulk
    |t|,|x| ≤ 0.7·2.5. REFERÊNCIA no MESMO substrato: c_scalar do escalar
    massless (Fase-1 verbatim) nas mesmas caixas/seeds.
    Critérios (régua ABSOLUTA, lição Fase 1): sobrevive-se
    |c_s(E2) − c_scalar(E2)| ≤ 0.10 E |c_s(E2) − c_s(E1′)| ≤ 0.10;
    sanidade |c − 1| ≤ 0.25 reportada.
  Q2-forte (diagnóstico barato da Fase 0 §3): histograma de gaps do espectro
    do ESCALAR massless por substrato — degenerescências exatas além de
    flutuação = surpresa a reportar (esperado: nenhuma; Axioma 2 = postulado).
  R-B (Hessiana de Hasse nativa): NÃO RODADA (pré-reg: diagnóstico opcional,
    não critério; declarado).

SAÍDAS: n4_fase2_rows.jsonl (checkpoint por config, retomável) +
n4_fase2.json. Flags: --smoke (L=2, 1 seed, 1 config + teste de degeneres-
cência tripla no vácuo ideal, à máquina).
"""
import json, os, sys, time, gc
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[0] / "N2_ENTROPIA_HORIZONTE"))
sys.path.insert(0, str(HERE.parents[0] / "N1_CONTROLE_SU4"))
import n2_core as nc            # noqa: E402
import sun_core as sc           # noqa: E402
import su3_core as s3           # noqa: E402

BASE_SEED = 20260703
RHO, TX = 4.0, 2.5
LS = [2.0, 3.0]
NSEEDS, NCFG = 4, 3
BURN, SPACING = 500, 200
J_ORD, J_DIS = 1.0, 0.05
K_IR = 12
C_CLIP = 0.2
ZERO_TOL = 1e-8
A_JOHN = (1.0 / (2 * np.pi)) * np.sqrt(RHO / 6.0)
KRES = 2 * np.pi / (1.4 * TX)
KMAX = 0.25 * 2 * np.pi * RHO ** 0.25
SMOKE = "--smoke" in sys.argv

if SMOKE:
    LS = [2.0]; NSEEDS = 1; NCFG = 1

ROWS_PATH = "n4_fase2_rows_smoke.jsonl" if SMOKE else "n4_fase2_rows.jsonl"
OUT_PATH = "n4_fase2_smoke.json" if SMOKE else "n4_fase2.json"


def log(m): print(f"[{time.strftime('%H:%M:%S')}] {m}", flush=True)


def emit(row):
    with open(ROWS_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(row) + "\n")


# ---------------- substrato (n2_phase2 verbatim) ----------------
def hasse(pts, L):
    rel = nc.causal_matrix(pts, L)
    B = rel.astype(np.float32)
    two = (B @ B) > 0.5
    Lk = rel & ~two
    g = s3.Graph(len(pts), np.argwhere(Lk))
    return g, Lk


# ---------------- quaternion e Hessiana O(4) ----------------
def quat_of(U):
    """U = a0 + i a·sigma -> unit 4-vector (a0,a1,a2,a3)."""
    a0 = U[:, 0, 0].real
    a3 = U[:, 0, 0].imag
    a2 = U[:, 0, 1].real
    a1 = U[:, 0, 1].imag
    return np.stack([a0, a1, a2, a3], axis=1)


def frame_of(e):
    """Frame ortonormal {f1,f2,f3} perp a e (Gram-Schmidt canônico)."""
    fs = []
    for k in range(4):
        v = np.zeros(4); v[k] = 1.0
        v = v - (v @ e) * e
        for f in fs:
            v = v - (v @ f) * f
        n = np.linalg.norm(v)
        if n > 1e-6:
            fs.append(v / n)
        if len(fs) == 3:
            break
    return np.array(fs)


def hessian_and_mass(a, edges, J):
    """Hessiana 3N×3N na carta transversal + massa projetada M(x) 3×3.
    Retorna (H, Mx, clipfrac, e)."""
    n = len(a)
    e = a.mean(axis=0)
    e = e / np.linalg.norm(e)
    F = frame_of(e)                       # (3,4)
    pi = a @ F.T                          # (n,3)
    c = a @ e                             # (n,) sinalizado
    nclip = int(np.sum(np.abs(c) < C_CLIP))
    c = np.sign(c) * np.maximum(np.abs(c), C_CLIP)
    r = pi / c[:, None]                   # (n,3)

    i_, j_ = edges[:, 0], edges[:, 1]
    H = np.zeros((3 * n, 3 * n))
    # off-diagonal por link (simétrico): H_{xi,yj} = -J(delta_ij + r_i(x)r_j(y))
    for iA in range(3):
        for jB in range(3):
            val = -J * ((1.0 if iA == jB else 0.0) + r[i_, iA] * r[j_, jB])
            H[3 * i_ + iA, 3 * j_ + jB] += val
            H[3 * j_ + jB, 3 * i_ + iA] += val
    # diagonal: +J S_ij(x) B(x)
    B = np.zeros(n)
    np.add.at(B, i_, a[j_] @ e)
    np.add.at(B, j_, a[i_] @ e)
    S = (np.eye(3)[None] / c[:, None, None]
         + pi[:, :, None] * pi[:, None, :] / c[:, None, None] ** 3)
    for iA in range(3):
        for jB in range(3):
            H[3 * np.arange(n) + iA, 3 * np.arange(n) + jB] += J * S[:, iA, jB] * B
    # massa projetada: soma-de-linha em blocos
    z = np.zeros(n)
    np.add.at(z, i_, 1.0); np.add.at(z, j_, 1.0)
    Rs = np.zeros((n, 3))
    np.add.at(Rs, i_, r[j_]); np.add.at(Rs, j_, r[i_])
    Mx = J * (S * B[:, None, None] - z[:, None, None] * np.eye(3)[None]
              - r[:, :, None] * Rs[:, None, :])
    return H, Mx, nclip / n, e


# ---------------- Johnston tripleto ----------------
def idelta_triplet(Lk, Mx):
    n = Lk.shape[0]
    LT = Lk.T.astype(np.float64)
    Lt = np.kron(LT, np.eye(3))
    MLt = np.einsum("xab,xy->xayb", Mx, LT).reshape(3 * n, 3 * n)
    GR = A_JOHN * np.linalg.solve(
        (np.eye(3 * n) + (A_JOHN / RHO) * MLt).T, Lt.T).T
    return 1j * (GR - GR.T)


def idelta_scalar(Lk):
    LT = Lk.T.astype(np.float64)
    GR = A_JOHN * LT
    return 1j * (GR - GR.T)


def pair_resid(lam):
    s = np.sort(lam)
    return float(np.max(np.abs(s + s[::-1])) / np.max(np.abs(s)))


# ---------------- ocupação de direção (M2.2) ----------------
def dir_split(V, idx, n):
    """Lambda_ij = soma_{k in idx} soma_x u_k[x,i] conj(u_k[x,j]);
    Delta = (max-min)/mean dos autovalores (frame-free)."""
    O = np.zeros((3, 3), complex)
    for k in idx:
        u = V[:, k].reshape(n, 3)
        O += np.einsum("xi,xj->ij", u.conj(), u)
    ev = np.linalg.eigvalsh((O + O.conj().T) / 2).real
    return float((ev.max() - ev.min()) / ev.mean()), [float(x) for x in ev]


# ---------------- estimadores de dispersão (Fase 1 verbatim) ----------------
def qinterp(y0, y1, y2):
    d = y0 - 2 * y1 + y2
    return 0.0 if abs(d) < 1e-30 else 0.5 * (y0 - y2) / d


def binned_proj(tt, dxproj_fn, W, bulk, kvals, Tbox, h):
    idx = np.where(bulk)[0]
    i, j = np.triu_indices(len(idx), k=1)
    gi, gj = idx[i], idx[j]
    dt = tt[gj] - tt[gi]
    Wv = W[np.searchsorted(idx, gi), np.searchsorted(idx, gj)]
    tmax = 1.4 * Tbox
    nb = int(2 * tmax / h)
    bt = np.clip(((dt + tmax) / h).astype(int), 0, nb - 1)
    btm = nb - 1 - bt
    tcent = (np.arange(nb) + 0.5) * h - tmax
    out = {}
    for k in kvals:
        pr = dxproj_fn(gi, gj, k)
        acc = np.zeros(nb, complex); cnt = np.zeros(nb)
        np.add.at(acc, bt, Wv * pr); np.add.at(cnt, bt, 1)
        np.add.at(acc, btm, np.conj(Wv * pr)); np.add.at(cnt, btm, 1)
        Bn = np.where(cnt > 0, acc / np.maximum(cnt, 1), 0)
        out[float(k)] = (Bn, cnt)
    return tcent, out


def e2_peak(tcent, proj, Tbox, om_max):
    tmax = 1.4 * Tbox
    om_g = np.arange(0.0, om_max, 0.05)
    hann = 0.5 * (1 + np.cos(np.pi * tcent / tmax))
    ph = np.exp(1j * om_g[:, None] * tcent[None, :]) * hann[None, :]
    out = {}
    for k, (Bn, cnt) in proj.items():
        P = np.abs(ph @ Bn) ** 2
        allowed = om_g > 0.3
        Pm = np.where(allowed, P, 0)
        io = int(np.argmax(Pm))
        if Pm[io] <= 0:
            continue
        do = qinterp(P[io - 1], P[io], P[io + 1]) if 0 < io < len(om_g) - 1 else 0.0
        out[float(k)] = float(om_g[io] + do * 0.05)
    return out


def e1p_phase(tcent, proj):
    out = {}
    for k, (Bn, cnt) in proj.items():
        good = (cnt >= 10) & (np.abs(Bn) > 0)
        if good.sum() < 8:
            continue
        tt_ = tcent[good]
        phi = np.unwrap(np.angle(Bn[good]))
        wgt = np.abs(Bn[good]) * np.sqrt(cnt[good])
        wgt = wgt / wgt.max()
        A = np.vstack([tt_, np.ones_like(tt_)]).T * wgt[:, None]
        y = phi * wgt
        (sl, b0), _, _, _ = np.linalg.lstsq(A, y, rcond=None)
        pred = sl * tt_ + b0
        ss = np.sum(wgt ** 2 * (phi - pred) ** 2)
        st = np.sum(wgt ** 2 * (phi - np.average(phi, weights=wgt ** 2)) ** 2)
        r2 = 1 - ss / st if st > 0 else 0.0
        if r2 > 0.8:
            out[float(k)] = float(abs(sl))
    return out


def dispersion_c(pts, W_sub, bulk_idx, L):
    """c = omega(k1)/k1 nos dois estimadores; k1 = 2pi/L (emenda declarada)."""
    k1 = 2 * np.pi / L
    if not (KRES - 1e-9 <= k1 <= KMAX + 1e-9):
        return None
    t = pts[:, 0]
    bulk = np.zeros(len(pts), bool); bulk[bulk_idx] = True

    def dxp(gi, gj, k, ax=None):
        acc = np.zeros(len(gi), complex)
        for a in (2, 3):
            dx = pts[gj, a] - pts[gi, a]
            dx = (dx + L / 2) % L - L / 2
            acc += np.exp(-1j * k * dx)
        return acc / 2.0

    tcent, proj = binned_proj(t, dxp, W_sub, bulk, [k1], TX, 0.10)
    om_max = KMAX + 4.0
    r2 = e2_peak(tcent, proj, TX, om_max)
    r1 = e1p_phase(tcent, proj)
    return dict(k1=float(k1),
                c_e2=(r2.get(k1, np.nan) / k1) if k1 in r2 else None,
                c_e1p=(r1.get(k1, np.nan) / k1) if k1 in r1 else None)


# ---------------- run por config ----------------
def measure_config(pts, Lk, edges, a, J, L, tag, mscale=1.0):
    n = len(a)
    H, Mx, clipf, e = hessian_and_mass(a, edges, J)
    # quântico: tripleto SJ
    A = idelta_triplet(Lk, Mx * mscale)
    lam, V = np.linalg.eigh(A)
    pr = pair_resid(lam)
    top = np.argsort(-lam)[:K_IR]
    dq, evq = dir_split(V, top, n)
    # dispersão (só L=3, massless-limit trace W)
    disp = None
    if L == 3.0 and mscale == 1.0:
        bulk_idx = np.where((np.abs(pts[:, 0]) <= 0.7 * TX)
                            & (np.abs(pts[:, 1]) <= 0.7 * TX))[0]
        b3 = np.repeat(3 * bulk_idx, 3) + np.tile([0, 1, 2], len(bulk_idx))
        posm = lam > 0
        Vb = V[np.ix_(b3, np.where(posm)[0])]
        Wb = (Vb * lam[posm]) @ Vb.conj().T
        nb = len(bulk_idx)
        Wtr = Wb.reshape(nb, 3, nb, 3)
        Wtr = (Wtr[:, 0, :, 0] + Wtr[:, 1, :, 1] + Wtr[:, 2, :, 2]) / 3.0
        disp = dispersion_c(pts, Wtr, bulk_idx, L)
        del Vb, Wb, Wtr
    del A, V
    gc.collect()
    # clássico: régua no MESMO funcional
    lh, Vh = np.linalg.eigh(H)
    nz = int(np.sum(np.abs(lh) < ZERO_TOL * np.abs(lh).max()))
    soft = [k for k in np.argsort(np.abs(lh))
            if np.abs(lh[k]) >= ZERO_TOL * np.abs(lh).max()][:K_IR]
    dcl, evc = dir_split(Vh.astype(complex), soft, n)
    del H, Vh
    gc.collect()
    trM = float(np.mean(np.trace(Mx, axis1=1, axis2=2)) / 3.0)
    return dict(tag=tag, J=J, L=float(L), n=n, mscale=mscale,
                delta_q=dq, delta_cl=dcl, evq=evq, evc=evc,
                pair_resid=pr, n_zeros=nz, clip_frac=clipf,
                trM_mean=trM, disp=disp)


def scalar_reference(pts, Lk, L):
    """c_scalar massless + diagnóstico Q2-forte (gaps) no mesmo substrato."""
    A = idelta_scalar(Lk)
    lam, V = np.linalg.eigh(A)
    pr = pair_resid(lam)
    lp = np.sort(lam[lam > 0])[::-1][:60]
    gaps = np.abs(np.diff(lp)) / np.mean(lp)
    out = dict(pair_resid=pr, min_gap_rel=float(gaps.min()),
               frac_gap_lt_1e6=float(np.mean(gaps < 1e-6)))
    if L == 3.0:
        bulk_idx = np.where((np.abs(pts[:, 0]) <= 0.7 * TX)
                            & (np.abs(pts[:, 1]) <= 0.7 * TX))[0]
        posm = lam > 0
        Vb = V[np.ix_(bulk_idx, np.where(posm)[0])]
        Wb = (Vb * lam[posm]) @ Vb.conj().T
        out["disp"] = dispersion_c(pts, Wb, bulk_idx, L)
    return out


def smoke_ideal_check(Lk):
    """Vácuo ideal: M=0 => tripleto = escalar x3 (degenerescência à máquina)."""
    n = Lk.shape[0]
    As = idelta_scalar(Lk)
    ls = np.linalg.eigvalsh(As)
    At = idelta_triplet(Lk, np.zeros((n, 3, 3)))
    lt = np.linalg.eigvalsh(At)
    err = float(np.max(np.abs(np.sort(np.repeat(ls, 3)) - np.sort(lt))))
    return err


# ---------------- agregação ----------------
def sem(v):
    v = np.asarray(v, float)
    return float(v.std(ddof=1) / np.sqrt(len(v))) if len(v) > 1 else float("nan")


def aggregate(rows):
    out = {"cells": {}}
    for J, jt in ((J_ORD, "ord"), (J_DIS, "dis")):
        for L in LS:
            sel = [r for r in rows if r["J"] == J and r["L"] == L
                   and r["mscale"] == 1.0]
            if not sel:
                continue
            dq = [r["delta_q"] for r in sel]
            dc = [r["delta_cl"] for r in sel]
            out["cells"][f"{jt}_L{L}"] = dict(
                n_cfg=len(sel),
                delta_q=[float(np.mean(dq)), sem(dq)],
                delta_cl=[float(np.mean(dc)), sem(dc)],
                ratio=float(np.mean(dq) / np.mean(dc)) if np.mean(dc) > 0 else None,
                clip_frac=float(np.mean([r["clip_frac"] for r in sel])),
                n_zeros=[r["n_zeros"] for r in sel][:4],
                trM_mean=float(np.mean([r["trM_mean"] for r in sel])),
                max_pair_resid=float(max(r["pair_resid"] for r in sel)))
    # ---- M2.2 / D3 (células ordenadas)
    d3_parts = {}
    excede = {}
    for L in LS:
        c = out["cells"].get(f"ord_L{L}")
        if not c:
            continue
        mq, sq = c["delta_q"]; mc, scl = c["delta_cl"]
        gap = mq - 3 * mc
        sg = np.sqrt(sq ** 2 + (3 * scl) ** 2)
        excede[L] = bool(gap > 2 * sg)
        d3_parts[f"L{L}"] = dict(delta_q=mq, delta_cl=mc, gap_3x=gap, sig=sg)
    nao_decresce = None
    if "ord_L2.0" in out["cells"] and "ord_L3.0" in out["cells"]:
        q2, s2 = out["cells"]["ord_L2.0"]["delta_q"]
        q3, s3_ = out["cells"]["ord_L3.0"]["delta_q"]
        s2 = 0.0 if not np.isfinite(s2) else s2
        s3_ = 0.0 if not np.isfinite(s3_) else s3_
        nao_decresce = bool(q3 >= q2 - 2 * np.sqrt(s2 ** 2 + s3_ ** 2))
    d3 = bool(all(excede.get(L, False) for L in LS) and bool(nao_decresce))
    out["M2_2"] = dict(D3=d3, excede_3x=excede, nao_decresce=nao_decresce,
                       detalhe=d3_parts)
    # robustez x4 (célula decisiva)
    r4 = [r for r in rows if r["J"] == J_ORD and r["L"] == 3.0
          and r["mscale"] == 4.0]
    if r4:
        dq4 = [r["delta_q"] for r in r4]
        m4 = float(np.mean(dq4))
        base = out["cells"]["ord_L3.0"]["delta_q"][0]
        cl3 = out["cells"]["ord_L3.0"]["delta_cl"][0]
        out["M2_2"]["robustez_x4"] = dict(
            delta_q_x4=m4, sem=sem(dq4),
            excede_3x_x4=bool(m4 > 3 * cl3),
            consistente=bool((m4 > 3 * cl3) == excede.get(3.0, False)))
    # ---- M2.1 (L=3 ordenado, single-k; régua absoluta)
    cs2 = [r["disp"]["c_e2"] for r in rows
           if r["J"] == J_ORD and r["L"] == 3.0 and r["mscale"] == 1.0
           and r.get("disp") and r["disp"].get("c_e2")]
    cs1 = [r["disp"]["c_e1p"] for r in rows
           if r["J"] == J_ORD and r["L"] == 3.0 and r["mscale"] == 1.0
           and r.get("disp") and r["disp"].get("c_e1p")]
    csc = [r["scalar_ref"]["disp"]["c_e2"] for r in rows
           if r.get("scalar_ref") and r["scalar_ref"].get("disp")
           and r["scalar_ref"]["disp"].get("c_e2")]
    if cs2 and csc:
        m2 = dict(c_goldstone_e2=[float(np.mean(cs2)), sem(cs2), len(cs2)],
                  c_goldstone_e1p=([float(np.mean(cs1)), sem(cs1), len(cs1)]
                                   if cs1 else None),
                  c_scalar_e2=[float(np.mean(csc)), sem(csc), len(csc)])
        dvs = abs(np.mean(cs2) - np.mean(csc))
        dee = abs(np.mean(cs2) - np.mean(cs1)) if cs1 else None
        m2["abs_dev_vs_scalar"] = float(dvs)
        m2["abs_dev_e2_e1p"] = float(dee) if dee is not None else None
        m2["passa"] = bool(dvs <= 0.10 and (dee is None or dee <= 0.10))
        m2["sanidade_c1"] = dict(gold=float(abs(np.mean(cs2) - 1)),
                                 scalar=float(abs(np.mean(csc) - 1)))
        out["M2_1"] = m2
    # ---- Q2-forte (gaps do escalar)
    gmins = [r["scalar_ref"]["min_gap_rel"] for r in rows if r.get("scalar_ref")]
    if gmins:
        out["Q2_forte"] = dict(
            min_gap_rel=float(min(gmins)),
            degenerescencia_exata=bool(min(gmins) < 1e-10),
            nota="esperado: nenhuma (Poisson sem simetria); Axioma 2 = postulado")
    return out


def main():
    t0 = time.time()
    rows = []
    if os.path.exists(ROWS_PATH) and not SMOKE:
        with open(ROWS_PATH, encoding="utf-8") as f:
            rows = [json.loads(l) for l in f if l.strip()]
        log(f"checkpoint: {len(rows)} rows")
    done = {r["tag"] for r in rows}

    for L in LS:
        for seed in range(NSEEDS):
            rng = np.random.default_rng(BASE_SEED + 811 * int(L) + seed)
            pts = nc.sprinkle(RHO, TX, L, 4, rng)
            g, Lk = hasse(pts, L)
            edges = g.edges
            log(f"substrato L={L} s={seed}: n={len(pts)} links={len(edges)}")
            if SMOKE:
                err = smoke_ideal_check(Lk)
                log(f"  SMOKE vácuo ideal: max|tripleto - escalar×3| = {err:.2e}")
            sref = None
            for J, jt in ((J_ORD, "ord"), (J_DIS, "dis")):
                base_tag = f"{jt}_L{L}_s{seed}"
                if all(f"{base_tag}_c{c}" in done for c in range(NCFG)) and not SMOKE:
                    continue
                mdl = sc.SUNChiralModel(g, 2, J=J, seed=BASE_SEED + 331 * seed
                                        + int(L) + (0 if J == J_ORD else 7))
                mdl.equilibrate(BURN, adapt=True)
                ms = []
                for cfg in range(NCFG):
                    for _ in range(SPACING):
                        mdl.sweep()
                        ms.append(mdl.order_parameter())
                    tag = f"{base_tag}_c{cfg}"
                    if tag in done:
                        continue
                    a = quat_of(mdl.U)
                    row = measure_config(pts, Lk, edges, a, J, L, tag)
                    tau, ess = sc.tau_int(np.array(ms))
                    row["m_order"] = float(ms[-1]); row["tau_int"] = tau
                    row["ess"] = ess
                    if sref is None and J == J_ORD:
                        sref = scalar_reference(pts, Lk, L)
                    if J == J_ORD and cfg == 0:
                        row["scalar_ref"] = sref
                    rows.append(row); emit(row)
                    log(f"  {tag}: m={row['m_order']:.3f} dq={row['delta_q']:.4f} "
                        f"dcl={row['delta_cl']:.4f} clip={row['clip_frac']:.3f} "
                        f"nz={row['n_zeros']} pr={row['pair_resid']:.0e}"
                        + (f" disp={row['disp']}" if row.get("disp") else ""))
                    # robustez x4 na célula decisiva
                    if J == J_ORD and L == 3.0 and not SMOKE:
                        tag4 = tag + "_x4"
                        if tag4 not in done:
                            row4 = measure_config(pts, Lk, edges, a, J, L,
                                                  tag4, mscale=4.0)
                            rows.append(row4); emit(row4)
                            log(f"  {tag4}: dq={row4['delta_q']:.4f}")
    out = dict(meta=dict(base_seed=BASE_SEED, smoke=SMOKE, rho=RHO, tx=TX,
                         Ls=LS, nseeds=NSEEDS, ncfg=NCFG, burn=BURN,
                         spacing=SPACING, J=[J_ORD, J_DIS], K_ir=K_IR,
                         c_clip=C_CLIP, kres=KRES, kmax=KMAX),
               verdicts=aggregate(rows), runtime_s=time.time() - t0)
    json.dump(out, open(OUT_PATH, "w", encoding="utf-8"), indent=1)
    v = out["verdicts"]
    log(f"FIM {out['runtime_s']:.0f}s | D3={v.get('M2_2', {}).get('D3')} "
        f"| M2.1={v.get('M2_1', {}).get('passa')}")


if __name__ == "__main__":
    main()
