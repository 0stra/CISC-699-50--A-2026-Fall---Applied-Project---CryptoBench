# RELEASE_MANIFEST.md

Release candidate inventory, generated 4 November 2026 for Assignment 10 (generator output, then reviewed). Every tracked file except this one, with its SHA-256 and role. The stable evidence version is the git tag named in `README.md`. Files that are not in this list are not part of the release candidate. No restricted data, credentials or third-party code is stored in this repository.

Not in the repository on purpose: `Md5Crypt.java`, `StringUtils.java` and the Semgrep rules (public; fetched and hash-checked by `docs/REPRODUCE.md`).

Format of each line: path, SHA-256, role.

- `.semgrep.yml`  
  sha256 `7588848f6364e9561d175ff9292e129e90414697f39d4743f1b851524e451c8d`  
  Tool config; still names dead ruleset p/cryptography (ISSUE-06); not used by any run
- `README.md`  
  sha256 `015f185bdec92d4983d44d980f99cd018a00ff8d583453268db90dceecba5bd0`  
  Research README (purpose, inventory, provenance, steps, restrictions, limits, navigation)
- `analysis/raw/README.md`  
  sha256 `8d11592f871323aa46944eefcab2757483494757d30e09903dff4b0b7d42dc9b`  
  Raw folder note
- `analysis/raw/TC2_template_roundtrip_PERSONAL_2026-10-21.txt`  
  sha256 `3b7ad19b8ec3573d365e93cbc510fe952b597774f72d8bbb31c749c5c9470b3d`  
  Raw run record: my own run on my MacBook
- `analysis/raw/audit_REVIEWER_freshagent_2026-11-04.md`  
  sha256 `d9e10dc5bc1e54ad3c7d4f12030b764cf2ed4cb58194d3f744b79c96c02657d5`  
  Verbatim report of the fresh-agent audit (AI reviewer, low independence)
- `analysis/raw/semgrep_TC1_Md5Crypt_2026-10-18.txt`  
  sha256 `a92c51c905f57e6936765b49265b4089e2265b5264a461030419ec5387e34b36`  
  Raw run record: run by Claude in container (R1)
- `analysis/raw/semgrep_TC1_mac_attempt_2026-10-18.txt`  
  sha256 `129382dc6db1488341b9395867c786e9615b877367a6924e65f6d8e14fedad3f`  
  Raw run record: laptop attempt typed by Claude Code (P1)
- `analysis/raw/semgrep_TC5_known_negative_PERSONAL_2026-10-21.txt`  
  sha256 `69393f18b3f3b14aa445a232e3806b2dfebdb83ca537536a8d79c18449e00507`  
  Raw run record: my own run on my MacBook
- `analysis/raw/semgrep_checks_D_E_PERSONAL_2026-11-04.txt`  
  sha256 `4d22cd0bdb7b7bf3e3635840d79006741b62ad72bc8d4f28aa688783029cd54f`  
  Raw run record: my own checks D and E on my MacBook (P6)
- `analysis/raw/semgrep_per_rule_PERSONAL_2026-11-04.txt`  
  sha256 `d1025935d69d444039b66b84a28d5daee836b80ca0d42ac8b6faf90fb9bbf6b4`  
  Raw run record: my own check F, the other three rules one at a time (P7)
- `analysis/raw/semgrep_pilot_official_rules_PERSONAL_2026-10-21.txt`  
  sha256 `1bd15911e40f6fec126ffa063ad0b8a5ead3dd0079f394b10c3ad389ead86702`  
  Raw run record: my own run on my MacBook
- `analysis/raw/semgrep_pilot_official_rules_REFERENCE_2026-10-21.txt`  
  sha256 `7d447b2b5c1356815a032e69224e7b221fd295e212d50320187e85faf7aa6cef`  
  Raw run record: run by Claude in container
- `analysis/raw/semgrep_rerun_PERSONAL_2026-10-31.txt`  
  sha256 `b946647bdb457b48e4902fe11e708e7c77bbe0983587a29f13f800c46990f353`  
  Raw run record: my own run on my MacBook
- `analysis/raw/semgrep_samshape_control_REFERENCE_2026-11-04.txt`  
  sha256 `adae4e3eee608e03f3312f7729c174044f59affe875235b53122fcf7cb6acfc7`  
  Raw run record: control run by Claude in container (R3)
- `analysis/results/claims_register_2026-10-29.md`  
  sha256 `edfefb65c11d57b3622f95125d3c45ca3c90606081c4d4decfdfc3cac5d0719c`  
  Claims register v1 (kept unchanged)
- `analysis/results/claims_register_2026-11-04.md`  
  sha256 `1195ae99e7285be7c622afa7589c76f0b20fc8b1c001196dc13f6bd02225b0fd`  
  Claims register v2 (kept unchanged)
- `analysis/results/figure_1_proof_map.png`  
  sha256 `115e131ebda343cfdbedb18dbb3ab58ac3327941b00f6fc147eb5ae091530488`  
  Figure: claims to records
- `analysis/results/figure_2_zero_classification.png`  
  sha256 `50ac37f918f6e4b9963e7a061db79a92fc5e6d3a52636f749a1de16dfbbe1e97`  
  Figure: how a zero is classified
- `analysis/scored/README.md`  
  sha256 `975fa9cc5d17847138b6595daaef1f6a6bc2889623f12fb804acdf6da2f74d8a`  
  Placeholder; no scoring yet
- `data/README.md`  
  sha256 `76afd2bb26d6e142999b19224b091530c64e3e8bd1e9716d5a8a6e5cf724552f`  
  Data folder note
- `data/reference_inventory/README.md`  
  sha256 `13ff39ef15e1d41de2ef20b8c540e1468aec7c36f23b0ffef68e0b2fbbf4ed2d`  
  Inventory folder note
- `data/reference_inventory/md5crypt_pilot_reference_list_2026-10-21.md`  
  sha256 `087e4eef8cbf95ef714f85ea31d457561b1c714cc5967a6f21ac0603bccfec0e`  
  Provisional nine-entry list, drafted by Claude; not independent (ISSUE-09)
- `data/reference_inventory/own_pass/agreed_lines.txt`  
  sha256 `731dfca930029e1bc8d4934256037c349a244f0f3b27dad3aa8099d2f0765447`  
  The 53 agreed line numbers
- `data/reference_inventory/own_pass/own_pass_1.md`  
  sha256 `70a15ead13c587155f2adf1759ff568bef934d9d2b0ae3b80a0a45572765ed6f`  
  My own pass 1 (not fully independent)
- `data/reference_inventory/own_pass/own_pass_2.md`  
  sha256 `8488a8644117c3d61a0a25bd41c0c375987d1f075b7c02973c941aead56f5954`  
  My own pass 2 (4 November)
- `data/reference_inventory/own_pass/own_pass_agreed.md`  
  sha256 `20725010499850f732455d55df74f3e404c8823676bf0d93a31c9f367bceddb9`  
  My agreed list and the three rules I applied (53 lines)
- `data/reference_inventory/own_pass/own_pass_vs_claude.md`  
  sha256 `a1b13737fd2c34d3eda8996a41084018cc626ea76a2cfa112dd2e2af77657a58`  
  Comparison of the agreed list with the provisional list (prepared by Claude)
- `data/reference_inventory/own_pass/p1_lines.txt`  
  sha256 `0990fc24885f080cd1e2e031a89793c7e0fd6be18f8fb58b8d455b883ea091f1`  
  Line numbers from pass 1 (60)
- `data/reference_inventory/own_pass/p2_lines.txt`  
  sha256 `08aa79c803a58cd6acc5f68e0933f958aef7e1295aa3cccf124eb2cde778e79b`  
  Line numbers from pass 2 (73, ranges expanded)
- `data/reference_inventory/reference_inventory_template.json`  
  sha256 `a851ef3d6547c6e75f728144f2e8b9575b0853f4e63a4f9b65c693ad89a2139d`  
  CBOM-style inventory template (JSON validity checked only)
- `data/test_material/README.md`  
  sha256 `8bd8fd9345dabd4fad18199154a30986e3524e541667108b4a71d256423ea254`  
  Selection criteria; holds only the control
- `data/test_material/same_shape_control/README.md`  
  sha256 `e02652358ceeee9f425a3fa911cdb463881ecf887f5a54400c1bed7d2312b5c1`  
  Control provenance and limits
- `data/test_material/same_shape_control/SameShapeControl.java`  
  sha256 `657e8eb1ac803fecb27dcbe7808781c5fd315a4981c7f33424645d25ae7c8539`  
  Synthetic 14-line control (written by Claude); not a sample
- `docs/AUDIT_RECORD_A10.md`  
  sha256 `3a6e0a4f4562b8b0831d8dfc585c5ee2f6e6303613dd79e2337c4eca8ede1c00`  
  Audit of this release candidate
- `docs/ENVIRONMENT.md`  
  sha256 `3123eeb41c04c4605f5ced2321441f77a79ebf8f18ea02b96786b48c5a018a5f`  
  Pinned versions, hashes, check results
- `docs/ISSUE_LOG.md`  
  sha256 `a5c497eb42285eef247d09339bf0af3388ea243350beafaa07faefa285243918`  
  Issues and risks
- `docs/PROCEDURE_NOTES.md`  
  sha256 `f95afa397619b8bf35eee1dc7f3f9101e44c4ca66148a7f626e50ec9b917068c`  
  Status, run labels, protocol rules, fallback rules
- `docs/REPRODUCE.md`  
  sha256 `fa595a23b4903e47fdebaeabd131bc7c49c3b21b2853a83c70f917911fe90429`  
  Step-by-step reproduction of checks A, B, C, D
- `docs/RESPONSE_LOG.md`  
  sha256 `155c0bc5610dee3502d1ac6cd99d8b8ca8d558369c00c73e589fbc3937ad1469`  
  Feedback item, change, location, unresolved issue
- `journal/2026-10-04.md`  
  sha256 `06ecf50518df0a89f4c105a29daa53345be056b51aee0349726f4caed6048041`  
  Dated working entry
- `journal/2026-10-18-test-case-1-mac-attempt.md`  
  sha256 `00fa3b2e66c603dc360aaeb0cf7d5863b730adbdb6d3e1e3890e385d39707e63`  
  Dated working entry
- `journal/2026-10-18.md`  
  sha256 `8fdb01809adf8f541217656baba458b74468a757e02582e17ada55fae8e1efcc`  
  Dated working entry
- `journal/2026-10-21.md`  
  sha256 `b23cf194e4891f466f87525635bb6253af4b744c9aefd846f0aaa36b17edd7ca`  
  Dated working entry
- `journal/2026-10-22.md`  
  sha256 `e3342388510975c3305eaee41ccaa0e285eb1dbd97327fbe64680bf55d63f940`  
  Dated working entry
- `journal/2026-10-29.md`  
  sha256 `0a23c2916aba4b4083248e42de9ba7be158db8827968a7df60e1388425c41112`  
  Dated working entry
- `journal/2026-10-31.md`  
  sha256 `1128a98e69ff26c14c81cbc9973e7a662feb5935c6020c2bebc7415a8641e09d`  
  Dated working entry
- `journal/README.md`  
  sha256 `1b819658a7d86afe71c422e8e9c7c10dc27ed6f101dd115b152a911cccbc0359`  
  Dated working entry
- `research/03_literature_requirements_brief.docx`  
  sha256 `079d31c0775f35bc1be8a20d08c799a707cd95cad8ea804d064c87a88bbedd6f`  
  Assignment 03 Literature and Requirements Brief, as submitted (copied from my computer, unedited)
- `research/04_design_review_package.docx`  
  sha256 `fcaa35e9fc9c66d3e077990d769e53e6dc97102db861f9aaf2a0dc6f488c9f50`  
  Assignment 04 Design Review Package, as submitted (copied from my computer, unedited)
- `sonar-project.properties`  
  sha256 `025dc6e6a69c0ecfc5f0b0e1b860e86db04c833e3822cb2b7746a4d174cf8d64`  
  SonarQube config; plugin not installed (ISSUE-01); nothing run
