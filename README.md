# CryptoBench

A Comparative Benchmark of Cryptographic Discovery Methods for Post-Quantum Migration Readiness.

CISC 699 thesis, Harrisburg University. Student: Nitin Prakash. Supervisor: Dr. Majid Shaalan.

## What this is

A non-coding thesis that compares existing cryptographic discovery tools (Semgrep, the Sonar Cryptography Plugin inside SonarQube, and a TLS scanner) against an independently built reference inventory in CBOM (CycloneDX) form. There is no custom code and there are no custom rules. Everything here is configuration, records and evidence.

## Where things are

- `docs/PROCEDURE_NOTES.md`: current status of each method, run labels, protocol rules and fallback rules. Start here.
- `docs/ENVIRONMENT.md`: pinned tool versions, the rules commit, input file hashes and check results.
- `docs/ISSUE_LOG.md`: issue and risk log.
- `analysis/raw/`: unmodified tool output and run records, one file per run.
- `analysis/scored/`: scoring against the frozen inventory (not started).
- `data/test_material/`: selected samples and authorised endpoints.
- `data/reference_inventory/`: the inventory template and the provisional pilot list for `Md5Crypt.java`.
- `journal/`: dated working entries, one file per session.
- `research/`: the submitted literature brief (Assignment 03) and design review (Assignment 04), where uploaded.
- `.semgrep.yml` and `sonar-project.properties`: tool configuration. Note: `.semgrep.yml` still names the registry ruleset `p/cryptography`, which returns HTTP 404 (ISSUE-06). Runs use unmodified rule files pinned by commit instead, listed in `docs/ENVIRONMENT.md`.

## How to read the run records

- Files ending `REFERENCE` are reference runs done by Claude (an AI assistant) in a cloud container, not on my computer.
- Files ending `PERSONAL` are my own runs on my MacBook.
- Each record states who ran it, the tool version, the rules commit and the input file hashes. Raw records are not edited after they are written, except to correct their headers.

## AI use

Claude and Claude Code were used on this project. Each assignment carries a file-specific AI-use log, and the raw records and journal entries say which runs and drafts were done by AI.
