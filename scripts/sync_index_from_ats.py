#!/usr/bin/env python3
"""Regenerate the synced content sections of index.html from docs/masters/ats.md.

docs/masters/ats.md is the source of truth for skills, experience, and
projects. Run this after editing the master, then commit both files:

    python scripts/sync_index_from_ats.py

The rewritten regions are delimited in index.html by
"<!-- BEGIN ATS SYNC: <name> ... -->" / "<!-- END ATS SYNC: <name> -->"
comment pairs. Everything outside those regions is site-specific and left
untouched -- including the hero bio, which is a deliberately terse summary
distilled from the master's Summary section (and scraped by
generate_resume.py as the PDF summary). When the master's Summary changes
materially, refresh the hero bio by hand (or ask Claude) to match.

The generated markup keeps the classes generate_resume.py scrapes
(chip/hi, tl-item, tl-date, tl-company, tl-role, tl-desc, ach, tl-chip,
proj-card, proj-name, proj-desc, ptag, proj-link), so the resume PDF
pipeline keeps working. No third-party dependencies.
"""

import html as html_lib
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
ATS_PATH = REPO / "docs" / "masters" / "ats.md"
INDEX_PATH = REPO / "index.html"


# ---------------------------------------------------------------------------
# ats.md parsing
# ---------------------------------------------------------------------------

def strip_html_comments(text: str) -> str:
    return re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)


def md_inline_to_html(text: str) -> str:
    """Escape HTML, then convert **bold** to <b> and dashes to entities."""
    text = html_lib.escape(text, quote=False)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    return text


def split_sections(md: str) -> dict:
    """Return {section title: body} for each ## section."""
    sections = {}
    parts = re.split(r"^## ", md, flags=re.MULTILINE)
    for part in parts[1:]:
        title, _, body = part.partition("\n")
        sections[title.strip()] = body.strip()
    return sections


def split_entries(section_body: str) -> list:
    """Return [(title, body), ...] for each ### entry in a section."""
    entries = []
    parts = re.split(r"^### ", section_body, flags=re.MULTILINE)
    for part in parts[1:]:
        title, _, body = part.partition("\n")
        entries.append((title.strip(), body.strip()))
    return entries


def parse_skills(body: str) -> dict:
    skills = {"core": [], "additional": []}
    for label, key in (("Core", "core"), ("Additional", "additional")):
        m = re.search(r"\*\*%s:\*\*\s*(.+)" % label, body)
        if m:
            skills[key] = [s.strip() for s in m.group(1).split(",") if s.strip()]
    return skills


def parse_experience_entry(title: str, body: str) -> dict:
    entry = {
        "title": title,
        "company": "",
        "date": "",
        "progression": "",
        "desc": "",
        "achievements": [],  # list of (is_heading, text)
        "tech": [],
    }
    desc_lines = []
    for raw_line in body.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith("Technologies:"):
            entry["tech"] = [t.strip() for t in line[len("Technologies:"):].split(",") if t.strip()]
        elif line.startswith("- "):
            entry["achievements"].append((False, line[2:].strip()))
        elif re.fullmatch(r"\*\*Featured Project.*\*\*", line):
            entry["achievements"].append((True, line.strip("*").strip()))
        elif not entry["company"] and " | " in line:
            segments = [s.strip() for s in line.split("|")]
            entry["company"] = segments[0]
            entry["date"] = segments[-1]
        else:
            desc_lines.append(line)

    desc = " ".join(desc_lines)
    m = re.match(r"Progressed (.+?\(.*?\))\.\s*(.*)", desc)
    if m:
        entry["progression"] = m.group(1)
        desc = m.group(2)
    entry["desc"] = desc
    return entry


def parse_project_entry(title: str, body: str) -> dict:
    proj = {"name": title, "desc": "", "tags": [], "link": ""}
    desc_lines = []
    for raw_line in body.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith("Technologies:"):
            proj["tags"] = [t.strip() for t in line[len("Technologies:"):].split(",") if t.strip()]
        elif line.startswith("Link:"):
            proj["link"] = line[len("Link:"):].strip()
        else:
            desc_lines.append(line)
    proj["desc"] = " ".join(desc_lines)
    return proj


# ---------------------------------------------------------------------------
# index.html rendering
# ---------------------------------------------------------------------------

def render_skills(skills: dict) -> str:
    lines = []
    for skill in skills["core"]:
        lines.append(f'        <span class="chip hi">{md_inline_to_html(skill)}</span>')
    for skill in skills["additional"]:
        lines.append(f'        <span class="chip">{md_inline_to_html(skill)}</span>')
    return "\n".join(lines)


def render_experience(entries: list) -> str:
    items = []
    for entry in entries:
        date = md_inline_to_html(entry["date"]).upper().replace(" - ", " &mdash; ")
        role = md_inline_to_html(entry["title"])
        if entry["progression"]:
            progression = md_inline_to_html(entry["progression"]).replace(" &gt; ", " &rarr; ")
            role += f" &nbsp;&mdash;&nbsp; {progression}"

        lines = [
            '      <div class="tl-item">',
            '        <div class="tl-dot"></div>',
            f'        <p class="tl-date">{date}</p>',
            f'        <h3 class="tl-company">{md_inline_to_html(entry["company"])}</h3>',
            f'        <p class="tl-role">{role}</p>',
        ]
        if entry["desc"]:
            lines.append(f'        <p class="tl-desc">{md_inline_to_html(entry["desc"])}</p>')
        if entry["achievements"]:
            lines.append('        <div class="achievements">')
            for is_heading, text in entry["achievements"]:
                rendered = md_inline_to_html(text)
                if is_heading:
                    rendered = f"<b>{rendered}</b>"
                lines.append(f'          <div class="ach"><span>{rendered}</span></div>')
            lines.append('        </div>')
        if entry["tech"]:
            lines.append('        <div class="tl-chips">')
            for tech in entry["tech"]:
                lines.append(f'          <span class="tl-chip">{md_inline_to_html(tech)}</span>')
            lines.append('        </div>')
        lines.append('      </div>')
        items.append("\n".join(lines))
    return "\n\n".join(items)


def link_label(link: str) -> str:
    if "github.com" in link:
        return "GitHub &rarr;"
    if link.endswith(".pdf"):
        return "Project Plan &rarr;"
    return "Link &rarr;"


def render_projects(projects: list) -> str:
    cards = []
    for i, proj in enumerate(projects, start=1):
        lines = [
            '      <article class="proj-card">',
            f'        <p class="proj-num">{i:02d}</p>',
            f'        <h3 class="proj-name">{md_inline_to_html(proj["name"])}</h3>',
            f'        <p class="proj-desc">{md_inline_to_html(proj["desc"])}</p>',
        ]
        if proj["tags"]:
            lines.append('        <div class="proj-tags">')
            for tag in proj["tags"]:
                lines.append(f'          <span class="ptag">{md_inline_to_html(tag)}</span>')
            lines.append('        </div>')
        if proj["link"]:
            href = html_lib.escape(proj["link"], quote=True)
            lines.append(
                f'        <a href="{href}" target="_blank" rel="noopener" class="proj-link">{link_label(proj["link"])}</a>'
            )
        lines.append('      </article>')
        cards.append("\n".join(lines))
    return "\n\n".join(cards)


def replace_region(html: str, name: str, inner: str, closing_indent: str) -> str:
    pattern = re.compile(
        r"(<!-- BEGIN ATS SYNC: %s[^>]*-->)\n.*?(<!-- END ATS SYNC: %s -->)" % (re.escape(name), re.escape(name)),
        re.DOTALL,
    )
    if not pattern.search(html):
        sys.exit(f"error: ATS SYNC markers for '{name}' not found in index.html")
    return pattern.sub(lambda m: f"{m.group(1)}\n{inner}\n{closing_indent}{m.group(2)}", html, count=1)


# ---------------------------------------------------------------------------
# Entrypoint
# ---------------------------------------------------------------------------

def main() -> None:
    md = strip_html_comments(ATS_PATH.read_text(encoding="utf-8"))
    sections = split_sections(md)
    for required in ("Skills", "Experience", "Projects"):
        if required not in sections:
            sys.exit(f"error: '## {required}' section not found in {ATS_PATH}")

    skills = parse_skills(sections["Skills"])
    experience = [parse_experience_entry(t, b) for t, b in split_entries(sections["Experience"])]
    projects = [parse_project_entry(t, b) for t, b in split_entries(sections["Projects"])]

    html = INDEX_PATH.read_text(encoding="utf-8")
    html = replace_region(html, "skills", render_skills(skills), "        ")
    html = replace_region(html, "experience", render_experience(experience), "      ")
    html = replace_region(html, "projects", render_projects(projects), "      ")
    INDEX_PATH.write_text(html, encoding="utf-8")

    print(f"index.html synced from {ATS_PATH.relative_to(REPO)}:")
    print(f"  skills: {len(skills['core'])} core + {len(skills['additional'])} additional")
    print(f"  experience entries: {len(experience)}")
    print(f"  projects: {len(projects)}")


if __name__ == "__main__":
    main()
