# Thesis submission audit — 16 October 2026

## Scope and outcome

This audit covers the five editable chapters, front matter, 48 works in the assembled bibliography, appendices, and the regenerated Word and PDF files. The literature review now includes the previously missing work on explainable fashion recommendation, generated recommendation explanations, source attribution, atomic claims and automated judges. The revised documents build successfully.

The thesis is **not yet cleared for submission**. The current Doctoral School production guide is available only on the University Hub and was not supplied for this audit. The University also requires a Turnitin Originality Report and a written originality declaration countersigned by the supervisor. Neither is in this repository. The author must confirm the truth of the ethics approval and prior-publication statements before signing. These are documentary checks, not changes that can be inferred from the thesis text.

## Document and prose checks

- The table of contents follows the title page. The lists of figures and tables, declaration, abbreviations and abstract precede Chapter 1. Chapter order is Introduction, Literature Review, Methodology, Results, then Discussion and Conclusion. References and appendices follow Chapter 5.
- The editable front-matter lists now include both figures and all eleven tables. The generated PDF lists and page numbers were checked visually. Table 2.1, Figure 3.1 and Table 4.2 were inspected at page size and are readable.
- The revised PDF has 78 pages. The DOCX opens normally and Word reports 93 pages; the two renderers paginate differently. The abstract contains 269 words. The build uses Arial 12-point body text, 1.5 line spacing and 30 mm margins. A short orphan page at the end of Chapter 4 was removed before this final build.
- All five chapters received an AI-assisted editorial review. Repetitive openings, inflated summaries, and contrast formulas were revised where they did not carry an essential scientific distinction. Technical contrasts, measurements and caveats were retained. The edit is a prose review, not a detector score or a guarantee about how an AI detector would classify the thesis.
- The consolidated Markdown matches the five chapter sources, front matter and appendices exactly. The build reported 48 consolidated references and no unresolved or conflicting citations.
- The frozen-release audit passed all recorded hashes and deterministic checks, including 1,000 recommendation cases, 3,000 explanation cells and 16,804 verified claims. This validates the release record, not the semantic correctness of automated judgements.

## Source and originality checks

Each of the 48 bibliography entries appears in the thesis body. Twenty-nine DOI entries matched scholarly metadata for title and author. The remaining DOI preprint and the conference pages, other preprints, dataset/model cards and Holm journal record were checked on their original hosting sites. The paper comparisons in Chapter 2 were reviewed against the available abstracts and publisher/proceedings descriptions. No fictitious source or obvious claim-to-source mismatch was found in that review.

One metadata nuance remains: the DOI registry lists a one-page-shifted range for Tan et al. [18], while the publisher's own PDF prints pages 10373–10382. The thesis follows the PDF. Lin et al. [30] appeared online in 2019 and in the cited 2020 journal issue. These are not evidence that either source is invented.

An exact-overlap screen compared all five chapter bodies with 26 available abstracts among the 30 DOI records. It found no matching eight-word sequence. This does **not** establish that the thesis is free of plagiarism: abstracts are only part of each paper, copyrighted full texts were not all available, and web indexing is incomplete. The required Turnitin report and the author's review of its matches remain necessary.

The 200-rule fashion knowledge base has a separate registry of 39 source URLs. Its September 2026 audit recorded all 39 as reachable. A fresh URL check returned 200 for 38 pages; the remaining MasterClass page returned 403 to the automated client but appeared at its original address in a live search result. The rules are labelled medium reliability and their records explicitly distinguish source-backed styling directions from bounded model enrichment. URL reachability does not verify every clause of those 200 rule texts. The thesis states this limitation in Chapters 2, 3 and 5.

## Remaining submission checks

Current regulations have now been downloaded into [the Salford submission pack](thesis/submission_guidance/README.md), which contains the Hub link, Turnitin access route, forms checklist, SEE support contact and an unsent request draft. The current guide and forms still require University access. The 2026/27 regulations require Notice of Presentation at least two months before intended thesis submission; the author should confirm that this has already been completed for the planned November date.

1. Compare the final files with the current Doctoral School *Guide to the Production, Submission and Examination of your Postgraduate Thesis* from the private Hub. The March 2026 Word-formatting manual in `thesis/` was used for document mechanics, but it is not that research-thesis submission guide. The public 2026/27 Code of Practice points to the private guide for format requirements.
2. Run the final PDF through the University's Turnitin process and review its Originality Report, including quotations, bibliography, overlap with any prior work and the generated appendix examples.
3. Confirm the in-thesis declaration about prior publication or submission, and confirm the ethics approval reference **12425** against the approval document. Arrange the separate signed declaration and supervisor countersignature.
4. Have the author and supervisors review the final argument, numerical interpretations and AI-use acknowledgement under current University guidance. Bibliographic validation and prose editing cannot certify research authorship or the truth of project-specific declarations.
5. If the editable DOCX is requested, review its final pagination in Word. The file opens and Word updates its fields, but the full visual layout review in this audit used the submission PDF.

The public [2026/27 Code of Practice](https://www.salford.ac.uk/sites/default/files/2026-07/pgrcodeofpractice2627.pdf) points to the private guide. The [2026/27 Research Award Regulations](https://www.salford.ac.uk/sites/default/files/2026-07/academicregulationsresearch2627.pdf) require written originality confirmation with supervisor countersignature (19.7) and the Turnitin report with the thesis (21.2). The older public [2024/25 thesis-format appendix](https://www.salford.ac.uk/sites/default/files/2024-09/FinalPGRCodeOfPractice2425.pdf) gives the order and typography used as provisional checks above.

## Bibliography audit

After the submission-readiness audit, the abstract and Chapters 1, 4 and 5 were revised to give the contribution appropriate prominence. The revised framing reports the 21.02-percentage-point trace-support gain alongside the 0.6-point HR@10 reduction, explicitly distinguishes the two experimental comparisons, and consolidates repeated methodological qualifications in Section 5.8. Future ranking improvements remain proposals, not claimed results. The final build, source synchronisation, DOCX integrity, PDF horizontal margin checks and frozen-release audit passed. No new model inference was used to change experimental results.

The number of citations below counts citation locations in the assembled thesis body. Each linked record was checked for existence and bibliographic identity. It does not mean every sentence has been certified against a complete source text.

| No. | Source record | Citation locations | Check |
|---:|---|---:|---|
| 1 | [Image-based recommendations on styles and substitutes](https://doi.org/10.1145/2766462.2767755) | 3 | DOI metadata |
| 2 | [Learning fashion compatibility with bidirectional LSTMs](https://doi.org/10.1145/3123266.3123394) | 6 | DOI metadata |
| 3 | [Learning type-aware embeddings for fashion compatibility](https://doi.org/10.1007/978-3-030-01270-0_24) | 6 | DOI metadata |
| 4 | [Context-aware visual compatibility prediction](https://openaccess.thecvf.com/content_CVPR_2019/html/Cucurull_Context-Aware_Visual_Compatibility_Prediction_CVPR_2019_paper.html) | 2 | Publisher/proceedings |
| 5 | [Learning transferable visual models from natural language supervision](https://proceedings.mlr.press/v139/radford21a.html) | 4 | Publisher/proceedings |
| 6 | [Explainable recommendation: A survey and new perspectives](https://doi.org/10.1561/1500000066) | 2 | DOI metadata |
| 7 | [Reinforcement knowledge graph reasoning for explainable recommendation](https://doi.org/10.1145/3331184.3331203) | 4 | DOI metadata |
| 8 | [Faithfully explainable recommendation via neural logic reasoning](https://doi.org/10.18653/v1/2021.naacl-main.245) | 4 | DOI metadata |
| 9 | [Survey of hallucination in natural language generation](https://doi.org/10.1145/3571730) | 2 | DOI metadata |
| 10 | [Towards faithfully interpretable NLP systems: How should we define and evaluate faithfulness?](https://doi.org/10.18653/v1/2020.acl-main.386) | 7 | DOI metadata |
| 11 | [Attention is not not explanation](https://doi.org/10.18653/v1/D19-1002) | 4 | DOI metadata |
| 12 | [Towards faithful model explanation in NLP: A survey](https://doi.org/10.1162/coli_a_00511) | 3 | DOI metadata |
| 13 | [Retrieval-augmented generation for knowledge-intensive NLP tasks](https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html) | 2 | Publisher/proceedings |
| 14 | [Enabling large language models to generate text with citations](https://doi.org/10.18653/v1/2023.emnlp-main.398) | 7 | DOI metadata |
| 15 | [Towards fine-grained citation evaluation in generated text: A comparative analysis of faithfulness metrics](https://doi.org/10.18653/v1/2024.inlg-main.35) | 3 | DOI metadata |
| 16 | [Measuring Attribution in Natural Language Generation Models](https://aclanthology.org/2023.cl-4.2/) | 5 | Publisher/proceedings |
| 17 | [FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation](https://doi.org/10.18653/v1/2023.emnlp-main.741) | 6 | DOI metadata |
| 18 | [Learning similarity conditions without explicit supervision](https://doi.org/10.1109/ICCV.2019.01047) | 1 | DOI metadata |
| 19 | [Complete the look: Scene-based complementary product recommendation](https://openaccess.thecvf.com/content_CVPR_2019/html/Kang_Complete_the_Look_Scene-Based_Complementary_Product_Recommendation_CVPR_2019_paper.html) | 1 | Publisher/proceedings |
| 20 | [Cumulated gain-based evaluation of IR techniques](https://doi.org/10.1145/582415.582418) | 2 | DOI metadata |
| 21 | [Sentence-BERT: Sentence embeddings using Siamese BERT-networks](https://doi.org/10.18653/v1/D19-1410) | 2 | DOI metadata |
| 22 | [MiniLM: Deep self-attention distillation for task-agnostic compression of pre-trained transformers](https://proceedings.neurips.cc/paper/2020/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html) | 2 | Publisher/proceedings |
| 23 | [Contrastive language and vision learning of general fashion concepts](https://doi.org/10.1038/s41598-022-23052-9) | 2 | DOI metadata |
| 24 | [Explainable fashion compatibility prediction: An attribute-augmented neural framework](https://doi.org/10.1016/j.elerap.2024.101451) | 3 | DOI metadata |
| 25 | [Text2Outfit: Controllable Outfit Generation with Multimodal Language Models](https://doi.org/10.1109/ICCV51701.2025.01500) | 3 | DOI metadata |
| 26 | [A Survey of Explanations in Recommender Systems](https://doi.org/10.1109/ICDEW.2007.4401070) | 4 | DOI metadata |
| 27 | [Explaining the user experience of recommender systems](https://doi.org/10.1007/s11257-011-9118-4) | 4 | DOI metadata |
| 28 | [Attention is not Explanation](https://doi.org/10.18653/v1/N19-1357) | 1 | DOI metadata |
| 29 | [Explainable Fashion Recommendation: A Semantic Attribute Region Guided Approach](https://doi.org/10.24963/ijcai.2019/650) | 3 | DOI metadata |
| 30 | [Explainable Outfit Recommendation with Joint Outfit Matching and Comment Generation](https://doi.org/10.1109/TKDE.2019.2906190) | 3 | DOI metadata |
| 31 | [Personalized Prompt Learning for Explainable Recommendation](https://doi.org/10.1145/3580488) | 2 | DOI metadata |
| 32 | [Recommendation as Language Processing (RLP): A Unified Pretrain, Personalized Prompt & Predict Paradigm (P5)](https://doi.org/10.1145/3523227.3546767) | 2 | DOI metadata |
| 33 | [Language Models Don't Always Say What They Think](https://proceedings.neurips.cc/paper_files/paper/2023/hash/ed3fea9033a80fea1376299fa7863f4a-Abstract-Conference.html) | 2 | Publisher/proceedings |
| 34 | [Towards a rigorous science of interpretable machine learning](https://arxiv.org/abs/1702.08608) | 2 | Primary preprint |
| 35 | [ARES: An automated evaluation framework for retrieval-augmented generation systems](https://doi.org/10.18653/v1/2024.naacl-long.20) | 4 | DOI metadata |
| 36 | [RAGAs: Automated Evaluation of Retrieval Augmented Generation](https://doi.org/10.18653/v1/2024.eacl-demo.16) | 2 | DOI metadata |
| 37 | [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://proceedings.neurips.cc/paper_files/paper/2023/hash/91f18a1287b398d378ef22505bf41832-Abstract-Datasets_and_Benchmarks.html) | 3 | Publisher/proceedings |
| 38 | [The FACTS Grounding Leaderboard](https://arxiv.org/abs/2501.03200) | 1 | Primary preprint |
| 39 | [The Lifecycle of LLM-as-a-Judge for Large-Scale Recommendation Explanations](https://arxiv.org/abs/2608.18300v3) | 3 | Primary preprint |
| 40 | [Polyvore dataset card](https://huggingface.co/datasets/Marqo/polyvore) | 2 | Original card |
| 41 | [Qwen3-Embedding-0.6B model card](https://huggingface.co/Qwen/Qwen3-Embedding-0.6B) | 1 | Original card |
| 42 | [An Introduction to the Bootstrap](https://doi.org/10.1007/978-1-4899-4541-9) | 2 | DOI metadata |
| 43 | [Gemma 4 12B model card](https://huggingface.co/google/gemma-4-12B) | 1 | Original card |
| 44 | [Llama 3.1 8B Instruct model card](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct) | 1 | Original card |
| 45 | [Ministral 3 14B Instruct 2512 model card](https://huggingface.co/mistralai/Ministral-3-14B-Instruct-2512) | 1 | Original card |
| 46 | [Qwen3.5-9B model card](https://huggingface.co/Qwen/Qwen3.5-9B) | 1 | Original card |
| 47 | [Phi-4 model card](https://huggingface.co/microsoft/phi-4) | 1 | Original card |
| 48 | [A simple sequentially rejective multiple test procedure](https://www.jstor.org/stable/4615733) | 2 | Journal archive |
