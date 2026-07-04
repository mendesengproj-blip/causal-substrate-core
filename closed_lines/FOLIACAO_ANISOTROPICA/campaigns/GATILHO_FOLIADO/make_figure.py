"""Figura do gatilho foliado: C4(N) por lam (arma, acima do tipo-CDT 2D) e z(lam) no
topo (finito, cresce com o acoplamento tipo-tempo). NAO Lorentz-invariante (titulo)."""
import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
meas = json.load(open(os.path.join(HERE, "foliated.json")))

CDT2D_C4 = 0.145
POISSON_C4 = 0.029
DEATH = 0.02

lams = [float(k) for k in meas["by_lam"]]
colors = plt.cm.plasma(np.linspace(0.1, 0.85, len(lams)))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13.5, 5.4))

# painel 1: C4(N) por lam
for k, col in zip(meas["by_lam"], colors):
    R = meas["by_lam"][k]; rows = R["rows"]
    N = [r["N"] for r in rows]; c4 = [r["C4"] for r in rows]; ce = [r["C4_sem"] for r in rows]
    lab = r"$\lambda=%s$%s" % (k, " (fatias soltas)" if float(k) == 0 else "")
    ax1.errorbar(N, c4, yerr=ce, marker="o", color=col, lw=1.6, capsize=2, label=lab)
ax1.axhline(CDT2D_C4, ls="--", color="green", label=r"tipo-CDT 2D $C_4\approx0.145$ (armou)")
ax1.axhline(POISSON_C4, ls=":", color="gray", label=r"Poisson $C_4\approx0.029$")
ax1.axhline(DEATH, ls=":", color="red", label=r"limiar de morte 0.02")
ax1.set_xscale("log"); ax1.set_xlabel("N (eventos)"); ax1.set_ylabel(r"$C_4$")
ax1.set_title(r"Barreira 2: $C_4(N)$ SATURA positivo em TODO $\lambda$"
              "\n(estrutura de fatia sobrevive ao acoplamento tipo-tempo)")
ax1.legend(fontsize=7.5, loc="center right"); ax1.grid(alpha=0.3, which="both")

# painel 2: z(lam) e C4(lam) no topo N
ztop = [meas["by_lam"][k]["rows"][-1]["z_mean"] for k in meas["by_lam"]]
c4top = [meas["by_lam"][k]["rows"][-1]["C4"] for k in meas["by_lam"]]
ax2.plot(lams, ztop, marker="s", color="C3", lw=1.8, label=r"$\langle z\rangle$ (topo N)")
ax2.set_xlabel(r"$\lambda$ (anisotropia de Lifshitz $r_t/r_s$)")
ax2.set_ylabel(r"$\langle z\rangle$", color="C3"); ax2.tick_params(axis="y", labelcolor="C3")
ax2.set_title(r"$\langle z\rangle$ finito e cresce com $\lambda$ (orbita compacta);"
              "\n$C_4$ persiste — ARMA p/ $\\lambda>0$ (espaco-tempo genuino)")
ax2b = ax2.twinx()
ax2b.plot(lams, c4top, marker="o", color="C0", lw=1.8, label=r"$C_4$ (topo N)")
ax2b.axhline(DEATH, ls=":", color="red")
ax2b.set_ylabel(r"$C_4$", color="C0"); ax2b.tick_params(axis="y", labelcolor="C0")
ax2b.set_ylim(0, max(c4top) * 1.3)
ax2.grid(alpha=0.3)

fig.suptitle("Substrato FOLIADO anisotropico (Horava-Lifshitz discreto) -- "
             "NAO LORENTZ-INVARIANTE -- VEREDITO: ARMA (ambas as barreiras)",
             fontsize=11.5, y=1.02, weight="bold")
fig.tight_layout()
out = os.path.join(HERE, "foliated.png")
fig.savefig(out, dpi=130, bbox_inches="tight")
print("figura salva:", out)
