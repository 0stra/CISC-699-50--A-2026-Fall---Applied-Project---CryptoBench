# Speaking script: CryptoBench feasibility pilot (about 9 minutes)

Read it slowly and pause at each slide change. Times are cumulative. Pronounce "CycloneDX" as "cyclone-D-X". If you run long, skip the sentences in brackets.

## Slide 1. Cover (0:00 to 0:30)

Hello. I am Nitin Prakash, and this is my thesis project, CryptoBench. I want to be clear from the first minute: this is a feasibility pilot. Only one of the three planned tools has run, on one file. Everything I say today is a claim from my thesis, and nothing here has been approved by my supervisor, Dr. Shaalan.

## Slide 2. Problem (0:30 to 1:15)

Organisations that want to move to post-quantum cryptography first need an inventory: where do we use cryptography today? Several free tools say they can discover it. There are code-scanning rules, a Sonar plugin, and TLS scanners. Published guidance says no single method is enough. But a practitioner has little evidence of what each tool catches and what it misses, measured against an answer key that someone built independently. My project was designed to produce that evidence.

## Slide 3. Literature and gap (1:15 to 2:15)

The literature gives me three things. Policy documents, such as the NIST draft on cryptographic discovery, say the need is real, but they describe tests and do not report results. CycloneDX and ECMA-424 give a format for writing an inventory down. And two recent papers, Cryptoscope and Crypsy, show that building an inventory with static analysis is feasible. Both are preprints, and both use benchmarks their authors built.

One result matters for my work. Crypsy scores 0.75, 0.86 or 0.95 on the same benchmark, depending on what you count. A score depends on the counting unit. [I have not yet read these papers myself; my verification table lists my reading plan.]

The gap is this: nobody has compared free, off-the-shelf methods from different layers against one independently built answer key.

## Slide 4. Research questions (2:15 to 3:00)

I had four questions. One: does the Semgrep procedure run and repeat? Answered, for one file. Two: what explains zero findings on a file that clearly makes MD5 digests? Answered in part, for one rule. Three: what does a reference inventory need? Not answered; I decided the unit and built a candidate, but it is not frozen. Four, the main question: how do three methods compare on coverage, false positives and effort? Not answered. Dr. Shaalan's feedback invited me to frame this as a Semgrep feasibility study. I have asked him to agree to that framing and have no reply yet.

## Slide 5. Method (3:00 to 3:45)

The design had three tools and a hand-built inventory. What I executed is narrower: four official Semgrep rules on one public file, Md5Crypt.java from Apache Commons Codec, with the commits and file hashes pinned. I ran controls: a positive control, a negative control, and a control that has the same code shape as the file I am testing. On 19 November I added twelve small test files that change one feature of the code at a time. No custom code and no custom rules.

## Slide 6. Evidence: the procedure repeats (3:45 to 4:45)

Here are the counts. The positive control gives one finding. The target file gives zero from all four rules. The negative control gives zero. The same-shape control gives one. This held on four Semgrep versions. I ran it, my AI assistant ran it, and on 19 November another person, Gaurav Sharma, ran it with a helper script. All 33 comparisons matched. I want to be careful about that third run: it is one person on one occasion, he used a script and not the document by hand, and what he told me about not using AI or help is relayed by me and not verified.

## Slide 7. Evidence: what the zero means (4:45 to 6:15)

This is the part my supervisor called the strongest, and he asked me to split it into three conclusions. One: the scanner ran. The controls support this. Two: one particular pattern did not match. The rule needs the call written as DigestUtils dot getMd5Digest, dot digest, in one expression. The file stores the digest object in a variable first. I tested this with twelve variants. For each, I wrote the expected result and committed it before running. All twelve came out as predicted. Three: the inventory contains an item that was not reported. That is not established, because the inventory is not frozen. So my claim about the zero stays provisional. The variants were written and run by my AI assistant, and I still have to read the rule file myself and re-run them.

## Slide 8. Evidence: the inventory (6:15 to 7:15)

Building the answer key turned out to be a measurement problem. My two manual passes marked 60 and 73 lines and disagreed on 39. After reconciling, 53 lines were agreed. I then grouped them into ten operation items, which are valid CycloneDX 1.6 and hashed. Only three of those ten are the call this rule is written to see. So a call-pattern rule reporting less than an inventory lists is partly not a miss at all. The inventory is not frozen. Gaurav also sent an independent list of operations. It mostly matches my items, but it has salt and prefix steps that mine lacks, and his line numbers do not match the file. I have not yet reviewed that comparison.

## Slide 9. Contribution (7:15 to 8:00)

So what is the contribution? A bounded method, not a benchmark result. First, a three-way reading of a zero: the scanner ran, a pattern did not match, or an inventory item is unreported. Second, controls and variants that match the shape of the code. Third, the observation that the unit of an inventory entry decides what it contains. Fourth, a trail from every claim to its raw record, with a status and a stated limit. I make no claim about how good any tool is, and none about post-quantum readiness.

## Slide 10. Limits and what is next (8:00 to 8:40)

The limits: one file, four rules, synthetic variants, an inventory that is a candidate, and one independent helper whose statements I cannot verify. Sonar and the TLS scanner have not started. By 22 November I will read the rule and re-run the variants myself, review the ten items against the independent list, clear a few open points with Gaurav, and read the papers. Only then will I freeze the inventory. After that, and with my supervisor's agreement, scored runs can be planned.

## Slide 11. AI use (8:40 to 9:10)

Last, AI use. My assistant, Claude, drafted text and figures, wrote and ran the twelve variants, and grouped the candidate inventory. I decided the unit of measurement, not to freeze the inventory, and the framing. I have not yet checked the rule, the papers or the grouping myself, and the thesis says so. The full log is Appendix B. Thank you. I am happy to take questions.

## If asked

- **Why not Sonar or TLS?** The plugin is not installed and no TLS target is authorised. I did not invent results.
- **Is the explanation of the zero established?** No, it is provisional until I read the rule and re-run the variants.
- **Why the operation as the unit?** The feedback pointed to assets or operations, and a line unit cannot be compared with asset-level tools. My supervisor has not confirmed the choice.
- **Who ran the twelve variants?** My AI assistant. I will re-run them myself.
