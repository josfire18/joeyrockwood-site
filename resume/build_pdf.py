"""Rebuild Joseph-Rockwood-Resume.pdf from resume/resume.html.

Usage (from the repo root):  python3 resume/build_pdf.py
Needs: pip install playwright pypdf  and a Chrome/Chromium install.

Renders the print layout with headless Chrome, then rewrites the PDF's
document info so it carries only a title and author (no producer, no
creator tool, no timestamps, no local file paths).
"""
import io
import pathlib
import shutil

from playwright.sync_api import sync_playwright
from pypdf import PdfReader, PdfWriter

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "resume" / "resume.html"
OUT = ROOT / "Joseph-Rockwood-Resume.pdf"


def find_chrome():
    for name in ("google-chrome", "chromium", "chromium-browser", "chrome"):
        path = shutil.which(name)
        if path:
            return path
    return None  # fall back to Playwright's bundled browser


def render() -> bytes:
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=find_chrome())
        page = browser.new_page()
        page.goto(SRC.as_uri(), wait_until="load")
        pdf = page.pdf(format="Letter", print_background=True, prefer_css_page_size=True)
        browser.close()
        return pdf


def scrub(pdf: bytes) -> bytes:
    writer = PdfWriter(clone_from=PdfReader(io.BytesIO(pdf)))
    writer._info = None  # drop Chrome's info dict (producer, creator, dates)
    writer.add_metadata({"/Title": "Joseph Rockwood — Résumé", "/Author": "Joseph Rockwood"})
    buf = io.BytesIO()
    writer.write(buf)
    return buf.getvalue()


if __name__ == "__main__":
    OUT.write_bytes(scrub(render()))
    print(f"wrote {OUT.relative_to(ROOT)} ({OUT.stat().st_size // 1024} KB)")
