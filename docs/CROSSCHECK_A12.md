# Cross-check of claims, numbers, figures and identifiers, Assignment 12

Date: 19 November 2026. Compared: the Assignment 12 thesis (near-final draft), the research deck (11 slides) and the evidence in this repository. The check was done by Claude, by searching the thesis source, the deck files and the raw records for each item below, and by reading the raw outputs. I have not yet repeated it. No table is used; each item says what was compared and the result.

## How evidence is identified

Appendix A of the thesis gives every evidence file a stable identifier, EV-01 to EV-51. The deck and the response note use the same identifiers. An identifier names a file path in this repository, and the path does not change between versions. A file that changes content keeps its identifier and gets a new commit hash. The file list is fixed at the Assignment 12 record commit given in the thesis.

## Numbers and facts

- **Counts on Md5Crypt.java.** Check A: 1 finding, line 15. Checks B and C: 0 findings. Check D: 1 finding, line 6. Check E: 0 findings on two files. Check F: `use-of-md5` 3 (lines 7, 15, 29), `weak-random` 3 (lines 48, 51, 165), `md5-used-as-password` 1 (line 41), 0 on Md5Crypt.java; `getInstance` count 0. Thesis §4.1 and §4.3, deck slide 5, raw records EV-09 to EV-15. Matches.
- **MD5 calls at lines 259, 275, 312** of Md5Crypt.java and the unprefixed call at line 469 of DigestUtils.java. Thesis §4.3, deck slide 6, K4 analysis EV-18. Matches.
- **Twelve variants.** Expected: V00 match; V01 to V04 no match; V05 match; V06 no match; V07, V08 match; V09, V10 no match; V11 match. Observed in the raw output (Semgrep 1.186.0): 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1 findings. 12 of 12 agree. The expected file was committed in `45f6180` before the run. Thesis §4.3, Figure 4, deck slide 6, EV-17, EV-19. Matches. V07 reports line 7 (the `.getMd5Digest()` line), as the thesis says.
- **Inventory.** The candidate has 10 items (checked by loading the JSON) covering the 53 agreed lines; SHA-256 `fa216520553f393ec294727c11e1e33a03e03a792a463f96be943b05a096f9cc` was recomputed and equals the value in `docs/INVENTORY_FREEZE_RECORD.md`. The two earlier passes marked 60 and 73 lines and disagreed on 39 lines (13 only in pass 1, 26 only in pass 2). Thesis §3.3 and §4.4, deck slide 7. Matches.
- **Pinned inputs.** semgrep-rules commit 17e31e11…, commons-codec commit f13dd50f…, Md5Crypt.java 361 lines with SHA-256 fa779456…, StringUtils.java 425 lines. Thesis §3.4, deck slide 4, `docs/ENVIRONMENT.md`. Matches.
- **Semgrep versions.** 1.99.0 (laptop), 1.181.0 (cloud container), 1.185.0 (my fresh container, 14 November), 1.186.0 (variants, 19 November). Thesis §3.4, deck slide 5. Matches.
- **Literature numbers** (Crypsy F1 0.75, 0.86, 0.95; Cryptoscope 92% and 11 of 15). Thesis §2.3 and §2.4, deck slide 3. These match what Claude recorded in `docs/CITATION_CHECK_2026-11-14.md`. I have not read the papers, so this is consistency only, not verification (marks † and ‡).

## Added after Gaurav’s run (19 November evening)

- His output (EV-48) was compared with the expected values in `docs/REPRODUCE.md`: rules commit, seven hashes, counts for checks A to F and `getInstance` 0. All agree, and the thesis (§3.6, §4.1), the note, the outline and the deck state the same count (33 of 33 matched). His run is described the same way everywhere: one person other than me, helper script, statements unverified.
- His source-pass list (EV-49) is cited as received, compared in draft by operation (EV-51), not reviewed by me. No document says the inventory is frozen or independent.
- Figure 1 (gate status) was redrawn: the independent re-run row now reads “DONE, ONE PERSON”.

## Claims and status

- K4 is "provisional, strengthened" in the claims register version 4, in the thesis (abstract, §4.3, §4.6, §5.2) and on deck slide 6. None says it is established.
- The third conclusion (an inventory item was not reported) is described as not established in the register, the thesis and the deck.
- The deck does not say more than the thesis: it does not claim a tool comparison, a result about post-quantum readiness, independent reproducibility or a frozen inventory. The deck names the feasibility framing as subject to Dr. Shaalan’s agreement, as the thesis does.
- No statement in the thesis, deck or note says that my supervisor approved anything.

## Figures

- Thesis Figure 1 = `figure_7_gate_status_2026-11-19.png` (not used in the deck).
- Thesis Figure 2 = `figure_9_zero_classification_2026-11-19.png`.
- Thesis Figure 3 = `figure_3_rule_results_2026-11-05.png` (unchanged from the 5 November version).
- Thesis Figure 4 = `figure_10_k4_variants_2026-11-19.png` (also on deck slide 6).
- Thesis Figure 5 = `figure_8_claim_record_map_2026-11-19.png`.
- Figures 1, 2, 4 and 5 were drawn by one script (`analysis/results/figures_a12_source.py`); each was checked by eye by Claude for overlap and for the labels “AI” (run by Claude) and “CANDIDATE, NOT FROZEN”. I have not checked them.

## New files added to the evidence index after this check was drafted

- EV-43 `figure_10_k4_variants_2026-11-19.png`, EV-44 `docs/CROSSCHECK_A12.md`, EV-45 `docs/RESPONSE_NOTE_A12.md`, EV-46 the walkthrough script, EV-47 the speaking outline. Deck slide 6 uses the image of EV-43 by upload.

## Quotations

The thesis quotes one phrase (“suffer from extremely low precision and recall”, Amann et al., 2019). It was checked by Claude against the abstract page. I have not read the paper. The earlier quotation “collapse dramatically” is not used.

## Open differences found

- The Appendix A heading in the Assignment 11 thesis had no identifiers; now fixed.
- The Assignment 11 figures 4 to 6 are replaced by figures 7 to 9; the old files remain in the repository unchanged.
- Nothing else differs. Items not checkable by search (the independent run, the source pass, my reading of the papers) are not done and are listed as open in the response note.
