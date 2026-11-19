# AI_VALIDATION_LEDGER.md

Validation ledger for Assignment 10, written 5 November 2026. The instructor asked that important labels, screening decisions, classifications, citations or mappings proposed by AI tools be independently validated. This ledger lists each one: what the AI proposed, who checked it, how, and where it stands. "Independent" here means checked by someone or something other than the AI that proposed it, using the source and not the AI's own summary.

Status words: **Validated** (checked against the source by me or by a separate process), **Partly validated**, **Not yet validated** (an AI proposed it and no independent check exists). Nothing here is validated by my supervisor.

## 1. The provisional reference list (nine MD5 entries in Md5Crypt.java)

- Proposed by: Claude, 21 October.
- Checked by: me, with my pass 1 (not independent: I had seen the list) and my pass 2 and agreed list (4 November), which came closer to independence.
- How: I read the numbered file and made my own list; the comparison is in `own_pass_vs_claude.md`.
- Status: **Partly validated.** The passes disagreed on 39 lines and I reconciled them with three rules. The 43 lines my agreed list adds are digest operations and zeroing. Dr. Shaalan has not confirmed the list. The list is not frozen (ISSUE-09).

## 2. The reading of the rule patterns (why the rule misses the variable form)

- Proposed by: Claude, 4 November, from the rule file.
- Checked by: the behavioural checks D and E (my own runs, P6) show the outcome (line 6 found, lines 10 to 12 not). I have not re-read the rule YAML myself.
- Status: **Partly validated.** The outcome is validated; the reading of the pattern is not. K4 stays provisional.

## 3. The shape of the control file

- Proposed by: Claude, which wrote `SameShapeControl.java`.
- Checked by: the file is 14 lines and I read it. It is synthetic and its sha256 is pinned. Claude and I both ran it.
- Status: **Partly validated.** I confirmed the two shapes match the lines they were meant to copy (Md5Crypt.java lines 259, 275, 312 and the rule's own test file); my run was not blind (L7).

## 4. The claims register and its mapping from claims to records

- Proposed by: Claude (all versions).
- Checked by: Claude compared each claim with the raw records by search before submitting; the fresh-agent audit (a separate AI process with low independence) re-checked the mapping on the audited commit and found defects, since fixed (`docs/CORRECTION_HISTORY.md`). I have not compared every line myself.
- Status: **Partly validated.** The check was made by AI processes, not by me.

## 5. The classification of the zero (coverage gap, two causes)

- Proposed by: Claude.
- Checked by: checks D, E and F show the observations (P6, P7). The classification is an interpretation.
- Status: **Partly validated.** Observations Validated; the classification is Not yet validated by anyone other than the AI that proposed it.

## 6. Citations

- Found or stated by: Claude, for the Literature and Requirements Brief and the Design Review Package.
- Checked by: Claude, on 14 November 2026, against publisher, repository or standards-body pages (`docs/CITATION_CHECK_2026-11-14.md`). That check found four statements in my earlier work that could not be confirmed (they are not used in the thesis draft) and corrected one author list. Nobody independent of the AI has checked them. I have not opened Amann et al. 2019, Ami et al., arXiv:2608.04857, arXiv:2503.19531 or Cronbach and Meehl 1955.
- Status: **Partly validated** (AI check against source pages only). My next step is to open each † item and record whether it says what the text says.

## 7. Issue numbers and cross-references

- Proposed by: Claude when drafting the logs.
- Checked by: a fresh-agent audit and my read. Earlier errors in Hard Stop 3 (false statements in the AI log, inconsistent issue numbering) were corrected and are listed in `docs/CORRECTION_HISTORY.md`.
- Status: **Validated for the audited commit** by search; re-run when files change.

## 8. The hashes and the line numbers

- Hashes: computed by Claude in the container and by me with `shasum -a 256` on the MacBook; they agree. Status: **Validated.**
- Line numbers in my pass entries: checked by Claude against the pinned file after the first draft of pass 2 was found to point at comments, imports and braces; the second draft was correct. Status: **Validated by an AI check against the file.**

## 9. The fresh-agent audit

- Performed by: a fresh AI agent that had not seen the work. Its report is `analysis/raw/audit_REVIEWER_freshagent_2026-11-04.md`, verbatim.
- Status: it is an AI checking AI-assisted work with a low independence level. It is not a replication by a person who is not me and it is not described as one.

## 9b. The fresh-environment re-run (14 November)

- Claude wrote the commands as paste-ready blocks from `docs/REPRODUCE.md`; I ran them in a fresh Docker container. Claude's first set of commands was faulty (two faults named in the record) and produced only error output; Claude corrected them and I ran the corrected set.
- Verification: I compared each result with the expected value in `docs/REPRODUCE.md`, and Claude compared the pasted output again line by line. All matched.
- Status: an author re-run, not an independent one (ISSUE-11 stays open). The file written by the `script` command is not yet in the record; the record uses the text I copied from the terminal.

## 9c. Assignment 12 work (19 November)

- Claude analysed the rule file, wrote and ran twelve K4 variants (run R4), grouped my 53 agreed lines into 10 operation-level items, built the CycloneDX 1.6 JSON, validated it with check-jsonschema, wrote the K4 analysis, the inventory freeze record, the independent source-pass package, the verification matrix and the response log entries H1 to H5.
- What I checked so far: I decided the unit (operation primary) and decided not to freeze the inventory before an independent source pass. I have not yet reviewed the item grouping, read the rule file, re-run the variants or read any cited paper. Those are listed as pending in `docs/RESPONSE_LOG.md` (H1, H2, H5) and `docs/VERIFICATION_MATRIX_2026-11-19.md`.
- Verification Claude did: it wrote the expected outcomes for the variants before running them and committed them first (`45f6180`); it ran a negative control for the schema validation; it checked that the 10 items cover exactly the 53 agreed lines.

## 10. What I will do next

I will re-read the rule YAML against lines 15 and 259 (item 2), open the cited papers (item 6) and ask for an independent human run of `docs/REPRODUCE.md`. These are planned, not done.
