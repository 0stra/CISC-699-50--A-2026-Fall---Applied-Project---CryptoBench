# ENVIRONMENT.md

CryptoBench pinned environment record. Last updated 21 October 2026 (Hard Stop 4). Only values I have seen printed in a terminal or on screen are filled in. Anything not yet installed or checked is marked as such, not guessed.

## 1. My laptop (personal runs)

Source: `analysis/raw/semgrep_pilot_official_rules_PERSONAL_2026-10-21.txt`, checked on 21 October 2026, about 7:12 PM EDT.

- Machine: MacBook Pro
- Operating system: macOS 15.7.9 (build 24G830)
- Python: 3.8.2 (system Python)
- Semgrep: 1.99.0, installed in a virtual environment at `~/.semgrep-venv`. This is the newest Semgrep that supports Python 3.8. A direct `pip3 install --user semgrep` failed on this Mac (old pip 19.2.3, no Homebrew), which is why the virtual environment is used.
- Semgrep options used in every run: `--metrics=off` and `--disable-version-check`
- Known warning, harmless: NotOpenSSLWarning about LibreSSL 2.8.3
- Editor seen on 18 October: Visual Studio Code 1.142

## 2. Cloud container (reference runs by Claude, not my computer)

Source: `analysis/raw/semgrep_pilot_official_rules_REFERENCE_2026-10-21.txt` and `analysis/raw/semgrep_TC1_Md5Crypt_2026-10-18.txt`.

- Operating system: Ubuntu 24.04.5 LTS
- Python: 3.13.16
- Semgrep: 1.181.0
- Same options as above

## 3. Semgrep rules (pinned)

- Repository: https://github.com/semgrep/semgrep-rules
- Commit: `17e31e11ebac99fb7dfe1cd288f7a32151b6f3f9` (HEAD printed as "Merge pull request #4083 from semgrep/malaverdiere/fix-keyvault-timeadd-duration")
- Files used, unmodified: `java/lang/security/audit/crypto/use-of-md5-digest-utils.yaml`, `use-of-md5.yaml`, `weak-random.yaml` (same folder), and `java/lang/security/audit/md5-used-as-password.yaml`
- Registry rulesets are not used. `p/cryptography` and `p/crypto` return HTTP 404 (18 October, my Mac, ISSUE-06). The registry returned 403 in the container.
- `.semgrep.yml` in the repository root still names `p/cryptography`. It will be changed only after Dr. Shaalan confirms the replacement. Until then no run uses it.

## 4. Input files (pinned)

- Target: `Md5Crypt.java` from apache/commons-codec (Apache License 2.0), commit `f13dd50f566c318283c4138820b15d75c26a0217`, 361 lines
  - sha256: `fa779456b25d2d36a6c464e200e106c2fa8e94a45dc608844ceb04407ea90747` (same on my laptop and in the container)
- Positive-control file: `java/lang/security/audit/crypto/use-of-md5-digest-utils.java` from the rules commit above
  - sha256: `bd22fdb5ef195e383ec69aa9dbf1d0fd8f6cb5d41aef3f725f1aba5e5aa05908` (same on both machines)
- Known-negative file (check C): `StringUtils.java` from apache/commons-codec, same commit `f13dd50f566c318283c4138820b15d75c26a0217`, 425 lines, no cryptography words
  - sha256: `6c44ebc7424c69fd04b6f3df10332934a149e6901fd29e86d96df4176527a99a`
- The 18 October laptop copy of `Md5Crypt.java` came from the master branch with no commit recorded and was not hash-checked. It is not used for the 21 October results.

## 5. Commands

The exact commands for checks A and B are in the two raw files named above. They are not repeated here so there is one source of truth.

## 6. Results at this date (for the record)

- Check A (the MD5 DigestUtils rule on its own test file): 1 finding at line 15, exit 0. Container run twice, identical. Laptop run twice with separate outputs, identical (diff showed no differences).
- Check B (four official rules on `Md5Crypt.java`): 0 findings, exit 0. Container run twice, identical. Laptop run twice with separate outputs, identical.
- Check C (the same four rules on `StringUtils.java`, a file with no cryptography): 0 findings, exit 0, run twice on my laptop with separate outputs, identical. Run on 21 October before 10:02:46 PM EDT.
- Test case 2 (inventory template round-trip), on my laptop: passed on the third attempt (21 October 2026, 22:26 EDT). Attempt 1 failed (file not valid JSON), attempt 2 saved without my entry. Attempt 3: the copy parses, contains 1 cryptographic-asset entry, and differs from the original only by the added components block. Template sha256 `a851ef3d6547c6e75f728144f2e8b9575b0853f4e63a4f9b65c693ad89a2139d`, 25 lines, original unchanged. Checks JSON validity only, not the CycloneDX schema. See `analysis/raw/TC2_template_roundtrip_PERSONAL_2026-10-21.txt`.
- Laptop and container agree on both checks. Not tested on other rules.

## 7. Not yet installed or not yet recorded

- SonarQube: not installed. Version pairing with the Sonar Cryptography Plugin (RISK-01 / ISSUE-01) is untested.
- Sonar Cryptography Plugin: not installed.
- TLS scanner: not yet selected or installed. No endpoint is scanned until written authorisation is on file, or the service is one I own.
- Git version on my laptop: not recorded.

## 8. Verification log

- 21 October 2026: laptop rules commit confirmed with `git rev-parse HEAD`; file and fixture sha256 match the container values; checks A and B give the same findings on both machines.
- 21 October 2026 (night): check C run twice on my laptop; file sha256 recorded; `diff` showed no differences.
- 21 October 2026 (later): second laptop run of each check saved as A2 and B2; `diff` against the first outputs showed no differences.

## 9. SonarQube and plugin version window (from the design)

Restored from the Sprint I template on 29 October 2026 so the design constraint stays next to the version record. Releases of the Sonar Cryptography Plugin from 1.3.7 onward require SonarQube 9.9 LTS or later, and SonarQube 10.5.0 and above is documented to break the plugin's cryptography rules without an error. The installed SonarQube version must therefore fall from 9.9 LTS up to, but not including, 10.5.0. Neither tool is installed yet (see section 7), so no version is recorded.

## 10. Setup steps for a peer to reproduce this environment

1. Install the pinned Python and Git.
2. Install Semgrep at the version in section 1 or 2 and use only the unmodified rule files pinned in section 3. Add no custom rules.
3. Install SonarQube at a version inside the window in section 9 and confirm it starts.
4. Install the Sonar Cryptography Plugin at a version paired to that SonarQube version.
5. Install the TLS scanning tool.
6. Record every installed version in this file before running any method on real test material.

No step needs custom code: every tool is installed and configured, not written.
