# Source fidelity and validation record

Audit date: **2026-11-13 (Asia/Shanghai)**.

## Source contract

- Entry: PALOMAR-2026-10-09-000005, version 1.
- Exact user permalink: https://palomar-registry.org/entry?id=PALOMAR-2026-10-09-000005&version=1
- Machine-readable record actually used: https://data.palomar-registry.org/entries/PALOMAR-2026-10-09-000005-v1.json
- Upstream: https://github.com/mrklwk/zeta-density-three-over-two-sigma-lean
- Pinned revision: `804bdb55b1fc40e6a1a6878fd96078644a70e288`.
- Download URL: https://codeload.github.com/mrklwk/zeta-density-three-over-two-sigma-lean/tar.gz/804bdb55b1fc40e6a1a6878fd96078644a70e288
- Original project path: `lean/`.
- Registered toolchain: `leanprover/lean4:v4.35.0-rc2`.
- Registered mathlib revision: `065356127b1dc0016f66b7283ce0ce2c4055aa55`.

The source snapshot was not edited. Its existing comments, receipts, manifests and licensing files are archived as historical source material, not assertions of fresh verification performed in this task.

## Checks actually performed in this task

### 1. Exact downloaded source preservation

Every one of the **560 regular files** in `registered-source.tar.gz` was compared byte-for-byte with the extracted snapshot: **zero mismatches**.

Archive SHA-256:
`e6fb642043c8e24fcc8ea171d7786cb6a7a2a47467d9a0fe741fe815e2566efc`.

Pinned `lean/Solution.lean` SHA-256:
`2316b521f6b5e1775c7498f797e04a92dcc53960416e98c6602b4e1debd8d11f`.

The latter equals the `verification.solution_sha256` in the saved registry JSON.

### 2. Import/text navigation inventory

Starting from `Solution`, traversal of local textual imports identified **448 local modules**, **69,776 source lines**, and **3,538 regex-recognized declaration starts**. The `lean/` tree contains 460 Lean files and 71,726 lines. Files outside this tree, such as auxiliary verification inputs, are preserved in the full snapshot but are not part of these tree counts.

These counts describe a **text/import closure**, not the elaborated logical dependency closure of the two endpoint declarations. The declaration regex is not a Lean parser and may omit generated, anonymous or unusually formatted declarations. Historical inventory numbers in upstream documentation have different scopes and must not be equated with these checks.

### 3. Mathematical reconstruction and focused fidelity review

The following chains were reconstructed from pinned source statements and proof bodies, with explicit mathematical objects and prose:

- Actual zero regions, finite analytic order and local factorization; positive multiplicities; exact endpoint membership; conjugation.
- Independent Type I complete-pair comparison, product/divisor grouping, fixed Poisson band, full Mellin line, compact IBP parameter family, finite-valued supremum, scalar absorption and integer-length optimization.
- Actual Weyl producer: finite differencing/B-process, monotone-weight transfer, literal sharp AFE, Gamma-Laplace Abel limits, both dual cutoff gaps and compact initial heights.
- Actual fourth-moment producer: entire pole-cleared numerator, rectangle identity, divisor L-series, Gamma/digamma shifts, finite-prefix/true-tail decomposition, proved discrete Hilbert and Dirichlet mean-square estimates.
- Literal exponential point mean: finite rectangle, moving double pole, small-line Gamma kernel, actual double convolution, horizontal edges, full-to-truncated mean, compact completion and finite overlap inequality.
- Actual Atkinson source: frozen weight, quadratic Gamma phase, physical Gaussian, smooth compact test, integer-lattice phase, modulus-one Voronoi and complete dual sums, Bessel Mellin convergence strip, Neumann ray expansion, both signed saddles, symmetric odd-term cancellation, Fresnel Abel value, correction/remainder/K0 bounds and finite stationary cutoff.
- Height-dependent prefix masks, exact minimum-prefix Gram entries, near and far gaps, separated reciprocal rows, physical budget normalization, local absorption and parity cluster occupancy.
- Full superlevel measure from a finite maximal separated cover; truncated layer cake; native fourth/high-low twelfth moment and exact compact-origin induction to `[0,3T]`.
- Exact Möbius detector, removed unit term, smooth partition/tail, beta-independent Taylor extraction, fixed bounded convolution family, same-ordinate detection, Jensen multiplicity restoration, short exponent accounting.
- Uniform damped Mellin transform, moving long-block residue, weighted critical mean, weighted twelfth power, whole-line tail `T^(-113)`, long saving, exact short/complement partition, compact slabs and both-sign final accumulation.

Focused review corrected only the **English exposition**, not the Lean sources:

1. The actual stationary carrier integral includes the original `x^(-1/2)` before the square-coordinate Jacobian cancels it.
2. `FiniteVariationBound` has a uniform norm bound and a separately bounded increment sum; its summation-by-parts consequence spends the factor two.
3. The root phase is `2*pi*(2A*log y-y^2+2by)`, with `A=T/(2*pi)`.
4. The cubic-phase residual has the source's `4T|z|^4/r^4` bound.
5. The Hilbert comparison scales the **conjugated first family**, retaining the source kernel orientation.
6. The zero-origin moment adapter is the actual inductive bound using `2 <= 2^r`, not a substituted geometric-series proof.
7. The fourth-moment source expression `min eta 1/20` means **min(eta,1)/20** by application precedence. It is not a source error and was not changed.
8. Hidden tab/form-feed escapes were removed from TeX mathematics; long displayed formulas were broken across valid lines.

The final prose treats constants and thresholds with the original quantifier ordering. It does not introduce epsilon=0, sigma=3/4, effective constants, or uniformity at limiting parameters.

### 4. Source correspondence resolution

The manuscript has **81 displayed source-correspondence groups**. The archived ledger resolves each named declaration to its file and starting line. The accompanying verifier reports:

- unresolved source correspondences: **0**;
- undefined LaTeX labels: **0**;
- duplicate LaTeX labels: **0**;
- unexpected control characters: **0**.

A declaration-name match is a navigation check, not a semantic certificate for the adjacent English proof. The mathematical review is separate and source-driven.

### 5. LaTeX compilation and PDF inspection

- Standalone TeX, no external bibliography file required.
- Successfully compiled with **Tectonic 0.17.0**.
- Latest reading PDF: **49 pages**.
- Latest compile log: **no TeX errors, unresolved references or overfull boxes**.
- All pages were inspected programmatically for text outside the designated page area; representative title, stationary-proof and ending pages were also rendered and visually checked.
- The stored `zeta-density-blueprint.log` is the latest successful compilation log.

The principal deliverable remains `.tex`; the PDF is an additional reading copy.

## Verification not performed

- **No fresh Lean compilation or kernel replay was performed here.** The current local Lean version differs from the registry's pinned version; no environment or user Lean project was modified to force a rebuild.
- The registry reports historical verification with permitted axioms `propext`, `Classical.choice`, `Quot.sound`, at its recorded source and workflow. Its historical URL is https://github.com/PalomarRegistry/PalomarSubmission/actions/runs/37722058778 . This is not a new run in this task.
- The English manuscript is **not machine-checked mathematics** and has not undergone independent human peer review. Source fidelity was reviewed, but compilation and file hashes do not prove the exposition correct.
- The blueprint explains substantial local analytic chains and the imported foundational interfaces. It does **not** claim a line-by-line prose translation of every local declaration or every transitive mathlib proof. Casts, finite bookkeeping and equivalent integral encodings are consolidated where they do not change substantive mathematics.
- Academic references in registry metadata are attribution/context. No claim is made that the full external Heath-Brown, Kerr or Tao–Trudgian–Yang papers were independently reread as part of this task.
- `Challenge.lean` contains intentional specification holes and is not imported by production `Solution`; they are not used to justify the manuscript.

## Reproduction

Run `python3 verify-archive.py`. The script rebuilds the navigation records from the unmodified source, compares all extracted source files to the archive, and checks labels/correspondences. Compile with `tectonic --keep-logs zeta-density-blueprint.tex` if Tectonic is available.

The accompanying SHA-256 manifest binds the final archive deliverables and source snapshot. The private-repository receipt records the uploaded revision and privacy check separately, after the upload succeeds.
