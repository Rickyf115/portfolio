# CLAUDE.md

Guidance for Claude Code (and Copilot) when generating or editing resume and cover letter content in this repo. See `docs/README.md` for the directory layout.

## Personal Context

The real source of truth is **`docs/masters/ats.md`** — tracked in git (unlike the tailored copies in `docs/prospectives/` and `docs/submitted/`, which stay gitignored). It holds every skill, role, achievement, and project, written for tailoring rather than for the webpage (`index.html` is the terse, site-facing version). If it doesn't exist yet, copy it from `docs/masters/ats.template.md` and have the user fill it in — don't fabricate its contents.

Read `docs/masters/ats.md` before generating any tailored resume or cover letter.

The summary (rendered as the hero bio), skills, experience, and projects sections of `index.html` are generated from `ats.md`: after editing the master, run `python scripts/sync_index_from_ats.py` and commit both files. Never hand-edit the `ATS SYNC` marked regions of `index.html` — the next sync overwrites them. Content outside those markers (hero name/title, education-free layout) is site-specific and edited directly.

## Workflow

1. Get a job description.
2. Assess fit against `docs/masters/ats.md` before writing anything: strong matches, honest gaps, overall take (strong / reasonable / stretch fit). Present this to the user first.
3. Draft the tailored resume in `docs/prospectives/<company>.md`.
4. If a cover letter is wanted, draft `docs/prospectives/<company>-cover-letter.md` alongside it.
5. Render to PDF: `python scripts/generate_tailored_resume.py docs/prospectives/<company>.md` (`pip install -r scripts/requirements.txt` once, first). Iterate until the resume is a single page.
6. On actual submission, move/copy both files into `docs/submitted/` under the same names.

## Avoid Fabrication

- Never invent employers, dates, metrics, tools, certifications, or outcomes.
- If a requested change needs a fact that isn't in `docs/masters/ats.md`, ask for it instead of guessing.
- Keep quantified claims (percentages, dollar amounts, team sizes) exactly as stated in the master unless the user gives you an update.

## Formatting Rules

### General
- Plain ASCII punctuation. No em dashes or en dashes.
- Preserve established wording and quantified claims unless asked to change them.
- Keep edits minimal and scoped to what's requested — don't rewrite whole sections unprompted.

### Resumes (`masters/ats.md`, `prospectives/<company>.md`, `submitted/<company>.md`)
- Heading hierarchy: `#` name, `##` section titles (Summary, Skills, Experience, Projects, Education, Certifications), `###` entry titles (job title / project name).
- Contact line: plain text directly under the name, `email | linkedin | github`, pipe-separated.
- Bullets: third-person implied (no "I"). Lead with a strong action verb.
  - Current role, present tense: Serve, Own, Lead, Build, Drive, Maintain.
  - Past roles, past tense: Led, Built, Delivered, Designed, Implemented.
- Bold is used for lead-in labels and inline metrics only in `masters/ats.md`. Tailored resumes in `prospectives/`/`submitted/` use plain text in bullets — no bold.
- Section order: Summary (optional in tailored copies, keep only if the role benefits from a holistic framing) > Skills > Experience > Projects > Education > Certifications.
- Skills format: `**Core:** skill, skill` / `**Additional:** skill, skill`. Reorder and prune per job description; front-load what the posting emphasizes.

### Cover Letters (`<company>-cover-letter.md`)
- Filename must contain `cover-letter` — `scripts/generate_tailored_resume.py` uses that to switch to letter styling instead of resume styling.
- No heading levels (`#`/`##`/`###`) at all. Structure: bold name, plain contact line, blank line, date, blank line, company name + role title, `---`, then the letter body.
- Voice: first person throughout ("I serve...", "I am writing..."). Confident and direct, not self-congratulatory — state credentials as facts with metrics, not adjectives.
- Greeting: `To [Name] at [Company],` if a hiring contact is known, otherwise `To the [Company] hiring team,`.
- Body: 3-5 short paragraphs — hook/interest, relevant credibility with a concrete metric, the most relevant specific experience for this role, then close.
- Sign-off is always:
  ```
  Thank you for your time and consideration.

  <Your Name>
  ```
- Zero links in cover letters.

## PDF Output

- `scripts/sync_index_from_ats.py` — regenerates the `ATS SYNC` regions of `index.html` from `docs/masters/ats.md`. Local/manual, no dependencies.
- `scripts/generate_resume.py` — scrapes `index.html`, renders the single canonical site-facing resume to `Misc/resume.pdf`. Runs in CI on every push to `master`.
- `scripts/generate_tailored_resume.py <path/to/file.md>` — renders any file under `docs/prospectives/` or `docs/submitted/` to `docs/pdf/<name>.pdf`. Local/manual only, not run in CI, not committed (`docs/pdf/` is gitignored).

## ATS Compatibility (Greenhouse, Workday, etc.)

Resumes generated here need to survive machine parsing, not just look good. Constraints already baked into `generate_resume.py` and `generate_tailored_resume.py` — don't undo them when touching the CSS:

- **No `letter-spacing` on headings.** Confirmed bug: `letter-spacing` combined with `text-transform: uppercase` on section headers made `pdftotext` (and by extension most ATS text extractors, which use the same glyph-position heuristics) read `EXPERIENCE` as `E XPERIENCE`, `SUMMARY` as `S UMMARY`, etc. — silently breaking exact-match section-header detection. Both scripts had this and both were fixed; never reintroduce `letter-spacing` on text that needs to stay machine-readable.
- Single column, no tables for layout or content, no headers/footers, no text boxes, no icon-only contact info (email/LinkedIn/GitHub must appear as visible text, not just an icon glyph).
- Standard section header words only: Summary, Skills, Experience, Projects, Education, Certifications.
- `overflow-wrap: break-word` is set on `body` in both scripts so long unbroken strings (URLs) don't overflow the page rather than wrap.
- **After any CSS change to either script, verify with `pdftotext -layout <output>.pdf -` (or equivalent) and check that section headers and the name extract as single unbroken words** before trusting the output.
