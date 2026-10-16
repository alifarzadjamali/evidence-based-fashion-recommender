---
title: "Evidence-Constrained Multimodal Fashion Recommendation with Trace-Grounded Explanations"
author: "Ali Jamali"
date: "November 2026"
subtitle: |
  A thesis submitted in partial fulfilment of the requirements for the degree of Master of Philosophy  
  University of Salford  
  School of Science, Engineering and Environment  
  Supervisors: Dr. Taha Mansouri - Dr. Ali Alameer
geometry: "a4paper,margin=30mm"
fontsize: 12pt
linestretch: 1.5
colorlinks: true
linkcolor: black
urlcolor: blue
toc: false
toc-depth: 3
numbersections: false
header-includes:
  - |
    ```{=latex}
    \usepackage{microtype}
    \usepackage{booktabs}
    \usepackage{longtable}
    \usepackage{graphicx}
    \usepackage{float}
    \usepackage{needspace}
    \usepackage{etoolbox}
    \AtBeginEnvironment{longtable}{\small}
    ```
include-before:
  - |
    ```{=latex}
    \clearpage
    ```
---

# Contents

\newpage

# List of figures

- **Figure 3.1.** Recommendation, locked evidence and paired explanation assessment.
- **Figure 4.1.** Paired explanation contrasts with 95% case-clustered bootstrap intervals.

\newpage

# List of tables

- **Table 2.1.** Explanation targets and evaluation boundaries in related work.
- **Table 4.1.** Micro-averaged recommendation effectiveness on 1,000 frozen test cases.
- **Table 4.2.** Overall paired explanation contrasts (Rule-RAG minus No-RAG).
- **Table 4.3.** Recorded citation-entailment labels by explanation condition.
- **Table A.1.** Accepted records by generator, condition and pipeline stage.
- **Table A.2.** Complete generator pairs for support and restricted UIFR.
- **Table A.3.** MiniLM text: recommendation estimates and 95% intervals.
- **Table A.4.** CLIP image: recommendation estimates and 95% intervals.
- **Table A.5.** CLIP text: recommendation estimates and 95% intervals.
- **Table A.6.** Fused CLIP: recommendation estimates and 95% intervals.
- **Table A.7.** Evidence rerank: recommendation estimates and 95% intervals.

\newpage
# Declaration

I declare that this thesis is my own work, undertaken during my Master of Philosophy programme at the University of Salford. Sources of information, text, data and images are acknowledged in the thesis. No part of this thesis has previously been published or submitted for an academic award or for publication.

\newpage

# Abbreviations

| Abbreviation | Meaning |
|---|---|
| CNN | Convolutional neural network |
| DFH | Discounted first-hit score |
| FLOPs | Floating-point operations |
| LSTM | Long short-term memory |
| NLP | Natural language processing |
| pp | Percentage points |
| RQ | Research question |
| SHA-256 | Secure Hash Algorithm, 256-bit |
| CI | Confidence interval |
| CLIP | Contrastive Language--Image Pre-training |
| FITB | Fill in the blank |
| HR | Hit rate |
| KB | Knowledge base |
| KG | Knowledge graph |
| LLM | Large language model |
| MRR | Mean reciprocal rank |
| NDCG | Normalised discounted cumulative gain |
| RAG | Retrieval-augmented generation |
| UIFR | Unsupported Item-Fact Rate |

\newpage

# Abstract

This thesis examines whether fashion recommendation explanations reflect the evidence used to rank
items. An evidence-constrained pipeline links recommendation and explanation through an explicit
decision trace. Frozen CLIP image and text representations rank same-category candidates from
held-out Polyvore outfits. A supplied, source-linked knowledge base of 200 fashion rules
supplies a separate evidence score; up to five eligible rules are retained as the symbolic trace
used in reranking. The selected item is then locked, and paired No-RAG and Rule-RAG explanations
differ only in access to that trace and its grounding instructions.

The recommendation experiment contains 1,000 cases across five categories. Fused CLIP was the
strongest tested method overall on the conventional top-five, top-ten, discounted first-hit and reciprocal-rank
measures. Evidence reranking retained 97.4% of fused CLIP's HR@10 (23.1% to 22.5%), while
making rule contributions inspectable; the other reported ranking measures also declined. The explanation experiment used
500 evidence-eligible cases and three local generators, yielding 2,969 accepted explanations and
16,804 verified claims. Under generator-specific complete pairing
and case-clustered inference, trace access increased reranking-trace claim support by 21.02
percentage points (95% CI 19.72--22.37) and full-KB claim support by 21.40 points (20.11--22.71).
Trace-supported claims per 100 words increased by 1.60 (1.48--1.72). The common-reference
Unsupported Item-Fact Rate was inconclusive because only 53 complete pairs were eligible.

The pipeline preserves the symbolic evidence used in reranking, reuses it during explanation, and
evaluates generated claims against explicit source boundaries. The results establish a substantial
source-support gain under the frozen automated evaluator, alongside a modest absolute HR@10
reduction in the separate ranking comparison. Independent human assessment and refinement of
the evidence-aware ranking objective are priorities for further work.

\newpage

# Chapter 1: Introduction
## 1.1 Background and motivation

Fashion recommendation requires a model of how garments work together. Two similar garments may be substitutes, while visually different items may complement one another in an outfit. McAuley et al. showed that product images can help model both compatibility and substitution (1). Later work represented outfits as sequences, type-specific relations and graphs (2, 3, 4). These representations use information about item context and category when ranking candidates.

Modern fashion catalogues also contain product text. Titles and descriptions may identify category, brand, material, or style terms that are difficult to infer reliably from pixels, while images contain appearance information that catalogue text may omit. Contrastive vision-language models provide a practical way to combine these signals within a shared representation (5). A multimodal ranker can therefore exploit complementary image and text evidence without requiring every visual property to be translated into language.

Ranking performance leaves the reason for an individual recommendation unclear. A fluent answer to a user's question may omit the information that influenced the ranking. Explainable recommendation research has proposed features, reviews, knowledge-graph paths and generated language as ways to communicate reasons (6, 7, 8). Whether those reasons reflect the decision process requires a separate test.

Generative language models can turn sparse catalogue information into style advice, sometimes adding colours, materials, comfort claims or occasions absent from their input. Source inconsistency is a recognised problem in natural-language generation (9). An explanation may sound reasonable to a reader while giving an inaccurate account of the mechanism or evidence behind a decision (10, 11, 12). In fashion recommendation, this leaves open whether a fluent rationale describes the selected product and its ranking evidence.

Retrieval-augmented generation offers a partial response by displaying external context during generation (13). Yet retrieved context and decision evidence are not necessarily the same thing. Documents retrieved after an item has been selected may support a persuasive account without showing that those documents participated in selection. Furthermore, access to relevant evidence does not ensure that every generated claim is entailed by it. Citation identifiers can improve auditability, but a citation is only informative when its source actually supports the associated claim (14, 15).

This thesis connects recommendation and explanation through a record produced during ranking. The system combines CLIP image and text representations with a score derived from curated fashion rules. For each candidate, it retains up to five eligible rules and their score contributions. The selected recommendation and its symbolic trace are frozen after reranking, before explanation generation. The trace records the rules that contributed numerically to the decision.

The explanation experiment then holds the selected item constant. For each case and language generator, a No-RAG explanation receives common context A: the request and frozen query and recommended-item identities, categories, and catalogue text. Its paired Rule-RAG explanation receives the same A plus exact trace B. This design isolates access to the symbolic decision trace more closely than comparing explanations of different recommendations. It also permits a necessary terminological distinction: agreement with hidden B is post-hoc decision-trace alignment for No-RAG, while agreement with visible B is decision-trace faithfulness for Rule-RAG.

The study remains deliberately bounded. Images participate in representation and ranking, but they are not captioned and do not become textual explanation evidence. The task is sampled, same-category, controlled-pool ranking over held-out Polyvore outfits rather than personalised, full-catalogue serving. The symbolic trace explains the fashion-rule component of a hybrid reranker, not every internal computation performed by CLIP. Explanation outcomes are measured through a frozen automated pipeline in which Qwen 3.5 9B extracts atomic claims and Phi-4 14B verifies them against the supplied sources. This role separation strengthens auditability, but the results remain operational system evaluation rather than human-validated ground truth.

## 1.2 Problem statement

Existing fashion recommendation research provides increasingly capable representations of item compatibility, but conventional ranking metrics answer only whether relevant items are placed near the top of a candidate list. They do not show whether an explanation accurately describes information used by the system. This creates a gap between recommendation effectiveness and explanation faithfulness.

The gap has three parts. First, high-performing multimodal representations are generally latent. Although an image and its catalogue text can jointly influence a similarity score, the score does not naturally provide a concise verbal account of the decision. Translating latent similarity into unrestricted prose risks presenting an interpretation as if it were an observed causal trace.

Second, post-hoc natural-language explanations can exploit information that did not participate in the recommendation or introduce details absent from the supplied context. In fashion, this problem is particularly visible when an explanation attributes colour, material, comfort or suitability to a product whose catalogue description supplies no such information. An unsupported assertion is not necessarily false in the world, but it is not justified by the evidence available to the generator. Treating unsupported and contradicted claims as equivalent would overstate what the experiment can establish.

Third, standard explanation-quality scores can conceal source-specific failures. Fluency, clarity, specificity, and general usefulness do not directly measure whether claims match the actual decision trace or whether cited rules entail them. A system may receive a high holistic score while misapplying a conditional rule or attaching a valid-looking identifier to an unsupported claim. Claim-level attribution and citation evaluation address this problem by checking support against specified sources (14, 16, 17).

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

\newpage

# Chapter 2: Literature Review
## 2.1 Introduction

This chapter positions the thesis at the intersection of fashion compatibility modelling, multimodal information retrieval, explainable recommendation, retrieval-augmented generation (RAG), and explanation-faithfulness evaluation. These areas address related but distinct questions. Fashion recommendation asks which item is compatible with a query or partial outfit. Multimodal retrieval asks how image and text signals should be represented and combined. Explainable recommendation asks how the basis of a recommendation can be communicated. RAG supplies external context to a generator. Faithfulness research asks whether an explanation accurately reflects the evidence or process it claims to explain.

The review concentrates on the relationship between recommendation evidence and explanatory language. Its central question is how prior work connects an interpretable recommendation mechanism to an explanation, and what evidence is needed to assess that connection. This requires distinguishing predictive performance, source attribution and user experience.

The review proceeds in six parts. Section 2.2 examines the development of fashion compatibility and outfit recommendation. Section 2.3 discusses multimodal representations and the distinction between latent compatibility and verbal evidence. Section 2.4 reviews explainable and knowledge-aware recommendation. Section 2.5 considers generative explanation, RAG, citations, and unsupported claims. Section 2.6 examines faithfulness definitions and evaluation methods. Section 2.7 compares representative studies and derives the research gap that leads directly to the methodology in Chapter 3.

## 2.2 Fashion compatibility and outfit recommendation

### 2.2.1 From visual similarity to compatibility

Visual similarity alone cannot identify every useful addition to an outfit. Two nearly identical black shoes may be substitutes, while a shoe and a pair of trousers can be complementary. A fashion representation must account for relations between item types when ranking additions to an outfit.

McAuley et al. (1) learned visual relationships for styles and substitutes from large-scale product data. Their results showed that convolutional image features can represent compatibility derived from observed relationships. The learned distances support recommendation, although they do not explain why a particular candidate complements a query.

Han et al. (2) treated an outfit as an ordered sequence and learned compatibility with bidirectional LSTMs. The model captures dependencies across outfit components and supports fill-in-the-blank evaluation. Its sequence representation uses an imposed item order, and its learned state does not provide an inspectable language account of an individual decision.

Vasileva et al. (3) explicitly distinguished similarity from compatibility through type-aware embeddings. Their model learns item-type-specific relations so that comparisons can be conditioned on categories such as tops, bottoms, or shoes. This matches the intuition that different features matter for different cross-category relationships. The associated Polyvore-Outfits dataset and fill-in-the-blank tasks became important resources for compatibility research. Their type-aware treatment also makes category restrictions an explicit part of evaluation design.

### 2.2.2 Context, graphs, and outfit structure

Cucurull et al. (4) argued that compatibility should depend on item context and proposed graph neural representations conditioned on products known to be compatible. Their results on Polyvore, Fashion-Gen, and Amazon data demonstrated the benefit of relational context over isolated pairwise comparison. Graph-based methods can model higher-order outfit structure, but their explanatory value depends on whether graph paths or learned relationships are exposed and demonstrably used in prediction.

Tan et al. (18) learned similarity conditions without requiring explicit condition labels at test time. By representing distinct semantic subspaces as latent variables, the model improved generalisation across fashion datasets. This line of work illustrates a recurring trade-off: more flexible latent representations can improve predictive capability while making a human-readable account of an individual decision less direct.

Kang et al. (19) extended complementary recommendation to scene images in *Complete the Look*. Compared with catalogue images, scene inputs provide context about an existing outfit and its surroundings. The resulting task involves locating useful visual context as well as identifying compatible products. It should therefore be distinguished from the catalogue-item setting used in many Polyvore studies.

The studies model different relations: substitution, sequence context, item type and scene context. Their task results are consequently difficult to compare directly. A learned compatibility score also leaves the basis of an individual recommendation unclear. Section 2.4 examines fashion models that address explanation directly.

### 2.2.3 Evaluation conventions and their limits

Outfit-compatibility classification and fill-in-the-blank (FITB) evaluation test related but different abilities. Classification distinguishes compatible from constructed incompatible outfits; FITB asks a model to recover a missing item among alternatives (2, 3). Retrieval measures such as hit rate and reciprocal rank locate relevant items in an ordered list, while discounted gain rewards relevant results near the top (20). Comparisons require a common relevance definition and candidate protocol.

The Polyvore protocols in Han et al. and Vasileva et al. derive positives from curated outfits (2, 3). This provides an observable relevance label. A limitation of that label is that an item absent from a particular outfit may still be a plausible alternative. This thesis therefore interprets co-occurrence as an offline evaluation proxy, rather than a complete judgement of fashion compatibility.

Vasileva et al. distinguish disjoint and non-disjoint settings when examining generalisation (3). Their treatment shows why the unit of separation matters: an unseen outfit may contain familiar items. Split construction and duplicate checks should consequently be reported alongside ranking scores. The specific controls used in this study are described in Chapter 3.

## 2.3 Multimodal representation and evidence boundaries

### 2.3.1 Image and text as complementary signals

Catalogue text provides explicit product terms, while images represent appearance that descriptions may omit. CLIP learns aligned image and text representations and supports zero-shot transfer (5). Sentence-BERT instead produces sentence representations suitable for semantic similarity, and MiniLM provides a compact transformer architecture (21, 22). These resources make frozen retrieval baselines feasible, although their original training objectives differ from outfit compatibility.

FashionCLIP adapts contrastive image–text learning to fashion data (23), showing the value of domain-specific representation learning. Li et al. combine visual information and attributes in an explainable attribute-augmented framework, using an attribute-pair encoder to represent pairing knowledge (24). These approaches motivate stronger fashion representations, while also raising a separate evaluation question: which interpretable attributes support the explanation of an individual recommendation?

Zhai et al. (25) address controllable outfit generation in *Text2Outfit: Controllable Outfit Generation with Multimodal Language Models*. Their model supports text-to-outfit and seed-to-outfit tasks, predicting outfit composition and item representations. This extends the range of fashion tasks handled through language, but its generation objective differs from assessing the support of a written explanation for an already selected catalogue item. It provides relevant context without serving as a directly comparable baseline for the paired experiment here.

### 2.3.2 Representation is not textual evidence

An image embedding can inform a ranking without supplying verified textual attributes. Colour, silhouette, pattern, composition and other correlations may affect similarity, but their individual contributions are not recoverable from the score alone. An explanation that says “the burgundy trousers match the leather shoes” needs evidence for both attributes. Processing the images with CLIP does not establish that those attributes were represented explicitly or caused the ranking.

A useful distinction is between evidence available to the language generator and features used by the ranker. When a generator receives catalogue text and rules, its product assertions can be checked against those sources. Claims about image content require an additional visual-grounding assessment. Neither a cosine score nor a generic rule about matching colours establishes the colour of a particular item.

Jacovi and Goldberg distinguish an explanation that appears convincing from one that accurately reflects the process being explained (10). For a hybrid ranker, this requires specifying which component an explanation targets. A trace of rule contributions can expose the symbolic calculation while leaving the neural representation only partially interpreted.

## 2.4 Explainable recommender systems

### 2.4.1 Purposes and forms of recommendation explanation

Explanations in recommender systems serve several possible goals: transparency, scrutability, trust, effectiveness, persuasiveness, efficiency and satisfaction (26). These objectives can conflict. A persuasive explanation may increase acceptance without accurately exposing the recommendation process; a technically faithful trace may be difficult for a user to understand. Evaluation must therefore match the stated purpose.

Zhang and Chen (6) survey explainable recommendation approaches including neighbourhood, matrix-factorisation, topic, graph, deep-learning, and natural-language methods. Feature-based explanations can identify influential attributes; review-based methods can reuse user-authored evidence; path-based systems can expose relations between users and products. Natural-language generation can improve accessibility, but it introduces another model whose output may diverge from the recommendation evidence.

Knijnenburg et al. (27) provide a framework for the user experience of recommender systems. They relate objective system aspects to subjective perceptions, experience and interaction. This framework is relevant when asking how people respond to a recommendation; it does not supply a taxonomy of explanation methods. Automated source-support scores and user-experience measures therefore require separate interpretation.

### 2.4.2 Post-hoc and mechanism-linked explanations

Post-hoc explanations are produced after a prediction and may approximate its basis through surrogate features, attention, retrieved examples, or generated rationales. Their fidelity requires a test appropriate to the claimed explanation target (10, 12). Attention weights, for example, have generated substantial debate over when they constitute explanations and what kind of causal claim they support (28, 11). Jain and Wallace found that attention distributions could vary substantially without corresponding prediction changes, while Wiegreffe and Pinter questioned whether the proposed tests were sufficient to dismiss attention as an explanation. Their disagreement reinforces the need to specify both the explanatory claim and the test used to assess it.

Mechanism-linked approaches instead incorporate interpretable components into prediction. Policy-Guided Path Reasoning uses knowledge-graph paths to connect users and recommended items (7). LOGER combines knowledge-graph embeddings with neural logic rules and uses learned rule importance to guide path reasoning for explainable recommendation (8). These systems demonstrate that paths or rules can be part of recommendation rather than decoration added afterwards.

These studies establish that recommendation and interpretable reasoning can be connected within one architecture. The remaining question for a language interface is whether generated claims accurately communicate the recorded reasoning. A path or rule used by a recommender does not itself constrain every sentence subsequently produced by a language model.

### 2.4.3 Explainable fashion and personalised language generation

Explainable fashion recommendation predates large language models. Hou et al. (29) propose SAERS, which represents semantic clothing attributes and uses attention to model users’ preferences for them. Its visual attribute highlights offer an interpretable connection between a recommended garment and personalised preference. The explanation target is consequently different from a textual rule citation: it concerns which visual attributes help account for a recommendation.

Lin et al. (30) provide a closer precedent for natural-language fashion explanations. Their neural outfit recommendation model jointly learns outfit matching and comment generation. Mutual attention supports visual matching, while cross-modality attention supplies visual features to a recurrent comment generator. Recommendation and language generation share a trained model, and generated comments are evaluated against human comments using BLEU and ROUGE. This establishes a substantive connection between outfit recommendation and explanatory text. Reference-text similarity, however, answers a different question from whether each generated proposition is entailed by a saved decision record.

The contrast with Hou et al. is instructive. Visual highlighting exposes attribute preferences, whereas Lin et al. generate a sentence about a matching outfit. Both make recommendation more interpretable, but they expose different objects and need different evaluation criteria. The present study builds on this distinction by asking about support for individual statements relative to a symbolic record retained during ranking.

Outside fashion, PEPLER integrates user and item identifiers into pretrained language models through personalised prompt learning (31). It investigates discrete and continuous prompts, together with training strategies that connect recommendation information to generated explanations. P5 recasts several recommendation tasks, including explanation generation, in a common text-to-text framework (32). These approaches demonstrate how recommendation information can condition language generation. They also show why fluent, personalised output needs a separate source-support test when the intended claim is evidential faithfulness. Neither identifier conditioning nor a shared language objective automatically supplies that test.

### 2.4.4 Limits of symbolic evidence

An interpretable component is not automatically correct. A generic rule may be sensible in the abstract but only partially applicable to a specific query-candidate pair. Semantic retrieval may select a rule whose antecedent is not established. Reliability categories supplied with a rule base are not empirical probabilities. A faithful explanation can therefore accurately report questionable evidence.

This distinction separates three evaluation targets. Recommendation metrics examine whether the hybrid system ranks held-out outfit items. Evidence-participation diagnostics examine whether the rule component materially changes selection and whether diverse rules are used. Explanation metrics examine whether generated language matches the stored trace and avoids unsupported instance-level claims. No single target validates the other two.

A symbolic trace supplies a record against which language can be assessed. Its evidential value depends on the rule content and its applicability to the case. A generator may accurately paraphrase a questionable rule, or overstate a reasonable conditional rule. Source support and rule validity therefore remain separate assessment tasks.

## 2.5 Retrieval-augmented generation and cited explanations

### 2.5.1 Retrieval as external context

RAG combines parametric generation with retrieved external information (13). It has become a common strategy for improving factuality and updating knowledge without retraining the generator. In recommendation, retrieved reviews, catalogue fields, knowledge-graph facts, or domain guidance can support conversational answers and item justifications.

However, “retrieved,” “visible,” and “used” describe different relationships. A document can be retrieved but excluded from a prompt; it can be displayed but ignored by the generator; it can influence wording without having influenced item selection. Standard RAG commonly grounds the answer in visible context, but it does not necessarily connect that context to the upstream recommendation decision.

The connection to recommendation depends on when retrieval occurs. Rules retrieved during ranking can be retained for explanation; rules retrieved after selection provide supporting context for a decision already made. Both are useful designs, but only the former directly records the contribution of the retrieved component to item selection.

### 2.5.2 Hallucination, unsupportedness, and contradiction

Hallucination terminology varies across language-generation research. Ji et al. (9) review factual inconsistency and distinguish errors relative to sources from errors relative to world knowledge. For this study, the supplied evidence boundary is more observable than world truth. A claim is unsupported when A and B do not entail it, contradicted when the supplied evidence entails its opposite, and not verifiable when the evidence is insufficient for the applicable schema.

This vocabulary matters in fashion. If a model calls a bag leather when neither item text nor trace establishes material, the claim may happen to be true. The experiment can show that it is unverified by supplied evidence, not that it is factually false. Conversely, contradiction is rare because sparse catalogue context seldom states the opposite of a generated style assertion. Collapsing unsupported and contradicted categories would inflate the apparent detection of falsehood.

This distinction also affects denominators. A support rate calculated only for concrete product assertions describes a different set of claims from one that includes subjective styling advice. An evaluation should state which claims are eligible, how evidence is supplied and how missing judgements are handled.

### 2.5.3 Citations as claim-source relations

Gao et al. (14) introduce ALCE, evaluating cited generation through fluency, answer correctness and citation quality. Citation recall concerns whether statements receive supporting citations; citation precision concerns the relevance of the attached citations. These dimensions distinguish a well-written answer from one whose individual claims are supported by its references. Zhang et al. (15) subsequently compare fine-grained citation-faithfulness metrics, including their treatment of full, partial and absent support. Their results caution against assuming that different automatic metrics measure entailment equally well.

Rashkin et al. (16) formulate attribution to identified sources through the AIS framework. The evaluation asks whether an output can be supported by the supplied source, which makes the evidence boundary explicit. This is useful for recommendation because an assertion can be plausible in general yet unsupported by a particular product record. Source attribution also differs from causal explanation: a document that supports a sentence may have had no role in selecting the item.

FActScore decomposes long-form generated text into atomic facts and assesses the proportion supported by a knowledge source (17). Its motivation is that one response can contain both supported and unsupported information. Adapting this principle to recommendation requires care over claim boundaries, conditional style advice and the source against which support is assessed. It also requires retaining the information needed for the intended metric. Claim-level entailment labels alone do not establish citation precision or coverage if the underlying citation relations and eligible-claim denominator are unavailable.

## 2.6 Faithfulness and evaluation

### 2.6.1 Plausibility, faithfulness, and the object of explanation

Jacovi and Goldberg (10) argue that faithfulness must be defined relative to a model and an explanation target. An explanation should correspond to the process it purports to describe rather than merely satisfy human expectations. Wiegreffe and Pinter (11) likewise show that debates about explanation require explicit claims and tests. Lyu et al. (12) organise faithful-explanation research into similarity-based, model-internal, gradient, counterfactual, and self-explaining approaches, illustrating that no single measure applies universally.

For a hybrid recommender, the object of explanation must be stated precisely. The CLIP component produces a latent compatibility score; the rule component produces an auditable score from up to five eligible contributions. B is a complete record of the latter but not the former. “Decision-trace faithfulness” in this thesis therefore means faithfulness to the symbolic evidence trace used within the decision, not full causal explanation of the hybrid model.

Turpin et al. (33) show that chain-of-thought explanations can omit factors that influence model answers, including biasing features in prompts. Their experiments concern reasoning tasks rather than fashion recommendation, but they provide a methodological warning: a generated rationale cannot be accepted as a faithful account merely because it is coherent. A controlled comparison of evidence visibility provides a narrower test of how a specified source changes explanatory language.

### 2.6.2 Functional and human-grounded evaluation

Explanation evaluation can be functionally grounded, application grounded, or human grounded. Functional measures test formal or computational properties without users. Human-grounded experiments use simplified tasks with people, while application-grounded work evaluates explanations with intended users or domain experts. Doshi-Velez and Kim (34) set out this distinction to connect evaluation design to the kind of interpretability claim being made.

Functional assessment is particularly useful when large numbers of outputs must be checked against explicit evidence. Its conclusions depend on the evaluator and operational definitions. Human-grounded work is still needed for questions about comprehension, usefulness and trust.

ARES trains judges for context relevance, answer faithfulness and answer relevance, and uses human annotations in its estimation procedure (35). RAGAs supplies a complementary framework for automated assessment of retrieval-augmented outputs, including faithfulness and relevance (36). Both make evaluation more scalable. Their validation procedures cannot be assumed to carry over to a different local verifier, domain or claim schema; those require their own calibration.

### 2.6.3 Atomic claims and aggregation

Whole-response labels can hide mixed support, motivating atomic evaluation in FActScore (17). An explanation may contain one trace-supported styling relation, two unsupported product attributes, and a correct item identity. Atomic claim extraction enables these components to be assessed separately. It also introduces boundary decisions: conjunctions may be split inconsistently, pronouns may obscure the target item, and conditional language may be converted into overly definite propositions.

Both micro and macro aggregation are therefore useful. Claim-micro rates weight explanations with more extracted claims more heavily. Explanation-macro rates first calculate within-explanation proportions and then average units. Paired macro differences compare the same case-generator combination across conditions, while clustered bootstrap intervals recognise that several generator outputs derive from the same recommendation case.

Eligibility also changes the interpretation of a support rate. An explanation containing no claim within the assessment scope supplies no denominator for that measure. Comparisons should therefore report the eligible populations and account for differences in which kinds of claims the generators make. Chapter 3 applies this principle to the restricted item-fact measure.

### 2.6.4 Length and evaluator dependence

Explanation length affects both the number of propositions available for assessment and the reader?s experience of an answer. It is consequently useful to distinguish the proportion of supported claims from their density within the text. Any benefit to readability would require a separate user study.

Zheng et al. (37) identify position, verbosity and self-enhancement biases in LLM judgements. Although their experiments assess answer quality rather than this thesis’s exact entailment task, the results show why output length and judge identity deserve attention. Normalising supported claims by words can describe one aspect of length dependence, but it does not isolate all changes in content selection or rhetoric.

Recent work extends these concerns to longer contexts and deployed recommendation. FACTS Grounding separates fulfilment of a user request from grounding in an input document and combines several judges to reduce evaluation bias (38). Kong et al. (39) describe a lifecycle for judges of recommendation explanations, using human-labelled benchmarks, rubric refinement and continuing alignment checks. The latter is a 2026 preprint reporting a production setting; its findings should not be transferred directly to a small offline fashion study. Together, these studies support treating evaluator calibration as an empirical requirement rather than assuming that assigning different models to extraction and verification establishes accuracy.

## 2.7 Comparative synthesis and research gap

### 2.7.1 Comparison of representative research

Table 2.1 compares the closest strands by the object they explain and the evidence they evaluate. The comparison identifies differences in research questions; it does not rank the studies on a common performance scale.

*Table 2.1. Explanation targets and evaluation boundaries in related work.*

| Study | Explanation or representation | Boundary relevant to this study |
|---|---|---|
| Hou et al. (29) | Personalised visual attribute highlights | Attribute preference differs from sentence-level source support. |
| Lin et al. (30) | Joint outfit matching and comment generation | BLEU and ROUGE assess reference-text similarity. |
| Li et al. (24) | Attribute-level pairing knowledge | Interpretable compatibility differs from auditing free-form explanations. |
| Xian et al.; Zhu et al. (7, 8) | Paths and logic participating in recommendation | Mechanism linkage motivates retaining decision evidence. |
| PEPLER; P5 (31, 32) | Language conditioned on recommendation information | Conditioning requires a separate faithfulness test. |
| Zhai et al. (25) | Controllable outfit generation | The task produces outfits, rather than auditing explanations of locked items. |
| Gao et al.; Rashkin et al. (14, 16) | Citation and source attribution | Source support does not itself establish participation in ranking. |
| Min et al. (17) | Atomic factual support | Claim decomposition requires a domain-specific evidence definition. |
| ARES; RAGAs (35, 36) | Automated RAG assessment | Judge validity depends on calibration and task transfer. |
| Zheng et al.; Kong et al. (37, 39) | Judge bias and operational evaluation | Independent human assessment remains relevant. |

### 2.7.2 Research gap and scope

The reviewed work already connects fashion recommendation to interpretable attributes and generated comments (29, 30, 24). Knowledge-graph and logic-based systems also link recommendation to interpretable reasoning (7, 8). The contribution sought here is therefore a specific combination of provenance and evaluation: retaining the rules that numerically contributed to a hybrid ranking, locking the selected item, and varying whether an explanation generator can see that same record.

This question joins two bodies of evidence. Recommendation research supplies mechanisms that expose paths, rules or attributes. Attribution and citation research supplies methods for assessing whether individual statements are supported by identified sources (14, 16, 17). Combining them makes it possible to ask whether visibility of a retained ranking trace improves measured support, while keeping recommendation identity constant.

Several boundaries follow from the review. The symbolic trace explains only its own contribution to a hybrid score. A positive source-support result does not establish that the rule is valid for every context, and automated judgements require calibration before they can be treated as semantic ground truth (10, 35, 37). User-experience benefits also require their own assessment (27, 26). Chapter 3 uses these boundaries to define a controlled offline study, with recommendation effectiveness, claim support and citation entailment reported separately.

## 2.8 Chapter summary

Fashion recommendation research has used visual attributes, generated comments, knowledge-graph paths and rules to make decisions more interpretable. Attribution research offers methods for checking individual statements against sources. This thesis tests whether showing a generator the rules retained during ranking changes its explanation of a fixed selected item. Chapter 3 defines the comparison and measures ranking effectiveness, source support and citation entailment separately. The experiment does not measure user experience or independently validate its automated judges.

\newpage

# Chapter 3: Methodology
## 3.1 Introduction

This chapter describes the offline experiment used to connect multimodal recommendation to a saved symbolic trace and to assess the explanations generated from it. Data preparation, representations, candidate pools and rules were fixed before the confirmatory run. The recommendation stage then locked an item and its contributing rule trace for each case. Paired explanations of that item were generated with and without access to the trace. Ranking effectiveness, rule participation and explanation support were assessed separately.

The design follows a paired-comparison principle. For each explanation case, common context A contained the request, query-item text and identity, and locked recommended-item text and identity. Exact trace B contained the eligible rules, up to the configured maximum of five, that contributed to the frozen evidence score. The No-RAG generator received A alone. The Rule-RAG generator received A and B, while recommendation identity was held constant. This intervention isolates access to the decision trace at the explanation stage. It does not isolate every possible effect of prompt wording or output length, and it does not turn the No-RAG condition into a grounded explanation when its text happens to agree with B. Accordingly, B agreement in No-RAG is post-hoc alignment, whereas Rule-RAG support is evidence-grounded because B was visible during generation.

The study evaluates an offline system using held-out outfit co-occurrence as the relevance label. Qwen extracts atomic claims and Phi-4 checks their support against the stored evidence packets. The resulting measures are operational definitions for this experiment. Independent annotation would be needed to establish the accuracy of the automated judgements.

## 3.2 Research questions and experimental logic

The methodology addresses four linked research questions. RQ1 asks whether making the exact fashion-rule trace visible during generation improves support by the actual reranking trace and by the final KB packet. RQ2 asks whether the same intervention changes the rate of eligible concrete item-fact claims that are unsupported by a common reference packet. RQ3 asks whether syntactically present Rule-RAG citations are entailed by the cited rules at claim level. RQ4 asks whether the primary support effects remain directionally stable across the three generators and five target categories.

The causal contrast is deliberately narrow. For case \(q\), let \(r_q\) be the recommendation locked in Stage 2, \(A_q\) the common case context, and \(B_q\) the exact retrieved-rule trace. For generator \(g\), the two outputs are

\[
\begin{aligned}
E^{\mathrm{NoRAG}}_{qg} &= G_g(A_q),\\
E^{\mathrm{RuleRAG}}_{qg} &= G_g(A_q,B_q).
\end{aligned}
\tag{3.1}
\]

Both outputs explain the same \(r_q\). The paired elements are the case, locked recommendation, generator, decoding configuration, and common context. The intervention is the availability of \(B_q\): Rule-RAG receives the exact trace and associated grounding instruction, whereas No-RAG does not. Both conditions receive the same 45–75-word instruction. The contrast therefore identifies the effect of trace-grounded prompting, while recognising that the evidence and citation instructions are part of that intervention. Claim outcomes are reported as rates and, where appropriate, per 100 generated words.

Equation (3.1) specifies the generator’s visible information. The recommendation is fixed before either call, and the symbolic trace is recorded during ranking. This ordering permits a paired comparison in which evidence visibility changes while recommendation identity is held constant.

The trace records the rules, similarities, ordering and contributions used by the symbolic evidence component. It covers that component of the hybrid score. The CLIP representation remains latent, so trace support is a narrower target than a complete causal account of the recommendation (10, 11).

## 3.3 Staged research design and freezing policy

Figure 3.1 summarises the pipeline and its evidence boundaries.

![](figures/pipeline.png){width=100%}

*Figure 3.1. Recommendation, locked evidence and paired explanation assessment.*

The final project was implemented in five frozen stages. Stage 1 performed preflight, audited the final 200-rule KB, fixed the dataset/split and validation-only settings, and bound prompts and configurations. Stage 2 executed 1,000 recommendations and 3,000 fresh explanation attempts. Stage 3 extracted atomic claims from accepted explanations. Stage 4 verified claims against the frozen evidence packets and applied the documented deterministic logical-consistency invariant. Stage 5 derived final tables, figures, paired bootstrap inference, release hashes, and quality checks without new model calls.

Freezing served two purposes. First, it prevented test performance from influencing model weights, fusion weights, evidence weights, pool size, rule count, or prompts. Second, it preserved a stable provenance chain. Each major artifact was written once, bound to a SHA-256 digest, and named in a stage manifest. Model identifiers were accompanied by immutable revisions or local model digests. Configuration objects were canonicalised and hashed. Stage 5 derived all final analysis from the saved Stages 1–4 records and made zero new model calls.

The final confirmatory settings were fixed before Stage 2: image/text CLIP fusion was 0.40/0.60; evidence reranking was CLIP/evidence 0.75/0.25; up to five eligible rules contributed to each trace; and the primary candidate pool contained approximately 100 candidates. Generator identities, decoding settings, Rule-RAG prompt form, and claim schemas were frozen before full generation. The verifier-contract correction is separately recorded in final provenance and binds the release to the actual Stage-4 prompt hash.

## 3.4 Data source, unit of analysis, and preprocessing

### 3.4.1 Dataset and fields

The data source was the `Marqo/polyvore` dataset (40) at immutable revision `8c782ee447faf2d2a0402ac883cf07d3b3f43e1c`, configuration `default`, source split `data`, and fingerprint `9c97dc763773e2a2`. Polyvore-derived outfit data are widely used for fashion compatibility research because an outfit supplies a set of items curated to appear together (2, 3, 40). The present study used only the raw item identifier, category, product text, outfit association, and image. Textual explanation evidence was intentionally limited: images entered the recommendation representation but were never captioned, classified, or converted into attributes for A or B.

The pinned source contained 94,096 raw item rows. The validated five-category mapping retained 47,872 eligible items across 19,094 outfits: bags, bottoms, outerwear, shoes, and tops. These prepared counts, rather than intermediate raw-dataset counts, define the frozen split and the confirmatory experiment.

### 3.4.2 Outfit-disjoint splitting

The outfit, not the item row, was the primary split unit. Outfit IDs were ordered by SHA-256 over a fixed seed and assigned to exact quotas of 13,365 development outfits, 2,864 validation outfits, and 2,865 test outfits. This procedure is deterministic and prevents items from the same outfit appearing on opposite sides of the research split. Within the test partition, case selection used a separate seeded SHA-256 order and sampled 200 cases for each broad category, producing 1,000 confirmatory recommendation cases.

Exact duplicate images were audited by hashing image bytes. Eighteen duplicate groups were identified, of which nine crossed the initial research split. Outfits connected by shared exact-image hashes were treated as connected components. Each cross-split component was moved to the split of its lowest seeded-hash anchor; singleton outfits were then moved in a separate deterministic order to restore the original quotas. Twelve outfits changed assignment in total: nine component reassignments and three quota-restoring reassignments. The final split retained its exact quotas and contained no cross-split outfit or exact-image leakage. This is stricter than relying on unique item IDs, because separately identified catalogue rows can still carry identical visual content.

### 3.4.3 Query construction and candidate pools

Each case selected a query item and a target category representing the missing outfit component. All known same-outfit positives in that target category were retained. Negatives were sampled from items of the same target category belonging to other test outfits. The query item was always excluded. Category restriction makes the task a controlled within-category ranking problem: the model chooses *which* pair of shoes or *which* top, rather than receiving credit merely for predicting the requested item type.

Stage 2 used up to 99 same-category negatives together with all known positives for each of the 1,000 confirmatory cases. Pool sizes can exceed 100 when a case has multiple retained positives. The design is therefore sampled controlled-pool ranking rather than full-catalogue retrieval. Absolute ranking values must be interpreted within this fixed test regime; they do not estimate production-scale catalogue retrieval performance.

## 3.5 Representation learning and baseline retrieval

### 3.5.1 Text representation

The text-only baseline used `sentence-transformers/all-MiniLM-L6-v2` at immutable revision `1110a243fdf4706b3f48f1d95db1a4f5529b4d41`. Sentence-BERT-style encoders map sentences into a shared dense space suitable for cosine retrieval (21), while MiniLM distils transformer self-attention into a more compact architecture (22). Product text was encoded into 384-dimensional float32 vectors and L2 normalised. Texts were truncated only according to the pinned encoder limit of 256 tokens. This pathway provided a lightweight semantic baseline distinct from CLIP text encoding.

### 3.5.2 CLIP image and text representation

The multimodal ranker used `openai/clip-vit-base-patch32` at immutable revision `3d74acf9a28c67741b2f4f2ea7635f0aaf6f0268`. CLIP learns aligned visual and language representations from image–text pairs (5). Item images and product text were embedded into 512-dimensional float32 vectors. All vectors were L2 normalised, and Stage-1 preflight confirmed maximum norm errors below \(1.2\times10^{-7}\). Distinct input items also produced non-zero pairwise distances, ruling out degenerate caches.

For a query with normalised image vector \(v_q\) and text vector \(t_q\), the fused query representation was

\[
z_q=\alpha v_q+(1-\alpha)t_q,
\qquad
f_q=\frac{z_q}{\lVert z_q\rVert_2},
\tag{3.2}
\]

The frozen confirmatory system used \(\alpha=0.40\). Candidate \(i\) received CLIP compatibility

\[
s_{\mathrm{CLIP}}(q,i)=f_q^{\top}f_i.
\tag{3.3}
\]

This is cosine similarity because the vectors are normalised. Separate CLIP-image and CLIP-text baselines used their respective query and candidate modalities without fusion. Deterministic item-ID ordering resolved exact score ties.

### 3.5.3 Validation of fusion and computation boundary

The configuration fixed the image/text weights at 0.40/0.60 before the confirmatory run. It also specified a validation grid with image weights from 0 to 1 in steps of 0.20, marked as diagnostic only. That grid did not select the confirmatory operating point. Representations were cached and hash-bound so that ranking calculations could reuse the same encoder outputs.

The experiment records model sizes, quantisation, device configuration, token counts, latency and model digests where available. Kernel-level operation counters were not collected, so no FLOP estimate is reported. Cached representations are reused in ranking and the final analysis makes no model calls.

## 3.6 Curated fashion rule base and exact decision trace

### 3.6.1 Knowledge-base construction

The supplied knowledge base contained 200 source-linked rules, with 40 assigned to each recommended category: bags, bottoms, outerwear, shoes and tops. Each record included a stable identifier, rule text, category, applicability fields and provenance. The rule file was frozen before the confirmatory experiment. Source links document the basis of the rules; they do not establish that every operational applicability field or extension is explicitly stated by the cited source.

Rules express styling relationships rather than verified catalogue facts. Examples include complementarity between apparel types, consistency of formality, seasonal layering, or matching dominant colours. This distinction is essential. A generic instruction to recommend colour-compatible items can support the reason for seeking compatibility, but it cannot prove the actual colour of a particular candidate or that a particular pair definitely matches. The common-reference item-fact analysis therefore uses strict instance-level entailment and does not convert prescriptive advice into product metadata.

### 3.6.2 Rule retrieval and scoring

For each query–candidate pair, the system created a textual representation from the query category and text, user request, candidate category and text, and target category. Rules were filtered before scoring by recommendation category and by explicit applicability gates for query group, required context, query terms, and candidate terms. Semantic similarity between the pair representation and rule text was calculated using normalised `qwen3-embedding:0.6b` vectors (41). The final experiment assigned every retained rule the same weight and no category bonus. Rule \(r\) therefore received

\[
u(q,i,r)=\cos(e_{q,i},e_r).
\tag{3.4}
\]

Here, \(e_{q,i}\) is the candidate representation and \(e_r\) is the rule embedding. Rules were sorted by contribution with stable rule-ID tie-breaking, and up to \(k=5\) eligible rules were retained. Fewer rules were retained when fewer than five passed the applicability gates; empty traces remained explicit zero-evidence cases and were not backfilled with merely similar rules.

For the retained set \(R_k(q,i)\), the candidate evidence score combined its maximum and mean contribution,

\[
s_E(q,i)=0.7\max_{r\in R_k(q,i)}u(q,i,r)
+0.3\frac{1}{\lvert R_k(q,i)\rvert}\sum_{r\in R_k(q,i)}u(q,i,r).
\tag{3.5}
\]

The stored trace included the candidate ID, representation hash, filter counts, retained rule IDs and texts, retrieval ranks, similarities, weights, contributions and final evidence score. These fields allow the symbolic score to be reconstructed before the trace is supplied to the explanation model.

## 3.7 Evidence-aware reranking and recommendation locking

Raw CLIP and evidence scores have different ranges. Within each candidate pool, min–max normalisation converted each to \([0,1]\):

\[
\widetilde{s}(i)=
\begin{cases}
\dfrac{s(i)-\min_j s(j)}{\max_j s(j)-\min_j s(j)}, & \max_j s(j)>\min_j s(j),\\
0, & \max_j s(j)=\min_j s(j).
\end{cases}
\tag{3.6}
\]

If all candidates shared the same score, the deterministic implementation handled the zero range without introducing random noise. The final reranking score was

\[
s_R(q,i)=0.75\,\widetilde{s}_{\mathrm{CLIP}}(q,i)+0.25\,\widetilde{s}_{E}(q,i).
\tag{3.7}
\]

The configuration fixed the CLIP/evidence weights at 0.75/0.25 and the maximum rule count at five. Its validation Pareto analysis was descriptive and did not select these values. Candidate-pool size, rule count, and weights were frozen before testing. The top-ranked reranked item became the locked recommendation. The Stage-2 explanation calls could explain this item but could not replace it. This lock is the methodological bridge between recommendation and explanation experiments: both conditions refer to the same decision, and the trace used for Rule-RAG is the trace stored for that item during reranking.

Evidence participation was assessed through changes in the top item and top-five order, overlap at five and ten, rank displacement, evidence-score gains, rule coverage and rule-use entropy. These diagnostics describe how reranking alters the decision. Relevance metrics separately assess agreement with held-out outfit co-occurrence.

## 3.8 Recommendation evaluation

### 3.8.1 Relevance and metrics

An item was relevant if it belonged to the query outfit and matched the target category. All known positives were retained. For the rank \(r\) of the first relevant item, hit rate at cut-off \(K\) was

\[
\mathrm{HR@}K=\mathrm{I}(r\leq K),
\tag{3.8}
\]

where \(\mathrm{I}\) equals one when its condition is true and zero otherwise. If no relevant item is retrieved, both hit rate and reciprocal rank are zero. Otherwise reciprocal rank is \(1/r\), and MRR averages this value over cases.

The released Stage-5 analysis also reports a discounted first-hit score:

\[
\mathrm{DFH@}K=\frac{\mathrm{I}(r\leq K)}{\log_2(r+1)}.
\tag{3.9}
\]

The frozen files name this quantity `ndcg_at_K`. It equals binary NDCG for a case with one positive, but standard NDCG sums discounted relevance over all retrieved positives and normalises by the ideal ranking (20). Here, 24 of the 1,000 pools contain multiple positives, so the distinction matters. The thesis uses DFH for the released values and preserves them without recomputation. The general ranking utility in the repository implements multi-positive NDCG; the released Stage-5 summary uses the first-hit calculation above. Consequently the reported DFH estimates should not be compared directly with conventional multi-positive NDCG from other studies. Cut-offs one, five and ten are retained, with ten the principal reporting cut-off.

Five frozen confirmatory methods were compared: MiniLM text, CLIP image, CLIP text, fused CLIP, and evidence reranking. Metrics were reported as micro estimates over cases, by target category, and as category macro estimates. The main scientific contrast compared fused CLIP with evidence reranking, because this isolates the addition of the evidence score to the same multimodal base. The frozen run did not add post-confirmatory representation baselines or retune the primary system.

### 3.8.2 Statistical inference

Cases were not treated as fully independent when they shared a query outfit. Recommendation confidence intervals therefore used the query outfit as the bootstrap cluster. For each of 5,000 replicates, complete query-outfit clusters were sampled with replacement, all their cases were retained, and the statistic was recomputed. The 2.5th and 97.5th percentiles formed a 95% interval (42). The released recommendation table reports percentile intervals for each method and metric; it does not report pairwise recommendation p-values or a multiple-comparison test. The test set was not used to choose a weight, prompt, or model.

## 3.9 Explanation-generation experiment

### 3.9.1 Common context A

For every locked case, A contained the complete frozen common information made available to both generators: the user request; query-item ID, category, and product text; and locked recommended-item ID, category, and product text. The displayed prompt used minimal names, while the saved packet retained identity and category provenance. No image caption, visual detector, outside catalogue lookup, brand knowledge, or inferred fashion attribute was added.

### 3.9.2 Exact trace B and conditions

B contained the complete retained trace described in Section 3.6, with between one and five rules for the evidence-eligible explanation cases. It was hidden from No-RAG generation but retained in the frozen record for paired assessment. The No-RAG prompt asked for an explanation of why the locked item suited the request using A and imposed the same 45–75-word contract used by Rule-RAG. The Rule-RAG prompt displayed A and B, included rule IDs and rule text, required at least one exact trace citation, and used the same numerical limits. A/B hashes were stored with every generation record. Thus the word-budget assignment is controlled, although observed word counts and the additional Rule-RAG instructions are not identical.

The No-RAG condition represents an unconstrained post-hoc rationale, not a condition with no information: it can use explicit product text in A. The Rule-RAG condition represents trace-assisted generation. A claim that restates an explicit material term from a product title may therefore be A-supported in either condition. A claim that follows a styling rule may be B-supported. A claim that invents “waterproof”, “premium leather”, or a definite instance-level colour match without such evidence is unsupported by the supplied evidence, but is not automatically factually false.

### 3.9.3 Generators and decoding

Three local, digest-pinned instruction models generated the explanations: Gemma 4 12B (43), Llama 3.1 8B Instruct Q8_0 (44), and Ministral 3 14B Instruct Q4_K_M (45). The generator roster and decoding configuration were frozen before the full run. Each case–generator combination was attempted in both conditions under the same locked recommendation and common context; only the Rule-RAG prompt received the stored trace.

Five hundred locked, evidence-eligible cases were sampled from the final recommendation run, balanced with 100 cases each for bags, bottoms, outerwear, shoes, and tops. Crossing 500 cases, three generators, and two conditions produced 3,000 attempted explanation cells. Every prompt, response, latency, word count, model digest, and content hash was preserved. Outputs were immutable after generation. Stage 2 accepted 2,969 cells; the 31 terminal failures were all Llama Rule-RAG outputs that exceeded the shared 75-word limit after the permitted retries. Final comparisons therefore use generator-specific complete pairs only.

## 3.10 Validation-only configuration freezing

Before the full run, validation-only sensitivity grids examined fusion and evidence-reranking settings. They were used to freeze an image/text mixture of 0.40/0.60, a CLIP/evidence mixture of 0.75/0.25, and a maximum of five retrieved rules per candidate. The grids are reported as validation evidence rather than pooled with the confirmatory results; no final recommendation, explanation, extraction, or verification outcome was selected after observing the test results.

The final Rule-RAG configuration was also frozen before generation. It displayed the complete non-empty retained trace in score order with stable IDs and rule text; it required at least one exact trace citation and imposed the same 45–75-word limits used in No-RAG. Validation work set this contract and the ranking settings, but no pilot outcome is combined with the final estimates. The confirmatory corpus is solely the 3,000 Stage-2 attempted cells and the frozen Stage-3 and Stage-4 assessments derived from accepted outputs.

## 3.11 Atomic-claim extraction and verification

### 3.11.1 Extraction

The complete explanation, rather than a sentence sample, was passed to a frozen Qwen 3.5 9B extractor (46). The extractor enumerated independent atomic fashion or styling propositions, split independently checkable conjunctions, assigned sequential claim IDs, and applied the frozen claim schema. Extraction assessed neither truth nor support. Of 2,969 accepted explanations, 2,965 accepted extractions yielded 17,710 atomic claims; four terminal extraction failures were retained as missing records.

Claim role was assigned deterministically after extraction. `item_type` claims were identity/context claims because they commonly state what item is being recommended. The other schema labels were treated as substantive because even simple categories such as colour and material can carry explanatory content. Records that failed extraction or verification were retained as terminal failures and were not assigned invented claim labels.

### 3.11.2 Multi-source verification

Phi-4 14B (47) verified each extracted claim against complete context A, exact trace B, the record-specific full-KB candidate packet, and observed citations. The final schema preserves four distinct outcomes: `trace_support`, `full_kb_support`, `common_reference_support`, and `citation_entailment`. A `not_supported` value means that the specified evidence packet does not entail the claim under the frozen closed-world protocol; it is not a statement that the claim is false.

Using Phi-4 for verification separates the verifier from the Qwen 3.5 extractor and from the three explanation generators. Stage 4 accepted 2,861 verification records covering 16,804 claims; 104 terminal verification records were retained as missing. A deterministic consistency correction then changed only `full_kb_support` from `not_supported` to `supported` for 163 claims that were trace-supported after confirming that the trace rule occurred in the same record's full-KB packet. This enforces the trace-subset invariant by treating the trace-support verdict as authoritative. It makes no new model call, but it can propagate a mistaken trace-support label into the full-KB outcome.

## 3.12 Study-specific explanation metrics

### 3.12.1 Reranking-trace claim support

Let \(C(E)\) be the verified claims in explanation \(E\). Define \(I_T(c)=1\) when the verifier labels claim \(c\) as trace-supported and zero otherwise. Then

\[
T(E)=\frac{\sum_{c\in C(E)}I_T(c)}{|C(E)|}.
\tag{3.10}
\]

For No-RAG, this measures agreement with a trace hidden during generation. For Rule-RAG, it measures support from the trace supplied in the prompt. The comparison concerns trace-grounded prompting; a positive label alone does not prove the generator’s internal causal dependence on a particular rule.

### 3.12.2 Full-KB and common-reference support

Define \(I_K(c)=1\) when a claim is supported by the record-specific full-KB candidate packet. Full-KB support uses the same verified claim denominator:

\[
F(E)=\frac{\sum_{c\in C(E)}I_K(c)}{|C(E)|}.
\tag{3.11}
\]

This wider source boundary includes rules that did not contribute to the retained trace. The consistency correction described in Section 3.11.2 makes every trace-supported claim full-KB-supported.

For item-fact assessment, the deterministic eligibility gate first excludes subjective styling terms and requires a concrete item or case entity. It then tests whether the content tokens of an explicit predicate, or of the remaining claim, occur in the supplied fact text. Claims failing this literal-coverage test are ineligible. This substantially narrows the measure: a newly invented attribute may be excluded before verification, so UIFR cannot estimate the overall prevalence of unsupported product attributes.

Let \(C_I(E)\) contain the eligible claims and let \(I_U(c)=1\) when common-reference support is `not_supported`. The restricted Unsupported Item-Fact Rate is

\[
U(E)=\frac{\sum_{c\in C_I(E)}I_U(c)}{|C_I(E)|}.
\tag{3.12}
\]

An explanation with no eligible claim has no UIFR estimate. Paired analysis requires eligibility in both conditions. This is a secondary sensitivity measure with a restricted denominator.

### 3.12.3 Trace-supported claim density

For an explanation containing \(W(E)\) words, trace-supported claim density is

\[
D(E)=100\frac{\sum_{c\in C(E)}I_T(c)}{W(E)}.
\tag{3.13}
\]

Density complements the claim proportion by expressing support relative to text length. It does not control all changes in which claims a generator chooses to make.

### 3.12.4 Citation entailment and reporting scope

The final verifier records one citation label per claim: `entails`, `does_not_entail` or `N/A`. The thesis reports these labels descriptively for Rule-RAG, with No-RAG retained as N/A. They are claim-level judgements, rather than a count of independently verified citation–source relations.

The final schema does not retain the complete relation-level information and eligible-claim classification needed to reconstruct citation precision and coverage as defined in the cited-generation literature (14). Those metrics are therefore not estimated. Table 4.3 gives the observable label counts and their denominator. Trace support, full-KB support, restricted item-fact support and citation entailment retain their separate evidence boundaries throughout the analysis.

## 3.13 Final paired inference

For every final explanation outcome, the estimand was the paired Rule-RAG minus No-RAG difference. Analysis first retained complete pairs within each generator: 474 for Gemma, 438 for Llama, and 456 for Ministral. Generator-specific differences were then averaged within a case whenever more than one generator pair was available, yielding 498 paired cases for the primary analysis. This avoids treating unequal marginal condition totals as if they formed paired observations.

For metric \(m\), the case-level contrast was

\[
\widehat{\Delta}_m=
\frac{1}{|Q|}\sum_{q\in Q}
\left(\frac{1}{|G_q|}\sum_{g\in G_q}d_{qg}^{(m)}\right).
\tag{3.14}
\]

Here, \(d_{qg}^{(m)}\) is the generator-specific paired difference and \(G_q\) is the set of complete generator pairs for case \(q\). Percentile 95% confidence intervals were obtained from 5,000 bootstrap resamples of case IDs. Holm correction (48) was applied to the predeclared family of primary support, UIFR, and trace-density contrasts. Citation entailment is summarised descriptively for Rule-RAG because it has no No-RAG counterpart.

## 3.14 Heterogeneity, robustness, and qualitative analysis

Primary trace-support, full-KB-support, and trace-density differences were estimated separately for the three generators and five categories using the same complete-pair rule. These subgroup estimates test directional stability rather than generalisation beyond the evaluated roster. UIFR subgroup analyses are especially cautious because the common-reference item-fact criterion yields a small jointly eligible set.

Missingness was retained as an observable property of the pipeline. The 31 terminal explanation failures were confined to Llama Rule-RAG outputs that exceeded the shared word cap after permitted retries; this produces the smaller Llama complete-pair count and rules out a misleading all-generator balanced-total calculation. Four accepted explanations did not yield accepted claim extraction, and 104 verification records remained terminal. Neither source corpus was silently completed, imputed, or regenerated. Stage 5 reports attempted and accepted denominators alongside the complete-pair analysis, and support rates are calculated only from the verified claims available under the frozen schema. This is conservative: it preserves the distinction between an unobserved assessment and a claim that the verifier labelled not supported.

The bootstrap unit also follows the pairing structure at the case level. A case can contribute up to three generator-specific pairs, so resampling every text independently would understate uncertainty by treating correlated outputs as unrelated observations. Resampling case IDs retains all complete generator pairs for each selected case and repeats the within-case averaging rule. Generator-specific estimates retain their own complete pairs, while category summaries are based on the same frozen case and generator identifiers. This makes the overall and subgroup analyses traceable to one coherent unit of inference, even though the available pair counts differ across generators.

The analysis distinguishes support prevalence from claim opportunity. A shorter text can contain fewer substantive propositions, whereas a longer text can provide more opportunities both for supported relational statements and for unsupported item details. Trace-supported-claim density, expressed per 100 generated words, therefore complements the support-rate outcomes. UIFR does not receive a forced denominator adjustment because its eligibility is defined by the presence of concrete item-fact claims in both conditions; its restricted complete-pair estimate is reported separately rather than extrapolated to explanations that made no eligible assertion. These choices make the final estimands narrower, but also prevent a broad claim of factual reliability from being inferred from a source-specific support result.

Appendix B presents paired examples drawn from the frozen records. It preserves the supplied context, retained rule texts, generated explanations and verifier labels. The examples illustrate the meaning and limitations of the automated labels; their selection does not support a prevalence estimate.

## 3.15 Reproducibility, software, and ethical boundaries

The project received ethics approval from the University of Salford (reference 12425).

The implementation used Python 3.12 on Windows 11. Embedding and LLM stages were configured for CUDA where available. The repository pins dependencies through `uv.lock`, model revisions or immutable local digests, dataset revision, random seeds, and canonical configuration hashes. Major tables, figures, JSONL corpora, and manifests are SHA-256 bound. Ruff linting and the project test suite cover data leakage, deterministic ranking, rule retrieval, prompt separation, schemas, refusal handling, statistics, artifact integrity, and the trace-support-to-full-KB-support invariant. Stage 5 validates principal output hashes and records the release boundary.

The study uses catalogue images and descriptions from a research dataset and makes no inference about protected personal attributes. It is not a safety-critical wardrobe adviser, product-authentication system, or factual catalogue service. Product text may be noisy, and outfit co-occurrence reflects platform curation rather than universal taste. Generated explanations must therefore be read as system outputs about supplied records, not authoritative fashion or product claims.

Automated assessment presents a more important validity limitation. Qwen 3.5 9B extracts claims and Phi-4 14B verifies them; this separates claim construction from entailment but does not establish either model's semantic accuracy. The restricted UIFR definition improves source-boundary transparency but cannot resolve every mixed natural-language claim. No human ratings, independent external annotations, or partial-entailment audit are included. The strongest warranted conclusion is comparative: under this frozen system evaluator, access to the exact retained trace changes measured trace support, full-KB support, trace-supported-claim density, and citation-related provenance. It does not establish human preference, factual correctness in the world, or causal faithfulness to every internal neural computation.

## 3.16 Validity controls and decision rules

Several controls were applied before results were interpreted. Construct validity was protected by refusing to collapse all explanation properties into a single “grounding” score. Trace support addresses agreement with the actual rule trace, full-KB support addresses broader rule grounding, UIFR addresses a narrow class of concrete product assertions, and citation entailment addresses whether an attached rule supports its claim. These measures can move differently. For example, an explanation can accurately paraphrase B while adding an unsupported material claim, or it can use a citation that does not entail the proposition it accompanies. Reporting each rate separately prevents one favourable dimension from concealing another failure.

Internal validity depended on pairing and freezing. The recommendation, A packet, B packet, generator, and case were identical within each No-RAG/Rule-RAG comparison. Outputs were not edited to equalise length, remove refusals, repair citations, or improve examples. Stage-2 generation records were hashed before assessment, and Stage-3 and Stage-4 outputs were preserved before deterministic metric derivation. Model selection and hyperparameter search were confined to development or validation data. These controls do not remove the prompt-and-length difference intrinsic to the intervention, but they prevent test-driven tuning and recommendation changes from contaminating the explanation contrast.

Statistical-conclusion validity was addressed through the appropriate dependence unit. Recommendation cases can share an outfit, so recommendation intervals resample query outfits. Explanation texts from three generators can share a case, so Stage-5 analyses resample case IDs after averaging complete generator-specific pairs within case. Micro and macro estimates answer different questions and are not treated as interchangeable: micro rates weight explanations in proportion to their number of claims, whereas macro rates weight each eligible explanation equally. The UIFR paired result has the additional jointly eligible restriction; it therefore describes texts that actually make concrete item-fact claims on both sides and is not extrapolated to all complete pairs.

External validity is bounded by the sampled catalogue, five broad categories, controlled pools, three local quantised generators, and supplied rule base. The system does not model individual user histories, price, availability, body measurements, culture-specific dress norms, or time-varying trends. Outfit co-occurrence is a useful offline relevance signal but does not prove that every held-out item would be preferred by a new user. The final release does not provide a larger-pool result from which to estimate full-catalogue performance.

Reliability was supported by deterministic execution and independent re-computation from stored artifacts. SHA-256 ordering replaced random iteration in split, case, tie, and example selection. Generation used greedy deterministic settings, while structured assessment calls retained model digests and raw-response hashes. Each derived table can be traced to a manifest listing input and output hashes. Re-running the publication analysis does not invoke a model; it combines immutable records, recomputes rates and cluster resamples, and recreates figures and examples.

Interpretation follows the evidence available to each measure. “Unsupported” means unsupported by the specified source; a factual-falsehood claim requires evidence of contradiction. No-RAG support records agreement with hidden rules, and the restricted UIFR result applies only to jointly eligible outputs. The ranking comparison reports the observed reduction in aggregate relevance measures alongside the increase in evidence alignment.

## 3.17 Chapter summary

The methodology connects recommendation and explanation through a locked decision and an exact symbolic trace. Multimodal CLIP retrieval supplies the base ranking; a filtered, source-grounded fashion rule base contributes an evidence score; fixed settings define the fusion and reranking design; and the confirmatory evaluation quantifies both recommendation effectiveness and ranking change. The explanation experiment holds recommendation identity constant while varying access to B across three generators and five categories. Atomic claims, trace and full-KB support, common-reference UIFR, citation entailment, complete-pair inference, subgroup estimates, and frozen qualitative examples provide complementary views of the output.

Every reported explanation can be traced to its A packet, B trace, generator digest, locked candidate, claim list and verification record. The experiment relies on automated assessment, so Chapter 4 reports quantitative differences as system measurements, without treating the claim labels as independently validated truth.

\newpage

# Chapter 4: Results
## 4.1 Introduction

This chapter reports the frozen final five-stage experiment. Every result is derived from the canonical Stages 1–5 artifacts; no model was called during final analysis. Results follow the pipeline: preflight, recommendation evaluation, explanation generation, extraction and verification, then paired claim-level contrasts. A claim described as unsupported is unsupported by the supplied source under the frozen protocol; it is not thereby false in the world. Citation syntax is also kept separate from citation entailment.

No-RAG and Rule-RAG explain the same locked recommendation for each case and generator. Both receive common context A; Rule-RAG also receives the retained reranking trace B. The comparison measures the effect of making that stored evidence available during generation.

## 4.2 Final preflight and frozen design

Stage 1 passed the final preflight gate. Dataset and split inputs, embeddings, candidate-pool construction, prompts, schemas, and output hashes were frozen before confirmatory work. The final knowledge base contains 200 curated fashion rules, exactly 40 each for bags, bottoms, outerwear, shoes, and tops. The audit confirmed unique identifiers, complete provenance, and no exact or threshold-defined near duplicates.

The frozen operating point used image/text fusion of 0.40/0.60, CLIP/evidence weights of 0.75/0.25 and up to five eligible rules per candidate. Validation grids were diagnostic; the configuration fixed these settings. The complete retained trace saved during reranking was supplied unchanged as Rule-RAG evidence.

## 4.3 Recommendation results

The recommendation evaluation contained 1,000 held-out cases, 200 per category, drawn from 734 underlying query outfits. Confidence intervals use 5,000 percentile bootstrap replicates clustered by query outfit. The task remains controlled same-category candidate-pool ranking, with held-out outfit co-occurrence as an offline relevance proxy.

*Table 4.1. Micro-averaged recommendation effectiveness on 1,000 frozen test cases. Values are shown as percentages; Appendix A provides the released estimates and confidence intervals. DFH is the discounted first-hit measure defined in Section 3.8.1; the frozen files label it NDCG.*

| Method | HR@1 | HR@5 | HR@10 | DFH@5 | DFH@10 | MRR |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| MiniLM text | 4.8% | 12.0% | 17.7% | 8.4% | 10.3% | 10.2% |
| CLIP image | 3.2% | 12.6% | 22.0% | 7.9% | 10.9% | 10.0% |
| CLIP text | 3.5% | 13.8% | 21.2% | 8.6% | 11.0% | 10.1% |
| Fused CLIP | 4.5% | 14.3% | 23.1% | 9.4% | 12.2% | 11.4% |
| Evidence rerank | 3.8% | 13.2% | 22.5% | 8.5% | 11.4% | 10.6% |


Fused CLIP had the highest HR@5, HR@10, DFH and MRR; MiniLM had the highest HR@1. Evidence reranking retained 97.4% of fused CLIP's HR@10: the change from 23.1% to 22.5% was a 0.6-percentage-point reduction. HR@5 declined by 1.1 points, from 14.3% to 13.2%; all reported aggregate relevance measures were lower after reranking. The symbolic score changed the top-ranked recommendation in 26.5% of cases. Mean top-five overlap was 3.859, mean top-one evidence-score gain was 0.1473, and mean pre-to-post rank shift was 0.566. One hundred and forty-eight of the 200 rules occurred in at least one locked trace. The retained traces therefore document an active contribution to selection, with the full ranking trade-off quantified in Table 4.1.

## 4.4 Explanation completion and pairing

Five hundred evidence-eligible locked recommendations, balanced at 100 cases per category, formed the explanation study. Gemma 4 12B, Llama 3.1 8B Instruct, and Ministral 3 14B Instruct generated both conditions, giving 3,000 attempted cells. Stage 2 accepted 2,969 explanations. The 31 terminal failures were all Llama Rule-RAG responses exceeding the shared 75-word limit after permitted retries; none was replaced or silently repaired.

Final inference therefore uses generator-specific complete pairs: Gemma 474, Llama 438, and Ministral 456. For the overall estimate, generator-level within-case differences are averaged before resampling, leaving 498 underlying cases with at least one complete generator pair. This prevents multiple generator outputs for a case being treated as independent observations and avoids raw unequal condition totals.

## 4.5 Extraction and verification completion

Qwen 3.5 9B extracted atomic claims from the 2,969 accepted explanations. Stage 3 accepted 2,965 extraction records containing 17,710 claims; four terminal extraction failures were retained. Phi-4 14B then verified claims against A, the exact trace, the full-KB candidate packet, and observed citations. Stage 4 accepted 2,861 verification records covering 16,804 claims. The 104 terminal verification failures remain in the canonical missingness record.

The verifier preserves separate fields for `trace_support`, `full_kb_support`, `common_reference_support`, and `citation_entailment`. Of the verified claims, 2,058 were trace-supported and 2,095 were supported by the full KB packet. Common-reference support was 961 supported, 13 not supported, and 15,830 not applicable. Citation entailment was 1,820 entails, 5,502 does not entail, and 9,482 not applicable.

A deterministic correction addressed 163 logically impossible labels where trace support was supported but full-KB support was not supported. For every affected claim, the trace rule was confirmed to occur in its full-KB packet. Only the full-KB label was changed to supported; no model was rerun and no other field was altered. This correction assumes that the trace-support label is correct. The final invariant is explicit: trace support implies full-KB support.

## 4.6 Paired explanation results

Primary contrasts use 5,000 paired percentile bootstrap replicates clustered by underlying case (42), with Holm adjustment across four prespecified overall metrics (48). Table 4.2 presents Rule-RAG minus No-RAG. Positive values favour Rule-RAG except for UIFR, where lower is preferable.

For metric \(m\), the reported effect is the average within-case difference after first averaging the available generator-specific complete-pair differences:

\[
\widehat{\Delta}_m=
\frac{1}{|Q|}\sum_{q\in Q}
\left(\frac{1}{|G_q|}\sum_{g\in G_q}
\bigl[m(E^{\mathrm{RuleRAG}}_{qg})-m(E^{\mathrm{NoRAG}}_{qg})\bigr]\right).
\tag{4.1}
\]

Here, \(Q\) is the set of underlying cases with at least one complete pair and \(G_q\) is the available generator set for case \(q\). The expression clarifies why three generator outputs for one case are not treated as three independent cases.

*Table 4.2. Overall paired explanation contrasts (Rule-RAG minus No-RAG). Rate differences are percentage points; density remains in claims per 100 words.*

| Metric | Paired cases | Difference | 95% CI | Adjusted p |
| --- | ---: | ---: | ---: | ---: |
| Reranking-trace claim support rate | 498 | +21.02 pp | +19.72 to +22.37 pp | 0.0016 |
| Full-KB claim support rate | 498 | +21.40 pp | +20.11 to +22.71 pp | 0.0016 |
| Unsupported Item-Fact Rate | 53 | +0.63 pp | −5.03 to +5.66 pp | 0.9042 |
| Trace-supported claims per 100 words | 498 | +1.60 | +1.48 to +1.72 | 0.0016 |


Rule-RAG substantially increased claims supported by both the exact trace and the wider final KB packet. The increase of 1.60 trace-supported claims per 100 words shows that the advantage remains when support is expressed relative to output length. This normalisation does not isolate all behavioural effects of the prompt. For No-RAG, agreement with hidden B is post-hoc alignment; for Rule-RAG, support is evidence-grounded because B was available in the prompt.

Figure 4.1 visualises the four contrasts on their correct units, separating rate differences from claim density.

![](../artifacts/figures/final_explanation_paired_contrasts_corrected.png){width=95%}

*Figure 4.1. Paired explanation contrasts with 95% case-clustered bootstrap intervals.*

UIFR is inconclusive. It applies only when both paired explanations contain the relevant common-reference item-fact claim type, leaving 53 pairs. The interval includes both small benefit and small harm, so it cannot justify a corpus-wide claim that Rule-RAG reduces item-fact overreach.

## 4.7 Robustness, citations, and research questions

The primary support effects were positive for every generator. Trace-support differences were +25.09 percentage points for Gemma, +26.74 for Llama, and +11.35 for Ministral; full-KB differences were +25.22, +27.26, and +11.77 points. All corresponding confidence intervals excluded zero. All five categories also showed positive trace and full-KB support differences, with intervals excluding zero. This establishes directional robustness within the tested roster and categories, not universal generalisation.

Citation markers improve inspectability but are not treated as support. A claim can carry a malformed, irrelevant, or non-entailing rule identifier. The verified citation-entailment field is therefore essential: the experiment demonstrates source provenance and stronger source-grounded claim rates, but not that citation syntax alone validates a claim.

Table 4.3 summarises the citation-entailment labels for the 8,075 verified Rule-RAG claims. Among the 7,322 claims assigned a non-N/A label, 24.86% were labelled `entails`. This is a descriptive claim-label proportion, not relation-level citation precision or coverage. The predominance of `does_not_entail` labels limits any claim of citation reliability.

*Table 4.3. Recorded citation-entailment labels by explanation condition.*

| Label | No-RAG claims | Rule-RAG claims |
|---|---:|---:|
| Entails | 0 | 1,820 |
| Does not entail | 0 | 5,502 |
| N/A | 8,729 | 753 |
| Total | 8,729 | 8,075 |

## 4.8 Missingness and failure accounting

The pipeline retained failure records at every stage. Of 3,000 generation attempts, 2,969 explanations were accepted. Of these, 2,965 were successfully extracted and 2,861 completed verification. This yields a final claim-verification coverage of 16,804 claims from 2,861 explanation records. Failures were not converted to zero claims, favourable labels, or synthetic replacements. Such handling would create a false appearance of complete coverage and could bias a comparison if a condition were more difficult to parse or verify.

The generation failures were not balanced: all 31 occurred in Llama Rule-RAG. These failures indicate difficulty satisfying the output contract; their semantic quality was not assessed. Still, it matters because a complete-pair estimate describes retained paired outputs, not the behaviour of cells that failed the output contract. The generator-specific pairing policy addresses the immediate statistical issue: it prevents a Rule-RAG total of 469 being compared with a No-RAG total of 500 as if the observations were paired. It does not turn missing outputs into evidence of success.

Verification failure was smaller but present in both conditions. Gemma had 22 No-RAG and three Rule-RAG terminal verification failures; Llama had 18 and 16; Ministral had 22 and 23. These counts show why missingness must be reported by generator and condition rather than as one aggregate percentage. The final results should be interpreted with the generator-by-condition denominator table in Appendix A, particularly for secondary outcomes whose eligibility is already restricted.

## 4.9 Statistical checks

The overall explanation analysis uses the underlying case as the resampling unit because outputs from different generators share the same locked recommendation and evidence. The analysis first computes each available generator-specific paired difference, then averages available generator effects within case, and finally bootstraps cases. This procedure respects both repeated measurement and unequal complete-pair availability. It is more conservative than treating the 1,368 complete case–generator pairs as independent rows.

The confidence intervals use 5,000 paired bootstrap replicates. Holm correction is applied across the four overall explanation outcomes. For the three positive support outcomes, the two-sided bootstrap p-value reaches the procedure’s minimum of 0.0004 before adjustment and 0.0016 afterwards. These values describe resampling uncertainty conditional on the observed cases and automated labels; they exclude uncertainty about the verifier’s semantic accuracy.

The UIFR result illustrates why effect size, eligibility, and precision must be read together. Its point estimate is close to zero and its interval is much wider than those of the primary support metrics. The limiting factor is not merely a lack of arithmetic power; it is that a common-reference item-fact outcome is substantively defined only for a small subset of paired explanations. Reporting it as a null result with its denominator is more informative than either omitting it or extrapolating it to every output.

## 4.10 Reproducibility and audit trail

The final analysis is reproducible from frozen records rather than from regenerated language. Stage manifests bind the input and output hashes for each stage, including the final recommendation, explanation, extraction, verification, and analysis tables. The release record identifies the final verification SHA-256 as `0f554e58be51c0529c59814f3c5de379ec66c02afbb8fa2c5e48249a32ae9b3e`. The final implementation also passed `ruff check .` and 54 automated tests. These checks do not validate the substantive fashion rules or the models' semantic judgements, but they make record substitution, schema drift, and broken joins detectable.

The joins between stages were exact. Three thousand explanation records were attempted; 2,969 accepted Stage-2 outputs entered extraction; 2,965 accepted Stage-3 records entered verification; and 2,861 accepted Stage-4 records provided canonical claim labels. Claim identifiers were preserved from extraction into verification. The final analysis reads the Stage-4 schema directly, including trace support, full-KB support, common-reference support, and citation entailment. The release manifest identifies the exact files used for these joins.

The Stage-1 manifest retains its original prompt-configuration hash and records an amendment for the final Stage-4 verifier contract. The release is bound to the actual final prompt and configuration hashes. The amendment and deterministic consistency correction are documented separately from generation; no explanation, extraction or verification call was repeated as part of the Stage-5 analysis.

## 4.11 Chapter summary

Fused CLIP ranked best overall. Evidence reranking scored lower on every aggregate metric, changed the top item in 26.5% of cases, and stored a rule trace.

Trace access improved source support and supported-claim density. Item-fact support was inconclusive, and most applicable citation labels indicated no entailment. Chapter 5 examines these results and evaluator limitations.

\newpage

# Chapter 5: Discussion and Conclusion
## 5.1 Introduction

This chapter interprets the findings in relation to the research problem and literature reviewed in Chapter 2. The study began from a practical tension. Multimodal fashion recommenders can rank visually and semantically compatible products, while language models can explain almost any selected item fluently. Neither capability ensures that the explanation describes the evidence that actually influenced the recommendation. The implemented system addresses this gap by storing the source-grounded fashion-rule component of the reranking decision and exposing that same trace to an explanation generator.

The evaluation covered 1,000 ranking cases and 500 explanation cases across three generators. Of 3,000 planned generation cells, 2,969 were accepted; the assessment pipeline extracted 17,710 claims and verified 16,804. Supplying the retained trace increased trace support by 21.02 percentage points and full-KB support by 21.40 points. The architecture connects a numerical recommendation decision to evidence that can be inspected in its explanation, while the paired design measures the benefit of exposing that evidence for a fixed recommendation. This chapter discusses these contributions and consolidates their methodological limits in Section 5.8.

## 5.2 Interpretation of recommendation findings

### 5.2.1 Value of multimodal fusion

Fused CLIP achieved the highest top-five and top-ten hit rates among the tested methods (Table 4.1), although MiniLM had the highest HR@1. Combining image and text representations was therefore useful within this candidate protocol. The result is consistent with the modalities supplying complementary catalogue information, but the experiment does not identify which visual or textual features caused an individual ranking change.

The result aligns with multimodal fashion research in which learned visual representations improve style compatibility and category-aware outfit modelling (1, 2, 5). The controlled held-out task provides a common basis for comparing the fixed representations and the contribution of evidence reranking.

FashionCLIP and Text2Outfit illustrate how domain adaptation and task-specific generation extend beyond a frozen general-purpose encoder (23, 25). They provide context for extending the representation. The present experiment isolates the addition of an explicit rule score to the same multimodal ranking and evaluates language against its retained trace.

### 5.2.2 Accuracy and evidence alignment are different objectives

Evidence reranking retained 97.4% of fused CLIP's HR@10: the hit rate changed from 23.1% to 22.5%, an absolute reduction of 0.6 percentage points. HR@5 changed from 14.3% to 13.2%, and the released DFH@10 from 12.23% to 11.45%. All reported aggregate ranking metrics were lower at the tested 0.75/0.25 operating point. These figures quantify the relevance outcome alongside the addition of an inspectable symbolic contribution.

The reranker changed the top item in 26.5% of cases and increased the selected item's evidence score by 0.1473 on average. The rules therefore participated in selection, and the saved contributions identify how they entered the ranking objective. This is the architectural basis for carrying decision evidence into explanation generation.

Ranking and explanation were evaluated through separate comparisons. The ranking study compared fused CLIP with evidence reranking; the explanation study held the recommendation fixed and varied trace access and grounding instructions. Together they measure ranking behaviour and explanation support, but they do not estimate a causal price of faithfulness. Section 5.8 discusses the relevance proxy and rule coverage that constrain this interpretation.

## 5.3 Interpretation of explanation faithfulness

### 5.3.1 From plausible rationale to trace-linked account

The primary outcome measures support by the retained rule trace. Rule-RAG improved this rate by 21.02 percentage points, with a 95% interval of 19.72 to 22.37 points (Table 4.2). Full-KB support improved by 21.40 percentage points. The similar gains suggest that the measured benefit was concentrated in evidence already available in the trace.

Agreement between No-RAG claims and the hidden trace can arise from a generator's prior knowledge. Rule-RAG receives the retained trace directly, and the paired contrast measures the effect of that access together with its grounding instructions. This design tests source support for the same recommendation in both conditions. The distinction between measured source support and internal causal faithfulness follows evaluation concerns in prior work (10, 33).

The positive support direction held across the tested generators and categories. Effect magnitudes differed, with Ministral showing a smaller trace-support change than Gemma or Llama. This suggests that the response to evidence depends on the generator, even when the recommendation and prompt contract are held fixed.

### 5.3.2 Unsupported item-specific assertions

The final UIFR outcome addresses a different failure: concrete item facts unsupported by the common reference packet. Its estimate was +0.63 percentage points for Rule-RAG minus No-RAG, with a 95% interval from −5.03 to +5.66 and Holm-adjusted \(p=0.9042\). Only 53 complete pairs were eligible. The result is therefore inconclusive, not evidence that Rule-RAG either reduces or increases unsupported item facts.

Appendix B shows paired outputs together with their supplied evidence and automated labels. These records illustrate how a model can paraphrase a rule, attach a citation and still receive a negative entailment judgement. They also show why a reviewer needs the original text and evidence to assess whether the verifier’s decision is reasonable.

### 5.3.3 Citation entailment

The recorded Rule-RAG claims received 1,820 `entails`, 5,502 `does_not_entail` and 753 `N/A` labels (Table 4.3). Thus, displaying rule identifiers did not ensure positive entailment judgements under the frozen verifier. The result is consistent with the need to evaluate citation quality separately from answer fluency and overall correctness (14, 15).

The architecture makes cited rules inspectable and permits citation use to be assessed separately from overall source support. The counts are claim-level labels; the reporting limits for relation-level citation precision and coverage are set out in Section 5.8.

## 5.4 Relationship between grounding and user-facing quality

The source-support gains give a concrete basis for evaluating evidence-grounded explanations. Trace support links language to evidence used in the symbolic reranker; full-KB support assesses agreement with the broader available packet; and supported-claim density measures how much supported content appears within a given amount of text. Their agreement strengthens the finding that Rule-RAG improves measured grounding under the shared prompt contract.

User-facing quality is a separate evaluation objective. The user-experience and explanation-goal frameworks reviewed in Chapter 2 provide criteria for assessing clarity, usefulness and persuasion (27, 26). Prior work also distinguishes the user experience of an explanation from its faithfulness to the decision process (27, 34, 26). The present framework preserves the measures needed to examine those relationships: a future user study can compare preferences with source support and citation entailment, while retaining the original explanation and evidence for review.

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

The first priority is independent assessment of the source-support judgements. AIS and FActScore provide relevant principles for source attribution and atomic annotation (16, 17), while ARES illustrates the role of human-labelled data in automated estimation (35). The recent judge-lifecycle study motivates checking evaluator alignment as models and catalogues change (39). These procedures would allow sampling uncertainty and evaluator error to be considered separately.

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

\newpage

# References

(1) McAuley, J. et al. (2015) ‘Image-based recommendations on styles and substitutes’, *Proceedings of SIGIR 2015*, pp. 43–52. https://doi.org/10.1145/2766462.2767755.

(2) Han, X. et al. (2017) ‘Learning fashion compatibility with bidirectional LSTMs’, *Proceedings of the 25th ACM International Conference on Multimedia*, pp. 1078–1086. https://doi.org/10.1145/3123266.3123394.

(3) Vasileva, M.I. et al. (2018) ‘Learning type-aware embeddings for fashion compatibility’, *Computer Vision – ECCV 2018*, LNCS 11220, pp. 405–421. https://doi.org/10.1007/978-3-030-01270-0_24.

(4) Cucurull, G. et al. (2019) ‘Context-aware visual compatibility prediction’, *Proceedings of CVPR 2019*, pp. 12617–12626. https://openaccess.thecvf.com/content_CVPR_2019/html/Cucurull_Context-Aware_Visual_Compatibility_Prediction_CVPR_2019_paper.html.

(5) Radford, A. et al. (2021) ‘Learning transferable visual models from natural language supervision’, *Proceedings of ICML 2021*, 139, pp. 8748–8763. https://proceedings.mlr.press/v139/radford21a.html.

(6) Zhang, Y. and Chen, X. (2020) ‘Explainable recommendation: A survey and new perspectives’, *Foundations and Trends in Information Retrieval*, 14(1), pp. 1–101. https://doi.org/10.1561/1500000066.

(7) Xian, Y. et al. (2019) ‘Reinforcement knowledge graph reasoning for explainable recommendation’, *Proceedings of SIGIR 2019*, pp. 285–294. https://doi.org/10.1145/3331184.3331203.

(8) Zhu, Y. et al. (2021) ‘Faithfully explainable recommendation via neural logic reasoning’, *Proceedings of NAACL 2021*, pp. 3083–3090. https://doi.org/10.18653/v1/2021.naacl-main.245.

(9) Ji, Z. et al. (2023) ‘Survey of hallucination in natural language generation’, *ACM Computing Surveys*, 55(12), Article 248. https://doi.org/10.1145/3571730.

(10) Jacovi, A. and Goldberg, Y. (2020) ‘Towards faithfully interpretable NLP systems: How should we define and evaluate faithfulness?’, *Proceedings of ACL 2020*, pp. 4198–4205. https://doi.org/10.18653/v1/2020.acl-main.386.

(11) Wiegreffe, S. and Pinter, Y. (2019) ‘Attention is not not explanation’, *Proceedings of EMNLP-IJCNLP 2019*, pp. 11–20. https://doi.org/10.18653/v1/D19-1002.

(12) Lyu, Q. et al. (2024) ‘Towards faithful model explanation in NLP: A survey’, *Computational Linguistics*, 50(2), pp. 657–723. https://doi.org/10.1162/coli_a_00511.

(13) Lewis, P. et al. (2020) ‘Retrieval-augmented generation for knowledge-intensive NLP tasks’, *Advances in Neural Information Processing Systems*, 33, pp. 9459–9474. https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html.

(14) Gao, T. et al. (2023) ‘Enabling large language models to generate text with citations’, *Proceedings of EMNLP 2023*, pp. 6465–6488. https://doi.org/10.18653/v1/2023.emnlp-main.398.

(15) Zhang, W. et al. (2024) ‘Towards fine-grained citation evaluation in generated text: A comparative analysis of faithfulness metrics’, *Proceedings of INLG 2024*, pp. 427–439. https://doi.org/10.18653/v1/2024.inlg-main.35.

(16) Rashkin, H. et al. (2023) ‘Measuring Attribution in Natural Language Generation Models’, *Computational Linguistics*, 49(4), pp. 777–840. https://aclanthology.org/2023.cl-4.2/.

(17) Min, S. et al. (2023) ‘FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation’, *Proceedings of EMNLP 2023*, pp. 12076–12100. https://doi.org/10.18653/v1/2023.emnlp-main.741.

(18) Tan, R. et al. (2019) ‘Learning similarity conditions without explicit supervision’, *Proceedings of ICCV 2019*, pp. 10373–10382. https://doi.org/10.1109/ICCV.2019.01047.

(19) Kang, W.-C. et al. (2019) ‘Complete the look: Scene-based complementary product recommendation’, *Proceedings of CVPR 2019*, pp. 10532–10541. https://openaccess.thecvf.com/content_CVPR_2019/html/Kang_Complete_the_Look_Scene-Based_Complementary_Product_Recommendation_CVPR_2019_paper.html.

(20) Järvelin, K. and Kekäläinen, J. (2002) ‘Cumulated gain-based evaluation of IR techniques’, *ACM Transactions on Information Systems*, 20(4), pp. 422–446. https://doi.org/10.1145/582415.582418.

(21) Reimers, N. and Gurevych, I. (2019) ‘Sentence-BERT: Sentence embeddings using Siamese BERT-networks’, *Proceedings of EMNLP-IJCNLP 2019*, pp. 3982–3992. https://doi.org/10.18653/v1/D19-1410.

(22) Wang, W. et al. (2020) ‘MiniLM: Deep self-attention distillation for task-agnostic compression of pre-trained transformers’, *Advances in Neural Information Processing Systems*, 33, pp. 5776–5788. https://proceedings.neurips.cc/paper/2020/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html.

(23) Chia, P.J. et al. (2022) ‘Contrastive language and vision learning of general fashion concepts’, *Scientific Reports*, 12, Article 18958. https://doi.org/10.1038/s41598-022-23052-9.

(24) Li, Y. et al. (2024) ‘Explainable fashion compatibility prediction: An attribute-augmented neural framework’, *Electronic Commerce Research and Applications*, 68, Article 101451. https://doi.org/10.1016/j.elerap.2024.101451.

(25) Zhai, Y. et al. (2025) ‘Text2Outfit: Controllable Outfit Generation with Multimodal Language Models’, *Proceedings of ICCV 2025*, pp. 16165–16174. https://doi.org/10.1109/ICCV51701.2025.01500.

(26) Tintarev, N. and Masthoff, J. (2007) ‘A Survey of Explanations in Recommender Systems’, *IEEE 23rd International Conference on Data Engineering Workshop*, pp. 801–810. https://doi.org/10.1109/ICDEW.2007.4401070.

(27) Knijnenburg, B.P. et al. (2012) ‘Explaining the user experience of recommender systems’, *User Modeling and User-Adapted Interaction*, 22(4–5), pp. 441–504. https://doi.org/10.1007/s11257-011-9118-4.

(28) Jain, S. and Wallace, B.C. (2019) ‘Attention is not Explanation’, *Proceedings of NAACL 2019*, pp. 3543–3556. https://doi.org/10.18653/v1/N19-1357.

(29) Hou, M. et al. (2019) ‘Explainable Fashion Recommendation: A Semantic Attribute Region Guided Approach’, *Proceedings of IJCAI 2019*, pp. 4681–4688. https://doi.org/10.24963/ijcai.2019/650.

(30) Lin, Y. et al. (2020) ‘Explainable Outfit Recommendation with Joint Outfit Matching and Comment Generation’, *IEEE Transactions on Knowledge and Data Engineering*, 32(8), pp. 1502–1516. https://doi.org/10.1109/TKDE.2019.2906190.

(31) Li, L. et al. (2023) ‘Personalized Prompt Learning for Explainable Recommendation’, *ACM Transactions on Information Systems*, 41(4), Article 103. https://doi.org/10.1145/3580488.

(32) Geng, S. et al. (2022) ‘Recommendation as Language Processing (RLP): A Unified Pretrain, Personalized Prompt & Predict Paradigm (P5)’, *Proceedings of RecSys 2022*, pp. 299–315. https://doi.org/10.1145/3523227.3546767.

(33) Turpin, M. et al. (2023) ‘Language Models Don’t Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting’, *Advances in Neural Information Processing Systems*, 36. https://proceedings.neurips.cc/paper_files/paper/2023/hash/ed3fea9033a80fea1376299fa7863f4a-Abstract-Conference.html.

(34) Doshi-Velez, F. and Kim, B. (2017) ‘Towards a rigorous science of interpretable machine learning’, arXiv:1702.08608. https://arxiv.org/abs/1702.08608.

(35) Saad-Falcon, J. et al. (2024) ‘ARES: An automated evaluation framework for retrieval-augmented generation systems’, *Proceedings of NAACL 2024*, pp. 338–354. https://doi.org/10.18653/v1/2024.naacl-long.20.

(36) Es, S. et al. (2024) ‘RAGAs: Automated Evaluation of Retrieval Augmented Generation’, *Proceedings of EACL 2024: System Demonstrations*, pp. 150–158. https://doi.org/10.18653/v1/2024.eacl-demo.16.

(37) Zheng, L. et al. (2023) ‘Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena’, *Advances in Neural Information Processing Systems*, 36. https://proceedings.neurips.cc/paper_files/paper/2023/hash/91f18a1287b398d378ef22505bf41832-Abstract-Datasets_and_Benchmarks.html.

(38) Jacovi, A. et al. (2025) ‘The FACTS Grounding Leaderboard: Benchmarking LLMs’ Ability to Ground Responses to Long-Form Input’, *arXiv preprint*, arXiv:2501.03200. https://doi.org/10.48550/arXiv.2501.03200.

(39) Kong, E.Y. et al. (2026) ‘The Lifecycle of LLM-as-a-Judge for Large-Scale Recommendation Explanations’, *arXiv preprint*, arXiv:2608.18300v3. https://arxiv.org/abs/2608.18300v3.

(40) Marqo (n.d.) *Polyvore dataset card*. https://huggingface.co/datasets/Marqo/polyvore (Accessed: 12 October 2026).

(41) Qwen (2025) *Qwen3-Embedding-0.6B model card*. https://huggingface.co/Qwen/Qwen3-Embedding-0.6B (Accessed: 12 October 2026).

(42) Efron, B. and Tibshirani, R.J. (1993) *An Introduction to the Bootstrap*. New York: Chapman & Hall. https://doi.org/10.1007/978-1-4899-4541-9.

(43) Google DeepMind (2026) *Gemma 4 12B model card*. https://huggingface.co/google/gemma-4-12B (Accessed: 12 October 2026).

(44) Meta (2024) *Llama 3.1 8B Instruct model card*. https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct (Accessed: 12 October 2026).

(45) Mistral AI (2025) *Ministral 3 14B Instruct 2512 model card*. https://huggingface.co/mistralai/Ministral-3-14B-Instruct-2512 (Accessed: 12 October 2026).

(46) Qwen (2026) *Qwen3.5-9B model card*. https://huggingface.co/Qwen/Qwen3.5-9B (Accessed: 12 October 2026).

(47) Microsoft (2024) *Phi-4 model card*. https://huggingface.co/microsoft/phi-4 (Accessed: 12 October 2026).

(48) Holm, S. (1979) ‘A simple sequentially rejective multiple test procedure’, *Scandinavian Journal of Statistics*, 6(2), pp. 65–70. https://www.jstor.org/stable/4615733.

\newpage

# Appendix A: Supplementary quantitative results

## A.1 Pipeline denominators

Table A.1 counts accepted records, with 500 generation attempts for each generator–condition cell. Extraction starts from accepted generation, and verification starts from accepted extraction. A complete support pair requires accepted verification in both conditions.

*Table A.1. Accepted records by generator, condition and pipeline stage.*

| Generator / condition | Generated | Extracted | Verified |
|---|---:|---:|---:|
| Gemma / No-RAG | 500 | 499 | 477 |
| Gemma / Rule-RAG | 500 | 500 | 497 |
| Llama / No-RAG | 500 | 500 | 482 |
| Llama / Rule-RAG | 469 | 469 | 453 |
| Ministral / No-RAG | 500 | 497 | 475 |
| Ministral / Rule-RAG | 500 | 500 | 477 |


*Table A.2. Complete generator pairs for support and restricted UIFR.*

| Generator | Support pairs | UIFR pairs |
|---|---:|---:|
| Gemma | 474 | 11 |
| Llama | 438 | 21 |
| Ministral | 456 | 28 |

Across generators, the corresponding counts of underlying cases are 498 and 53. These are case counts after within-case averaging, not the sum of generator pairs.

## A.2 Recommendation estimates and intervals

The following tables reproduce the micro estimates and percentile 95% intervals in `recommendation_metrics_with_ci.csv`. Values are percentages, shown to three decimal places. Intervals use 5,000 resamples of the 734 query outfits. DFH denotes the released first-hit discount; its source columns are named `ndcg_at_5` and `ndcg_at_10`. Section 3.8.1 explains the distinction from multi-positive NDCG.

*Table A.3. MiniLM text: recommendation estimates and 95% intervals (%).*

| Metric | Estimate | 95% CI |
|---|---:|---:|
| HR@1 | 4.800 | 3.371 to 6.349 |
| HR@5 | 12.000 | 9.788 to 14.199 |
| HR@10 | 17.700 | 15.104 to 20.300 |
| DFH@5 | 8.427 | 6.782 to 10.198 |
| DFH@10 | 10.258 | 8.517 to 12.042 |
| MRR | 10.159 | 8.661 to 11.788 |

*Table A.4. CLIP image: recommendation estimates and 95% intervals (%).*

| Metric | Estimate | 95% CI |
|---|---:|---:|
| HR@1 | 3.200 | 2.119 to 4.390 |
| HR@5 | 12.600 | 10.558 to 14.724 |
| HR@10 | 22.000 | 19.422 to 24.554 |
| DFH@5 | 7.852 | 6.504 to 9.290 |
| DFH@10 | 10.898 | 9.391 to 12.449 |
| MRR | 9.960 | 8.757 to 11.167 |

*Table A.5. CLIP text: recommendation estimates and 95% intervals (%).*

| Metric | Estimate | 95% CI |
|---|---:|---:|
| HR@1 | 3.500 | 2.323 to 4.786 |
| HR@5 | 13.800 | 11.475 to 16.142 |
| HR@10 | 21.200 | 18.408 to 24.000 |
| DFH@5 | 8.634 | 7.080 to 10.315 |
| DFH@10 | 10.954 | 9.318 to 12.710 |
| MRR | 10.087 | 8.691 to 11.602 |

*Table A.6. Fused CLIP: recommendation estimates and 95% intervals (%).*

| Metric | Estimate | 95% CI |
|---|---:|---:|
| HR@1 | 4.500 | 3.147 to 5.918 |
| HR@5 | 14.300 | 12.004 to 16.785 |
| HR@10 | 23.100 | 20.393 to 25.949 |
| DFH@5 | 9.429 | 7.681 to 11.225 |
| DFH@10 | 12.234 | 10.471 to 14.035 |
| MRR | 11.443 | 9.963 to 12.960 |

*Table A.7. Evidence rerank: recommendation estimates and 95% intervals (%).*

| Metric | Estimate | 95% CI |
|---|---:|---:|
| HR@1 | 3.800 | 2.610 to 5.111 |
| HR@5 | 13.200 | 11.045 to 15.501 |
| HR@10 | 22.500 | 19.802 to 25.198 |
| DFH@5 | 8.471 | 6.878 to 10.107 |
| DFH@10 | 11.445 | 9.850 to 13.159 |
| MRR | 10.556 | 9.184 to 11.947 |


\newpage


# Appendix B: Paired examples and automated judgements

These examples reproduce generated text and recorded labels without correction. They are illustrations, not human-validated judgements or a representative estimate of error frequency. To avoid choosing only favourable outputs, selection takes the lowest case ID with a complete Gemma pair and a single retained rule in each of two categories, tops and bags. Claim IDs are local to each explanation. The full release preserves the remaining generators and cases.

## B.1 Tops example

Case `case-026665827bfaaf65`; generator Gemma 4 12B; locked item `216633121_1`.

Request: Recommend a top that works with this outfit.

Query item: Knee Length Skirts | givenchy skirt green leopard-print stretch-jersey

Recommended item: Tops | victoria beckham denim printed cropped top

Retained rule `K004` (contribution 0.535167):

> With a skirt, let the skirt's shape and texture determine the top. A simple tee, tank, or fine knit relaxes a satin, pleated, embellished, or leather skirt; a crisp shirt or blouse makes a denim or simple skirt more polished; and a cropped or tucked top helps when a midi or maxi skirt has a fuller shape. Keeping one half of the outfit visually quieter makes the silhouette and texture feel deliberate rather than busy.

### B.1.1 No-RAG

> The structured texture of the denim cropped top provides a sophisticated contrast to the fluid, stretch-jersey fabric of the leopard-print skirt. By choosing a cropped silhouette, you define your waistline and balance the bold pattern of the bottom piece. The denim material grounds the exotic print, creating a balanced look that feels both modern and effortlessly chic for a polished daytime ensemble.

Recorded claim judgements follow. T = trace support; K = full-KB support; I = common-reference support; C = citation entailment.

**C1.** The denim cropped top has a structured texture.

T: not_supported; K: not_supported; I: N/A; C: N/A.

**C2.** The skirt is made of fluid, stretch-jersey fabric.

T: not_supported; K: not_supported; I: N/A; C: N/A.

**C3.** The skirt has a leopard-print pattern.

T: not_supported; K: not_supported; I: N/A; C: N/A.

**C4.** The top has a cropped silhouette.

T: not_supported; K: not_supported; I: N/A; C: N/A.

**C5.** The denim material grounds the exotic print of the skirt.

T: not_supported; K: not_supported; I: N/A; C: N/A.

### B.1.2 Rule-RAG

> The Victoria Beckham denim printed cropped top is an excellent choice because its cropped silhouette provides a balanced proportion when paired with a midi-length skirt [K004]. Since the skirt features a bold leopard print, the structured nature of the denim top helps keep the overall look intentional. This combination ensures the outfit feels balanced rather than overly busy by grounding the textured print [K004].

Recorded claim judgements follow. T = trace support; K = full-KB support; I = common-reference support; C = citation entailment.

**C1.** The Victoria Beckham denim printed cropped top is an excellent choice.

T: not_supported; K: not_supported; I: N/A; C: does_not_entail.

**C2.** The top has a cropped silhouette.

T: not_supported; K: not_supported; I: N/A; C: does_not_entail.

**C3.** The top is made of denim.

T: not_supported; K: not_supported; I: N/A; C: does_not_entail.

**C4.** The top has a printed pattern.

T: not_supported; K: not_supported; I: N/A; C: does_not_entail.

**C5.** The skirt is midi-length.

T: not_supported; K: not_supported; I: N/A; C: does_not_entail.

**C6.** The skirt features a bold leopard print.

T: not_supported; K: not_supported; I: N/A; C: does_not_entail.

**C7.** The top is structured.

T: not_supported; K: not_supported; I: N/A; C: does_not_entail.

The labels above are outputs of the frozen automated assessment. A supported label should be read against the quoted rule and catalogue context; it does not independently verify the product or establish the correctness of the rule.

## B.2 Bags example

Case `case-04f411a897ac7ef9`; generator Gemma 4 12B; locked item `122542728_4`.

Request: Recommend a bag that completes this outfit.

Query item: Pants | balenciaga balenciaga striped wide-leg trousers

Recommended item: Handbags | striped beach bag

Retained rule `K161` (contribution 0.629479):

> Trousers can support several bag shapes, so let formality and volume decide. Tailored or wool trousers work with structured totes, top-handles, shoulder bags, or slim crossbodies for work; relaxed or cropped pants suit softer shoulder bags and practical crossbodies for weekends. With very wide trousers, a bag with some structure prevents the whole outfit from becoming slouchy, while slim or straight pants can take a softer hobo or tote more easily.

### B.2.1 No-RAG

> A striped beach bag creates a cohesive visual narrative by echoing the linear patterns of your Balenciaga trousers. This repetition of stripes establishes a sophisticated, intentional aesthetic that ties the entire look together. The relaxed silhouette of the bag perfectly complements the volume of the wide-leg cut, ensuring the ensemble feels balanced and stylish while maintaining a cohesive, high-fashion theme throughout the entire outfit.

Recorded claim judgements follow. T = trace support; K = full-KB support; I = common-reference support; C = citation entailment.

**C1.** A striped beach bag creates a cohesive visual narrative by echoing the linear patterns of your Balenciaga trousers.

T: not_supported; K: not_supported; I: N/A; C: N/A.

**C2.** The relaxed silhouette of the bag perfectly complements the volume of the wide-leg cut.

T: not_supported; K: not_supported; I: N/A; C: N/A.

### B.2.2 Rule-RAG

> The striped beach bag is an excellent choice to complement your wide-leg trousers. Because your trousers feature a wide silhouette, selecting a bag with some structure is essential to ensure the overall look remains polished rather than becoming too slouchy [K161]. This specific selection balances the volume of the pants while maintaining a cohesive aesthetic for a more relaxed, stylish ensemble.

Recorded claim judgements follow. T = trace support; K = full-KB support; I = common-reference support; C = citation entailment.

**C1.** The striped beach bag is an excellent choice to complement your wide-leg trousers.

T: not_supported; K: not_supported; I: N/A; C: does_not_entail.

**C2.** Your trousers feature a wide silhouette.

T: not_supported; K: not_supported; I: N/A; C: does_not_entail.

**C3.** Selecting a bag with some structure is essential to ensure the overall look remains polished rather than becoming too slouchy.

T: supported; K: supported; I: N/A; C: entails.

**C4.** This specific selection balances the volume of the pants while maintaining a cohesive aesthetic for a more relaxed, stylish ensemble.

T: not_supported; K: not_supported; I: N/A; C: does_not_entail.

The labels above are outputs of the frozen automated assessment. A supported label should be read against the quoted rule and catalogue context; it does not independently verify the product or establish the correctness of the rule.
