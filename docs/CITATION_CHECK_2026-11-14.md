# CITATION_CHECK_2026-11-14.md

Check of the citations used in the Assignment 11 thesis draft, made on 14 November 2026 by Claude (AI assistant), which fetched each source's publisher, repository or standards-body page. **I (Nitin) have not yet opened these papers myself.** This is an AI check against source pages, not my own reading. It does not make any citation "validated by me". My confirmation step is listed at the end.

Check words: **Confirmed** (the page shows the stated title, authors, venue and year), **Partly confirmed** (the item exists, but a detail could not be seen), **Not used** (a statement in my earlier work could not be confirmed, so the draft does not use it), **Not rechecked** (carried from an earlier assignment; I read the primary source then, nothing new was checked now).

## Peer-reviewed and preprint literature

- **Amann, Nguyen, Nadi, Nguyen and Mezini (2019), IEEE Transactions on Software Engineering 45(12).** The arXiv abstract (1712.00242) confirms the title, the five authors and the finding that existing detectors "suffer from extremely low precision and recall" on the authors' benchmark; its method includes original-author validation. The IEEE page could not be fetched, so volume, pages and DOI come from my Assignment 04 list and are Partly confirmed. **Not used:** my Assignment 04 text puts the words "collapse dramatically" in quotation marks and attributes them to this paper. They do not appear in the abstract and I could not find them. The draft uses the abstract's wording only.
- **Ami et al., "Mutation-based Evaluation of Cryptographic API Misuse Detectors", ACM Transactions on Privacy and Security (2026).** The NSF Public Access Repository record names the title and the journal, and its abstract describes MASC, 14 detectors in total (nine from a 2022 study plus five), and six new undocumented flaws in the extended study. That page leaves the author, date and DOI fields blank, and the publisher page for DOI 10.1145/3796221 could not be fetched. So the venue is Confirmed; the year, the author list and the DOI are **not yet confirmed**. The draft cites the venue and writes the year as "2026, to be confirmed".
- **Ami et al. (2022), arXiv:2107.07065.** The abstract confirms the MASC framework, nine detectors and 19 undocumented flaws. The authors and venue were not shown in the fetched text, so the draft cites it as an arXiv preprint (Partly confirmed). **Not used:** my Assignment 04 sentence about "MUBench on fifteen detectors, nine of them crypto detectors [Ami et al., 2024]" could not be traced to any source.
- **Näther and Hirsch (2026), "Hidden Ciphers and Where to Find Them", arXiv:2608.04857.** Confirmed: title, authors, submission date (5 August 2026). The full text names the scanner Crypsy and the synthetic benchmark Cryben, reports an occurrence-level discovery F1 of 0.75 (precision 0.87, recall 0.66) over 197 ground-truth occurrences, 0.86 when 43 by-design counting differences are excluded, and 0.95 at component granularity (48 components), with a ground truth described as a CycloneDX v1.7 CBOM built independently of Crypsy. **Correction to my Assignment 04 list:** it said "author(s) withheld"; the authors are now known. This is a preprint, not peer reviewed.
- **Moffie et al. (2025), "Cryptoscope: Analyzing cryptographic usages in modern software", arXiv:2503.19531.** Confirmed: title, IBM Research authors, abstract (92% of test cases give asset views including related material; 11 of 15 weaknesses detected in the CamBench benchmark). The fetched page showed no submission date; the year 2025 comes from the arXiv identifier. A preprint, and the results are the authors' own.

## Method and pilot-study literature

- **Cronbach and Meehl (1955), "Construct validity in psychological tests", Psychological Bulletin 52, 281-302.** Confirmed from the reprint at Classics in the History of Psychology (title, authors, journal, volume, pages, year; the issue number, 4, is from memory, not from that page). Confirmed use: construct validity is investigated when no criterion is accepted as fully defining the quality measured.
- **Lancaster, Dodd and Williamson (2004), Journal of Evaluation in Clinical Practice 10(2), 307-312.** Confirmed (Lancaster University record).
- **Eldridge et al. (2016), PLoS ONE 11(3), e0150205.** Confirmed (DOAJ record, DOI 10.1371/journal.pone.0150205): pilot studies are a subset of feasibility studies, and the authors recommend labelling each type clearly.
- **Thabane et al. (2010), BMC Medical Research Methodology 10, article 1.** Title, journal and year Confirmed (DOAJ record; DOI 10.1186/1471-2288-10-1 seen in a result link). The author list and volume are from memory and Partly confirmed.
- All four come from clinical research. The draft uses only the general principle (a pilot tests whether a procedure can work; it does not estimate effects).

## Standards and official documents

- **NIST IR 8610, second round of the additional digital signature schemes (14 May 2026).** Confirmed. First author is Alagic (not Moody, as my Assignment 03 list said; Moody is among the authors). Nine candidates advanced: FAEST, HAWK, MAYO, MQOM, QR-UOV, SDitH, SNOVA, SQIsign, UOV.
- **NIST Round 3 additional signatures page.** Lists nine candidates and states that the HAWK submission team has withdrawn HAWK. The page (updated 13 October 2026) gives no withdrawal date. The date "29 July 2026" in my Assignment 04 list is **not confirmed** and is not used.
- **ECMA-424, 2nd edition (December 2025).** Confirmed: defines the CycloneDX v1.7 specification and includes modelling for cryptographic artefacts. The page does not use the word "CBOM".
- **NIST SP 1800-38 (draft), published 19 December 2023.** Confirmed as a preliminary draft; the page says Volume B covers cryptographic discovery (a test plan, a use case, threats, a starting approach and an architecture). The exact title of Volume B differs between my Assignment 03 and 04 lists and from the NIST page title ("Migration to Post-Quantum Cryptography: Preparation for Considering the Implementation and Adoption of Quantum Safe Cryptography"), so the draft cites the NIST page title and the volume letter.
- **NIST SP 800-230 initial public draft (2026).** A NIST page and news item exist; only its existence was checked. The draft does not rely on its content.

## Not rechecked in this check

CISA, NSA and NIST "Quantum-Readiness: Migration to Post-Quantum Cryptography" (August 2023); OMB M-23-02; NSM-10; CISA "Strategy for Migrating to Automated Post-Quantum Cryptography Discovery and Inventory Tools" (my Assignment 03 gives August 2024; the month should be checked); FIPS 203, 204 and 205 (13 August 2024); NIST's HQC selection (11 March 2025) and NIST IR 8545; the NCCoE project and workstream pages; the Semgrep rules repository; the Sonar Cryptography Plugin repository; Apache Commons Codec. In the thesis these carry the mark "‡".

## What I must do next

I open each paper or page above that carries "†" in the reference list, read the passage the draft relies on, and write one line here per item: opened (date), says what the draft says (yes or no), correction. Until then the status of every citation is "checked by an AI against a source page; not yet read by me".
