#!/usr/bin/env python3
"""
Update 6: Add fixed mobile-only CTA bar (WhatsApp + Book Now) to all pages.
Sits at the bottom of the viewport on mobile, always visible while scrolling.
"""
import os, glob

BASE = "/Users/harrybingham/Desktop/New Folder With Items 2/Buisness Mac/Saturn Results/Claud/YK WELLNESS OFFICIAL SITE"
FRESHA = "https://www.fresha.com/a/yk-wellness-london-westway-sports-fitness-centre-uk-1-crowthorne-road-git4ohyh"
WA     = "https://api.whatsapp.com/send/?phone=%2B447910007933&text&type=phone_number&app_absent=0"

WA_SVG = '<svg viewBox="0 0 24 24" fill="currentColor" width="20" height="20" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>'

CTA_BAR = f"""
  <!-- Mobile sticky CTA bar -->
  <div class="mobile-cta-bar" id="mobileCTABar">
    <a href="{WA}" class="mobile-cta-bar__wa" target="_blank" rel="noopener">
      WhatsApp
      {WA_SVG}
    </a>
    <a href="{FRESHA}" class="mobile-cta-bar__book btn btn-primary" target="_blank" rel="noopener">Book Now</a>
  </div>"""

files = (
    [os.path.join(BASE, 'index.html')] +
    glob.glob(os.path.join(BASE, '*/index.html'))
)

print("=== Adding mobile CTA bar to HTML files ===")
for path in sorted(files):
    rel = os.path.relpath(path, BASE)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'mobile-cta-bar' in content:
        print(f"  — {rel} (already has bar)")
        continue

    if '</body>' not in content:
        print(f"  ! {rel} (no </body> tag)")
        continue

    content = content.replace('</body>', CTA_BAR + '\n</body>')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  ✓ {rel}")

# ── CSS ──────────────────────────────────────────────────────────────
print("\n=== Adding CSS ===")
css_path = os.path.join(BASE, 'style.css')
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

if 'mobile-cta-bar' not in css:
    css += """
/* ── Mobile sticky CTA bar ──────────────────────────────────────── */
.mobile-cta-bar {
  display: none; /* hidden on desktop */
}
@media (max-width: 768px) {
  .mobile-cta-bar {
    display: flex;
    flex-direction: column;
    gap: 0.55rem;
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    z-index: 9000;
    padding: 0.85rem 1rem 1.1rem;
    background: #fff;
    border-top: 1px solid #ede8e1;
    box-shadow: 0 -4px 20px rgba(0,0,0,0.08);
  }

  /* Push page footer up so bar doesn't overlap content */
  body { padding-bottom: 130px; }

  .mobile-cta-bar__wa {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
    padding: 0.85rem 1.25rem;
    background: #25D366;
    color: #fff;
    border-radius: 10px;
    font-family: var(--font-sans);
    font-size: 1rem;
    font-weight: 600;
    text-decoration: none;
    box-sizing: border-box;
    transition: background 0.2s;
  }
  .mobile-cta-bar__wa:hover,
  .mobile-cta-bar__wa:active { background: #1ebe5d; }
  .mobile-cta-bar__wa svg { flex-shrink: 0; }

  .mobile-cta-bar__book {
    display: block;
    width: 100%;
    text-align: center;
    border-radius: 10px;
    padding: 0.85rem 1.25rem;
    font-size: 1rem;
    box-sizing: border-box;
  }
}
"""
    print("  ✓ CSS added")
else:
    print("  — CSS already present")

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)
print("  ✓ style.css saved")

print("\n=== Done ===")
