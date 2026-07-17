#!/usr/bin/env python3
"""Render a tailored resume/cover-letter Markdown file (docs/prospectives or
docs/submitted) to PDF. Unlike generate_resume.py, this does not scrape
index.html -- it renders whatever Markdown file you point it at directly.
"""

import sys
from pathlib import Path

import markdown as md

RESUME_CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 10pt;
  color: #111;
  background: #fff;
  max-width: 7.5in;
  margin: 0 auto;
  padding: 0.75in 0.75in;
  line-height: 1.45;
  overflow-wrap: break-word;
}
a { color: #111; }

h1 {
  font-size: 22pt;
  font-weight: 700;
  margin-bottom: 2pt;
}
h1 + p {
  font-size: 8.5pt;
  color: #333;
  margin-bottom: 10pt;
}
h1 + p a { color: #333; }

h2 {
  font-size: 9pt;
  font-weight: 700;
  text-transform: uppercase;
  border-bottom: 1.5px solid #111;
  padding-bottom: 2pt;
  margin: 14pt 0 7pt;
}

h3 {
  font-size: 10pt;
  font-weight: 700;
  margin-top: 8pt;
}

h3 + p {
  font-size: 9pt;
  color: #555;
  margin-bottom: 3pt;
}

p {
  font-size: 9.5pt;
  color: #222;
  margin: 2pt 0;
}

hr {
  border: none;
  border-top: 1px solid #ccc;
  margin: 8pt 0;
}

ul {
  margin: 4pt 0 6pt 14pt;
  padding: 0;
}
li {
  font-size: 9pt;
  color: #222;
  margin-bottom: 2pt;
}

strong { font-weight: 700; }
em { font-style: italic; }

@media print {
  body { padding: 0; }
}
"""

# Cover letters (see CLAUDE.md) use no headings at all -- just a bold name,
# a plain contact line, and paragraphs -- so they're styled by paragraph
# position rather than heading level.
LETTER_CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 10.5pt;
  color: #111;
  background: #fff;
  max-width: 7.5in;
  margin: 0 auto;
  padding: 0.9in 0.9in;
  line-height: 1.5;
  overflow-wrap: break-word;
}
a { color: #111; }

body > p:first-of-type strong {
  display: block;
  font-size: 15pt;
  margin-bottom: 2pt;
}

p {
  margin: 9pt 0;
}

hr {
  border: none;
  border-top: 1px solid #ccc;
  margin: 10pt 0;
}

strong { font-weight: 700; }
em { font-style: italic; }

@media print {
  body { padding: 0; }
}
"""


def convert(md_path: Path, out_path: Path) -> None:
    from weasyprint import HTML

    is_cover_letter = "cover-letter" in md_path.stem
    css = LETTER_CSS if is_cover_letter else RESUME_CSS

    text = md_path.read_text(encoding="utf-8")
    body_html = md.markdown(text, extensions=["extra", "sane_lists", "nl2br"])

    kind = "Cover Letter" if is_cover_letter else "Resume"
    title = md_path.stem.replace("-", " ").replace("_", " ").title()
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{title} {kind}</title>
<style>{css}</style>
</head>
<body>
{body_html}
</body>
</html>"""

    out_path.parent.mkdir(parents=True, exist_ok=True)
    HTML(string=html).write_pdf(str(out_path))
    print(f"{kind} saved to {out_path}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scripts/generate_tailored_resume.py <path/to/file.md>")
        sys.exit(1)

    md_path = Path(sys.argv[1])
    if not md_path.exists():
        print(f"File not found: {md_path}")
        sys.exit(1)

    repo_root = Path(__file__).parent.parent
    out_path = repo_root / "docs" / "pdf" / f"{md_path.stem}.pdf"

    convert(md_path, out_path)
