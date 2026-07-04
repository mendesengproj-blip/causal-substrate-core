# causal-substrate-core

The axiomatic core of a research programme on emergence over Lorentz-invariant
causal substrates: **what is a Lorentz-invariant discrete order permitted to
carry?** Two axioms (a Poisson-sprinkled causal order, forced by discreteness +
invariance, and a generic compact internal field), one pair lemma (*time with
sign, space without sign and without structure*), one three-layer boundary
theorem, a combinatorial trichotomy, a built-in thinning renormalization, a
parity no-go, and exactly two external inputs — each carrying a proof of its own
necessity.

## The manuscripts

| Folder | Manuscript | Venue | Status |
|---|---|---|---|
| `core_paper/` | *What a Lorentz-invariant discrete order can carry: an axiomatic core for emergence on causal substrates* (8 pp) | Phys. Rev. D | Submitted |
| `wen_complement/` | *Why Lorentz-invariant causal sets cannot support an emergent U(1): a causal complement to string-net theory* (4 pp) | Class. Quantum Grav. | Submitted |
| `constraints_paper/` | *What any causal-substrate model must satisfy: structural constraints as a checklist for emergent physics* (5 pp) | Found. Phys. / CQG (perspective) | Draft — awaiting companion reviews |

The first two are self-contained (`.tex` + bibliography + cover letter) and compile
with `pdflatex ×2` (core paper, embedded bibliography) or
`pdflatex → bibtex → pdflatex ×2` (Wen complement). The constraints paper packages
the programme's necessity theorems as an explicit checklist any model built on a
causal order must pass, and proves its four own classification results
(Sec. below) in a self-contained appendix; it compiles with `pdflatex ×2`.

The measured inputs both papers cite come from the companion TEIC programme —
six manuscripts under review or submission-ready at MNRAS, PRD, PRL and CQG —
whose reproducible core is public at
**<https://github.com/mendesengproj-blip/TEIC>**.

## `campaigns/` — the pre-registered research record, with its code and data

Every claim graded [measured] in the manuscripts traces to a campaign executed
under the programme's discipline: **pre-registration before any code** (priors,
windows, kill criteria frozen in `PRE_REGISTRO.md`), engineering gates before
measurement, amendments only pre-run with a git trail, and negatives reported as
negatives. The `campaigns/` folder carries those records verbatim — and, for the
computational campaigns, the **generators themselves plus the emitted verdicts**
(`*.py` + `*.json`/`*.jsonl` with run parameters and numbers embedded), so every
quoted number can be checked against its recorded run and re-executed:

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
- `M1B_FLANCO_PENTAGONAL/` — the pentagonal flank *constructed*: rank-frustrated
  percolating loop lattices exist, but only as rigid non-invariant crystals
- `M1C_FRONTEIRA_NAO_POISSON/` — the non-Poisson frontier *closes* by a geometric
  dichotomy (dense ⇒ 1D blocks via posts; sparse ⇒ hyperbolic Galton–Watson tree),
  with the closure hardened to theorem on the transitive-percolation axis
- `F2_CONTROLE_G2/` — the exceptional-group control: G₂ (trivial center) mirrors
  SU(N); confinement is center-independent at the accessible scales

### The classification series and the constraints checklist

The programme's second-generation results — necessity theorems read forwards, as
a decision procedure — ship as their own campaigns, and are packaged by
`constraints_paper/`:

- `M5_CLASSIFICACAO/` — the classification theorem: a substrate is
  string-net-admissible **iff** it is non-invariant (unified battery across every
  named class)
- `M6_HOSPEDAGEM/` — the hosting theorem: the coupling factors through the
  bi-invariant metric, so the matter form is an a priori function of the compact
  target *X = G/H* (Goldstone count = dim *X*, certified across SU(2/3/4), G₂, and
  the coset O(3)/S²=2)
- `M8_TOPOLOGIA/` — the topological classification: protected matter textures are
  exactly π_n(X)≠0 (charge survives thinning); gauge defects are forbidden
- `M9_SIMETRIAS_DISCRETAS/` — the discrete-symmetry classification by the carrier
  criterion: a symmetry breaks iff it has an intrinsic carrier (P never, T
  empirically, C dynamically)

## `closed_lines/` — the substrate-family measurements behind the trichotomy

The core paper's Sec. IV states that the programme *measured* seven substrate
families fail the string-net requirements ("the binary alternative") before the
trichotomy made it a theorem. Those closed research lines ship here verbatim,
code + verdicts + closing records: `REPULSAO_LORENTZ/` (Lorentz-invariant pair
repulsion: Matérn II in s², clean death), `TEORIA_CDT/` (the CDT-substrate line:
3D engine, the falsified information-seed, the NESS drive, the 4D kinematic
trigger), `FOLIACAO_ANISOTROPICA/` (the foliated Hořava–Lifshitz escape — breaks
Lorentz by construction, labelled as such), `NAO_PAIRWISE_E_NEQ/`,
`SINTESE_SETE_MORTES/` (the binary-structure synthesis), `MECANISMOS_DE_ESCALA/`
and `LEVANTAMENTO_PRE_CAUSAL/` (analytical closings). The remaining families
(Poisson itself, the Rideout–Sorkin growth models, long-range percolation) are
measured in the TEIC repository's `docs/campaigns/`.

**Language note.** The campaign records are kept in Portuguese, the working
language of the research record; the manuscripts and this README are the English
interface. The `*.py` generators and `*.json`/`*.jsonl` outputs the records cite
ship in the same folders (commit hashes refer to the programme's working
history). The programme charter and roadmap (`CHARTER.md`, `ROADMAP_V2.md`) sit
at the repository root. Requirements: Python 3.12 with `numpy` and `scipy`.

## How to break these papers

The core is deductive, so it is attackable at named joints (stated in the
manuscripts): an emergent photon on an invariant causal substrate must falsify the
pair lemma or leave the Poisson measure — the pentagonal-flank route through the
trichotomy is now closed by construction (its only realization is a non-invariant
crystal, `M1B_`), and the non-Poisson route is closed for sequential growth
(`M1C_`), so the two combinatorial escapes have merged into the single live
frontier of genuinely non-Markovian dynamical geometry; emergent chirality must
break the isometry or exhaustion lemmas (equivalently, exhibit a carrier for
parity, `M9_`); an emergent scale must exhibit a relevant direction under
thinning; a radiatively stabilized Skyrmion must overturn a 130σ measurement. A
theory that tells you exactly where to hit it is doing its job.

## License

MIT — see `LICENSE`.

## Author

Miqueias Alves Mendes — Independent Researcher, Ibiapina, Ceará, Brazil
(mikalvesm@gmail.com)
