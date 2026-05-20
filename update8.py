#!/usr/bin/env python3
"""
Update 8:
  1. What to Expect cards — vertical stack on mobile
  2. Fix Facebook link sitewide
  3. Fix horizontal scroll (overflow-x: hidden)
  4. Replace map placeholder with real iframe on homepage
  5. CSS updates
"""
import os, re, glob

BASE = "/Users/harrybingham/Desktop/New Folder With Items 2/Buisness Mac/Saturn Results/Claud/YK WELLNESS OFFICIAL SITE"
FB = "https://www.facebook.com/ykwellness.london/"

MAP_IFRAME = '''<div class="map-embed fade-up">
        <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2783.496058748103!2d-0.22262122325936398!3d51.51615701006345!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x48761018edd5e72d%3A0xad5518ba53d1a609!2sYK%20Wellness!5e1!3m2!1sen!2suk!4v1776879716383!5m2!1sen!2suk" width="100%" height="100%" style="border:0;display:block;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
      </div>'''

OLD_MAP = '''<div class="map-placeholder fade-up">
        <span>📍</span>
        <span class="map-placeholder__label">Westway Sports Centre, W10</span>
        <a href="https://maps.google.com/?q=Westway+Sports+Centre+1+Crowthorne+Road+London+W10+6RP" target="_blank" class="btn btn-white" style="margin-top:1rem;font-size:0.85rem;">Open in Google Maps</a>
      </div>'''

files = [os.path.join(BASE, 'index.html')] + glob.glob(os.path.join(BASE, '*/index.html'))

# ── 1. What to Expect grid ───────────────────────────────────────────
print("=== 1. What to Expect grid ===")
mt_path = os.path.join(BASE, 'massage-therapy', 'index.html')
with open(mt_path, 'r', encoding='utf-8') as f:
    mt = f.read()

OLD_GRID = 'style="display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;margin-top:2rem;" class="fade-up"'
NEW_GRID = 'class="expect-grid fade-up"'
if OLD_GRID in mt:
    mt = mt.replace(OLD_GRID, NEW_GRID)
    with open(mt_path, 'w', encoding='utf-8') as f:
        f.write(mt)
    print("  ✓ expect-grid class applied")
else:
    print("  ! not found — trying alternate order")
    mt = re.sub(
        r'class="fade-up"\s*style="display:grid;grid-template-columns:1fr 1fr;gap:1\.5rem;margin-top:2rem;"',
        'class="expect-grid fade-up"',
        mt
    )
    # Also try without fade-up
    mt = mt.replace(
        'style="display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;margin-top:2rem;"',
        'class="expect-grid fade-up"'
    )
    with open(mt_path, 'w', encoding='utf-8') as f:
        f.write(mt)
    print("  ✓ applied via fallback")

# ── 2. Fix Facebook links sitewide ──────────────────────────────────
print("\n=== 2. Fix Facebook links ===")
for path in sorted(files):
    rel = os.path.relpath(path, BASE)
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    if 'aria-label="Facebook"' not in html:
        continue
    updated = re.sub(
        r'href="[^"]*"\s*(class="social-btn"\s*aria-label="Facebook"|class="social-btn" aria-label="Facebook")',
        f'href="{FB}" \\1',
        html
    )
    if updated == html:
        # Try simpler replace
        updated = html.replace('href="#" class="social-btn" aria-label="Facebook"',
                               f'href="{FB}" class="social-btn" aria-label="Facebook"')
    if updated != html:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(updated)
        print(f"  ✓ {rel}")
    else:
        print(f"  ! {rel} — pattern not matched")

# ── 3. Replace map placeholder with iframe on homepage ──────────────
print("\n=== 3. Map on homepage ===")
idx_path = os.path.join(BASE, 'index.html')
with open(idx_path, 'r', encoding='utf-8') as f:
    idx = f.read()
if OLD_MAP in idx:
    idx = idx.replace(OLD_MAP, MAP_IFRAME)
    with open(idx_path, 'w', encoding='utf-8') as f:
        f.write(idx)
    print("  ✓ Map iframe added to homepage")
else:
    print("  ! OLD_MAP block not found exactly — check manually")

# ── 4. CSS updates ───────────────────────────────────────────────────
print("\n=== 4. CSS ===")
css_path = os.path.join(BASE, 'style.css')
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# 4a. overflow-x: hidden on html + body
css = css.replace(
    'html { scroll-behavior: smooth; font-size: 16px; }',
    'html { scroll-behavior: smooth; font-size: 16px; overflow-x: hidden; }'
)
css = css.replace(
    'body {\n  font-family: var(--font-sans);\n  background: var(--charcoal);\n  color: var(--charcoal);\n  line-height: 1.7;\n  -webkit-font-smoothing: antialiased;\n}',
    'body {\n  font-family: var(--font-sans);\n  background: var(--charcoal);\n  color: var(--charcoal);\n  line-height: 1.7;\n  -webkit-font-smoothing: antialiased;\n  overflow-x: hidden;\n}'
)
print("  ✓ overflow-x: hidden added")

# 4b. expect-grid class
if 'expect-grid' not in css:
    css += """
/* What to Expect cards grid */
.expect-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
  margin-top: 2rem;
}
@media (max-width: 600px) {
  .expect-grid {
    grid-template-columns: 1fr;
  }
}
"""
    print("  ✓ .expect-grid CSS added")

# 4c. map-embed class for the iframe container
if 'map-embed' not in css:
    css += """
/* Homepage map embed */
.map-embed {
  border-radius: var(--radius-lg);
  overflow: hidden;
  aspect-ratio: 4/3;
  position: relative;
}
.map-embed iframe {
  position: absolute;
  top: 0; left: 0;
  width: 100%; height: 100%;
  border: 0;
  display: block;
}
"""
    print("  ✓ .map-embed CSS added")

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)
print("  ✓ style.css saved")

print("\n=== Done ===")
