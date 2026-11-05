# Claims register, version 2 (4 November 2026, Assignment 10)

Version 1 (29 October 2026, Assignment 09) is kept unchanged at `analysis/results/claims_register_2026-10-29.md`. This version adds claim K8, updates K4 and L2 after the same-shape control, and fixes each claim to a stable evidence version.

**Stable evidence version.** The audited release candidate is commit `aeec71de620e5d8a000adbd79af4bd50ce929886` (called a10-rc1 in `docs/AUDIT_RECORD_A10.md`). Fixes made after the audit are in later commits; the final commit and its tag `a10-rc3` are named in `docs/AUDIT_RECORD_A10.md`. A file cannot contain its own commit hash, which is why the hashes are recorded in the audit record. A claim made later should cite the tag and the claim number, for example "K8 at a10-rc3". Raw records are not edited after they are written, so the file names below are stable. If a record changes, a new tag is made.

Written by Claude (AI assistant) from the existing records. K8 rests on a new run made by Claude in its container (R3); I did not run it. I repeated checks D and E myself on my MacBook on 4 November (record P6); I had the expected values in front of me.

Run labels: R = reference run by Claude in a cloud container (R3 = the 4 November control run). P6 = my 4 November checks D and E on my MacBook. P7 = my 4 November check F (the other three rules). P = run on my MacBook. P1 was typed by Claude Code at my request; P3 and P4 I typed and ran myself. TC2 = my three attempts at the template round-trip.

Figure files: `analysis/results/figure_1_proof_map.png` (claims to records) and `analysis/results/figure_2_zero_classification.png` (how a zero is classified).

## K1 (O1) - Observation recorded

**Claim.** The Semgrep procedure runs end to end on public inputs (a public Apache-licensed Java file, public rules).

**Records.** R1, 18 October, reference run by Claude in a cloud container (Semgrep 1.181.0), 24 rules, 0 findings, twice. R2, 21 October, reference run by Claude in the container, checks A and B. P3, 21 October, my own checks A and B on my MacBook, each twice. P4, 21 October, my own check C on my MacBook, twice.

**Files.** `analysis/raw/semgrep_TC1_Md5Crypt_2026-10-18.txt`, `analysis/raw/semgrep_pilot_official_rules_REFERENCE_2026-10-21.txt`, `analysis/raw/semgrep_pilot_official_rules_PERSONAL_2026-10-21.txt`, `analysis/raw/semgrep_TC5_known_negative_PERSONAL_2026-10-21.txt`

**Limits.** L1, L6.

**Not claimed.** Anything about the Sonar plugin, the TLS scanner or Java code in general.

## K2 (O1) - Observation recorded

**Claim.** The registry ruleset p/cryptography named in my project files returned HTTP 404 (exit code 7) and nothing was scanned (ISSUE-06).

**Records.** P1, 18 October, my laptop attempt typed by Claude Code, failed (HTTP 404).

**Files.** `analysis/raw/semgrep_TC1_mac_attempt_2026-10-18.txt`, `journal/2026-10-18-test-case-1-mac-attempt.md`

**Limits.** seen on 18 October only; not re-requested since.

**Not claimed.** That the ruleset can never be fetched.

## K3 (O2) - Observation recorded

**Claim.** The official rule use-of-md5-digest-utils fires on its own test file: 1 finding at line 15, repeated, same on both machines.

**Records.** R2, 21 October, reference run by Claude in the container, checks A and B. P3, 21 October, my own checks A and B on my MacBook, each twice.

**Files.** `analysis/raw/semgrep_pilot_official_rules_REFERENCE_2026-10-21.txt`, `analysis/raw/semgrep_pilot_official_rules_PERSONAL_2026-10-21.txt`

**Limits.** L2.

**Not claimed.** That the rule fires on the variable form of the same call.

## K4 (O2) - Interpretation, supported for all four rules

**Claim.** The zero from four official rules on Md5Crypt.java (reference list: MD5 created at lines 259, 275, 312) is a coverage gap, not a broken tool, with two different causes. For use-of-md5-digest-utils the call is in the file in a form (stored in a variable) that the rule does not match (check D, K8). For the other three rules (use-of-md5, md5-used-as-password, weak-random) the file has no call they target (no getInstance; Random only as a type), and each rule fires on its own test file (check F, K9).

**Records.** R2 and P3 (checks A and B, 21 October); R3 and P6 (checks D and E, 4 November); P7 (check F, 4 November).

**Files.** `analysis/raw/semgrep_pilot_official_rules_REFERENCE_2026-10-21.txt`, `analysis/raw/semgrep_pilot_official_rules_PERSONAL_2026-10-21.txt`, `analysis/raw/semgrep_samshape_control_REFERENCE_2026-11-04.txt`, `analysis/raw/semgrep_checks_D_E_PERSONAL_2026-11-04.txt`, `analysis/raw/semgrep_per_rule_PERSONAL_2026-11-04.txt`, `data/reference_inventory/md5crypt_pilot_reference_list_2026-10-21.md`

**Limits.** L2 (reduced), L3, L9.

**Not claimed.** That any rule would miss other forms of these calls; anything about Semgrep recall in general; the 0 of 3 is an illustration of the calculation.

## K5 (O2) - Observation recorded

**Claim.** The same four rules give 0 findings, twice, on StringUtils.java (425 lines, no cryptography): no false positive on that file.

**Records.** P4, 21 October, my own check C on my MacBook, twice.

**Files.** `analysis/raw/semgrep_TC5_known_negative_PERSONAL_2026-10-21.txt`

**Limits.** L1.

**Not claimed.** A false-positive rate.

## K6 (O3) - Observation recorded

**Claim.** Checks A, B and C repeat on my MacBook (Semgrep 1.99.0) with the same findings as the container (Semgrep 1.181.0), each run twice with an empty diff between the two outputs.

**Records.** R2, 21 October, reference run by Claude in the container, checks A and B. P3, 21 October, my own checks A and B on my MacBook, each twice. P4, 21 October, my own check C on my MacBook, twice.

**Files.** `analysis/raw/semgrep_pilot_official_rules_REFERENCE_2026-10-21.txt`, `analysis/raw/semgrep_pilot_official_rules_PERSONAL_2026-10-21.txt`, `analysis/raw/semgrep_TC5_known_negative_PERSONAL_2026-10-21.txt`

**Limits.** L4.

**Not claimed.** Equivalence of the two Semgrep versions or machines.

## K7 (O4) - Observation recorded

**Claim.** Adding one entry to a copy of the inventory template by hand needs three checks (parse, entry count, comparison with the original); attempt 1 failed to parse, attempt 2 saved nothing, attempt 3 passed.

**Records.** Test case 2, 21 October, my three attempts at the template round-trip.

**Files.** `analysis/raw/TC2_template_roundtrip_PERSONAL_2026-10-21.txt`

**Limits.** L5.

**Not claimed.** CycloneDX schema validity, or that the process scales to a full inventory.

## K8 (O2) - Observation recorded (new)

**Claim.** On a 14-line control with the same call in two shapes, the unmodified official rule use-of-md5-digest-utils finds the chained form (line 6) and does not find the variable form (lines 10 to 12), which is the shape Md5Crypt.java uses at lines 259, 275 and 312. The same rule also finds nothing in DigestUtils.java, DigestUtilsTest.java or Md5Crypt.java from the pinned commit.

**Records.** R3, 4 November, reference run by Claude in the container (Semgrep 1.181.0). P6, 4 November, my own checks D and E on my MacBook (Semgrep 1.99.0), each twice, identical: 1 finding at line 6, 0 findings on DigestUtils.java and DigestUtilsTest.java.

**Files.** `analysis/raw/semgrep_samshape_control_REFERENCE_2026-11-04.txt`, `analysis/raw/semgrep_checks_D_E_PERSONAL_2026-11-04.txt`, `data/test_material/same_shape_control/SameShapeControl.java`, `data/test_material/same_shape_control/README.md`

**Limits.** L1, L7, L8.

**Not claimed.** How common either shape is in real code; behaviour of any other rule; behaviour of other Semgrep versions.

## K9 (O2) - Observation recorded (new)

**Claim.** Each of the other three official rules finds its expected findings on its own test file (use-of-md5: 3 at lines 7, 15, 29; weak-random: 3 at lines 48, 51, 165; md5-used-as-password: 1 at line 41) and finds 0 on Md5Crypt.java, which contains no getInstance call.

**Records.** P7, 4 November, my own run on my MacBook (Semgrep 1.99.0), one run each. Claude had run the same commands in its container (Semgrep 1.181.0) beforehand and got the same counts; that run was not saved as a record.

**Files.** `analysis/raw/semgrep_per_rule_PERSONAL_2026-11-04.txt`

**Limits.** L9.

**Not claimed.** Behaviour of these rules on other forms of the calls; any statement about other Java files.

## Limits

**L1.** One file per tool, chosen by convenience (it uses MD5 and is public). Consequence: no claim about rates or about Java code in general.

**L2.** The Check A positive control has a different code shape from Md5Crypt.java (ISSUE-08). Check D adds a same-shape pair for one rule. Consequence: the explanation of the zero is now tested for that rule only; the other three rules are not probed one by one.

**L3.** The reference list was drafted by Claude, not built by two independent passes of mine (ISSUE-09). Consequence: any recall figure from it is an illustration only.

**L4.** Self-check on two Semgrep versions and two machines, two checks each. Consequence: repeatability of my execution, not equivalence of versions.

**L5.** The template check covers JSON validity, not the CycloneDX schema. Consequence: the inventory instrument is only partly validated.

**L7.** The control file is synthetic (written by Claude). It was run by Claude (1.181.0) and by me (1.99.0, P6), one rule, two versions. Consequence: K8 holds for this one rule and these two versions only; my P6 run was not blind to the expected result.

**L8.** DigestUtils.java line 469 holds `getMd5Digest().digest(data)` without the `DigestUtils.` prefix and the rule does not match it. This is a second shape the rule misses; it was observed, not explored. Consequence: the shape gap has at least two forms.

**L9.** Check F ran once per rule, my run was not blind, and Claude's earlier container run of the same commands was not saved. Consequence: K9 is a single run on one version.

**L6.** The Sonar plugin and the TLS scanner have not been run. Consequence: nothing here is a three-way comparison.

## Pinned inputs

Md5Crypt.java: apache/commons-codec commit f13dd50f566c318283c4138820b15d75c26a0217, 361 lines, sha256 fa779456b25d2d36a6c464e200e106c2fa8e94a45dc608844ceb04407ea90747. StringUtils.java: same commit, 425 lines, sha256 6c44ebc7424c69fd04b6f3df10332934a149e6901fd29e86d96df4176527a99a. Rules: semgrep/semgrep-rules commit 17e31e11ebac99fb7dfe1cd288f7a32151b6f3f9. Rule fixture sha256 bd22fdb5ef195e383ec69aa9dbf1d0fd8f6cb5d41aef3f725f1aba5e5aa05908. Inventory template sha256 a851ef3d6547c6e75f728144f2e8b9575b0853f4e63a4f9b65c693ad89a2139d. Semgrep 1.181.0 (container, Ubuntu 24.04.5, Python 3.13.16); Semgrep 1.99.0 (MacBook, macOS 15.7.9, Python 3.8.2). Control file SameShapeControl.java sha256 657e8eb1ac803fecb27dcbe7808781c5fd315a4981c7f33424645d25ae7c8539. Rule yaml use-of-md5-digest-utils.yaml sha256 a0614baf029418dd9b298713c3328f371faa1edb0eac7cc2c4a3a99ce1a220a5 (computed in the container).
