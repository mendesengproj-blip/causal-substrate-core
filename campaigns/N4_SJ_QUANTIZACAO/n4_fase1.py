# -*- coding: utf-8 -*-
"""
N4 — FASE 1: vácuo SJ do escalar livre no substrato-caixa do programa.
Pré-registro §5 (grades/medições) + §7 (janelas) + §8 (mortes D1/D2) +
lições do Gate G (GATE_G_RESULTADO §4: E2-COM primário; sinal massivo J₀;
validação dois-estimadores do gap MIGRADA para cá = M1.3).

DECLARAÇÃO PRÉ-RUN (commitada antes de executar; nenhum critério muda depois):

GEOMETRIA (congelada agora — aspecto não fixado no pré-reg):
  EMENDA PRÉ-RUN (achada pelo smoke, declarada antes do run real): no cilindro
  o G_R massless = ½C SÓ vale sem enrolamento (além de Δt = L_x/2 o propagador
  verdadeiro é a soma de imagens ½·N_img; smoke com T=1.5,L_x=2 deu modos fora
  da shell — sintoma). Geometria re-congelada na fronteira SEM-ENROLAMENTO
  2T ≤ L_x/2, onde ordem min-imagem e ½C são EXATOS (e N_img é não-intrínseco,
  logo proibido pela higiene anti-circularidade — a saída certa é a geometria).
  d=2: cilindro t ∈ [−1, 1] × x ∈ S¹ de circunferência L_x=4 (min-imagem
       na ordem). V=8. N ∈ {1024, 2048, 4096} ⇒ ρ = {128, 256, 512}
       (varrida ×4, como pré-registrado). 12 seeds (BASE 20260702).
       Modos k_n = πn/2; janela n ∈ {2..11}/{2..16}/{2..22}; m_ctrl = 3π/2.
       d=4 já estava na fronteira sem-enrolamento (2T = L/2 toca imagens só
       em medida nula no cone) — inalterado.
  d=4: laje t ∈ [−T, T] × toro [0,L)³, aspecto 2T = L/2 congelado.
       ρ=8 ⇒ L=(N/4)^{1/4}: N=2000: L=4.729; 4000: 5.623; 8000: 6.687. 12 seeds.
  Ordem: i ≺ j ⇔ Δt > |Δx⃗|_min-imagem (estrita). Bulk: |t| ≤ 0.7·T (15% de
  cada borda-t; toro não tem borda espacial).

PROPAGADORES (Fase 0 §4.1 + erratum Gate G):
  d=2 massless G_R = ½C^T; massivo ½C^T(I + (m²/2ρ)C^T)^{-1} [J₀ alternante].
  d=4 massless G_R = aL^T, a=(1/2π)√(ρ/6); massivo aL^T(I + (m²a/ρ)L^T)^{-1}.
  iΔ = i(G_R − G_R^T); W_SJ = Pos(iΔ).

JANELA IR (§7, congelada): k ∈ [2·(2π/L_x), 0.25·2π·ρ^{1/d}], modos exatos do
  toro k_n = 2πn/L_x:
  d=2 (k_n = πn): n ∈ {2..6} / {2..9} / {2..13} por tamanho.
  d=4 (k_n = 2πn/L): k_max = 2.643; N=2000: JANELA VAZIA (k_2=2.657>k_max —
  declarado: N=2000 só contribui p/ M1.1/M1.4); N=4000: n=2 (2.235);
  N=8000: n=2 (1.879). Fit c em d=4 = UNIÃO dos pontos entre tamanhos
  (c é adimensional e independente de L; declarado).

ESTIMADORES (§7 + lição Gate G):
  E2 (PRIMÁRIO, média de COM): pares de bulk projetados em e^{−ik_nΔx}
    (min-imagem; d=4: 3 eixos agregados por isotropia), binados em Δt
    (h=0.05 d=2 / 0.10 d=4), janela de Hann, FT → pico ω*(k_n) com
    interpolação quadrática (busca ω > 0.3).
  E1 (SECUNDÁRIO, mode-side): top-100 modos SJ; projeção EXATA nos k_n do
    toro; n dominante por potência; ω_q = pico da FT temporal; proeminência
    ≥ 25× mediana; ω*(k_n) = mediana dos modos aceitos naquele n (≥2 modos).
  Fits ponderados: σ_ω = π/(1.4·T) (resolução de Hann da janela Δt usada).
  massless: ω = c·k pela origem; massivo: ω² = c²k² + m² (2 par.; d=4: c
  FIXADO no valor massless d=4 — 1 só k na janela; declarado).

MEDIÇÕES E CRITÉRIOS:
  M1.1 estabilidade (D1): resíduo de pareamento ±λ < 1e-10 em TODOS os
    runs; deriva da inclinação da torre (n=4..40) entre tamanhos consecutivos
    ≤ 0.10 (d=2) / 0.20 (d=4); fração de kernel numérico reportada.
    D1 = pareamento falha OU deriva estoura (com gate G verde = morte).
  M1.2 dispersão (D2): d=2: |c_E2 − 1| ≤ 0.15 E |c_E1 − c_E2| ≤ 2σ comb.
    d=4: |c_E2 − 1| ≤ 0.20 (ressalva de janela declarada: 2 pontos k).
    D2 = em d=2, os DOIS estimadores com ridge e ambos |c−1| > 0.15, OU
    nenhum ridge nos dois. d=4 falhando com d=2 passando = TENSÃO reportada
    (investigação antes de morte; janela estreita declarada).
  M1.3 controle massivo (validação migrada do Gate G): d=2, N=2048,
    m = 3·(2π/L_x) = 3π ≈ 9.4248: |m_fit/m − 1| ≤ 0.15 nos DOIS estimadores
    E concordância 2σ. d=4, N=4000, m = 3·(2π/L) = 3.352: reportado
    (resolução π/(1.4T) ≈ 1.6 comparável ao gap — INCONCLUSIVO-por-resolução
    é saída declarada, não morte).
  M1.4 densidade espectral: inclinação da torre + localização do desvio UV
    vs ρ^{1/d} — REPORTADO, sem critério de morte (pré-reg).
  BD cross-check (N-hig 2, robustez, NÃO morte): d=2, N=2048, massless,
    2º operador = d'Alembertiano BD suavizado retardado (ε=0.25, kernel
    smeared_weight do C5 validado; nível de FORMA — dispersão independe de
    normalização): B̃ = −½I + ε·K_ret, G_BD = B̃^{-1}; c_BD pelo E2:
    consistência |c_BD − c_E2^Johnston| ≤ 2σ reportada.

EMENDAS DE INSTRUMENTO (declaradas pré-run; eigenproblem SJ do cilindro-laje
resolvido no papel: kernel rank-2 por k, modos EXATAMENTE on-shell ω=k,
λ=√(CS)/k, C,S = T ± sin(2kT)/2k; top λ medidos batem: zero-modo k=0
λ=ρ·2/√3≈144 e n=1 λ=ρ/k≈82 — espectro CERTO; o desvio era JANELAMENTO):
  1. PISO DE RESOLUÇÃO nos fits: só pontos com k ≥ k_res = 2π/(1.4·T)
     (modo com kT < 2π não completa ciclo na laje; pico de Fourier desaba
     p/ ω≈0 — viés de janela, não física). d=2: n ≥ 3.
  2. E1 mode-side SUBSTITUÍDO por E1′ = FASE (emenda declarada, 3ª ocorrência
     da lição mode-side): o eigenproblem contínuo mostra que modos com kT~π
     são misturas elípticas de e^{±ikt} (coef √(C/S)) e no discreto hibridizam
     com a pilha UV pós-joelho (debug commitado: 0/30 modos aceitos, ω de
     modos individuais é ruído). E1′ = inclinação da FASE desembrulhada da
     MESMA W̃(Δt,k_n) projetada (família "FT de W em bins" do §7; extração no
     domínio do TEMPO: ω̂ = |dφ/dΔt| por LSQ ponderado em |B|·√cnt, aceito se
     R²_fase > 0.8) — patologias opostas ao pico de potência do E2 (imune a
     vazamento; sem piso de resolução próprio, mas o piso k_res é mantido
     uniforme nos DOIS por disciplina). Caveat declarado: E1′/E2 compartilham
     o binning; a independência total de instrumento vem do BD cross-check.
     Mode-side fica DOCUMENTADO como diagnóstico (não computado nos runs).
  3. d=4: {2000,4000,8000} só M1.1/M1.4 (conta no papel: k_res > k_max —
     janelas sub-resolução com o vínculo sem-enrolamento 2T=L/2; mínimo p/
     resolver n=3 é L>6.79 ⇔ N>8500); DISPERSÃO d=4 = N=16000, 6 seeds,
     Lanczos top-200 (cláusula do pré-reg agora NECESSÁRIA), W parcial p/
     E2; massivo idem (c fixado do massless). Fallback por MemoryError:
     N=12000 (n=3 ainda resolvível: k=2.55 > k_res=2.43).
SAÍDAS: n4_fase1_rows.jsonl (checkpoint por run) + n4_fase1.json (agregado).
Flags: --smoke (máquina), --d2 (só d=2), --d4 (só d=4).
"""
import json, os, sys, time, gc
import numpy as np

BASE_SEED = 20260702
NSEEDS = 12
SMOKE = "--smoke" in sys.argv
ONLY_D2 = "--d2" in sys.argv
ONLY_D4 = "--d4" in sys.argv

# geometria d=2
T2, LX2 = 1.0, 4.0
SIZES2 = [1024, 2048, 4096]
M2_CTRL_N = 2048
M2_IN = 3.0 * 2 * np.pi / LX2          # 3π

# geometria d=4
SIZES4 = [2000, 4000, 8000]
RHO4 = 8.0
M4_CTRL_N = 4000
EPS_BD = 0.25

if SMOKE:
    SIZES2 = [512]; SIZES4 = [1000]; NSEEDS = 2
    M2_CTRL_N = 512; M4_CTRL_N = 1000

ROWS_PATH = "n4_fase1_rows_smoke.jsonl" if SMOKE else "n4_fase1_rows.jsonl"
OUT_PATH = "n4_fase1_smoke.json" if SMOKE else "n4_fase1.json"

def log(m): print(f"[{time.strftime('%H:%M:%S')}] {m}", flush=True)

def emit(row):
    with open(ROWS_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(row) + "\n")

def qinterp(y0, y1, y2):
    d = y0 - 2 * y1 + y2
    return 0.0 if abs(d) < 1e-30 else 0.5 * (y0 - y2) / d

# ---------------- substratos ----------------
def sprinkle_d2(N, rng):
    t = rng.uniform(-T2, T2, N)
    x = rng.uniform(0, LX2, N)
    o = np.argsort(t)
    return t[o], x[o]

def order_d2(t, x):
    dt = t[None, :] - t[:, None]
    dx = np.abs(x[None, :] - x[:, None])
    dx = np.minimum(dx, LX2 - dx)
    return dt > dx

def sprinkle_d4(N, rng):
    Lb = (N / 4.0) ** 0.25
    Tb = Lb / 4.0
    t = rng.uniform(-Tb, Tb, N)
    xs = rng.uniform(0, Lb, (N, 3))
    o = np.argsort(t)
    return t[o], xs[o], Lb, Tb

def order_d4(t, xs, Lb):
    dt = t[None, :] - t[:, None]
    d2 = np.zeros_like(dt)
    for a in range(3):
        dxa = np.abs(xs[None, :, a] - xs[:, None, a])
        dxa = np.minimum(dxa, Lb - dxa)
        d2 += dxa * dxa
    return dt > np.sqrt(d2)

def links_of(C):
    Cf = C.astype(np.float32)
    two = (Cf @ Cf) > 0.5
    return C & ~two

# ---------------- iDelta ----------------
def idelta_d2(C, m2=0.0, rho=None):
    CT = C.T.astype(np.float64)
    if m2 == 0.0:
        GR = 0.5 * CT
    else:
        a = m2 / (2.0 * rho)
        GR = 0.5 * np.linalg.solve((np.eye(CT.shape[0]) + a * CT).T, CT.T).T
    return 1j * (GR - GR.T)

def idelta_d4(C, rho, m2=0.0):
    Lk = links_of(C)
    LT = Lk.T.astype(np.float64)
    a = (1.0 / (2 * np.pi)) * np.sqrt(rho / 6.0)
    if m2 == 0.0:
        GR = a * LT
    else:
        b = m2 * a / rho
        GR = a * np.linalg.solve((np.eye(LT.shape[0]) + b * LT).T, LT.T).T
    return 1j * (GR - GR.T)

def idelta_bd_d2(C):
    Cf = C.astype(np.float32)
    M2 = (Cf @ Cf).astype(np.float64)      # M2[i,j] = #{z: i<z<j}
    eps = EPS_BD
    m = M2.T                                # card. p/ par (x recebe de y<x)
    W = ((1 - eps) ** m
         - 2 * m * eps * (1 - eps) ** (m - 1)
         + (m * (m - 1) / 2.0) * eps ** 2 * (1 - eps) ** (m - 2))
    K = np.where(C.T, W, 0.0)
    B = -0.5 * np.eye(C.shape[0]) + eps * K
    G = np.linalg.inv(B)
    return 1j * (G - G.T)

# ---------------- métricas espectrais (M1.1 / M1.4) ----------------
def spec_stats(lam):
    s = np.sort(lam)
    pr = float(np.max(np.abs(s + s[::-1])) / np.max(np.abs(s)))
    lp = np.sort(lam[lam > 0])[::-1]
    n = np.arange(1, len(lp) + 1)
    msk = (n >= 4) & (n <= 40)
    slope = float(np.polyfit(np.log(n[msk]), np.log(lp[msk]), 1)[0])
    kerfrac = float(np.mean(np.abs(lam) < 1e-8 * np.abs(lam).max()))
    # M1.4: joelho da torre = onde a inclinação local dobra (janela móvel)
    ll, ln = np.log(lp[:min(len(lp), 400)]), np.log(n[:min(len(lp), 400)])
    bend = None
    w = 8
    for i0 in range(4, len(ll) - 2 * w):
        s1 = np.polyfit(ln[i0:i0 + w], ll[i0:i0 + w], 1)[0]
        s2 = np.polyfit(ln[i0 + w:i0 + 2 * w], ll[i0 + w:i0 + 2 * w], 1)[0]
        if s2 < 2.0 * slope and s1 > 1.5 * slope:
            bend = int(i0 + w); break
    return dict(pair_resid=pr, slope=slope, kernel_frac=kerfrac, bend_n=bend)

# ---------------- projeção binada compartilhada ----------------
def binned_proj(tt, dxproj_fn, W, bulk, kvals, Tbox, h):
    """W̃(Δt, k_n): projeção dos pares de bulk em e^{-ik dx}, binada em Δt.
    Retorna (tcent, {k: (B, cnt)})."""
    idx = np.where(bulk)[0]
    i, j = np.triu_indices(len(idx), k=1)
    gi, gj = idx[i], idx[j]
    dt = tt[gj] - tt[gi]
    Wv = W[gi, gj]
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
        B = np.where(cnt > 0, acc / np.maximum(cnt, 1), 0)
        out[float(k)] = (B, cnt)
    return tcent, out

# ---------------- E2: pico de potência (Hann) ----------------
def e2_ridge_from(tcent, proj, Tbox, om_max):
    tmax = 1.4 * Tbox
    om_g = np.arange(0.0, om_max, 0.05)
    hann = 0.5 * (1 + np.cos(np.pi * tcent / tmax))
    ph = np.exp(1j * om_g[:, None] * tcent[None, :]) * hann[None, :]
    out = {}
    for k, (B, cnt) in proj.items():
        P = np.abs(ph @ B) ** 2
        allowed = om_g > 0.3
        Pm = np.where(allowed, P, 0)
        io = int(np.argmax(Pm))
        if Pm[io] <= 0:
            continue
        do = qinterp(P[io - 1], P[io], P[io + 1]) if 0 < io < len(om_g) - 1 else 0.0
        out[float(k)] = float(om_g[io] + do * 0.05)
    return out

# ---------------- E1': inclinação de fase (domínio do tempo) ----------------
def e1p_ridge_from(tcent, proj):
    out = {}
    for k, (B, cnt) in proj.items():
        good = (cnt >= 10) & (np.abs(B) > 0)
        if good.sum() < 8:
            continue
        tt_ = tcent[good]
        phi = np.unwrap(np.angle(B[good]))
        wgt = np.abs(B[good]) * np.sqrt(cnt[good])
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

# ---------------- E1: dispersão mode-side ----------------
def e1_ridge(tt, xproj_fn, lam, V, kvals, om_max, top=100, kall=None):
    """kall = candidatos ampliados (inclui fora da janela) p/ atribuição
    honesta do k dominante; o ponto só entra se o k atribuído ∈ janela."""
    om_g = np.arange(0.0, om_max, 0.05)
    idx = np.argsort(-lam)[:top]
    cand = kall if kall is not None else kvals
    pts = {}
    for q in idx:
        w = V[:, q]
        best = (0.0, None, None)
        for k in cand:
            z = w * xproj_fn(k)
            s = np.abs(np.exp(1j * om_g[:, None] * tt[None, :]) @ z) ** 2
            pk = s.max()
            if pk > best[0]:
                best = (pk, k, s)
        pk, k, s = best
        if k is None or k not in kvals or pk < 25.0 * np.median(s):
            continue
        io = int(np.argmax(s))
        if not (0 < io < len(om_g) - 1) or om_g[io] <= 0.3:
            continue
        do = qinterp(s[io - 1], s[io], s[io + 1])
        pts.setdefault(float(k), []).append(float(om_g[io] + do * 0.05))
    return {k: float(np.median(v)) for k, v in pts.items() if len(v) >= 2}

# ---------------- fits ----------------
def fit_c(ridge, sig, kmin=0.0):
    ridge = {k: v for k, v in ridge.items() if k >= kmin - 1e-9}
    ks = np.array(sorted(ridge)); om = np.array([ridge[k] for k in ks])
    if len(ks) < 1: return None
    wgt = 1.0 / sig ** 2
    c = float(np.sum(wgt * ks * om) / np.sum(wgt * ks * ks))
    return dict(c=c, npts=int(len(ks)),
                ridge={f"{k:.4f}": float(o) for k, o in ridge.items()})

def fit_m(ridge, sig, c_fixed=None, kmin=0.0):
    ridge = {k: v for k, v in ridge.items() if k >= kmin - 1e-9}
    ks = np.array(sorted(ridge)); om = np.array([ridge[k] for k in ks])
    if len(ks) < 1: return None
    if c_fixed is not None or len(ks) < 2:
        c2 = (c_fixed if c_fixed is not None else 1.0) ** 2
        m2 = float(np.mean(om ** 2 - c2 * ks ** 2))
        return dict(m=float(np.sqrt(max(m2, 0))), c=float(np.sqrt(c2)),
                    npts=int(len(ks)), c_fixed=True,
                    ridge={f"{k:.4f}": float(o) for k, o in ridge.items()})
    sw = 2 * om * sig
    A = np.vstack([ks ** 2, np.ones_like(ks)]).T / sw[:, None]
    y = om ** 2 / sw
    (c2, m2), _, _, _ = np.linalg.lstsq(A, y, rcond=None)
    return dict(m=float(np.sqrt(max(m2, 0))), c=float(np.sqrt(max(c2, 0))),
                npts=int(len(ks)), c_fixed=False,
                ridge={f"{k:.4f}": float(o) for k, o in ridge.items()})

# ---------------- runs ----------------
def kwindow_d2(rho):
    kmax = 0.25 * 2 * np.pi * np.sqrt(rho)
    ns = [n for n in range(2, 40) if 2 * np.pi * n / LX2 <= kmax]
    return [2 * np.pi * n / LX2 for n in ns]

def run_d2(N, seed, m2=0.0, op="johnston"):
    rho = N / (2 * T2 * LX2)
    rng = np.random.default_rng(BASE_SEED + 10 * N + seed)
    t, x = sprinkle_d2(N, rng)
    C = order_d2(t, x)
    if op == "bd":
        A = idelta_bd_d2(C)
    else:
        A = idelta_d2(C, m2=m2, rho=rho)
    lam, V = np.linalg.eigh(A)
    st = spec_stats(lam)
    posm = lam > 0
    Wm = (V[:, posm] * lam[posm]) @ V[:, posm].conj().T
    bulk = np.abs(t) <= 0.7 * T2
    kv = kwindow_d2(rho)
    om_max = max(kv) + (np.sqrt(m2) if m2 > 0 else 0) + 6.0

    def dxp(gi, gj, k):
        dx = x[gj] - x[gi]
        dx = (dx + LX2 / 2) % LX2 - LX2 / 2
        return np.exp(-1j * k * dx)

    tcent, proj = binned_proj(t, dxp, Wm, bulk, kv, T2, 0.05)
    r2 = e2_ridge_from(tcent, proj, T2, om_max)
    r1 = e1p_ridge_from(tcent, proj)
    del A, V, Wm
    gc.collect()
    sig = np.pi / (1.4 * T2)
    kres = 2 * np.pi / (1.4 * T2)
    if m2 == 0.0:
        f2 = fit_c(r2, sig, kmin=kres); f1 = fit_c(r1, sig, kmin=kres)
    else:
        f2 = fit_m(r2, sig, kmin=kres); f1 = fit_m(r1, sig, kmin=kres)
    return dict(d=2, N=N, seed=seed, m_in=float(np.sqrt(m2)), op=op,
                spec=st, e2=f2, e1=f1)

def kwindow_d4(Lb):
    kmax = 0.25 * 2 * np.pi * RHO4 ** 0.25
    kmin = 2 * 2 * np.pi / Lb
    ns = [n for n in range(2, 8) if kmin - 1e-9 <= 2 * np.pi * n / Lb <= kmax]
    return [2 * np.pi * n / Lb for n in ns]

D4_DISP_N = 16000
# Seeds da dispersão d=4: lista EXPLÍCITA (era range(6)). Seed 1 EXCLUÍDA:
# ARPACK não converge nela (>5h34 com tol=0 + >1h54 com tol=1e-7; espectro
# aglomerado) — cláusula de orçamento §9; seed de INSTRUMENTO (sorteio do
# sprinkling), não de física; substituída pela seed 6 p/ manter 6 seeds.
D4_DISP_SEEDLIST = [0, 2, 3, 4, 5, 6]

def run_d4_disp(N, seed, m2=0.0):
    """Dispersão d=4 via Lanczos top-200 (W parcial)."""
    from scipy.sparse.linalg import eigsh, LinearOperator
    rng = np.random.default_rng(BASE_SEED + 10 * N + 5 + seed)
    t, xs, Lb, Tb = sprinkle_d4(N, rng)
    C = order_d4(t, xs, Lb)
    Lk = links_of(C)
    del C
    gc.collect()
    LT = Lk.T.astype(np.float32)
    del Lk
    a = (1.0 / (2 * np.pi)) * np.sqrt(RHO4 / 6.0)
    if m2 == 0.0:
        GR = a * LT
    else:
        b = m2 * a / RHO4
        GR = a * np.linalg.solve((np.eye(N, dtype=np.float32) + b * LT).T, LT.T).T
    del LT
    gc.collect()
    # v4: diagonalizacao DENSA parcial (LAPACK evr, top-200) no lugar do
    # ARPACK — 2 de 3 seeds nao convergiam (espectro aglomerado do iDelta:
    # >5h34 s=1 tol=0, >1h54 s=1 tol=1e-7, >3h s=2) = patologia SISTEMATICA
    # do Lanczos neste operador, nao seed ruim. Metodo de diagonalizacao =
    # instrumento; criterios e janelas INALTERADOS. Tempo deterministico.
    from scipy.linalg import eigh as dense_eigh
    Amat = (1j * (GR - GR.T)).astype(np.complex64)
    del GR
    gc.collect()
    lam, V = dense_eigh(Amat, subset_by_index=[N - 200, N - 1],
                        driver="evr", overwrite_a=True)
    del Amat
    gc.collect()
    o = np.argsort(-lam)
    lam, V = lam[o], V[:, o]
    bulk = np.abs(t) <= 0.7 * Tb
    kres4 = 2 * np.pi / (1.4 * Tb)
    kv = [k for k in kwindow_d4(Lb) if k >= kres4 - 1e-9]
    om_max = (max(kv) + (np.sqrt(m2) if m2 > 0 else 0) + 4.0) if kv else 8.0
    posm = lam > 0
    Wm = (V[:, posm] * lam[posm]) @ V[:, posm].conj().T
    ridge2_ax, ridge1_ax = {}, {}
    for ax in range(3):
        def dxp(gi, gj, k, ax=ax):
            dx = xs[gj, ax] - xs[gi, ax]
            dx = (dx + Lb / 2) % Lb - Lb / 2
            return np.exp(-1j * k * dx)
        tcent, proj = binned_proj(t, dxp, Wm, bulk, kv, Tb, 0.10)
        r2 = e2_ridge_from(tcent, proj, Tb, om_max)
        for k, o2 in r2.items():
            ridge2_ax.setdefault(k, []).append(o2)
        r1 = e1p_ridge_from(tcent, proj)
        for k, o2 in r1.items():
            ridge1_ax.setdefault(k, []).append(o2)
    del V, Wm
    gc.collect()
    r2m = {k: float(np.mean(v)) for k, v in ridge2_ax.items()}
    r1m = {k: float(np.mean(v)) for k, v in ridge1_ax.items()}
    return dict(d=4, N=N, seed=seed, m_in=float(np.sqrt(m2)), op="lanczos",
                Lb=float(Lb), Tb=float(Tb),
                spec=dict(pair_resid=float("nan"), slope=float("nan"),
                          kernel_frac=float("nan"), bend_n=None, partial=True),
                e2=dict(ridge={f"{k:.4f}": v for k, v in r2m.items()}),
                e1=dict(ridge={f"{k:.4f}": v for k, v in r1m.items()}),
                sig_om=float(np.pi / (1.4 * Tb)))

def run_d4(N, seed, m2=0.0):
    rng = np.random.default_rng(BASE_SEED + 10 * N + 5 + seed)
    t, xs, Lb, Tb = sprinkle_d4(N, rng)
    C = order_d4(t, xs, Lb)
    A = idelta_d4(C, RHO4, m2=m2)
    lam, V = np.linalg.eigh(A)
    st = spec_stats(lam)
    del A, V
    gc.collect()
    return dict(d=4, N=N, seed=seed, m_in=float(np.sqrt(m2)), op="johnston",
                Lb=float(Lb), Tb=float(Tb), spec=st,
                e2=dict(ridge={}), e1=dict(ridge={}),
                sig_om=float(np.pi / (1.4 * Tb)))

# ---------------- agregação ----------------
def sem(a):
    a = np.asarray(a, float)
    return float(a.std(ddof=1) / np.sqrt(len(a))) if len(a) > 1 else float("nan")

def aggregate(rows):
    out = {}
    # ---- M1.1 (D1)
    prs = [r["spec"]["pair_resid"] for r in rows]
    d1_pair = max(prs) < 1e-10
    drift_ok, drifts = True, {}
    for d, sizes, tol in ((2, SIZES2, 0.10), (4, SIZES4, 0.20)):
        sl = {}
        for N in sizes:
            v = [r["spec"]["slope"] for r in rows
                 if r["d"] == d and r["N"] == N and r["m_in"] == 0 and r["op"] == "johnston"]
            if v: sl[N] = float(np.mean(v))
        ks = sorted(sl)
        for a, b in zip(ks, ks[1:]):
            drifts[f"d{d}:{a}->{b}"] = sl[b] - sl[a]
            if abs(sl[b] - sl[a]) > tol: drift_ok = False
    out["M1_1"] = dict(passa=bool(d1_pair and drift_ok),
                       max_pair_resid=float(max(prs)), drifts=drifts,
                       D1=bool(not (d1_pair and drift_ok)))
    # ---- M1.2 d=2 (D2)
    for est in ("e2", "e1"):
        cs = [r[est]["c"] for r in rows
              if r["d"] == 2 and r["m_in"] == 0 and r["op"] == "johnston"
              and r.get(est) and "c" in r[est]]
        out[f"M1_2_d2_{est}"] = dict(c=float(np.mean(cs)), sem=sem(cs), n=len(cs)) if cs else None
    c2, c1 = out["M1_2_d2_e2"], out["M1_2_d2_e1"]
    ok2 = c2 and abs(c2["c"] - 1) <= 0.15
    ok1 = c1 and abs(c1["c"] - 1) <= 0.15
    conc = (c2 and c1 and
            abs(c2["c"] - c1["c"]) <= 2 * np.sqrt((c2["sem"] or 0) ** 2 + (c1["sem"] or 0) ** 2))
    out["M1_2_d2"] = dict(passa=bool(ok2 and conc), D2=bool(not ok2 and not ok1))
    # ---- M1.2 d=4 (união entre tamanhos, por seed onde possível)
    pts = {}
    for r in rows:
        if r["d"] == 4 and r["m_in"] == 0 and r["op"] == "lanczos":
            for kk, oo in r["e2"]["ridge"].items():
                pts.setdefault(float(kk), []).append(oo)
    if pts:
        ks = np.array(sorted(pts))
        oms = np.array([np.mean(pts[k]) for k in ks])
        c4 = float(np.sum(ks * oms) / np.sum(ks * ks))
        out["M1_2_d4"] = dict(c=c4, npts=int(len(ks)),
                              ridge={f"{k:.4f}": [float(np.mean(pts[k])), sem(pts[k])] for k in ks},
                              passa=bool(abs(c4 - 1) <= 0.20))
    # ---- M1.3 d=2 (validação migrada)
    for est in ("e2", "e1"):
        ms = [r[est]["m"] for r in rows
              if r["d"] == 2 and r["m_in"] > 0 and r.get(est) and "m" in r[est]]
        out[f"M1_3_d2_{est}"] = dict(m=float(np.mean(ms)), sem=sem(ms), n=len(ms),
                                     m_in=M2_IN, dev=float(np.mean(ms) / M2_IN - 1)) if ms else None
    m2r, m1r = out["M1_3_d2_e2"], out["M1_3_d2_e1"]
    okm2 = m2r and abs(m2r["dev"]) <= 0.15
    okm1 = m1r and abs(m1r["dev"]) <= 0.15
    concm = (m2r and m1r and
             abs(m2r["m"] - m1r["m"]) <= 2 * np.sqrt((m2r["sem"] or 0) ** 2 + (m1r["sem"] or 0) ** 2))
    out["M1_3_d2"] = dict(passa=bool(okm2 and okm1 and concm))
    # ---- M1.3 d=4 (reportado; c fixado do massless d=4)
    c4v = out.get("M1_2_d4", {}).get("c", 1.0)
    pts4 = {}
    m4in_v = [r["m_in"] for r in rows if r["d"] == 4 and r["m_in"] > 0]
    for r in rows:
        if r["d"] == 4 and r["m_in"] > 0 and r["op"] == "lanczos":
            for kk, oo in r["e2"]["ridge"].items():
                pts4.setdefault(float(kk), []).append(oo)
    if pts4:
        ks = np.array(sorted(pts4)); oms = np.array([np.mean(pts4[k]) for k in ks])
        m2fit = np.mean(oms ** 2 - c4v ** 2 * ks ** 2)
        m4in = float(np.mean(m4in_v)) if m4in_v else float("nan")
        out["M1_3_d4"] = dict(m=float(np.sqrt(max(m2fit, 0))), m_in=float(m4in),
                              c_fixed=float(c4v), npts=int(len(ks)), gated=False)
    # ---- M1.4 (reportado)
    m14 = {}
    for d in (2, 4):
        for N in (SIZES2 if d == 2 else SIZES4):
            v = [r["spec"] for r in rows
                 if r["d"] == d and r["N"] == N and r["m_in"] == 0 and r["op"] == "johnston"]
            if v:
                m14[f"d{d}_N{N}"] = dict(
                    slope=float(np.mean([s["slope"] for s in v])),
                    bend_n=[s["bend_n"] for s in v],
                    kernel_frac=float(np.mean([s["kernel_frac"] for s in v])))
    out["M1_4"] = m14
    # ---- BD cross-check
    cbds = [r["e2"]["c"] for r in rows
            if r["d"] == 2 and r["op"] == "bd" and r.get("e2") and "c" in r["e2"]]
    if cbds:
        cb, sb = float(np.mean(cbds)), sem(cbds)
        cj = out["M1_2_d2_e2"]
        out["BD_check"] = dict(c_bd=cb, sem=sb, n=len(cbds),
                               consistent=bool(abs(cb - cj["c"]) <= 2 * np.sqrt(sb ** 2 + (cj["sem"] or 0) ** 2)))
    # ---- veredito global
    out["D1"] = out["M1_1"]["D1"]
    out["D2"] = out["M1_2_d2"]["D2"]
    out["PASSA_FASE1"] = bool(out["M1_1"]["passa"] and out["M1_2_d2"]["passa"]
                              and out["M1_3_d2"]["passa"] and not out["D1"] and not out["D2"])
    return out

def main():
    t0 = time.time()
    rows = []
    if os.path.exists(ROWS_PATH) and not SMOKE:
        with open(ROWS_PATH, encoding="utf-8") as f:
            rows = [json.loads(l) for l in f if l.strip()]
        done = {(r["d"], r["N"], r["seed"], r["m_in"], r["op"]) for r in rows}
        log(f"checkpoint: {len(rows)} rows carregadas")
    else:
        done = set()

    def want(d, N, seed, m_in, op):
        return (d, N, seed, m_in, op) not in done

    if not ONLY_D4:
        for N in SIZES2:
            for s in range(NSEEDS):
                if want(2, N, s, 0.0, "johnston"):
                    r = run_d2(N, s); rows.append(r); emit(r)
                    log(f"d2 N={N} s={s}: slope={r['spec']['slope']:.3f} "
                        f"c_E2={r['e2']['c'] if r['e2'] else None} c_E1={r['e1']['c'] if r['e1'] else None}")
        for s in range(NSEEDS):
            if want(2, M2_CTRL_N, s, float(M2_IN), "johnston"):
                r = run_d2(M2_CTRL_N, s, m2=M2_IN ** 2); rows.append(r); emit(r)
                log(f"d2 massivo s={s}: m_E2={r['e2']['m'] if r['e2'] else None} "
                    f"m_E1={r['e1']['m'] if r['e1'] else None} (alvo {M2_IN:.3f})")
            if want(2, M2_CTRL_N, s, 0.0, "bd"):
                r = run_d2(M2_CTRL_N, s, op="bd"); rows.append(r); emit(r)
                log(f"d2 BD s={s}: c_BD={r['e2']['c'] if r['e2'] else None}")
    if not ONLY_D2:
        for N in SIZES4:
            for s in range(NSEEDS):
                if want(4, N, s, 0.0, "johnston"):
                    r = run_d4(N, s); rows.append(r); emit(r)
                    log(f"d4 N={N} s={s}: slope={r['spec']['slope']:.3f} ridge2={r['e2']['ridge']}")
        if not SMOKE:
            Nd = D4_DISP_N
            m4 = 3 * 2 * np.pi / (Nd / 4.0) ** 0.25
            for s in D4_DISP_SEEDLIST:
                for mm in (0.0, m4):
                    if want(4, Nd, s, float(mm), "lanczos"):
                        try:
                            r = run_d4_disp(Nd, s, m2=(mm ** 2 if mm else 0.0))
                        except MemoryError:
                            log("MemoryError -> fallback N=12000 (declarado)")
                            Nd = 12000
                            m4 = 3 * 2 * np.pi / (Nd / 4.0) ** 0.25
                            r = run_d4_disp(Nd, s, m2=(mm ** 2 if mm else 0.0))
                        rows.append(r); emit(r)
                        log(f"d4 disp N={Nd} s={s} m={mm:.3f}: e2={r['e2']['ridge']} e1={r['e1']['ridge']}")

    out = dict(meta=dict(base_seed=BASE_SEED, smoke=SMOKE, T2=T2, LX2=LX2,
                         sizes2=SIZES2, sizes4=SIZES4, rho4=RHO4,
                         m2_ctrl=float(M2_IN), eps_bd=EPS_BD, nseeds=NSEEDS),
               verdicts=aggregate(rows), runtime_s=time.time() - t0)
    json.dump(out, open(OUT_PATH, "w", encoding="utf-8"), indent=1)
    v = out["verdicts"]
    log(f"FIM {out['runtime_s']:.0f}s PASSA={v['PASSA_FASE1']} D1={v['D1']} D2={v['D2']}")

if __name__ == "__main__":
    main()
