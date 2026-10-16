"""Render the thesis PDF with numbered equations and tables that can span pages."""

import json
import re
from pathlib import Path

import pypandoc
import typst
import yaml
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
THESIS = ROOT / "thesis"


def main() -> None:
    markdown = (THESIS / "final_thesis.md").read_text(encoding="utf-8")
    equation_numbers = re.findall(r"\\tag\{([^}]+)\}", markdown)
    metadata = yaml.safe_load(markdown.split("---", 2)[1])
    markdown = re.sub(r"\\tag\{([^}]+)\}", lambda m: r"\qquad\text{(" + m[1] + ")}", markdown)
    body = (
        pypandoc.convert_text(
            markdown, "typst", format="markdown+raw_tex+tex_math_single_backslash"
        )
        .replace("\r\n", "\n")
        .replace("\r", "\n")
    )
    captions = []

    def caption(match):
        kind, number, text = match.groups()
        text = " ".join(text.split())
        label = f"caption-{kind.lower()}-{number}"
        captions.append((kind, number, text, label))
        sticky = "true" if kind == "Table" else "false"
        page_break = "#pagebreak(weak: true)\n" if kind == "Table" and number == "2.1" else ""
        return (
            page_break + f"#block(above: 0.8em, below: 0.4em, sticky: {sticky})"
            f"[#emph[{kind} {number}. {text}]] <{label}>"
        )

    body = re.sub(r"#emph\[(Table|Figure) ([A-Z0-9]+\.\d+)\. (.*?)\]", caption, body, flags=re.S)
    front, chapters = body.split("= Chapter 1: Introduction", 1)
    chapters = "= Chapter 1: Introduction" + chapters
    front = re.sub(
        r"= Contents\n<contents>.*?(?=\n= List of figures)",
        "#heading(level: 1, outlined: false)[Contents]\n#outline(title: none, depth: 3)\n",
        front,
        flags=re.S,
    )

    def list_body(kind):
        cells = []
        for found, number, text, label in captions:
            if found == kind:
                text = text.split(". ", 1)[0].rstrip(".") + "."
                cells += [
                    f"[#link(<{label}>)[{kind} {number}. #text({json.dumps(text)})]]",
                    f"[#context counter(page).at(<{label}>).first()]",
                ]
        return (
            "#grid(columns: (1fr, auto), column-gutter: 1em, row-gutter: 0.6em,\n"
            + ",\n".join(cells)
            + ")\n"
        )

    for heading, kind in (("List of figures", "Figure"), ("List of tables", "Table")):
        front = re.sub(
            r"= " + heading + r"\n<[^>]+>.*?(?=\n= )",
            lambda m, heading=heading, kind=kind: "= " + heading + "\n" + list_body(kind),
            front,
            flags=re.S,
        )
    front = re.sub(
        r"(?m)^= (List of figures|List of tables|Declaration|Abbreviations|Abstract)$",
        r"#pagebreak()\n= \1",
        front,
    )
    chapters = re.sub(
        r"(?m)^= (Chapter [2-5]:|References|Appendix [A-Z]:)",
        r"#pagebreak()\n= \1",
        chapters,
    )
    chapters = chapters.replace(
        "columns: (14.29%, 14.29%, 14.29%, 14.29%, 14.29%, 14.29%, 14.29%),",
        "columns: (23%, 12%, 12%, 12%, 14%, 14%, 13%),",
    )
    # Long comparison tables may span pages. Keep smaller tables together.
    body_table = re.compile(
        r"#figure\(\s+align\(center\)\[(#table\(.*?\))\]\s*, kind: table\s*\)", re.S
    )

    def table_block(match):
        value = match[1]
        if "[Paired cases]" in value:
            value = re.sub(
                r"columns: \([^)]*\)", "columns: (32%, 12%, 17%, 24%, 15%)", value, count=1
            ).replace("[Paired cases]", "[Cases]")
        breakable = "true" if "[Study]" in value else "false"
        return f"#block(breakable: {breakable})[#align(center)[{value}]]"

    front = body_table.sub(table_block, front)
    chapters = body_table.sub(table_block, chapters)
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
    preamble = """#set page(paper: "a4", margin: 3cm)
#set text(font: "Arial", size: 12pt, top-edge: 0.75em, bottom-edge: 0.25em)
#set par(leading: 0.75em, spacing: 1.25em, justify: false)
#show raw: set text(font: "Arial", size: 12pt)
#show figure.where(kind: table): set block(breakable: true)
#set table(inset: 5pt, stroke: 0.4pt)
#show table.header: set text(weight: "bold")
#show heading.where(level: 1): set text(size: 16pt)
#show heading.where(level: 2): set text(size: 14pt)
#show heading.where(level: 3): set text(size: 12pt)
#show quote: set par(leading: 0.25em)
"""
    result = (
        preamble + "#align(center)[\n" + "\n".join(title_lines) + "\n]\n"
        '#pagebreak()\n#set page(numbering: "i")\n#counter(page).update(1)\n'
        + front
        + '\n#pagebreak()\n#set page(numbering: "1")\n#counter(page).update(1)\n'
        + chapters
    )
    source = THESIS / "final_thesis.typ"
    source.write_text(result, encoding="utf-8", newline="\n")
    try:
        typst.compile(str(source), output=str(THESIS / "final_thesis.pdf"), root=str(ROOT))
    finally:
        source.unlink()
    rendered = "\n".join(
        page.extract_text() or "" for page in PdfReader(THESIS / "final_thesis.pdf").pages
    )
    missing = [number for number in equation_numbers if f"({number})" not in rendered]
    if missing:
        raise ValueError(f"Equation numbers missing from PDF: {missing}")
    print("Rendered final_thesis.pdf with 12-point Arial and 18-point body baselines.")


if __name__ == "__main__":
    main()
