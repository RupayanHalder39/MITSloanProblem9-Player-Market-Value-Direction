# Public Release Audit

## Scope

This is a curated public package derived from the read-only master research project. The final publication source was `Problem9_Beyond Today’s Price_ Predicting the Direction of Football Player Market Values from Recent Performance.docx.pdf`. The master project's handoff, final evidence report, claim audit, frozen tables, figure traceability, final figure package, and validation outputs were consulted.

## Included

- Final paper, copied without modification.
- Four final research figures in PNG and PDF form.
- Aggregate Championship, cross-competition, shortlist, ablation, and bootstrap tables.
- Public validator and research documentation.
- Researcher photograph and SoccerSolver logo, copied from the established project assets.

## Deliberately excluded

- Raw and processed row-level data, SQL dumps, databases, model binaries, caches, and exploratory artifacts.
- Player-identifying breakout records and top-error tables.
- Internal reports, reviewer correspondence, obsolete manuscripts, and working notes.
- Standalone software screenshots; no separate redistribution authorization was found.

## Data and licensing decision

No evidence establishing public redistribution rights for the row-level source data was found. Data are therefore excluded and reproduction is classified as **partial**. The MIT License applies only to original repository software, not to the paper, data, images, logos, or third-party material.

## Scientific consistency

Verified against frozen source tables: 752 Championship valuation events / 606 players; M1/M5 MAE 0.3066/0.2957; direction accuracy 35.6%/46.7%; majority benchmark 42.3%; Spearman 0.278/0.296; 27/27 external direction wins; 8/27 external exact-value wins; 2,000 player-clustered bootstrap draws with supported MAE/direction but not Spearman difference; and 10 missed pre-declared extreme breakouts. No scientific result was recalculated or changed.

## Validation and safety

- `python3 scripts/verify_release.py`: PASS.
- Python compilation: PASS.
- README links: PASS through the release validator.
- `CITATION.cff` YAML parse: PASS.
- Final paper: confirmed as two-page A4 PDF.
- Secret and credential pattern scan: PASS (no matches).
- Restricted-format scan: PASS (no Parquet, SQL, database, serialized-model, or environment files).
- Portability scan: PASS (no public dependency on the private master path).
- Symlink scan: PASS (none present).
- Large-file scan: PASS (no file over 10 MB).
- Staged-path inspection: PASS; 29 curated release files only.

## Publication

- Repository: https://github.com/RupayanHalder39/MITSloanProblem9-Player-Market-Value-Direction
- Commit: initial public release commit (see repository history)
- Push: pending final network operation

## Remaining limitation

End-to-end model reconstruction requires authorized row-level valuation and match-performance data.
