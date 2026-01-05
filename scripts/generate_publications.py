#!/usr/bin/env python3
"""
Generate publications.md from BibTeX file.

Usage:
    python scripts/generate_publications.py

Reads: data/papers.bib
Writes: content/publications.md
"""

import re
from pathlib import Path
from collections import defaultdict

# Configuration
YOUR_NAME = "Vaidya, Varad"  # Name as it appears in BibTeX (Last, First)
YOUR_NAME_DISPLAY = "Varad Vaidya"  # How to display your name (bolded)


def parse_bibtex(bib_content):
    """Parse BibTeX file content into list of entries."""
    entries = []

    # Match BibTeX entries: @type{key, ... }
    entry_pattern = re.compile(r"@(\w+)\s*\{\s*([^,]+)\s*,\s*(.*?)\n\s*\}", re.DOTALL)

    for match in entry_pattern.finditer(bib_content):
        entry_type = match.group(1).lower()
        entry_key = match.group(2).strip()
        fields_str = match.group(3)

        # Parse individual fields
        fields = {"type": entry_type, "key": entry_key}

        # Match field = {value} or field = "value"
        field_pattern = re.compile(
            r"(\w+)\s*=\s*[{\"](.+?)[}\"](?:\s*,|\s*$)", re.DOTALL
        )

        for field_match in field_pattern.finditer(fields_str):
            field_name = field_match.group(1).lower()
            field_value = field_match.group(2).strip()
            # Clean up whitespace
            field_value = " ".join(field_value.split())
            fields[field_name] = field_value

        entries.append(fields)

    return entries


def format_authors(author_str):
    """Format author string, bolding your name."""
    # Split by 'and'
    authors = [a.strip() for a in author_str.split(" and ")]

    formatted = []
    for author in authors:
        # Handle "Last, First" format
        if "," in author:
            parts = author.split(",")
            last = parts[0].strip()
            first = parts[1].strip() if len(parts) > 1 else ""
            display_name = f"{first} {last}".strip()
        else:
            display_name = author

        # Check if this is your name (case-insensitive)
        if (
            YOUR_NAME.lower() in author.lower()
            or YOUR_NAME_DISPLAY.lower() in display_name.lower()
        ):
            formatted.append(f"<strong>{display_name}</strong>")
        elif author.lower() == "others":
            formatted.append("et al.")
        else:
            formatted.append(display_name)

    return ", ".join(formatted)


def format_entry_html(entry):
    """Format a single BibTeX entry as HTML card."""
    title = entry.get("title", "Untitled")
    authors = format_authors(entry.get("author", ""))
    year = entry.get("year", "")

    # Determine venue
    venue = entry.get("journal") or entry.get("booktitle") or ""

    # Build HTML
    html = ['<div class="pub-card">']
    html.append(f'  <div class="pub-title">{title}</div>')
    html.append(f'  <div class="pub-authors">{authors}</div>')

    if venue:
        html.append(f'  <div class="pub-venue">{venue}, {year}</div>')

    # Add note if present
    if "note" in entry:
        html.append(f'  <div class="pub-note">{entry["note"]}</div>')

    # Add links if present
    links = []
    if "url" in entry:
        links.append(f'<a href="{entry["url"]}">📄 Paper</a>')
    if "doi" in entry:
        links.append(f'<a href="https://doi.org/{entry["doi"]}">🔗 DOI</a>')
    if "arxiv" in entry:
        links.append(f'<a href="https://arxiv.org/abs/{entry["arxiv"]}">📚 arXiv</a>')
    if "code" in entry:
        links.append(f'<a href="{entry["code"]}">💻 Code</a>')
    if "video" in entry:
        links.append(f'<a href="{entry["video"]}">🎬 Video</a>')
    if "pdf" in entry:
        links.append(f'<a href="{entry["pdf"]}">📄 PDF</a>')

    if links:
        html.append(f'  <div class="pub-links">{" ".join(links)}</div>')

    html.append("</div>")

    return "\n".join(html)


def generate_publications_md(entries):
    """Generate full publications.md content."""
    # Group entries by year
    by_year = defaultdict(list)
    for entry in entries:
        year = entry.get("year", "Unknown")
        by_year[year].append(entry)

    # Sort years descending
    sorted_years = sorted(by_year.keys(), reverse=True)

    # Build markdown with HTML
    lines = [
        "---",
        'title: "Publications"',
        'description: "Academic publications and research papers"',
        "---",
        "",
        "<!-- This file is auto-generated from data/papers.bib -->",
        "<!-- Run: python scripts/generate_publications.py -->",
        "",
        '<div class="publications-page">',
        "",
    ]

    for year in sorted_years:
        lines.append(f'<div class="pub-year">{year}</div>')
        lines.append("")

        for entry in by_year[year]:
            lines.append(format_entry_html(entry))
            lines.append("")

    lines.append("</div>")

    return "\n".join(lines)


def main():
    # Get paths relative to script location
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent

    bib_path = repo_root / "data" / "papers.bib"
    output_path = repo_root / "content" / "publications.md"

    # Read BibTeX
    if not bib_path.exists():
        print(f"Error: {bib_path} not found")
        return 1

    print(f"Reading: {bib_path}")
    bib_content = bib_path.read_text()

    # Parse entries
    entries = parse_bibtex(bib_content)
    print(f"Found {len(entries)} publication(s)")

    # Generate markdown
    md_content = generate_publications_md(entries)

    # Write output
    output_path.write_text(md_content)
    print(f"Generated: {output_path}")

    return 0


if __name__ == "__main__":
    exit(main())
