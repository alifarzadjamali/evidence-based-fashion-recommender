# Chapter 5

# Discussion and Conclusion

## 5.1 Introduction

This chapter interprets the findings in relation to the research problem and literature reviewed in Chapter 2. The study began from a practical tension. Multimodal fashion recommenders can rank visually and semantically compatible products, while language models can explain almost any selected item fluently. Neither capability ensures that the explanation describes the evidence that actually influenced the recommendation. The implemented system addresses this gap by storing the source-grounded fashion-rule component of the reranking decision and exposing that same trace to an explanation generator.

The evaluation covered 1,000 ranking cases and 500 explanation cases across three generators. Of 3,000 planned generation cells, 2,969 were accepted; the assessment pipeline extracted 17,710 claims and verified 16,804. Supplying the retained trace increased trace support by 21.02 percentage points and full-KB support by 21.40 points. The architecture connects a numerical recommendation decision to evidence that can be inspected in its explanation, while the paired design measures the benefit of exposing that evidence for a fixed recommendation. This chapter discusses these contributions and consolidates their methodological limits in Section 5.8.

## 5.2 Interpretation of recommendation findings

### 5.2.1 Value of multimodal fusion

Fused CLIP achieved the highest top-five and top-ten hit rates among the tested methods (Table 4.1), although MiniLM had the highest HR@1. Combining image and text representations was therefore useful within this candidate protocol. The result is consistent with the modalities supplying complementary catalogue information, but the experiment does not identify which visual or textual features caused an individual ranking change.

The result aligns with multimodal fashion research in which learned visual representations improve style compatibility and category-aware outfit modelling [1,2,5]. The controlled held-out task provides a common basis for comparing the fixed representations and the contribution of evidence reranking.

FashionCLIP and Text2Outfit illustrate how domain adaptation and task-specific generation extend beyond a frozen general-purpose encoder [25,22]. They provide context for extending the representation. The present experiment isolates the addition of an explicit rule score to the same multimodal ranking and evaluates language against its retained trace.

### 5.2.2 Accuracy and evidence alignment are different objectives

Evidence reranking retained 97.4% of fused CLIP's HR@10: the hit rate changed from 23.1% to 22.5%, an absolute reduction of 0.6 percentage points. HR@5 changed from 14.3% to 13.2%, and the released DFH@10 from 12.23% to 11.45%. All reported aggregate ranking metrics were lower at the tested 0.75/0.25 operating point. These figures quantify the relevance outcome alongside the addition of an inspectable symbolic contribution.

The reranker changed the top item in 26.5% of cases and increased the selected item's evidence score by 0.1473 on average. The rules therefore participated in selection, and the saved contributions identify how they entered the ranking objective. This is the architectural basis for carrying decision evidence into explanation generation.

Ranking and explanation were evaluated through separate comparisons. The ranking study compared fused CLIP with evidence reranking; the explanation study held the recommendation fixed and varied trace access and grounding instructions. Together they measure ranking behaviour and explanation support, but they do not estimate a causal price of faithfulness. Section 5.8 discusses the relevance proxy and rule coverage that constrain this interpretation.

## 5.3 Interpretation of explanation faithfulness

### 5.3.1 From plausible rationale to trace-linked account

The primary outcome measures support by the retained rule trace. Rule-RAG improved this rate by 21.02 percentage points, with a 95% interval of 19.72 to 22.37 points (Table 4.2). Full-KB support improved by 21.40 percentage points. The similar gains suggest that the measured benefit was concentrated in evidence already available in the trace.

Agreement between No-RAG claims and the hidden trace can arise from a generator's prior knowledge. Rule-RAG receives the retained trace directly, and the paired contrast measures the effect of that access together with its grounding instructions. This design tests source support for the same recommendation in both conditions. The distinction between measured source support and internal causal faithfulness follows evaluation concerns in prior work [10,35].

The positive support direction held across the tested generators and categories. Effect magnitudes differed, with Ministral showing a smaller trace-support change than Gemma or Llama. This suggests that the response to evidence depends on the generator, even when the recommendation and prompt contract are held fixed.

### 5.3.2 Unsupported item-specific assertions

The final UIFR outcome addresses a different failure: concrete item facts unsupported by the common reference packet. Its estimate was +0.63 percentage points for Rule-RAG minus No-RAG, with a 95% interval from −5.03 to +5.66 and Holm-adjusted \(p=0.9042\). Only 53 complete pairs were eligible. The result is therefore inconclusive, not evidence that Rule-RAG either reduces or increases unsupported item facts.

Appendix B shows paired outputs together with their supplied evidence and automated labels. These records illustrate how a model can paraphrase a rule, attach a citation and still receive a negative entailment judgement. They also show why a reviewer needs the original text and evidence to assess whether the verifier’s decision is reasonable.

### 5.3.3 Citation entailment

The recorded Rule-RAG claims received 1,820 `entails`, 5,502 `does_not_entail` and 753 `N/A` labels (Table 4.3). Thus, displaying rule identifiers did not ensure positive entailment judgements under the frozen verifier. The result is consistent with the need to evaluate citation quality separately from answer fluency and overall correctness [14,15].

The architecture makes cited rules inspectable and permits citation use to be assessed separately from overall source support. The counts are claim-level labels; the reporting limits for relation-level citation precision and coverage are set out in Section 5.8.

## 5.4 Relationship between grounding and user-facing quality

The source-support gains give a concrete basis for evaluating evidence-grounded explanations. Trace support links language to evidence used in the symbolic reranker; full-KB support assesses agreement with the broader available packet; and supported-claim density measures how much supported content appears within a given amount of text. Their agreement strengthens the finding that Rule-RAG improves measured grounding under the shared prompt contract.

User-facing quality is a separate evaluation objective. The user-experience and explanation-goal frameworks reviewed in Chapter 2 provide criteria for assessing clarity, usefulness and persuasion [9,33]. Prior work also distinguishes the user experience of an explanation from its faithfulness to the decision process [9,28,33]. The present framework preserves the measures needed to examine those relationships: a future user study can compare preferences with source support and citation entailment, while retaining the original explanation and evidence for review.

## 5.5 Generator and category heterogeneity

The primary support effects were positive across all three generators and five categories. This consistency extends the overall result across the evaluated models and product groups, with effect magnitudes showing how strongly each generator responded to the supplied evidence. Ministral's smaller gain, for example, identifies generator choice as a relevant factor in the size of the benefit.

Complete pairs were 474 for Gemma, 438 for Llama, and 456 for Ministral; the overall analysis used 498 cases with at least one available generator pair. Reporting these denominators alongside subgroup estimates makes the coverage of the stability analysis explicit. The pooled contrast remains the primary estimate, with subgroup results describing variation within the tested setting.

## 5.6 The role of explanation length

Both conditions were instructed to use 45 to 75 words. Across accepted outputs, No-RAG averaged 62.10 words and Rule-RAG 64.83, a residual difference of 2.72 words under the shared contract. The common length contract makes the support comparison relevant to explanations of similar length, while leaving a measurable residual length difference.

Rule-RAG added 1.60 trace-supported claims per 100 words. This density gain complements the higher claim-level support rates: the benefit persists when supported content is expressed relative to text length. Evidence access and citation instructions can also change proposition selection, and the experiment estimates their combined effect under the shared length contract.

## 5.7 Contributions of the research

The first contribution is an end-to-end architecture that connects multimodal ranking to a reusable explanation trace. CLIP image and text representations support candidate retrieval; curated fashion rules participate numerically in reranking; and the complete set of up to five retained contributions is stored before explanation generation. This avoids constructing “evidence” after the recommendation has already been chosen.

The second contribution is a paired experimental design that locks recommendation identity. No-RAG and Rule-RAG explain the same item for the same user request and generator. Differences in explanation cannot be attributed to one condition receiving an easier or more compatible recommendation. This is a practical design pattern for evaluating explanation interventions in recommender systems.

The third contribution is a measurement framework for the study's different evidence boundaries. Trace support assesses agreement with B; full-KB support uses the broader final rule packet; UIFR concerns eligible concrete item facts; and supported-claim density accounts for text length. The No-RAG condition can agree with a hidden trace after the fact, while Rule-RAG can use a visible trace. Citation entailment examines whether a cited rule supports its claim. Reporting these outcomes separately shows which aspect of an explanation changed.

The fourth contribution is a reproducible analysis record. It preserves data and model revisions, model digests, configuration and prompt hashes, rule traces, response hashes, cluster units and derived artifacts. The Stage-5 paired analysis, subgroup summaries, figures and qualitative selection use saved records without new model inference. This matters for local generative experiments because outputs can change after server or model updates.

Together, these contributions provide an implemented and evaluated route from multimodal candidate ranking to explanations with inspectable decision evidence. The evaluation demonstrates a measured source-support benefit across three generators and five categories, supported by saved claim assessments and paired uncertainty estimates.

## 5.8 Limitations

### 5.8.1 Offline relevance and controlled pools

Same-outfit co-occurrence is an imperfect relevance proxy. It reflects one curated outfit rather than all acceptable combinations and labels plausible alternatives as negatives. Candidate pools contain sampled same-category items, not a live catalogue with inventory, price, user history, or business constraints. Metrics at approximately 100 candidates cannot be transferred directly to full-catalogue serving. No larger-pool estimate is included in the final release, so the direction and size of any change at catalogue scale remain unmeasured.

The tested reranker lowered every reported aggregate ranking metric. No predeclared non-inferiority margin was used, so the observed HR@10 retention does not establish equivalent relevance or a negligible penalty. Generic rule prescriptions may differ from the taste signal represented by a curated outfit. Validation-selected evidence weights and more conditional rules are plausible ways to improve relevance, but their effectiveness remains untested.

### 5.8.2 Visual representation and fusion

The frozen CLIP pathway is not fine-tuned on the exact outfit-completion objective, body fit, or subtle fashion attributes. The study deliberately avoided visual captioning so that images could not leak unverified text into explanations. This protects the evidence boundary but means an explanation cannot legitimately mention genuine visual properties unless product text or a rule supports them.

### 5.8.3 Rule-base coverage and semantics

The supplied 200-rule base is finite and generic, with source links and record-level provenance. Their provenance does not constitute independent professional certification or empirical truth probabilities, and semantic retrieval can select a rule whose antecedent only partly matches the case. The trace faithfully records what the algorithm used, but the algorithm's rule choice can itself be questionable. Trace support rewards alignment with B, not correctness of B. Recommendation metrics partly evaluate the consequence, but do not validate individual rules.

### 5.8.4 Automated evaluation

No human audit is part of the final study. Qwen-generated claim boundaries and Phi support labels can be wrong. Cross-model separation is stronger than using one model for both tasks, but shared training data and general LLM biases remain possible. The deterministic logical-consistency correction cannot correct semantic mistakes; it only enforces the trace-subset invariant. The restricted UIFR schema improves conservatism at the cost of coverage. Reported confidence intervals quantify sampling variation over cases, not evaluator uncertainty.

Four extractions and 104 verifications remained terminal failures. Saved raw records and denominators make these failures inspectable. UIFR eligibility requires literal coverage and a concrete item reference, so unsupported novel attributes may be excluded before semantic verification. Its 53 complete pairs limit both precision and the range of assertions represented. A broader product-fact audit would require independently annotated eligibility and support.

Citation precision and coverage cannot be reconstructed from the saved claim labels because complete claim-source relations and the eligible-claim denominator were not retained. The predominance of `does_not_entail` labels establishes a citation-use problem under the verifier, even alongside the overall source-support improvement.

The binary trace and KB labels also leave partial support unresolved. A statement that accurately paraphrases part of a conditional rule may overstate its applicability to the selected item. Quantifying such overstatement would require a separate annotation definition and cannot be recovered from the present labels.

Source support also does not establish the internal causal contribution of individual rules to generation; removing or replacing rules would be needed to test that contribution. No user study establishes whether the explanations improve clarity, usefulness or persuasion.

### 5.8.5 Generalisability and model dependence

The three generators are quantised local models between 8.0B and 13.9B parameters. Greedy decoding improves reproducibility but does not represent common stochastic chat settings. The assessment models are also local and quantised. Results may differ for larger proprietary models, domain-fine-tuned generators, alternative RAG templates, or repeated stochastic samples. The tested categories cover common apparel groups but not dresses as an independent target, cosmetics, sizing, or personalised styling.

Accepted coverage was uneven, including 31 terminal Rule-RAG word-count failures for Llama. UIFR intersections were smaller still because both outputs needed eligible item-fact claims. Category differences may reflect rule conditionality and product-title quality, so subgroup estimates describe the evaluated setting.

### 5.8.6 Computational reporting

Model sizes, quantisation, latency and output counts describe the implementation’s computational demands. The absence of FLOP or energy measurements limits hardware-normalised comparisons. Prospective profiling should account for sequence lengths, cache reuse and quantised kernels before an efficiency claim is made.

## 5.9 Implications for system design

For developers, the main implication is that evidence should be produced during the decision and carried forward as a typed artifact. A list of documents retrieved only after selection can explain a candidate without showing that those documents influenced it. The stored B trace instead binds rule identifiers and contributions to the chosen item. This makes later generation and auditing possible.

The second implication is to constrain instance-level language. A system can safely say that a rule recommends considering colour compatibility without asserting that two unknown colours match. Product facts should come from explicit catalogue metadata or verified visual attributes, and rule advice should remain relational. Prompt instructions can encourage this distinction, but deterministic post-generation checks or constrained templates may be needed for high-stakes deployment.

Citation checks require explicit claim–source relations. Systems should preserve cited spans, rule IDs, eligibility decisions and support judgements so that precision and coverage can be reconstructed. The present schema’s reporting limits demonstrate the importance of retaining these records at collection time.

Deployment decisions also need explicit relevance and explanation requirements. Validation diagnostics can show how evidence weights trade off ranking and interpretability, but acceptable thresholds should be set before test results are inspected. This thesis evaluates one fixed operating point and does not establish an optimal deployment policy.

## 5.10 Future research

The first priority is independent assessment of the source-support judgements. AIS and FActScore provide relevant principles for source attribution and atomic annotation [36,37], while ARES illustrates the role of human-labelled data in automated estimation [24]. The recent judge-lifecycle study motivates checking evaluator alignment as models and catalogues change [41]. These procedures would allow sampling uncertainty and evaluator error to be considered separately.

A factorial study could cross evidence visibility with length instructions while holding recommendations fixed. It could separate effects of trace access, citation instructions and concision. Repeated samples would show variation across decoding runs and generators. This would require new generation and assessment.

Third, visual evidence could be added under a separate, explicit boundary. A verified attribute extractor could produce an image-evidence block C containing confidence-scored colour, pattern, and silhouette observations. Explanations could then cite A, B, or C. This would allow legitimate visual specificity while maintaining source provenance, provided that the extractor is evaluated against an attribute benchmark with calibrated thresholds.

Fourth, a future project could construct a dataset-grounded compatibility knowledge graph from an independent fashion dataset. It should preserve relation-level provenance and statistically estimated compatibility relations, remain separate from the recommendation benchmark used for evaluation, and distinguish observations from inferred edges. That resource could support KG-supervised recommendation, controlled rule-retrieval ablations, and conventional compatibility-prediction or fill-in-the-blank validation. The same selected evidence could then be carried into explanation. This is a proposed extension, not a component or result of the completed experiment.

Fifth, recommendation evaluation could move beyond sampled co-occurrence through temporal hold-outs, larger catalogue pools, stronger compatibility objectives, and calibrated fusion. Tuning evidence weights on validation data and applying rules only when their conditions are met could test whether relevance can be recovered while retaining inspectable traces; no such recovery is established by the present results. A future comparison should evaluate general and fashion-domain encoders at their own validation-selected weights, with the same split and candidate protocol. User-centred evaluation remains outside the scope of the present automated thesis.

Computational efficiency also warrants direct measurement. Prospective profiling could record tokens, joules, latency percentiles, GPU memory, and operation counts for each stage. Smaller generators or extractive templates may recover most faithfulness benefits at lower cost. A controlled throughput study would be needed before claiming an efficiency benefit from evidence constraints.

## 5.11 Conclusions against the research questions and objectives

RQ1 asked whether access to the retained trace improves support by that trace and the wider KB packet. The paired results support this claim under the frozen automated evaluator. Trace support increased by 21.02 percentage points (95% interval: 19.72 to 22.37), full-KB support by 21.40 points, and trace-supported-claim density by 1.60 claims per 100 words.

RQ2 asked whether trace access reduces unsupported concrete item-fact assertions. The result is inconclusive. Only 53 underlying cases contributed jointly eligible pairs, and the literal eligibility gate limits the range of product assertions represented. The experiment therefore provides no basis for a general reduction claim.

RQ3 asked whether citation syntax corresponds to claim–rule entailment. Most applicable Rule-RAG claim labels were `does_not_entail`. Citation markers made sources inspectable but did not reliably indicate support under the verifier. Relation-level precision and coverage remain unestimated because the required records were not retained.

RQ4 asked whether explanation differences were directionally stable across generators and categories. The primary support effects were positive across all three generators and five categories. This supports stability within the evaluated setting; failure asymmetry and restricted UIFR eligibility limit the secondary comparisons.

The four objectives were addressed as follows. Objective 1 produced a reproducible multimodal ranking pipeline with outfit and exact-image leakage controls. Objective 2 incorporated the supplied rules numerically into reranking and preserved their contributions before explanation. Objective 3 implemented paired trace-visible and trace-hidden generation for locked recommendations. Objective 4 produced claim-level source assessments, subgroup estimates and clustered uncertainty, while revealing limitations in item-fact eligibility and citation reporting.

The study demonstrates that exposing retained decision evidence improves measured source support in explanations of fixed fashion recommendations. Its contribution combines an operational architecture, a controlled comparison across three generators, and a reproducible assessment record. The 21.02-point trace-support gain and higher supported-claim density establish the explanation benefit within the evaluated setting, while the limitations in Section 5.8 define the next steps for relevance tuning, citation validation and user assessment.

## References

[1] McAuley, J. et al. (2015) ‘Image-based recommendations on styles and substitutes’, *Proceedings of SIGIR 2015*, pp. 43–52. https://doi.org/10.1145/2766462.2767755.

[2] Han, X. et al. (2017) ‘Learning fashion compatibility with bidirectional LSTMs’, *Proceedings of the 25th ACM International Conference on Multimedia*, pp. 1078–1086. https://doi.org/10.1145/3123266.3123394.

[5] Radford, A. et al. (2021) ‘Learning transferable visual models from natural language supervision’, *Proceedings of ICML 2021*, 139, pp. 8748–8763. https://proceedings.mlr.press/v139/radford21a.html.

[9] Knijnenburg, B.P. et al. (2012) ‘Explaining the user experience of recommender systems’, *User Modeling and User-Adapted Interaction*, 22(4–5), pp. 441–504. https://doi.org/10.1007/s11257-011-9118-4.

[10] Jacovi, A. and Goldberg, Y. (2020) ‘Towards faithfully interpretable NLP systems: How should we define and evaluate faithfulness?’, *Proceedings of ACL 2020*, pp. 4198–4205. https://doi.org/10.18653/v1/2020.acl-main.386.

[14] Gao, T. et al. (2023) ‘Enabling large language models to generate text with citations’, *Proceedings of EMNLP 2023*, pp. 6465–6488. https://doi.org/10.18653/v1/2023.emnlp-main.398.

[15] Zhang, W. et al. (2024) ‘Towards fine-grained citation evaluation in generated text: A comparative analysis of faithfulness metrics’, *Proceedings of INLG 2024*, pp. 427–439. https://doi.org/10.18653/v1/2024.inlg-main.35.

[22] Zhai, Y. et al. (2025) ‘Text2Outfit: Controllable Outfit Generation with Multimodal Language Models’, *Proceedings of ICCV 2025*, pp. 16165–16174. https://doi.org/10.1109/ICCV51701.2025.01500.

[24] Saad-Falcon, J. et al. (2024) ‘ARES: An automated evaluation framework for retrieval-augmented generation systems’, *Proceedings of NAACL 2024*, pp. 338–354. https://doi.org/10.18653/v1/2024.naacl-long.20.

[25] Chia, P.J. et al. (2022) ‘Contrastive language and vision learning of general fashion concepts’, *Scientific Reports*, 12, Article 18958. https://doi.org/10.1038/s41598-022-23052-9.

[28] Doshi-Velez, F. and Kim, B. (2017) ‘Towards a rigorous science of interpretable machine learning’, arXiv:1702.08608. https://arxiv.org/abs/1702.08608.

[33] Tintarev, N. and Masthoff, J. (2007) ‘A Survey of Explanations in Recommender Systems’, *IEEE 23rd International Conference on Data Engineering Workshop*, pp. 801–810. https://doi.org/10.1109/ICDEW.2007.4401070.

[35] Turpin, M. et al. (2023) ‘Language Models Don’t Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting’, *Advances in Neural Information Processing Systems*, 36. https://proceedings.neurips.cc/paper_files/paper/2023/hash/ed3fea9033a80fea1376299fa7863f4a-Abstract-Conference.html.

[36] Rashkin, H. et al. (2023) ‘Measuring Attribution in Natural Language Generation Models’, *Computational Linguistics*, 49(4), pp. 777–840. https://aclanthology.org/2023.cl-4.2/.

[37] Min, S. et al. (2023) ‘FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation’, *Proceedings of EMNLP 2023*, pp. 12076–12100. https://doi.org/10.18653/v1/2023.emnlp-main.741.

[41] Kong, E.Y. et al. (2026) ‘The Lifecycle of LLM-as-a-Judge for Large-Scale Recommendation Explanations’, *arXiv preprint*, arXiv:2608.18300v3. https://arxiv.org/abs/2608.18300v3.
