# Website Rebuild Context

## What Was Done

Rebuilt academic website from al-folio Jekyll (77MB, 17 plugins) to minimal Hugo (~3MB, 0 plugins).

## Current State

- **Branch**: `master` (force-pushed, clean Hugo site)
- **Framework**: Hugo v0.92.2 (installed via apt)
- **Config file**: `config.toml` (not hugo.toml - older Hugo version)
- **Live at**: https://varadVaidya.github.io/

## File Structure

```
varadVaidya.github.io/
├── config.toml              # Main config
├── content/
│   ├── _index.md            # Homepage (About + News)
│   ├── blog/
│   │   ├── _index.md
│   │   └── spacecraft-dynamics.md
│   ├── projects/
│   │   ├── _index.md
│   │   ├── drone-balance.md
│   │   ├── kuka-youbot.md
│   │   └── math-demo.md     # Draft - math rendering demo
│   ├── publications.md      # Auto-generated from BibTeX
│   └── cv.md
├── data/
│   └── papers.bib           # BibTeX source for publications
├── scripts/
│   └── generate_publications.py  # BibTeX → Markdown generator
├── layouts/
│   ├── _default/
│   │   ├── baseof.html
│   │   ├── home.html
│   │   ├── single.html
│   │   └── list.html
│   └── partials/
│       ├── head.html        # Has KaTeX + Google Analytics
│       ├── header.html
│       └── footer.html
├── assets/css/main.css
├── static/img/              # Images go here
├── archetypes/              # Templates for new content
├── .github/workflows/deploy.yml
└── MAINTAIN.md              # Full maintenance guide
```

## Key Features

- **Math**: KaTeX via CDN, enabled per-page with `math: true` in front matter
- **Images**: Just drop in `static/img/`, reference as `/img/filename.png`
- **Analytics**: Google Analytics `G-MZC7H112MS`
- **Deployment**: GitHub Actions on push to master
- **Publications**: Auto-generated from `data/papers.bib`

## Commands

```bash
hugo server -D    # Local preview (with drafts)
hugo              # Build
hugo new blog/my-post.md      # New blog post
hugo new projects/my-proj.md  # New project
python3 scripts/generate_publications.py  # Regenerate publications from BibTeX
```

---

# BibTeX Publications System

## How It Works

1. Add publications to `data/papers.bib`
2. Run `python3 scripts/generate_publications.py`
3. Script generates `content/publications.md` automatically

## BibTeX Format

```bibtex
@inproceedings{key2025,
  title     = {Paper Title},
  author    = {Last, First and Vaidya, Varad and others},
  booktitle = {Conference Name},
  year      = {2025},
  note      = {Optional note about acceptance, presentation, etc.},
  url       = {https://paper-link.com},
  doi       = {10.1234/doi},
  arxiv     = {2401.12345},
  code      = {https://github.com/...},
  video     = {https://youtube.com/...}
}
```

## Features

- Groups publications by year (newest first)
- Auto-bolds your name ("Varad Vaidya")
- Generates links for: url, doi, arxiv, code, video
- Supports both `@article` and `@inproceedings` types

## To Customize

Edit `scripts/generate_publications.py`:
- `YOUR_NAME`: How your name appears in BibTeX (e.g., "Vaidya, Varad")
- `YOUR_NAME_DISPLAY`: How to display your name (e.g., "Varad Vaidya")
