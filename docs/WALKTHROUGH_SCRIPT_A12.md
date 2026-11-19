# Walkthrough script for the recorded explanation, Assignment 12

Target length 8 minutes (suggested range 6 to 10). Read in your own words. Screen: the thesis PDF, then the repository, then the deck. Record only after you have opened each file named here, so what you say is what you have seen. Where I wrote “I have not yet” it is true today; change it only if you have done the step.

**0:00 to 0:45. What this package is.** “This is Assignment 12 for CryptoBench. It is a feasibility pilot. Only Semgrep ran, on one file. The comparison with the Sonar plugin and a TLS scanner has not been run, and the thesis says that in the abstract.” Show the title page and abstract.

**0:45 to 2:15. What changed since the Assignment 11 feedback.** Open `docs/RESPONSE_LOG.md` entries H1 to H5. “Dr. Shaalan gave five priorities. For each I record the change, where the evidence is and what is unresolved.” Say the dispositions: H1 partly completed, the inventory is a candidate and not frozen; H2 partly completed, K4 stays provisional; H3, the independent run is pending; H4, the framing is narrowed, subject to his agreement; H5, my reading of the sources is pending.

**2:15 to 4:15. Claim to thesis to evidence.** Take K4. Open thesis §4.3, then Figure 3, then evidence EV-17 (raw output) and EV-19 (expected outcomes committed before the run, commit 45f6180). “Twelve variants, twelve outcomes as predicted. The rule needs the chained call; the Md5Crypt calls are stored in a variable.” Then name the three conclusions and say the third is not established because the inventory is not frozen. Open `docs/K4_RULE_ANALYSIS_2026-11-19.md` and say that Claude wrote it and ran the variants and that I have not yet read the rule or re-run them.

**4:15 to 5:15. The inventory.** Open `data/reference_inventory/reference_inventory_v1_candidate_2026-11-19.json` (EV-21) and `docs/INVENTORY_FREEZE_RECORD.md`. “Ten operation items, 53 lines, valid CycloneDX 1.6 with a negative control, hash fa216520. Claude grouped them; I have not reviewed the grouping. It stays a candidate until an independent person has read the source.”

**5:15 to 6:30. The deck narrative.** Show the deck slides 2 to 9 quickly, naming the problem, the gap, the questions, the method, the evidence and the contribution. Say that the deck makes no claim stronger than the thesis, and show `docs/CROSSCHECK_A12.md`.

**6:30 to 7:30. Remaining work.** Read the list in the response note: my own reading of the rule and re-run of the variants (20 November), review of the grouping (21 November), the independent run and source pass (requested, due 22 November), reading the papers, agreeing the framing with Dr. Shaalan, freezing only after the independent pass.

**7:30 to 8:00. AI.** “Claude drafted text and figures, wrote and ran the variants and grouped the inventory. I decided the unit, no freeze and the framing. Appendix B lists each step and what I have not yet verified.”
