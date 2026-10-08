# Final thesis: independent pre-submission review and improvement plan

Review date: 1 October 2026. Repository baseline: `35df731`. Requested scope: review the completed project; prioritise defensible writing, provenance, references and presentation without rerunning models or changing the frozen experiment. This report does not implement thesis corrections.

## 1. Overall judgement

**I would not recommend submitting this exact version yet.** The project has a credible, bounded MPhil-level systems investigation, useful negative recommendation results, and a substantial reproducibility record. However, several statements about how the experiment was constructed or evaluated conflict with its own artifacts. These are more consequential than whether the prose sounds AI-assisted. Substantial pre-submission reporting revisions are warranted; this is an editorial judgement, not an institutional examination outcome or prediction of rejection.

The most important issues are:

1. The thesis describes the rule base as manually curated and denies automatic rule authoring, whereas the released records explicitly document bounded model enrichment.
2. The discussion reports citation precision and coverage that cannot be reconstructed from the final verifier schema; one denominator exceeds the final Rule-RAG claim population.
3. The NDCG equation describes standard multi-positive NDCG, but the released results and release audit use a first-relevant-item discounted score.
4. The explanation of UIFR eligibility omits a restrictive lexical gate that excludes many assertions containing information absent from the supplied facts.
5. The claim that validation selected the final weights conflicts with configuration identifying those weights as fixed and the Pareto analysis as descriptive.
6. The document still contains candidate/declaration placeholders and presentation defects.

These issues do **not** establish plagiarism or misconduct. They do require correction before an examiner is asked to trust the methodological account. Do not conceal a discrepancy simply because results are frozen. Preserve the results and accurately describe their actual provenance, calculation and limits.

### Integrity conclusions, carefully bounded

- All 28 consolidated bibliography entries correspond to identifiable real underlying works. This is not a hallucinated bibliography as a whole. One has an incorrect title and first-author initial; another has an invalid DOI-form link; a book DOI is registered but its destination failed.
- All 28 consolidated entries are cited somewhere in the final thesis. No genuine undefined numeric citation was found. This does not mean every citation supports every associated sentence.
- No specific instance of copied third-party prose was confirmed by the limited public-source and exact-overlap checks below. **This is not a plagiarism clearance or similarity percentage.**
- Authorship cannot be determined from the prose. There are repetitive, template-like editorial features, but they are not proof of AI generation. The documented model enrichment of the KB is a concrete disclosure issue, unlike subjective writing impressions.
- Most priority corrections can be made from existing artifacts and honest disclosure. New generation, retraining and a redesigned evaluator are not prerequisites to making the thesis substantially more accurate.

## 2. What was reviewed, and what remains unverified

Reviewed all five chapter Markdown sources, front matter, consolidated references and assembled Markdown; examined the 69-page PDF's text and selected rendered pages, including pages 4, 27, 43 and 52. Inspected DOCX XML for structural issues, not a complete visual rendering in Microsoft Word. The assembled Markdown matched the current builder's assembly of the sources at review time.

Cross-checked relevant claims against `configs/experiment.yaml`, the release configuration and prompts, KB records/source registry, saved rankings, explanations, extractions, verifications, record metrics, paired contrasts and release manifests. Inspected assessment, analysis and release-audit code. Read-only arithmetic checks used existing saved data; no models were called and no release artifacts were rewritten.

Checked the existence and bibliographic metadata of all 28 cited works using primary publication sites, DOI registration metadata and accessible papers. Downloaded and text-compared 17 accessible primary papers. Investigated claim-to-source fit at important citation sites. This was **not** an exhaustive sentence-by-sentence semantic verification against the full text of every cited work: some publisher access was blocked, and some checks establish metadata rather than full claim entailment.

Checked all 39 KB source URLs for reachability. That establishes neither endorsement of all 200 derived rules nor independent validation of each rule's full content. External pages are mutable. Access statuses below describe this review, not permanent guarantees.

No Turnitin/iThenticate institutional database, private student-submission corpus, reliable authorship test, supervisor's records, authenticated doctoral-school guide or complete human-labelled assessment was available. No full thesis was uploaded to a third-party checking service. Short quoted phrases were used in public web searches. This report itself is AI-assisted review, not a certificate from a human examiner or the university.

## 3. Priority definitions and safeguards for future fixes

- **P0 — resolve before submission:** factual reporting contradictions, unsupported statistics, inaccurate provenance and submission placeholders.
- **P1 — important revision:** narrow interpretations, strengthen source attribution and make the thesis independently understandable.
- **P2 — presentation/depth:** improve clarity, navigation, synthesis and formatting.
- **Future work:** new experiments or altered evaluators; keep separate from the current reporting correction.

For a later implementation pass: edit chapter/front-matter sources, then regenerate the assembled thesis and exports. Do not independently edit only the generated PDF, DOCX or consolidated Markdown. Do not change prompts, labels, rankings, weights, splits, the KB or frozen release files to make the narrative look consistent. Never invent author actions, manual validation, ethics approval, source reading, preregistration or model details. Ask the candidate for missing historical facts. If a finding cannot be resolved from evidence, state the uncertainty rather than filling it with plausible prose.

## 4. Detailed findings and acceptance criteria

### F01 — P0: Correct knowledge-base provenance and AI-use disclosure

**Locations:** abstract/front matter; Chapter 3 §3.6.1; Chapter 5 §5.8.3; related source-grounded/manual-curation claims throughout.

**Evidence:** `data/kb/fashion_rules.csv` contains 200 records whose `source_validation_status` includes `verified_reachable_2026-08-21_plus_bounded_model_enrichment`. The evidence summaries and limitations explicitly distinguish source support from model enrichment. For example, K001 distinguishes source-backed jeans versatility from enriched occasion, colour and layering alternatives. This is incompatible with an unqualified account of solely manual construction and the sentence saying the project did not use automatic rule authoring.

The registry contains 39 sources from six editorial outlets. Rule-source attribution counts are Vogue 126, British Vogue 20, Who What Wear 23, GQ 19, British GQ 10 and MasterClass 2. The records classify 198 as fashion editorial and 2 as education editorial, with medium reliability. These are styling heuristics, not professionally certified or experimentally established fashion laws.

**Fix without rerun:** describe the documented construction as source-linked rules with bounded model enrichment; distinguish the supported core from extended conditions. Establish who assembled, enriched and checked the rules, and which model/process was used, only from surviving records or the candidate's confirmed account. Explain whether the candidate inherited a supplied KB. Disclose actual AI assistance in writing, code and KB preparation according to the applicable research-degree requirements. Do not assume enrichment means every rule was wholly machine-authored.

**Acceptance:** abstract, methods, limitations and declaration no longer contradict record-level provenance. No claim that all rule text is entailed by the linked source. A reader can distinguish source authorship, rule authoring, enrichment and validation.

### F02 — P0: Remove or substantiate the citation statistics

**Locations:** Chapter 3 §3.12.3; Chapter 5 §5.3.3 and RQ3 conclusions.

The discussion reports 87.5% precision (21/24) and 0.23% coverage (19/8,275). No current calculation or final artifact was identified that supports these populations. The final claim-verification schema does not contain the per-claim supporting-rule IDs or support-required labels needed for the described intersection-based calculation. Accepted final Rule-RAG records contain **8,075 claims**, so 8,275 cannot be a subset of that final population.

Final accepted claim-level citation-entailment labels are:

| Condition | Entails | Does not entail | Not applicable | Total |
|---|---:|---:|---:|---:|
| Rule-RAG | 1,820 | 5,502 | 753 | 8,075 |
| No-RAG | 0 | 0 | 8,729 | 8,729 |

These counts describe saved labels, **not automatically citation-relation precision or coverage**. A claim, a citation marker and a claim–rule relation are different units. Do not replace the old precision with `1820 / (1820 + 5502)` without establishing and naming the appropriate unit.

**Fix without rerun:** locate an authentic derivation tied to the final data, if one exists; otherwise remove the unsupported precision/coverage numbers and the incompatible formula description. Report only defensible saved-label descriptives, with population and unit explicit. If historic numbers are retained for some reason, label them nonfinal and explain their provenance; they should not underpin the final RQ answer. Move final empirical citation results into Chapter 4 before interpreting them in Chapter 5. Do not attribute all failures to the generator: extraction, claim–citation association and verifier error remain possible.

**Acceptance:** every reported numerator and denominator maps to identifiable final records and an executable definition; no unsupported 8,275 denominator; no newly invented relation-level annotations.

### F03 — P0: Reconcile the NDCG definition with the released score

**Locations:** Chapter 3 Equation 3.9; recommendation tables and interpretation; `scripts/audit_final_release.py:recommendation_means`; `src/evidence_fashion/reranking.py:ranking_metrics`.

The equation and core ranking function implement standard DCG/IDCG over relevant items. The release audit instead discounts the **first** relevant position. These coincide for single-positive cases, but not generally for multiple positives. The final 1,000 pools contain 976 one-positive cases, 22 two-positive cases and 2 three-positive cases; pool sizes are correspondingly 100, 101 and 102.

Read-only recalculation from the saved rankings demonstrates the discrepancy:

| Method | Released “NDCG@5” | Standard multi-positive NDCG@5 | Released “NDCG@10” | Standard multi-positive NDCG@10 |
|---|---:|---:|---:|---:|
| CLIP image | 0.078521 | 0.077845 | 0.108976 | 0.108249 |
| CLIP text | 0.086336 | 0.084773 | 0.109536 | 0.107346 |
| Evidence reranking | 0.084714 | 0.083933 | 0.114452 | 0.113504 |
| Fused CLIP | 0.094289 | 0.093065 | 0.122340 | 0.120470 |
| MiniLM | 0.084274 | 0.083351 | 0.102584 | 0.101523 |

These diagnostic means are not replacement final results or newly computed confidence intervals. The discrepancy is small numerically but important definitionally. A passing release audit does not resolve it: that audit reproduces the released first-hit convention.

**Immediate reporting route, preserving frozen results:** explicitly describe the released first-hit discounted-gain convention, distinguish it from standard multi-positive NDCG, and make table labels, equation and limitations consistent. Preserve the raw artifact column names as historical machine keys if necessary, with a mapping in the thesis. Do not present the released values as standard NDCG under the existing equation.

**Alternative requiring a separate decision:** deterministic reanalysis of saved rankings and relevant intervals/tests under standard NDCG; this needs no model rerun but does change reported analysis and is outside this review's implementation scope. Ask before doing it.

**Acceptance:** one accurate definition for every displayed score, with the multiple-positive cases acknowledged. No silent relabelling that obscures the historical error and no silent replacement of frozen results.

### F04 — P0: Describe the actual UIFR eligibility filter

**Locations:** Chapter 3 §§3.11–3.12.2; Chapter 5 limitations; `src/evidence_fashion/assessment.py:common_reference_eligibility`.

Eligibility is not simply “a concrete item-fact claim.” The implementation excludes subjective/general styling, requires a concrete case entity, and checks a lexical relationship between predicate words and supplied fact tokens. A claim introducing words absent from the supplied facts can be excluded as `not_a_literal_supplied_case_fact`. Ineligible claims are forced to not-applicable in the assessment contract.

Across accepted final claims, recorded eligibility reasons are:

| Reason | Claims |
|---|---:|
| Not a literal supplied case fact | 9,351 |
| Subjective or general styling | 4,852 |
| No concrete case entity | 1,627 |
| Literal supplied case fact | 974 |

The 974 eligible claims have 961 supported and 13 unsupported labels. This gate can exclude precisely the novel product attributes a reader might expect a general hallucination measure to test. A record with no eligible claims is not necessarily a record with no factual assertions.

**Fix without rerun:** give the actual algorithm/pseudocode and exclusion counts; describe UIFR as a restricted literal-supplied-fact sensitivity measure, not comprehensive invention detection. Preserve the 53 complete eligible pairs and inconclusive result. Explain that narrow eligibility and sparse coverage limit interpretation independently of confidence-interval width.

**Acceptance:** no broad claim of hallucination prevention or general factual safety derived from UIFR. Redesigning the gate is future work, not a covert reporting fix.

### F05 — P0: Correct the validation-selection history

**Locations:** Chapter 3 introduction, §§3.5.3, 3.7, 3.10; Chapter 4 §4.2; Chapter 5 implications.

Chapter 3 says the 0.75/0.25 reranking setting was chosen through validation-only Pareto selection. Both current and release configurations specify `fixed_040_image_060_text`, `fixed_075_clip_025_evidence_top_k_5`, fusion `grid_role: diagnostic_only` and validation `pareto_role: descriptive_only`. Parts of the thesis already describe fixed settings, making the narrative internally inconsistent.

**Fix:** describe fixed confirmatory settings and diagnostic/descriptive sensitivity analysis unless dated evidence establishes a different actual selection history. Reconcile manifests and amendments before claiming exactly when choices were frozen. “Frozen” is not synonymous with preregistered. Do not infer an optimisation procedure from the existence of a grid.

**Acceptance:** a single evidence-backed chronological account; no unsupported Pareto-selection claim or suggestion that every setting was validation-optimised.

### F06 — P0: Complete submission information and declarations

**Location:** `thesis/front_matter.md` and generated title/front pages.

The author field still contains `[Candidate name required]`; declaration and acknowledgements contain candidate-action instructions. These are not submission-ready. Candidate identity, exact degree/school details, date and the required declaration must be confirmed, not guessed.

**Acceptance:** no placeholders or drafting instructions; declaration reflects actual authorship and assistance and uses the applicable university wording. Candidate/supervisor must supply information that cannot be established from the repository.

### F07 — P1: Use trace-grounding terminology consistently

**Locations:** research questions, Chapter 3 opening/metric labels, Chapter 5 §5.3 heading and conclusions.

The study measures textual support against retained artifacts using automated judges. Rule-RAG is still generated after the ranking decision. Authentic evidence exposure does not show the generator causally used each rule, nor that its prose reveals the neural ranker's internal reasoning. No-RAG can agree with hidden rules without having been grounded in them.

**Fix:** prefer “trace-supported claims,” “trace-grounded explanation condition” and “evaluator-assessed grounding.” Reserve “faithfulness” for its defined literature meaning, appropriately qualified claims, and exact publication titles. Do not mechanically replace the word in references or frozen prompts. Trace support also is not source-article entailment, real-world truth, user preference or recommendation accuracy.

**Acceptance:** the main contribution is support against a retained decision artifact, not proved causal faithfulness or universal truth. Never call all non-trace-supported claims hallucinations: legitimate context-A claims may not be supported by B.

### F08 — P1: Clarify “full-KB” support and label correction

Final full-KB verification uses retrieved candidate packets containing 8–13 rules, usually 10, rather than placing all 200 rules before the judge. Packet retrieval filters category/query grouping; it does not establish that every antecedent applies. Describe this as **KB-candidate-packet support**, explaining the historical `full_kb_support` key. Support in that packet is not evidence the generator saw or used an unexposed rule.

The documented 163 label promotions enforce the assumed subset relationship by promoting full-KB support when trace support is positive. This imposes logical consistency by trusting the trace verdict; it is not independent semantic validation. An erroneous trace-positive verdict could instead be the problem. Describe the assumption and the correction count, preserving the frozen labels. Distinguish prompt-contract remediation from post-verification label promotion.

**Acceptance:** exact evidence boundaries and correction direction are explicit. No claim that the consistency invariant proves semantic correctness or introduces no interpretive assumption.

### F09 — P1: State the remaining dependence and missingness limitations

The 500 explanation cases represent 425 unique outfits; the 498 paired cases represent 424 outfits. Explanation inference clusters case IDs, whereas recommendation inference uses outfits. Case clustering handles generators for the same case but does not absorb all dependence between different cases from the same outfit.

**Fix:** state this limitation and remove unqualified claims that the explanation design fully accounts for dependence. Likewise, complete-case analysis is not automatically “conservative”: missingness can select a different population. Describe attrition and the estimand among available pairs without guessing the direction of bias. Outfit-clustered sensitivity is an optional later deterministic reanalysis, not something to claim already done.

### F10 — P1: Describe the whole explanation intervention and generation accounting

**Locations:** Chapter 3 §3.9; release prompts and generation records.

The conditions differ in trace availability and associated instructions/framing, including “exact expert-rule trace.” No-RAG allows general knowledge while prohibiting invented concrete facts; it is not wholly unconstrained. Context A supplies the request and minimal item/category text, not the item IDs described as present in the prose; IDs can remain in record metadata without being prompt content.

**Fix:** include verbatim frozen prompts, a context-A/context-B schema and a real worked example. Preserve original prompt language as a historical artifact even when the thesis avoids calling rules expert-certified. Interpret the contrast as the complete tested prompt/evidence package, not isolation of an evidence-only causal mechanism.

Distinguish 3,000 planned condition–case–generator cells from actual generation attempts. Saved attempt counts imply 3,254 attempts: No-RAG 1,491 cells with one attempt and 9 with two; Rule-RAG 1,288 with one, 179 with two and 33 with three. Downstream accepted records are 1,434 No-RAG and 1,427 Rule-RAG; separate generation failure from later extraction/verification attrition. Do not imply greedy decoding guarantees bitwise cross-hardware reproducibility.

**Acceptance:** a reader can reconstruct what was shown to each model and follow each stage's counts without confusing attempts, successful generations, verified records, pairs and cases.

### F11 — P1: Correct bibliography errors and unsupported attribution

Specific corrections and source links are in the ledger below. Most urgent are Text2Outfit metadata, Holm's invalid DOI-form link and the inaccessible bootstrap-book destination. These do not mean the underlying works are fictional.

Chapter 3 §3.4.1 associates McAuley et al. (2015) with the Polyvore data description, although that paper concerns a different recommendation dataset/context. Cite the actual pinned dataset distribution directly and distinguish the Han/Vasileva Polyvore variants from the distribution used here. Add a proper reference to the exact dataset card/version and relevant official model cards/checkpoints. Do not invent a paper for a checkpoint whose appropriate source is a model card.

Chapter 2 §2.6.2 should cite Doshi-Velez and Kim at the functional-/human-/application-grounded evaluation taxonomy, not rely only on their citation elsewhere. Source proximity matters.

**Acceptance:** bibliographic metadata matches the cited version; methods references support the actual resource used; citations appear next to the claims they support. No padding the bibliography to reach an arbitrary count.

### F12 — P1: Strengthen results reporting without new experiments

Chapter 4 is compact relative to the methods. Give the reader absolute levels, analysis units, sample sizes and uncertainty alongside differences, and present evidence before discussion. Use the same complete-pair estimand throughout.

Existing paired, case-averaged descriptives yield approximately:

| Outcome | No-RAG | Rule-RAG | Difference |
|---|---:|---:|---:|
| Trace-supported claim fraction | 3.07% | 24.08% | 21.02 percentage points |
| KB-candidate-packet-supported fraction | 3.13% | 24.53% | 21.40 percentage points |

These are averages for the paired analysis, not pooled claim-level proportions. Do not mix them with marginal rates from a different denominator. Add existing generator-specific summaries only when their provenance and unit are clear; label exploratory comparisons as such.

Qualify fused CLIP as strongest on the specified aggregate metrics, not universally best: MiniLM HR@1 is 4.8%, versus fused CLIP 4.5%. Do not imply statistical superiority where no corresponding test was performed. Keep the finding that evidence reranking did not improve conventional recommendation effectiveness, subject to the metric-definition correction in F03.

### F13 — P1: Make source-to-rule accountability inspectable

A reachable URL is not semantic validation. At least one Vogue outfit-formulas link is a changing category/hub page used for 21 rules. It provides weaker recoverable provenance than a stable article passage. Source linkage alone cannot justify enriched conditions.

**Fix without changing the KB:** document the source-audit method and its limits; add an appendix mapping representative rule IDs to source-backed content and enrichment. Where feasible, document all rule-to-source relationships in an audit companion without changing the frozen rules. Use article title, author/date when available, access date and a specific passage/section or legitimate archived reference. Keep quotations brief and respect copyright. Do not retrospectively mark every rule “verified” solely because its URL returns 200.

### F14 — P1: Make contribution and related-work comparisons analytical

The table in Chapter 2 often establishes that previous work did not investigate this exact task. That alone does not establish originality. Compare LOGER, PGPR, ALCE and ARES by mechanism: what evidence affects a decision, what reaches generation, what the evaluator sees, and what their tests can establish. Distinguish using existing methods in a controlled system from inventing those methods.

Avoid universal “first” claims without an adequate literature basis. The contribution can be a carefully bounded implementation and evaluation of retained evidence traces, including the negative reranking result. Support all strong statements that a previous paper lacks a feature by checking the actual paper, not only its abstract.

Chapter 2 also refers to normalising unsupported claims per 100 words, while the final outcome is trace-supported-claim density. Align this account with the implemented quantity.

### F15 — P2: Improve flow, tone and examination readability

The prose is generally intelligible and cautious, but repeated disclaimers crowd out explanation. In the assembled pre-reference text, “frozen” appears about 54 times, “exact” 59 times and “rather than” 51 times. The 21.02 and 21.40 effects each recur seven times; the 53-pair count recurs eight times. Counts are editorial indicators, not AI-detection evidence.

Condense repeated assertions that the work is bounded, not maximal, and makes zero model calls during analysis. State each evidence boundary clearly in methods, discuss its consequence once, and summarise it briefly at the end. Replace self-evaluative claims such as “This conclusion is deliberately useful rather than maximal” with the concrete result. Remove unexplained drafting-history phrases such as “the earlier conclusion” and administrative language such as “authorised” where the authorisation is not defined. Reduce the repeated FLOPs justification to a short limitations statement.

Move Chapter 3's chapter summary after its validity-controls section. Add one end-to-end worked case using real existing records: outfit/request, candidate decision, retrieved rules, both explanations, extracted claims, labels and what the example does not prove. Include an unflattering or ambiguous case as well as a successful one; identify selection as illustrative, not representative sampling. Use a compact architecture/data-flow figure if it genuinely makes evidence boundaries clearer.

### F16 — P2: Repair equations and exported presentation

- Around Equation 3.12/§3.12, the sentence about accounting for opportunities created by more words appears immediately after UIFR, despite UIFR using a claim denominator. The trace-supported density subsection/formula needs restoring: 100 times the number of trace-supported claims divided by the actual word-count convention used by the code. Verify tokenisation and zero-length handling before writing the definition.
- Equation numbering jumps to 3.14, leaving 3.13 absent. Avoid repeated prose definitions around the fusion and NDCG equations; ensure every symbol is introduced once and every formula matches implementation.
- Rendered PDF page 4 starts the Declaration on the final contents page. Give major front-matter elements appropriate page boundaries.
- The related-work table on PDF pages 27–29 has extremely narrow, heavily wrapped columns. Reformat/split it or use a suitable landscape layout; preserve readable font size and repeated headers. No clipping was confirmed on the inspected page.
- The inspected results figure is not visibly clipped, but labels are small; check at normal reading scale and in print.
- DOCX XML shows automatically prefixed heading text such as `7Chapter 1: Introduction`; the builder uses `--number-sections`. Investigate duplicate/confusing numbering in Word. Raw LaTeX page breaks are not a reliable DOCX layout mechanism. Word rendering remains to be checked, so these are export risks, not a claimed visual inspection of the entire DOCX.
- The DOCX contains mathematical objects and no detected inserted/deleted tracked changes; its comments file was empty. This is useful hygiene, not proof that the visual export is correct.

**Acceptance:** rebuild from sources and visually inspect every page of the final submission format, contents/list entries, tables, equations, hyperlinks and front matter. Do not certify PDF and DOCX equivalence from their shared Markdown alone.

## 5. Complete bibliography ledger

Numbers below are the **consolidated final reference numbers**, not chapter-local numbers. “Metadata verified” establishes the publication's identity and main bibliographic fields, not every attributed claim. HTTP blocking by a publisher is not evidence of a fabricated reference.

| Ref | Work | Verification and required action |
|---|---|---|
| 1 | McAuley et al., 2015, Image-based recommendations | Real; DOI metadata matches SIGIR, pp. 43–52. Publisher access blocked. Correct the Polyvore attribution discussed in F11. [DOI](https://doi.org/10.1145/2766462.2767755). |
| 2 | Han et al., 2017, bidirectional LSTMs | Real; title, venue and pp. 1078–1086 match. Publisher access blocked, not a bad DOI. [DOI](https://doi.org/10.1145/3123266.3123394). |
| 3 | Vasileva et al., 2018, type-aware embeddings | Real; ECVA record/PDF accessible; pp. 390–405 match. [Primary record](https://www.ecva.net/papers/eccv_2018/papers_ECCV/html/Mariya_Vasileva_Learning_Type-Aware_Embeddings_ECCV_2018_paper.php). |
| 4 | Cucurull et al., 2019, context-aware compatibility | Real; primary PDF accessible through direct retrieval; CVPR pp. 12617–12626 match. Some browser requests blocked. [Primary record](https://openaccess.thecvf.com/content_CVPR_2019/html/Cucurull_Context-Aware_Visual_Compatibility_Prediction_CVPR_2019_paper.html). |
| 5 | Radford et al., 2021, CLIP | Real; accessible PMLR record/PDF; volume 139, pp. 8748–8763 match. Cite the actual checkpoint separately where needed. [Primary record](https://proceedings.mlr.press/v139/radford21a.html). |
| 6 | Zhang and Chen, 2020, explainable recommendation survey | Real; registered metadata matches 14(1), 1–101; publisher redirect blocked. [DOI](https://doi.org/10.1561/1500000066). |
| 7 | Xian et al., 2019, PGPR | Real; registered metadata matches SIGIR pp. 285–294; publisher blocked. [DOI](https://doi.org/10.1145/3331184.3331203). |
| 8 | Zhu et al., 2021, LOGER | Real; ACL paper accessible, pp. 3083–3090. Prefer the functioning canonical ACL link where DOI routing fails. [Primary record](https://aclanthology.org/2021.naacl-main.245/). |
| 9 | Knijnenburg et al., 2012, recommender user experience | Real; metadata and accessible author copy support the entry, 22, 441–504. Do not infer user-experience benefits from this thesis's offline results. [DOI](https://doi.org/10.1007/s11257-011-9118-4). |
| 10 | Jacovi and Goldberg, 2020, faithfulness | Real; pp. 4198–4205 match. Legacy DOI route encountered blocking; canonical ACL page works. Important conceptual source, not evidence that this system is causally faithful. [Primary record](https://aclanthology.org/2020.acl-main.386/). |
| 11 | Wiegreffe and Pinter, 2019 | Real; title and pp. 11–20 match. Preserve the deliberate double “not” in the title. Use canonical ACL link if necessary. [Primary record](https://aclanthology.org/D19-1002/). |
| 12 | Lyu et al., 2024, faithful-explanation survey | Real; Computational Linguistics 50(2), 657–723 match. MIT route blocked; ACL record works. [Primary record](https://aclanthology.org/2024.cl-2.6/). |
| 13 | Lewis et al., 2020, RAG | Real; NeurIPS 33, 9459–9474, primary paper accessible. General RAG background, not a direct validation of this rule-trace intervention. [Primary record](https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html). |
| 14 | Gao et al., 2023, ALCE | Real; EMNLP pp. 6465–6488, primary paper accessible. Citation evaluation motivation does not establish that the thesis implemented identical units/metrics. [Primary record](https://aclanthology.org/2023.emnlp-main.398/). |
| 15 | Zhang et al., 2024, fine-grained citation evaluation | Real; INLG pp. 427–439 match, primary paper accessible. Compare the actual evaluation definitions. [Primary record](https://aclanthology.org/2024.inlg-main.35/). |
| 16 | Tan et al., 2019, similarity conditions | Real. CVF printed pages are 10373–10382 as in the thesis; Crossref has an offset range. Do not mechanically replace the primary paper's pages with registry metadata. [Primary paper](https://openaccess.thecvf.com/content_ICCV_2019/papers/Tan_Learning_Similarity_Conditions_Without_Explicit_Supervision_ICCV_2019_paper.pdf). |
| 17 | Kang et al., 2019, Complete the Look | Real; CVPR pp. 10532–10541 match, primary paper accessible. [Primary record](https://openaccess.thecvf.com/content_CVPR_2019/html/Kang_Complete_the_Look_Scene-Based_Complementary_Product_Recommendation_CVPR_2019_paper.html). |
| 18 | Järvelin and Kekäläinen, 2002 | Real; TOIS 20(4), 422–446 match; publisher blocked. This citation does not cure the implementation/definition mismatch in F03. [DOI](https://doi.org/10.1145/582415.582418). |
| 19 | Reimers and Gurevych, 2019, Sentence-BERT | Real; pp. 3982–3992 match. Canonical ACL page works despite legacy-route blocking. Cite the exact deployed embedding model additionally. [Primary record](https://aclanthology.org/D19-1410/). |
| 20 | Wang et al., 2020, MiniLM | Real; NeurIPS 33, 5776–5788 match, paper accessible. Distillation paper is not a substitute for the actual checkpoint/model card. [Primary record](https://proceedings.neurips.cc/paper/2020/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html). |
| 21 | Li et al., 2024, attribute-augmented framework | Real; authors, title, ECRA volume 68/article 101451 confirmed through registration and author publication information. Publisher access varied. [DOI](https://doi.org/10.1016/j.elerap.2024.101451). |
| 22 | Zhai et al., 2025, Text2Outfit | **Correct metadata.** First author is Yuanhao Zhai, not “Zhai, W.” Correct title: *Text2Outfit: Controllable Outfit Generation with Multimodal Language Models*. ICCV pp. 16165–16174 and listed DOI identify the real paper. Chapter 2 local reference 25 also needs correction. [Primary PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhai_Text2Outfit_Controllable_Outfit_Generation_with_Multimodal_Language_Models_ICCV_2025_paper.pdf). |
| 23 | Ji et al., 2023, hallucination survey | Real; ACM Computing Surveys 55(12), article 248 match; publisher blocked. Do not equate its broad hallucination concept with the restricted UIFR gate. [DOI](https://doi.org/10.1145/3571730). |
| 24 | Saad-Falcon et al., 2024, ARES | Real; NAACL pp. 338–354 match, primary paper accessible. Its existence does not validate this thesis's particular local judges. [Primary record](https://aclanthology.org/2024.naacl-long.20/). |
| 25 | Chia et al., 2022, FashionCLIP | Real; Scientific Reports 12, article 18958 matches, publisher accessible. Make clear whether used as related work or an actual experimental checkpoint. [DOI](https://doi.org/10.1038/s41598-022-23052-9). |
| 26 | Efron and Tibshirani, 1993, bootstrap book | Real; DOI `10.1007/978-1-4899-4541-9` is registered, but its publisher destination failed. Check the exact cited edition/publisher against its title page and supply a working authoritative catalogue/publisher link. Do not invent a replacement DOI. [Registration metadata](https://api.crossref.org/works/10.1007%2F978-1-4899-4541-9). |
| 27 | Holm, 1979, sequentially rejective procedure | Real; journal 6(2), 65–70. **Listed `doi.org/10.2307/4615733` returned DOI-not-found and registration lookup failed.** Use the real JSTOR stable link rather than treating the stable identifier as a verified DOI. JSTOR automated access can itself be blocked. [Stable record](https://www.jstor.org/stable/4615733); [accessible original scan](https://sci2s.ugr.es/keel/pdf/specific/articulo/0052_001.pdf). |
| 28 | Doshi-Velez and Kim, 2017 | Real; arXiv title, authors and identifier match. Add the missing proximal citation to the evaluation taxonomy. [Primary record](https://arxiv.org/abs/1702.08608). |

Chapter-local reference lists contain a few entries not cited in that chapter (Chapter 3 local 11; Chapter 4 local 1 and 4; Chapter 5 local 5, 6, 7 and 9). The consolidated builder omits these unused local entries, so they are a source-maintenance issue, not uncited padding in the submitted bibliography. Preserve chapter-local mapping when correcting entries; do not hand-renumber the final file independently.

### KB source-link audit

Of the 39 unique KB URLs, 35 returned accessible pages and four returned access blocking (403), not a confirmed missing-page response:

- [MasterClass: matching clothes using the colour wheel](https://www.masterclass.com/articles/how-to-match-clothes-using-the-color-wheel)
- [Who What Wear: best T-shirt outfits](https://www.whowhatwear.com/best-t-shirt-outfits)
- [Who What Wear: indigo denim outfits](https://www.whowhatwear.com/fashion/outfit-ideas/indigo-denim-outfits-2026)
- [Who What Wear: biker-boots outfits](https://www.whowhatwear.com/fashion/shoes/biker-boots-outfits)

The complete source identities are in `data/kb/kb_source_registry.csv`. The repository's September URL audit is historical evidence, not a substitute for this review's checks. Manually inspect the four blocked links through permitted access and document access dates. Even all-200 HTTP success would not resolve F01 or F13.

## 6. Plagiarism and AI-authorship assessment

### Checks performed

Compared the pre-bibliography thesis text against extracted full text from accessible primary PDFs for references **3, 4, 5, 8, 9, 10, 11, 13, 14, 15, 16, 17, 19, 20, 22, 24 and 28**. Normalisation lowercased alphanumeric text, joined PDF line-end hyphenation and removed thesis numeric citation markers. No exact contiguous 12-word match was found in this comparison. The temporary diagnostic script was held outside the repository; this test is described here so its narrow scope is explicit.

Also searched eight distinctive quoted thesis phrases publicly, including “Fashion recommendation is a demanding application of information retrieval,” “An interpretable component is not automatically correct,” and “Trace support rewards alignment with B, not correctness of B.” Searches did not establish a copied third-party passage. Search engines sometimes return approximate rather than exact phrase results.

These tests miss shorter borrowing, close paraphrase, translated copying, unattributed ideas, inaccessible works, unpublished theses and extraction failures. Neither no exact overlap nor low institutional similarity proves responsible attribution. Conversely, reference titles, standard methods wording and the author's own public repository can cause legitimate matches.

### Required next integrity checks

Use the university-approved similarity process and review each substantive match with the supervisor. Classify quotation, properly attributed paraphrase, standard technical phrasing, bibliographic material, prior self-publication and unattributed borrowing separately. Do not target a magic similarity percentage. Confirm the history of any related paper, repository text or earlier submission and disclose reuse where required. Do not upload unpublished thesis material to an unapproved detector or rewriting service.

Style cannot establish whether this thesis was AI-written. Template-like repetition, unusually consistent caveats and self-evaluative prose justify editing for clarity, not an accusation. Detector research also documents false positives for non-native English writing; see [Liang et al., 2023](https://arxiv.org/abs/2304.02819). No AI-percentage score is warranted here.

The appropriate response is truthful assistance disclosure, preserved drafts/notes/version history, accurate provenance, source reading and the candidate's ability to explain decisions. Do not introduce deliberate errors, superficial paraphrases or “humanising” edits to evade detection. The KB enrichment discrepancy is a factual priority regardless of how the prose sounds.

## 7. MPhil scope, chapter balance and institutional checks

The scope is plausible for an MPhil: a defined offline recommendation problem, multiple baselines, a retained-evidence intervention and controlled explanation comparisons. Five recommendation methods, 1,000 cases and a three-generator explanation study are a substantive empirical basis. Negative recommendation results are legitimate findings. A new state-of-the-art model is not necessary to make this a coherent research contribution.

The current chapter bodies contain approximately **18,136 whitespace-delimited words**, including headings, tables and mathematics; this is not an official university word count. Approximate chapter counts are 2,103 / 4,631 / 5,574 / 2,185 / 3,643. The results chapter is notably short relative to methods and discussion. This is a reason to improve self-contained reporting and analysis, not to add filler or infer failure from length. Twenty-eight references is neither an automatic deficiency nor a guarantee of adequate scholarship.

| Chapter | Main revision objective |
|---|---|
| 1 | Define the narrower grounding contribution and align RQs with what the recorded metrics can answer. Keep promises consistent with actual evaluation. |
| 2 | Deepen mechanism-level comparisons; repair resource attribution and terminology; distinguish conceptual motivation from empirical evidence for this system. |
| 3 | Correct provenance, parameter-selection history, metric definitions, eligibility, evidence boundaries and inference units. Add exact prompts and a worked example. |
| 4 | Present complete final evidence before interpretation: units, populations, absolute levels, differences, intervals, attrition and citation-label results. Resolve score naming. |
| 5 | Answer each RQ directly, remove unsupported citation statistics, distinguish limitations from established failures, and shorten repeated safeguards. |
| Front matter/exports | Complete candidate information and declarations, fix page boundaries and check both export formats visually. |

For Salford, the public [2026/27 research-award regulations](https://www.salford.ac.uk/sites/default/files/2026-07/academicregulationsresearch2627.pdf) identify the relevant award framework. The latest public PGR code located was [2025/26, version 8.3](https://www.salford.ac.uk/sites/default/files/2026-02/pgrcodeofpractice2526.pdf). Its submission section addresses authorship, attribution and the institutional similarity process; its examination guidance considers understanding, research methods, purpose, critical discussion and contribution. Confirm the edition applicable to this candidate. This review does not assign a formal examination outcome.

Detailed production/submission guidance is linked through an authenticated Doctoral School resource and was not available here. Therefore, **word limits, margins, required declaration wording, exact front-matter order and final submission-format compliance remain unverified**. Obtain the current guide from the candidate or supervisor rather than applying an old publicly indexed limit.

Salford's [public generative-AI guidance](https://www.salford.ac.uk/skills/using-gen-ai-at-salford) requires following the applicable assessment guidance, protecting information, checking original sources and taking responsibility for submitted work. General permission to use AI is not a substitute for research-degree-specific instructions. Confirm permitted assistance and disclosure with the supervisor/Doctoral School; do not claim approval based only on this general page.

Add a concise ethics/data-use statement grounded in the actual dataset and institutional determination. A dataset licence does not automatically settle every underlying image right. No evidence here authorises inventing ethics approval or claiming exemption without the relevant determination. Clarify the absence of user-study evidence and the limits of transferring editorial styling norms across populations.

## 8. Secondary future work — not prerequisites for the present writing pass

Keep these separate from corrections needed to describe the completed work truthfully:

1. Human audit of a stratified sample of extracted claims, verification labels and source-to-rule entailment; estimate agreement/error rather than assuming a second model is an independent gold standard.
2. Redesign UIFR eligibility to evaluate genuinely novel product-attribute assertions, then rerun the affected assessment stages with a new versioned protocol.
3. Isolate trace content from instruction/expert-framing changes in a new controlled generation study.
4. Broader candidate pools, additional datasets, stochastic seeds, larger models, user studies and prospective efficiency measurement.
5. Build a more tightly sourced rule base with explicit human review and evaluate it as a new version, not as an unannounced modification of this experiment.
6. With approval, perform deterministic sensitivity analyses on existing records: standard multi-positive NDCG and outfit-clustered explanation inference. These need no model rerun but would alter the analysis and must be labelled transparently.

The existence of these opportunities does not require reopening the whole project. However, the current thesis must disclose the relevant limitations now; deferring experiments must not defer honesty about what existing measures actually mean.

## 9. Ordered implementation checklist for a later session

### Pass A — resolve facts before rewriting

- [ ] Confirm candidate details, actual KB construction/AI-assistance history, relevant prior-publication history and applicable institutional guide.
- [ ] Resolve F01–F06 from artifacts and confirmed facts. Preserve a small claim-to-artifact mapping for every numerical statement.
- [ ] Decide the reporting treatment of released first-hit scores; do not change any analysis without explicit agreement.
- [ ] Remove or authenticate the strict citation statistics and replace incompatible method descriptions.
- [ ] Confirm all reported populations, exclusion counts, correction counts and attrition stages.

### Pass B — revise the scientific account

- [ ] Apply F07–F14 consistently across abstract, RQs, methods, results and conclusions.
- [ ] Correct the 28-entry bibliography and local mappings; add actual dataset/model-card sources and the missing taxonomy citation.
- [ ] Add a provenance appendix, exact prompt appendix and existing-record worked example without inventing new observations.
- [ ] Keep newly added descriptives tied to the same analysis population and label illustrative/exploratory material clearly.

### Pass C — edit and export

- [ ] Apply F15–F16, reduce repeated caveats and replace vague self-evaluation with specific evidence.
- [ ] Regenerate consolidated Markdown, references, PDF and DOCX using the repository builder.
- [ ] Check every citation resolves to the intended entry; verify equation/table/figure numbering and every page of the submission export.
- [ ] Recheck URL failures manually; preserve distinctions between blocked, missing and semantically inadequate sources.
- [ ] Run relevant non-model build/audit checks, understanding that the existing release audit does not validate the NDCG terminology.
- [ ] Inspect the diff: no changed release data, prompts, labels, KB or model configuration; no unsupported claims introduced by polishing.

### Pass D — candidate and supervisor sign-off

- [ ] Candidate can explain every main equation, denominator, evidence boundary and negative finding without relying on this report.
- [ ] Supervisor reviews corrected provenance, metric limitations and assistance disclosure.
- [ ] Complete the approved institutional similarity review and address actual problematic matches.
- [ ] Verify current submission requirements and declaration wording against the authenticated guide.
- [ ] Confirm this is the intended final version before any commit/push or submission workflow.

## 10. Final recommendation

Prioritise **accuracy of the research account over cosmetic de-AI-ing**. The defensible thesis is a bounded study showing how supplying retained rule traces changes automated support measurements, while not improving the tested recommendation effectiveness and not establishing comprehensive factual or causal faithfulness. That can be a worthwhile MPhil contribution.

The immediate obstacle is not confirmed plagiarism. It is a set of preventable contradictions between prose and evidence, plus incomplete submission preparation. Correct those, obtain the institutional integrity checks that this review cannot provide, and have the candidate and supervisor approve the resulting account. This report supersedes any earlier blanket reassurance that the thesis was fully audited or ready to submit.
