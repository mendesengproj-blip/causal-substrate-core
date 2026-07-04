"""Chunk runner for phase 2b (workaround for background tasks being killed):
runs a subset of (J, L, seed) cases in the foreground and appends JSONL rows.
Usage: python n2_phase2b_chunk.py <J> <L> <seed0> <seed1>
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from n2_phase2b import run_case

HERE = Path(__file__).resolve().parent
OUT = HERE / "n2_phase2b_rows.jsonl"

J = float(sys.argv[1])
L = float(sys.argv[2])
s0, s1 = int(sys.argv[3]), int(sys.argv[4])

with OUT.open("a") as f:
    for seed in range(s0, s1):
        r = run_case(L, seed, J)
        row = {"J": J, "L": L, "seed": seed, **r}
        f.write(json.dumps(row) + "\n")
        print(f"J={J} L={L} seed={seed}: I={r['I']:.3f} shuf={r['I_shuffle']:.3f} "
              f"m={r['m']:.3f} ESS={r['ess']:.0f}", flush=True)
