# INVENTORY_FREEZE_RECORD.md

Record of the reference inventory for Md5Crypt.java, 19 November 2026 (Assignment 12). Answers the Assignment 11 feedback, priority 1. **Status: candidate v1, hashed, NOT frozen.**

## Decisions made on 19 November 2026

- **Unit of measurement (decided by me, Nitin Prakash, on 19 November 2026, accepting Claude's proposal).** The primary unit is the *operation*: one item per cryptographic operation or material that a reviewer can name, with its algorithm or material type, file, line locations and the evidence for it. Source lines are supporting evidence only. The earlier counts (60 and 73 lines in my two passes, 53 lines in the agreed list) are line counts; the candidate inventory has 10 items covering the same 53 lines. Dr. Shaalan has not yet confirmed this choice.
- **Freeze status (decided by me on 19 November 2026).** Not frozen. I will freeze only after a person other than me has inspected the source without seeing the Semgrep output or the earlier lists, and the disagreements have been recorded and resolved. I did not choose to freeze it as a deviation.

## The candidate

- File: `data/reference_inventory/reference_inventory_v1_candidate_2026-11-19.json` (CycloneDX 1.6; one component per item; `evidence.occurrences` with file and line for every supporting line).
- SHA-256: `fa216520553f393ec294727c11e1e33a03e03a792a463f96be943b05a096f9cc`.
- Content: 10 items, 53 line occurrences, one file (`Md5Crypt.java`, commit `f13dd50f…`, sha256 `fa779456…`).
- Provenance: the 53 lines are my agreed list (`data/reference_inventory/own_pass/agreed_lines.txt`), reconciled by me from my passes 1 and 2 under rules 1A, 2A and 3B. Claude grouped the lines into the 10 items and wrote the item descriptions on 19 November 2026. **I have not yet reviewed that grouping.**
- Schema validation: valid against CycloneDX 1.6, with a negative control that failed as it should (`analysis/raw/cyclonedx_schema_validation_REFERENCE_2026-11-19.txt`, check-jsonschema 0.39.0).

## Why it is not frozen (the limits)

1. The first list was drafted by Claude (provisional list, 21 October) and my pass 1 followed it.
2. My pass 2 and the agreed list were reconciled by my own rules after the two passes disagreed on 39 lines (ISSUE-09).
3. No second person has inspected the source.
4. The item grouping and descriptions were written by Claude and are not yet reviewed by me.
5. Dr. Shaalan has not confirmed the unit or the list.

## What freezing will require

1. I review the 10 items against the source and record any change (a change makes a new candidate and a new hash).
2. An independent reviewer completes `docs/INDEPENDENT_SOURCE_PASS_PACKAGE.md` without the Semgrep output or the earlier lists.
3. Disagreements between their list and the candidate are recorded item by item with how each was resolved.
4. The agreed file is validated against the CycloneDX 1.6 schema again.
5. The final file's SHA-256 is written here and in the response log, and the file is not changed afterwards. A later change is a new version with a new hash.

No recall or precision is calculated from this inventory before step 5. If step 2 cannot be done, the thesis keeps the limit and the candidate stays a candidate.

## Items (summary; the JSON is the record)

- CB-INV-01 MD5 digest for the main hash (9 lines, includes creation at 259).
- CB-INV-02 MD5 digest for the alternate sum (5 lines, creation at 275).
- CB-INV-03 MD5 digest created and used in each of 1,000 rounds (11 lines, creation at 312).
- CB-INV-04 MD5-based crypt scheme and its parameters (6 lines).
- CB-INV-05 random salt generation (2 lines).
- CB-INV-06 SecureRandom instance (1 line).
- CB-INV-07 salt validation and extraction (6 lines).
- CB-INV-08 password converted to bytes (1 line).
- CB-INV-09 final digest encoded to crypt Base64 (6 lines).
- CB-INV-10 zeroising of secret bytes (6 lines).

Only the three creation lines 259, 275 and 312 are the target of the Semgrep MD5 rules. The other items show how much of the file's cryptographic behaviour a call-pattern rule does not address by design; they are not misses by Semgrep.
