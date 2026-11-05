# ISSUE_LOG.md

CryptoBench issue and risk log. Updated 22 October 2026 (Hard Stop 3, thesis version 2), revised 31 October 2026 (ISSUE-09 progress), revised 4 November 2026 (ISSUE-08 control and ISSUE-09 pass 2, Assignment 10). Belongs at `docs/ISSUE_LOG.md`. Owner of every item: Nitin (individual project).

## Issues

- ISSUE-01, Sonar Cryptography Plugin not installed. Severity: high. State: open. The 25 October gate in Assignment 07 Rule 1 has passed without the plugin being installed, so the fallback applies (Semgrep and the TLS scanner, plugin reported as an open dependency) unless Dr. Shaalan decides otherwise.
- ISSUE-02, Semgrep registry rule drift. Severity: medium. State: mitigated for the pilot runs by local rules pinned by commit. Open for any run that uses the registry.
- ISSUE-03, repository folder nesting. Severity: low. State: closed. Leftover copies under `docs/` were moved to the top-level folders in the repository reorganisation; to be confirmed from the repository tree.
- ISSUE-04, environment record placeholders. Severity: medium. State: partly closed. Semgrep, Python and operating system are filled in. SonarQube, plugin, TLS scanner and Git are still empty.
- ISSUE-05, no tool-execution evidence. Severity: high (version 1). State: closed for Semgrep by R1, P1, R2, P3, P4 and test case 2. Open for the plugin and the TLS scanner.
- ISSUE-06, ruleset p/cryptography does not exist (HTTP 404 on 18 October, also p/crypto). Severity: high. State: mitigated by pinned local rules,`.semgrep.yml` unchanged.
- ISSUE-07, Semgrep 1.99.0 on the laptop and 1.181.0 in the container. Severity: medium. State: checked for checks A, B and C, which give the same findings. Scored runs to use one environment.
- ISSUE-08 (new, 22 October), positive control of the wrong code shape. The control passes on the chained MD5 form and Md5Crypt.java uses the variable form, so a passing control did not warn about the miss. Severity: medium to high. State: closed for the pilot file on 4 November 2026, with the limits in the claims register. A same-shape control (`data/test_material/same_shape_control/`) was run by Claude (R3, `analysis/raw/semgrep_samshape_control_REFERENCE_2026-11-04.txt`): the rule finds the chained form (line 6) and not the variable form (lines 10-12). That explains the zero for this one rule. I repeated the control on my MacBook (P6, Semgrep 1.99.0) with the same result. On the same day I ran the other three rules one at a time (P7): each fires on its own test file and finds nothing in Md5Crypt.java, which has no call they target. Still open: other forms of those calls were not tested, and the control is one pair of shapes. Protocol change 2 still applies.
- ISSUE-09 (new, 22 October), reference list not independent. Severity: high. State: narrowed on 4 November 2026, not closed. Pass 1 (31 October) was not independent of the list Claude drafted. Pass 2 (4 November, after reading the numbered file, with help listed in `own_pass_agreed.md`) and an agreed list of 53 lines exist (`data/reference_inventory/own_pass/`); the comparison with the provisional list is in `own_pass_vs_claude.md`. The passes disagreed on 39 lines and the agreed list applies my three rules to those lines, so it is not the full agreement of two independent passes that the freeze rule asks for. Closed only if Dr. Shaalan accepts the reconciled list as frozen, or after a further independent pass.
- ISSUE-10 (new, 22 October), hand-editing of the inventory template failed twice before passing (test case 2). Severity: low to medium. State: mitigated by protocol change 5. Not checked against the CycloneDX schema, so not fully closed.

## Risks carried forward

- RISK-01, SonarQube and plugin version pairing. High. Untested.
- RISK-02, inventory labelling errors. Medium. The pilot shows why a list I did not build cannot be the answer key.
- RISK-03, transcription errors in hand scoring. Medium. Applies when scoring starts.
- RISK-04, selection bias in test material. Medium. The one file used was chosen by convenience.
- RISK-05, TLS endpoint authorisation. Medium. Unchanged. No endpoint is scanned without written authorisation.

