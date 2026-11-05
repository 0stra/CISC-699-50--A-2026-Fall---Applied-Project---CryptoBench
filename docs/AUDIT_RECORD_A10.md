# AUDIT_RECORD_A10.md

Audit of the Assignment 10 release candidate, 4 November 2026. Written by Claude (AI assistant) from the audit report and my instructions. I have read it but have not repeated the audit myself (see section 2).

## 1. What was audited

The release candidate "rc1" is commit `aeec71de620e5d8a000adbd79af4bd50ce929886` on `main`. The audited key result is the chain in `README.md` section 6: checks A, B, C and the new same-shape control D give the findings the claims register states (K3, K5, K8, and the reading in K4). Instructions under test: `README.md` and `docs/REPRODUCE.md` at that commit.

## 2. Reviewer and degree of independence

- **Reviewer.** A fresh Claude agent (AI) started with no knowledge of this project. It was told to read only `README.md` and `docs/REPRODUCE.md`, to work in an empty folder, and to fetch everything from the network. It ran in the same cloud environment that made the reference runs (Ubuntu 24.04.5, Python 3.13.16, Semgrep 1.181.0, 4 Nov 2026 01:03 UTC).
- **Independence: low.** Same AI family as the author of the instructions, same environment, same Semgrep version. It does show that the written steps are enough for a reader without project context; it does not show that a human on another machine would get the same result. It is not an independent replication.
- **Second check, by me (self-audit).** On 4 November 2026 (20:14 to 20:19 EST) I followed the steps on my MacBook (macOS 15.7.9, Semgrep 1.99.0) in a new empty folder and ran checks D and E twice each. Record: `analysis/raw/semgrep_checks_D_E_PERSONAL_2026-11-04.txt`. All seven hashes matched; D gave 1 finding at line 6; E gave 0 findings; repeat runs identical. Independence: I am the project owner, I had the expected values in front of me, and Claude supplied the commands and read my output files. It is a self-audit of two checks on a second machine and Semgrep version, not an independent replication. I did not rerun checks A, B and C in this audit (they were repeated earlier as P3, P4 and P5).
- **Problems met in my run.** My first attempt at D scanned a missing file because my repository copy was not updated; a pull was blocked by two untracked files. Both are recorded in the raw file. I also found that Semgrep 1.99.0 prints no `Findings: N` line; the instructions were changed.
- **Full report.** `analysis/raw/audit_REVIEWER_freshagent_2026-11-04.md` (verbatim; one comment line added).

## 3. Expected against observed

All values below are from the fresh agent's report.

- **Inputs.** The rules commit printed exactly `17e31e11ebac99fb7dfe1cd288f7a32151b6f3f9`. All five SHA-256 values matched. Line counts 361, 425 and 14 matched.
- **Check A.** Expected 1 finding at line 15. Observed 1 finding at line 15. Two runs identical.
- **Check B.** Expected 0 findings from 4 rules. Observed 0. Two runs identical.
- **Check C.** Expected 0 findings from 4 rules. Observed 0. Two runs identical.
- **Check D.** Expected 1 finding at line 6 only. Observed 1 finding at line 6, none on lines 10 to 12. Two runs identical.
- **Navigation of claim K8.** The README path (register, record, raw file, REPRODUCE check D, limits) worked, apart from the defects below.

## 4. Discrepancies, corrections and remaining limits

1. **Missing tag (real defect).** The README and register named tag `a10-rc1`, which did not exist on GitHub. My attempt to push a tag from the cloud session was refused by the connection. Fix: docs now name the commit hash for the audited version, and the final tag `a10-rc2` is created by me from my own computer. **Remaining:** until I create the tag, the commit hash is the only stable identifier. As of the commit that adds this record no tag exists on GitHub (`git ls-remote --tags origin` printed nothing).
2. **Part of K8 not reproducible from the steps (real defect).** The claim that the rule also finds nothing in `DigestUtils.java` and `DigestUtilsTest.java`, and that `Md5Crypt.java` uses the variable form at lines 259, 275 and 312, had no command. Fix: check E added to `docs/REPRODUCE.md` (fetch both files, hash-check, scan, and print lines 259, 275, 312 and 469). I ran the new check E steps myself in the same container: 0 findings on 2 files, the printed lines match. That re-test is by the author and is not independent.
3. **Vague wording (minor).** `WORK` and `REPO` were placeholders; output says `Findings: 1 (1 blocking)`, not `Findings: 1`; the working folder was implied; "tracked by git" message unexplained; reviewer file delivery unclear. All fixed in `docs/REPRODUCE.md`.
4. **Not testable by the reviewer.** Two machines and two Semgrep versions (K1, K6) were tested only in my earlier runs (R2, P3, P4, P5, and now P6 for checks D and E). The fresh agent used one machine and one version. This stays a limit for checks A, B and C in this audit.
5. **Semgrep 1.99.0 output differs (found by my run).** It prints no `Findings: N` line. Fixed in `docs/REPRODUCE.md`.

## 5. Quality-risk checks made for this assignment

- **Input integrity.** SHA-256 of every pinned input is stated and was re-verified by the fresh agent (5 of 5). The manifest (`docs/RELEASE_MANIFEST.md`) was generated by a script from the tracked files, so its hashes are not typed by hand.
- **Control shape (the leakage-like risk).** Check A used a positive control of the wrong code shape for the target (ISSUE-08). Check D adds a same-shape pair. Result: the zero on `Md5Crypt.java` is explained for this one rule. The other three rules were then probed one at a time (P7): each fires on its own test file, and `Md5Crypt.java` has no call they target. `DigestUtils.java` line 469 shows a second shape that the rule misses (L8). The reading is therefore narrowed in K4, not widened.
- **Repeatability and sensitivity.** Earlier runs: same findings on two Semgrep versions and two machines, each run twice (R2, P3, P4, P5). Not tested: other versions, other rules, other files. The second runs in two records are summarised ("same as A1") rather than printed in full; the diff results are stated. This is a limit on how much a reader can recheck from those records alone.
- **Provenance consistency.** Counts and line numbers in the claims register were compared with the raw records by search: line 15 appears in every check-A record (R2, P3, P5), "Ran 4 rules on 1 file: 0 findings" in every check B and C record, line 6 only in the check D record. I also found that on 31 October the attribution to Claude had been removed from `own_pass_1.md`, `docs/PROCEDURE_NOTES.md` and `journal/2026-10-31.md`, which made them understate AI help. These lines were restored in the release commit. Issue numbers (ISSUE-01 to ISSUE-10) were counted across all documents and used consistently.
- **Unsupported assumptions.** Claim K4 previously read as an explanation for all four rules; now limited to one. Claim K8 states that the control is synthetic and was run once by Claude (L7). Nothing is claimed about recall, precision or Java code in general.
- **Not checked.** The inventory template against the CycloneDX schema (L5). The provisional reference list against an independent pass (ISSUE-09). The Sonar plugin and the TLS scanner (not installed or scanned).

## 6. Access and restrictions during the audit

No restricted data, credentials or third-party endpoints were used. The reviewer fetched only public files. No TLS endpoint was scanned. See `README.md` section 7.

## 7. Evidence versions

- Audited: commit `aeec71de620e5d8a000adbd79af4bd50ce929886` ("rc1").
- Final (after fixes): see `README.md`; tag `a10-rc3`, created by me at the final commit (`a10-rc2` points to the earlier commit baa4134). The final commit hash is given in the Assignment 10 audit memo.
