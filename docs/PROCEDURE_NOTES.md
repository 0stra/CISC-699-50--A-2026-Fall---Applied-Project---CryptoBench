# PROCEDURE_NOTES.md

CryptoBench procedure notes and protocol. Updated 22 October 2026 (Hard Stop 3, thesis version 2). Belongs at `docs/PROCEDURE_NOTES.md`.

This file says what currently works, what is partial and what is blocked, and which rules my procedure follows. It does not repeat commands. The exact commands are in the raw files in `analysis/raw/`, so there is one source of truth.

## 1. Status of each method (22 October 2026)

- Semgrep: pilot done on one public file (Md5Crypt.java). Runs R1, P1, R2, P3 and P4 and test case 2 are recorded. Usable with the protocol changes in section 3. No accuracy claim.
- Sonar Cryptography Plugin (inside SonarQube): not installed, not tested. Version pairing with SonarQube is unchecked (ISSUE-01, RISK-01).
- TLS scanner: not selected or installed. No endpoint scanned. No written authorisation on file (RISK-05).
- Reference inventory: template only. A nine-entry pilot list for Md5Crypt.java exists, drafted by Claude. It is provisional and not independent (ISSUE-09).

## 2. Run vocabulary (same as Assignment 08)

- R1, R2: reference runs done by Claude in a cloud container, not on my computer.
- P1, P3, P4: my own runs on my MacBook.
- P2: one extra VS Code scan with custom rules. Supplementary only.
- Test case 2: my own attempts to add one entry to a copy of the inventory template.

## 3. Protocol (changed after the pilot)

1. Every zero is reported with its control and a note on which code shapes the rule covers. It is classed as non-functional, true negative, or coverage gap.
2. A positive control must contain the same code shape as the thing it validates. If no official rule detects a shape that appears in the samples, the gap is recorded for the method. No custom rules (NFR-6).
3. The registry ruleset p/cryptography is replaced by unmodified rule files pinned by commit. `.semgrep.yml` is changed only after Dr. Shaalan confirms.
4. Every run record states who ran it and where (reference or personal), the tool version, the rules commit and the input hashes.
5. After any hand edit of an inventory file I check three things: it parses, the expected entries are counted, and it is compared with the original. Edits are made on a copy only.
6. Scored runs are done in one environment, with its versions recorded in `docs/ENVIRONMENT.md`.

## 4. Order of work (unchanged from the design, with this pilot's lessons)

1. Reference inventory frozen after two independent passes by me agree. Nothing is scanned on the pilot set before this.
2. Known-positive and known-negative gate for each method, on validation samples only.
3. Run each method, keep raw output unedited, then repeat.
4. Hand-score by category against the frozen inventory.

## 5. Fallback rules set in Assignment 07 (unchanged)

- Rule 1: if the plugin has not passed its known-positive check by 25 October, continue with Semgrep and the TLS scanner and report the plugin as an open dependency.
- Rule 2: if TLS authorisation is not in writing by 1 November, scan only a service I own and label it that way.
- Rule 3: if fewer than 15 samples are found, report a method-feasibility case study.
