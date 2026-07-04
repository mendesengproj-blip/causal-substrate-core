"""
make_figure.py -- dois paineis do gatilho da repulsao Lorentz-invariante:
(1) <z>(N) por alpha -- diverge em todo alpha (barreira 1 falha);
(2) C4(N) por alpha vs referencias da linhagem -- rastreia Poisson e decai
    (barreira 2 falha). As series por alpha caem QUASE EM CIMA umas das outras:
    a repulsao nao move nenhum dos dois observaveis. Veredito: MORTE_LIMPA.
"""
import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
meas = json.load(open(os.path.join(HERE, "repulsion.json")))

# referencias da linhagem (mesmo estimador C4 = mean local square clustering)
CSG_C4 = 0.0190        # plato intermediate do CSG (RS-CLUSTERING) -- tipo-arvore
CDT2D_C4 = 0.145       # tipo-CDT 2D (rede dim-finita) -- o unico que ARMA C4
POISSON_RS_C4 = 0.0291 # controle Poisson da RS-CLUSTERING (diamante)

alphas = [str(a) for a in meas["alphas"]]
colors = plt.cm.viridis(np.linspace(0.15, 0.85, len(alphas)))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13.5, 5.4))

for a, col in zip(alphas, colors):
    rows = meas["by_alpha"][a]["rows"]
    N = np.array([r["N_mean"] for r in rows])
    z = np.array([r["z_mean"] for r in rows]); ze = np.array([r["z_sem"] for r in rows])
    c4 = np.array([r["C4"] for r in rows]); c4e = np.array([r["C4_sem"] for r in rows])
    lab = (r"$\alpha=%s$ (Poisson)" % a) if float(a) == 0 else r"$\alpha=%s$" % a
    ax1.errorbar(N, z, yerr=ze, marker="o", color=col, capsize=2, lw=1.6, label=lab)
    ax2.errorbar(N, c4, yerr=c4e, marker="o", color=col, capsize=2, lw=1.6, label=lab)

# ---- painel 1: <z>(N) ----
ax1.set_xscale("log")
ax1.set_xlabel(r"$N$ (eventos retidos)")
ax1.set_ylabel(r"$\langle z\rangle$ (grafo de cobertura)")
ax1.set_title(r"Barreira 1: $\langle z\rangle(N)$ DIVERGE em todo $\alpha$"
              "\n(expoente local rel. +0.36 a +0.44; repulsao nao reduz a coordenacao)")
ax1.legend(fontsize=8, loc="upper left", title="repulsao")
ax1.grid(alpha=0.3, which="both")

# ---- painel 2: C4(N) vs referencias ----
ax2.set_xscale("log")
ax2.axhline(CDT2D_C4, ls="--", color="C3", lw=1.3, label=r"tipo-CDT 2D $C_4\approx0.145$ (ARMA)")
ax2.axhline(POISSON_RS_C4, ls=":", color="gray", label=r"Poisson-RS $C_4\approx0.029$")
ax2.axhline(CSG_C4, ls=":", color="C1", label=r"CSG $C_4\approx0.019$ (arvore)")
ax2.set_xlabel(r"$N$ (eventos retidos)")
ax2.set_ylabel(r"$C_4$ (square clustering, normalizado)")
ax2.set_title(r"Barreira 2: $C_4(N)$ DECAI e rastreia Poisson em todo $\alpha$"
              "\n(nao cria laco de dimensao finita; longe do tipo-CDT 2D)")
ax2.legend(fontsize=7.5, loc="upper right")
ax2.grid(alpha=0.3, which="both")

fig.suptitle("Processo de ponto com repulsao Lorentz-invariante (Matern II em $s^2$) "
             "— VEREDITO: MORTE_LIMPA (ambas as barreiras falham)", fontsize=11.5, y=1.02)
fig.tight_layout()
out = os.path.join(HERE, "repulsion.png")
fig.savefig(out, dpi=130, bbox_inches="tight")
print(f"figura salva: {out}")
