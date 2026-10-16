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
