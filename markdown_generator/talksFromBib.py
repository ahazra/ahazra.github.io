#!/usr/bin/env python
# coding: utf-8

# Generates _talks/*.md from Talks.bib
# Venue = note field, location = location field, type = howpublished field

from pybtex.database.input import bibtex
import os
import re

BIB_FILE = "Talks.bib"
OUT_DIR  = "../_talks"

html_escape_table = {"&": "&amp;", '"': "&quot;", "'": "&apos;"}

def html_escape(text):
    return "".join(html_escape_table.get(c, c) for c in text)

def get_field(b, key, default=""):
    val = b.get(key, default)
    return str(val).replace("{", "").replace("}", "").replace("\\", "").strip() if val else ""

parser = bibtex.Parser()
bibdata = parser.parse_file(BIB_FILE)

for bib_id in bibdata.entries:
    b = bibdata.entries[bib_id].fields

    try:
        date_str = str(b["date"])
        date_parts = date_str.split("-")
        pub_year  = date_parts[0]
        pub_month = date_parts[1] if len(date_parts) > 1 else "01"
        pub_day   = date_parts[2] if len(date_parts) > 2 else "01"
        pub_date  = f"{pub_year}-{pub_month}-{pub_day}"

        title = get_field(b, "title")
        talk_type = get_field(b, "howpublished") or get_field(b, "type") or "Talk"
        venue    = get_field(b, "note")
        location = get_field(b, "location")

        # URL slug from bib key (already unique and descriptive)
        url_slug = re.sub(r"[^a-zA-Z0-9_-]", "", bib_id)
        md_filename = f"{pub_date}-{url_slug}.md"
        permalink   = f"/talks/{pub_date}-{url_slug}"

        md  = f'---\ntitle: "{html_escape(title)}"\n'
        md += f'collection: talks\n'
        md += f'type: "{html_escape(talk_type)}"\n'
        md += f'permalink: {permalink}\n'
        if venue:
            md += f'venue: "{html_escape(venue)}"\n'
        md += f'date: {pub_date}\n'
        if location:
            md += f'location: "{html_escape(location)}"\n'
        md += '---\n'

        out_path = os.path.join(OUT_DIR, os.path.basename(md_filename))
        with open(out_path, "w") as f:
            f.write(md)
        print(f'OK  {bib_id}: "{title[:60]}{"..." if len(title) > 60 else ""}"')

    except KeyError as e:
        print(f'WARN  missing field {e} in {bib_id}')
        continue
