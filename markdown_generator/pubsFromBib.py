#!/usr/bin/env python
# coding: utf-8

from pybtex.database.input import bibtex
import pybtex.database.input.bibtex
import string
import html
import os
import re

publist = {
    "journal": {
        "file": "Journ_pub.bib",
        "keywords": "journaltitle",
        "venue-pretext": "",
        "collection": {"name": "publications", "type": "journal", "permalink": "/publication/"}
    },
    "conference": {
        "file": "MyPub.bib",
        "keywords": "booktitle",
        "venue-pretext": "In the proceedings of ",
        "collection": {"name": "publications", "type": "conference", "permalink": "/publication/"}
    },
    "thesis": {
        "file": "MyPub.bib",
        "keywords": "school",
        "venue-pretext": "",
        "collection": {"name": "publications", "type": "thesis", "permalink": "/publication/"}
    }
}

html_escape_table = {"&": "&amp;", '"': "&quot;", "'": "&apos;"}

def html_escape(text):
    return "".join(html_escape_table.get(c, c) for c in text)

def get_field(b, *keys):
    """Return first matching field value, or None."""
    for k in keys:
        if k in b and len(str(b[k]).strip()) > 0:
            return str(b[k]).strip()
    return None

for pubsource, meta in publist.items():
    if not os.path.exists(meta["file"]):
        print(f'Skipping {pubsource}: file {meta["file"]} not found')
        continue

    parser = bibtex.Parser()
    bibdata = parser.parse_file(meta["file"])

    for bib_id in bibdata.entries:
        b = bibdata.entries[bib_id].fields
        pub_day = "01"

        try:
            date_parts = str(b["date"]).split("-")
            pub_year = date_parts[0]
            pub_month = date_parts[1] if len(date_parts) > 1 else "01"
            pub_date = f"{pub_year}-{pub_month}-{pub_day}"

            clean_title = b["title"].replace("{", "").replace("}", "").replace("\\", "").replace(" ", "-")
            url_slug = re.sub(r"\[.*\]|[^a-zA-Z0-9_-]", "", clean_title).replace("--", "-")
            md_filename = f"{pub_date}-{url_slug}.md".replace("--", "-")
            html_filename = f"{pub_date}-{url_slug}".replace("--", "-")

            # Authors list
            authors = []
            for author in bibdata.entries[bib_id].persons.get("author", []):
                first = " ".join(author.first_names)
                last = " ".join(author.last_names)
                authors.append(f"{first} {last}")

            # Citation string (title shown separately, so omitted here)
            title_clean = b["title"].replace("{", "").replace("}", "").replace("\\", "")
            venue_raw = meta["venue-pretext"] + b.get(meta["keywords"], "").replace("{", "").replace("}", "").replace("\\", "")
            citation = " ".join(f"{a}," for a in authors)
            citation += f' {html_escape(venue_raw)}, {pub_year}.'

            # Optional fields
            doi    = get_field(b, "doi")
            arxiv  = get_field(b, "eprint") if get_field(b, "eprinttype", "archiveprefix") in ("arXiv", "arxiv", None) else None
            url    = get_field(b, "url")
            abstract = get_field(b, "abstract")

            ## Build YAML front matter
            md  = f'---\ntitle: "{html_escape(title_clean)}"\n'
            md += f'collection: {meta["collection"]["name"]}\n'
            md += f'type: "{meta["collection"]["type"]}"\n'
            md += f'permalink: {meta["collection"]["permalink"]}{html_filename}\n'
            md += f'date: {pub_date}\n'
            md += f'venue: \'{html_escape(venue_raw)}\'\n'

            # Authors as YAML list
            md += 'authors:\n'
            for a in authors:
                md += f'  - "{html_escape(a)}"\n'

            if doi:
                md += f'doi: "{doi}"\n'
            if arxiv:
                md += f'arxiv: "{arxiv}"\n'
            if url:
                md += f'paperurl: \'{url}\'\n'
            if abstract:
                md += f'excerpt: \'{html_escape(abstract)}\'\n'

            md += f'citation: \'{html_escape(citation)}\'\n'
            md += '---\n'

            # Page body
            if abstract:
                md += f'\n{html_escape(abstract)}\n'
            if url:
                md += f'\n[Read more]({url}){{:target="_blank"}}\n'

            out_path = os.path.join("..", "_publications", os.path.basename(md_filename))
            with open(out_path, "w") as f:
                f.write(md)
            print(f'OK  {bib_id}: "{b["title"][:60]}{"..." if len(b["title"]) > 60 else ""}"')

        except KeyError as e:
            print(f'WARN  missing field {e} in {bib_id}: "{b.get("title", "?")[:40]}"')
            continue
