"""make_figures.py -- NESS_GEOMETRIA: figuras de síntese (robusto a JSON faltante).

Painel 1 (Gate 2): área de histerese (produção de entropia/ciclo) vs período P -- a
assinatura adiabático<->não-adiabático. Painel 2 (escala, se houver): chi_max(N) sob NESS
com overlay das curvas de referência (Poisson N^0.07, CDT-equilíbrio N^0.24).
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent


def load(name):
    p = HERE / name
    return json.loads(p.read_text()) if p.exists() else None


def main():
    g2 = load("gate2.json") or load("gate2_smoke.json")
    sc = load("scaling_ness.json") or load("scaling_ness_smoke.json")
    br = load("b_resolution.json")
    npan = 1 + (1 if sc else 0) + (1 if br else 0)
    fig, axes = plt.subplots(1, npan, figsize=(6.2 * npan, 4.6))
    if npan == 1:
        axes = [axes]

    # --- Painel 1: histerese vs P (Gate 2) ---
    ax = axes[0]
    if g2:
        fe = g2.get("frac_envelope_vs_P", {})
        Ps = sorted(int(k) for k in fe)
        ys = [fe[str(P)] for P in Ps]
        ax.plot(Ps, ys, "o-", color="crimson", lw=2, ms=8)
        ax.set_xscale("log")
        ax.set_xlabel("período do drive  P  (sweeps/ciclo)")
        ax.set_ylabel("área de histerese / envelope  (≈ entropia/ciclo)")
        ax.set_title("Gate 2: quebra de balanço detalhado\n(pico=NESS; →0=adiabático/DB restaura)")
        ax.axhline(0, color="grey", lw=0.7)
        ax.grid(alpha=0.3)
    else:
        ax.text(0.5, 0.5, "gate2.json ausente", ha="center", va="center")

    # --- Painel 2: escala chi_max(N) com overlay ---
    if sc:
        ax = axes[1]
        B = sc.get("B_universality", {})
        per = B.get("per_size", {})
        Ns = np.array([per[k]["N0"] for k in per])
        chimax = np.array([per[k]["chi_max"] for k in per])
        order = np.argsort(Ns)
        Ns, chimax = Ns[order], chimax[order]
        ax.plot(Ns, chimax, "s-", color="navy", lw=2, ms=9,
                label=f"NESS  χ_max~N^{B.get('chi_max_exponent',float('nan')):.2f}")
        # overlays de referência (curvas conhecidas, ancoradas no 1º ponto da NESS)
        if len(Ns) >= 2:
            c0 = chimax[0] / (Ns[0] ** 0.0)
            xs = np.array([Ns.min(), Ns.max()])
            ax.plot(xs, chimax[0] * (xs / Ns[0]) ** 0.07, "--", color="grey",
                    label="Poisson N^0.07 (MF)")
            ax.plot(xs, chimax[0] * (xs / Ns[0]) ** 0.24, ":", color="green",
                    label="CDT-equilíbrio N^0.24")
            ax.plot(xs, chimax[0] * (xs / Ns[0]) ** 0.66, "-.", color="orange",
                    label="geométrico-3D N^0.66")
        ax.set_xscale("log"); ax.set_yscale("log")
        ax.set_xlabel("N (nós)"); ax.set_ylabel("χ_max")
        ax.set_title("Escala sob NESS vs referências")
        ax.legend(fontsize=8); ax.grid(alpha=0.3, which="both")

    # --- Painel 3: x(A) — resolução da Pergunta B (varredura de amplitude) ---
    if br:
        ax = axes[1 + (1 if sc else 0)]
        byA = br["by_A"]
        As = sorted(float(a) for a in byA)
        xs = [byA[str(a) if str(a) in byA else f"{a}"]["x"] for a in As]
        # tolera chaves "0.0" etc
        xs = [byA[k]["x"] for k in sorted(byA, key=lambda s: float(s))]
        As = sorted(float(a) for a in byA)
        ax.plot(As, xs, "o-", color="purple", lw=2, ms=9)
        ax.axhline(0.5, color="grey", ls="--", label="teto mean-field (0.5)")
        ax.axhline(0.66, color="orange", ls="-.", label="geométrico-3D (0.66)")
        ax.axhline(0.24, color="green", ls=":", label="CDT-equilíbrio (0.24)")
        ax.set_xlabel("amplitude do drive  A  (intensidade do não-equilíbrio)")
        ax.set_ylabel("expoente  x  de χ_max~N^x")
        ax.set_title("Resolução B: x(A) DISPERSO, sem tendência\n(= ruído/MF; o 0.53 era flutuação)")
        ax.set_ylim(0, 0.8)
        ax.legend(fontsize=8); ax.grid(alpha=0.3)

    fig.tight_layout()
    out = HERE / "ness_figures.png"
    fig.savefig(out, dpi=130)
    print(f"[escrito: {out}]  (gate2={'sim' if g2 else 'não'}, escala={'sim' if sc else 'não'})")


if __name__ == "__main__":
    main()
