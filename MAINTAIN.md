# Website Maintenance Guide

This is a minimal Hugo-based academic website. No web development knowledge required!

## Quick Reference

| Task | Command |
|------|---------|
| Preview locally | `hugo server -D` |
| Build site | `hugo` |
| New blog post | `hugo new blog/my-post.md` |
| New project | `hugo new projects/my-project.md` |
| Deploy | `git add . && git commit -m "msg" && git push` |

---

## Local Development

### Prerequisites
- Hugo installed (`sudo apt install hugo`)
- Git installed

### Preview Your Site
```bash
cd /path/to/varadVaidya.github.io
hugo server -D
```
Open http://localhost:1313 in your browser. Changes auto-reload!

The `-D` flag shows draft content (posts with `draft: true`).

### Build for Production
```bash
hugo
```
This creates the `public/` folder with the static site.

---

## Creating Content

### New Blog Post
```bash
hugo new blog/my-new-post.md
```

This creates `content/blog/my-new-post.md` with:
```yaml
---
title: "My New Post"
date: 2025-01-05
description: ""
tags: []
math: false
draft: true
---

Write your post here...
```

Edit the file, then:
1. Change `draft: true` to `draft: false` when ready to publish
2. Add a description
3. Add tags if desired
4. Set `math: true` if you need equations

### New Project
```bash
hugo new projects/my-project.md
```

Edit `content/projects/my-project.md`:
```yaml
---
title: "My Project"
date: 2025-01-05
description: "Short description for the listing page"
image: "/img/project-image.png"
tags: ["robotics", "control"]
draft: true
---

## Description
...

## Links
- [GitHub](https://github.com/...)
```

### Adding Images

1. Copy your image to `static/img/`:
   ```bash
   cp my-image.png static/img/
   ```

2. Reference in markdown:
   ```markdown
   ![Description](/img/my-image.png)
   ```

That's it! No special processing needed.

### Using Math (LaTeX)

1. Add `math: true` to your front matter:
   ```yaml
   ---
   title: "My Post"
   math: true
   ---
   ```

2. Write equations:
   - Inline: `$E = mc^2$` → $E = mc^2$
   - Block:
     ```
     $$
     \int_0^\infty e^{-x^2} dx = \sqrt{\pi}
     $$
     ```

See `content/projects/math-demo.md` for more examples.

---

## Deploying Changes

### Standard Workflow
```bash
# 1. Make your changes
# 2. Preview locally
hugo server -D

# 3. When happy, commit and push
git add .
git commit -m "Add new blog post about X"
git push
```

GitHub Actions automatically builds and deploys your site!

### Check Deployment Status
Go to: https://github.com/varadVaidya/varadVaidya.github.io/actions

---

## File Structure

```
varadVaidya.github.io/
├── config.toml          # Site configuration
├── content/
│   ├── _index.md        # Homepage (About page)
│   ├── blog/
│   │   ├── _index.md    # Blog listing page
│   │   └── *.md         # Blog posts
│   ├── projects/
│   │   ├── _index.md    # Projects listing page
│   │   └── *.md         # Individual projects
│   ├── publications.md  # Publications page
│   └── cv.md            # CV page
├── static/
│   └── img/             # All images go here
├── layouts/             # HTML templates (rarely need to edit)
├── assets/css/main.css  # Styles (edit if you want to change look)
└── archetypes/          # Templates for new content
```

---

## Common Tasks

### Update Homepage/About
Edit `content/_index.md`

### Update News Items
Edit the `news` section in `content/_index.md`:
```yaml
news:
  - date: "Jan 2025"
    text: "Something exciting happened!"
  - date: "Dec 2024"
    text: "Another announcement"
```

### Add a Publication
Edit `content/publications.md` and add:
```markdown
**Paper Title**
Author1, Author2, **Your Name**, et al.
*Journal/Conference Name*, Year
[PDF](link) | [Code](link)
```

### Update CV Link
Edit `content/cv.md` and change the Google Drive link.

### Change Site Title/Description
Edit `config.toml`:
```toml
title = "Your Name"
[params]
  author = "Your Name"
  description = "Your tagline"
```

### Update Social Links
Edit `config.toml`:
```toml
[params]
  email = "your@email.com"
  github = "yourusername"
  linkedin = "your-linkedin-id"
  scholar = "your-scholar-id"
  twitter = "yourhandle"
```

### Change Navigation Menu
Edit `config.toml`:
```toml
[menu]
  [[menu.main]]
    name = "About"
    url = "/"
    weight = 1
  # Add more menu items...
```

---

## Styling

The site uses a single CSS file: `assets/css/main.css`

### Key CSS Variables (at top of file)
```css
:root {
  --color-text: #333;        /* Main text color */
  --color-link: #0066cc;     /* Link color */
  --color-bg: #fff;          /* Background */
  --max-width: 750px;        /* Content width */
}
```

Change these to adjust the overall look.

---

## Troubleshooting

### Site not updating after push?
1. Check GitHub Actions: https://github.com/varadVaidya/varadVaidya.github.io/actions
2. Wait a few minutes for deployment
3. Hard refresh browser (Ctrl+Shift+R)

### Hugo command not found?
```bash
sudo apt install hugo
```

### Math not rendering?
Make sure you have `math: true` in the front matter.

### Image not showing?
1. Check the image is in `static/img/`
2. Check the path starts with `/img/` (not `static/img/`)

### Draft posts not showing?
Use `hugo server -D` to show drafts locally. Remove `draft: true` to publish.

---

## Analytics

Google Analytics is configured. View stats at:
https://analytics.google.com

Analytics ID: `G-MZC7H112MS`

---

## Backup

Your entire site is in this git repository. To backup:
```bash
git push
```

To restore on a new machine:
```bash
git clone https://github.com/varadVaidya/varadVaidya.github.io.git
```

---

## Need Help?

- Hugo Documentation: https://gohugo.io/documentation/
- Markdown Guide: https://www.markdownguide.org/
- KaTeX Supported Functions: https://katex.org/docs/supported.html
