# Journal, 18 October 2026 (second entry)

## Test case 1 attempted on my own computer

**Who ran it, and where.** I ran this on my MacBook on 18 October 2026, around 2:35 to 2:36 PM, using Claude Code (an AI assistant in the terminal) to type the commands at my request. I read the output. The full output is in `analysis/raw/semgrep_TC1_mac_attempt_2026-10-18.txt`.

**What happened.**
- `pip3 install semgrep` failed, because this Mac has only the system Python 3.8.2 with pip 19.2.3 and no Homebrew. Installing into a separate virtual environment worked and gave Semgrep 1.99.0, the newest version that supports Python 3.8.
- I downloaded `Md5Crypt.java` from apache/commons-codec (361 lines, Apache License). It came from the master branch, so I did not record a commit hash for it.
- I ran Semgrep twice with `--config p/cryptography`. Both runs failed the same way: "Failed to download configuration from https://semgrep.dev/p/cryptography HTTP 404", exit code 7. No file was scanned.
- A registry check showed `p/cryptography` and `p/crypto` return 404, while `p/java` and `p/security-audit` return 200.

**Result for test case 1: not passed.** The pass criterion (a clean finish with readable output) was not met on my machine.

**What this shows.** The ruleset name written in my project files, `p/cryptography`, does not exist in the Semgrep registry on this date. This is a real defect in my plan, found by running the tool. It also means my project's `.semgrep.yml` is wrong as written. The earlier container run (see `journal/2026-10-18.md`) worked only because it used rules taken from the semgrep-rules GitHub repository.

**New issues logged.**
- ISSUE-06: the ruleset `p/cryptography` does not exist (HTTP 404 on 18 Oct). Severity: high, because every Semgrep run in my plan names it. Mitigation: use the unmodified Java crypto audit rules from the semgrep-rules repository, pinned by commit, instead. This also fixes the rule drift problem in ISSUE-02. Status: open until Dr. Shaalan confirms the change.
- ISSUE-07: my Mac's Python 3.8 limits Semgrep to 1.99.0, while the container run used 1.181.0. Results from the two versions may not be comparable. Severity: medium. Mitigation: pin and record the version used for each run, and do all scored runs in one environment. Status: open.

**What this does not show.** It says nothing about whether Semgrep detects cryptography, because nothing was scanned.

**Next.** Re-run test case 1 on my Mac using the crypto audit rules from semgrep-rules (clone the repository, note the commit, scan the same file twice), save the output in `analysis/raw/`, and record the versions in `docs/ENVIRONMENT.md`. Ask Dr. Shaalan to confirm the ruleset change.
