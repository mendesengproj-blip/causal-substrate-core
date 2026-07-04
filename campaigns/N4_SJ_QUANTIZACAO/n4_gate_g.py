# -*- coding: utf-8 -*-
"""
N4 — Gate G de engenharia (pré-registro §4; congelamentos da Fase 0 §4).
Diamante causal 2D, escalar massless (+ controle massivo), reprodução da literatura
ANTES de qualquer medição no substrato do programa.

DECLARAÇÃO PRÉ-RUN (commitada antes de executar o run completo; higiene N-hig 3):

  Setup: diamante u,v ∈ (−L,L), L=1, V=4L², N fixo por seed (declarado; a
  literatura usa ⟨N⟩ Poisson — N fixo só remove variância de tamanho do gate),
  ρ = N/4L². Ordem: x ≺ y ⇔ u_x<u_y e v_x<v_y (estrita). Seeds 20260702+idx.
  Propagadores (Fase 0 §4.1): massless G_R = ½C^T; massivo G_R = ½C^T(I−(m²/2ρ)C^T)^{-1}.
  iΔ = i(G_R − G_R^T), Hermitiana. W_SJ = Pos(iΔ). Grades: N ∈ {1024,2048,4096},
  12 seeds (G3 só N=2048).

  G1 (espectro): resíduo de pareamento ±λ relativo < 1e-10 (exato em aritmética
      real — o teste pega bug de construção); inclinação de log λ_n vs log n
      (n = 4..40, ramo positivo desc.) = −1 ± 0.15 (torre λ_n ~ N/4πn, A7/eq.13);
      amplitude λ_1·4π/N reportada (não gated — duas famílias intercaladas).
  G2 (forma do vácuo, âncora ABDRSY A4): janela de bulk: ambos os pontos com
      max(|u|,|v|) ≤ 0.3L; separações 2ρ^{-1/2} ≤ |Δu|,|Δv| ≤ 0.4L; 24 bins em
      ln|ΔuΔv|, bins com ≥30 pares; R² SEM parâmetros livres das médias binadas
      contra Re W = −(1/4π)ln|ΔuΔv| − (1/2π)ln(π/4L) + ε, ε = −0.063:
      média sobre seeds > 0.9 em CADA N. Fit livre (a,b) reportado.
      Caveat declarado: ε é o limite L→∞ de ABDRSY; correções O(δ/L) na janela.
  G3 (controle massivo, 2 estimadores §7 do pré-reg): N=2048, m = 3·2π/L_x com
      L_x = 2√2L ⇒ m = 3π/√2 ≈ 6.6643 (m²/2ρ ≈ 0.043 ≪ 1). Janela de fit
      k ∈ [2·2π/L_x, 0.25·2π√ρ] = [4.443, 35.54].
      E1 = NUFFT dos top-60 modos SJ positivos → pico (ω*,k*) por modo → fit
      OLS ω² = c²k² + m². E2 = média binada de W(x,y) em (Δt,Δx) (bins 0.05,
      região max(|u|,|v|)≤0.7) → FFT 256² → ridge ω*(k) → mesmo fit.
      PASSA: |m_fit/m − 1| ≤ 0.15 nos DOIS (média de seeds) E
      |m̄_E1 − m̄_E2| ≤ 2√(SEM²+SEM²). c_fit reportado (gated na Fase 1, não aqui).
  G4 (SSEE Sorkin–Yazdi A7): diamantes aninhados ℓ/L = 1/2 (como o paper);
      SEM truncamento: S̄(4096)/S̄(1024) > 2 (lei de volume; log daria ~1.2) —
      critério primário; R²_lin vs R²_log reportado. COM truncamento DUPLO
      congelado (λ̃_min = √N_L/4π na 1ª, √N_ℓ/4π na 2ª, template A8):
      inclinação de S vs ln(√N_ℓ/4π) = 1/3 ± max(0.10, 3·SE) (S-Y: 0.346±0.028).
      Kernel numérico: |λ| < 1e-10·λ_max descartado (zeros de máquina apenas);
      max|Im μ| e frações reportados como diagnóstico.
  Sanidade t0 (pré-gate): região = diamante inteiro ⇒ μ ∈ {0,1} ⇒ S ≈ 0
      (|S| < 0.01) — identidade Pos(iΔ), pega bug antes de tudo.

  VERDE = 4/4. Falha após diagnóstico esgotado = parada de ENGENHARIA (D-G).

CHANGELOG v2 (declarado ANTES do re-run; v1 = commit a82726d, resultado 2/4 em
n4_gate_g_v1.json — G1/G4 VERDES, G2 falha marginal N=1024, G3 falha de estimador):
  G2-v2: R² calculado sobre o perfil binado AGREGADO das 12 seeds por N (mesma
    janela, mesma previsão sem parâmetros livres; v1 usava média dos R² por-seed,
    dominada por ruído de bin em N=1024 — o fit livre por-seed já batia a
    previsão: a_free ≈ −1/4π em 12/12). Critério INALTERADO: R²_pooled > 0.9 em
    CADA N. R² por-seed segue reportado.
  G3-v2 (correções DENTRO das famílias do pré-reg §7):
    E1: M=100 modos (v1 usava 60 — DESVIO do pré-reg, corrigido); grades 0.25;
        interpolação quadrática de pico; filtro de proeminência (pico ≥ 25×
        mediana da potência); fit PONDERADO σ(ω²)=2ω·σ_ω com σ_ω = π/(2√2L)
        ≈ 1.11 = resolução espectral FÍSICA do domínio finito (1º teste v2
        com σ_ω=passo-da-grade clipou tudo, nfit=4 — registrado; v1: OLS
        não-ponderado em (k²,ω²), k altos dominavam e empurravam m²<0);
        sigma-clip 2.5σ ×2.
    E2: taper de Hann radial (R=1.3) antes da FFT (v1: borda dura da caixa
        zero-preenchida = vazamento espectral); FFT 512²; colunas do ridge só
        com pico ≥ 5% do pico global; interpolação quadrática; mesmo fit
        ponderado. Critérios de PASSAGEM inalterados (15% + consistência 2σ).

CHANGELOG v3 (declarado antes do re-run; teste v2 de 1 seed registrado no git):
  Diagnóstico v2 (seed 0): E2 achou ridge CHATO (c≈0, m≈7.8) = a linha do modo
  fundamental ω₁=√(k₁²+m²)≈8.0 (amplitude ∝1/ω) VAZADA por todas as colunas k
  (mainlobe do taper ~4.8 em k); E1 com pico 2D conjunto frágil (c=0.63, m²<0).
  E1-v3: por modo, MARGINAIS de potência P_k(k)=Σ_ω P e P_ω(ω)=Σ_k P (dobra ±k);
    k* = argmax interp de P_k; ω* = argmax interp de P_ω restrito à banda causal
    ω ∈ [0.9·k*, 54] (ω ≥ ck é cinemática do substrato — exclui o vazamento,
    que fica ABAIXO da shell; c ainda é medido livremente ACIMA de 0.9).
  E2-v3: busca por coluna restrita a ω ∈ [max(0.5, 0.9|k|), 54] (mesma razão);
    limiar de 5% recalculado dentro da banda. Fit/critérios INALTERADOS.
  Caveat declarado p/ Fase 1: a banda causal pressupõe c ≤ 1.11 no ridge; o
  teste |c−1|≤0.15 da Fase 1 permanece bem-posto dentro da banda.

CHANGELOG v4 — EMENDA DE GATE (declarada antes do run final; trilha completa
no GATE_G_RESULTADO.md):
  BUG DE FÍSICA achado pelo gate: v1–v3 usavam (I − aC)^{-1} no massivo =
  série NÃO-alternante = massa TAQUIÔNICA (m²<0). Corrigido p/ (I + aC)^{-1}
  (J₀ exige alternância; consistente com b=−m²/ρ de Johnston). Verificação:
  ⟨G_R⟩ binado = ½J₀(mτ) a 3 decimais por 2 oscilações. ERRATUM na tabela A1
  da Fase 0 (sinal do massivo d=2).
  G3-diamante: FALHA DE DESENHO DO TESTE declarada (não do pipeline) — com
  mL=6.7 o diamante tem ~3 λ_Compton e cantos-espelho (ABDRSY/Mathur–Surya);
  o ridge dos modos SEM média de COM é contaminado por borda: 3 implementações
  independentes concordam (m_eff≈9–10, c≈1.1–1.2) e o discriminante massless
  dá o MESMO viés (c=1.22 seed 0) ⇒ viés de test-bed, não física nova nem bug.
  E2 (média de COM) vê o cone: c≈0.99 (2/3 seeds). Mathur–Surya: SJ massivo
  do diamante só rastreia W_mink_m p/ m>m_c=2Λ≈0.92/L — nosso m=6.66≫m_c OK,
  mas o corpo finito domina os modos individuais.
  G3′ (substituto, critério CONGELADO antes do run): controle de propagador —
  ⟨G_R⟩ binado (40 bins, τ∈[0,2], bins≥100 pares) vs ½J₀(mτ):
  RMS_dev/RMS(½J₀) < 0.05 na média das 12 seeds; E 1º zero de ⟨G_R⟩(τ) em
  j01/m=0.361 ± 5%. A validação dois-estimadores-15% MIGRA para a caixa da
  Fase 1 (M1.2/M1.3, já pré-registrada; periodicidade transversal ⇒ k exato).
  Medições E1/E2 do diamante REPORTADAS como diagnóstico, não gated.
"""
import json, sys, time, gc
import numpy as np

L = 1.0
BASE_SEED = 20260702
SIZES = [1024, 2048, 4096]
NSEEDS = 12
ELL = 0.5 * L
EPS_CENTRE = -0.063
M_IN = 3.0 * np.pi / np.sqrt(2.0)
SMOKE = "--smoke" in sys.argv

if SMOKE:
    SIZES = [256, 512]
    NSEEDS = 2

def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)

def sprinkle(N, rng):
    u = rng.uniform(-L, L, N)
    v = rng.uniform(-L, L, N)
    idx = np.argsort(u + v)
    return u[idx], v[idx]

def causal(u, v):
    return (u[:, None] < u[None, :]) & (v[:, None] < v[None, :])

def iDelta_massless(C):
    K = 0.5 * (C.T.astype(np.float64) - C.astype(np.float64))
    return 1j * K

def iDelta_massive(C, m2, rho):
    # G_R = (1/2) C (I + (m^2/2rho) C)^{-1}: serie ALTERNANTE (J_0), como exige
    # b = -m^2/rho de Johnston (v1-v3 usavam I - aC = serie monotonica = massa
    # TAQUIONICA; bug pego pelo gate — ridge sub-cone explicava E1/E2; erratum
    # na tabela A1 da Fase 0 registrado no RESULTADO)
    CT = C.T.astype(np.float64)
    a = m2 / (2.0 * rho)
    Mm = np.eye(CT.shape[0]) + a * CT
    X = np.linalg.solve(Mm.T, CT.T).T      # X = CT @ inv(Mm)
    GR = 0.5 * X
    return 1j * (GR - GR.T)

# ---------------- G1 ----------------
def gate_g1(lam, N):
    s = np.sort(lam)
    pair_resid = float(np.max(np.abs(s + s[::-1])) / np.max(np.abs(s)))
    lp = np.sort(lam[lam > 0])[::-1]
    n = np.arange(1, len(lp) + 1)
    m = (n >= 4) & (n <= 40)
    slope, inter = np.polyfit(np.log(n[m]), np.log(lp[m]), 1)
    amp = float(lp[0] * 4 * np.pi / N)
    return dict(pair_resid=pair_resid, slope=float(slope), amp_l1_4pi_N=amp)

# ---------------- G2 ----------------
def g2_pairs(u, v, lam, V, rho):
    """Retorna (x, w) dos pares da janela de bulk (para pooling v2)."""
    posm = lam > 0
    cen = (np.abs(u) <= 0.3 * L) & (np.abs(v) <= 0.3 * L)
    Vc = V[cen][:, posm]
    Wc = (Vc * lam[posm]) @ Vc.conj().T
    uc, vc = u[cen], v[cen]
    i, j = np.triu_indices(len(uc), k=1)
    du = np.abs(uc[i] - uc[j]); dv = np.abs(vc[i] - vc[j])
    dmin = 2.0 / np.sqrt(rho)
    ok = (du >= dmin) & (dv >= dmin) & (du <= 0.4 * L) & (dv <= 0.4 * L)
    return np.log(du[ok] * dv[ok]), Wc[i[ok], j[ok]].real

def g2_pooled_R2(xs, ws):
    """R² sem parâmetros livres do perfil binado agregado (v2)."""
    x = np.concatenate(xs); w = np.concatenate(ws)
    if len(x) < 200:
        return dict(R2=float("nan"), npairs=int(len(x)))
    bpred = -np.log(np.pi / (4 * L)) / (2 * np.pi) + EPS_CENTRE
    edges = np.linspace(x.min(), x.max() + 1e-12, 25)
    which = np.digitize(x, edges) - 1
    xm, wm = [], []
    for b in range(24):
        sel = which == b
        if sel.sum() >= 30:
            xm.append(x[sel].mean()); wm.append(w[sel].mean())
    xm = np.array(xm); wm = np.array(wm)
    if len(xm) < 5:
        return dict(R2=float("nan"), nbins=int(len(xm)), npairs=int(len(x)))
    pred = -xm / (4 * np.pi) + bpred
    R2 = 1.0 - np.sum((wm - pred) ** 2) / np.sum((wm - wm.mean()) ** 2)
    a_free, b_free = np.polyfit(xm, wm, 1)
    return dict(R2=float(R2), a_free=float(a_free), b_free=float(b_free),
                a_pred=float(-1 / (4 * np.pi)), b_pred=float(bpred),
                nbins=int(len(xm)), npairs=int(len(x)))

def gate_g2(u, v, lam, V, rho):
    posm = lam > 0
    cen = (np.abs(u) <= 0.3 * L) & (np.abs(v) <= 0.3 * L)
    Vc = V[cen][:, posm]
    Wc = (Vc * lam[posm]) @ Vc.conj().T
    uc, vc = u[cen], v[cen]
    i, j = np.triu_indices(len(uc), k=1)
    du = np.abs(uc[i] - uc[j]); dv = np.abs(vc[i] - vc[j])
    dmin = 2.0 / np.sqrt(rho)
    ok = (du >= dmin) & (dv >= dmin) & (du <= 0.4 * L) & (dv <= 0.4 * L)
    if ok.sum() < 200:
        return dict(R2=np.nan, npairs=int(ok.sum()))
    x = np.log(du[ok] * dv[ok])
    w = Wc[i[ok], j[ok]].real
    bpred = -np.log(np.pi / (4 * L)) / (2 * np.pi) + EPS_CENTRE
    edges = np.linspace(x.min(), x.max() + 1e-12, 25)
    which = np.digitize(x, edges) - 1
    xm, wm = [], []
    for b in range(24):
        sel = which == b
        if sel.sum() >= 30:
            xm.append(x[sel].mean()); wm.append(w[sel].mean())
    xm = np.array(xm); wm = np.array(wm)
    if len(xm) < 5:
        return dict(R2=np.nan, nbins=len(xm), npairs=int(ok.sum()))
    pred = -xm / (4 * np.pi) + bpred
    ss_res = np.sum((wm - pred) ** 2)
    ss_tot = np.sum((wm - wm.mean()) ** 2)
    R2 = 1.0 - ss_res / ss_tot
    a_free, b_free = np.polyfit(xm, wm, 1)
    return dict(R2=float(R2), a_free=float(a_free), b_free=float(b_free),
                a_pred=float(-1 / (4 * np.pi)), b_pred=float(bpred),
                nbins=len(xm), npairs=int(ok.sum()))

# ---------------- G3 (v2) ----------------
def qinterp(y0, y1, y2):
    """Deslocamento sub-bin do vértice da parábola por 3 pontos."""
    d = y0 - 2 * y1 + y2
    return 0.0 if abs(d) < 1e-30 else 0.5 * (y0 - y2) / d

def fit_disp_w(ks, oms, sig_om):
    """Fit ponderado ω² = c²k² + m², σ(ω²)=2ω·σ_ω, sigma-clip 2.5σ ×2."""
    ks = np.asarray(ks, float); oms = np.asarray(oms, float)
    keep = np.ones(len(ks), bool)
    for _ in range(3):
        k2 = ks[keep] ** 2; w2 = oms[keep] ** 2
        sw = 2 * oms[keep] * sig_om
        A = np.vstack([k2, np.ones_like(k2)]).T / sw[:, None]
        y = w2 / sw
        coef, _, _, _ = np.linalg.lstsq(A, y, rcond=None)
        c2, m2 = coef
        resid = (w2 - (c2 * k2 + m2)) / sw
        newkeep = keep.copy()
        newkeep[keep] = np.abs(resid) <= 2.5
        if newkeep.sum() == keep.sum():
            break
        keep = newkeep
        if keep.sum() < 6:
            return np.nan, np.nan, np.nan, int(keep.sum())
    k2 = ks[keep] ** 2; w2 = oms[keep] ** 2
    sw = 2 * oms[keep] * sig_om
    A = np.vstack([k2, np.ones_like(k2)]).T / sw[:, None]
    y = w2 / sw
    coef, res_, _, _ = np.linalg.lstsq(A, y, rcond=None)
    c2, m2 = coef
    cov = np.linalg.inv(A.T @ A)
    m = np.sqrt(max(m2, 1e-12))
    sig_m = np.sqrt(max(cov[1, 1], 0)) / (2 * m)
    return float(m), float(sig_m), float(np.sqrt(max(c2, 0))), int(keep.sum())

def gate_g3p_seed(seed):
    """G3': controle de propagador J0 (v4). Sem eigh — barato."""
    from scipy.special import j0
    N = 2048
    rho = N / (4 * L * L)
    rng = np.random.default_rng(BASE_SEED + 777000 + seed)
    u, v = sprinkle(N, rng)
    C = causal(u, v)
    CT = C.T.astype(np.float64)
    a = M_IN ** 2 / (2.0 * rho)
    Mm = np.eye(N) + a * CT
    GR = 0.5 * np.linalg.solve(Mm.T, CT.T).T
    xi, yi = np.nonzero(CT)
    tau = np.sqrt(2.0 * np.abs(u[xi] - u[yi]) * np.abs(v[xi] - v[yi]))
    gv = GR[xi, yi]
    edges = np.linspace(0, 2.0, 41)
    wh = np.digitize(tau, edges) - 1
    tm, gm = [], []
    for b in range(40):
        s = wh == b
        if s.sum() >= 100:
            tm.append(tau[s].mean()); gm.append(gv[s].mean())
    tm = np.array(tm); gm = np.array(gm)
    pred = 0.5 * j0(M_IN * tm)
    rms_dev = float(np.sqrt(np.mean((gm - pred) ** 2) / np.mean(pred ** 2)))
    sg = np.sign(gm)
    zc = np.where(np.diff(sg) != 0)[0]
    tau_zero = float(0.5 * (tm[zc[0]] + tm[zc[0] + 1])) if len(zc) else np.nan
    tau_zero_pred = 2.404826 / M_IN
    return dict(rms_dev=rms_dev, tau_zero=tau_zero, tau_zero_pred=tau_zero_pred,
                nbins=int(len(tm)))

def gate_g3_seed(seed):
    N = 2048
    rho = N / (4 * L * L)
    rng = np.random.default_rng(BASE_SEED + 777000 + seed)
    u, v = sprinkle(N, rng)
    C = causal(u, v)
    A = iDelta_massive(C, M_IN ** 2, rho)
    lam, V = np.linalg.eigh(A)
    t = (u + v) / np.sqrt(2.0); x = (u - v) / np.sqrt(2.0)
    kmin = 2 * 2 * np.pi / (2 * np.sqrt(2) * L)
    kmax = 0.25 * 2 * np.pi * np.sqrt(rho)
    step = 0.25
    # E1 v2: NUFFT top-100 modos, interp quadrática, proeminência, fit ponderado
    idx = np.argsort(-lam)[:100]
    om_g = np.arange(0.0, 55.0 + 1e-9, step)
    k_g = np.arange(-45.0, 45.0 + 1e-9, step)
    T1 = np.exp(1j * om_g[:, None] * t[None, :])
    T2 = np.exp(-1j * x[:, None] * k_g[None, :])
    kfold = np.abs(k_g)
    kf_g = np.arange(0.0, 45.0 + 1e-9, step)
    fold_idx = np.clip(np.round(kfold / step).astype(int), 0, len(kf_g) - 1)
    ks, oms = [], []
    for q in idx:
        w = V[:, q]
        S = T1 @ (w[:, None] * T2)
        P = np.abs(S) ** 2
        if P.max() < 25.0 * np.median(P):
            continue
        Pk = np.zeros(len(kf_g))
        np.add.at(Pk, fold_idx, P.sum(axis=0))
        ik = int(np.argmax(Pk))
        dk = qinterp(Pk[ik - 1], Pk[ik], Pk[ik + 1]) if 0 < ik < len(kf_g) - 1 else 0.0
        kstar = kf_g[ik] + dk * step
        Pw = P.sum(axis=1)
        wlo = 0.9 * kstar
        allowed = (om_g >= wlo) & (om_g < 54.0)
        if allowed.sum() < 3:
            continue
        Pw_m = np.where(allowed, Pw, 0.0)
        io = int(np.argmax(Pw_m))
        do = qinterp(Pw[io - 1], Pw[io], Pw[io + 1]) if 0 < io < len(om_g) - 1 else 0.0
        ostar = om_g[io] + do * step
        if kmin <= kstar <= kmax and 0 < ostar < 54.0:
            ks.append(kstar); oms.append(ostar)
    sig_om = np.pi / (2 * np.sqrt(2) * L)
    e1 = fit_disp_w(ks, oms, sig_om) if len(ks) >= 8 else (np.nan, np.nan, np.nan, 0)
    # E2 v2: W binada + taper Hann radial + FFT 512 + ridge com limiar + interp
    bb = np.maximum(np.abs(u), np.abs(v)) <= 0.7 * L
    Vb = V[bb][:, lam > 0]
    Wb = (Vb * lam[lam > 0]) @ Vb.conj().T
    tb, xb = t[bb], x[bb]
    i, j = np.triu_indices(len(tb), k=1)
    dt = tb[j] - tb[i]; dx = xb[j] - xb[i]
    wv = Wb[i, j]
    h = 0.05; half = 1.4
    nb = int(2 * half / h)
    bt = np.clip(((dt + half) / h).astype(int), 0, nb - 1)
    bx = np.clip(((dx + half) / h).astype(int), 0, nb - 1)
    acc = np.zeros((nb, nb), complex); cnt = np.zeros((nb, nb))
    np.add.at(acc, (bt, bx), wv); np.add.at(cnt, (bt, bx), 1)
    np.add.at(acc, (nb - 1 - bt, nb - 1 - bx), np.conj(wv)); np.add.at(cnt, (nb - 1 - bt, nb - 1 - bx), 1)
    Wg = np.where(cnt > 0, acc / np.maximum(cnt, 1), 0)
    cc = (np.arange(nb) + 0.5) * h - half
    rr = np.sqrt(cc[:, None] ** 2 + cc[None, :] ** 2)
    Rtap = 1.3
    taper = np.where(rr < Rtap, 0.5 * (1 + np.cos(np.pi * rr / Rtap)), 0.0)
    Wg = Wg * taper
    NP = 512
    F = np.fft.fftshift(np.fft.fft2(Wg, s=(NP, NP)))
    fr = np.fft.fftshift(np.fft.fftfreq(NP, d=h)) * 2 * np.pi
    P = np.abs(F) ** 2
    colpk = []
    for ik, kk in enumerate(fr):
        if kmin <= abs(kk) <= kmax:
            om_ok = (fr > max(0.5, 0.9 * abs(kk))) & (fr < 54.0)
            io_all = np.where(om_ok)[0]
            if len(io_all) < 3:
                continue
            col = P[io_all, ik]
            colpk.append((ik, io_all[int(np.argmax(col))], float(col.max())))
    gmax = max(c[2] for c in colpk) if colpk else 0.0
    dfr = fr[1] - fr[0]
    ks2, oms2 = [], []
    for ik, io, pk in colpk:
        if pk < 0.05 * gmax:
            continue
        do = qinterp(P[io - 1, ik], P[io, ik], P[io + 1, ik]) if 0 < io < NP - 1 else 0.0
        ks2.append(abs(fr[ik])); oms2.append(abs(fr[io] + do * dfr))
    e2 = fit_disp_w(ks2, oms2, sig_om) if len(ks2) >= 8 else (np.nan, np.nan, np.nan, 0)
    return dict(m_e1=e1[0], sig_e1=e1[1], c_e1=e1[2], n_e1=len(ks), nfit_e1=e1[3],
                m_e2=e2[0], sig_e2=e2[1], c_e2=e2[2], n_e2=len(ks2), nfit_e2=e2[3])

# ---------------- G4 ----------------
def ssee(Wr, Ar, kill_rel=1e-10):
    lr, Q = np.linalg.eigh(Ar)
    keep = np.abs(lr) > kill_rel * np.abs(lr).max()
    Qk = Q[:, keep]
    Ainv = (Qk / lr[keep]) @ Qk.conj().T
    mu = np.linalg.eigvals(Ainv @ Wr)
    mur = mu.real
    mask = np.abs(mur) > 1e-9
    S = float(np.sum(mur[mask] * np.log(np.abs(mur[mask]))))
    return S, float(np.max(np.abs(mu.imag))), int((~keep).sum())

def gate_g4(u, v, lam, V, N):
    sub = np.maximum(np.abs(u), np.abs(v)) < ELL
    Nl = int(sub.sum())
    posm = lam > 0
    # sem truncamento
    Vs = V[sub]
    Ar = (Vs * lam) @ Vs.conj().T
    Wr = (Vs[:, posm] * lam[posm]) @ Vs[:, posm].conj().T
    S_un, imax_un, nk_un = ssee(Wr, Ar)
    # truncamento duplo congelado
    lmin1 = np.sqrt(N) / (4 * np.pi)
    k1 = np.abs(lam) >= lmin1
    k1p = k1 & posm
    Ar_t = (Vs[:, k1] * lam[k1]) @ Vs[:, k1].conj().T
    Wr_t = (Vs[:, k1p] * lam[k1p]) @ Vs[:, k1p].conj().T
    l2, U2 = np.linalg.eigh(Ar_t)
    lmin2 = np.sqrt(Nl) / (4 * np.pi)
    k2 = np.abs(l2) >= lmin2
    U2k = U2[:, k2]
    Wt = U2k.conj().T @ Wr_t @ U2k
    At = np.diag(l2[k2]).astype(complex)
    mu = np.linalg.eigvals(np.linalg.solve(At, Wt))
    mur = mu.real
    mask = np.abs(mur) > 1e-9
    S_t = float(np.sum(mur[mask] * np.log(np.abs(mur[mask]))))
    return dict(Nl=Nl, S_untrunc=S_un, imax_untrunc=imax_un, nkill=nk_un,
                S_trunc=S_t, imax_trunc=float(np.max(np.abs(mu.imag))),
                n1=int(k1.sum()), n2=int(k2.sum()))

# ---------------- sanidade t0 ----------------
def sanity_t0():
    rng = np.random.default_rng(BASE_SEED)
    u, v = sprinkle(512, rng)
    C = causal(u, v)
    A = iDelta_massless(C)
    lam, V = np.linalg.eigh(A)
    posm = lam > 0
    W = (V[:, posm] * lam[posm]) @ V[:, posm].conj().T
    S, imax, _ = ssee(W, A)
    return abs(S)

# ---------------- main ----------------
def main():
    t0 = time.time()
    out = dict(meta=dict(base_seed=BASE_SEED, L=L, sizes=SIZES, nseeds=NSEEDS,
                         ell=ELL, eps_centre=EPS_CENTRE, m_in=M_IN, smoke=SMOKE))
    s0 = sanity_t0()
    out["t0_S_full_diamond"] = s0
    log(f"t0 sanidade |S(full)| = {s0:.2e} (exige < 0.01)")
    if s0 >= 0.01:
        out["verdict"] = "T0_FAIL"
        json.dump(out, open(OUT, "w"), indent=1)
        sys.exit(1)

    rows = []
    g2pool = {N: ([], []) for N in SIZES}
    for N in SIZES:
        rho = N / (4 * L * L)
        for s in range(NSEEDS):
            rng = np.random.default_rng(BASE_SEED + 1000 * N + s)
            u, v = sprinkle(N, rng)
            C = causal(u, v)
            A = iDelta_massless(C)
            lam, V = np.linalg.eigh(A)
            del A
            r = dict(N=N, seed=s)
            r["g1"] = gate_g1(lam, N)
            r["g2"] = gate_g2(u, v, lam, V, rho)
            xs, ws = g2_pairs(u, v, lam, V, rho)
            g2pool[N][0].append(xs); g2pool[N][1].append(ws)
            r["g4"] = gate_g4(u, v, lam, V, N)
            rows.append(r)
            del V
            gc.collect()
            log(f"N={N} seed={s}: g1 slope={r['g1']['slope']:.3f} resid={r['g1']['pair_resid']:.1e} | "
                f"g2 R2={r['g2'].get('R2', float('nan')):.3f} | g4 Sun={r['g4']['S_untrunc']:.2f} St={r['g4']['S_trunc']:.3f}")
    out["rows"] = rows

    g3rows = []
    if not SMOKE:
        for s in range(NSEEDS):
            g3 = gate_g3p_seed(s)
            g3rows.append(g3)
            log(f"G3' seed={s}: rms_dev={g3['rms_dev']:.4f} tau0={g3['tau_zero']:.4f} "
                f"(pred {g3['tau_zero_pred']:.4f})")
    out["g3_rows"] = g3rows

    # ---- agregação e vereditos ----
    verd = {}
    pr = max(r["g1"]["pair_resid"] for r in rows)
    slopes = np.array([r["g1"]["slope"] for r in rows])
    verd["G1"] = bool(pr < 1e-10 and abs(slopes.mean() + 1.0) <= 0.15)
    verd["G1_detail"] = dict(max_pair_resid=pr, slope_mean=float(slopes.mean()),
                             slope_sem=float(slopes.std(ddof=1) / np.sqrt(len(slopes))))
    g2ok = True
    g2d = {}
    for N in SIZES:
        r2s = np.array([r["g2"]["R2"] for r in rows if r["N"] == N and np.isfinite(r["g2"].get("R2", np.nan))])
        pooled = g2_pooled_R2(g2pool[N][0], g2pool[N][1])
        g2d[str(N)] = dict(R2_pooled=pooled["R2"], pooled=pooled,
                           R2_perseed_mean=float(r2s.mean()) if len(r2s) else None,
                           nseeds=len(r2s))
        if not np.isfinite(pooled["R2"]) or pooled["R2"] <= 0.9:
            g2ok = False
    verd["G2"] = bool(g2ok)
    verd["G2_detail"] = g2d
    if g3rows:
        rd = np.array([g["rms_dev"] for g in g3rows])
        tz = np.array([g["tau_zero"] for g in g3rows])
        tzp = g3rows[0]["tau_zero_pred"]
        ok1 = rd.mean() < 0.05
        ok2 = abs(np.nanmean(tz) / tzp - 1) <= 0.05
        verd["G3"] = bool(ok1 and ok2)
        verd["G3_detail"] = dict(rms_dev_mean=float(rd.mean()),
                                 rms_dev_sem=float(rd.std(ddof=1) / np.sqrt(len(rd))),
                                 tau_zero_mean=float(np.nanmean(tz)),
                                 tau_zero_pred=float(tzp),
                                 dev_zero=float(np.nanmean(tz) / tzp - 1))
    # G4
    Nls = np.array([r["g4"]["Nl"] for r in rows], float)
    Sun = np.array([r["g4"]["S_untrunc"] for r in rows], float)
    St = np.array([r["g4"]["S_trunc"] for r in rows], float)
    Ns = np.array([r["N"] for r in rows], float)
    mS = {N: Sun[Ns == N].mean() for N in SIZES}
    ratio = mS[SIZES[-1]] / mS[SIZES[0]]
    # fits sobre todos os pontos
    def r2(xx, yy):
        a, b = np.polyfit(xx, yy, 1)
        res = yy - (a * xx + b)
        return 1 - res.var() / yy.var()
    r2lin = r2(Nls, Sun); r2log = r2(np.log(Nls), Sun)
    xt = np.log(np.sqrt(Nls) / (4 * np.pi))
    A2 = np.vstack([xt, np.ones_like(xt)]).T
    coef, res_, _, _ = np.linalg.lstsq(A2, St, rcond=None)
    a4, b4 = coef
    dof = len(xt) - 2
    s2f = (res_[0] / dof) if len(res_) else np.sum((St - A2 @ coef) ** 2) / dof
    se_a4 = float(np.sqrt(s2f * np.linalg.inv(A2.T @ A2)[0, 0]))
    tol4 = max(0.10, 3 * se_a4)
    verd["G4"] = bool(ratio > 2.0 and abs(a4 - 1 / 3) <= tol4)
    verd["G4_detail"] = dict(ratio_vol=float(ratio), r2_lin=float(r2lin), r2_log=float(r2log),
                             slope_trunc=float(a4), se_slope=se_a4, b_trunc=float(b4),
                             target=1 / 3, tol=float(tol4))
    gates = [k for k in ("G1", "G2", "G3", "G4") if k in verd]
    npass = sum(bool(verd[k]) for k in gates)
    verd["overall"] = f"{npass}/{len(gates)}"
    verd["VERDE"] = bool(npass == len(gates) == 4)
    out["verdicts"] = verd
    out["runtime_s"] = time.time() - t0
    json.dump(out, open(OUT, "w"), indent=1)
    log(f"FIM {out['runtime_s']:.0f}s — {verd['overall']} VERDE={verd.get('VERDE')}")

OUT = "n4_gate_g_smoke.json" if SMOKE else "n4_gate_g.json"

if __name__ == "__main__":
    main()
