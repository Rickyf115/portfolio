#!/usr/bin/env python3
"""Generate a job-application-friendly resume PDF from portfolio HTML content."""

import os
import re
import sys
from pathlib import Path

import anthropic
from bs4 import BeautifulSoup


def extract_portfolio_content(html_path: str) -> dict:
    with open(html_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    contact = {
        "name": "Ricky Faure",
        "title": "Principal Software Engineer",
        "email": "rickyf115@pm.me",
        "linkedin": "https://www.linkedin.com/in/ricardo-faure-805175128/",
        "github": "https://github.com/Rickyf115",
    }

    bio_el = soup.find(class_="hero-bio")
    contact["bio"] = bio_el.get_text(strip=True) if bio_el else ""

    skills = [chip.get_text(strip=True) for chip in soup.find_all(class_="chip")]

    experience = []
    for item in soup.find_all(class_="tl-item"):

        def text(cls, parent=item):
            el = parent.find(class_=cls)
            return el.get_text(strip=True) if el else ""

        exp = {
            "date": text("tl-date"),
            "company": text("tl-company"),
            "role": text("tl-role"),
            "desc": text("tl-desc"),
            "achievements": [a.get_text(strip=True) for a in item.find_all(class_="ach")],
            "tech": [t.get_text(strip=True) for t in item.find_all(class_="tl-chip")],
        }
        experience.append(exp)

    projects = []
    for card in soup.find_all(class_="proj-card"):

        def text(cls, parent=card):
            el = parent.find(class_=cls)
            return el.get_text(strip=True) if el else ""

        proj = {
            "name": text("proj-name"),
            "desc": text("proj-desc"),
            "tags": [t.get_text(strip=True) for t in card.find_all(class_="ptag")],
        }
        projects.append(proj)

    return {
        "contact": contact,
        "skills": skills,
        "experience": experience,
        "projects": projects,
    }


def build_prompt(content: dict) -> str:
    c = content["contact"]
    lines = [
        f"Name: {c['name']}",
        f"Title: {c['title']}",
        f"Email: {c['email']}",
        f"LinkedIn: {c['linkedin']}",
        f"GitHub: {c['github']}",
        f"Bio: {c['bio']}",
        "",
        "TECHNICAL SKILLS:",
        ", ".join(content["skills"]),
        "",
        "WORK EXPERIENCE:",
    ]

    for exp in content["experience"]:
        lines += [
            f"\nCompany: {exp['company']}",
            f"Role: {exp['role']}",
            f"Period: {exp['date']}",
            f"Description: {exp['desc']}",
        ]
        if exp["achievements"]:
            lines.append("Key Achievements:")
            for ach in exp["achievements"]:
                lines.append(f"  - {ach}")
        if exp["tech"]:
            lines.append(f"Technologies: {', '.join(exp['tech'])}")

    lines += ["", "PROJECTS:"]
    for proj in content["projects"]:
        lines += [
            f"\nProject: {proj['name']}",
            f"Description: {proj['desc']}",
            f"Technologies: {', '.join(proj['tags'])}",
        ]

    return "\n".join(lines)


def generate_resume_html(portfolio_content: dict) -> str:
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    prompt_data = build_prompt(portfolio_content)

    message = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=4096,
        messages=[
            {
                "role": "user",
                "content": (
                    "You are an expert resume writer. Using the portfolio content below, "
                    "create a clean, ATS-friendly, job-application-ready resume in HTML format.\n\n"
                    "Requirements:\n"
                    "- Professional single-column layout optimized for PDF printing (A4/Letter)\n"
                    "- White background (#ffffff), dark text (#111111) — print-friendly\n"
                    "- Embedded CSS only — no external stylesheets, no web fonts\n"
                    "- System sans-serif font stack: Arial, Helvetica, sans-serif\n"
                    "- Sections in order: Contact Info, Summary, Skills, Experience, Projects\n"
                    "- Skills grouped into 3 categories: Cloud & Infrastructure, Languages & Frameworks, Tools & Practices\n"
                    "- Experience bullets are concise, impact-focused, and include quantified metrics where available\n"
                    "- Page margins: 1in; max-width: 7.5in; font-size: 10pt\n"
                    "- Name as large header, section headers as bold uppercase with a rule line\n"
                    "- Return ONLY the complete HTML document starting with <!DOCTYPE html>. No markdown, no code fences, no commentary.\n\n"
                    f"PORTFOLIO CONTENT:\n{prompt_data}"
                ),
            }
        ],
    )

    html = message.content[0].text.strip()
    # Strip any accidental markdown code fences
    html = re.sub(r"^```[a-z]*\n?", "", html)
    html = re.sub(r"\n?```$", "", html)
    return html


def convert_to_pdf(html_content: str, output_path: str) -> None:
    from weasyprint import HTML

    HTML(string=html_content).write_pdf(output_path)


if __name__ == "__main__":
    repo_root = Path(__file__).parent.parent
    portfolio_path = repo_root / "index.html"
    output_path = repo_root / "Misc" / "resume.pdf"

    print("Extracting portfolio content...")
    content = extract_portfolio_content(str(portfolio_path))

    print("Generating resume with Claude API...")
    resume_html = generate_resume_html(content)

    print("Converting to PDF...")
    convert_to_pdf(resume_html, str(output_path))

    print(f"Resume saved to {output_path}")
