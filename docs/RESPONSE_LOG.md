# RESPONSE_LOG.md

Response log for the feedback on Assignment 09 (professor feedback, received before 4 November 2026). Each item: what was asked, the change made, where it is, and what is still unresolved. Updated 4 November 2026 (Assignment 10) and 14 November 2026 (Assignment 11: feedback on Assignment 10 added at the end).

## F1. "Independently check the inventory"

- **Change made.** I did a second pass over `Md5Crypt.java` on 4 November (`own_pass_2.md`), compared it with my pass 1 (13 lines only in pass 1, 26 only in pass 2, 43 in both after dropping four brace lines), wrote an agreed list of 53 lines by applying three rules I chose (`own_pass_agreed.md`), and compared it with the provisional list (`own_pass_vs_claude.md`). Ten of the provisional list's 11 line numbers are in the agreed list; the agreed list adds 43 lines.
- **Location.** `data/reference_inventory/own_pass/`; ISSUE-09 in `docs/ISSUE_LOG.md`.
- **Unresolved.** Pass 1 was not independent of the provisional list; pass 2 followed my reading of the numbered file with help described in `own_pass_agreed.md`; the agreed list is a rule-based reconciliation, not full agreement of two independent passes. ISSUE-09 is narrowed, not closed. Dr. Shaalan has not been asked to confirm the list. No recall figure may be computed from it.

## F2. "Create a same-shape control"

- **Change made.** Added a 14-line control with the same MD5 call in the chained and variable forms, and ran the unmodified official rule on it. Result: the rule finds the chained form (line 6) only.
- **Location.** `data/test_material/same_shape_control/`; `analysis/raw/semgrep_samshape_control_REFERENCE_2026-11-04.txt`; claim K8 and updated K4 in `analysis/results/claims_register_2026-11-04.md`; ISSUE-08 in `docs/ISSUE_LOG.md`; check D in `docs/REPRODUCE.md`.
- **Unresolved.** The control was written by Claude and first run by Claude in the container. I repeated checks D and E on my MacBook (P6, `analysis/raw/semgrep_checks_D_E_PERSONAL_2026-11-04.txt`) with the same results; that run was not blind. The other three rules were checked one at a time on 4 November (P7, `analysis/raw/semgrep_per_rule_PERSONAL_2026-11-04.txt`): they have no matching call in `Md5Crypt.java`, a different cause from the shape gap. That run was once per rule.

## F3. "Attach stable claim records"

- **Change made.** Claims register version 2 with a stable evidence version (git tag), records, files, limits and "not claimed" lines for K1 to K8. Release manifest with SHA-256 for every file.
- **Location.** `analysis/results/claims_register_2026-11-05.md` (version 3; version 2 kept); `docs/RELEASE_MANIFEST.md`.
- **Unresolved.** The register was written by Claude from the records; I have not yet checked every line against the raw files myself.

## F4. "Run the frozen procedure on the planned sample for Assignment 11"

- **Change made.** None yet. This is the Assignment 11 task.
- **Location.** Not applicable.
- **Unresolved.** The procedure cannot be called frozen while the reference inventory is not frozen (ISSUE-09) and no sample is selected. Fallback Rule 1 (continue with Semgrep and the TLS scanner) is in force; Rule 3 applies if fewer than 15 samples can be selected.

## Audit findings of 4 November 2026 (Assignment 10)

- **Tag did not exist.** Change: docs name the commit hash; I create the tag `a10-rc2`. Location: `docs/AUDIT_RECORD_A10.md` section 4. Unresolved until I push the tag.
- **K8 part not reproducible.** Change: check E added. Location: `docs/REPRODUCE.md` section 3. Unresolved: the re-test was by the author only.
- **Vague wording.** Change: placeholders, working folder, output wording and reviewer file delivery clarified. Location: `docs/REPRODUCE.md`. Unresolved: none known.
- **AI attribution removed from three files on 31 October.** Change: restored. Location: `data/reference_inventory/own_pass/own_pass_1.md`, `docs/PROCEDURE_NOTES.md`, `journal/2026-10-31.md`. Unresolved: none.
- **Check D wording on Semgrep 1.99.0.** My P6 run showed that 1.99.0 prints no `Findings: N` line. Change: expected outputs now rely on the `Ran ...` line. Location: `docs/REPRODUCE.md`. Unresolved: none.

## Feedback on Assignment 10 (received after the 8 November submission; answered 14 November 2026, Assignment 11)

The feedback said the release makes a limited procedural finding examinable and praised the candid treatment of the unfrozen inventory and provisional interpretations. It asked, before Assignment 11, for: (1) a genuine independent human run; (2) a frozen reference inventory; (3) validation of the remaining citations; (4) a stable final tag and manifest relationship. It added that these actions prepare the evidence base and do not imply thesis completion.

## G1. "Obtain a genuine independent human run"

- **Change made.** None yet. No person other than me has run `docs/REPRODUCE.md`; no one was available between 5 and 14 November. I prepared the request text and the record template in `docs/INDEPENDENT_RUN_PACKAGE.md`.
- **Location.** `docs/INDEPENDENT_RUN_PACKAGE.md`; the gate is shown as NOT DONE in Figure 1 of the thesis draft.
- **Added later on 14 November.** Because no one was available, I repeated checks A to F myself in a fresh Ubuntu 24.04 Docker container on my MacBook (Semgrep 1.185.0, a third version). Every result matched `docs/REPRODUCE.md`. This is a fresh-environment author re-run, not an independent run: I am the author and Claude wrote the commands. The first attempt failed because Claude's commands were faulty and is kept in the record. Evidence: `analysis/raw/semgrep_checks_A_to_F_PERSONAL_FRESHENV_2026-11-14.txt`.
- **Unresolved.** The independent run itself. The reviewer runs on record are a fresh AI agent (low independence), my own checks (P6, P7) and now the fresh-environment re-run (P8). None is a run by another person. Planned: ask a classmate or Dr. Shaalan's nominee; record the output unedited as a `REVIEWER` file.

## G2. "Freeze the reference inventory"

- **Change made.** None, by my decision on 14 November: the freeze rule (two independent passes agree) is not met, and Dr. Shaalan has not confirmed the reconciled list of 53 lines. Freezing it anyway would have meant a deviation from my own rule without his agreement, so every inventory-related result stays provisional. The thesis draft states this in sections 3.3, 4.4 and 6.
- **Location.** `docs/ISSUE_LOG.md` (ISSUE-09, narrowed, not closed); `data/reference_inventory/own_pass/`.
- **Unresolved.** The freeze. Planned: ask Dr. Shaalan to confirm the reconciled list or to say what a further independent pass must look like; if he cannot reply in time, record a deviation with the list's hash and its limits before any scoring.

## G3. "Validate the remaining citations"

- **Change made.** Claude checked each citation used in the thesis draft against the publisher, repository or standards-body page on 14 November (`docs/CITATION_CHECK_2026-11-14.md`). Four statements in my earlier work could not be confirmed and are not used in the draft: the quoted "collapse dramatically" attributed to Amann et al., the "MUBench on fifteen detectors [Ami et al., 2024]" sentence, the HAWK withdrawal date, and the author line "withheld" for arXiv:2608.04857 (the authors are Näther and Hirsch). One author list was wrong (NIST IR 8610 begins with Alagic).
- **Location.** `docs/CITATION_CHECK_2026-11-14.md`; `docs/SOURCE_LEDGER.md` section 6; reference list of the thesis draft (marks † and ‡).
- **Unresolved.** I have not opened the papers myself, so no citation is validated by me. The year, authors and DOI of Ami et al. (TOPS) are unconfirmed. Planned: I open each † item and record one line per item in the citation check.

## G4. "Stabilize the final tag/manifest relationship"

- **Change made.** Rules for the relationship and a check of every manifest against its tag are in `docs/TAG_AND_MANIFEST.md`. At `a10-rc6` all 56 manifest entries match the files. The check found one problem: nine files had been edited in the web editor after the tag; they were restored to the tagged text on 14 November and the edited versions stay in history (`docs/CORRECTION_HISTORY.md`).
- **Location.** `docs/TAG_AND_MANIFEST.md`; `docs/CORRECTION_HISTORY.md`.
- **Unresolved.** The Assignment 11 record tag (`a11-draft1`) is created by me after the commit named in the cover note.

## G5. "Record substantive feedback and how it was answered" (instructor priority 7 for the Assignment 10 submission)

- **Change made.** This log is the record: F1 to F4 answer the Assignment 09 feedback; G1 to G4 answer the Assignment 10 feedback. The first set of Assignment 10 priorities (items 1 to 6) was answered by `docs/SOURCE_LEDGER.md`, `docs/AI_VALIDATION_LEDGER.md`, `docs/CORRECTION_HISTORY.md`, claims register v3, Figure 3 and the README status section.
- **Location.** This file.
- **Unresolved.** No supervisor feedback is on record for either set. Nothing here is supervisor-approved.

---

# Response to the Assignment 11 feedback (Assignment 12, 19 November 2026)

Dr. Shaalan's Assignment 11 feedback has five priorities, H1 to H5 below. Each entry gives the disposition (completed, reasoned disagreement, or pending with a specific action), the change made, where the evidence is, and what is unresolved. Nothing here is supervisor-approved; there is no reply from Dr. Shaalan on the inventory or the narrower framing.

## H1. "Establish a trustworthy reference inventory" (sections 3.3, 4.4, 5.5)

- **Disposition.** Partly completed; the freeze is pending with a specific action.
- **Change made.** (1) Unit of measurement decided on 19 November: the operation is the primary unit, lines are supporting evidence. (2) The 53 agreed lines were grouped into 10 items, each with asset type, algorithm or material, file, line locations and a one-sentence reason (`data/reference_inventory/reference_inventory_v1_candidate_2026-11-19.json`). Claude wrote the grouping; I have not yet reviewed it. (3) The file was validated against the CycloneDX 1.6 schema with check-jsonschema, with a negative control (`analysis/raw/cyclonedx_schema_validation_REFERENCE_2026-11-19.txt`). (4) The file was hashed (SHA-256 `fa216520553f393ec294727c11e1e33a03e03a792a463f96be943b05a096f9cc`) and recorded as a candidate, not frozen (`docs/INVENTORY_FREEZE_RECORD.md`). (5) A request and template for an independent source pass was written (`docs/INDEPENDENT_SOURCE_PASS_PACKAGE.md`).
- **Location.** `docs/INVENTORY_FREEZE_RECORD.md`; thesis sections 3.3, 4.4 and 5.5; ISSUE-09.
- **Unresolved.** No second person has inspected the source. I have not yet reviewed the item grouping. Dr. Shaalan has not confirmed the unit. The inventory is not frozen, and no recall or precision is calculated. Planned: I review the 10 items (by 21 November); the independent pass is requested from the person who agreed to run the reproduction steps; the freeze happens only after that, or the limitation stays in the thesis.

## H2. "Strengthen the interpretation of zero findings" (sections 4.3, 5.2)

- **Disposition.** Partly completed; my own reading and re-run are pending with a specific action.
- **Change made.** The pinned rule `use-of-md5-digest-utils.yaml` was analysed and its exact matching conditions written down (`docs/K4_RULE_ANALYSIS_2026-11-19.md`). Twelve synthetic variants that change one feature at a time were written with their expected outcomes committed first (`data/test_material/k4_variants/`, commit `45f6180`), then run once by Claude (Semgrep 1.186.0); all twelve matched the expectation, including the unprefixed call (V02, as at `DigestUtils.java` line 469) and a fully qualified receiver (V03). Claims register version 4 splits K4 into three conclusions (the scanner ran; a particular pattern did not match; the inventory holds an item that was not reported) and keeps K4 provisional (`analysis/results/claims_register_2026-11-19.md`). The thesis now separates the three conclusions.
- **Location.** `analysis/raw/semgrep_K4_variants_REFERENCE_2026-11-19.txt`; the register; thesis sections 4.3 and 5.2.
- **Unresolved.** I have not read the rule file myself and have not re-run the variants; both are my checklist in the K4 analysis. K4 moves to "survived with limits" only after that. The third conclusion depends on the unfrozen inventory.

## H3. "Demonstrate independent reproducibility" (sections 3.5, 3.6, 3.8)

- **Disposition.** Pending with a specific action.
- **Change made.** The feedback agrees the 14 November Docker run is repeatability, not independence; the thesis says the same. The original `session_transcript.txt` of that run is to be attached (I have it). A person has agreed to follow `docs/REPRODUCE.md` using `docs/INDEPENDENT_RUN_PACKAGE.md`.
- **Location.** `analysis/raw/semgrep_checks_A_to_F_PERSONAL_FRESHENV_2026-11-14.txt`; `docs/INDEPENDENT_RUN_PACKAGE.md`; thesis section 3.5, 3.6.
- **Unresolved.** The independent run has not been done. Planned: send the package by 20 November and ask for the output by 22 November; file it unedited as a `REVIEWER` record. If it does not arrive, the thesis says so.

## H4. "Align the findings with the thesis contribution" (sections 1.2, 4, 5, 7)

- **Disposition.** Completed for the framing; scoring is not possible and stays pending.
- **Change made.** The thesis question, contribution and conclusion now frame the completed work as a Semgrep feasibility study, as the feedback allows, subject to Dr. Shaalan's agreement. I did not manufacture results for Sonar or TLS. The thesis states how coverage, false positives and effort will be counted once an inventory is frozen (one declared unit; true positives, false positives and false negatives; undefined measures reported as "not estimable"; effort recorded by phase: setup, scanning, review, reconciliation), and that none is calculated now.
- **Location.** Thesis sections 1.2, 5, 7; deck slides on contribution and limits.
- **Unresolved.** Dr. Shaalan has not agreed to the narrower framing; I have asked for his view in the Week 12 worksheet and will ask again by email.

## H5. "Complete human verification of AI-supported material" (sections 2, 4.3, References, Appendix B)

- **Disposition.** Pending with a specific action.
- **Change made.** A matrix links each important literature claim to its source, the AI step, what the source page showed, and my verification action (`docs/VERIFICATION_MATRIX_2026-11-19.md`). Every source is still marked † or ‡; I have not read any of them.
- **Location.** `docs/VERIFICATION_MATRIX_2026-11-19.md`; `docs/CITATION_CHECK_2026-11-14.md`; thesis reference list.
- **Unresolved.** All reading. Planned: 21 November, starting with Näther and Hirsch, Ami et al. (year, authors and DOI of the TOPS paper) and Amann et al. Figure 4 and the register are updated when a claim changes.

## Update, 19 November 2026 evening: independent run and source pass received (H1, H3)

- **H3, independent reproducibility.** A person other than me (Gaurav Sharma) ran the checks A to F with the helper script (Semgrep 1.186.0, Ubuntu container). All results matched the expected values (33 matched, 0 differed). Record: `analysis/raw/semgrep_checks_A_to_F_REVIEWER_2026-11-19.txt`; notes and open points in `docs/INDEPENDENT_REVIEW_RECORD_2026-11-19.md`. Limits: a helper script was used, not the document by hand; the runner name was left as a placeholder; his statements about no AI use and no help are his, relayed to me, and unverified.
- **H1, inventory.** The same person wrote an independent list of operations (`data/reference_inventory/independent_pass_REVIEWER_2026-11-19.txt`). A draft comparison by operation is in `data/reference_inventory/independent_pass_comparison_2026-11-19.md`: most items agree; the helper’s list has wrapper-level salt and prefix operations that the candidate largely lacks. His line numbers do not match the pinned file. I have not reviewed the comparison. The inventory is still not frozen.
- **Not yet changed:** the thesis, deck and response note (they still say the independent run and pass are not done). They will be updated after I review the comparison.
