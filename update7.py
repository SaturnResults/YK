#!/usr/bin/env python3
"""
Update 7: Remove mobile-cta-bar from all HTML pages, CSS and JS.
WhatsApp + Book Now stays in the nav drawer footer only.
"""
import os, re, glob

BASE = "/Users/harrybingham/Desktop/New Folder With Items 2/Buisness Mac/Saturn Results/Claud/YK WELLNESS OFFICIAL SITE"

# ── 1. Strip mobile-cta-bar block from every HTML file ──────────────
files = [os.path.join(BASE, 'index.html')] + glob.glob(os.path.join(BASE, '*/index.html'))

print("=== Removing mobile-cta-bar from HTML ===")
for path in sorted(files):
    rel = os.path.relpath(path, BASE)
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    if 'mobile-cta-bar' not in html:
        print(f"  — {rel} (already clean)")
        continue
    cleaned = re.sub(
        r'\n?\s*<!-- Mobile sticky CTA bar -->.*?</div>\s*\n?',
        '\n',
        html,
        flags=re.DOTALL
    )
    if cleaned == html:
        # fallback: remove the div directly
        cleaned = re.sub(
            r'\n?\s*<div class="mobile-cta-bar"[^>]*>.*?</div>\s*\n?',
            '\n',
            html,
            flags=re.DOTALL
        )
    with open(path, 'w', encoding='utf-8') as f:
        f.write(cleaned)
    print(f"  ✓ {rel}")

# ── 2. Remove mobile-cta-bar CSS block from style.css ───────────────
print("\n=== Removing mobile-cta-bar CSS ===")
css_path = os.path.join(BASE, 'style.css')
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

css = re.sub(
    r'/\* ── Mobile sticky CTA bar.*?(?=\n/\*|\Z)',
    '',
    css,
    flags=re.DOTALL
)
# Also remove the body padding-bottom rule if isolated
css = re.sub(
    r'@media \(max-width: 768px\) \{\s*body \{ padding-bottom: \d+px; \}\s*\}',
    '',
    css
)
with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css.rstrip() + '\n')
print("  ✓ CSS cleaned")

# ── 3. Remove mobileCTABar JS from main.js ───────────────────────────
print("\n=== Cleaning main.js ===")
js_path = os.path.join(BASE, 'main.js')
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

js = js.replace('const mobileCTABar = document.getElementById(\'mobileCTABar\');\n\n', '')
js = js.replace('  if (mobileCTABar) mobileCTABar.style.display = \'none\';\n', '')
js = js.replace('  if (mobileCTABar) mobileCTABar.style.display = \'\';\n', '')

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)
print("  ✓ main.js cleaned")

print("\n=== Done ===")
