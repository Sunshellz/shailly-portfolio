# -*- coding: utf-8 -*-
"""Build the portfolio pages."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from chrome import page, BASE
import content_core as core
import content_cases as cases
import content_samples as samples

HOME_SCHEMA = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Shailly",
  "jobTitle": "Operations & Program Management",
  "description": "Operations and program management professional working across program coordination, process improvement, recruitment, onboarding, and educational initiatives.",
  "email": "mailto:i.am.shailly@gmail.com",
  "telephone": "+917300711147",
  "sameAs": ["https://www.linkedin.com/in/shailly-presently"],
  "alumniOf": ["Panjab University, Chandigarh", "CHRIST University, Bengaluru"]
}
</script>"""

PAGES = [
    ("index.html",
     "Shailly — Operations &amp; Program Management",
     "Shailly is an operations and program management professional turning ideas, moving parts, and messy processes into organised, executable work. Projects, work samples, and experience.",
     core.HOME, "website", None, HOME_SCHEMA),
    ("about/index.html",
     "About — Shailly | Operations, Program Management &amp; Process Improvement",
     "How Shailly works: structure from ambiguity, people and coordination, practical systems, and ownership. Background across content, education, program operations, and recruitment.",
     core.ABOUT, "website", None, ""),
    ("experience/index.html",
     "Experience — Shailly | Operations, Program Management &amp; Content",
     "Full experience: Academic Counselor at Vedantu; Program Operations Coordinator, Head of Content, and Social Media Manager at The Period Society Rajasthan; content, copywriting, and business development roles; education.",
     core.EXPERIENCE, "website", None, ""),
    ("work/index.html",
     "Selected Work — Shailly | Projects, Work Samples &amp; Documents",
     "Four implemented projects, two independent work samples, and two organisational documents — recruitment workflow redesign, Instagram Live series, menstrual health initiatives, Kraftshala analytics, and U&I program design.",
     core.WORK_INDEX, "website", None, ""),
    ("work/recruitment-onboarding-workflow/index.html",
     "Recruitment &amp; Onboarding Workflow Redesign — Shailly",
     "Case study: rebuilding volunteer recruitment at The Period Society Rajasthan — one role-based application form, central candidate tracking, standardised communication, and tracked onboarding. Interview scheduling moved from several weeks to under seven days.",
     cases.CASE01, "article", "Recruitment &amp; Onboarding Workflow Redesign — Shailly", ""),
    ("work/instagram-live-series/index.html",
     "Instagram Live Series — Shailly | Case Study",
     "Case study: conceiving and running a recurring Instagram Live series at The Period Society Rajasthan — 10+ sessions, 15+ speakers prepared, and a format volunteers could host.",
     cases.CASE02, "article", "Instagram Live Series — Shailly", ""),
    ("work/ending-the-period-stigma/index.html",
     "Ending the Period Stigma — Shailly | Case Study",
     "Case study: a research-based menstrual health awareness initiative at CHRIST University, Bengaluru, adapted from school and NGO outreach into a collaborative campus exhibition engaging 70+ students.",
     cases.CASE03, "article", "Ending the Period Stigma — Shailly", ""),
    ("work/menstrual-health-webinar/index.html",
     "Menstrual Health Webinar — Shailly | Case Study",
     "Case study: the content, speaker preparation, and coordination behind a menstrual health webinar with Rotaract Club of Dyal Singh College and Project Aaina — six roles, approximately 50 attendees.",
     cases.CASE04, "article", "Menstrual Health Webinar — Shailly", ""),
    ("work/samples/kraftshala-assignment/index.html",
     "Student Experience &amp; Operational Analytics — Shailly | Work Sample",
     "Kraftshala Program Management work sample: a four-scenario student support framework and operational analytics across cancellations, session delays, batch performance, and expert reliability.",
     samples.SAMPLE01, "article", "Student Experience &amp; Operational Analytics — Shailly", ""),
    ("work/samples/ui-fellowship-presentation/index.html",
     "U&amp;I Fellowship — Program Design &amp; Recruitment Operations — Shailly",
     "Independent work sample: a fellowship recruitment and operating model covering a venue partnership proposal, leadership structure, recruitment operating system, coordination framework, and timelines.",
     samples.SAMPLE02, "article", "U&I Fellowship — Program Design &amp; Recruitment Operations — Shailly", ""),
    ("work/samples/volunteer-agreement/index.html",
     "Volunteer Agreement — Shailly | Organisational Documentation",
     "A sample organisational document formalising volunteer expectations, responsibilities, supervision, confidentiality, and terms of engagement. Redacted excerpts.",
     samples.DOC01, "article", "Volunteer Agreement — Shailly", ""),
    ("work/samples/memorandum-of-agreement/index.html",
     "Memorandum of Agreement — Shailly | Organisational Documentation",
     "A sample collaboration document covering scope, responsibilities, terms, funding arrangements, and formal agreement between parties. Redacted excerpts.",
     samples.DOC02, "article", "Memorandum of Agreement — Shailly", ""),
    ("skills/index.html",
     "Skills &amp; Certifications — Shailly | Operations &amp; Program Management",
     "Skills across project and program operations, process improvement and systems, communication and coordination, research and content, and tools — with Google, Asana, Moodle, and NIELIT certifications.",
     core.SKILLS, "website", None, ""),
    ("contact/index.html",
     "Contact — Shailly | Operations &amp; Program Management",
     "Contact Shailly for operations, program management, and coordination opportunities. Email, phone, and LinkedIn.",
     core.CONTACT, "website", None, ""),
]

SITEMAP_URLS = [
    ("/", "1.0", "monthly"),
    ("/about/", "0.8", "monthly"),
    ("/experience/", "0.9", "monthly"),
    ("/work/", "0.9", "monthly"),
    ("/work/recruitment-onboarding-workflow/", "1.0", "monthly"),
    ("/work/instagram-live-series/", "0.8", "yearly"),
    ("/work/ending-the-period-stigma/", "0.8", "yearly"),
    ("/work/menstrual-health-webinar/", "0.8", "yearly"),
    ("/work/samples/kraftshala-assignment/", "0.9", "monthly"),
    ("/work/samples/ui-fellowship-presentation/", "0.8", "yearly"),
    ("/work/samples/volunteer-agreement/", "0.6", "yearly"),
    ("/work/samples/memorandum-of-agreement/", "0.6", "yearly"),
    ("/skills/", "0.8", "monthly"),
    ("/contact/", "0.8", "yearly"),
]

REDIRECT = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="robots" content="noindex, follow">
<title>Moved — Menstrual Health Webinar — Shailly</title>
<meta name="description" content="This case study has moved to the Menstrual Health Webinar page on Shailly's portfolio.">
<link rel="canonical" href="BASE/work/menstrual-health-webinar/">
<meta http-equiv="refresh" content="0; url=/work/menstrual-health-webinar/">
</head>
<body>
<p>This case study has moved to <a href="/work/menstrual-health-webinar/">Menstrual Health Webinar</a>.</p>
</body>
</html>
""".replace("BASE", BASE)


def main():
    for path, title, desc, body, ogtype, ogtitle, extra in PAGES:
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
        page(path, title, desc, body, og_type=ogtype, og_title=ogtitle, extra_head=extra)
        print("wrote", path)

    with open("work/educational-webinar-delhi-university/index.html", "w", encoding="utf-8") as fh:
        fh.write(REDIRECT)
    print("wrote redirect")

    rows = []
    for url, pr, freq in SITEMAP_URLS:
        rows.append(
            "  <url>\n    <loc>%s%s</loc>\n    <lastmod>2026-11-11</lastmod>\n"
            "    <changefreq>%s</changefreq>\n    <priority>%s</priority>\n  </url>"
            % (BASE, url, freq, pr)
        )
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(rows)
        + "\n</urlset>\n"
    )
    with open("sitemap.xml", "w", encoding="utf-8") as fh:
        fh.write(xml)
    print("wrote sitemap.xml")


if __name__ == "__main__":
    main()
