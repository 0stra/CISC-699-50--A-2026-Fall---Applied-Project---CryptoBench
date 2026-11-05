# SOURCE_LEDGER.md

Source ledger for the Assignment 10 release candidate, written 5 November 2026 in answer to the instructor's request to confirm the source of every important result, figure, table, label and interpretation. For each item: where it comes from, who produced it, and whether I have checked it myself. "Checked by me" means I looked at the source and compared it; it does not mean supervisor approval, which none of this has.

Verification words used: **Recorded** (a raw record exists in `analysis/raw/`), **Checked by me** (I compared it with its source), **Not yet checked by me** (an AI produced or found it and I have not opened the source), **Unverified** (I could not trace it).

## 1. Results (the claims K1 to K9)

Each claim in `analysis/results/claims_register_2026-11-05.md` names its records and files. The route is claim, record label, raw file, command line and output inside the raw file.

- **K1, K5, K6 (repeatability, known negative).** Source: raw records of runs R1, R2 (Claude, container) and P3, P4 (my MacBook). Produced by: Claude for R1 and R2, me for P3 and P4. Status: Recorded; the MacBook runs were also done my myself.
- **K2 (ruleset returned HTTP 404).** Source: raw record P1. Status: Recorded; seen once, 18 October, and not re-requested.
- **K3 (rule fires on its own test file).** Source: R2 and P3. Status: Recorded; reproduced by me.
- **K7 (template round-trip).** Source: raw record TC2, my own three attempts. Status: Recorded.
- **K8 (shape gap).** Source: R3 (Claude, container) and P6 (my MacBook). Status: Recorded; my run was not blind to the expected result.
- **K9 (other three rules).** Source: P7 (my MacBook, one run each). Claude's earlier container run of the same commands was not saved. Status: Recorded, single run.
- **K4 (interpretation: two causes of the zero).** Source: K8 and K9, plus a reading of the rule patterns made by Claude. Status: Not yet checked by me for the rule-pattern reading. The claim stays provisional until I re-read the rule file against lines 15 and 259.

## 2. Figures

- **Figure 1 (`figure_1_proof_map.png`, claims to records).** Drawn by Claude on 29 October with matplotlib from the content of claims register version 1. The script (`figs.py`) lived in Claude's workspace and is not in this repository, so the figure cannot be regenerated from the repository. It shows no new data; its content is the claims register. Status: Not yet checked by me line by line.
- **Figure 2 (`figure_2_zero_classification.png`, how a zero is classified).** Same source, same limit. It is a diagram of a decision rule, not a measurement.
- **Figure 3 (`figure_3_rule_results_2026-11-05.png`, findings per rule).** Drawn by Claude on 5 November. Source of every number: counts in the raw records P6 and P7 (1, 3, 3 and 1 findings on the rules' own test files; 0 on Md5Crypt.java for all four). The generating script is stored as `analysis/results/figure_3_source.py` so the figure can be regenerated. Status: Recorded numbers; I have compared the four counts with the raw files.

None of the figures is evidence in itself. Each repeats what a raw record says.

## 3. Tables

The package contains no tables of results. The reference-list tables and the inventory template are lists of entries, covered in section 4.

## 4. Labels (inventory entries, line lists)

- **Provisional reference list (nine entries, `md5crypt_pilot_reference_list_2026-10-21.md`).** Produced by Claude on 21 October. Not independent. Status: used only as an illustration; never as an answer key.
- **My pass 1, pass 2 and the agreed list of 53 lines.** Produced by me. Pass 1 followed the list Claude had drafted. Pass 2 was written after reading the numbered file, with the help described in `own_pass_agreed.md`. The agreed list is a reconciliation under three rules of passes that disagreed on 39 lines. Claude checked the line numbers in my entries against the pinned file. Status: Recorded; not frozen; not confirmed by my supervisor (ISSUE-09).
- **Comparison with the provisional list (`own_pass_vs_claude.md`).** Prepared by Claude from the two lists. Status: Not yet checked by me line by line.

## 5. Interpretations

- **A zero from the tool is a coverage gap, not safety.** Source: K8 and K9. This is an interpretation (K4). Status: provisional, as above.
- **The audit's finding that the package is reproducible.** Source: `analysis/raw/audit_REVIEWER_freshagent_2026-11-04.md`, a report by a fresh AI agent with low independence, and my own run P6. Status: Recorded; this is not a replication by a person other than me.

## 6. Citations

The references below come from my Literature and Requirements Brief (`research/03`) and Design Review Package (`research/04`), which Claude helped find and write.

- Amann et al. 2019, IEEE Transactions on Software Engineering 45(12), doi 10.1109/TSE.2018.2827384. Status: Not yet checked by me; I have not opened the paper.
- Ami et al. 2026, ACM Transactions on Privacy and Security, doi 10.1145/3796221, "Mutation-based Evaluation of Cryptographic API Misuse Detectors". Status: Not yet checked by me; the venue and year are still to be confirmed against the paper.
- arXiv:2608.04857 and arXiv:2503.19531 (Cryptoscope). Status: Not yet checked by me.
- Cronbach and Meehl 1955 (construct validity). Status: Unverified.
- Pilot-study references (Lancaster 2004, Thabane 2010, Eldridge 2016). Status: Not rechecked in this audit.

No citation in this package should be treated as verified until I have opened it and confirmed that it says what the text says it says.

## 7. Where a source could not be fully traced

- Figures 1 and 2: script not stored (section 2).
- K9: Claude's first container run was not saved.
- The attempts that did not run to a result on 4 November are not reproduced in the P6 and P7 records; they are in git history (`docs/CORRECTION_HISTORY.md`).
