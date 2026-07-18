#!/usr/bin/env python3
"""Generate a job-application-friendly resume PDF from portfolio HTML content."""

import html as html_lib
import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup


def clean_text(el) -> str:
    """Extract element text with single spaces, so inline tags like <b>
    don't glue words together ("achieving99.5%via") in the PDF text layer."""
    if el is None:
        return ""
    return re.sub(r"\s+", " ", el.get_text(" ", strip=True))


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------

def extract_portfolio_content(html_path: str) -> dict:
    with open(html_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    footer = soup.find("footer")

    def footer_href(substring):
        if footer:
            a = footer.find("a", href=lambda h: h and substring in h)
            return a["href"] if a else ""
        return ""

    name_el = soup.find("h1", class_="hero-name")
    name = name_el.get_text(" ", strip=True) if name_el else "Ricky Faure"

    title_el = soup.find("title")
    title = ""
    if title_el:
        raw = title_el.get_text(strip=True)
        # "Ricky Faure — Principal Software Engineer" -> take part after em dash
        if "—" in raw:
            title = raw.split("—", 1)[1].strip()

    bio_el = soup.find(class_="hero-bio")
    bio = bio_el.get_text(strip=True) if bio_el else ""

    email_href = footer_href("mailto:")
    email = email_href.replace("mailto:", "") if email_href else ""
    linkedin = footer_href("linkedin.com")
    github = footer_href("github.com")

    contact = {
        "name": name,
        "title": title,
        "email": email,
        "linkedin": linkedin,
        "github": github,
        "bio": bio,
    }

    # Skills — .chip.hi are primary, plain .chip are secondary
    primary_skills = [
        el.get_text(strip=True)
        for el in soup.find_all("span", class_="chip")
        if "hi" in el.get("class", [])
    ]
    secondary_skills = [
        el.get_text(strip=True)
        for el in soup.find_all("span", class_="chip")
        if "hi" not in el.get("class", [])
    ]

    experience = []
    for item in soup.find_all(class_="tl-item"):
        exp = {
            "date": clean_text(item.find(class_="tl-date")),
            "company": clean_text(item.find(class_="tl-company")),
            "role": clean_text(item.find(class_="tl-role")),
            "desc": clean_text(item.find(class_="tl-desc")),
            "achievements": [clean_text(a) for a in item.find_all(class_="ach")],
            "tech": [clean_text(c) for c in item.find_all(class_="tl-chip")],
        }
        experience.append(exp)

    projects = []
    for card in soup.find_all(class_="proj-card"):
        link_el = card.find(class_="proj-link")
        proj = {
            "name": clean_text(card.find(class_="proj-name")),
            "desc": clean_text(card.find(class_="proj-desc")),
            "tags": [clean_text(tg) for tg in card.find_all(class_="ptag")],
            "link": link_el["href"] if link_el and link_el.get("href") else "",
        }
        projects.append(proj)

    return {
        "contact": contact,
        "primary_skills": primary_skills,
        "secondary_skills": secondary_skills,
        "experience": experience,
        "projects": projects,
    }


# ---------------------------------------------------------------------------
# HTML resume builder
# ---------------------------------------------------------------------------

def _e(text: str) -> str:
    """HTML-escape a string."""
    return html_lib.escape(str(text))


def build_resume_html(content: dict) -> str:
    c = content["contact"]

    # ---- contact header ----
    contact_parts = []
    if c["email"]:
        contact_parts.append(f'<a href="mailto:{_e(c["email"])}">{_e(c["email"])}</a>')
    if c["linkedin"]:
        contact_parts.append(f'<a href="{_e(c["linkedin"])}">{_e(c["linkedin"])}</a>')
    if c["github"]:
        contact_parts.append(f'<a href="{_e(c["github"])}">{_e(c["github"])}</a>')
    contact_line = " &nbsp;|&nbsp; ".join(contact_parts)

    # ---- skills ----
    def skill_tags(skills):
        return "".join(f'<span class="skill-tag">{_e(s)}</span>' for s in skills)

    skills_html = ""
    if content["primary_skills"]:
        skills_html += f'<div class="skill-group"><span class="skill-label">Core:</span> {skill_tags(content["primary_skills"])}</div>'
    if content["secondary_skills"]:
        skills_html += f'<div class="skill-group"><span class="skill-label">Additional:</span> {skill_tags(content["secondary_skills"])}</div>'

    # ---- experience ----
    exp_html = ""
    for exp in content["experience"]:
        bullets = ""
        for ach in exp["achievements"]:
            bullets += f"<li>{_e(ach)}</li>"
        bullets_block = f"<ul>{bullets}</ul>" if bullets else ""

        tech_block = ""
        if exp["tech"]:
            tech_block = f'<p class="tech-line"><strong>Technologies:</strong> {_e(", ".join(exp["tech"]))}</p>'

        exp_html += f"""
        <div class="entry">
          <div class="entry-header">
            <span class="entry-org">{_e(exp["company"])}</span>
            <span class="entry-date">{_e(exp["date"])}</span>
          </div>
          <p class="entry-role">{_e(exp["role"])}</p>
          <p class="entry-desc">{_e(exp["desc"])}</p>
          {bullets_block}
          {tech_block}
        </div>"""

    # ---- projects ----
    proj_html = ""
    for proj in content["projects"]:
        name_part = _e(proj["name"])
        if proj["link"] and not proj["link"].endswith(".pdf"):
            name_part = f'<a href="{_e(proj["link"])}">{_e(proj["name"])}</a>'

        tags_part = ""
        if proj["tags"]:
            tags_part = f'<span class="proj-tags">{_e(" · ".join(proj["tags"]))}</span>'

        proj_html += f"""
        <div class="entry">
          <div class="entry-header">
            <span class="entry-org">{name_part}</span>
            {tags_part}
          </div>
          <p class="entry-desc">{_e(proj["desc"])}</p>
        </div>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{_e(c["name"])} — Resume</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    font-family: Arial, Helvetica, sans-serif;
    font-size: 10pt;
    color: #111;
    background: #fff;
    max-width: 7.5in;
    margin: 0 auto;
    padding: 0.75in 0.75in;
    line-height: 1.45;
    overflow-wrap: break-word;
  }}
  a {{ color: #111; text-decoration: none; }}

  /* Header */
  .resume-name {{
    font-size: 22pt;
    font-weight: 700;
    margin-bottom: 2pt;
  }}
  .resume-title {{
    font-size: 11pt;
    color: #444;
    margin-bottom: 5pt;
  }}
  .resume-contact {{
    font-size: 8.5pt;
    color: #333;
    margin-bottom: 14pt;
  }}
  .resume-contact a {{ color: #333; }}

  /* Section headers */
  h2 {{
    font-size: 9pt;
    font-weight: 700;
    text-transform: uppercase;
    border-bottom: 1.5px solid #111;
    padding-bottom: 2pt;
    margin: 14pt 0 7pt;
  }}

  /* Summary */
  .summary {{ font-size: 9.5pt; color: #222; }}

  /* Skills */
  .skill-group {{ margin-bottom: 4pt; font-size: 9pt; }}
  .skill-label {{ font-weight: 700; }}
  .skill-tag {{
    display: inline-block;
    background: #f0f0f0;
    border: 1px solid #ccc;
    border-radius: 3px;
    padding: 0 4pt;
    margin: 1pt 2pt 1pt 0;
    font-size: 8pt;
  }}

  /* Experience / Projects */
  .entry {{ margin-bottom: 10pt; }}
  .entry-header {{
    display: flex;
    justify-content: space-between;
    align-items: baseline;
  }}
  .entry-org {{ font-weight: 700; font-size: 10pt; }}
  .entry-date {{ font-size: 8.5pt; color: #555; white-space: nowrap; margin-left: 8pt; }}
  .entry-role {{ font-style: italic; font-size: 9.5pt; color: #222; margin-top: 1pt; }}
  .entry-desc {{ font-size: 9pt; color: #333; margin-top: 2pt; }}
  ul {{
    margin: 4pt 0 4pt 14pt;
    padding: 0;
  }}
  li {{
    font-size: 9pt;
    color: #222;
    margin-bottom: 2pt;
  }}
  .tech-line {{ font-size: 8.5pt; color: #444; margin-top: 3pt; }}
  .proj-tags {{ font-size: 8.5pt; color: #555; white-space: nowrap; margin-left: 8pt; }}

  @media print {{
    body {{ padding: 0; }}
  }}
</style>
</head>
<body>

<p class="resume-name">{_e(c["name"])}</p>
<p class="resume-title">{_e(c["title"])}</p>
<p class="resume-contact">{contact_line}</p>

<h2>Summary</h2>
<p class="summary">{_e(c["bio"])}</p>

<h2>Skills</h2>
{skills_html}

<h2>Experience</h2>
{exp_html}

<h2>Projects</h2>
{proj_html}

</body>
</html>"""


# ---------------------------------------------------------------------------
# PDF conversion
# ---------------------------------------------------------------------------

def convert_to_pdf(html_content: str, output_path: str) -> None:
    from weasyprint import HTML
    HTML(string=html_content).write_pdf(output_path)


# ---------------------------------------------------------------------------
# Entrypoint
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    repo_root = Path(__file__).parent.parent
    portfolio_path = repo_root / "index.html"
    output_path = repo_root / "Misc" / "resume.pdf"

    print("Extracting portfolio content...")
    content = extract_portfolio_content(str(portfolio_path))

    print("Building resume HTML...")
    resume_html = build_resume_html(content)

    print("Converting to PDF...")
    convert_to_pdf(resume_html, str(output_path))

    print(f"Resume saved to {output_path}")
