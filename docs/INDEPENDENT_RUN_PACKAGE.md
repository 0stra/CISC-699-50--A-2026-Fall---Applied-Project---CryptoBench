# INDEPENDENT_RUN_PACKAGE.md

Request and record template for an independent human run of `docs/REPRODUCE.md`. Prepared 14 November 2026. **No independent human run has been done as of this date.** **Update, 14 November, evening:** I repeated checks A to F myself in a fresh Docker container (`analysis/raw/semgrep_checks_A_to_F_PERSONAL_FRESHENV_2026-11-14.txt`). That is an author re-run, not an independent run; this package is still needed. This file exists so that the run can be done and recorded when a person is available; it is not a record of one.

## Who can run it

Any person other than me (Nitin Prakash) and other than an AI assistant: a classmate, a colleague, or Dr. Shaalan or someone he names. They need a Linux or macOS terminal, `git`, `curl`, Python 3.8 or newer and Semgrep. About 20 minutes. No account, key or credential is needed. They must not scan any third-party endpoint.

## Request text (copy as is)

"I am asking for a short, independent run of the reproduction steps for my thesis pilot. Please open `docs/REPRODUCE.md` in the repository (tag `a10-rc6`, https://github.com/0stra/CISC-699-50--A-2026-Fall---Applied-Project---CryptoBench) and follow it exactly, without asking me for help during the run. If a step is unclear or a result differs from the expected one, do not fix it quietly: write down what you did and what you saw. Please send me your terminal output and the answers below. Your own words are what I need."

## What the runner sends back

1. Their name or initials, date, operating system, `semgrep --version`.
2. The terminal output of each check (A to F), saved in full.
3. For each check: the expected result in `docs/REPRODUCE.md`, the result they got, and whether they match.
4. Every point where they hesitated, guessed or got stuck.
5. One sentence: "I followed the steps without help from the author" (true or false, and if false, what help was given).

## How I record it

I save their output unedited as `analysis/raw/semgrep_checks_A_to_F_REVIEWER_<date>.txt` and add a short audit note (who, date, independence, result, differences, fixes) to `docs/AUDIT_RECORD_A10.md` or a new audit record. Differences that expose a defect in the instructions are fixed in `docs/REPRODUCE.md` and listed in `docs/CORRECTION_HISTORY.md`. The gate "independent human re-run" changes from NOT DONE only after the record is in the repository.
