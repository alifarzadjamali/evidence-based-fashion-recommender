# Pre-submission review: *Evidence-Constrained Multimodal Fashion Recommendation with Trace-Grounded Explanations*

> Historical review of the draft as it stood on 12 October 2026. For checks on the revised thesis, see [thesis_submission_audit.md](thesis_submission_audit.md). Page numbers and several findings below no longer describe the current document.

**Thesis:** MPhil, School of Science, Engineering and Environment, University of Salford (author: Ali Jamali; planned submission November 2026)
**Review date:** 12 October 2026
**What was reviewed:** structure, literature review, formatting against Salford rules, whether the sources are real and cited correctly, claims with no source, plagiarism risk, signs of AI writing, and other things that could cause problems at submission.
**Not reviewed:** methodology and results, except for one internal-consistency note in section 9.

Page numbers below are the ones printed on the thesis pages.

---

## Summary

The thesis is not ready to submit yet, though most of the fixes are mechanical. The most serious problems are:

- a broken table (Table 2.1)
- one reference that looks invented ([22])
- layout that does not meet Salford's research-thesis rules
- leftover sentences from earlier drafts
- writing that reads as heavily AI-generated

---

## 1. Fix before submitting

1. **Table 2.1 is broken (p.14).** The last three rows (Jacovi & Goldberg [10], Gao [14], Saad-Falcon [24]) are printed on top of each other and over the page number, so they cannot be read. The caption has ended up on p.15, away from the table.
2. **Reference [22] has the wrong title and the wrong first-author initial.** The real paper is "Text2Outfit: *Controllable Outfit Generation with Multimodal Language Models*" by **Zhai, Y.** (Yuanhao), not "W.". The page numbers and DOI are correct. This is what a made-up citation looks like, and that would be a serious problem in a misconduct case.
3. **Leftovers from earlier drafts.** These sentences only make sense to someone who saw a previous version:
   - p.39: "cannot sustain the earlier conclusion of substantial citation integrity" — no such earlier conclusion exists in this thesis.
   - p.42: "Evidence Overreach Rate was removed" — this measure is never introduced.
   - p.43: "It was not added late to the present thesis"
   - p.35: "legacy outcome names"
   - p.19 and p.35: "authorised verifier-contract correction" — authorised by whom?
4. **Material referred to but never shown.** This includes:
   - the qualitative examples (p.27, p.39)
   - the "released table" (p.31) and the "denominator table" (p.34)
   - the larger-pool sensitivity results (p.29, p.41)
   - the validation grids and Pareto procedure (p.22, p.24)

   Either add appendices or remove the references. Also, the citation precision and coverage figures (87.5%, 0.23%) appear for the first time in the Discussion (§5.3.3). They belong in Chapter 4.
5. **Ethics approval is never mentioned.** The regulations require an ethics application with a "Favourable Opinion outcome" before any data collection, and say students "must retain a copy to present at assessments" (Regs 9.1–9.3). Add a one-line statement.
6. **Submission paperwork.**
   - A separate signed Declaration of Originality, countersigned by the supervisor (Reg. 19.7).
   - A Turnitin Originality Report submitted with the thesis (Reg. 21.2).

---

## 2. Formatting against Salford's rules

There is no public School of Science, Engineering and Environment dissertation template, and that template would be for taught degrees anyway. An MPhil follows the research-degree thesis rules. The most recent public version of those is **Appendix 2 of the 2024/25 research-student Code of Practice**. The current Code points to a Doctoral School guide that is not public, so confirm with PGR Support that nothing has changed.

| Rule | This thesis | Status |
|---|---|---|
| "12 point, using a sans-serif font" | Times New Roman 12pt, which is a serif font | ❌ |
| "One-and-a-half, or else double, spacing" | About 1.15 spacing (single) | ❌ |
| Margins: at least 30mm at the document edge, at least 20mm elsewhere | 25.4mm on every side | ❌ |
| The contents page "shall immediately follow the title page" | Declaration comes before Contents | ⚠️ |
| Order: Contents → lists → Acknowledgements → Declaration → Abbreviations → Abstract | No Acknowledgements; Declaration out of place | ⚠️ |
| Abstract no longer than 300 words | 256 words | ✅ |
| MPhil maximum 50,000 words | About 18,000 words of body text | ✅ (but thin) |
| Page numbering: roman numerals for front matter, then consecutive | Correct | ✅ |
| Numbered citations listed in order of appearance | Correct | ✅ |

### Smaller layout problems

- **Equations:**
  - The indicator "1" overprints the text in the formulas on p.22, p.25 and p.26.
  - p.18 refers to "Equation (3.1)", but no equations are numbered.
  - NDCG is defined twice on p.23.
  - α = 0.40 is stated twice on p.20.
  - "HR@ K" has a stray space.
  - A full stop comes before "where" and "which" after the displayed equations on p.20–21.
- **Tables:** table captions sit below the tables. They usually go above.
- **Numbers:**
  - p.39 uses a hyphen in "-5.03"; Table 4.2 uses a proper minus sign.
  - Chapter 4 gives percentages and Chapter 5 gives decimals for the same results.
- **Abbreviations list:** LSTM, CNN, NLP, FLOPs, SHA-256, pp and RQ are missing. FITB is listed but never used.
- **Title page:** the student ID will become public once the thesis is deposited in the university repository (USIR). Consider removing it.

---

## 3. Structure

- The five-chapter structure (Introduction, Literature Review, Methodology, Results, Discussion and Conclusion) is fine.
- There is **no system or pipeline diagram**. The thesis has only one figure, which is unusual for a systems thesis.
- **The literature review reports the thesis's own design and results.** Examples are on p.8 (exact-image hashing; "the completed results support…"), p.11 (the verifier "frequently returned null…") and p.13 (the average word counts of 62.10 and 64.83). Move these to Chapters 3–4.
- **The same headline numbers come back again and again.** 21.02 and 21.40 appear seven times each, 26.5% five times, and "53 pairs" six times. Cut most of the repeats.
- **§5.11 should answer RQ1–RQ4 and the four objectives explicitly, one by one.** At the moment the RQs are only answered in §4.7.
- There are no Acknowledgements and no appendices.
- The contributions are listed in §1.5 (four) and again in §5.7 (four, plus "two negative contributions"). Make the two lists match.

---

## 4. Literature review

- It is short for an MPhil: about 10 pages and 28 references in total.
- It mostly works through one paper per paragraph. Most of the comparison between studies sits in Table 2.1, which is the broken table.
- **The biggest gap: no explainable *fashion* recommendation work is reviewed.** That is the closest prior work, and examiners will ask about it. Worth looking at (check each one before citing):
  - Hou et al. 2019 (IJCAI), on fashion explanation
  - Lin et al. 2020 (TKDE), on explainable outfit recommendation
  - PEPLER (Li, Zhang & Chen 2023) and P5 (Geng et al. 2022), on language-model-based explanations
  - Turpin et al. 2023, on whether language models' own explanations are faithful
  - Rashkin et al. 2023, on attribution
  - FActScore (Min et al. 2023), on atomic claims
  - RAGAS (Es et al. 2024)
  - Zheng et al. 2023, on using language models as judges
  - Tintarev & Masthoff (2007/2011), on what explanations are for
  - Jain & Wallace 2019, on the attention debate
- The gaps in §2.7.2 are stated without any citations showing that each gap actually exists.

---

## 5. Are the sources real and cited correctly?

All 28 references exist. The problems are listed below.

### Wrong reference or wrong use of a source

- **[22]:** wrong title and first-author initial (see section 1).
- **[9] Knijnenburg et al. (2012) is used for the wrong thing, in three places.** The paper is a framework for evaluating the *user experience* of recommender systems. It is not about explaining recommendations. It does not support:
  - the list of explanation goals (transparency, scrutability, trust…) on p.9 — that list comes from Tintarev & Masthoff
  - "feature-based, review-based, knowledge-graph… rationales" on p.1
  - "explanation properties" being a separate level in its framework
- **[1]** is cited for Polyvore data on p.19, but McAuley et al. used Amazon data.
- **[14]:** "distinguish correctness from completeness" (p.11 and Table 2.1) is inaccurate. That paper's benchmark measures fluency, correctness, and citation recall and precision.
- **[18]:** the (2^rel − 1)/log₂(k+1) form of NDCG on p.23 comes from Burges et al. (2005), not from Järvelin & Kekäläinen.
- **[12]:** the paper's category is "backpropagation-based", not "gradient".
- **[28]** is not cited on p.12, which is where its framework (functionally-, application- and human-grounded evaluation) is used.

### Reference details

- [9] is missing the issue number, 22(4–5).
- [3] should cite the published conference proceedings version (LNCS vol. 11220), pp. 405–421.
- [10] has the wrong closing quotation mark after "faithfulness?".
- [26] gives "Chapman & Hall/CRC", but the 1993 publisher was Chapman & Hall, New York.
- Eight entries shorten the author list to "et al." while the others list every author. Pick one approach.
- [21]: the title, journal, volume and article number check out. The author list could not be checked automatically, so confirm it on ScienceDirect.

### Models and dataset not cited at all

Gemma 4 12B, Llama 3.1 8B Instruct, Ministral 3 14B Instruct, Qwen 3.5 9B, Phi-4, Qwen3-Embedding-0.6B and the Hugging Face `Marqo/polyvore` dataset are all real. None of them is cited. Cite each one's technical report or model card.

### Referencing style

Salford's research-thesis rules accept numbered citations listed in order of appearance, so the numbering is fine. The reference entries are written in a Harvard-like format. The university's main style is APA 7, so confirm the expected style with the supervisors and apply one format consistently.

---

## 6. Claims with no source

| Page | Claim | Suggested fix |
|---|---|---|
| p.1 | Language models "add likely-sounding colours, materials…" | Cite [23] or other work on hallucination |
| p.2 | Colour, material and similar descriptions are "easy to generate plausibly" | Add a source or soften the claim |
| p.2–3 | Quality scores "can conceal source-specific failures" | Add a source |
| p.7–8 | Metrics sentence cites [18], which only supports NDCG | Cite [2] and [3] for fill-in-the-blank and compatibility tasks |
| p.8 | "Polyvore co-occurrence is a practical but incomplete relevance proxy" | Add a source |
| p.8 | "outfit-disjoint logic used in prior work" | Say which work (Vasileva et al. [3]) |
| p.9 | Post-hoc methods (surrogate features, attention, generated rationales) | Add sources |
| p.10 | Attention-as-explanation debate | Also cite Jain & Wallace (2019) |
| p.10 | RAG "has become a common strategy…"; its use in recommendation | Add sources |
| p.11 | Citation precision and coverage "adopted" | Attribute to [14] |
| p.12 | Functionally-, application- and human-grounded evaluation | Cite [28] |
| p.13 | Atomic-claim extraction approach | Cite FActScore (Min et al. 2023) |
| p.13 | "Explanation length is a major design issue" | Add a source |
| p.13 | "Same model family… can create correlated errors" | Add a source |
| p.39 | "evidence theatre" in quotation marks | Either cite where it comes from or remove the quotation marks |

---

## 7. Plagiarism

Every sentence that describes a cited paper was compared with that paper's abstract. **No copying was found.** The closest matches are short, cited paraphrases of [4] Cucurull et al. and [8] Zhu et al., and a list of technical terms taken from [24] ARES.

This review could not run Turnitin, and a Turnitin Originality Report is required anyway (Reg. 21.2). If any chapter has already been published, say so explicitly in the declaration. Salford's misconduct procedure treats unacknowledged reuse of published work as self-plagiarism and says this is "particularly relevant for students on Postgraduate Research Awards".

---

## 8. Does it read as AI-written?

**It reads as heavily AI-generated or AI-rewritten.** This cannot be proven, and no detector is reliable. Detector models could not be run for this review because the site that hosts them was blocked, so this judgement comes from measuring writing patterns and reading closely.

### What points that way

- **Constant negation and contrast.** There are 12.3 "not/cannot" per 1,000 words, roughly 2–3 times what is normal in academic writing. 23% of sentences contain a negation, and "rather than" appears 50 times. Lines like "post-hoc alignment, not grounding" run all the way through.
- **Very even sentence length.** The average is 18–21 words in every chapter.
- **Neat one-line paragraph endings**, such as "Preserving this mixed result is part of the empirical contribution" and "This conclusion is deliberately useful rather than maximal".
- **The draft leftovers in section 1, the invented title for [22] and the misreading of [9].** These are typical of text produced by repeatedly asking an AI to revise, and of sources that were not read in full.
- **Absent:** the classic ChatGPT words ("delve", "pivotal") and em dashes. Simple word-list checks would not flag it, but statistical detectors like Turnitin's probably would.

### Salford's position on generative AI

- Detection tools "are not institutionally approved and must not be used to investigate suspected cases of academic misconduct" (generative AI policy, paragraph 40).
- Misconduct is using AI "to intentionally mislead others or misrepresent the abilities or understanding of an individual" (paragraph 37).
- Use of AI in research is covered by a separate research statement. Ask the supervisors or the Doctoral School whether an AI acknowledgement is needed. If AI helped with the drafting, add one, and rewrite Chapters 2 and 5 in the author's own voice. The viva is where this will actually be tested.
- Salford's guidance also says never to put "unpublished research, your own or anyone else's work" into AI tools the university has not approved. Microsoft 365 Copilot is the approved one.

---

## 9. One thing outside the review's scope

The citation-entailment counts on p.32 (1,820 entails against 5,502 does not entail) do not obviously match the figures on p.39 (24 evaluated citation relations; "19 of 8,275" claims). An examiner is likely to spot this, so reconcile the two or explain how they differ.

---

## How this review was done, and its limits

- This review was prepared with an AI assistant (Claude).
- All 57 pages were read. Font sizes, margins and line spacing were measured from the PDF.
- Each reference was checked against publisher pages, the ACL Anthology, CVF Open Access, arXiv, NeurIPS and PMLR proceedings, and Nature.
- Salford's rules were taken from official university documents (listed below).
- Turnitin and AI-detector models could not be run.
- The suggested additional literature should be checked before it is cited.

---

## Sources

- [Salford PGR Code of Practice 2024/25 (Appendix 2: thesis format)](https://salford.ac.uk/sites/default/files/2024-09/FinalPGRCodeOfPractice2425.pdf)
- [Salford PGR Code of Practice 2026/27](https://www.salford.ac.uk/sites/default/files/2026-07/pgrcodeofpractice2627.pdf)
- [Academic Regulations for Research Awards 2026/27](https://www.salford.ac.uk/sites/default/files/2026-07/academicregulationsresearch2627.pdf)
- [Generative AI in Learning, Teaching and Assessment Policy (May 2026)](https://www.salford.ac.uk/sites/default/files/2026-05/generativeaipolicy.pdf)
- [Using GenAI at Salford](https://www.salford.ac.uk/skills/using-gen-ai-at-salford)
- [Student Academic Integrity Policy and Academic Misconduct Procedure (Jan 2026)](https://www.salford.ac.uk/sites/default/files/2026-01/studentacademicintegritypolicyacademicmisconductprocedure.pdf)
- [Salford referencing guidance](https://www.salford.ac.uk/skills/referencing-and-plagiarism)
- [Text2Outfit at ICCV 2025](https://iccv.thecvf.com/virtual/2025/poster/993)
- [Text2Outfit on ML Anthology](https://mlanthology.org/iccv/2025/zhai2025iccv-text2outfit)
- [ScienceDirect entry for reference [21]](https://www.sciencedirect.com/science/article/abs/pii/S1567422324000966)
