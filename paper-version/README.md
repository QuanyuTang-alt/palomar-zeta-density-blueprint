# Paper-style study version

This folder contains an English learning note based on the pinned Lean development of Mark Lewko and the contributors credited upstream. It is an exposition of others' results, not an original research submission. There is no abstract, MSC classification or keywords.

## Reading files

- `zeta-density-study.tex` — complete standalone LaTeX source; the dependency diagram is native TikZ.
- `zeta-density-study.pdf` — compiled reading copy, 44 pages.
- `REVISION-NOTES.md` — Chinese explanation of the changes and their mathematical scope.
- `PROPOSITION-REVIEW.md` — review of all 25 original propositions and three definitions, with simplification decisions and limits.
- `BIBLIOGRAPHY-CHECK.md` — source-by-source bibliography and attribution checks.

## Suggested reading

Read Sections 1–7 first. They prove the zero-density theorem using the independent large-values estimate and the classical twelfth-moment theorem of Heath-Brown. Appendices A–F retain the detailed formal-development route through the moment and the associated analytic calculations. These are not discarded from the study archive merely because a citation shortens the main line.

The original 49-page blueprint and the fixed source snapshot remain in the parent directory without modification. Each of its 81 source-correspondence groups is preserved as a comment in the new TeX. `study-source-map.json` relocates those groups to the new manuscript; the original source ledger still resolves the declaration names and source lines.

## Reproduction and scope

Compile with `tectonic --keep-logs zeta-density-study.tex`. Standard LaTeX engines with the listed packages may also be used, but only the stated Tectonic build has been tested.

Run `python3 verify-study.py` to check source preservation, environment counts, label/citation coverage and PDF page boundaries. Its JSON output is `editorial-check.json`. This utility checks text and artifacts; it does **not** prove the English mathematics, certify bibliography support, or replay Lean. See `PROPOSITION-REVIEW.md` for the separate mathematical review.

The authoritative editable file is `zeta-density-study.tex`. The local first-draft generator is deliberately excluded from Git because it predates the manual mathematical and editorial corrections. Recompile the TeX; do not regenerate the final text from that prototype.

Attribution and licenses follow the parent archive: explanatory material under AGPL-3.0-only, with all original and third-party notices preserved. No new Lean kernel replay or independent human peer review is claimed.
