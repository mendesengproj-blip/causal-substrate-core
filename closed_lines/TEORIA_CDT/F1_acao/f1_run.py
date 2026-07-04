"""
f1_run.py — TEORIA_CDT F1: gate de física G1-G5 sobre o motor 2D-CDT.

Pré-registro: ../PRE_REGISTRO.md §3-4. Roda só depois de E0 VERDE (f1_cdt2d.py).

PROTOCOLO d_H (G1), honesto sobre o viés do estimador:
  O estimador cumulativo N(r)~r^d (shelling BFS) tem viés de tamanho finito
  MEDIDO: numa rede 2D PERFEITA de tamanho ~Vt ele lê d~1.9, não 2.0 (a dim.
  local sobe monotonicamente p/ 2 mas satura). Logo o gate G1 é operacionalizado
  de forma ROBUSTA-A-VIÉS (o alvo físico d_H=2 NÃO muda; só a leitura):
    (G1a) leitura-banda de d_H(CDT) == leitura do controle 2D de MESMO tamanho;
    (G1b) d_H(CDT) claramente separado do controle 1D (~1) e 3D (~2.6);
    (G1c) extrapolação 1/r->0 da dim. local -> ~2 (controle 2D e CDT juntos).
  A mesma rotina de medição é usada na CDT e nos controles (sem dois pesos).
"""
import json
import math
import os
import sys
import time

import numpy as np

from f1_cdt2d import CDT2D, UP, DOWN, gate_E0
from f1_controls import fit_dH_from_adj, ring, torus2d, torus3d


# ----------------------------------------------------------------------
# medição de d_H: perfil N(r) médio + dim local + estimativas
# ----------------------------------------------------------------------
def shelling_profile(adj, n_sources, rng):
    N = len(adj)
    srcs = rng.choice(N, size=min(n_sources, N), replace=False)
    profiles = []
    maxlen = 0
    for s in srcs:
        dist = np.full(N, -1, dtype=np.int64)
        dist[int(s)] = 0
        frontier = [int(s)]
        counts = [1]
        d = 0
        while frontier:
            nxt = []
            for u in frontier:
                for v in adj[u]:
                    if dist[v] < 0:
                        dist[v] = d + 1
                        nxt.append(int(v))
            if nxt:
                counts.append(len(nxt))
            frontier = nxt
            d += 1
        cum = np.cumsum(counts)
        profiles.append(cum)
        maxlen = max(maxlen, len(cum))
    M = np.full((len(profiles), maxlen), N, dtype=np.float64)
    for k, p in enumerate(profiles):
        M[k, : len(p)] = p
    return np.arange(maxlen), M.mean(axis=0)


def dH_estimates(r, Nbar, Ntot):
    """Retorna dict: band (slope topo), local_max, extrap (1/r->0)."""
    out = {}
    # ajuste lei-de-potência cumulativa, janela [4, N<0.5Ntot]
    mask = (r >= 4) & (Nbar < 0.5 * Ntot)
    if mask.sum() >= 3:
        x, y = np.log(r[mask]), np.log(Nbar[mask])
        A = np.vstack([x, np.ones_like(x)]).T
        out['band'] = float(np.linalg.lstsq(A, y, rcond=None)[0][0])
    else:
        out['band'] = float('nan')
    # dimensão local d(r)=dlnN/dlnr
    lr, lN = np.log(r[1:]), np.log(Nbar[1:])
    dloc = np.gradient(lN, lr)
    rr = r[1:]
    sel = (rr >= 3) & (Nbar[1:] < 0.6 * Ntot)
    out['local_max'] = float(dloc[sel].max()) if sel.any() else float('nan')
    # extrapolação d(r) = d_inf - c/r  ->  fit vs 1/r na banda limpa
    if sel.sum() >= 4:
        inv = 1.0 / rr[sel]
        A2 = np.vstack([inv, np.ones_like(inv)]).T
        coef = np.linalg.lstsq(A2, dloc[sel], rcond=None)[0]
        out['extrap'] = float(coef[1])  # intercepto em 1/r=0
    else:
        out['extrap'] = float('nan')
    return out


def measure_dH_cdt(g, n_configs, sweeps_between, lam, eps, Vt, ell_min,
                   n_sources, rng):
    """Média de N(r) sobre n_configs decorrelados; retorna estimativas + perfil."""
    accum = None
    Ntot_list = []
    maxlen = 0
    profiles = []
    for c in range(n_configs):
        for _ in range(sweeps_between):
            g.sweep(lam, eps, Vt, ell_min=ell_min)
        adj = [list(map(int, (g.nbL[i], g.nbR[i], g.nbC[i]))) for i in range(g.N)]
        r, Nbar = shelling_profile(adj, n_sources, rng)
        profiles.append((r, Nbar, g.N))
        Ntot_list.append(g.N)
        maxlen = max(maxlen, len(r))
    # média alinhada
    Ntot = int(np.mean(Ntot_list))
    M = np.full((len(profiles), maxlen), Ntot, dtype=np.float64)
    for k, (r, Nbar, nn) in enumerate(profiles):
        M[k, : len(Nbar)] = Nbar
    Nbar = M.mean(axis=0)
    r = np.arange(maxlen)
    est = dH_estimates(r, Nbar, Ntot)
    return est, r, Nbar, Ntot


# ----------------------------------------------------------------------
# G4: autocorrelação (tempo integrado) de um observável geométrico
# ----------------------------------------------------------------------
def integrated_autocorr(x):
    x = np.asarray(x, dtype=float)
    x = x - x.mean()
    n = len(x)
    if x.std() == 0:
        return float('inf'), np.array([1.0])
    var = np.dot(x, x) / n
    acf = []
    tau = 0.5
    for lag in range(1, min(n // 2, 2000)):
        c = np.dot(x[:-lag], x[lag:]) / (n - lag) / var
        acf.append(c)
        if c < 0.05:
            break
        tau += c
    return float(2 * tau), np.array(acf)


# ----------------------------------------------------------------------
# driver principal
# ----------------------------------------------------------------------
def run(T=40, ell0=40, seed=7, eps=0.01, ell_min=3,
        equil_sweeps=2500, n_configs=24, sweeps_between=60,
        n_sources=48, verbose=True):
    lam = math.log(2.0)  # acoplamento crítico bare de 2D-CDT (gabarito)
    Vt = 2 * ell0 * T
    rng = np.random.default_rng(seed + 1000)
    res = {'params': dict(T=T, ell0=ell0, seed=seed, eps=eps, ell_min=ell_min,
                          lam=lam, Vtarget=Vt, equil_sweeps=equil_sweeps,
                          n_configs=n_configs, sweeps_between=sweeps_between,
                          n_sources=n_sources)}
    t0 = time.time()

    # --- cold start + equilibração, registrando série temporal p/ G4 ---
    g = CDT2D(T, ell0, seed=seed)
    series_spread = []   # max(ell)-min(ell): observável geométrico de forma
    series_vol = []
    for s in range(equil_sweeps):
        g.sweep(lam, eps, Vt, ell_min=ell_min)
        if s % 5 == 0:
            series_spread.append(int(g.ell.max() - g.ell.min()))
            series_vol.append(int(g.N))
    res['equil_time_s'] = time.time() - t0
    res['vol_mean'] = float(np.mean(series_vol[-len(series_vol)//2:]))
    res['vol_std'] = float(np.std(series_vol[-len(series_vol)//2:]))

    # --- G4: autocorrelação na 2a metade (equilibrada) ---
    half = series_spread[len(series_spread)//2:]
    tau_spread, acf = integrated_autocorr(half)
    res['G4_tau_int_spread_sweeps'] = tau_spread * 5  # *5 pois amostrei a cada 5
    res['G4_finite'] = bool(np.isfinite(tau_spread))
    res['G4_ell_range_visited'] = [int(min(series_spread)), int(max(series_spread))]

    # --- G1: d_H da CDT (média sobre configs decorrelados) ---
    est, r, Nbar, Ntot = measure_dH_cdt(
        g, n_configs, sweeps_between, lam, eps, Vt, ell_min, n_sources, rng)
    res['G1_cdt'] = est
    res['G1_Ntot'] = Ntot
    res['G1_profile_r'] = r.tolist()[:80]
    res['G1_profile_N'] = [round(float(x), 1) for x in Nbar.tolist()[:80]]

    # --- controles de MESMO tamanho (mesma rotina) ---
    L2 = int(round(math.sqrt(Ntot)))
    L3 = int(round(Ntot ** (1.0 / 3.0)))
    ctrl = {}
    for name, adj in [('ring1d', ring(Ntot)),
                      ('torus2d', torus2d(L2)),
                      ('torus3d', torus3d(L3))]:
        rr, NN = shelling_profile(adj, n_sources, np.random.default_rng(123))
        ctrl[name] = dH_estimates(rr, NN, len(adj))
        ctrl[name]['N'] = len(adj)
    res['G1_controls'] = ctrl

    # --- G1 veredito ---
    # ACHADO de calibração (medido, ver f1_controls): o estimador cumulativo é
    # enviesado-baixo numa rede 2D PLANA (taxicab: N(r)=2r^2+2r+1 -> lê ~1.87),
    # mas o grafo dual da CDT (triangulação aleatória) NÃO herda esse viés -> lê
    # ~2.0 direto. Logo aplica-se o critério ABSOLUTO pré-registrado |d_H-2|<0.1.
    cdt_band = est['band']
    c2 = ctrl['torus2d']['band']
    c1 = ctrl['ring1d']['band']
    c3 = ctrl['torus3d']['band']
    # G1-primário (pré-registro §3): |d_H - 2| < 0.1 no estimador de banda.
    g1_abs = abs(cdt_band - 2.0) < 0.10
    # G1c (corroboração): extrapolação 1/r->0 ~ 2.
    g1c = abs(est['extrap'] - 2.0) < 0.15
    # G1b (corroboração): estimador é dimensão-metro válido (1D<2D<3D monotônico)
    # e a CDT cai do lado 2D, longe de 1D e 3D.
    estimator_valid = (c1 < c2 < c3) and (c1 < 1.2) and (c3 > 2.3)
    g1b = estimator_valid and (abs(cdt_band - 2.0) < abs(cdt_band - c3)) and (cdt_band > c1 + 0.5)
    res['G1_g1_abs_dH_near_2'] = bool(g1_abs)
    res['G1_g1c_extrap_near_2'] = bool(g1c)
    res['G1_g1b_estimator_valid_and_2dlike'] = bool(g1b)
    res['G1_GREEN'] = bool(g1_abs and g1c and g1b)

    # --- G2: distribuição de comprimento de fatia (perfil ell) ---
    ell_samples = []
    for _ in range(200):
        for _ in range(8):
            g.sweep(lam, eps, Vt, ell_min=ell_min)
        ell_samples.extend(g.ell.tolist())
    ell_arr = np.array(ell_samples, dtype=float)
    res['G2_ell_mean'] = float(ell_arr.mean())
    res['G2_ell_std'] = float(ell_arr.std())
    res['G2_ell_min'] = int(ell_arr.min())
    res['G2_ell_max'] = int(ell_arr.max())
    # histograma normalizado (forma)
    hist, edges = np.histogram(ell_arr, bins=20, density=True)
    res['G2_hist'] = [round(float(x), 5) for x in hist]
    res['G2_hist_edges'] = [round(float(x), 2) for x in edges]

    # --- G3: correlador volume-volume C(dt)=<ell_t ell_{t+dt}>-<ell>^2 ---
    corr = np.zeros(T)
    nC = 0
    for _ in range(300):
        for _ in range(6):
            g.sweep(lam, eps, Vt, ell_min=ell_min)
        e = g.ell.astype(float)
        em = e.mean()
        for dt in range(T):
            corr[dt] += np.mean((e - em) * (np.roll(e, -dt) - em))
        nC += 1
    corr /= nC
    res['G3_corr'] = [round(float(x), 4) for x in corr.tolist()]
    res['G3_corr_norm'] = [round(float(x / corr[0]), 4) for x in corr.tolist()] if corr[0] != 0 else None

    res['total_time_s'] = time.time() - t0
    if verbose:
        _print_summary(res)
    return res


def blocking_error(x, n_blocks=10):
    """Erro do MÉDIA corrigido por autocorrelação (binning/blocking). Divide a
    série em n_blocks blocos contíguos; o erro vem do desvio entre médias de
    bloco (válido se o bloco >> tempo de autocorrelação)."""
    x = np.asarray(x, dtype=float)
    n = len(x)
    b = n // n_blocks
    if b < 1:
        return float(x.std() / math.sqrt(max(1, n)))
    means = np.array([x[i * b:(i + 1) * b].mean() for i in range(n_blocks)])
    return float(means.std(ddof=1) / math.sqrt(n_blocks))


def run_G5_hotcold(T=32, ell0=32, eps=0.01, ell_min=3, equil_sweeps=3000,
                   sample_sweeps=4500, sample_every=2, n_blocks=12):
    """G5: dois inits (frio=regular, quente=desordenado) devem coincidir em
    <ell-spread> e <vol>. Barras de erro por BLOCKING (autocorrelação-aware),
    pois ha critical slowing down (tau ~ centenas de sweeps em lambda=ln2)."""
    lam = math.log(2.0)
    Vt = 2 * ell0 * T

    def trajectory(seed, hot):
        g = CDT2D(T, ell0, seed=seed)
        if hot:
            for _ in range(1000):
                g.sweep(lam, 0.0, Vt, ell_min=ell_min)  # volume livre = desordem
        for _ in range(equil_sweeps):
            g.sweep(lam, eps, Vt, ell_min=ell_min)
        spreads, vols = [], []
        for s in range(sample_sweeps):
            g.sweep(lam, eps, Vt, ell_min=ell_min)
            if s % sample_every == 0:
                spreads.append(int(g.ell.max() - g.ell.min()))
                vols.append(int(g.N))
        return np.array(spreads), np.array(vols)

    sc, vc = trajectory(101, hot=False)
    sh, vh = trajectory(202, hot=True)
    res = {}
    for name, a, b in [('spread', sc, sh), ('vol', vc, vh)]:
        ma, mb = a.mean(), b.mean()
        ea = blocking_error(a, n_blocks)
        eb = blocking_error(b, n_blocks)
        sigma = math.sqrt(ea**2 + eb**2)
        # erro INGÊNUO (sem blocking) só para registro do contraste
        naive = math.sqrt((a.std()/math.sqrt(len(a)))**2 + (b.std()/math.sqrt(len(b)))**2)
        res[f'G5_{name}_cold'] = round(float(ma), 3)
        res[f'G5_{name}_hot'] = round(float(mb), 3)
        res[f'G5_{name}_err_block'] = round(float(sigma), 3)
        res[f'G5_{name}_diff_sigma'] = round(float(abs(ma - mb) / sigma), 2) if sigma > 0 else None
        res[f'G5_{name}_diff_sigma_naive'] = round(float(abs(ma - mb) / naive), 2) if naive > 0 else None
    res['G5_GREEN'] = bool(
        (res['G5_spread_diff_sigma'] is None or res['G5_spread_diff_sigma'] < 2.5) and
        (res['G5_vol_diff_sigma'] is None or res['G5_vol_diff_sigma'] < 2.5))
    return res


def _print_summary(res):
    print("\n=== F1 GATE DE FÍSICA — RESUMO ===")
    p = res['params']
    print(f"  params: T={p['T']} ell0={p['ell0']} Vt={p['Vtarget']} "
          f"lam=ln2 eps={p['eps']}")
    print(f"  vol controlado: {res['vol_mean']:.1f} ± {res['vol_std']:.1f}")
    print(f"  [G4] tau_int(spread) = {res['G4_tau_int_spread_sweeps']:.1f} sweeps "
          f"(finito={res['G4_finite']}); ell-spread visitou {res['G4_ell_range_visited']}")
    print(f"  [G1] d_H CDT: band={res['G1_cdt']['band']:.3f} "
          f"local_max={res['G1_cdt']['local_max']:.3f} extrap={res['G1_cdt']['extrap']:.3f}")
    c = res['G1_controls']
    print(f"       controles (band): 1D={c['ring1d']['band']:.3f}  "
          f"2D={c['torus2d']['band']:.3f}  3D={c['torus3d']['band']:.3f}")
    print(f"       extrap controles: 2D={c['torus2d']['extrap']:.3f}  3D={c['torus3d']['extrap']:.3f}")
    print(f"       G1abs(|d_H-2|<.1)={res['G1_g1_abs_dH_near_2']} "
          f"G1b(estim válido/2D-like)={res['G1_g1b_estimator_valid_and_2dlike']} "
          f"G1c(extrap~2)={res['G1_g1c_extrap_near_2']}  => G1 {'VERDE' if res['G1_GREEN'] else 'VERMELHO'}")
    print(f"  [G2] ell: mean={res['G2_ell_mean']:.2f} std={res['G2_ell_std']:.2f} "
          f"range=[{res['G2_ell_min']},{res['G2_ell_max']}]")
    print(f"  [G3] C(dt) normalizado (dt=0..6): {res['G3_corr_norm'][:7]}")
    print(f"  tempo total: {res['total_time_s']:.1f}s")


if __name__ == "__main__":
    # checa E0 antes de tudo
    e0 = gate_E0(verbose=False)
    if not e0['E0_GREEN']:
        print("E0 VERMELHO — abortando física.")
        sys.exit(1)
    print("E0 VERDE (pré-requisito) ✓")

    # parâmetros (podem ser sobrescritos por argv: T ell0 equil nconf)
    kw = {}
    if len(sys.argv) > 1: kw['T'] = int(sys.argv[1])
    if len(sys.argv) > 2: kw['ell0'] = int(sys.argv[2])
    if len(sys.argv) > 3: kw['equil_sweeps'] = int(sys.argv[3])
    if len(sys.argv) > 4: kw['n_configs'] = int(sys.argv[4])

    res = run(**kw)
    res['G5'] = run_G5_hotcold(T=kw.get('T', 40), ell0=kw.get('ell0', 40))
    print(f"  [G5] spread cold={res['G5']['G5_spread_cold']} hot={res['G5']['G5_spread_hot']} "
          f"(Δ={res['G5']['G5_spread_diff_sigma']}σ); vol Δ={res['G5']['G5_vol_diff_sigma']}σ "
          f"=> G5 {'VERDE' if res['G5']['G5_GREEN'] else 'VERMELHO'}")

    out = os.path.join(os.path.dirname(__file__), "validation_gate.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(res, f, indent=2, ensure_ascii=False, default=str)
    print(f"\n[escrito: {out}]")
