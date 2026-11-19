# INDEPENDENT_SOURCE_PASS_PACKAGE.md

Request and record template for an independent source pass over `Md5Crypt.java`. Prepared 19 November 2026 for Assignment 12. **No independent source pass had been done as of this date. Update 19 November evening: one list was received; see `docs/INDEPENDENT_REVIEW_RECORD_2026-11-19.md`.** This file is a request, not a record of one.

## Who

A person other than me (Nitin Prakash) and other than an AI assistant, who has not worked on the project. They need a text editor or a browser. About 45 to 60 minutes. They should not look at any Semgrep output or at `data/reference_inventory/` before they finish.

## What I will send them (and nothing else)

- The file: https://github.com/apache/commons-codec/blob/f13dd50f566c318283c4138820b15d75c26a0217/src/main/java/org/apache/commons/codec/digest/Md5Crypt.java (361 lines, public, Apache License 2.0).
- The request text below and the record template.

## Request text (copy as is)

"Please read this one Java file and list every place where it performs, or prepares for, a cryptographic operation. Work from the source only. For each one, write a short name for the operation, the algorithm or kind of material involved (for example a hash algorithm, a random number source, a salt, a password), the line number or numbers, and one sentence on why you think it counts. Say where you were unsure and what you decided. Do not ask me what I think counts; if a rule is unclear, write down how you interpreted it. Please send it back as you wrote it."

## What they send back

1. Name or initials, date, how long it took.
2. Their list, one item per line: name, algorithm or material, line numbers, reason.
3. Places they were unsure and what they decided.
4. One sentence: "I did this from the source only, without help from the author" (true or false, and if false, what help was given).

## How I record it

I save their text unedited as `data/reference_inventory/independent_pass_REVIEWER_<date>.md`. Then, item by item, I compare it with `reference_inventory_v1_candidate_2026-11-19.json` and write the result (agree, disagree, one-sided, resolved how) in `data/reference_inventory/independent_pass_comparison_<date>.md`, using no tool output. Only after that, and after schema validation, is a frozen version hashed (`docs/INVENTORY_FREEZE_RECORD.md`).
