# RELEASE_MANIFEST.md

Release candidate inventory, generated 4 November 2026 for Assignment 10 and regenerated 14 November 2026 for Assignment 11 and 19 November 2026 for Assignment 12 (generator output, then reviewed). Every tracked file except this one, with its SHA-256 and role. The stable evidence version is the git tag named in `README.md`. Files that are not in this list are not part of the release candidate. No restricted data, credentials or third-party code is stored in this repository.

Not in the repository on purpose: `Md5Crypt.java`, `StringUtils.java` and the Semgrep rules (public; fetched and hash-checked by `docs/REPRODUCE.md`).

Format of each line: path, SHA-256, role.

- `.semgrep.yml`  
  sha256 `7588848f6364e9561d175ff9292e129e90414697f39d4743f1b851524e451c8d`  
  Tool config; still names dead ruleset p/cryptography (ISSUE-06); not used by any run
- `README.md`  
  sha256 `b0e01b5bba6dd0f931668cb1c6d6603efb00e5efde4cb5f869f72e9c1ae5a088`  
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
- `analysis/raw/cyclonedx_schema_validation_REFERENCE_2026-11-19.txt`  
  sha256 `c3424af015b9d783a28a01af4cb7691ff0bb6827e08a3d33d017218ba9f47088`  
  Raw record: CycloneDX 1.6 schema validation of the candidate inventory, with negative control (check-jsonschema 0.39.0)
- `analysis/raw/semgrep_K4_variants_REFERENCE_2026-11-19.txt`  
  sha256 `16da81a31a92a6f8b294abe2ce7d1f30dbf4a38a9b1060534a27c94a92a4b5f2`  
  Raw run record: twelve K4 variants on the pinned rule, run by Claude (R4, Semgrep 1.186.0); expected outcomes committed before the run
- `analysis/raw/semgrep_TC1_Md5Crypt_2026-10-18.txt`  
  sha256 `a92c51c905f57e6936765b49265b4089e2265b5264a461030419ec5387e34b36`  
  Raw run record: run by Claude in container (R1)
- `analysis/raw/semgrep_TC1_mac_attempt_2026-10-18.txt`  
  sha256 `129382dc6db1488341b9395867c786e9615b877367a6924e65f6d8e14fedad3f`  
  Raw run record: laptop attempt typed by Claude Code (P1)
- `analysis/raw/semgrep_TC5_known_negative_PERSONAL_2026-10-21.txt`  
  sha256 `69393f18b3f3b14aa445a232e3806b2dfebdb83ca537536a8d79c18449e00507`  
  Raw run record: my own run on my MacBook
- `analysis/raw/semgrep_checks_A_to_F_PERSONAL_FRESHENV_2026-11-14.txt`  
  sha256 `edc5ac7e38f44d15e82148322480a6b9a5fa6f6e367cb96fac91eb4499d28884`  
  Raw run record: my own fresh-environment re-run of checks A to F in a Docker container, Semgrep 1.185.0 (P8); author re-run, not independent; includes the invalid first attempt
- `analysis/raw/semgrep_checks_A_to_F_REVIEWER_2026-11-19.txt`  
  sha256 `833e83b37565bd32ddf88036a5374ee6afcdf73f6eda00f47f7b3774e1bd3da9`  
  Raw run record: independent run by Gaurav Sharma with the helper script (terminal text, unedited)
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
- `analysis/results/claims_register_2026-11-05.md`  
  sha256 `e3466ec913a48c6b598e29099aa0895c8b0f115903cde08a3cc0367ec6386aeb`  
  Claims register v3: statuses added, L2 corrected
- `analysis/results/claims_register_2026-11-19.md`  
  sha256 `e0a44f48edc364dfdb21be4502e7d6adea4a8e2be8cbd2abccd74ef63e0659ca`  
  Claims register version 4 (K4 and K9 revised; K4 still provisional)
- `analysis/results/figure_10_k4_variants_2026-11-19.png`  
  sha256 `4a1c404cd256d4d83e87119707b47043527ce9566126b01eaee00618ef59abf8`  
  Figure 4 of the Assignment 12 thesis (twelve K4 variants); drawn by Claude
- `analysis/results/figure_1_proof_map.png`  
  sha256 `115e131ebda343cfdbedb18dbb3ab58ac3327941b00f6fc147eb5ae091530488`  
  Figure: claims to records
- `analysis/results/figure_2_zero_classification.png`  
  sha256 `50ac37f918f6e4b9963e7a061db79a92fc5e6d3a52636f749a1de16dfbbe1e97`  
  Figure: how a zero is classified
- `analysis/results/figure_3_rule_results_2026-11-05.png`  
  sha256 `d55260461dc1a62c09d85549bd37b2594dc55a7a09d2a2679d9bf66eefc3ef30`  
  Figure: findings per rule, own test file against Md5Crypt.java
- `analysis/results/figure_3_source.py`  
  sha256 `8a5c0590d3d3c9180b7bea24f762933a655fac4a3e2eac8214a00900aed4459f`  
  Script that draws figure 3 (numbers from P6 and P7)
- `analysis/results/figure_4_gate_status_2026-11-14.png`  
  sha256 `9ea120fe6f6d36a8a15e26ef43c9d23e83defe584a7eaa4113a5185035f86086`  
  Figure: gates set in advance and where each stands
- `analysis/results/figure_5_claim_record_map_2026-11-14.png`  
  sha256 `75d2d40d5848cf41829cf45826f0e003b5864a2afa0777cc3ae78bbc971f05c9`  
  Figure: claims to records with status (K1 to K9)
- `analysis/results/figure_6_zero_classification_2026-11-14.png`  
  sha256 `0d9deef026a8f049ee004755e566d673897123da3dfc553932e98202dd3d6dc2`  
  Figure: how the zero on Md5Crypt.java is classified (K8, K9)
- `analysis/results/figure_7_gate_status_2026-11-19.png`  
  sha256 `6fda13f4b2fa3c2eb6d90723ea0e6aaa32c3d561326d7a153ba7886555317e46`  
  Figure 1 of the Assignment 12 thesis (gate status); drawn by Claude
- `analysis/results/figure_8_claim_record_map_2026-11-19.png`  
  sha256 `53c5827686a9692daa79a5b8945007c9909cb78a6d5964175b390ca616cb102a`  
  Figure 5 of the Assignment 12 thesis (claim to record map); drawn by Claude
- `analysis/results/figure_9_zero_classification_2026-11-19.png`  
  sha256 `fd820bfb8a7cd503bdfea5bd76d975b5146bb5a0ada6a67eda91a7fe36fe0cef`  
  Figure 2 of the Assignment 12 thesis (classification of the zero); drawn by Claude
- `analysis/results/figures_a12_source.py`  
  sha256 `d4aed27fab89b2397806cca9c8dd45be791eedb77ccbeef96b76d1aa5c902a64`  
  Script that draws figures 1, 2, 4 and 5 of the Assignment 12 thesis; written by Claude
- `analysis/results/figures_thesis_source.py`  
  sha256 `3d602e75d2ac85906b7e7b174ded3c6f2f701cf91b1d405e2df5bb6a39e683de`  
  Script that draws figures 4 to 6 (facts from the claims register and logs)
- `analysis/scored/README.md`  
  sha256 `975fa9cc5d17847138b6595daaef1f6a6bc2889623f12fb804acdf6da2f74d8a`  
  Placeholder; no scoring yet
- `data/README.md`  
  sha256 `76afd2bb26d6e142999b19224b091530c64e3e8bd1e9716d5a8a6e5cf724552f`  
  Data folder note
- `data/reference_inventory/README.md`  
  sha256 `13ff39ef15e1d41de2ef20b8c540e1468aec7c36f23b0ffef68e0b2fbbf4ed2d`  
  Inventory folder note
- `data/reference_inventory/independent_pass_REVIEWER_2026-11-19.txt`  
  sha256 `0924b7ebd2a663d59e3f9312715065ba0a48665034c34c381452129b76c57060`  
  Independent source-pass list by Gaurav Sharma (unedited; line numbers do not match the pinned file)
- `data/reference_inventory/independent_pass_REVIEWER_annotated_copy_Md5Crypt_2026-11-19.java.txt`  
  sha256 `10d358121e01b32f210f36e5261fee9e05fc9edb395cf52b569b4319110c7c45`  
  His annotated copy of Md5Crypt.java (header line added; not the pinned file)
- `data/reference_inventory/independent_pass_comparison_2026-11-19.md`  
  sha256 `425bcc8a5c4f27522d219d5454ddd115e74ae12958550b19d12855e76f38a4b5`  
  Draft comparison by operation of the independent pass with candidate v1 (Claude; not yet reviewed by Nitin)
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
- `data/reference_inventory/reference_inventory_v1_candidate_2026-11-19.json`  
  sha256 `fa216520553f393ec294727c11e1e33a03e03a792a463f96be943b05a096f9cc`  
  Candidate reference inventory v1 (CycloneDX 1.6, 10 items, 53 lines); hashed, not frozen, not independent
- `data/test_material/README.md`  
  sha256 `8bd8fd9345dabd4fad18199154a30986e3524e541667108b4a71d256423ea254`  
  Selection criteria; holds only the control
- `data/test_material/k4_variants/README.md`  
  sha256 `5007588c9028478ed51a2266d764a0e79eaa8308177e2c7325ea6f72d26603cc`  
  Explains the twelve K4 variants (synthetic, Claude-written)
- `data/test_material/k4_variants/V00_chained_baseline.java`  
  sha256 `92a469203ba7070efbe3f5544d88ba149f892a1fc7097476c34bb6eba0c3bf05`  
  Synthetic Java variant for K4 (Claude-written; one code feature changed)
- `data/test_material/k4_variants/V01_variable_form.java`  
  sha256 `ff3f170cc6f610b2088d1fc730716953d7ac2a2fac7cea69a364657d4c7281e9`  
  Synthetic Java variant for K4 (Claude-written; one code feature changed)
- `data/test_material/k4_variants/V02_unprefixed_call.java`  
  sha256 `fba9d47c59ef5de0c9bae7f6dbb4621e3a972929c5d06c3b6c7b2b4f5acb11e8`  
  Synthetic Java variant for K4 (Claude-written; one code feature changed)
- `data/test_material/k4_variants/V03_fully_qualified_receiver.java`  
  sha256 `a15e82e51635eeb6670631c56000b5fd1b365a1050cafe824853b2222d8bee76`  
  Synthetic Java variant for K4 (Claude-written; one code feature changed)
- `data/test_material/k4_variants/V04_sha512_chained.java`  
  sha256 `365bbea08064e545b7d2a4debd770045328e9373494685af6326c8b7d4da90b5`  
  Synthetic Java variant for K4 (Claude-written; one code feature changed)
- `data/test_material/k4_variants/V05_chained_digest_no_args.java`  
  sha256 `cab8e3eee5bca870e70db7d30681b44390f44abcc010dc8661b23199f29324e7`  
  Synthetic Java variant for K4 (Claude-written; one code feature changed)
- `data/test_material/k4_variants/V06_chained_update_not_digest.java`  
  sha256 `c85992f7ca1c7028d1e1289068b1f9e6fa18a439d468fa01ed5b5931544aeca0`  
  Synthetic Java variant for K4 (Claude-written; one code feature changed)
- `data/test_material/k4_variants/V07_chained_across_lines.java`  
  sha256 `6c254476825e759cab8169c9cf1692d14b7c95ff379bbed7638890df67dc248d`  
  Synthetic Java variant for K4 (Claude-written; one code feature changed)
- `data/test_material/k4_variants/V08_parenthesised_call.java`  
  sha256 `e8554a680d63d1d5974ba397a691debfa68b2a1c987c3cb31d39654e53f8c68c`  
  Synthetic Java variant for K4 (Claude-written; one code feature changed)
- `data/test_material/k4_variants/V09_md5_static_helper.java`  
  sha256 `cf9ae67ed4d72ff0a275b26cfc1e249060d355ee816f955c9f64180c19319f20`  
  Synthetic Java variant for K4 (Claude-written; one code feature changed)
- `data/test_material/k4_variants/V10_md5Hex_helper.java`  
  sha256 `6e66a986fde85bf41ada68c2df5f2733e6005777c0b7997eeb67b4218b18473b`  
  Synthetic Java variant for K4 (Claude-written; one code feature changed)
- `data/test_material/k4_variants/V11_chained_result_assigned.java`  
  sha256 `f3849d67acf61d14d27d369a0eb07d9a5b752d850cf66f38d1221067df210494`  
  Synthetic Java variant for K4 (Claude-written; one code feature changed)
- `data/test_material/k4_variants/expected_outcomes.tsv`  
  sha256 `25ea3e95effdc971ce3375a197026d6408bb6380d28ecd8401f847b1b6ed5fa8`  
  Expected outcome per variant, committed before any run
- `data/test_material/same_shape_control/README.md`  
  sha256 `e02652358ceeee9f425a3fa911cdb463881ecf887f5a54400c1bed7d2312b5c1`  
  Control provenance and limits
- `data/test_material/same_shape_control/SameShapeControl.java`  
  sha256 `657e8eb1ac803fecb27dcbe7808781c5fd315a4981c7f33424645d25ae7c8539`  
  Synthetic 14-line control (written by Claude); not a sample
- `docs/AI_VALIDATION_LEDGER.md`  
  sha256 `a24a8a8ae7cf8c0f4dfc195f19d35417025dbf228c1a74a06d80cf93abb9ae9c`  
  What AI tools proposed, who checked it and how
- `docs/AUDIT_RECORD_A10.md`  
  sha256 `3a6e0a4f4562b8b0831d8dfc585c5ee2f6e6303613dd79e2337c4eca8ede1c00`  
  Audit of this release candidate
- `docs/CITATION_CHECK_2026-11-14.md`  
  sha256 `8fbf74705285357abd3996bad755fda5da18421bb0ee32f691702757bb5e4a6a`  
  AI check of each citation used in the thesis draft (not my own reading)
- `docs/CORRECTION_HISTORY.md`  
  sha256 `ee82dd0d180f65c499006a7cd9a4cee3b8b6705c57eb15a091a5b0dc90177165`  
  Corrections with commit hashes; pointer to earlier text
- `docs/CROSSCHECK_A12.md`  
  sha256 `0a3c59a2dbf6b63c812d2fd7c6d37c98893328d8ee405e0d4c67b1379f0dd0f5`  
  Cross-check of numbers, claims and figures across thesis, deck and evidence (Claude, not yet repeated by me)
- `docs/ENVIRONMENT.md`  
  sha256 `3123eeb41c04c4605f5ced2321441f77a79ebf8f18ea02b96786b48c5a018a5f`  
  Pinned versions, hashes, check results
- `docs/INDEPENDENT_REVIEW_RECORD_2026-11-19.md`  
  sha256 `eacf340d7b0429e4beadcdf8319a016047371e119cbf44dedfce6cd8bfe1b404`  
  Record of the independent run and source pass: what was received, statements, discrepancies, status
- `docs/INDEPENDENT_RUN_PACKAGE.md`  
  sha256 `38ffa8f5469eeb77fa42638405ab95e6cd262d5768f5b2426ea391f826ce1374`  
  Request text and record template for an independent human run (not yet done)
- `docs/INDEPENDENT_SOURCE_PASS_PACKAGE.md`  
  sha256 `e5ceeb2aab4e864d94722cfbd2cec745c8994866c5c55617f60e0eef786767f5`  
  Request and record template for an independent source pass (not yet done)
- `docs/INVENTORY_FREEZE_RECORD.md`  
  sha256 `3e23316cf36c6fd37cac5dd614ae3ebf5a4a2a772daa704cfe3a97773ed5f2f2`  
  Unit decision, candidate hash, why not frozen, what freezing requires
- `docs/ISSUE_LOG.md`  
  sha256 `afb48176bd2653d94c0e2ad114574b8046949fcfe66886959bc6869c8e37e70d`  
  Issues and risks
- `docs/K4_RULE_ANALYSIS_2026-11-19.md`  
  sha256 `12c3942c585da567bd9f236a17fdcd17af0f7024ed5d3a7cd406ec700730438d`  
  Matching conditions of the rule behind K4, twelve variants, what is and is not supported, my checklist
- `docs/PROCEDURE_NOTES.md`  
  sha256 `f95afa397619b8bf35eee1dc7f3f9101e44c4ca66148a7f626e50ec9b917068c`  
  Status, run labels, protocol rules, fallback rules
- `docs/REPRODUCE.md`  
  sha256 `fa595a23b4903e47fdebaeabd131bc7c49c3b21b2853a83c70f917911fe90429`  
  Step-by-step reproduction of checks A, B, C, D
- `docs/RESPONSE_LOG.md`  
  sha256 `02d1d1939ba07142d626fbc0df74de86fa7b08e9e1272cbc0c483ffe2112f37e`  
  Feedback item, change, location, unresolved issue
- `docs/RESPONSE_NOTE_A12.md`  
  sha256 `d9456a6abf49e5fa6357ffa2457eff04c69a898cfeaa59b8e5e23ee073f8fc81`  
  Response and remaining-work note, text version
- `docs/SOURCE_LEDGER.md`  
  sha256 `429c9f6a772e9988d45cc5a9462544527ab88cadc12b53e7c37d38139f7381bc`  
  Source of every result, figure, label, interpretation and citation, with verification status
- `docs/SPEAKING_OUTLINE_A12.md`  
  sha256 `144f7a37823e1c7b516a1905a792c9a683cf734569361f043fadeb9a466ea488`  
  Speaking outline for the deck
- `docs/SPEAKING_SCRIPT_A12.md`  
  sha256 `3a7392a3ea58aa214d5baa85569de8c462952d48ae2848417bd58216037b6197`  
  Nine-minute speaking script for the deck (written by Claude; not yet rehearsed by me)
- `docs/TAG_AND_MANIFEST.md`  
  sha256 `38dcffd8cee491a708bb0a3fe87af05b999a93eab776cd74b4b337766f726e22`  
  How tags and the manifest relate; manifest check; drift found and restored
- `docs/VERIFICATION_MATRIX_2026-11-19.md`  
  sha256 `725782981e7abf222b24be5f5f18afd5f24a0a5063d2784036180d037bb3eabb`  
  Literature claims linked to source, AI step and my verification (not yet done)
- `docs/WALKTHROUGH_SCRIPT_A12.md`  
  sha256 `3ae487b2fc446ba30f61c3cd6cc4ccfc10e8b6c919b249fb0e63135b17fb3c3c`  
  Script for the recorded walkthrough
- `docs/independent_run/SOP_FRIEND.md`  
  sha256 `70b6cf05552cbb68e75505d9bb4f57f9571b853d05d87b8a5c9928ae73d7da81`  
  One-page guide for the independent helper (source pass first, then the run)
- `docs/independent_run/cb_run.sh`  
  sha256 `01afcd8bb492c85b4c4736c1d46b10880c6e74e091f42f47a0c0fd2d1f06031b`  
  Helper shell script for the independent run: wraps the commands of docs/REPRODUCE.md, adds no analysis (written by Claude, tested once by Claude on Semgrep 1.186.0: 33 matched, 0 differed; test not filed as a record)
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
- `journal/2026-11-14.md`  
  sha256 `839e7fc289828c287efbf3bdd4e61b9d8676956b3616581ae171e61f7c4640a7`  
  Dated working entry
- `journal/2026-11-19.md`  
  sha256 `8b127f8d34052a7ed1456f1da554293e3993265881f3c3e4a7e974b695c1eae3`  
  Dated journal entry for Assignment 12
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
- `submission/A11/CryptoBench_11_Cover_Note_Revision_Plan.docx`  
  sha256 `0d02c8891aab05c2aa174bde8b689aaff310c4128f15b06a9fbe7544a3814ebe`  
  Assignment 11 submission copy (thesis draft or cover note); not part of the research record
- `submission/A11/CryptoBench_11_Cover_Note_Revision_Plan.pdf`  
  sha256 `a33c6d186eebe5341ca49c4aeb31668a3e45d55f927fb9746b142e1507f22566`  
  Assignment 11 submission copy (thesis draft or cover note); not part of the research record
- `submission/A11/CryptoBench_11_Full_Draft_Thesis.docx`  
  sha256 `b626904027df58897cbee396d4da2d795166e8bb36870a418eea9a77d7952400`  
  Assignment 11 submission copy (thesis draft or cover note); not part of the research record
- `submission/A11/CryptoBench_11_Full_Draft_Thesis.pdf`  
  sha256 `419443d7c67ba5e1cba4bd2b419f92b11cb2c112d2b43464fa209263e7475253`  
  Assignment 11 submission copy (thesis draft or cover note); not part of the research record
- `submission/A12/CryptoBench_12_NearFinal_Thesis.docx`  
  sha256 `225fc817d4d2ca83401f972a7aa3d23284bbc111682c05dfe3a67288a1fe3b93`  
  Assignment 12 submission copy (thesis or note); not part of the record at the cited commit
- `submission/A12/CryptoBench_12_NearFinal_Thesis.pdf`  
  sha256 `85bdcdde7197e702793b27fd4fe113668e440a5df62a7c009bfa531bb576aee8`  
  Assignment 12 submission copy (thesis or note); not part of the record at the cited commit
- `submission/A12/CryptoBench_12_Response_and_Remaining_Work_Note.docx`  
  sha256 `e88467db1f0de185af940d68fcaab02ce05158a8cef090c4904ec5b9ac3bf950`  
  Assignment 12 submission copy (thesis or note); not part of the record at the cited commit
- `submission/A12/CryptoBench_12_Response_and_Remaining_Work_Note.pdf`  
  sha256 `e2932789f53de00e1ccbb4bbf07e339c852c6d17a3b124550d14cc230dd566d6`  
  Assignment 12 submission copy (thesis or note); not part of the record at the cited commit
