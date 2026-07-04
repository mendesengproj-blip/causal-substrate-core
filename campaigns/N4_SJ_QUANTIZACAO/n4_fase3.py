# -*- coding: utf-8 -*-
"""
N4 — FASE 3: SSEE pelo canto de Rindler (liga N4 a N2). Pré-registro §5
(Fase 3) + Fase 0 §4.2 (truncamento congelado) + §4.4 (geometria N2 verbatim)
+ §5.1 (M3.1 rebaixada a gate de reprodução) + §5.2 (eixos genuinamente
nossos). Gate do funil: Gate G VERDE 4/4 + Fase 1 sem D1/D2 — satisfeito
(GATE_G_RESULTADO.md; FASE1_RESULTADO.md). Independente da Fase 2.

DECLARAÇÃO PRÉ-RUN (commitada antes de executar; nenhum critério muda depois):

GEOMETRIA (pré-reg §5 Fase 3 + Fase 0 §4.4 "geometria de N2 verbatim"):
  Caixa em M⁴: (t, x) ∈ [−TX, TX]², TX = 2.5 (o valor da N2 fase 2 — não
  fixado no pré-reg de N4; congelado AGORA, antes de rodar). Transversal
  (y, z) ∈ [0, L)² PERIÓDICA (min-imagem na ordem), L ∈ {1.5, 2, 3} (pré-reg).
  ρ = 8 (pré-reg), N Poisson-realizado (convenção N2). Horizonte = plano nulo
  u = t − x = 0; canto = {t=0, x=0}, área transversal L².
  Ordem: Δt > |Δx⃗| com min-imagem em y,z (n2_core verbatim).
  CAVEAT DE ENROLAMENTO (declarado): com Δt até 5 > L/2 a transversal
  enrola (a laje da Fase 1 evitava isso; aqui a geometria É a de N2, onde a
  MI clássica mediu L^3.36 — a comparação limpa exige o MESMO grafo).
  O kernel de Johnston aL é exato por-intervalo apenas onde o intervalo
  não enrola; a fração de LINKS enrolados é REPORTADA por L como
  diagnóstico da contaminação (se ela crescer com L e o expoente for
  limítrofe, o caveat entra no resultado).

SUB-REGIÃO (pré-reg: "laje interna junto ao canto, janela como em N2 fase 2"):
  >> EMENDA PRÉ-RUN (achada pelo SMOKE, declarada e commitada ANTES do run
  real — precedente: emendas no-wrap/k_res da Fase 1). O smoke (commit v1,
  n4_fase3_rows_smoke.jsonl, preservado como evidência) mediu um PISO DE
  RESOLUÇÃO do estimador SSEE: com N_O ≤ 17 o pipeline inverte
  (S_trunc > S_untrunc: 11.5 vs 2.6; instável entre seeds: S_a2 9.7 vs 21.5)
  e com N_O ≤ 5 degenera (S_un = −8.9e15, |Im μ| = 0.07); com N_O ≥ 60 é
  saudável e estável (S_un 37.2/41.2; S_a1 4.52/4.70 ≪ S_un — o padrão do
  G4). A laje N2-fase-2 (espessura u = 0.5) é mais fina que a escala de
  discretude ρ^{−1/4} ≈ 0.59 — sub-resolução em L ∈ {1.5, 2}. Instrumento,
  não física; a saída certa é a geometria (como na Fase 1). Re-congelado:
  W_MAIN (PRINCIPAL, M3.1/M3.2): O = {0 < u < 1.0, |t| < 2.0} — a MESMA
    família da N2 fase 2 escalada ×2 (proporção u:t = 1:2 mantida; segue
    "laje interna junto ao canto"); N_O ≈ 31L² = {70, 124, 280} — todos
    acima do piso. Critérios físicos de M3.1/M3.2 INALTERADOS.
  W_HALF (diagnóstico): O = {0 < u < 0.5, |t| < 1} — a janela N2-fase-2
    verbatim, computada só onde N_O ≥ 40 (⇒ só L=3, N_O ≈ 72).
  PISO DECLARADO: janela com N_O < 40 não é computada (sub-resolução).
  Eixo-janela (diagnóstico volume-vs-área, em L=3): razão
  S(W_MAIN)/S(W_HALF) — volume ⇒ ~4 (razão dos volumes); área ⇒ ~1
  (localiza no canto).
  (O eixo-L NÃO separa volume de área — N_O ∝ L² E área ∝ L²; separa
  área-compatível (expoente 2) de SUPER-área (>2, a 4ª face). O eixo-janela
  é o separador volume-vs-área. Ambos declarados aqui, antes de rodar.)

CONSTRUÇÃO (Fase 0 §4.1 + Fase 1):
  d=4 massless: G_R = a·Lk^T, a = (1/2π)√(ρ/6), Lk = matriz de links;
  iΔ = i(G_R − G_R^T); W_SJ = Pos(iΔ). Espectro denso (eigh) por run.
  SSEE (A8, eq. 12): μ de (iΔ|_O)⁻¹ W|_O; S = Σ μ ln|μ| (máscara |μ|>1e-9;
  pipeline validado no Gate G4 contra Sorkin–Yazdi).

TRUNCAMENTO (Fase 0 §4.2, congelado lá — NÚMERO, α=1, DUPLO):
  1º: top n1 = round(α·N^{3/4}) modos de iΔ por |λ| → iΔ^t, W^t; restringe a O;
  2º: diagonaliza iΔ^t|_O, top n2 = round(α·N_O^{3/4}) por |l|; W projetado
  na base duplamente truncada; μ generalizado na base truncada.
  α = 1 é O critério; α = 2 REPORTADO (robustez declarada, nunca ajustada).
  Guarda numérica (instrumento): modos com |l| < 1e-12·max descartados do
  solve (evita inversão de zeros; não é critério).

GRADES: L ∈ {1.5, 2, 3} × 24 seeds (BASE 20260703; 24 e não 12 porque
  N_O(W2) ∈ {18, 32, 72} é pequeno e o custo por run é trivial — decisão de
  potência declarada AGORA, não após ver variâncias).

MEDIÇÕES E CRITÉRIOS (congelados; expoentes = OLS ponderado log-log sobre
médias por L com SEM sobre seeds, como N2):
  M3.1 (GATE de reprodução, Fase 0 §5.1 — volume sem truncamento):
    κ_un = expoente de S_untrunc(W_MAIN) vs L ∈ [1.5, 2.5]  (extensivo ⇒ 2)
    E  S_untrunc/S_trunc(α=1) em L=3  > 2  (estilo G4).
    FALHA ⇒ parada de ENGENHARIA (bug de pipeline, não física) — pré-reg §8.
  M3.2 (A MEDIÇÃO; nenhuma saída é morte — pré-reg §8.6):
    κ_tr = expoente de S_trunc(α=1, W_MAIN) vs L; tol = max(0.30, 2·SE_κ):
      |κ_tr − 2| ≤ tol  ⇒ ÁREA (resgate quântico — upgrade do Teorema da
                          Fronteira, delta no paper-núcleo)
      κ_tr − 2 > tol    ⇒ SUPER-ÁREA (4ª face, quântica — N2-F2 sobe a
                          estrutural)
      2 − κ_tr > tol    ⇒ SUB-ÁREA (surpresa; reportar como tal)
    Robustez: mesma classificação com α=2; discordância entre α=1 e α=2 ⇒
    flag ROBUSTEZ_FRACA anexada ao veredito (α=1 decide; flag reportada).
    Tolerância 0.30 congelada por separação: o clássico de N2-F2 deu 3.36
    (Δ = 1.36 ≫ 0.30); 2·SE protege contra sub-potência.
  DIAGNÓSTICOS (reportados, sem critério): eixo-janela W_MAIN/W_HALF em L=3
    (razão vs 4 de volume); fração de links enrolados por L; pair_resid
    (higiene ±λ da Fase 1); n1/n2/N_O; imax (|Im μ|); sanidade S0 (O = caixa
    inteira, seed 0 por L: S ≈ 0 puro, como G4).

SAÍDAS: n4_fase3_rows.jsonl (checkpoint por run, retomável) + n4_fase3.json.
Flags: --smoke (L=1.5, 2 seeds, valida instrumento na máquina).
"""
import json, os, sys, time, gc
import numpy as np

BASE_SEED = 20260703
RHO, TX = 8.0, 2.5
LS = [1.5, 2.0, 3.0]
NSEEDS = 24
WINDOWS = {"WH": (0.5, 1.0), "WM": (1.0, 2.0)}   # WM = principal (emenda)
WMAIN = "WM"
NO_FLOOR = 40                                     # piso de resolução (smoke)
ALPHAS = (1.0, 2.0)
SMOKE = "--smoke" in sys.argv

if SMOKE:
    LS = [1.5]; NSEEDS = 2

ROWS_PATH = "n4_fase3_rows_smoke.jsonl" if SMOKE else "n4_fase3_rows.jsonl"
OUT_PATH = "n4_fase3_smoke.json" if SMOKE else "n4_fase3.json"


def log(m): print(f"[{time.strftime('%H:%M:%S')}] {m}", flush=True)


def emit(row):
    with open(ROWS_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(row) + "\n")


# ---------------- substrato (n2_core verbatim, ρ=8) ----------------
def sprinkle(L, rng):
    vol = (2 * TX) ** 2 * L * L
    n = int(rng.poisson(RHO * vol))
    pts = np.empty((n, 4))
    pts[:, 0] = rng.uniform(-TX, TX, n)
    pts[:, 1] = rng.uniform(-TX, TX, n)
    pts[:, 2] = rng.uniform(0.0, L, n)
    pts[:, 3] = rng.uniform(0.0, L, n)
    return pts[np.argsort(pts[:, 0])]


def causal(pts, L):
    t = pts[:, 0]
    dt = t[None, :] - t[:, None]
    dx2 = (pts[None, :, 1] - pts[:, None, 1]) ** 2
    for k in (2, 3):
        dp = np.abs(pts[None, :, k] - pts[:, None, k])
        dp = np.minimum(dp, L - dp)
        dx2 = dx2 + dp * dp
    return (dt > 0) & (dt * dt > dx2)


def links_of(C):
    Cf = C.astype(np.float32)
    two = (Cf @ Cf) > 0.5
    return C & ~two


def idelta_d4(Lk):
    a = (1.0 / (2 * np.pi)) * np.sqrt(RHO / 6.0)
    GR = a * Lk.T.astype(np.float64)
    return 1j * (GR - GR.T)


def wrap_frac(pts, Lk, L):
    ii, jj = np.nonzero(Lk)
    if len(ii) == 0:
        return 0.0
    w = np.zeros(len(ii), bool)
    for k in (2, 3):
        w |= np.abs(pts[ii, k] - pts[jj, k]) > L / 2
    return float(np.mean(w))


# ---------------- SSEE (pipeline do Gate G4; A8 eq. 12) ----------------
def entropy_from_mu(mu):
    mur = mu.real
    mask = np.abs(mur) > 1e-9
    S = float(np.sum(mur[mask] * np.log(np.abs(mur[mask]))))
    return S, float(np.max(np.abs(mu.imag))) if len(mu) else 0.0


def ssee_untrunc(lam, V, sub, kill_rel=1e-10):
    Vs = V[sub]
    posm = lam > 0
    Ar = (Vs * lam) @ Vs.conj().T
    Wr = (Vs[:, posm] * lam[posm]) @ Vs[:, posm].conj().T
    lr, Q = np.linalg.eigh(Ar)
    keep = np.abs(lr) > kill_rel * np.abs(lr).max()
    Ainv = (Q[:, keep] / lr[keep]) @ Q[:, keep].conj().T
    mu = np.linalg.eigvals(Ainv @ Wr)
    S, imax = entropy_from_mu(mu)
    return S, imax, int((~keep).sum())


def ssee_trunc_number(lam, V, sub, alpha):
    """Truncamento duplo de NÚMERO congelado (Fase 0 §4.2)."""
    N = len(lam)
    Nl = int(sub.sum())
    n1 = max(2, int(round(alpha * N ** 0.75)))
    keep1 = np.argsort(-np.abs(lam))[:min(n1, N)]
    lk = lam[keep1]
    Vs = V[sub][:, keep1]
    Ar_t = (Vs * lk) @ Vs.conj().T
    pos = lk > 0
    Wr_t = (Vs[:, pos] * lk[pos]) @ Vs[:, pos].conj().T
    l2, U2 = np.linalg.eigh(Ar_t)
    n2 = max(2, int(round(alpha * Nl ** 0.75)))
    o2 = np.argsort(-np.abs(l2))[:min(n2, len(l2))]
    # guarda numérica declarada (instrumento): não inverter zeros
    o2 = o2[np.abs(l2[o2]) > 1e-12 * np.abs(l2).max()]
    U2k = U2[:, o2]
    Wt = U2k.conj().T @ Wr_t @ U2k
    mu = np.linalg.eigvals(Wt / l2[o2][:, None])
    S, imax = entropy_from_mu(mu)
    return S, imax, int(len(keep1)), int(len(o2))


def pair_resid(lam):
    s = np.sort(lam)
    return float(np.max(np.abs(s + s[::-1])) / np.max(np.abs(s)))


# ---------------- run ----------------
def run_case(L, seed, do_sanity):
    rng = np.random.default_rng(BASE_SEED + 977 * int(L * 10) + seed)
    pts = sprinkle(L, rng)
    N = len(pts)
    C = causal(pts, L)
    Lk = links_of(C)
    wf = wrap_frac(pts, Lk, L)
    del C
    A = idelta_d4(Lk)
    del Lk
    gc.collect()
    lam, V = np.linalg.eigh(A)
    pr = pair_resid(lam)
    del A
    gc.collect()

    u = pts[:, 0] - pts[:, 1]
    t = pts[:, 0]
    row = dict(L=float(L), seed=seed, N=N, wrap_frac=wf, pair_resid=pr, win={})
    for wname, (w, tw) in WINDOWS.items():
        sub = (u > 0) & (u < w) & (np.abs(t) < tw)
        Nl = int(sub.sum())
        if Nl < NO_FLOOR:                     # piso de resolução (emenda)
            row["win"][wname] = dict(N_O=Nl, skipped=True)
            continue
        S_un, im_un, nk = ssee_untrunc(lam, V, sub)
        d = dict(N_O=Nl, S_un=S_un, imax_un=im_un, nkill=nk)
        for a in ALPHAS:
            if a == 1.0 or wname == WMAIN:    # α=2 só na janela principal
                S_t, im_t, n1, n2 = ssee_trunc_number(lam, V, sub, a)
                d[f"S_a{int(a)}"] = S_t
                d[f"imax_a{int(a)}"] = im_t
                d[f"n1_a{int(a)}"], d[f"n2_a{int(a)}"] = n1, n2
        row["win"][wname] = d
    if do_sanity:
        allsub = np.ones(N, bool)
        S0, _, _ = ssee_untrunc(lam, V, allsub)
        row["S0_fullbox"] = S0
    del lam, V
    gc.collect()
    return row


# ---------------- agregação ----------------
def sem(a):
    a = np.asarray(a, float)
    return float(a.std(ddof=1) / np.sqrt(len(a))) if len(a) > 1 else float("nan")


def loglog_slope(xs, ys, errs):
    """OLS ponderado de log y vs log x (n2_core verbatim)."""
    xs = np.asarray(xs, float); ys = np.asarray(ys, float)
    keep = ys > 0
    if keep.sum() < 2:
        return float("nan"), float("nan")
    x, y = np.log(xs[keep]), np.log(ys[keep])
    w = (np.asarray(ys)[keep] / np.maximum(np.asarray(errs)[keep], 1e-12)) ** 2
    W = np.sum(w)
    xb, yb = np.sum(w * x) / W, np.sum(w * y) / W
    sxx = np.sum(w * (x - xb) ** 2)
    slope = np.sum(w * (x - xb) * (y - yb)) / sxx
    resid = y - yb - slope * (x - xb)
    dof = max(len(x) - 2, 1)
    s2 = np.sum(w * resid ** 2) / dof
    return float(slope), float(np.sqrt(s2 / sxx))


def classify(slope, se):
    tol = max(0.30, 2 * se)
    if abs(slope - 2.0) <= tol:
        return "AREA"
    return "SUPER_AREA" if slope > 2.0 else "SUB_AREA"


def aggregate(rows):
    out = {"per_L": {}}

    def series(key_fn):
        Ls, mus, sems = [], [], []
        for L in LS:
            v = [key_fn(r) for r in rows
                 if r["L"] == L and key_fn(r) is not None]
            if v:
                Ls.append(L); mus.append(float(np.mean(v))); sems.append(sem(v))
        return Ls, mus, sems

    def get(r, wname, field):
        d = r["win"].get(wname)
        return d.get(field) if d and not d.get("skipped") else None

    for L in LS:
        rl = [r for r in rows if r["L"] == L]
        ent = dict(nseeds=len(rl),
                   N=float(np.mean([r["N"] for r in rl])),
                   wrap_frac=float(np.mean([r["wrap_frac"] for r in rl])),
                   max_pair_resid=float(max(r["pair_resid"] for r in rl)))
        for wname in WINDOWS:
            NOs = [get(r, wname, "N_O") for r in rl]
            NOs = [x for x in NOs if x]
            ent[wname] = dict(
                N_O=float(np.mean(NOs)) if NOs else 0,
                S_un=[float(np.mean(v)), sem(v)] if (v := [x for x in (get(r, wname, "S_un") for r in rl) if x is not None]) else None,
                S_a1=[float(np.mean(v)), sem(v)] if (v := [x for x in (get(r, wname, "S_a1") for r in rl) if x is not None]) else None,
                S_a2=[float(np.mean(v)), sem(v)] if (v := [x for x in (get(r, wname, "S_a2") for r in rl) if x is not None]) else None)
        s0 = [r.get("S0_fullbox") for r in rl if "S0_fullbox" in r]
        if s0:
            ent["S0_fullbox"] = float(s0[0])
        out["per_L"][f"L{L}"] = ent

    # ---- M3.1 (gate de reprodução)
    Ls, mu_un, se_un = series(lambda r: get(r, WMAIN, "S_un"))
    k_un, se_kun = loglog_slope(Ls, mu_un, se_un)
    _, mu_a1, se_a1 = series(lambda r: get(r, WMAIN, "S_a1"))
    ratio_L3 = (mu_un[-1] / mu_a1[-1]) if (mu_un and mu_a1 and mu_a1[-1] > 0) else float("nan")
    m31_pass = bool(1.5 <= k_un <= 2.5 and ratio_L3 > 2.0)
    out["M3_1"] = dict(kappa_un=k_un, se=se_kun, ratio_un_tr_L3=float(ratio_L3),
                       passa=m31_pass,
                       nota="gate de reprodução (Fase 0 §5.1): falha = engenharia, não física")

    # ---- M3.2 (a medição)
    k_a1, se_ka1 = loglog_slope(Ls, mu_a1, se_a1)
    cls1 = classify(k_a1, se_ka1)
    _, mu_a2, se_a2v = series(lambda r: get(r, WMAIN, "S_a2"))
    k_a2, se_ka2 = loglog_slope(Ls, mu_a2, se_a2v)
    cls2 = classify(k_a2, se_ka2)
    out["M3_2"] = dict(kappa_a1=k_a1, se_a1=se_ka1, class_a1=cls1,
                       kappa_a2=k_a2, se_a2=se_ka2, class_a2=cls2,
                       robustez_fraca=bool(cls1 != cls2),
                       veredito=cls1 + ("+ROBUSTEZ_FRACA" if cls1 != cls2 else ""))

    # ---- eixo-janela (diagnóstico volume-vs-área em L=3; razão vs 4)
    wdiag = {}
    for L in LS:
        e = out["per_L"][f"L{L}"]
        try:
            wdiag[f"L{L}"] = dict(
                trunc_WM_WH=float(e[WMAIN]["S_a1"][0] / e["WH"]["S_a1"][0]),
                untrunc_WM_WH=float(e[WMAIN]["S_un"][0] / e["WH"]["S_un"][0]))
        except (TypeError, ZeroDivisionError, KeyError):
            wdiag[f"L{L}"] = None
    out["window_axis"] = dict(razao_volume_prevista=4.0, razoes=wdiag,
                              nota="volume ⇒ ~4; área ⇒ ~1 (localiza no canto); "
                                   "WH só acima do piso N_O ≥ 40 (⇒ L=3)")
    return out


def main():
    t0 = time.time()
    rows = []
    if os.path.exists(ROWS_PATH) and not SMOKE:
        with open(ROWS_PATH, encoding="utf-8") as f:
            rows = [json.loads(l) for l in f if l.strip()]
        log(f"checkpoint: {len(rows)} rows carregadas")
    done = {(r["L"], r["seed"]) for r in rows}

    for L in LS:
        for s in range(NSEEDS):
            if (float(L), s) in done:
                continue
            r = run_case(L, s, do_sanity=(s == 0))
            rows.append(r)
            emit(r)
            wm = r["win"].get(WMAIN, {})
            log(f"L={L} s={s}: N={r['N']} N_O={wm.get('N_O')} "
                f"S_un={wm.get('S_un', float('nan')):.3f} "
                f"S_a1={wm.get('S_a1', float('nan')):.4f} "
                f"S_a2={wm.get('S_a2', float('nan')):.4f} "
                f"wrap={r['wrap_frac']:.3f} pr={r['pair_resid']:.1e}"
                + (f" S0={r.get('S0_fullbox'):.2e}" if "S0_fullbox" in r else ""))

    out = dict(meta=dict(base_seed=BASE_SEED, smoke=SMOKE, rho=RHO, tx=TX,
                         Ls=LS, nseeds=NSEEDS, windows=WINDOWS, alphas=ALPHAS),
               verdicts=aggregate(rows), runtime_s=time.time() - t0)
    json.dump(out, open(OUT_PATH, "w", encoding="utf-8"), indent=1)
    v = out["verdicts"]
    log(f"FIM {out['runtime_s']:.0f}s | M3.1 passa={v['M3_1']['passa']} "
        f"k_un={v['M3_1']['kappa_un']:.2f} | M3.2 {v['M3_2']['veredito']} "
        f"k_a1={v['M3_2']['kappa_a1']:.2f}±{v['M3_2']['se_a1']:.2f}")


if __name__ == "__main__":
    main()
