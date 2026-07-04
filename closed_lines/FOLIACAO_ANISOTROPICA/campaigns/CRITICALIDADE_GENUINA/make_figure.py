"""Figura: chi_max(N) controle vs foliado (mesmo expoente) + xi/L(N). NAO Lorentz-inv."""
import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, "criticality.json")))
c = d["comparison"]


def series(key):
    S = d[key]["sizes"]
    N = np.array([s["N_mean"] for s in S])
    chi = np.array([s["chi_max"] for s in S])
    xiL = np.array([min(s["rows"], key=lambda r: abs(r["J"] - s["Jc"]))["xi_over_L"] for s in S])
    return N, chi, xiL


Nc, chic, xilc = series("control_lattice")
Nf, chif, xilf = series("foliated_lam075")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13.5, 5.4))

# painel 1: chi_max(N) log-log
for N, chi, lab, col, x, xe in [
        (Nc, chic, "reticulado puro (controle)", "C0", c["chi_exp_control"], c["chi_exp_control_err"]),
        (Nf, chif, r"foliado $\lambda=0.75$ (NÃO Lorentz)", "C3", c["chi_exp_foliated"], c["chi_exp_foliated_err"])]:
    ax1.loglog(N, chi, "o-", color=col, lw=1.8, label=f"{lab}: x={x:.3f}±{xe:.3f}")
    ff = np.polyfit(np.log(N), np.log(chi), 1)
    ax1.loglog(N, np.exp(np.polyval(ff, np.log(N))), ":", color=col, alpha=0.6)
# referencia MF das 7 mortes
ax1.loglog(Nc, chic[0] * (Nc / Nc[0]) ** 0.2, "--", color="gray", alpha=0.7,
           label=r"MF causal (7 mortes) $x\approx0.1$–$0.24$")
ax1.set_xlabel("N"); ax1.set_ylabel(r"$\chi_{max}$")
ax1.set_title(r"$\chi_{max}\sim N^x$: foliado e reticulado MESMO expoente"
              "\n($\\Delta x/\\sigma=%.2f<2$ — classes INDISTINGUÍVEIS)" % c["diff_over_sigma"])
ax1.legend(fontsize=8); ax1.grid(alpha=0.3, which="both")

# painel 2: xi/L(N) at Jc
ax2.semilogx(Nc, xilc, "o-", color="C0", lw=1.8, label="reticulado (controle)")
ax2.semilogx(Nf, xilf, "o-", color="C3", lw=1.8, label=r"foliado $\lambda=0.75$")
ax2.set_xlabel("N"); ax2.set_ylabel(r"$\xi_{2nd}/L$ em $J_c$")
ax2.set_title("$\\xi/L$ ordem-1 e estável (criticalidade genuína, não MF);\n"
              "$J_c$ estável (controle 0.66, foliado ~0.32) — não deriva a 0")
ax2.legend(fontsize=8); ax2.grid(alpha=0.3, which="both")
ax2.set_ylim(0, max(xilf.max(), xilc.max()) * 1.4)

fig.suptitle("Criticalidade sobre FOLIACAO_ANISOTROPICA — NÃO LORENTZ-INVARIANTE — "
             "VEREDITO: criticalidade de RETICULADO conhecida (não é física nova)",
             fontsize=11, y=1.02, weight="bold")
fig.tight_layout()
out = os.path.join(HERE, "criticality.png")
fig.savefig(out, dpi=130, bbox_inches="tight")
print("figura:", out)
