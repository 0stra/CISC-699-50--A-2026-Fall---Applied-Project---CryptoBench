# K4 controlled variants (Assignment 12)

Twelve small synthetic Java files that test, one code feature at a time, what the pinned rule `java/lang/security/audit/crypto/use-of-md5-digest-utils.yaml` (semgrep-rules commit 17e31e11ebac99fb7dfe1cd288f7a32151b6f3f9) matches. The rule's pattern is `$DU.$GET_ALGO().digest(...)` with `$GET_ALGO` = `getMd5Digest` and `$DU` = `DigestUtils`: a call named getMd5Digest on a receiver named DigestUtils, with `.digest(...)` chained directly on that call.

Written by Claude on 19 November 2026 from reading the rule. Synthetic material, not from any real project. `expected_outcomes.tsv` was written and committed BEFORE any variant was run; it holds the hypothesis for each file. Variants marked "(uncertain)" are real tests of the reading, not confirmations. A line marked `// TARGET` is the line a match would be reported on (or, for V01 and V06, the creation line that the rule does not report).

Run: `semgrep scan --metrics=off --disable-version-check --config <rules clone>/java/lang/security/audit/crypto/use-of-md5-digest-utils.yaml <file>` once per file. Results: `analysis/raw/`, files with `K4_variants` in the name.
