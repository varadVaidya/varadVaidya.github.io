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
│   ├── publications.md
│   └── cv.md
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

## Commands

```bash
hugo server -D    # Local preview (with drafts)
hugo              # Build
hugo new blog/my-post.md      # New blog post
hugo new projects/my-proj.md  # New project
```

---

# PENDING TASK: BibTeX Integration

## Goal

Add automatic publication list generation from BibTeX file.

## Current State

Publications are manually listed in `content/publications.md`:

```markdown
## 2025
**"Dynamics-Invariant Quadrotor Control"**
**Varad Vaidya**, et al. (Accepted to *IROS 2025*)...

## 2021
**Sahayak-An Autonomous COVID Aid Bot**
Karthik Raman, ... **Varad Vaidya**, ...
```

## Old BibTeX Location

The old site had BibTeX at `_bibliography/papers.bib` (now deleted). Sample entry:

```bibtex
@article{raman2021sahayak,
  abbr    = {ISMR},
  title   = {Sahayak-An Autonomous COVID Aid Bot},
  author  = {Raman, Karthik and Ringe, Prathamesh and Subhedar, Sania and Shah, Sushlok and Vaidya, Varad and Devada, Yagnesh and Fadia, Aayush and Srivastava, Kushagra and  Zade, Harshad and Kamat, Ajinkya and others},
  journal = {International Symposium of Medical Robotics},
  year    = {2021}
}
```

## Suggested Approach

### Option A: Hugo Module (Recommended if Hugo version supports)
Use a Hugo module like `hugo-cite` for BibTeX parsing.

### Option B: Simple Python Script
Create a script that:
1. Reads `data/papers.bib`
2. Generates `content/publications.md` from it
3. Run manually when bibliography updates

### Option C: Data Files + Template
1. Convert BibTeX to YAML/JSON in `data/publications.yaml`
2. Create a template that reads from data file

## Requirements

- User wants BibTeX support but not critical priority
- Keep it simple - user doesn't want to learn web dev
- Should work with Hugo v0.92.2 (apt version on Ubuntu)

## Notes

- Hugo v0.92.2 is older, some newer features may not work
- User prefers simple solutions over complex ones
- The `passthrough` config for math delimiters may not work in v0.92 (it's a newer feature), but KaTeX client-side rendering works fine
