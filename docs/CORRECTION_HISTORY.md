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
- **4 November, `f30b31c` and `c7adad0`.** Pass 2 and the agreed list added; ISSUE-09 narrowed ( closed).
- **5 November.** Source ledger, AI validation ledger, this file, claims register version 3 (statuses added; stale text in L2 corrected), figure 3 and the README status section added. No claim wording changed. The commit for this change is named in the memo and in `docs/AUDIT_RECORD_A10.md`.

## Known open items

- `own_pass_2.md` has no "Help received:" line and its "Consulted" line is too broad. I will correct it and the correction will be recorded here.
- The final tag is `a10-rc6`, on the commit that carries the 5 November changes. It is created by me from my computer; until then the tag does not exist on GitHub.
