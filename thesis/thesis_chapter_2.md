# Chapter 2

# Literature Review

## 2.1 Introduction

This chapter positions the thesis at the intersection of fashion compatibility modelling, multimodal information retrieval, explainable recommendation, retrieval-augmented generation (RAG), and explanation-faithfulness evaluation. These areas address related but distinct questions. Fashion recommendation asks which item is compatible with a query or partial outfit. Multimodal retrieval asks how image and text signals should be represented and combined. Explainable recommendation asks how the basis of a recommendation can be communicated. RAG supplies external context to a generator. Faithfulness research asks whether an explanation accurately reflects the evidence or process it claims to explain.

The review concentrates on the relationship between recommendation evidence and explanatory language. Its central question is how prior work connects an interpretable recommendation mechanism to an explanation, and what evidence is needed to assess that connection. This requires distinguishing predictive performance, source attribution and user experience.

The review proceeds in six parts. Section 2.2 examines the development of fashion compatibility and outfit recommendation. Section 2.3 discusses multimodal representations and the distinction between latent compatibility and verbal evidence. Section 2.4 reviews explainable and knowledge-aware recommendation. Section 2.5 considers generative explanation, RAG, citations, and unsupported claims. Section 2.6 examines faithfulness definitions and evaluation methods. Section 2.7 compares representative studies and derives the research gap that leads directly to the methodology in Chapter 3.

## 2.2 Fashion compatibility and outfit recommendation

### 2.2.1 From visual similarity to compatibility

Visual similarity alone cannot identify every useful addition to an outfit. Two nearly identical black shoes may be substitutes, while a shoe and a pair of trousers can be complementary. A fashion representation must account for relations between item types when ranking additions to an outfit.

McAuley et al. [1] learned visual relationships for styles and substitutes from large-scale product data. Their results showed that convolutional image features can represent compatibility derived from observed relationships. The learned distances support recommendation, although they do not explain why a particular candidate complements a query.

Han et al. [2] treated an outfit as an ordered sequence and learned compatibility with bidirectional LSTMs. The model captures dependencies across outfit components and supports fill-in-the-blank evaluation. Its sequence representation uses an imposed item order, and its learned state does not provide an inspectable language account of an individual decision.

Vasileva et al. [3] explicitly distinguished similarity from compatibility through type-aware embeddings. Their model learns item-type-specific relations so that comparisons can be conditioned on categories such as tops, bottoms, or shoes. This matches the intuition that different features matter for different cross-category relationships. The associated Polyvore-Outfits dataset and fill-in-the-blank tasks became important resources for compatibility research. Their type-aware treatment also makes category restrictions an explicit part of evaluation design.

### 2.2.2 Context, graphs, and outfit structure

Cucurull et al. [4] argued that compatibility should depend on item context and proposed graph neural representations conditioned on products known to be compatible. Their results on Polyvore, Fashion-Gen, and Amazon data demonstrated the benefit of relational context over isolated pairwise comparison. Graph-based methods can model higher-order outfit structure, but their explanatory value depends on whether graph paths or learned relationships are exposed and demonstrably used in prediction.

Tan et al. [16] learned similarity conditions without requiring explicit condition labels at test time. By representing distinct semantic subspaces as latent variables, the model improved generalisation across fashion datasets. This line of work illustrates a recurring trade-off: more flexible latent representations can improve predictive capability while making a human-readable account of an individual decision less direct.

Kang et al. [17] extended complementary recommendation to scene images in *Complete the Look*. Compared with catalogue images, scene inputs provide context about an existing outfit and its surroundings. The resulting task involves locating useful visual context as well as identifying compatible products. It should therefore be distinguished from the catalogue-item setting used in many Polyvore studies.

The studies model different relations: substitution, sequence context, item type and scene context. Their task results are consequently difficult to compare directly. A learned compatibility score also leaves the basis of an individual recommendation unclear. Section 2.4 examines fashion models that address explanation directly.

### 2.2.3 Evaluation conventions and their limits

Outfit-compatibility classification and fill-in-the-blank (FITB) evaluation test related but different abilities. Classification distinguishes compatible from constructed incompatible outfits; FITB asks a model to recover a missing item among alternatives [2,3]. Retrieval measures such as hit rate and reciprocal rank locate relevant items in an ordered list, while discounted gain rewards relevant results near the top [18]. Comparisons require a common relevance definition and candidate protocol.

The Polyvore protocols in Han et al. and Vasileva et al. derive positives from curated outfits [2,3]. This provides an observable relevance label. A limitation of that label is that an item absent from a particular outfit may still be a plausible alternative. This thesis therefore interprets co-occurrence as an offline evaluation proxy, rather than a complete judgement of fashion compatibility.

Vasileva et al. distinguish disjoint and non-disjoint settings when examining generalisation [3]. Their treatment shows why the unit of separation matters: an unseen outfit may contain familiar items. Split construction and duplicate checks should consequently be reported alongside ranking scores. The specific controls used in this study are described in Chapter 3.

## 2.3 Multimodal representation and evidence boundaries

### 2.3.1 Image and text as complementary signals

Catalogue text provides explicit product terms, while images represent appearance that descriptions may omit. CLIP learns aligned image and text representations and supports zero-shot transfer [5]. Sentence-BERT instead produces sentence representations suitable for semantic similarity, and MiniLM provides a compact transformer architecture [19,20]. These resources make frozen retrieval baselines feasible, although their original training objectives differ from outfit compatibility.

FashionCLIP adapts contrastive image–text learning to fashion data [25], showing the value of domain-specific representation learning. Li et al. combine visual information and attributes in an explainable attribute-augmented framework, using an attribute-pair encoder to represent pairing knowledge [21]. These approaches motivate stronger fashion representations, while also raising a separate evaluation question: which interpretable attributes support the explanation of an individual recommendation?

Zhai et al. [22] address controllable outfit generation in *Text2Outfit: Controllable Outfit Generation with Multimodal Language Models*. Their model supports text-to-outfit and seed-to-outfit tasks, predicting outfit composition and item representations. This extends the range of fashion tasks handled through language, but its generation objective differs from assessing the support of a written explanation for an already selected catalogue item. It provides relevant context without serving as a directly comparable baseline for the paired experiment here.

### 2.3.2 Representation is not textual evidence

An image embedding can inform a ranking without supplying verified textual attributes. Colour, silhouette, pattern, composition and other correlations may affect similarity, but their individual contributions are not recoverable from the score alone. An explanation that says “the burgundy trousers match the leather shoes” needs evidence for both attributes. Processing the images with CLIP does not establish that those attributes were represented explicitly or caused the ranking.

A useful distinction is between evidence available to the language generator and features used by the ranker. When a generator receives catalogue text and rules, its product assertions can be checked against those sources. Claims about image content require an additional visual-grounding assessment. Neither a cosine score nor a generic rule about matching colours establishes the colour of a particular item.

Jacovi and Goldberg distinguish an explanation that appears convincing from one that accurately reflects the process being explained [10]. For a hybrid ranker, this requires specifying which component an explanation targets. A trace of rule contributions can expose the symbolic calculation while leaving the neural representation only partially interpreted.

## 2.4 Explainable recommender systems

### 2.4.1 Purposes and forms of recommendation explanation

Explanations in recommender systems serve several possible goals: transparency, scrutability, trust, effectiveness, persuasiveness, efficiency and satisfaction [33]. These objectives can conflict. A persuasive explanation may increase acceptance without accurately exposing the recommendation process; a technically faithful trace may be difficult for a user to understand. Evaluation must therefore match the stated purpose.

Zhang and Chen [6] survey explainable recommendation approaches including neighbourhood, matrix-factorisation, topic, graph, deep-learning, and natural-language methods. Feature-based explanations can identify influential attributes; review-based methods can reuse user-authored evidence; path-based systems can expose relations between users and products. Natural-language generation can improve accessibility, but it introduces another model whose output may diverge from the recommendation evidence.

Knijnenburg et al. [9] provide a framework for the user experience of recommender systems. They relate objective system aspects to subjective perceptions, experience and interaction. This framework is relevant when asking how people respond to a recommendation; it does not supply a taxonomy of explanation methods. Automated source-support scores and user-experience measures therefore require separate interpretation.

### 2.4.2 Post-hoc and mechanism-linked explanations

Post-hoc explanations are produced after a prediction and may approximate its basis through surrogate features, attention, retrieved examples, or generated rationales. Their fidelity requires a test appropriate to the claimed explanation target [10,12]. Attention weights, for example, have generated substantial debate over when they constitute explanations and what kind of causal claim they support [34,11]. Jain and Wallace found that attention distributions could vary substantially without corresponding prediction changes, while Wiegreffe and Pinter questioned whether the proposed tests were sufficient to dismiss attention as an explanation. Their disagreement reinforces the need to specify both the explanatory claim and the test used to assess it.

Mechanism-linked approaches instead incorporate interpretable components into prediction. Policy-Guided Path Reasoning uses knowledge-graph paths to connect users and recommended items [7]. LOGER combines knowledge-graph embeddings with neural logic rules and uses learned rule importance to guide path reasoning for explainable recommendation [8]. These systems demonstrate that paths or rules can be part of recommendation rather than decoration added afterwards.

These studies establish that recommendation and interpretable reasoning can be connected within one architecture. The remaining question for a language interface is whether generated claims accurately communicate the recorded reasoning. A path or rule used by a recommender does not itself constrain every sentence subsequently produced by a language model.

### 2.4.3 Explainable fashion and personalised language generation

Explainable fashion recommendation predates large language models. Hou et al. [29] propose SAERS, which represents semantic clothing attributes and uses attention to model users’ preferences for them. Its visual attribute highlights offer an interpretable connection between a recommended garment and personalised preference. The explanation target is consequently different from a textual rule citation: it concerns which visual attributes help account for a recommendation.

Lin et al. [30] provide a closer precedent for natural-language fashion explanations. Their neural outfit recommendation model jointly learns outfit matching and comment generation. Mutual attention supports visual matching, while cross-modality attention supplies visual features to a recurrent comment generator. Recommendation and language generation share a trained model, and generated comments are evaluated against human comments using BLEU and ROUGE. This establishes a substantive connection between outfit recommendation and explanatory text. Reference-text similarity, however, answers a different question from whether each generated proposition is entailed by a saved decision record.

The contrast with Hou et al. is instructive. Visual highlighting exposes attribute preferences, whereas Lin et al. generate a sentence about a matching outfit. Both make recommendation more interpretable, but they expose different objects and need different evaluation criteria. The present study builds on this distinction by asking about support for individual statements relative to a symbolic record retained during ranking.

Outside fashion, PEPLER integrates user and item identifiers into pretrained language models through personalised prompt learning [31]. It investigates discrete and continuous prompts, together with training strategies that connect recommendation information to generated explanations. P5 recasts several recommendation tasks, including explanation generation, in a common text-to-text framework [32]. These approaches demonstrate how recommendation information can condition language generation. They also show why fluent, personalised output needs a separate source-support test when the intended claim is evidential faithfulness. Neither identifier conditioning nor a shared language objective automatically supplies that test.

### 2.4.4 Limits of symbolic evidence

An interpretable component is not automatically correct. A generic rule may be sensible in the abstract but only partially applicable to a specific query-candidate pair. Semantic retrieval may select a rule whose antecedent is not established. Reliability categories supplied with a rule base are not empirical probabilities. A faithful explanation can therefore accurately report questionable evidence.

This distinction separates three evaluation targets. Recommendation metrics examine whether the hybrid system ranks held-out outfit items. Evidence-participation diagnostics examine whether the rule component materially changes selection and whether diverse rules are used. Explanation metrics examine whether generated language matches the stored trace and avoids unsupported instance-level claims. No single target validates the other two.

A symbolic trace supplies a record against which language can be assessed. Its evidential value depends on the rule content and its applicability to the case. A generator may accurately paraphrase a questionable rule, or overstate a reasonable conditional rule. Source support and rule validity therefore remain separate assessment tasks.

## 2.5 Retrieval-augmented generation and cited explanations

### 2.5.1 Retrieval as external context

RAG combines parametric generation with retrieved external information [13]. It has become a common strategy for improving factuality and updating knowledge without retraining the generator. In recommendation, retrieved reviews, catalogue fields, knowledge-graph facts, or domain guidance can support conversational answers and item justifications.

However, “retrieved,” “visible,” and “used” describe different relationships. A document can be retrieved but excluded from a prompt; it can be displayed but ignored by the generator; it can influence wording without having influenced item selection. Standard RAG commonly grounds the answer in visible context, but it does not necessarily connect that context to the upstream recommendation decision.

The connection to recommendation depends on when retrieval occurs. Rules retrieved during ranking can be retained for explanation; rules retrieved after selection provide supporting context for a decision already made. Both are useful designs, but only the former directly records the contribution of the retrieved component to item selection.

### 2.5.2 Hallucination, unsupportedness, and contradiction

Hallucination terminology varies across language-generation research. Ji et al. [23] review factual inconsistency and distinguish errors relative to sources from errors relative to world knowledge. For this study, the supplied evidence boundary is more observable than world truth. A claim is unsupported when A and B do not entail it, contradicted when the supplied evidence entails its opposite, and not verifiable when the evidence is insufficient for the applicable schema.

This vocabulary matters in fashion. If a model calls a bag leather when neither item text nor trace establishes material, the claim may happen to be true. The experiment can show that it is unverified by supplied evidence, not that it is factually false. Conversely, contradiction is rare because sparse catalogue context seldom states the opposite of a generated style assertion. Collapsing unsupported and contradicted categories would inflate the apparent detection of falsehood.

This distinction also affects denominators. A support rate calculated only for concrete product assertions describes a different set of claims from one that includes subjective styling advice. An evaluation should state which claims are eligible, how evidence is supplied and how missing judgements are handled.

### 2.5.3 Citations as claim-source relations

Gao et al. [14] introduce ALCE, evaluating cited generation through fluency, answer correctness and citation quality. Citation recall concerns whether statements receive supporting citations; citation precision concerns the relevance of the attached citations. These dimensions distinguish a well-written answer from one whose individual claims are supported by its references. Zhang et al. [15] subsequently compare fine-grained citation-faithfulness metrics, including their treatment of full, partial and absent support. Their results caution against assuming that different automatic metrics measure entailment equally well.

Rashkin et al. [36] formulate attribution to identified sources through the AIS framework. The evaluation asks whether an output can be supported by the supplied source, which makes the evidence boundary explicit. This is useful for recommendation because an assertion can be plausible in general yet unsupported by a particular product record. Source attribution also differs from causal explanation: a document that supports a sentence may have had no role in selecting the item.

FActScore decomposes long-form generated text into atomic facts and assesses the proportion supported by a knowledge source [37]. Its motivation is that one response can contain both supported and unsupported information. Adapting this principle to recommendation requires care over claim boundaries, conditional style advice and the source against which support is assessed. It also requires retaining the information needed for the intended metric. Claim-level entailment labels alone do not establish citation precision or coverage if the underlying citation relations and eligible-claim denominator are unavailable.

## 2.6 Faithfulness and evaluation

### 2.6.1 Plausibility, faithfulness, and the object of explanation

Jacovi and Goldberg [10] argue that faithfulness must be defined relative to a model and an explanation target. An explanation should correspond to the process it purports to describe rather than merely satisfy human expectations. Wiegreffe and Pinter [11] likewise show that debates about explanation require explicit claims and tests. Lyu et al. [12] organise faithful-explanation research into similarity-based, model-internal, gradient, counterfactual, and self-explaining approaches, illustrating that no single measure applies universally.

For a hybrid recommender, the object of explanation must be stated precisely. The CLIP component produces a latent compatibility score; the rule component produces an auditable score from up to five eligible contributions. B is a complete record of the latter but not the former. “Decision-trace faithfulness” in this thesis therefore means faithfulness to the symbolic evidence trace used within the decision, not full causal explanation of the hybrid model.

Turpin et al. [35] show that chain-of-thought explanations can omit factors that influence model answers, including biasing features in prompts. Their experiments concern reasoning tasks rather than fashion recommendation, but they provide a methodological warning: a generated rationale cannot be accepted as a faithful account merely because it is coherent. A controlled comparison of evidence visibility provides a narrower test of how a specified source changes explanatory language.

### 2.6.2 Functional and human-grounded evaluation

Explanation evaluation can be functionally grounded, application grounded, or human grounded. Functional measures test formal or computational properties without users. Human-grounded experiments use simplified tasks with people, while application-grounded work evaluates explanations with intended users or domain experts. Doshi-Velez and Kim [28] set out this distinction to connect evaluation design to the kind of interpretability claim being made.

Functional assessment is particularly useful when large numbers of outputs must be checked against explicit evidence. Its conclusions depend on the evaluator and operational definitions. Human-grounded work is still needed for questions about comprehension, usefulness and trust.

ARES trains judges for context relevance, answer faithfulness and answer relevance, and uses human annotations in its estimation procedure [24]. RAGAs supplies a complementary framework for automated assessment of retrieval-augmented outputs, including faithfulness and relevance [38]. Both make evaluation more scalable. Their validation procedures cannot be assumed to carry over to a different local verifier, domain or claim schema; those require their own calibration.

### 2.6.3 Atomic claims and aggregation

Whole-response labels can hide mixed support, motivating atomic evaluation in FActScore [37]. An explanation may contain one trace-supported styling relation, two unsupported product attributes, and a correct item identity. Atomic claim extraction enables these components to be assessed separately. It also introduces boundary decisions: conjunctions may be split inconsistently, pronouns may obscure the target item, and conditional language may be converted into overly definite propositions.

Both micro and macro aggregation are therefore useful. Claim-micro rates weight explanations with more extracted claims more heavily. Explanation-macro rates first calculate within-explanation proportions and then average units. Paired macro differences compare the same case-generator combination across conditions, while clustered bootstrap intervals recognise that several generator outputs derive from the same recommendation case.

Eligibility also changes the interpretation of a support rate. An explanation containing no claim within the assessment scope supplies no denominator for that measure. Comparisons should therefore report the eligible populations and account for differences in which kinds of claims the generators make. Chapter 3 applies this principle to the restricted item-fact measure.

### 2.6.4 Length and evaluator dependence

Explanation length affects both the number of propositions available for assessment and the reader?s experience of an answer. It is consequently useful to distinguish the proportion of supported claims from their density within the text. Any benefit to readability would require a separate user study.

Zheng et al. [39] identify position, verbosity and self-enhancement biases in LLM judgements. Although their experiments assess answer quality rather than this thesis’s exact entailment task, the results show why output length and judge identity deserve attention. Normalising supported claims by words can describe one aspect of length dependence, but it does not isolate all changes in content selection or rhetoric.

Recent work extends these concerns to longer contexts and deployed recommendation. FACTS Grounding separates fulfilment of a user request from grounding in an input document and combines several judges to reduce evaluation bias [40]. Kong et al. [41] describe a lifecycle for judges of recommendation explanations, using human-labelled benchmarks, rubric refinement and continuing alignment checks. The latter is a 2026 preprint reporting a production setting; its findings should not be transferred directly to a small offline fashion study. Together, these studies support treating evaluator calibration as an empirical requirement rather than assuming that assigning different models to extraction and verification establishes accuracy.

## 2.7 Comparative synthesis and research gap

### 2.7.1 Comparison of representative research

Table 2.1 compares the closest strands by the object they explain and the evidence they evaluate. The comparison identifies differences in research questions; it does not rank the studies on a common performance scale.

*Table 2.1. Explanation targets and evaluation boundaries in related work.*

| Study | Explanation or representation | Boundary relevant to this study |
|---|---|---|
| Hou et al. [29] | Personalised visual attribute highlights | Attribute preference differs from sentence-level source support. |
| Lin et al. [30] | Joint outfit matching and comment generation | BLEU and ROUGE assess reference-text similarity. |
| Li et al. [21] | Attribute-level pairing knowledge | Interpretable compatibility differs from auditing free-form explanations. |
| Xian et al.; Zhu et al. [7,8] | Paths and logic participating in recommendation | Mechanism linkage motivates retaining decision evidence. |
| PEPLER; P5 [31,32] | Language conditioned on recommendation information | Conditioning requires a separate faithfulness test. |
| Zhai et al. [22] | Controllable outfit generation | The task produces outfits, rather than auditing explanations of locked items. |
| Gao et al.; Rashkin et al. [14,36] | Citation and source attribution | Source support does not itself establish participation in ranking. |
| Min et al. [37] | Atomic factual support | Claim decomposition requires a domain-specific evidence definition. |
| ARES; RAGAs [24,38] | Automated RAG assessment | Judge validity depends on calibration and task transfer. |
| Zheng et al.; Kong et al. [39,41] | Judge bias and operational evaluation | Independent human assessment remains relevant. |

### 2.7.2 Research gap and scope

The reviewed work already connects fashion recommendation to interpretable attributes and generated comments [29,30,21]. Knowledge-graph and logic-based systems also link recommendation to interpretable reasoning [7,8]. The contribution sought here is therefore a specific combination of provenance and evaluation: retaining the rules that numerically contributed to a hybrid ranking, locking the selected item, and varying whether an explanation generator can see that same record.

This question joins two bodies of evidence. Recommendation research supplies mechanisms that expose paths, rules or attributes. Attribution and citation research supplies methods for assessing whether individual statements are supported by identified sources [14,36,37]. Combining them makes it possible to ask whether visibility of a retained ranking trace improves measured support, while keeping recommendation identity constant.

Several boundaries follow from the review. The symbolic trace explains only its own contribution to a hybrid score. A positive source-support result does not establish that the rule is valid for every context, and automated judgements require calibration before they can be treated as semantic ground truth [10,24,39]. User-experience benefits also require their own assessment [9,33]. Chapter 3 uses these boundaries to define a controlled offline study, with recommendation effectiveness, claim support and citation entailment reported separately.

## 2.8 Chapter summary

Fashion recommendation research has used visual attributes, generated comments, knowledge-graph paths and rules to make decisions more interpretable. Attribution research offers methods for checking individual statements against sources. This thesis tests whether showing a generator the rules retained during ranking changes its explanation of a fixed selected item. Chapter 3 defines the comparison and measures ranking effectiveness, source support and citation entailment separately. The experiment does not measure user experience or independently validate its automated judges.

## References

[1] McAuley, J. et al. (2015) ‘Image-based recommendations on styles and substitutes’, *Proceedings of SIGIR 2015*, pp. 43–52. https://doi.org/10.1145/2766462.2767755.

[2] Han, X. et al. (2017) ‘Learning fashion compatibility with bidirectional LSTMs’, *Proceedings of the 25th ACM International Conference on Multimedia*, pp. 1078–1086. https://doi.org/10.1145/3123266.3123394.

[3] Vasileva, M.I. et al. (2018) ‘Learning type-aware embeddings for fashion compatibility’, *Computer Vision – ECCV 2018*, LNCS 11220, pp. 405–421. https://doi.org/10.1007/978-3-030-01270-0_24.

[4] Cucurull, G. et al. (2019) ‘Context-aware visual compatibility prediction’, *Proceedings of CVPR 2019*, pp. 12617–12626. https://openaccess.thecvf.com/content_CVPR_2019/html/Cucurull_Context-Aware_Visual_Compatibility_Prediction_CVPR_2019_paper.html.

[5] Radford, A. et al. (2021) ‘Learning transferable visual models from natural language supervision’, *Proceedings of ICML 2021*, 139, pp. 8748–8763. https://proceedings.mlr.press/v139/radford21a.html.

[6] Zhang, Y. and Chen, X. (2020) ‘Explainable recommendation: A survey and new perspectives’, *Foundations and Trends in Information Retrieval*, 14(1), pp. 1–101. https://doi.org/10.1561/1500000066.

[7] Xian, Y. et al. (2019) ‘Reinforcement knowledge graph reasoning for explainable recommendation’, *Proceedings of SIGIR 2019*, pp. 285–294. https://doi.org/10.1145/3331184.3331203.

[8] Zhu, Y. et al. (2021) ‘Faithfully explainable recommendation via neural logic reasoning’, *Proceedings of NAACL 2021*, pp. 3083–3090. https://doi.org/10.18653/v1/2021.naacl-main.245.

[9] Knijnenburg, B.P. et al. (2012) ‘Explaining the user experience of recommender systems’, *User Modeling and User-Adapted Interaction*, 22(4–5), pp. 441–504. https://doi.org/10.1007/s11257-011-9118-4.

[10] Jacovi, A. and Goldberg, Y. (2020) ‘Towards faithfully interpretable NLP systems: How should we define and evaluate faithfulness?’, *Proceedings of ACL 2020*, pp. 4198–4205. https://doi.org/10.18653/v1/2020.acl-main.386.

[11] Wiegreffe, S. and Pinter, Y. (2019) ‘Attention is not not explanation’, *Proceedings of EMNLP-IJCNLP 2019*, pp. 11–20. https://doi.org/10.18653/v1/D19-1002.

[12] Lyu, Q. et al. (2024) ‘Towards faithful model explanation in NLP: A survey’, *Computational Linguistics*, 50(2), pp. 657–723. https://doi.org/10.1162/coli_a_00511.

[13] Lewis, P. et al. (2020) ‘Retrieval-augmented generation for knowledge-intensive NLP tasks’, *Advances in Neural Information Processing Systems*, 33, pp. 9459–9474. https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html.

[14] Gao, T. et al. (2023) ‘Enabling large language models to generate text with citations’, *Proceedings of EMNLP 2023*, pp. 6465–6488. https://doi.org/10.18653/v1/2023.emnlp-main.398.

[15] Zhang, W. et al. (2024) ‘Towards fine-grained citation evaluation in generated text: A comparative analysis of faithfulness metrics’, *Proceedings of INLG 2024*, pp. 427–439. https://doi.org/10.18653/v1/2024.inlg-main.35.

[16] Tan, R. et al. (2019) ‘Learning similarity conditions without explicit supervision’, *Proceedings of ICCV 2019*, pp. 10373–10382. https://doi.org/10.1109/ICCV.2019.01047.

[17] Kang, W.-C. et al. (2019) ‘Complete the look: Scene-based complementary product recommendation’, *Proceedings of CVPR 2019*, pp. 10532–10541. https://openaccess.thecvf.com/content_CVPR_2019/html/Kang_Complete_the_Look_Scene-Based_Complementary_Product_Recommendation_CVPR_2019_paper.html.

[18] Järvelin, K. and Kekäläinen, J. (2002) ‘Cumulated gain-based evaluation of IR techniques’, *ACM Transactions on Information Systems*, 20(4), pp. 422–446. https://doi.org/10.1145/582415.582418.

[19] Reimers, N. and Gurevych, I. (2019) ‘Sentence-BERT: Sentence embeddings using Siamese BERT-networks’, *Proceedings of EMNLP-IJCNLP 2019*, pp. 3982–3992. https://doi.org/10.18653/v1/D19-1410.

[20] Wang, W. et al. (2020) ‘MiniLM: Deep self-attention distillation for task-agnostic compression of pre-trained transformers’, *Advances in Neural Information Processing Systems*, 33, pp. 5776–5788. https://proceedings.neurips.cc/paper/2020/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html.

[21] Li, Y. et al. (2024) ‘Explainable fashion compatibility prediction: An attribute-augmented neural framework’, *Electronic Commerce Research and Applications*, 68, Article 101451. https://doi.org/10.1016/j.elerap.2024.101451.

[22] Zhai, Y. et al. (2025) ‘Text2Outfit: Controllable Outfit Generation with Multimodal Language Models’, *Proceedings of ICCV 2025*, pp. 16165–16174. https://doi.org/10.1109/ICCV51701.2025.01500.

[23] Ji, Z. et al. (2023) ‘Survey of hallucination in natural language generation’, *ACM Computing Surveys*, 55(12), Article 248. https://doi.org/10.1145/3571730.

[24] Saad-Falcon, J. et al. (2024) ‘ARES: An automated evaluation framework for retrieval-augmented generation systems’, *Proceedings of NAACL 2024*, pp. 338–354. https://doi.org/10.18653/v1/2024.naacl-long.20.

[25] Chia, P.J. et al. (2022) ‘Contrastive language and vision learning of general fashion concepts’, *Scientific Reports*, 12, Article 18958. https://doi.org/10.1038/s41598-022-23052-9.

[28] Doshi-Velez, F. and Kim, B. (2017) ‘Towards a rigorous science of interpretable machine learning’, arXiv:1702.08608. https://arxiv.org/abs/1702.08608.

[29] Hou, M. et al. (2019) ‘Explainable Fashion Recommendation: A Semantic Attribute Region Guided Approach’, *Proceedings of IJCAI 2019*, pp. 4681–4688. https://doi.org/10.24963/ijcai.2019/650.

[30] Lin, Y. et al. (2020) ‘Explainable Outfit Recommendation with Joint Outfit Matching and Comment Generation’, *IEEE Transactions on Knowledge and Data Engineering*, 32(8), pp. 1502–1516. https://doi.org/10.1109/TKDE.2019.2906190.

[31] Li, L. et al. (2023) ‘Personalized Prompt Learning for Explainable Recommendation’, *ACM Transactions on Information Systems*, 41(4), Article 103. https://doi.org/10.1145/3580488.

[32] Geng, S. et al. (2022) ‘Recommendation as Language Processing (RLP): A Unified Pretrain, Personalized Prompt & Predict Paradigm (P5)’, *Proceedings of RecSys 2022*, pp. 299–315. https://doi.org/10.1145/3523227.3546767.

[33] Tintarev, N. and Masthoff, J. (2007) ‘A Survey of Explanations in Recommender Systems’, *IEEE 23rd International Conference on Data Engineering Workshop*, pp. 801–810. https://doi.org/10.1109/ICDEW.2007.4401070.

[34] Jain, S. and Wallace, B.C. (2019) ‘Attention is not Explanation’, *Proceedings of NAACL 2019*, pp. 3543–3556. https://doi.org/10.18653/v1/N19-1357.

[35] Turpin, M. et al. (2023) ‘Language Models Don’t Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting’, *Advances in Neural Information Processing Systems*, 36. https://proceedings.neurips.cc/paper_files/paper/2023/hash/ed3fea9033a80fea1376299fa7863f4a-Abstract-Conference.html.

[36] Rashkin, H. et al. (2023) ‘Measuring Attribution in Natural Language Generation Models’, *Computational Linguistics*, 49(4), pp. 777–840. https://aclanthology.org/2023.cl-4.2/.

[37] Min, S. et al. (2023) ‘FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation’, *Proceedings of EMNLP 2023*, pp. 12076–12100. https://doi.org/10.18653/v1/2023.emnlp-main.741.

[38] Es, S. et al. (2024) ‘RAGAs: Automated Evaluation of Retrieval Augmented Generation’, *Proceedings of EACL 2024: System Demonstrations*, pp. 150–158. https://doi.org/10.18653/v1/2024.eacl-demo.16.

[39] Zheng, L. et al. (2023) ‘Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena’, *Advances in Neural Information Processing Systems*, 36. https://proceedings.neurips.cc/paper_files/paper/2023/hash/91f18a1287b398d378ef22505bf41832-Abstract-Datasets_and_Benchmarks.html.

[40] Jacovi, A. et al. (2025) ‘The FACTS Grounding Leaderboard: Benchmarking LLMs’ Ability to Ground Responses to Long-Form Input’, *arXiv preprint*, arXiv:2501.03200. https://doi.org/10.48550/arXiv.2501.03200.

[41] Kong, E.Y. et al. (2026) ‘The Lifecycle of LLM-as-a-Judge for Large-Scale Recommendation Explanations’, *arXiv preprint*, arXiv:2608.18300v3. https://arxiv.org/abs/2608.18300v3.
