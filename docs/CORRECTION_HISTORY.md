# CORRECTION_HISTORY.md

Correction history for the Assignment 10 release candidate, written 5 November 2026 in answer to the instructor's request to preserve source records, correction histories, logs and repository materials. Every earlier version is in git (`git log`, `git show <commit>:<path>`). Raw run records are not edited after they are written, so this file is the pointer to what changed and where the earlier text lives.

## Corrections, in date order

- **Hard Stop 3 (22 to 31 October).** The AI log in the submitted document contained statements that were not true, and issue numbers were inconsistent between documents. Both were corrected in the revised documents and in `docs/ISSUE_LOG.md` (revised 31 October). The earlier text is the version already submitted; it was not rewritten in place.
- **31 October.** AI attribution lines in three repository files were removed by me and restored with a note (commit `aeec71d` restored them in the release candidate).
- **4 November, `aeec71d`.** Assignment 10 release candidate (a10-rc1) as audited by a fresh AI agent.
- **4 November, `0c6e0de` and `1a368b9`.** Defects found by that audit were fixed: wording in the audit record, a missing check E, and the tag-status wording. The audit report is stored verbatim in `analysis/raw/audit_REVIEWER_freshagent_2026-11-04.md`.
- **4 November, `baa4134`.** My own checks D and E (P6) added. Tag `a10-rc2` is on this commit. The wording about Semgrep 1.99.0 output (it prints no "Findings:" line) was corrected in `docs/REPRODUCE.md`.
- **4 November, `8de7ca6`.** Check F (P7) and claim K9 added; K4 narrowed from one cause to two. The earlier one-cause wording is at `baa4134`.
- **4 November, `81e88b0`.** Tag `a10-rc3` is on this commit. Typing slips and attempts that did not run to a result were trimmed from the P6 and P7 records. The untrimmed P6 text is at `baa4134` and the untrimmed P7 text at `8de7ca6`. The results in both records are unchanged.
- **4 November, `bac1a81`.** `research/03` and `research/04` added as submitted.
- **4 November, `f30b31c` and `c7adad0`.** Pass 2 and the agreed list added; ISSUE-09 narrowed (not closed). Three sentences in the memo that credited Claude's work to me were corrected before submission.
- **5 November.** Source ledger, AI validation ledger, this file, claims register version 3 (statuses added; stale text in L2 corrected), figure 3 and the README status section added. No claim wording changed. The commit for this change is named in the memo and in `docs/AUDIT_RECORD_A10.md`.

- **5 November, 18:33 to 19:01 (commits `3722947` to `fa8cb22`).** Nine files were edited in the GitHub web editor after the tag `a10-rc6` (README, claims register v3, audit record, correction history, issue log, reproduction steps, response log, source ledger, AI validation ledger). The edits removed or reworded statements that the provisional reference list, the control file, the claims registers, the figures and drafts of the documents were written by Claude; removed the note that Claude Code typed the P1 command; changed ISSUE-09 to read "closed"; removed several lines saying I had not checked every line; dropped the status section from the README; and pointed the README at the old register and a tag (`a10-rc5`) that does not exist. The same files in the tag were accurate: ISSUE-09 is not closed (the freeze rule is not met and the supervisor has not confirmed the list), and the AI authorship statements are true.
- **14 November.** The nine files were restored to their text at `a10-rc6` so that the record states who wrote what and what is open. The edited versions remain in history at the commits above. Why this matters: the record is the evidence behind every claim in the thesis, and the Assignment 10 feedback praised its candour. `docs/TAG_AND_MANIFEST.md` records the check and the rule for later edits.
- **14 November.** Citation check added (`docs/CITATION_CHECK_2026-11-14.md`); source ledger section 6 and AI validation ledger item 6 updated to say who checked what. The older figures 1 and 2 (`figure_1_proof_map.png`, `figure_2_zero_classification.png`, 29 October) are kept unchanged but are superseded by figures 4 to 6 (14 November), which show claims K8 and K9, the check F results and the claim statuses. Their source is `analysis/results/figures_thesis_source.py`.

- **14 November, evening.** Fresh-environment re-run added (`analysis/raw/semgrep_checks_A_to_F_PERSONAL_FRESHENV_2026-11-14.txt`). Its first attempt at checks A to F failed because the paste-ready commands Claude wrote were faulty (a missing line break merged two blocks, and a bash-only substitution was run in sh). The failed output is kept in the file and is stated as invalid; the second attempt, with corrected commands, is the result. No claim changed.

## Known open items

- `own_pass_2.md` has no "Help received:" line and its "Consulted" line says "nothing". `own_pass_agreed.md` records that Claude printed the numbered file for me, flagged wrong line numbers in my first draft of pass 2, and showed me disputed lines. I have not edited my pass 2 header. The header and the agreed-list note disagree; the agreed-list note is the accurate one. I will correct the header and record the correction here.
- The Assignment 11 record tag `a11-draft1` is created by me after the commit named in the cover note.
