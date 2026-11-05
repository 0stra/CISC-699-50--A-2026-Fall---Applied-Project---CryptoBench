# CryptoBench

A Comparative Benchmark of Cryptographic Discovery Methods for Post-Quantum Migration Readiness.

CISC 699 thesis, Harrisburg University. Student: Nitin Prakash. Supervisor: Dr. Majid Shaalan. This is the research README for the Assignment 10 release candidate (audited commit named in `docs/AUDIT_RECORD_A10.md`; final tag `a10-rc2`; updated 4 November 2026). It is a record of a pilot, not a finished study.

## 1. Purpose

The thesis compares existing cryptographic discovery tools (Semgrep, the Sonar Cryptography Plugin inside SonarQube, and a TLS scanner) against an independently built reference inventory in CBOM (CycloneDX) form, to see how ready each is to support post-quantum migration planning. There is no custom code and there are no custom rules. Everything here is configuration, records and evidence.

The principal claims that this release candidate lets a reviewer check are small and procedural. They say the Semgrep procedure runs on public inputs, what it returned, and how a zero result was classified. None of them answers the research question.

## 2. What is here (inventory)

The full list, with a SHA-256 for every file and its role, is `docs/RELEASE_MANIFEST.md`. In short:

- `docs/`: `PROCEDURE_NOTES.md` (status, run labels, protocol rules, fallback rules; start here), `ENVIRONMENT.md` (pinned versions and hashes), `ISSUE_LOG.md`, `REPRODUCE.md` (steps), `AUDIT_RECORD_A10.md` (the audit), `RESPONSE_LOG.md`, `RELEASE_MANIFEST.md`.
- `analysis/raw/`: unmodified run records, one file per run.
- `analysis/results/`: the claims register (`claims_register_2026-11-04.md`, version 2; version 1 is kept) and two figures.
- `analysis/scored/`: empty. Scoring has not started.
- `data/test_material/`: the same-shape control. No benchmark sample is selected yet.
- `data/reference_inventory/`: the inventory template, a provisional nine-entry list for `Md5Crypt.java`, and my own pass 1.
- `journal/`: dated working entries.
- `research/`: Assignments 03 and 04, where uploaded (not yet in this repository).
- `.semgrep.yml`, `sonar-project.properties`: tool configuration. `.semgrep.yml` still names the dead ruleset `p/cryptography` (ISSUE-06) and no run uses it.

## 3. Provenance

- **Code under test.** `Md5Crypt.java` and `StringUtils.java` from apache/commons-codec (Apache License 2.0), commit `f13dd50f566c318283c4138820b15d75c26a0217`. They are not stored here. The commands in `docs/REPRODUCE.md` download them and check their SHA-256.
- **Rules.** Unmodified files from semgrep/semgrep-rules, commit `17e31e11ebac99fb7dfe1cd288f7a32151b6f3f9`. Not stored here either.
- **Run records.** File names say who ran it. `REFERENCE` = run by Claude (AI assistant) in a cloud container, not on my computer. `PERSONAL` = my own run on my MacBook. Each record states the tool version, rules commit and input hashes. A run that Claude Code typed on my laptop (P1) is described as such in its record.
- **Authored by Claude.** The provisional reference list, the same-shape control file, the claims registers, the figures, and drafts of the docs were written by Claude from my instructions and the records. I reviewed them but have not checked every line myself. The AI log in each assignment document gives the detail.
- **Authored by me.** My own pass 1 over `Md5Crypt.java` (`data/reference_inventory/own_pass/`), my runs on the MacBook (P3, P4, P5, test case 2), and the decisions in the journal. Pass 1 is not fully independent because I had seen the provisional list first.

## 4. Prerequisites

A Linux or macOS terminal, `git`, `curl`, a SHA-256 tool, Python 3.8 or newer, Semgrep (1.99.0 or 1.181.0 recorded as working) and access to github.com. No account, key or credential is needed. Details: `docs/REPRODUCE.md`, section 0.

## 5. Steps

Follow `docs/REPRODUCE.md`. It has the exact commands for checks A, B, C and D, the expected output of each, and what to record. It has five checks (A to E) and takes about 15 minutes.

## 6. Expected outputs and argument structure

The argument has four steps. Each has a claim number in `analysis/results/claims_register_2026-11-04.md`.

1. The procedure runs on public inputs, repeatably (K1, K6): checks A, B, C give the same findings on two machines and two Semgrep versions.
2. The tool is not simply broken (K3): check A, the rule author's own test file, gives 1 finding at line 15.
3. It does not raise a false alarm on a file with no cryptography (K5): check C gives 0.
4. It returns 0 on `Md5Crypt.java` (check B), which creates MD5 digests at lines 259, 275 and 312. The same-shape control (K4, K8, checks D and E) shows the one rule built for this call finds the chained form and misses the variable form. So the zero is read as a coverage gap for that rule, not as safety.

Expected outputs: A = 1 finding (line 15); B = 0; C = 0; D = 1 finding (line 6 only); E = 0 on two further Apache files.

## 7. Restrictions and access

- **No restricted data is held or needed.** Every input is a public file or public rule. Nothing in this repository is personal data or a secret.
- **TLS scanner: nothing was scanned.** No endpoint has written authorisation on file (RISK-05; fallback Rule 2 in `docs/PROCEDURE_NOTES.md`). A reviewer must not scan any third-party endpoint to check this work. Any future TLS evidence will come from a service I own or one with written authorisation, and the authorisation (without private details) will be recorded here.
- **Safe substitutes.** The rule author's test file and my 14-line control are used only to demonstrate the procedure. They are not evidence about any protected or private system, and no verification of restricted findings is claimed.
- **Sonar Cryptography Plugin.** Not installed. A reviewer cannot reproduce anything for it (ISSUE-01).
- **Hand-made inputs.** The inventory is filled by hand. Its JSON validity was checked once (test case 2); its CycloneDX schema validity was not.

## 8. What is not here (known limitations)

- No benchmark sample set and no scored result. `analysis/scored/` is empty. The frozen procedure runs on the planned sample in Assignment 11.
- The reference inventory is not frozen. The provisional list was drafted by Claude; my pass 1 is not fully independent; pass 2, the agreed list and the comparison are still to do (ISSUE-09). No recall or precision may be computed from it.
- One file per tool, chosen by convenience (RISK-04).
- Two Semgrep versions are in use (ISSUE-07). Registry rules drift (ISSUE-02), so only the pinned files are used.
- The control file is synthetic and was run once by Claude (claims register L7).
- Nothing here has been confirmed by my supervisor. No approval is implied by any file.

## 9. Reviewer navigation: how to verify a claim

1. Open `analysis/results/claims_register_2026-11-04.md` and pick a claim (for example K8).
2. Read its Records and Files lines. Open the named raw file in `analysis/raw/` and find the command line and the output.
3. Run the matching check from `docs/REPRODUCE.md` yourself and compare.
4. Read the claim's Limits and Not claimed lines, and the matching entries in `docs/ISSUE_LOG.md`.
5. For how this package was audited, read `docs/AUDIT_RECORD_A10.md`; for what changed after professor feedback, read `docs/RESPONSE_LOG.md`.

## 10. AI use

Claude and Claude Code (AI assistants) were used on this project for research, drafting, running commands, formatting and packaging. The AI log in each assignment document and the notes in each record say what was done by AI and what by me.
