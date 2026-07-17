# Resume Docs

Source material and per-application tailoring, separate from the live site.

**Everything in `masters/`, `prospectives/`, and `submitted/` is gitignored except the `TEMPLATE`/`.template` files.** This content is personal, often names specific employers, and would otherwise get published by the Pages deploy (`.github/workflows/generate-resume.yml` uploads the whole repo). Only you have the real files; the repo tracks the shape via the templates below.

- **`masters/ats.template.md`** (tracked) — copy to `masters/ats.md` (gitignored) and fill in: every skill, role, achievement, and project, written for tailoring rather than for the webpage. `index.html` (and the resume it generates via `scripts/generate_resume.py`) stays the terse, site-facing version; `ats.md` is the deeper well tailored resumes and cover letters draw from. Keep it current as new achievements happen, and expand it before trimming a tailored copy down.
- **`prospectives/TEMPLATE.md`** (tracked) — draft tailored resumes for roles being considered live as `prospectives/<company>.md` (gitignored), one flat file per company (e.g. `prospectives/acme.md`, no subdirectories).
- **`submitted/TEMPLATE.md`** (tracked) — the resume actually sent for a given application, `submitted/<company>.md` (gitignored). Add `submitted/<company>-cover-letter.md` alongside it if a cover letter was also sent. Keep these around as a local record of what was sent where.

## Workflow

1. Get a job description.
2. Assess fit against `masters/ats.md` first: strong matches, honest gaps, overall take. Surface this before generating anything.
3. Draft a tailored resume in `prospectives/<company>.md`, trimmed and reordered to the role — don't invent employers, dates, metrics, or tools that aren't in `masters/ats.md`.
4. Render it to PDF locally: `pip install -r scripts/requirements.txt` once, then `python scripts/generate_tailored_resume.py docs/prospectives/<company>.md`. Output lands in `docs/pdf/<company>.pdf` (gitignored — local/manual only, not committed or built in CI).
5. Once actually submitted, move/copy the markdown into `submitted/<company>.md`.

Tailored markdown follows the same shape as `masters/ats.md`: `# Name`, a plain contact line, `##` section headers, `###` entry titles, bullet lists for achievements. `scripts/generate_tailored_resume.py` styles by tag (h1/h2/h3/ul/p), not by scraping specific classes, so any file following that shape renders correctly.

This is separate from `scripts/generate_resume.py`, which only renders the canonical resume from `index.html` and is wired into CI to keep `Misc/resume.pdf` in sync with the live site on every push.
