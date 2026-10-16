# Chapter 1

# Introduction

## 1.1 Background and motivation

Fashion recommendation requires a model of how garments work together. Two similar garments may be substitutes, while visually different items may complement one another in an outfit. McAuley et al. showed that product images can help model both compatibility and substitution [1]. Later work represented outfits as sequences, type-specific relations and graphs [2,3,4]. These representations use information about item context and category when ranking candidates.

Modern fashion catalogues also contain product text. Titles and descriptions may identify category, brand, material, or style terms that are difficult to infer reliably from pixels, while images contain appearance information that catalogue text may omit. Contrastive vision-language models provide a practical way to combine these signals within a shared representation [5]. A multimodal ranker can therefore exploit complementary image and text evidence without requiring every visual property to be translated into language.

Ranking performance leaves the reason for an individual recommendation unclear. A fluent answer to a user's question may omit the information that influenced the ranking. Explainable recommendation research has proposed features, reviews, knowledge-graph paths and generated language as ways to communicate reasons [6,7,8]. Whether those reasons reflect the decision process requires a separate test.

Generative language models can turn sparse catalogue information into style advice, sometimes adding colours, materials, comfort claims or occasions absent from their input. Source inconsistency is a recognised problem in natural-language generation [23]. An explanation may sound reasonable to a reader while giving an inaccurate account of the mechanism or evidence behind a decision [10,11,12]. In fashion recommendation, this leaves open whether a fluent rationale describes the selected product and its ranking evidence.

Retrieval-augmented generation offers a partial response by displaying external context during generation [13]. Yet retrieved context and decision evidence are not necessarily the same thing. Documents retrieved after an item has been selected may support a persuasive account without showing that those documents participated in selection. Furthermore, access to relevant evidence does not ensure that every generated claim is entailed by it. Citation identifiers can improve auditability, but a citation is only informative when its source actually supports the associated claim [14,15].

This thesis connects recommendation and explanation through a record produced during ranking. The system combines CLIP image and text representations with a score derived from curated fashion rules. For each candidate, it retains up to five eligible rules and their score contributions. The selected recommendation and its symbolic trace are frozen after reranking, before explanation generation. The trace records the rules that contributed numerically to the decision.

The explanation experiment then holds the selected item constant. For each case and language generator, a No-RAG explanation receives common context A: the request and frozen query and recommended-item identities, categories, and catalogue text. Its paired Rule-RAG explanation receives the same A plus exact trace B. This design isolates access to the symbolic decision trace more closely than comparing explanations of different recommendations. It also permits a necessary terminological distinction: agreement with hidden B is post-hoc decision-trace alignment for No-RAG, while agreement with visible B is decision-trace faithfulness for Rule-RAG.

The study remains deliberately bounded. Images participate in representation and ranking, but they are not captioned and do not become textual explanation evidence. The task is sampled, same-category, controlled-pool ranking over held-out Polyvore outfits rather than personalised, full-catalogue serving. The symbolic trace explains the fashion-rule component of a hybrid reranker, not every internal computation performed by CLIP. Explanation outcomes are measured through a frozen automated pipeline in which Qwen 3.5 9B extracts atomic claims and Phi-4 14B verifies them against the supplied sources. This role separation strengthens auditability, but the results remain operational system evaluation rather than human-validated ground truth.

## 1.2 Problem statement

Existing fashion recommendation research provides increasingly capable representations of item compatibility, but conventional ranking metrics answer only whether relevant items are placed near the top of a candidate list. They do not show whether an explanation accurately describes information used by the system. This creates a gap between recommendation effectiveness and explanation faithfulness.

The gap has three parts. First, high-performing multimodal representations are generally latent. Although an image and its catalogue text can jointly influence a similarity score, the score does not naturally provide a concise verbal account of the decision. Translating latent similarity into unrestricted prose risks presenting an interpretation as if it were an observed causal trace.

Second, post-hoc natural-language explanations can exploit information that did not participate in the recommendation or introduce details absent from the supplied context. In fashion, this problem is particularly visible when an explanation attributes colour, material, comfort or suitability to a product whose catalogue description supplies no such information. An unsupported assertion is not necessarily false in the world, but it is not justified by the evidence available to the generator. Treating unsupported and contradicted claims as equivalent would overstate what the experiment can establish.

Third, standard explanation-quality scores can conceal source-specific failures. Fluency, clarity, specificity, and general usefulness do not directly measure whether claims match the actual decision trace or whether cited rules entail them. A system may receive a high holistic score while misapplying a conditional rule or attaching a valid-looking identifier to an unsupported claim. Claim-level attribution and citation evaluation address this problem by checking support against specified sources [14,36,37].

This thesis addresses these problems through an evidence-aware hybrid architecture and a paired explanation experiment. Curated fashion rules contribute numerically to reranking and are stored as exact trace B. Recommendation effectiveness is evaluated separately from evidence participation. For the same locked recommendation, trace-visible and trace-hidden explanations are compared using reranking-trace claim support, full-knowledge-base claim support, Unsupported Item-Fact Rate (UIFR), citation entailment, and trace-supported claims per 100 words. These measures preserve the distinction between a sentence that is stylistically plausible and a claim that is grounded in an auditable source.

The study evaluates ranking relevance and explanation support separately. Rule reranking could make decisions easier to audit while reducing relevance, and an explanation could describe a trace accurately even when the rule base has incomplete domain coverage.

## 1.3 Aim, objectives, and research questions

The aim of this thesis is to develop and evaluate an evidence-constrained multimodal fashion recommendation framework in which generated explanations can be assessed against the exact fashion-rule trace used during recommendation.

The first objective is to construct a reproducible controlled-pool fashion-ranking pipeline that combines image and text representations while preventing outfit and exact-image leakage across research splits. This includes deterministic case construction, category-controlled candidate pools, pinned model and dataset revisions, and conventional ranking evaluation.

The second objective is to make source-grounded fashion evidence participate directly in ranking. A curated rule base is filtered and scored for each query-candidate pair, up to five eligible contributions form an evidence score, and a frozen mixture of multimodal compatibility and evidence scores reranks the pool. The complete contributing trace is stored before explanation generation.

The third objective is to compare post-hoc and trace-visible natural-language explanations under a paired design. Both conditions explain the same locked recommendation, use the same generator, decoding settings, and 45–75-word instruction, and differ in access to exact trace B and the associated evidence/citation instructions.

The fourth objective is to evaluate explanation behaviour at claim level. The study distinguishes support from the reranking trace, support from the full final knowledge-base candidate packet, common-reference item-fact support, and citation entailment. It also examines generator and category heterogeneity, complete-pair missingness, and case-clustered statistical uncertainty.

These objectives lead to four research questions:

- **RQ1:** To what extent does providing the exact retained reranking trace during generation improve claim support from that trace and from the final knowledge base, relative to a paired No-RAG baseline?
- **RQ2:** Does providing the trace reduce unsupported concrete item-fact assertions when both conditions are assessed against their common reference evidence?
- **RQ3:** Does citation syntax correspond to claim--rule entailment, rather than merely signalling the appearance of evidence use?
- **RQ4:** Are the observed explanation differences directionally stable across generators and fashion categories under generator-specific complete-pair, case-clustered analysis?

Recommendation effectiveness and evidence participation are supporting questions needed to interpret these RQs. The thesis tests whether multimodal fusion improves ranking relative to the corresponding single-modality CLIP pathways and whether curated fashion evidence materially changes selection. These tests establish what kind of decision the explanations are describing; they are not used to redefine explanation faithfulness as recommendation accuracy.

## 1.4 Scope and boundaries

The empirical dataset is the pinned `Marqo/polyvore` release described in Chapter 3. Held-out outfit co-occurrence supplies an offline relevance proxy. The primary evaluation contains approximately 100 same-category candidates per case and therefore represents sampled controlled-pool ranking. It does not model inventory, price, body fit, temporal preference, individual purchase history, or commercial serving constraints.

The multimodal pathway uses catalogue images and product text. It does not accept unconstrained real-world scene photographs, infer body characteristics, or perform image captioning. Keeping image pixels outside explanation evidence prevents unverified visual descriptions from entering A or B, but it also restricts what a legitimate explanation can say about visible properties.

The final fashion knowledge base contains 200 supplied, source-linked styling rules, exactly 40 for each target category: bags, bottoms, outerwear, shoes, and tops. These rules provide an inspectable experimental vocabulary for complementarity, formality, season, colour, and related styling considerations. They are not complete fashion knowledge, independently certified professional advice, verified product metadata, or universal prescriptions. Support from a retrieved rule does not establish that the rule is universally correct for every person or context.

The final experiment is an automated offline systems study. Three local generators produce paired explanations: Gemma 4 12B, Llama 3.1 8B Instruct, and Ministral 3 14B Instruct. Qwen 3.5 9B extracts claims and Phi-4 14B performs binary source verification. Confidence intervals quantify variation across sampled cases, not evaluator error. Human preference, trust, factual catalogue verification, and independent semantic annotation remain outside the completed experimental boundary.

## 1.5 Contributions

This thesis makes four principal contributions. First, it implements an end-to-end architecture in which a source-grounded fashion-rule trace is produced during multimodal reranking and retained for later explanation. Second, it introduces a paired evaluation design that locks recommendation identity, preventing recommendation differences from contaminating the explanation contrast. Third, it operationalises complementary claim-level measures of trace support, full-KB support, item-fact support, and citation entailment. Fourth, it provides a reproducible five-stage workflow with leakage control, validation diagnostics, frozen settings, canonical outputs, configuration hashes, and case-clustered statistical analysis.

The experimental record comprises 1,000 recommendation cases, 3,000 planned explanation cells, 17,710 extracted atomic claims and 16,804 verified claims. Trace visibility increased measured trace support by 21.02 percentage points, with positive effects across all three generators and five categories. In the recommendation comparison, evidence reranking retained 97.4% of fused CLIP's HR@10, moving from 23.1% to 22.5% while making the symbolic contribution inspectable. Together, these findings demonstrate a substantial improvement in source-supported explanation alongside a modest absolute top-ten ranking reduction. Chapter 4 reports all ranking measures, secondary explanation outcomes and uncertainty; Section 5.8 discusses the limits of these comparisons.

## 1.6 Thesis structure

Chapter 2 reviews fashion compatibility modelling, multimodal ranking, explainable recommendation, retrieval-augmented generation, faithfulness, citation evaluation, and automated assessment. It derives the gap addressed by the implemented study without claiming that evidence can guarantee perfect generation.

Chapter 3 specifies the staged methodology, data controls, multimodal representations, fashion-rule retrieval, reranking, locked explanation intervention, operational metrics, and statistical procedures. Chapter 4 reports recommendation and explanation results, subgroup stability, missingness, statistical checks, and the reproducibility record. Chapter 5 interprets those findings, separates accuracy from evidence alignment, states the limitations, and identifies independent assessment, verified visual evidence, user-centred evaluation, and a dataset-grounded compatibility knowledge graph as future work.

## 1.7 Chapter summary

The thesis investigates how to preserve an inspectable link between the symbolic component of a ranking decision and the language used to explain the selected item. The paired experiment evaluates that link against saved evidence and records the unsupported claims that remain. Chapter 2 places this question within the relevant literature.

## References

[1] McAuley, J. et al. (2015) ‘Image-based recommendations on styles and substitutes’, *Proceedings of SIGIR 2015*, pp. 43–52. https://doi.org/10.1145/2766462.2767755.

[2] Han, X. et al. (2017) ‘Learning fashion compatibility with bidirectional LSTMs’, *Proceedings of the 25th ACM International Conference on Multimedia*, pp. 1078–1086. https://doi.org/10.1145/3123266.3123394.

[3] Vasileva, M.I. et al. (2018) ‘Learning type-aware embeddings for fashion compatibility’, *Computer Vision – ECCV 2018*, LNCS 11220, pp. 405–421. https://doi.org/10.1007/978-3-030-01270-0_24.

[4] Cucurull, G. et al. (2019) ‘Context-aware visual compatibility prediction’, *Proceedings of CVPR 2019*, pp. 12617–12626. https://openaccess.thecvf.com/content_CVPR_2019/html/Cucurull_Context-Aware_Visual_Compatibility_Prediction_CVPR_2019_paper.html.

[5] Radford, A. et al. (2021) ‘Learning transferable visual models from natural language supervision’, *Proceedings of ICML 2021*, 139, pp. 8748–8763. https://proceedings.mlr.press/v139/radford21a.html.

[6] Zhang, Y. and Chen, X. (2020) ‘Explainable recommendation: A survey and new perspectives’, *Foundations and Trends in Information Retrieval*, 14(1), pp. 1–101. https://doi.org/10.1561/1500000066.

[7] Xian, Y. et al. (2019) ‘Reinforcement knowledge graph reasoning for explainable recommendation’, *Proceedings of SIGIR 2019*, pp. 285–294. https://doi.org/10.1145/3331184.3331203.

[8] Zhu, Y. et al. (2021) ‘Faithfully explainable recommendation via neural logic reasoning’, *Proceedings of NAACL 2021*, pp. 3083–3090. https://doi.org/10.18653/v1/2021.naacl-main.245.

[10] Jacovi, A. and Goldberg, Y. (2020) ‘Towards faithfully interpretable NLP systems: How should we define and evaluate faithfulness?’, *Proceedings of ACL 2020*, pp. 4198–4205. https://doi.org/10.18653/v1/2020.acl-main.386.

[11] Wiegreffe, S. and Pinter, Y. (2019) ‘Attention is not not explanation’, *Proceedings of EMNLP-IJCNLP 2019*, pp. 11–20. https://doi.org/10.18653/v1/D19-1002.

[12] Lyu, Q. et al. (2024) ‘Towards faithful model explanation in NLP: A survey’, *Computational Linguistics*, 50(2), pp. 657–723. https://doi.org/10.1162/coli_a_00511.

[13] Lewis, P. et al. (2020) ‘Retrieval-augmented generation for knowledge-intensive NLP tasks’, *Advances in Neural Information Processing Systems*, 33, pp. 9459–9474. https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html.

[14] Gao, T. et al. (2023) ‘Enabling large language models to generate text with citations’, *Proceedings of EMNLP 2023*, pp. 6465–6488. https://doi.org/10.18653/v1/2023.emnlp-main.398.

[15] Zhang, W. et al. (2024) ‘Towards fine-grained citation evaluation in generated text: A comparative analysis of faithfulness metrics’, *Proceedings of INLG 2024*, pp. 427–439. https://doi.org/10.18653/v1/2024.inlg-main.35.

[23] Ji, Z. et al. (2023) ‘Survey of hallucination in natural language generation’, *ACM Computing Surveys*, 55(12), Article 248. https://doi.org/10.1145/3571730.

[36] Rashkin, H. et al. (2023) ‘Measuring Attribution in Natural Language Generation Models’, *Computational Linguistics*, 49(4), pp. 777–840. https://aclanthology.org/2023.cl-4.2/.

[37] Min, S. et al. (2023) ‘FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation’, *Proceedings of EMNLP 2023*, pp. 12076–12100. https://doi.org/10.18653/v1/2023.emnlp-main.741.
