#!/usr/bin/env python3
"""
Update 5:
  1. Fix View More button (removeClass instead of style.display)
  2. Fix about-us grid: mobile responsive (no horizontal scroll, stacks vertically)
  3. Fix about-us em dashes + British English
  4. Fix mobile nav scroll (overflow-y: scroll, bigger accordion max-height)
"""
import os, re

BASE = "/Users/harrybingham/Desktop/New Folder With Items 2/Buisness Mac/Saturn Results/Claud/YK WELLNESS OFFICIAL SITE"

# ────────────────────────────────────────────────
# 1. Fix View More JS
# ────────────────────────────────────────────────
print("=== 1. Fix View More JS ===")
js_path = os.path.join(BASE, 'main.js')
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

OLD_JS = """  btn.addEventListener('click', function () {
    document.querySelectorAll('.testimonial-card--hidden').forEach(function (card) {
      card.style.display = '';
      // Trigger fade-up animation if not yet visible
      requestAnimationFrame(() => card.classList.add('visible'));
    });
    wrap.style.display = 'none';
  });"""

NEW_JS = """  btn.addEventListener('click', function () {
    document.querySelectorAll('.testimonial-card--hidden').forEach(function (card) {
      card.classList.remove('testimonial-card--hidden');
      requestAnimationFrame(() => card.classList.add('visible'));
    });
    wrap.style.display = 'none';
  });"""

if OLD_JS in js:
    js = js.replace(OLD_JS, NEW_JS)
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(js)
    print("  ✓ View More JS fixed")
else:
    print("  ! OLD_JS not found — manual check needed")

# ────────────────────────────────────────────────
# 2. Fix about-us grid: replace inline style with class
# ────────────────────────────────────────────────
print("\n=== 2. Fix about-us grid ===")
about_path = os.path.join(BASE, 'about-us', 'index.html')
with open(about_path, 'r', encoding='utf-8') as f:
    about = f.read()

OLD_GRID = 'style="display:grid;grid-template-columns:repeat(3,1fr);gap:1.5rem;margin-top:3rem;"'
NEW_GRID = 'class="about-pillars-grid"'

if OLD_GRID in about:
    about = about.replace(OLD_GRID + ' class="fade-up"', 'class="about-pillars-grid fade-up"')
    # Also handle if class comes before or the order is different
    about = about.replace(OLD_GRID, NEW_GRID)
    print("  ✓ Grid class replaced")
else:
    print("  ! OLD_GRID not found, trying regex")
    about = re.sub(
        r'style="display:grid;grid-template-columns:repeat\(3,1fr\);gap:1\.5rem;margin-top:3rem;"(\s*class="fade-up")?',
        'class="about-pillars-grid fade-up"',
        about
    )
    print("  ✓ Grid replaced via regex")

# ────────────────────────────────────────────────
# 3. Fix about-us em dashes + British English
# ────────────────────────────────────────────────
print("\n=== 3. Fix about-us em dashes ===")
replacements = [
    # Title/meta tags
    ('About Us | YK Wellness — West London',
     'About Us | YK Wellness, West London'),
    ('About YK Wellness — over 400 five-star reviews',
     'About YK Wellness: over 400 five-star reviews'),
    # Content
    ('through results — through clients who come back, and who send their friends.',
     'through results, through clients who come back and who send their friends.'),
    ('personalised care — taking time to understand each client',
     'personalised care, taking time to understand each client'),
    # Service pillar cards
    ('lymphatic drainage — each performed to the highest clinical standard.',
     'lymphatic drainage, each performed to the highest clinical standard.'),
    ('dysfunction — not just the symptom.',
     'dysfunction, not just the symptom.'),
    ('lymphatic drainage — advanced therapies for complex presentations.',
     'lymphatic drainage: advanced therapies for complex presentations.'),
    # FAQ
    ('We have consistently high recruitment standards — we only work',
     'We have consistently high recruitment standards; we only work'),
    ('Yes — Westway Sports Centre has ample on-site parking',
     'Yes, Westway Sports Centre has ample on-site parking'),
    # Any remaining em dashes
    (' — ', ', '),
]

changed = 0
for old, new in replacements:
    if old in about:
        about = about.replace(old, new)
        changed += 1

with open(about_path, 'w', encoding='utf-8') as f:
    f.write(about)
print(f"  ✓ {changed} replacements made in about-us/index.html")

# ────────────────────────────────────────────────
# 4. CSS: fix nav scroll + add about-pillars-grid
# ────────────────────────────────────────────────
print("\n=== 4. CSS fixes ===")
css_path = os.path.join(BASE, 'style.css')
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# 4a. Change overflow-y: auto → scroll on nav__mobile-body for iOS
css = css.replace(
    '.nav__mobile-body { flex: 1; min-height: 0; overflow-y: auto; padding: 0.5rem 0; -webkit-overflow-scrolling: touch; }',
    '.nav__mobile-body { flex: 1; min-height: 0; overflow-y: scroll; padding: 0.5rem 0; -webkit-overflow-scrolling: touch; }'
)
print("  ✓ nav__mobile-body overflow-y: scroll")

# 4b. Increase accordion max-height so all items visible
css = css.replace(
    '.nav__mobile-accordion.open .nav__mobile-accordion-body { max-height: 500px; }',
    '.nav__mobile-accordion.open .nav__mobile-accordion-body { max-height: 700px; }'
)
print("  ✓ accordion max-height: 700px")

# 4c. Add about-pillars-grid class if not present
if 'about-pillars-grid' not in css:
    css += """
/* About Us: service pillars grid — responsive */
.about-pillars-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
  margin-top: 3rem;
}
@media (max-width: 768px) {
  .about-pillars-grid {
    grid-template-columns: 1fr;
  }
}
"""
    print("  ✓ about-pillars-grid CSS added")
else:
    print("  — about-pillars-grid already in CSS")

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)
print("  ✓ style.css saved")

print("\n=== Done ===")
