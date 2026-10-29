# analysis/scored/

The manual scoring spreadsheet comparing each method's raw output
(`analysis/raw/`) against the frozen reference inventory
(`data/reference_inventory/`), per category (FR-9).

Scoring here is deliberately manual, not scripted (NFR-6): a spreadsheet
with visible formulas is directly auditable, where a script's internal
logic is not. Scoring rules are written and frozen before any scoring
begins (NFR-2), and a second, independent scoring pass is run over the
same raw output to confirm the same per-category counts are reached
(scoring-reproducibility gate) before any figure is reported.

This folder is empty as of this check-in; scoring has not started.
