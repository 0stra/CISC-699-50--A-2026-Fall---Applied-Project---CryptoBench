# K4_RULE_ANALYSIS_2026-11-19.md

Analysis of the pinned rule behind claim K4, written by Claude (AI assistant) on 19 November 2026 for Assignment 12, in answer to the Assignment 11 feedback (priority 2: inspect the rule, document the exact matching conditions, test one code feature at a time, record expected and observed outcomes, include the unprefixed call at `DigestUtils.java` line 469). **I (Nitin Prakash) have not yet read the rule file myself.** The checklist at the end is what I will do; until I have done it, K4 stays provisional (`analysis/results/claims_register_2026-11-19.md`).

## The rule

`java/lang/security/audit/crypto/use-of-md5-digest-utils.yaml` in semgrep/semgrep-rules commit `17e31e11ebac99fb7dfe1cd288f7a32151b6f3f9` (sha256 `a0614baf029418dd9b298713c3328f371faa1edb0eac7cc2c4a3a99ce1a220a5`). Its matching part is:

- `pattern: $DU.$GET_ALGO().digest(...)`
- `metavariable-pattern: $GET_ALGO` must be `getMd5Digest`
- `metavariable-pattern: $DU` must be `DigestUtils`
- `focus-metavariable: $GET_ALGO` (the finding is reported on the method name)

## Exact matching conditions (from the text of the rule)

1. There is a method call whose receiver expression is the name `DigestUtils`.
2. The method called on that receiver is named `getMd5Digest`.
3. A call to `digest` with any arguments (including none) is made directly on the result of that call, in the same expression.
4. Nothing in the rule looks at variables: it does not follow a value stored in a variable, and it does not match a creation call on its own.

## Reading against the code

- Positive control (the rule author's test file, line 15): `DigestUtils.getMd5Digest().digest(password.getBytes())` meets conditions 1 to 3. One finding, as observed (check A).
- `Md5Crypt.java` lines 259, 275 and 312: `final MessageDigest messageDigestMd5 = DigestUtils.getMd5Digest();` and the same forms. The digest is created and stored; `.digest()` is called later on the variable. Condition 3 fails, so the rule has nothing to match. Zero findings, as observed (checks B and E).
- `DigestUtils.java` line 469: `return getMd5Digest().digest(data);`. Conditions 2 and 3 hold but the call has no `DigestUtils.` receiver, so condition 1 fails. Zero findings, as observed (check E).
- The rule's own test file marks line 7, `MessageDigest.getInstance("MD5")`, with `ok:`. That is not a miss: this rule is about Commons Codec calls; `getInstance("MD5")` belongs to the rule `use-of-md5` (check F, 3 findings on its own test file).

## Controlled variants (R4)

Twelve synthetic files in `data/test_material/k4_variants/`; expected outcomes were committed in `45f6180` before the run; one run each by Claude, Semgrep 1.186.0, record `analysis/raw/semgrep_K4_variants_REFERENCE_2026-11-19.txt`. All twelve observed outcomes matched the expectation.

- V00 chained baseline: match, line 6.
- V01 variable form (creation stored, digest later): no match. Same shape as `Md5Crypt.java`.
- V02 unprefixed call `getMd5Digest().digest(data)`: no match. Same shape as `DigestUtils.java` line 469.
- V03 fully qualified receiver `org.apache.commons.codec.digest.DigestUtils`: no match (expected with uncertainty; the result is new information).
- V04 `getSha512Digest()` chained: no match.
- V05 chained `digest()` with no arguments: match.
- V06 chained `update(data)` instead of `digest`: no match.
- V07 the chained call split over three lines: match, reported on line 7, the line holding `.getMd5Digest()` (the effect of `focus-metavariable`).
- V08 parentheses around the creation call: match (expected with uncertainty).
- V09 `DigestUtils.md5(data)`: no match. Another API that computes MD5, not covered by this rule.
- V10 `DigestUtils.md5Hex(s)`: no match.
- V11 chained call with the result assigned to a variable: match.

## What this supports and what it does not

Supports: the cause named in K4 for this rule is the shape of the call. The rule needs `DigestUtils.getMd5Digest().digest(...)` written as one expression with that receiver name. Variable form, unprefixed form, fully qualified form and the one-call helpers `md5` and `md5Hex` are outside it. This is a statement about this rule, on twelve synthetic shapes.

Does not support: anything about how often these shapes occur in real code; any statement about the other three rules (their cause rests on check F, K9); any statement about Sonar or the TLS scanner; the third conclusion in K4 (that the inventory holds an item that was not reported) because the inventory is not frozen or independent.

## My checklist (not yet done)

1. Open the rule file (`java/lang/security/audit/crypto/use-of-md5-digest-utils.yaml` in the pinned clone) and read the four lines above myself. Write one sentence per condition in my own words.
2. Re-run the twelve variants in my Docker container (commands in the response log entry H2) and save the output as `analysis/raw/semgrep_K4_variants_PERSONAL_<date>.txt`.
3. Compare each result with `data/test_material/k4_variants/expected_outcomes.tsv`. Any difference is recorded, not fixed quietly.
4. If steps 1 to 3 agree, change the K4 status in a new register version. If not, change K4's wording.
