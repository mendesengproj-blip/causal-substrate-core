# -*- coding: utf-8 -*-
"""
n6_battery.py -- bateria SNA nas fases do path integral 2D (PRE_REGISTRO par.8).

Grade CONGELADA (implementacao dos '2 pontos por fase + 3 pela transicao'):
  multiplicadores de beta_pred=1.66/(N eps^2):
    random-side:   0.2, 0.5   | crystalline-side: 2.0, 4.0
    transicao:     0.85, 1.00, 1.15
  eps in {0.12, 0.21};  N in {30, 50, 70, 90, 120};  8 seeds/ponto =
  4 hot (init random) + 4 cold (init layered3)  [equilibracao FL1-style].
Sweeps: therm 2000 + 200 medidas a cada 5 (3000 total). Checkpoint JSONL
(n6_battery.jsonl): append por run; reinicio pula completados.
FILA ordenada: cristalino primeiro (medicao decisiva), depois random, depois
transicao; N crescente dentro de cada bloco.

SO RODA COM n6_gate.json VERDE.
"""
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from n6_core import run_point

HERE = os.path.dirname(os.path.abspath(__file__))
CKPT = os.path.join(HERE, "n6_battery.jsonl")

MULTS = {"crystal": [2.0, 4.0], "random": [0.2, 0.5],
         "transition": [0.85, 1.0, 1.15]}
EPSS = [0.12, 0.21]
NS = [30, 50, 70, 90, 120]
N_THERM, N_MEAS, MEAS_EVERY = 2000, 200, 5


def beta_pred(N, eps):
    return 1.66 / (N * eps * eps)


def queue():
    q = []
    for block in ("crystal", "random", "transition"):
        for N in NS:
            for eps in EPSS:
                for mult in MULTS[block]:
                    for s in range(8):
                        init = "random" if s < 4 else "layered3"
                        q.append({"block": block, "N": N, "eps": eps,
                                  "mult": mult, "seed": 31000 + s,
                                  "init": init})
    return q


def key(job):
    return (f"{job['block']}|N{job['N']}|e{job['eps']}|m{job['mult']}"
            f"|s{job['seed']}|{job['init']}")


def main():
    gate = json.loads(open(os.path.join(HERE, "n6_gate.json")).read())
    if gate["verdict"] != "GREEN":
        print("GATE NAO-VERDE -- bateria recusada.")
        sys.exit(1)
    done = set()
    if os.path.exists(CKPT):
        for line in open(CKPT):
            try:
                done.add(json.loads(line)["key"])
            except Exception:
                pass
    q = queue()
    todo = [j for j in q if key(j) not in done]
    print(f"N6 BATERIA: {len(q)} runs na grade congelada; "
          f"{len(done)} completos; {len(todo)} a rodar.")
    t0 = time.time()
    with open(CKPT, "a") as f:
        for i, job in enumerate(todo):
            b = job["mult"] * beta_pred(job["N"], job["eps"])
            r = run_point(job["N"], job["eps"], b, job["seed"], job["init"],
                          N_THERM, N_MEAS, MEAS_EVERY)
            r.update({"key": key(job), "block": job["block"],
                      "mult": job["mult"]})
            f.write(json.dumps(r) + "\n")
            f.flush()
            if (i + 1) % 16 == 0 or i == len(todo) - 1:
                el = time.time() - t0
                print(f"  [{i+1}/{len(todo)}] {job['block']} N={job['N']} "
                      f"eps={job['eps']} m={job['mult']} "
                      f"({el/60:.1f} min decorridos)", flush=True)
    print(f"BATERIA COMPLETA em {(time.time()-t0)/60:.1f} min. "
          f"Consolidar com n6_verdict.py.")


if __name__ == "__main__":
    main()
