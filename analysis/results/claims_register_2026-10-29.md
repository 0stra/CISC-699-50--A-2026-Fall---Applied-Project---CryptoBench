# Claims register, Assignment 09 (29 October 2026)

Each claim in the Assignment 09 memo, the records that support it, the limits that bound it and its status. Procedural pilot findings only. None of these answers the research question. Written by Claude (AI assistant) from the existing records in this repository; no new tool run was made. I have not yet compared every line against the raw files myself (see the AI log in the memo).

Run labels: R = reference run by Claude in a cloud container. P = run on my MacBook. P1 was typed by Claude Code at my request; P3 and P4 I typed and ran myself. TC2 = my three attempts at the template round-trip.

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

## K4 (O2) - Provisional interpretation

**Claim.** The zero from four official rules on Md5Crypt.java (reference list: MD5 created at lines 259, 275, 312) is a coverage gap for the variable form, not a broken tool.

**Records.** R2, 21 October, reference run by Claude in the container, checks A and B. P3, 21 October, my own checks A and B on my MacBook, each twice.

**Files.** `analysis/raw/semgrep_pilot_official_rules_REFERENCE_2026-10-21.txt`, `analysis/raw/semgrep_pilot_official_rules_PERSONAL_2026-10-21.txt`, `data/reference_inventory/md5crypt_pilot_reference_list_2026-10-21.md`

**Limits.** L2, L3.

**Not claimed.** Anything about Semgrep recall in general; the 0 of 3 is an illustration of the calculation.

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

## Limits

**L1.** One file per tool, chosen by convenience (it uses MD5 and is public). Consequence: no claim about rates or about Java code in general.

**L2.** The positive control has a different code shape from the code it is meant to vouch for (ISSUE-08). Consequence: the explanation of the zero is a reading, not a test.

**L3.** The reference list was drafted by Claude, not built by two independent passes of mine (ISSUE-09). Consequence: any recall figure from it is an illustration only.

**L4.** Self-check on two Semgrep versions and two machines, two checks each. Consequence: repeatability of my execution, not equivalence of versions.

**L5.** The template check covers JSON validity, not the CycloneDX schema. Consequence: the inventory instrument is only partly validated.

**L6.** The Sonar plugin and the TLS scanner have not been run. Consequence: nothing here is a three-way comparison.

## Pinned inputs

Md5Crypt.java: apache/commons-codec commit f13dd50f566c318283c4138820b15d75c26a0217, 361 lines, sha256 fa779456b25d2d36a6c464e200e106c2fa8e94a45dc608844ceb04407ea90747. StringUtils.java: same commit, 425 lines, sha256 6c44ebc7424c69fd04b6f3df10332934a149e6901fd29e86d96df4176527a99a. Rules: semgrep/semgrep-rules commit 17e31e11ebac99fb7dfe1cd288f7a32151b6f3f9. Rule fixture sha256 bd22fdb5ef195e383ec69aa9dbf1d0fd8f6cb5d41aef3f725f1aba5e5aa05908. Inventory template sha256 a851ef3d6547c6e75f728144f2e8b9575b0853f4e63a4f9b65c693ad89a2139d. Semgrep 1.181.0 (container, Ubuntu 24.04.5, Python 3.13.16); Semgrep 1.99.0 (MacBook, macOS 15.7.9, Python 3.8.2).
