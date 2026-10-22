# ISSUE_LOG.md

CryptoBench issue and risk log. Updated 22 October 2026 (Hard Stop 3, thesis version 2). Belongs at `docs/ISSUE_LOG.md`. Owner of every item: Nitin (individual project).

## Issues

- ISSUE-01, Sonar Cryptography Plugin not installed. Severity: high. State: open. The 25 October gate in Assignment 07 Rule 1 will not be met, so the fallback applies unless Dr. Shaalan decides otherwise.
- ISSUE-02, Semgrep registry rule drift. Severity: medium. State: mitigated for the pilot runs by local rules pinned by commit. Open for any run that uses the registry.
- ISSUE-03, repository folder nesting. Severity: low. State: open until I confirm from the repository tree that leftover copies under `docs/` are gone.
- ISSUE-04, environment record placeholders. Severity: medium. State: partly closed. Semgrep, Python and operating system are filled in. SonarQube, plugin, TLS scanner and Git are still empty.
- ISSUE-05, no tool-execution evidence. Severity: high (version 1). State: closed for Semgrep by R1, P1, R2, P3, P4 and test case 2. Open for the plugin and the TLS scanner.
- ISSUE-06, ruleset p/cryptography does not exist (HTTP 404 on 18 October, also p/crypto). Severity: high. State: mitigated by pinned local rules, awaiting Dr. Shaalan's confirmation. `.semgrep.yml` unchanged.
- ISSUE-07, Semgrep 1.99.0 on the laptop and 1.181.0 in the container. Severity: medium. State: checked for checks A, B and C, which give the same findings. Other rules untested. Scored runs to use one environment.
- ISSUE-08 (new, 22 October), positive control of the wrong code shape. The control passes on the chained MD5 form and Md5Crypt.java uses the variable form, so a passing control did not warn about the miss. Severity: medium to high. State: open. Protocol change 2 applies. Closed when a same-shape control is found or the gap is recorded.
- ISSUE-09 (new, 22 October), reference list not independent. Claude drafted the nine entries. Severity: high. State: open. My own pass is pending.
- ISSUE-10 (new, 22 October), hand-editing of the inventory template failed twice before passing (test case 2). Severity: low to medium. State: mitigated by protocol change 5. Not checked against the CycloneDX schema, so not fully closed.

## Risks carried forward

- RISK-01, SonarQube and plugin version pairing. High. Untested.
- RISK-02, inventory labelling errors. Medium. The pilot shows why a list I did not build cannot be the answer key.
- RISK-03, transcription errors in hand scoring. Medium. Applies when scoring starts.
- RISK-04, selection bias in test material. Medium. The one file used was chosen by convenience.
- RISK-05, TLS endpoint authorisation. Medium. Unchanged. No endpoint is scanned without written authorisation.

## Single risk most likely to undermine the midpoint evidence review

ISSUE-09. Every recall figure rests on a reference list I have not independently checked.
