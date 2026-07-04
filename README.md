# causal-substrate-core

The axiomatic core of a research programme on emergence over Lorentz-invariant
causal substrates: **what is a Lorentz-invariant discrete order permitted to
carry?** Two axioms (a Poisson-sprinkled causal order, forced by discreteness +
invariance, and a generic compact internal field), one pair lemma (*time with
sign, space without sign and without structure*), one three-layer boundary
theorem, a combinatorial trichotomy, a built-in thinning renormalization, a
parity no-go, and exactly two external inputs — each carrying a proof of its own
necessity.

## The two manuscripts

| Folder | Manuscript | Venue | Status |
|---|---|---|---|
| `core_paper/` | *What a Lorentz-invariant discrete order can carry: an axiomatic core for emergence on causal substrates* (8 pp) | Phys. Rev. D | Submission-ready |
| `wen_complement/` | *Why Lorentz-invariant causal sets cannot support an emergent U(1): a causal complement to string-net theory* (4 pp) | Class. Quantum Grav. | Submission-ready |

Each folder is self-contained (`.tex` + bibliography + cover letter) and compiles
with `pdflatex ×2` (core paper, embedded bibliography) or
`pdflatex → bibtex → pdflatex ×2` (Wen complement).

The measured inputs both papers cite come from the companion TEIC programme —
six manuscripts under review or submission-ready at MNRAS, PRD, PRL and CQG —
whose reproducible core is public at
**<https://github.com/mendesengproj-blip/TEIC>**.

## `campaigns/` — the pre-registered research record

Every claim graded [measured] in the manuscripts traces to a campaign executed
under the programme's discipline: **pre-registration before any code** (priors,
windows, kill criteria frozen in `PRE_REGISTRO.md`), engineering gates before
measurement, amendments only pre-run with a git trail, and negatives reported as
negatives. The `campaigns/` folder carries those records verbatim
(`RESULTADO.md` per campaign; phase-by-phase for the N4 quantization campaign):

- `N0_PRINCIPIO/`, `N0_STRESS_TEST/` — the boundary principle and its stress test
- `N1_CONTROLE_SU4/` — the compact target is *hosted, not selected* (SU(4) control)
- `N2_ENTROPIA_HORIZONTE/` — horizon entropy, two faces (geometric S∝A emerges;
  matter mutual information is super-area — the displayed failure of the area law)
- `N3_WEN_COMPLEMENT/` — the string-net complement (this repo's second paper)
- `N4_SJ_QUANTIZACAO/` — the Sorkin–Johnston quantization campaign (Q0 bit-theorem,
  the relativistic SJ vacuum, the Goldstone multiplet, the truncated horizon SSEE),
  with Gate G and phases 0–3
- `N5_SKYRME_RADIATIVO/` — the one-loop half of the Skyrme necessity proof
  (c_K^loop < 0 at ~130σ)
- `M1_TEOREMA_COMBINATORIO/`, `M3_ENDURECIMENTO/`, `M4_PAPER_NUCLEO/` — the
  combinatorial trichotomy, the proof hardening, and the core paper's build record

**Language note.** The campaign records are kept in Portuguese, the working
language of the research record; the manuscripts and this README are the English
interface. File references inside the records (`*.py`, `*.jsonl`, commit hashes)
point into the full research archive — code, raw outputs and checkpoints — which
is larger than this repository and **available from the author on request**.

## How to break these papers

The core is deductive, so it is attackable at named joints (stated in the
manuscripts): an emergent photon on an invariant causal substrate must break the
trichotomy through the pentagonal flank or falsify the pair lemma; emergent
chirality must break the isometry or exhaustion lemmas; an emergent scale must
exhibit a relevant direction under thinning; a radiatively stabilized Skyrmion
must overturn a 130σ measurement. A theory that tells you exactly where to hit
it is doing its job.

## License

MIT — see `LICENSE`.

## Author

Miqueias Alves Mendes — Independent Researcher, Ibiapina, Ceará, Brazil
(mikalvesm@gmail.com)
