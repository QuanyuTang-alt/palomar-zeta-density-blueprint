# Zeta zero-density proof: source-faithful English blueprint

An English mathematical reconstruction of Palomar entry **PALOMAR-2026-10-09-000005, version 1**, prepared for studying the formal proof and developing a future academic paper.

## Start here

- **`zeta-density-blueprint.tex`** — the principal deliverable: standalone LaTeX, definitions, full main statements and proofs, explicit parameter budgets, source correspondences and analytic-adapter appendices.
- **`zeta-density-blueprint.pdf`** — compiled reading copy, 49 pages.
- **`AUDIT.md`** — exact verification scope, fidelity checks and limitations.
- **`source-ledger.md`** — full paths and declaration starting lines for each displayed source correspondence, plus the local import inventory.
- **`source-reference-audit.json`** and **`source-import-inventory.json`** — machine-readable navigation and integrity records.
- **`verify-archive.py`** — reproducible source integrity and text/reference checks. This is an auxiliary audit utility, not part of the mathematical proof.

## Paper-style study version

The independent `paper-version/` folder contains the revised English learning note, compiled PDF, revision notes, proposition-by-proposition review, bibliography verification and reproducible editorial checks. The original blueprint and pinned source remain unchanged. This is a study of others' results, not a new research submission.

## Immutable mathematical source

Registry permalink:
https://palomar-registry.org/entry?id=PALOMAR-2026-10-09-000005&version=1

Registry record:
https://data.palomar-registry.org/entries/PALOMAR-2026-10-09-000005-v1.json

Upstream:
https://github.com/mrklwk/zeta-density-three-over-two-sigma-lean

Pinned commit: `804bdb55b1fc40e6a1a6878fd96078644a70e288`.

The exact downloaded archive is `registered-source.tar.gz`. Its complete extracted copy is the directory `zeta-density-three-over-two-sigma-lean-804bdb55b1fc40e6a1a6878fd96078644a70e288/`. All 560 regular source-archive files have been checked byte-for-byte against the archive. No original Lean file was edited.

## Mathematical content

The density endpoint counts all actual Riemann-zeta zeros with Re(rho) >= sigma and |Im(rho)| <= T, with positive finite analytic multiplicity. For every sigma > 3/4 and epsilon > 0, its bound is a constant times T raised to `3(1-sigma)/(2sigma)+epsilon`, for all real T >= 2. The companion actual twelfth moment is a constant times `T^(2+epsilon)` on `[0,3T]`, eventually in T.

The blueprint includes the independent Type I large-values argument; actual Weyl growth; the entire squared-zeta fourth-moment contour; point-to-local-mean production; the phase-corrected compact Voronoi source; both stationary signs and Fresnel factors; maximal-prefix Gram budgets; finite cluster occupancy; the high/low twelfth-moment assembly; exact smooth zero detection; a real-part-independent finite Taylor/convolution family; multiplicity-restoring Jensen sampling; the long weighted-mean reduction and physical tail; compact initial ranges and both ordinate signs.

## Reproduce the document checks

Run `python3 verify-archive.py` from this directory (or pass its absolute path). It checks the source archive and registry endpoint hash, rebuilds the source ledger and inventories, and tests that all displayed source correspondences and LaTeX cross-reference labels resolve. It does **not** elaborate Lean, verify kernel axioms or prove the English manuscript.

The TeX file is self-contained and uses standard LaTeX packages. It was compiled with Tectonic 0.17.0. With Tectonic installed, run `tectonic --keep-logs zeta-density-blueprint.tex`. Conventional LaTeX engines with the listed packages may also be used; their compilation has not been tested here.

The original Lean project is under the extracted snapshot's `lean/` directory and uses `leanprover/lean4:v4.35.0-rc2` and mathlib revision `065356127b1dc0016f66b7283ce0ce2c4055aa55`. Consult the preserved upstream build instructions and verification receipts if you wish to perform a new Lean replay. No new Lean kernel replay is claimed in this archive.

## Attribution and license

Mathematical development is attributed to **Mark Lewko** and the contributors credited upstream. This reconstruction is AI-assisted exposition, not a claim of a new proof or independent human peer review. Original upstream contributions retain **AGPL-3.0-only**; third-party material retains its MIT, MIT-0, Apache-2.0 and other notices. The upstream `LICENSE`, `NOTICE`, `CREDITS.md`, `PROVENANCE.md`, `LICENSE_STATUS.md` and all `third_party/` notices are preserved in the source snapshot. The blueprint and archive-specific explanatory material are provided under AGPL-3.0-only; this does not relicense any third-party material.

The GitHub repository was initially created as a private archive and subsequently made **public at the user's explicit request**. The original private-upload receipt records that earlier state; it is not a claim about current visibility. This repository is an explanatory archive, not an upstream modification or a claim of original research.
