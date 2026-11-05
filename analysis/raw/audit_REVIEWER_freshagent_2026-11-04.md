<!-- Verbatim report of a fresh Claude agent (AI, no prior context) that followed only README.md and docs/REPRODUCE.md at commit aeec71de620e5d8a000adbd79af4bd50ce929886, 4 Nov 2026. Not a human-independent replication. Only this comment line was added. -->

# Reproducibility audit report (audit-a10)

## 7. Statement (placed first for clarity)
I am an AI agent (Claude) given only the repository (commit aeec71de620e5d8a000adbd79af4bd50ce929886), README.md, docs/REPRODUCE.md and the audit rules. This is NOT a human-independent replication.

## 1. Environment
- OS: Linux 6.18.44-fc-v236 x86_64 (uname -a; "vm"). Python 3.13.16. Semgrep 1.181.0.
- Date/time UTC at start: Thu Nov 5 01:03:56 UTC 2026.
- Clone succeeded first time, no proxy problem. `git checkout aeec71de...` gave a detached HEAD at "Assignment 10 release candidate ...". The repo was not modified (git status clean).

## 2. REPRODUCE.md steps
Section 0: tools present (git, curl, sha256sum, Python 3.13.16 >= 3.8, semgrep 1.181.0 which is a recorded version). Network OK. REPO = /tmp/audit-a10/repo, WORK = /tmp/audit-a10/work.

Step 1: `git clone https://github.com/semgrep/semgrep-rules.git`; `git checkout 17e31e11ebac99fb7dfe1cd288f7a32151b6f3f9`; `git rev-parse HEAD` printed exactly 17e31e11ebac99fb7dfe1cd288f7a32151b6f3f9. Matches. (Step "mkdir WORK" is literal; I used my given folder.)

Step 2: ran the two curl -fsSL commands (rc=0 both) into ../ and `cp REPO/data/test_material/same_shape_control/SameShapeControl.java ../` (rc=0). Line counts via wc -l: 361, 425, 14 (match the stated counts).

Step 3: ran A, B, C, D each twice, with exactly the documented commands (cwd = semgrep-rules). Outputs saved at /tmp/audit-a10/work/out/{A,B,C,D}_{1,2}.txt; all exit codes 0. Details in section 4.

Step 4: `diff` of run 1 vs run 2 for each check: no differences at all (identical), including no timing/version line in this Semgrep version.

Step 5 (reading results) and 6 (what to record) are interpretive; I did not create files in analysis/raw/ (rules forbid modifying the repo). Step 7: nothing to run.

## 3. sha256 (step 2)
All five match the expected values exactly:
- Md5Crypt.java fa779456b25d2d36a6c464e200e106c2fa8e94a45dc608844ceb04407ea90747 - match
- StringUtils.java 6c44ebc7424c69fd04b6f3df10332934a149e6901fd29e86d96df4176527a99a - match
- SameShapeControl.java 657e8eb1ac803fecb27dcbe7808781c5fd315a4981c7f33424645d25ae7c8539 - match
- use-of-md5-digest-utils.java bd22fdb5ef195e383ec69aa9dbf1d0fd8f6cb5d41aef3f725f1aba5e5aa05908 - match
- use-of-md5-digest-utils.yaml a0614baf029418dd9b298713c3328f371faa1edb0eac7cc2c4a3a99ce1a220a5 - match

## 4. Checks
- A: "Findings: 1 (1 blocking)", one finding, line 15 (`byte[] hashValue = DigestUtils.getMd5Digest().digest(password.getBytes());`), summary "Ran 1 rule on 1 file: 1 finding." Matches expectation. Two runs identical.
- B: "Findings: 0 (0 blocking)", "Ran 4 rules on 1 file: 0 findings." Matches. Two runs identical.
- C: "Findings: 0 (0 blocking)", "Ran 4 rules on 1 file: 0 findings." Matches. Two runs identical.
- D: "Findings: 1 (1 blocking)", only line 6 (`return DigestUtils.getMd5Digest().digest(data);`), no finding on lines 10-12, summary "Ran 1 rule on 1 file: 1 finding." Matches. Two runs identical.

## 5. Discrepancies, ambiguities, guesses
No check failed. Items found:
1. Literal output differs trivially from the quoted "Expected: `Findings: 1`": the real line is "Findings: 1 (1 blocking)" (and "0 (0 blocking)"). Not a real mismatch; wording only.
2. Step 1.1 "`mkdir WORK`": WORK is a placeholder, never defined as a path; I had to substitute it. Likewise REPO. Minor.
3. Step 3 does not say explicitly "run from inside semgrep-rules", only implied by "You stay inside semgrep-rules". Fine but implicit.
4. Output says "Scanning 1 file tracked by git" although ../Md5Crypt.java etc. live outside any repo I created; harmless but the phrase is odd and undocumented.
5. Section 3's "Expected: ... Summary line" for the checks is satisfied, but "Findings: 1 ... line 15" is not printed as "Findings"; line number appears only in the code excerpt as "15┆". Minor.
6. Section 6 says to save records in `analysis/raw/` with REVIEWER label; this conflicts with the audit rule not to modify the repo (my constraint, not a doc fault); and it does not say how a reviewer should deliver such files back.
7. Tag mismatch: README says release candidate is git tag `a10-rc1`, and the claims register says "get it with `git rev-parse a10-rc1`". In my clone `git tag -l` printed nothing and `git ls-remote --tags origin` printed nothing, so the tag does not exist on the remote. The stable evidence version therefore cannot be resolved by tag; only the commit hash given to me identifies it. This is a real defect in the "stable evidence version" claim (see the output of the two commands above: empty).
8. REPRODUCE.md section 0 lists Python 3.8+ and Semgrep versions only as "recorded working"; I only tested 1.181.0 and one OS, so cross-version/machine claims (K1/K6, "two machines") are not something I could verify.
9. Check D line "no finding on lines 10 to 12" is verifiable from the output; but the README's explanation that Md5Crypt uses the variable form at 259, 275, 312 is not exercised by any command in REPRODUCE.md (the K8 claim also says the rule finds nothing in DigestUtils.java and DigestUtilsTest.java; those files are not fetched by REPRODUCE.md, so that part of K8 is not reproducible from the steps). I checked by eye that lines 259, 275, 312 of Md5Crypt.java contain `DigestUtils.getMd5Digest()` assigned to a MessageDigest variable (259: `final MessageDigest messageDigestMd5 = DigestUtils.getMd5Digest();`, 275: `MessageDigest altMessageDigestMd5 = DigestUtils.getMd5Digest();`, 312: `altMessageDigestMd5 = DigestUtils.getMd5Digest();`), consistent with the claim.
10. Check B/C use the file java/lang/security/audit/md5-used-as-password.yaml, which exists at the pinned commit; the other rule files also exist (scans ran 4 rules). No problem.
No step required guessing beyond items 2-3.

## 6. README navigation for claim K8
Followed README section 9: opened analysis/results/claims_register_2026-11-04.md, found K8 (line 97), its Records line (R3, 4 Nov, Claude container, Semgrep 1.181.0, not repeated by the student) and Files line (analysis/raw/semgrep_samshape_control_REFERENCE_2026-11-04.txt, the control file, its README). Opened the raw file: it contains the exact command, the fixture with line numbers, hash header, Semgrep version, rules commit, and output showing 1 finding at line 6; my D output matches it (apart from the displayed path: ../ctl/SameShapeControl.java there, ../SameShapeControl.java here, and blank-line formatting in the saved record). Step 3 (run matching check from REPRODUCE.md) worked: check D. Step 4 Limits L1, L7, L8 and ISSUE_LOG entries exist (ISSUE-02, ISSUE-07 seen). Navigation worked, with caveats: the K8 claim also covers DigestUtils.java/DigestUtilsTest.java which REPRODUCE.md does not reproduce (item 9), and the claims register's pointer to tag a10-rc1 fails (item 7). I did not open the L8 text, AUDIT_RECORD_A10.md or RESPONSE_LOG.md.

## 7. Statement
I am an AI agent given only the repository and these rules, so this is not a human-independent replication.
