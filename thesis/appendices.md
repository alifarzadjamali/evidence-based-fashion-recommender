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
