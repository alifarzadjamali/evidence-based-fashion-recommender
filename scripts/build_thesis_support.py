"""Build thesis appendices and a pipeline diagram from the release without inference."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import FancyBboxPatch

ROOT = Path(__file__).resolve().parents[1]
RELEASE = ROOT / "artifacts" / "release"
THESIS = ROOT / "thesis"
MODELS = {
    "gemma4:12b": "Gemma",
    "llama3.1:8b-instruct-q8_0": "Llama",
    "ministral-3:14b-instruct-2512-q4_K_M": "Ministral",
}


def records(name):
    return [
        json.loads(line)
        for line in (RELEASE / f"{name}.jsonl").read_text(encoding="utf-8").splitlines()
    ]


def key(row):
    return row["case_id"], row["generator_model_id"], row["condition"]


def diagram():
    plt.rcParams.update({"font.family": "Arial", "font.size": 12})
    fig, ax = plt.subplots(figsize=(8, 9))
    ax.set(xlim=(0, 10), ylim=(0, 12))
    ax.axis("off")

    def box(x, y, width, height, label, colour="#edf3f7"):
        ax.add_patch(
            FancyBboxPatch(
                (x, y),
                width,
                height,
                boxstyle="round,pad=0.12",
                facecolor=colour,
                edgecolor="#28475c",
            )
        )
        ax.text(x + width / 2, y + height / 2, label, ha="center", va="center", fontsize=16.3)

    def arrow(a, b):
        ax.annotate(
            "", xy=b, xytext=a, arrowprops={"arrowstyle": "->", "color": "#28475c", "lw": 1.5}
        )

    box(0.3, 10, 4.2, 1.25, "Catalogue images + text\nFrozen CLIP fusion\nCompatibility score")
    box(
        5.5,
        10,
        4.2,
        1.25,
        "Source-linked rules\nApplicability filters + retrieval\nEvidence score + exact trace",
    )
    box(
        1.4,
        7.7,
        7.2,
        1.3,
        "Within-pool score normalisation\n0.75 CLIP + 0.25 evidence\nLock "
        "recommendation and contributing trace",
    )
    arrow((2.4, 9.9), (3.6, 9.15))
    arrow((7.6, 9.9), (6.4, 9.15))
    box(0.3, 5.1, 4.2, 1.3, "No-RAG\nRequest + item text (A)\nLocked item", "#f4f1eb")
    box(5.5, 5.1, 4.2, 1.3, "Rule-RAG\nSame A + retained trace (B)\nSame locked item", "#eaf2e9")
    arrow((3.5, 7.55), (2.4, 6.55))
    arrow((6.5, 7.55), (7.6, 6.55))
    ax.text(5, 4.5, "Three generators; shared 45–75-word instruction", ha="center", fontsize=12)
    box(
        1.4,
        2.35,
        7.2,
        1.35,
        "Qwen: atomic claim extraction\nPhi-4: trace, KB, item-fact and citation "
        "labels\nRecorded failures and consistency correction",
    )
    arrow((2.4, 4.95), (3.3, 3.85))
    arrow((7.6, 4.95), (6.7, 3.85))
    box(
        1.4,
        0.1,
        7.2,
        1.2,
        "Complete generator pairs\nWithin-case averaging + case "
        "bootstrap\nSupport rates, density and descriptive citations",
    )
    arrow((5, 2.2), (5, 1.45))
    fig.tight_layout(pad=0.5)
    destination = THESIS / "figures"
    destination.mkdir(exist_ok=True)
    fig.savefig(destination / "pipeline.png", dpi=240, bbox_inches="tight")
    fig.savefig(destination / "pipeline.svg", bbox_inches="tight")
    svg = destination / "pipeline.svg"
    svg.write_text(
        "\n".join(line.rstrip() for line in svg.read_text(encoding="utf-8").splitlines()) + "\n",
        encoding="utf-8",
    )
    plt.close(fig)


def appendices():
    generations, extractions, verifications = (
        records(n) for n in ("explanations", "extractions", "verifications")
    )
    cases = {r["case_id"]: r for r in records("explanation_cases")}
    accepted = [
        {key(r): r for r in rows if r["status"] == "accepted"}
        for rows in (generations, extractions, verifications)
    ]
    counts = [
        Counter((r["generator_model_id"], r["condition"]) for r in rows.values())
        for rows in accepted
    ]
    out = [
        "# Appendix A: Supplementary quantitative results",
        "## A.1 Pipeline denominators",
        "Table A.1 counts accepted records, with 500 generation attempts for "
        "each generator–condition cell. Extraction starts from accepted "
        "generation, and verification starts from accepted extraction. A "
        "complete support pair requires accepted verification in both "
        "conditions.",
        "*Table A.1. Accepted records by generator, condition and pipeline stage.*",
        "| Generator / condition | Generated | Extracted | Verified |",
        "|---|---:|---:|---:|",
    ]
    for model, label in MODELS.items():
        for condition in ("no_rag", "rule_rag"):
            out.append(
                f"| {label} / {'No-RAG' if condition == 'no_rag' else 'Rule-RAG'} | "
                + " | ".join(str(c[model, condition]) for c in counts)
                + " |"
            )
    out += [
        "\n*Table A.2. Complete generator pairs for support and restricted UIFR.*",
        "| Generator | Support pairs | UIFR pairs |",
        "|---|---:|---:|",
    ]
    contrasts = pd.read_csv(RELEASE / "explanation_paired_contrasts.csv")
    for model, label in MODELS.items():
        rows = contrasts[
            (contrasts.scope == "generator") & (contrasts.scope_value == model)
        ].set_index("metric")
        out.append(
            f"| {label} | {int(rows.loc['trace_support_rate', 'paired_cases'])} | "
            f"{int(rows.loc['unsupported_item_fact_rate', 'paired_cases'])} |"
        )
    out += [
        "Across generators, the corresponding counts of underlying cases are "
        "498 and 53. These are case counts after within-case averaging, not the "
        "sum of generator pairs.",
        "## A.2 Recommendation estimates and intervals",
        "The following tables reproduce the micro estimates and percentile 95% "
        "intervals in `recommendation_metrics_with_ci.csv`. Values are "
        "percentages, shown to three decimal places. Intervals use 5,000 "
        "resamples of the 734 query outfits. DFH denotes the released first-hit "
        "discount; its source columns are named `ndcg_at_5` and `ndcg_at_10`. "
        "Section 3.8.1 explains the distinction from multi-positive NDCG.",
    ]
    rec = pd.read_csv(RELEASE / "recommendation_metrics_with_ci.csv")
    rec = rec[(rec.aggregation == "micro") & (rec.category == "all")]
    for number, (method, label) in enumerate(
        (
            ("minilm_text", "MiniLM text"),
            ("clip_image", "CLIP image"),
            ("clip_text", "CLIP text"),
            ("fused_clip", "Fused CLIP"),
            ("evidence_rerank", "Evidence rerank"),
        ),
        3,
    ):
        out += [
            f"*Table A.{number}. {label}: recommendation estimates and 95% intervals (%).*",
            "| Metric | Estimate | 95% CI |",
            "|---|---:|---:|",
        ]
        rows = rec[rec.method == method].set_index("metric")
        for metric, title in (
            ("hr_at_1", "HR@1"),
            ("hr_at_5", "HR@5"),
            ("hr_at_10", "HR@10"),
            ("ndcg_at_5", "DFH@5"),
            ("ndcg_at_10", "DFH@10"),
            ("mrr", "MRR"),
        ):
            r = rows.loc[metric]
            out.append(
                f"| {title} | {100 * r.estimate:.3f} | "
                f"{100 * r.ci_lower:.3f} to {100 * r.ci_upper:.3f} |"
            )
    out += [
        "\n\\newpage\n",
        "# Appendix B: Paired examples and automated judgements",
        "These examples reproduce generated text and recorded labels without "
        "correction. They are illustrations, not human-validated judgements or "
        "a representative estimate of error frequency. To avoid choosing only "
        "favourable outputs, selection takes the lowest case ID with a complete "
        "Gemma pair and a single retained rule in each of two categories, tops "
        "and bags. Claim IDs are local to each explanation. The full release "
        "preserves the remaining generators and cases.",
    ]
    g, x, v = accepted
    for number, category in enumerate(("tops", "bags"), 1):
        candidates = sorted(
            cid
            for cid, r in cases.items()
            if r["target_category"] == category
            and len(r["exact_stored_rule_trace_B"]["rules"]) == 1
            and all((cid, "gemma4:12b", c) in v for c in ("no_rag", "rule_rag"))
        )
        cid = candidates[0]
        case = cases[cid]
        out += [
            f"## B.{number} {category.capitalize()} example",
            f"Case `{cid}`; generator Gemma 4 12B; locked item `{case['locked_candidate_id']}`.",
        ]
        for field, label in (
            ("user_request", "Request"),
            ("query_item_minimal_name", "Query item"),
            ("locked_item_minimal_name", "Recommended item"),
        ):
            out.append(f"{label}: {case['common_context_A'][field]}")
        trace = case["exact_stored_rule_trace_B"]
        for rule in trace["rules"]:
            out += [
                f"Retained rule `{rule['rule_id']}` "
                f"(contribution {rule['weighted_contribution']:.6f}):",
                "> " + rule["rule_text"],
            ]
        for condition in ("no_rag", "rule_rag"):
            k = (cid, "gemma4:12b", condition)
            out += [
                f"### B.{number}.{'1' if condition == 'no_rag' else '2'} "
                f"{'No-RAG' if condition == 'no_rag' else 'Rule-RAG'}",
                "> " + g[k]["explanation"],
            ]
            claim_text = {c["claim_id"]: c["claim_text"] for c in x[k]["claims"]}
            out.append(
                "Recorded claim judgements follow. T = trace support; K = full-KB "
                "support; I = common-reference support; C = citation entailment."
            )
            for c in v[k]["claims"]:
                out.append(
                    f"**{c['claim_id']}.** {claim_text[c['claim_id']]}\n\n"
                    f"T: {c['trace_support']}; K: {c['full_kb_support']}; "
                    f"I: {c['common_reference_support']}; C: {c['citation_entailment']}."
                )
        out.append(
            "The labels above are outputs of the frozen automated assessment. A "
            "supported label should be read against the quoted rule and catalogue "
            "context; it does not independently verify the product or establish the "
            "correctness of the rule."
        )
    (THESIS / "appendices.md").write_text(
        "\n\n".join(out).replace("|\n\n|", "|\n|") + "\n", encoding="utf-8", newline="\n"
    )


if __name__ == "__main__":
    diagram()
    appendices()
    print("Built thesis diagram and appendices from frozen records; no model calls.")
