---
title: "Evidence-Constrained Multimodal Fashion Recommendation with Trace-Grounded Explanations"
author: "Ali Jamali"
date: "November 2026"
subtitle: |
  A thesis submitted in partial fulfilment of the requirements for the degree of Master of Philosophy  
  University of Salford  
  School of Science, Engineering and Environment  
  Student ID: @00818653  
  Supervisors: Dr. Taha Mansouri - Dr. Ali Alameer
geometry: "a4paper,margin=25.4mm"
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

# Declaration

I declare that this thesis is my own work, undertaken during my Master of Philosophy programme at
the University of Salford. I have acknowledged the sources of information, text, data and images
used in the thesis. Any material I have previously submitted or published, and any work carried
out with others, is identified where it appears.

\newpage

# Contents

\newpage

# List of figures

- **Figure 4.1.** Paired explanation contrasts with 95% case-clustered bootstrap intervals.

\newpage

# List of tables

- **Table 2.1.** Representative research strands and the gap addressed by this thesis.
- **Table 4.1.** Micro-averaged recommendation effectiveness on 1,000 frozen test cases.
- **Table 4.2.** Overall paired explanation contrasts (Rule-RAG minus No-RAG).

\newpage
# Abbreviations

| Abbreviation | Meaning |
|---|---|
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
held-out Polyvore outfits. A manually curated, source-grounded knowledge base of 200 fashion rules
supplies a separate evidence score; up to five eligible rules are retained as the symbolic trace
used in reranking. The selected item is then locked, and paired No-RAG and Rule-RAG explanations
differ only in access to that trace and its grounding instructions.

The recommendation experiment contains 1,000 cases across five categories. Fused CLIP was the
strongest tested method overall on the conventional top-five, top-ten, NDCG, and reciprocal-rank
measures. Evidence reranking changed the top-ranked item in 26.5% of cases but did not improve any
reported aggregate recommendation metric relative to fused CLIP. The explanation experiment used
500 evidence-eligible cases and three local generators. Under generator-specific complete pairing
and case-clustered inference, trace access increased reranking-trace claim support by 21.02
percentage points (95% CI 19.72--22.37) and full-KB claim support by 21.40 points (20.11--22.71).
Trace-supported claims per 100 words increased by 1.60 (1.48--1.72). The common-reference
Unsupported Item-Fact Rate was inconclusive because only 53 complete pairs were eligible.

The pipeline preserves the symbolic evidence used in reranking, reuses it during explanation, and
evaluates generated claims against explicit source boundaries. Under the frozen automated
evaluator, trace access improves claim support. The finding is limited by the negative ranking
result, the finite curated knowledge base, and the absence of human explanation assessment.

\newpage
