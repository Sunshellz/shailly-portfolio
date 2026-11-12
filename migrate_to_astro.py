# -*- coding: utf-8 -*-
"""One-time migration: build/run.py page registry -> Astro page components.

Reads the PAGES list (path, title, description, body, og_type, og_title, extra)
plus REDIRECT from the legacy build system and writes equivalent .astro files
under src/pages/. Content is passed through verbatim; only the props that end
up in <title>/<meta> are entity-unescaped (Astro re-escapes them on render).
"""
import html
import json
import os
import re
import sys

SRC = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(SRC, "build"))

import run  # noqa: E402  (module-level only; main() is never called)

PAGES_DIR = os.path.join(SRC, "src", "pages")
SCHEMA_RE = re.compile(r"<script type=\"application/ld\+json\">(.*?)</script>", re.S)


def write_astro(rel_page_dir, frontmatter, template):
    page_dir = os.path.join(PAGES_DIR, rel_page_dir) if rel_page_dir else PAGES_DIR
    os.makedirs(page_dir, exist_ok=True)
    out = os.path.join(page_dir, "index.astro")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(frontmatter + "\n\n" + template)
    print("wrote", os.path.relpath(out, SRC))


for path, title, desc, body, ogtype, ogtitle, extra in run.PAGES:
    route = path[: -len("index.html")].rstrip("/")  # "about/index.html" -> "about"
    depth = 1 if not route else route.count("/") + 2
    layout_import = "../" * depth + "layouts/Layout.astro"
    canonical_path = "/" if not route else "/" + route + "/"

    lines = ["import Layout from '%s';" % layout_import]
    if extra:
        schema = SCHEMA_RE.search(extra).group(1)
        lines.append("const headSchema = %s;" % json.dumps(schema))
    lines.append("---")
    frontmatter = "---\n" + "\n".join(lines)

    props = [
        "title=%s" % json.dumps(html.unescape(title)),
        "description=%s" % json.dumps(html.unescape(desc)),
        "path=%s" % json.dumps(canonical_path),
    ]
    if ogtype != "website":
        props.append('ogType="%s"' % ogtype)
    if ogtitle and ogtitle != title:
        props.append("ogTitle=%s" % json.dumps(html.unescape(ogtitle)))
    if extra:
        props.append("headSchema={headSchema}")

    body_text = body.strip("\n")
    if not body_text.endswith("\n"):
        body_text += "\n"
    template = "<Layout %s>\n%s</Layout>\n" % (" ".join(props), body_text)

    write_astro(route, frontmatter, template)

# The legacy redirect stub is a full standalone document (no site chrome).
redirect_dir = os.path.join(PAGES_DIR, "work", "educational-webinar-delhi-university")
os.makedirs(redirect_dir, exist_ok=True)
with open(os.path.join(redirect_dir, "index.astro"), "w", encoding="utf-8") as fh:
    fh.write("---\n---\n\n" + run.REDIRECT)
print("wrote redirect page")
