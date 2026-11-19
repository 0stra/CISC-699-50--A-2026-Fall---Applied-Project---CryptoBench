# Claims register, version 4 (19 November 2026, Assignment 12)

**What changed in version 4.** Version 3 (5 November 2026, `analysis/results/claims_register_2026-11-05.md`) is kept unchanged. Version 4 changes the status and records of K4 and K9 and the text of limits L2, L4, L5, L8 and L9 after four pieces of new evidence: the fresh-environment re-run P8 (14 November, Semgrep 1.185.0, `analysis/raw/semgrep_checks_A_to_F_PERSONAL_FRESHENV_2026-11-14.txt`); the K4 controlled variants R4 (19 November, run by Claude, Semgrep 1.186.0, `analysis/raw/semgrep_K4_variants_REFERENCE_2026-11-19.txt`, files in `data/test_material/k4_variants/`); the analysis of the rule file (`docs/K4_RULE_ANALYSIS_2026-11-19.md`); and the CycloneDX 1.6 schema validation of the candidate inventory (`analysis/raw/cyclonedx_schema_validation_REFERENCE_2026-11-19.txt`). No other claim wording changed. K4 is not upgraded to "survived", because I have not yet read the rule file myself or re-run the variants; the status line says what remains.

## (Version 3 text follows, with the changes named above)

---

Version 1 (29 October 2026, Assignment 09) and version 2 (4 November 2026) are kept unchanged at `analysis/results/claims_register_2026-10-29.md` and `analysis/results/claims_register_2026-11-04.md`. Version 3 changes no claim wording. It adds a **Status** line to every claim after an audit of the source of each claim (`docs/SOURCE_LEDGER.md`) and of what an AI proposed and who checked it (`docs/AI_VALIDATION_LEDGER.md`), and it corrects the stale text in L2.

**Rule for status.** A result stays provisional whenever its data source, its validation procedure or its supporting evidence is incomplete. A claim is carried forward as "survived with limits" only if it rests on a raw record that is in the repository, was reproduced at least once by me, and has its limit written next to it. "Survived" does not mean confirmed by my supervisor; she or he has confirmed nothing. Statuses: **survived with limits**, **provisional**. No claim is marked "confirmed".

**Stable evidence version.** The audited release candidate is commit `aeec71de620e5d8a000adbd79af4bd50ce929886` (called a10-rc1 in `docs/AUDIT_RECORD_A10.md`). Fixes made after the audit are in later commits; the final commit and its tag `a10-rc6` are named in `docs/AUDIT_RECORD_A10.md`. A file cannot contain its own commit hash, which is why the hashes are recorded in the audit record. A claim made later should cite the tag and the claim number, for example "K8 at a10-rc6". Raw records are not edited after they are written, so the file names below are stable. If a record changes, a new tag is made.

Written by Claude (AI assistant) from the existing records. K8 rests on a new run made by Claude in its container (R3); I did not run it. I repeated checks D and E myself on my MacBook on 4 November (record P6); I had the expected values in front of me.

Run labels: R = reference run by Claude in a cloud container (R3 = the 4 November control run). P6 = my 4 November checks D and E on my MacBook. P7 = my 4 November check F (the other three rules). P = run on my MacBook. P1 was typed by Claude Code at my request; P3 and P4 I typed and ran myself. TC2 = my three attempts at the template round-trip.

Figure files: `analysis/results/figure_1_proof_map.png` (claims to records), `analysis/results/figure_2_zero_classification.png` (how a zero is classified) and `analysis/results/figure_3_rule_results_2026-11-05.png` (findings per rule, own test file against Md5Crypt.java). Claude drew all three from the content of this register; they are not independent evidence (`docs/SOURCE_LEDGER.md`).

## K1 (O1) - Observation recorded

**Status (5 November 2026).** Survived with limits. Rests on four raw records (two of them my own runs); repeated twice on two machines. Limits L1, L6 stay attached.

**Claim.** The Semgrep procedure runs end to end on public inputs (a public Apache-licensed Java file, public rules).

**Records.** R1, 18 October, reference run by Claude in a cloud container (Semgrep 1.181.0), 24 rules, 0 findings, twice. R2, 21 October, reference run by Claude in the container, checks A and B. P3, 21 October, my own checks A and B on my MacBook, each twice. P4, 21 October, my own check C on my MacBook, twice.

**Files.** `analysis/raw/semgrep_TC1_Md5Crypt_2026-10-18.txt`, `analysis/raw/semgrep_pilot_official_rules_REFERENCE_2026-10-21.txt`, `analysis/raw/semgrep_pilot_official_rules_PERSONAL_2026-10-21.txt`, `analysis/raw/semgrep_TC5_known_negative_PERSONAL_2026-10-21.txt`

**Limits.** L1, L6.

**Not claimed.** Anything about the Sonar plugin, the TLS scanner or Java code in general.

## K2 (O1) - Observation recorded

**Status (5 November 2026).** Provisional. Observed once on 18 October (HTTP 404) and not re-requested since; the ruleset may have been available at other times.

**Claim.** The registry ruleset p/cryptography named in my project files returned HTTP 404 (exit code 7) and nothing was scanned (ISSUE-06).

**Records.** P1, 18 October, my laptop attempt typed by Claude Code, failed (HTTP 404).

**Files.** `analysis/raw/semgrep_TC1_mac_attempt_2026-10-18.txt`, `journal/2026-10-18-test-case-1-mac-attempt.md`

**Limits.** seen on 18 October only; not re-requested since.

**Not claimed.** That the ruleset can never be fetched.

## K3 (O2) - Observation recorded

**Status (5 November 2026).** Survived with limits. Raw records from both machines; reproduced by me (P3). Limit L2.

**Claim.** The official rule use-of-md5-digest-utils fires on its own test file: 1 finding at line 15, repeated, same on both machines.

**Records.** R2, 21 October, reference run by Claude in the container, checks A and B. P3, 21 October, my own checks A and B on my MacBook, each twice.

**Files.** `analysis/raw/semgrep_pilot_official_rules_REFERENCE_2026-10-21.txt`, `analysis/raw/semgrep_pilot_official_rules_PERSONAL_2026-10-21.txt`

**Limits.** L2.

**Not claimed.** That the rule fires on the variable form of the same call.

## K4 (O2) - Interpretation, supported for all four rules (revised in version 4)

**Status (19 November 2026).** Provisional, strengthened. The shape-gap cause for `use-of-md5-digest-utils` is now supported by the text of the rule (`docs/K4_RULE_ANALYSIS_2026-11-19.md`) and by twelve one-feature-at-a-time variants whose outcomes were written down before the run and all matched (R4, run by Claude). It stays provisional for three reasons: I have not yet read the rule file myself, I have not yet re-run the variants (planned, Docker, PERSONAL file), and the third conclusion below depends on an inventory that is not frozen. When I have read the rule and my own re-run matches, the status for conclusions 1 and 2 can move to "survived with limits".

**Claim, in three separate conclusions (as the Assignment 11 feedback asked).**
1. *The scanner ran.* Each of the four rules ran without error and fires on its own test file (check A, K3; check F, K9). Supported.
2. *A particular pattern did not match.* `use-of-md5-digest-utils` matches only a call named `getMd5Digest` on a receiver named `DigestUtils` with `.digest(...)` chained directly on it. `Md5Crypt.java` creates the digest and assigns it to a variable (lines 259, 275, 312), so the rule has nothing to match (check D, K8; variants V00 to V11). The other three rules target `MessageDigest.getInstance`, `Random` calls and password-hash patterns that the file does not contain (check F, K9). Supported by the rule text and by tests; waiting for my own reading and re-run.
3. *The reference inventory contains an item that was not reported.* In the candidate inventory v1 the three MD5 creation lines belong to items CB-INV-01 to CB-INV-03, and no Semgrep rule reported them. This is not established: the inventory is a candidate, not independent and not frozen (L3, `docs/INVENTORY_FREEZE_RECORD.md`). It is stated here as a consequence to be tested, not as a result.

**Records.** R2 and P3 (checks A and B, 21 October); R3 and P6 (checks D and E, 4 November); P7 (check F, 4 November); P8 (checks A to F, 14 November, fresh container, my run); R4 (variants V00 to V11, 19 November, Claude's run).

**Files.** `analysis/raw/semgrep_pilot_official_rules_REFERENCE_2026-10-21.txt`, `analysis/raw/semgrep_pilot_official_rules_PERSONAL_2026-10-21.txt`, `analysis/raw/semgrep_samshape_control_REFERENCE_2026-11-04.txt`, `analysis/raw/semgrep_checks_D_E_PERSONAL_2026-11-04.txt`, `analysis/raw/semgrep_per_rule_PERSONAL_2026-11-04.txt`, `analysis/raw/semgrep_checks_A_to_F_PERSONAL_FRESHENV_2026-11-14.txt`, `analysis/raw/semgrep_K4_variants_REFERENCE_2026-11-19.txt`, `data/test_material/k4_variants/`, `docs/K4_RULE_ANALYSIS_2026-11-19.md`, `data/reference_inventory/reference_inventory_v1_candidate_2026-11-19.json`

**Limits.** L2 (reduced), L3, L8, L9.

**Not claimed.** That any rule would miss other forms of these calls beyond the twelve variants; anything about Semgrep recall in general; that the file contains cryptography that no tool can find; the 0 of 3 is an illustration of the calculation.

## K5 (O2) - Observation recorded

**Status (5 November 2026).** Survived with limits. One raw record, my own run, twice. Limit L1.

**Claim.** The same four rules give 0 findings, twice, on StringUtils.java (425 lines, no cryptography): no false positive on that file.

**Records.** P4, 21 October, my own check C on my MacBook, twice.

**Files.** `analysis/raw/semgrep_TC5_known_negative_PERSONAL_2026-10-21.txt`

**Limits.** L1.

**Not claimed.** A false-positive rate.

## K6 (O3) - Observation recorded

**Status (5 November 2026).** Survived with limits. Raw records on both machines with an empty diff between repeats. Limit L4.

**Claim.** Checks A, B and C repeat on my MacBook (Semgrep 1.99.0) with the same findings as the container (Semgrep 1.181.0), each run twice with an empty diff between the two outputs.

**Records.** R2, 21 October, reference run by Claude in the container, checks A and B. P3, 21 October, my own checks A and B on my MacBook, each twice. P4, 21 October, my own check C on my MacBook, twice.

**Files.** `analysis/raw/semgrep_pilot_official_rules_REFERENCE_2026-10-21.txt`, `analysis/raw/semgrep_pilot_official_rules_PERSONAL_2026-10-21.txt`, `analysis/raw/semgrep_TC5_known_negative_PERSONAL_2026-10-21.txt`

**Limits.** L4.

**Not claimed.** Equivalence of the two Semgrep versions or machines.

## K7 (O4) - Observation recorded

**Status (5 November 2026).** Survived with limits. My own record of three attempts. Limit L5.

**Claim.** Adding one entry to a copy of the inventory template by hand needs three checks (parse, entry count, comparison with the original); attempt 1 failed to parse, attempt 2 saved nothing, attempt 3 passed.

**Records.** Test case 2, 21 October, my three attempts at the template round-trip.

**Files.** `analysis/raw/TC2_template_roundtrip_PERSONAL_2026-10-21.txt`

**Limits.** L5.

**Not claimed.** CycloneDX schema validity, or that the process scales to a full inventory.

## K8 (O2) - Observation recorded (new)

**Status (5 November 2026).** Survived with limits. Claude's run (R3) and my run (P6) agree. The control file was written by Claude and my run was not blind (L7). Single rule, two versions.

**Claim.** On a 14-line control with the same call in two shapes, the unmodified official rule use-of-md5-digest-utils finds the chained form (line 6) and does not find the variable form (lines 10 to 12), which is the shape Md5Crypt.java uses at lines 259, 275 and 312. The same rule also finds nothing in DigestUtils.java, DigestUtilsTest.java or Md5Crypt.java from the pinned commit.

**Records.** R3, 4 November, reference run by Claude in the container (Semgrep 1.181.0). P6, 4 November, my own checks D and E on my MacBook (Semgrep 1.99.0), each twice, identical: 1 finding at line 6, 0 findings on DigestUtils.java and DigestUtilsTest.java.

**Files.** `analysis/raw/semgrep_samshape_control_REFERENCE_2026-11-04.txt`, `analysis/raw/semgrep_checks_D_E_PERSONAL_2026-11-04.txt`, `data/test_material/same_shape_control/SameShapeControl.java`, `data/test_material/same_shape_control/README.md`

**Limits.** L1, L7, L8.

**Not claimed.** How common either shape is in real code; behaviour of any other rule; behaviour of other Semgrep versions.

## K9 (O2) - Observation recorded (new)

**Status (19 November 2026).** Survived with limits, one run in each of two environments. My run P7 (4 November, MacBook, Semgrep 1.99.0) and my fresh-container re-run P8 (14 November, Ubuntu, Semgrep 1.185.0) give the same counts and lines; Claude's earlier container run was not saved (L9). Both runs are mine and not blind, so this is repeatability, not independence.

**Claim.** Each of the other three official rules finds its expected findings on its own test file (use-of-md5: 3 at lines 7, 15, 29; weak-random: 3 at lines 48, 51, 165; md5-used-as-password: 1 at line 41) and finds 0 on Md5Crypt.java, which contains no getInstance call.

**Records.** P7, 4 November, my own run on my MacBook (Semgrep 1.99.0), one run each; P8, 14 November, my own run in a fresh Docker container (Semgrep 1.185.0), one run each, same counts and lines. Claude had run the same commands in its container (Semgrep 1.181.0) beforehand and got the same counts; that run was not saved as a record.

**Files.** `analysis/raw/semgrep_per_rule_PERSONAL_2026-11-04.txt`, `analysis/raw/semgrep_checks_A_to_F_PERSONAL_FRESHENV_2026-11-14.txt`

**Limits.** L9.

**Not claimed.** Behaviour of these rules on other forms of the calls; any statement about other Java files.

## Limits

**L1.** One file per tool, chosen by convenience (it uses MD5 and is public). Consequence: no claim about rates or about Java code in general.

**L2.** The Check A positive control has a different code shape from Md5Crypt.java (ISSUE-08). Check D adds a same-shape pair for one rule. Consequence: check D tests the explanation for one rule. The other three rules were each run on their own test file and on Md5Crypt.java in check F (K9), which shows they fire where expected and that the file has no matching call; no same-shape pair was built for them. Version 4: twelve variants were built for the one rule `use-of-md5-digest-utils` (R4); none for the other three.

**L3.** The provisional reference list was drafted by Claude. My pass 1 was not independent of it. My pass 2 and agreed list (53 lines, 4 November) exist but are reconciled by my own rules after the passes disagreed on 39 lines (ISSUE-09). Consequence: any recall figure from these lists is an illustration only, and the inventory is not frozen.

**L4.** Self-check by me on three Semgrep versions (1.99.0, 1.181.0 by Claude, 1.185.0 in a fresh container) and three environments; Claude's variant run used a fourth version (1.186.0). Consequence: repeatability of my execution, not independence and not equivalence of versions. No other person has run the steps (ISSUE-11).

**L5.** Version 4: the candidate inventory v1 was validated against the CycloneDX 1.6 schema with check-jsonschema 0.39.0, with a negative control that failed as it should (`analysis/raw/cyclonedx_schema_validation_REFERENCE_2026-11-19.txt`). The earlier template check covered JSON validity only. Consequence: the structure is valid; the items are not independently reviewed, and the version of the Sonar plugin's output schema is unconfirmed.

**L7.** The control file is synthetic (written by Claude). It was run by Claude (1.181.0) and by me (1.99.0, P6), one rule, two versions. Consequence: K8 holds for this one rule and these two versions only; my P6 run was not blind to the expected result.

**L8.** DigestUtils.java line 469 holds `getMd5Digest().digest(data)` without the `DigestUtils.` prefix and the rule does not match it. This is a second shape the rule misses; it was observed, not explored. Version 4: variant V02 reproduces it on a synthetic file (no match) and V03 shows a fully qualified receiver is also not matched. Consequence: the shape gap has at least three forms (variable, unprefixed call, fully qualified receiver); the rule needs `DigestUtils` as the receiver name.

**L9.** Check F ran once per rule and my run was not blind; Claude's earlier container run of the same commands was not saved. Version 4: my fresh-container re-run P8 is saved and gives the same results. Consequence: K9 is one run in each of two environments, both mine.

**L6.** The Sonar plugin and the TLS scanner have not been run. Consequence: nothing here is a three-way comparison.

## Pinned inputs

Md5Crypt.java: apache/commons-codec commit f13dd50f566c318283c4138820b15d75c26a0217, 361 lines, sha256 fa779456b25d2d36a6c464e200e106c2fa8e94a45dc608844ceb04407ea90747. StringUtils.java: same commit, 425 lines, sha256 6c44ebc7424c69fd04b6f3df10332934a149e6901fd29e86d96df4176527a99a. Rules: semgrep/semgrep-rules commit 17e31e11ebac99fb7dfe1cd288f7a32151b6f3f9. Rule fixture sha256 bd22fdb5ef195e383ec69aa9dbf1d0fd8f6cb5d41aef3f725f1aba5e5aa05908. Inventory template sha256 a851ef3d6547c6e75f728144f2e8b9575b0853f4e63a4f9b65c693ad89a2139d. Semgrep 1.181.0 (container, Ubuntu 24.04.5, Python 3.13.16); Semgrep 1.99.0 (MacBook, macOS 15.7.9, Python 3.8.2). Control file SameShapeControl.java sha256 657e8eb1ac803fecb27dcbe7808781c5fd315a4981c7f33424645d25ae7c8539. Rule yaml use-of-md5-digest-utils.yaml sha256 a0614baf029418dd9b298713c3328f371faa1edb0eac7cc2c4a3a99ce1a220a5 (computed in the container).
