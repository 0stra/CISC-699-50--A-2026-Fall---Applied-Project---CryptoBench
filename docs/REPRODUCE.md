# REPRODUCE.md

How to repeat the four Semgrep checks (A, B, C, D) on public inputs. Written 4 November 2026 for Assignment 10. Everything here uses public files and unmodified public rules. No credentials, no restricted data, no network scan.

What this reproduces: the pilot checks only. It does not reproduce any accuracy result, because none exists yet (see `README.md`, section "What is not here").

## 0. What you need

- A Linux or macOS terminal.
- `git`, `curl`, and a SHA-256 tool (`sha256sum` on Linux, `shasum -a 256` on macOS).
- Python 3.8 or newer and Semgrep. Recorded working versions: Semgrep 1.99.0 (macOS, Python 3.8.2) and Semgrep 1.181.0 (Ubuntu, Python 3.13.16). If you install a different Semgrep version, write it down. Findings may differ across versions (ISSUE-07).
- Internet access to `github.com` and `raw.githubusercontent.com`.
- A copy of this repository, because step 4 uses one file from it (`data/test_material/same_shape_control/SameShapeControl.java`). Call its location `REPO`.

Check Semgrep is installed: `semgrep --version` prints a version number.

## 1. Make an empty working folder and fetch the pinned rules

Use a new empty folder, outside `REPO`. `REPO` and `WORK` are placeholders for real folder paths you choose (for example `~/cb-repo` and `~/cb-work`).

1. Create the folder `WORK` (`mkdir -p ~/cb-work`) and `cd` into it.
2. `git clone https://github.com/semgrep/semgrep-rules.git`
3. `cd semgrep-rules`
4. `git checkout 17e31e11ebac99fb7dfe1cd288f7a32151b6f3f9`
5. `git rev-parse HEAD` must print exactly `17e31e11ebac99fb7dfe1cd288f7a32151b6f3f9`. If not, stop.

You stay inside the `semgrep-rules` folder for the rest of the steps, and run every command below from there. The commands use paths relative to it (`../` is `WORK`).

## 2. Fetch the two pinned Apache files and verify every file

1. `curl -fsSL -o ../Md5Crypt.java https://raw.githubusercontent.com/apache/commons-codec/f13dd50f566c318283c4138820b15d75c26a0217/src/main/java/org/apache/commons/codec/digest/Md5Crypt.java`
2. `curl -fsSL -o ../StringUtils.java https://raw.githubusercontent.com/apache/commons-codec/f13dd50f566c318283c4138820b15d75c26a0217/src/main/java/org/apache/commons/codec/binary/StringUtils.java`
3. Fetch two more pinned public files used by check E, from the same commit:
   - `curl -fsSL -o ../DigestUtils.java https://raw.githubusercontent.com/apache/commons-codec/f13dd50f566c318283c4138820b15d75c26a0217/src/main/java/org/apache/commons/codec/digest/DigestUtils.java`
   - `curl -fsSL -o ../DigestUtilsTest.java https://raw.githubusercontent.com/apache/commons-codec/f13dd50f566c318283c4138820b15d75c26a0217/src/test/java/org/apache/commons/codec/digest/DigestUtilsTest.java`
4. Copy the control file from your repository copy: `cp REPO/data/test_material/same_shape_control/SameShapeControl.java ../SameShapeControl.java` (replace `REPO` with the real path).
5. Compute the SHA-256 of each file and compare with the expected values:
   - `../Md5Crypt.java`: `fa779456b25d2d36a6c464e200e106c2fa8e94a45dc608844ceb04407ea90747` (361 lines)
   - `../StringUtils.java`: `6c44ebc7424c69fd04b6f3df10332934a149e6901fd29e86d96df4176527a99a` (425 lines)
   - `../DigestUtils.java`: `427fa77411e7a0ea7798151b199aa17892b7f1043ad7d26baf566d2d97e36347`
   - `../DigestUtilsTest.java`: `b886f74b8450318218366af7d486666de1e1a94945e81f3ba191ef36cbbda426`
   - `../SameShapeControl.java`: `657e8eb1ac803fecb27dcbe7808781c5fd315a4981c7f33424645d25ae7c8539` (14 lines)
   - `java/lang/security/audit/crypto/use-of-md5-digest-utils.java` (inside the rules clone): `bd22fdb5ef195e383ec69aa9dbf1d0fd8f6cb5d41aef3f725f1aba5e5aa05908`
   - `java/lang/security/audit/crypto/use-of-md5-digest-utils.yaml` (the rule, inside the rules clone): `a0614baf029418dd9b298713c3328f371faa1edb0eac7cc2c4a3a99ce1a220a5`
6. If any value differs, stop. The input is not the one the records describe.

## 3. Run the four checks

Every run uses the options `--metrics=off --disable-version-check`. Run each check twice and save the output to a file, so you can compare the two runs.

**Check A (positive control, rule author's own test file).**
`semgrep scan --metrics=off --disable-version-check --config java/lang/security/audit/crypto/use-of-md5-digest-utils.yaml java/lang/security/audit/crypto/use-of-md5-digest-utils.java`
Expected: the line `Ran 1 rule on 1 file: 1 finding.` is printed (Semgrep 1.181.0 also prints `Findings: 1 (1 blocking)` in the summary box; 1.99.0 does not), the finding excerpt is marked `15┆`, and the summary line reads `Ran 1 rule on 1 file: 1 finding.`

**Check B (four official rules on the target file).**
`semgrep scan --metrics=off --disable-version-check --config java/lang/security/audit/crypto/use-of-md5-digest-utils.yaml --config java/lang/security/audit/crypto/use-of-md5.yaml --config java/lang/security/audit/crypto/weak-random.yaml --config java/lang/security/audit/md5-used-as-password.yaml ../Md5Crypt.java`
Expected: `Ran 4 rules on 1 file: 0 findings.` (1.181.0 also prints `Findings: 0 (0 blocking)`).

**Check C (known negative, same four rules on a file with no cryptography).**
The same command as check B, with `../StringUtils.java` as the last argument.
Expected: `Ran 4 rules on 1 file: 0 findings.`

**Check D (same-shape control, added 4 November 2026).**
`semgrep scan --metrics=off --disable-version-check --config java/lang/security/audit/crypto/use-of-md5-digest-utils.yaml ../SameShapeControl.java`
Expected: the excerpt is marked `6┆` (`return DigestUtils.getMd5Digest().digest(data);`), and there is no finding on lines 10 to 12. Summary line: `Ran 1 rule on 1 file: 1 finding.`

**Check E (the same rule on two more public files, and the shape of Md5Crypt.java).**
`semgrep scan --metrics=off --disable-version-check --config java/lang/security/audit/crypto/use-of-md5-digest-utils.yaml ../DigestUtils.java ../DigestUtilsTest.java`
Expected: `Ran 1 rule on 2 files: 0 findings.` Then show the three lines of `Md5Crypt.java` that the claims refer to: `sed -n '259p;275p;312p' ../Md5Crypt.java`. Expected: each line assigns `DigestUtils.getMd5Digest()` to a variable (the variable form), at lines 259, 275 and 312. `DigestUtils.java` line 469 holds `getMd5Digest().digest(data)` without the `DigestUtils.` prefix (`sed -n 469p ../DigestUtils.java`), a second shape the rule does not match (claims register L8).

The line `Scanning 1 file tracked by git` can appear even though the files are outside any repository you made; it is Semgrep's wording and not a problem. Semgrep may print a warning about LibreSSL on macOS (harmless) and a "Scan Status" box. These are not findings.

**Check F (the other three rules, one at a time).**
For each of `crypto/use-of-md5`, `crypto/weak-random` and `md5-used-as-password` (folder `java/lang/security/audit/`): run the rule on its own official test file, then on `../Md5Crypt.java`, with the same options as above, e.g. `semgrep scan --metrics=off --disable-version-check --config java/lang/security/audit/crypto/use-of-md5.yaml java/lang/security/audit/crypto/use-of-md5.java`. Then run `grep -c getInstance ../Md5Crypt.java`.
Expected on the rule's own test file: use-of-md5 = 3 findings (lines 7, 15, 29); weak-random = 3 (lines 48, 51, 165); md5-used-as-password = 1 (line 41). Expected on `Md5Crypt.java`: 0 findings for each rule, and the `getInstance` count is 0.

## 4. Compare the two runs of each check

Save the first and second output of each check to separate files and run `diff` on them. Expected: no differences. Note that Semgrep output may contain a timing or version line in some versions; if `diff` shows only such a line, record it.

## 5. How to read the results

- Check A passing shows the rule works on the code shape it describes.
- Check C returning 0 shows the rules do not fire on a file with no cryptography.
- Check B returning 0 on `Md5Crypt.java`, which does use MD5, is a miss by these four rules. It is not evidence that the file is safe.
- Check D explains the miss: the rule finds the chained form and not the variable form. `Md5Crypt.java` uses the variable form (lines 259, 275, 312).
- Check D is one rule and two shapes made for this purpose. It says nothing about how common either shape is, or about other rules.

- Check F shows each of the other three rules works on its own test file and has no matching call in `Md5Crypt.java` (it has no `getInstance`, and `Random` appears only as a type). That is a different cause from check D.
- Check E shows the 0 findings on the two Apache files and lets you see the two shapes yourself.

## 6. What to record

For each run: who ran it, the date, the Semgrep version (`semgrep --version`), the operating system, the rules commit, the sha256 values from step 2, the exact command, the output, and any difference from the expected result above. Name files with `REFERENCE` (run by Claude), `PERSONAL` (run by the student) or `REVIEWER` (run by someone else), plus the date. The project owner puts them in `analysis/raw/`; a reviewer who cannot write to the repository sends the files to the owner or attaches them to the review.

## 7. Not reproducible from this repository

- The Sonar Cryptography Plugin and SonarQube: not installed, so there is nothing to run (ISSUE-01).
- The TLS scanner: not selected. No endpoint has authorisation on file (RISK-05). Do not scan any endpoint to "reproduce" this project.
- The reference inventory: only a provisional list and one partial own pass exist (ISSUE-09). No frozen answer key exists, so no recall or precision can be computed.
