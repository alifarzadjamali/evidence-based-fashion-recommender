"""Render the consolidated thesis PDF with A4 pages and sectioned numbering."""

import json
import re
from pathlib import Path

import pypandoc
import typst
import yaml
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
THESIS = ROOT / "thesis"
SOURCE = THESIS / "final_thesis.md"
OUTPUT = THESIS / "final_thesis.pdf"
TYPST_SOURCE = THESIS / "final_thesis.typ"


def main() -> None:
    markdown = SOURCE.read_text(encoding="utf-8")
    metadata = yaml.safe_load(markdown.split("---", 2)[1])
    body = (
        pypandoc.convert_file(
            str(SOURCE),
            "typst",
            format="markdown+raw_tex+tex_math_single_backslash",
            extra_args=[f"--resource-path={THESIS}"],
        )
        .replace("\r\n", "\n")
        .replace("\r", "\n")
    )
    front, chapters = body.split("= Chapter 1: Introduction", 1)
    chapters = "= Chapter 1: Introduction" + chapters
    front = front.replace(
        "= Contents\n<contents>",
        "#pagebreak()\n#heading(level: 1, outlined: false)[Contents]\n<contents>\n"
        "#outline(title: none, depth: 3)",
    )
    front = re.sub(
        r"(?m)^= (List of figures|List of tables|Abbreviations|Abstract)$",
        r"#pagebreak()\n= \1",
        front,
    )
    chapters = re.sub(
        r"(?m)^= (Chapter [2-5]:|References)",
        r"#pagebreak()\n= \1",
        chapters,
    )

    title_lines = [
        f'#text({json.dumps(metadata["title"])}, size: 16pt, weight: "bold")',
        "#v(2cm)",
        *[
            f"#text({json.dumps(line.strip())})#linebreak()"
            for line in metadata["subtitle"].splitlines()
        ],
        "#v(1cm)",
        f"#text({json.dumps(metadata['author'])})#linebreak()",
        f"#text({json.dumps(metadata['date'])})",
    ]
    title = "\n".join(title_lines)
    typst_text = (
        '#set page(paper: "a4", margin: 2.54cm)\n'
        '#set text(font: "Times New Roman", size: 12pt)\n'
        "#set par(leading: 0.65em, justify: false)\n"
        "#show table: set text(size: 9pt)\n"
        f"#align(center)[\n{title}\n]\n"
        "#pagebreak()\n"
        '#set page(numbering: "i")\n'
        "#counter(page).update(1)\n"
        + front
        + '\n#pagebreak()\n#set page(numbering: "1")\n#counter(page).update(1)\n'
        + chapters
    )
    TYPST_SOURCE.write_text(typst_text, encoding="utf-8", newline="\n")
    typst.compile(str(TYPST_SOURCE), output=str(OUTPUT), root=str(ROOT))

    labels = {
        "Figure 4.1.": "Paired explanation contrasts with 95% case-clustered bootstrap intervals.",
        "Table 2.1.": "Representative research strands and the gap addressed by this thesis.",
        "Table 4.1.": "Micro-averaged recommendation effectiveness on 1,000 frozen test cases.",
        "Table 4.2.": "Overall paired explanation contrasts (Rule-RAG minus No-RAG).",
    }
    pages = {}
    reader = PdfReader(OUTPUT)
    body_started = False
    for page in reader.pages:
        content = page.extract_text() or ""
        if "Chapter 1: Introduction" in content and re.search(r"\n1\s*$", content):
            body_started = True
        if not body_started:
            continue
        for label in labels:
            if label in content and label not in pages:
                number = re.search(r"\n(\d+)\s*$", content)
                if number:
                    pages[label] = number.group(1)
    if len(pages) != len(labels):
        raise ValueError(f"Could not locate all figure/table captions in PDF: {pages}")

    def list_grid(items: list[str]) -> str:
        cells = []
        for label in items:
            cells.append(f"[#text({json.dumps(label + ' ' + labels[label])})]")
            cells.append(f"[{pages[label]}]")
        return (
            "#grid(columns: (1fr, auto), column-gutter: 1em, row-gutter: 0.35em,\n"
            + ",\n".join(cells)
            + ")"
        )

    typst_text = re.sub(
        r"(?s)(= List of figures\n<list-of-figures>\n).*?(?=\n#pagebreak\(\)\n= List of tables)",
        lambda match: match.group(1) + list_grid(["Figure 4.1."]) + "\n",
        typst_text,
    )
    typst_text = re.sub(
        r"(?s)(= List of tables\n<list-of-tables>\n).*?(?=\n#pagebreak\(\)\n= Abbreviations)",
        lambda match: match.group(1) + list_grid(["Table 2.1.", "Table 4.1.", "Table 4.2."]) + "\n",
        typst_text,
    )
    TYPST_SOURCE.write_text(typst_text, encoding="utf-8", newline="\n")
    typst.compile(str(TYPST_SOURCE), output=str(OUTPUT), root=str(ROOT))
    TYPST_SOURCE.unlink()
    print(f"Rendered {OUTPUT}")


if __name__ == "__main__":
    main()
