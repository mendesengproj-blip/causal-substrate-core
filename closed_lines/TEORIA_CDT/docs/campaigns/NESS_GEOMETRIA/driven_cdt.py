"""driven_cdt.py -- NESS_GEOMETRIA: condução PARAMÉTRICA da geometria CDT 3D.

Pré-registro: PRE_REGISTRO.md (mecanismo (c) congelado). Reusa o motor F1b
(F1b_acao/f1b_cdt3d.py: CDT3D) e o equilibrador (f1b_dH.equilibrate) SEM tocar nos
5 movimentos de Pachner validados -- o drive é só k0(tau) variando por sweep, então o
validador check_manifold continua sendo o oráculo de cada configuração.

Drive: k0(tau) = k0_bar + A*cos(2*pi*tau/P).  A=0 recupera o F1b de equilíbrio verbatim
(controle nulo). Observáveis baratos por sweep: N3, N0, z=2*N1/N0, e os contadores de
aceitação por par de Pachner (do dict `stats` que CDT3D.sweep já preenche). d_H (caro,
BFS no grafo dual) é medido esparso.
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
# F1b_acao está em ../../../F1b_acao relativo a docs/campaigns/NESS_GEOMETRIA
CDT_DIR = HERE.parents[2] / "F1b_acao"
sys.path.insert(0, str(CDT_DIR))

from f1b_cdt3d import CDT3D            # noqa: E402  (motor CDT 3D, F1b, intacto)
from f1b_dH import equilibrate         # noqa: E402  (fase estendida, volume travado)

EPS = 0.0012                            # mesma rigidez de volume de F1b/cdt_substrate
ACC_KEYS = ("26", "62", "44", "23", "32")


def k0_of(tau, k0_bar, A, P):
    """k0 periódico no índice de sweep tau."""
    if A == 0.0 or P <= 0:
        return k0_bar
    return k0_bar + A * math.cos(2.0 * math.pi * tau / P)


def z_mean(g):
    """Grau médio do 1-esqueleto = 2*N1/N0 (barato: n_edges é mantido pelo motor)."""
    n0 = g.N0
    return 2.0 * g.n_edges / n0 if n0 else float("nan")


def build_driven(k0_bar, T, Vt, seed, therm=120):
    """Equilibra a geometria na fase estendida em k0_bar e devolve (g, k3).
    Volume travado por eps*(N3-Vt)^2; k3 calibrado e MANTIDO durante o drive."""
    g, k3 = equilibrate(k0_bar, T, Vt, seed, therm=therm, eps=EPS)
    return g, k3


def driven_run(g, k3, k0_bar, A, P, Vt, n_sweeps, seed_meas=0,
               dH_every=0, k3_gain=0.4, verbose=False):
    """Roda n_sweeps de dinâmica dirigida. Retorna dict de séries temporais.

    Por sweep registra: tau, fase do ciclo, k0, N3, N0, z, e o fluxo ACEITO de cada
    par (acc_26..acc_32) NAQUELE sweep (delta do dict stats). k3 adaptado suavemente
    p/ manter ⟨N3⟩≈Vt (o drive age na curvatura/coordenação, não no volume líquido).
    `dH_every`>0 mede d_H a cada dH_every sweeps (caro)."""
    gain = k3_gain * EPS
    rec = {k: [] for k in ("tau", "phase", "k0", "N3", "N0", "z", "k3")}
    for k in ACC_KEYS:
        rec["acc_" + k] = []
        rec["try_" + k] = []
    rec["dH_tau"] = []
    rec["dH"] = []
    prev = {("acc_" + k): 0 for k in ACC_KEYS}
    prev.update({("try_" + k): 0 for k in ACC_KEYS})
    stats = {}
    for tau in range(n_sweeps):
        k0 = k0_of(tau, k0_bar, A, P)
        g.sweep(k0, k3, EPS, Vt, n_steps=Vt, stats=stats)
        # adapta k3 para travar volume (mantém ⟨N3⟩≈Vt sob k0 variável)
        k3 += gain * (g.N3 - Vt)
        rec["tau"].append(tau)
        rec["phase"].append((tau % P) / P if (A != 0 and P > 0) else 0.0)
        rec["k0"].append(k0)
        rec["k3"].append(k3)
        rec["N3"].append(g.N3)
        rec["N0"].append(g.N0)
        rec["z"].append(z_mean(g))
        for k in ACC_KEYS:
            a = stats.get("acc_" + k, 0)
            t = stats.get("try_" + k, 0)
            rec["acc_" + k].append(a - prev["acc_" + k])
            rec["try_" + k].append(t - prev["try_" + k])
            prev["acc_" + k] = a
            prev["try_" + k] = t
        if dH_every and (tau + 1) % dH_every == 0:
            rec["dH_tau"].append(tau)
            rec["dH"].append(g.measure_dH(n_sources=30, seed=1000 + seed_meas + tau))
        if verbose and (tau % max(1, n_sweeps // 10) == 0):
            print(f"    tau={tau} k0={k0:.2f} N3={g.N3} N0={g.N0} z={z_mean(g):.2f}",
                  flush=True)
    for k in list(rec.keys()):
        rec[k] = np.asarray(rec[k], dtype=float)
    rec["manifold_ok"] = (len(g.check_manifold()) == 0)
    return rec


# ====================================================================== #
# CONTROLE NULO (sanidade): A=0 recupera o F1b de equilíbrio verbatim
# ====================================================================== #
def _smoke():
    print("=== driven_cdt smoke: controle nulo A=0 vs drive A>0 ===", flush=True)
    import time
    t0 = time.time()
    T, Vt = 8, 600
    g0, k3 = build_driven(2.5, T, Vt, seed=1, therm=40)
    print(f"  equilibrado: N3={g0.N3} N0={g0.N0} k3={k3:.3f} z={z_mean(g0):.2f} "
          f"manifold_ok={len(g0.check_manifold())==0}", flush=True)
    # A=0 (nulo)
    rec0 = driven_run(g0, k3, k0_bar=2.5, A=0.0, P=8, Vt=Vt, n_sweeps=40, dH_every=20)
    net0 = float(np.mean(rec0["acc_26"] - rec0["acc_62"]))
    print(f"  [A=0] N3 {rec0['N3'].mean():.0f}±{rec0['N3'].std():.0f}  "
          f"z {rec0['z'].mean():.2f}±{rec0['z'].std():.3f}  "
          f"net(26-62)/sweep={net0:+.2f}  manifold_ok={rec0['manifold_ok']}", flush=True)
    # A>0 (drive não-adiabático rápido, P pequeno)
    g1, k3b = build_driven(2.5, T, Vt, seed=2, therm=40)
    rec1 = driven_run(g1, k3b, k0_bar=2.5, A=1.5, P=4, Vt=Vt, n_sweeps=40, dH_every=20)
    print(f"  [A=1.5,P=4] N3 {rec1['N3'].mean():.0f}±{rec1['N3'].std():.0f}  "
          f"z {rec1['z'].mean():.2f}±{rec1['z'].std():.3f}  "
          f"k0 range [{rec1['k0'].min():.2f},{rec1['k0'].max():.2f}]  "
          f"manifold_ok={rec1['manifold_ok']}", flush=True)
    print(f"  z responde a k0? corr(k0,z)={np.corrcoef(rec1['k0'],rec1['z'])[0,1]:+.2f} "
          f"(A=0: corr={np.corrcoef(rec0['k0'],rec0['z'])[0,1] if rec0['k0'].std()>0 else 0:+.2f})",
          flush=True)
    print(f"  [{time.time()-t0:.0f}s] smoke OK", flush=True)


if __name__ == "__main__":
    _smoke()
