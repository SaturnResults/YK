#!/usr/bin/env python3
"""
Update pass 3:
  - Fix mobile nav scroll: body scrolls, header+footer stay fixed
  - Remove circular WhatsApp button from mobile header
  - Add full-width WhatsApp bar + Book Now to mobile footer
  - Update style.css accordingly
"""
import os, re, glob

BASE = "/Users/harrybingham/Desktop/New Folder With Items 2/Buisness Mac/Saturn Results/Claud/YK WELLNESS OFFICIAL SITE"
FRESHA = "https://www.fresha.com/a/yk-wellness-london-westway-sports-fitness-centre-uk-1-crowthorne-road-git4ohyh"
WA = "https://api.whatsapp.com/send/?phone=%2B447910007933&text&type=phone_number&app_absent=0"

WA_SVG = '<svg viewBox="0 0 24 24" fill="currentColor" width="20" height="20"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>'

# New footer block (same for ALL pages)
NEW_FOOTER_BLOCK = f"""  <div class="nav__mobile-footer">
    <a href="{WA}" class="nav__mobile-wa-full" target="_blank">
      WhatsApp
      {WA_SVG}
    </a>
    <a href="{FRESHA}" target="_blank" class="btn btn-primary">Book Now</a>
  </div>"""

OLD_FOOTER_BLOCK = f"""  <div class="nav__mobile-footer">
    <a href="{FRESHA}" target="_blank" class="btn btn-primary">Book Appointment</a>
  </div>"""

# ----------------------------------------------------------------
# Update all HTML files
# ----------------------------------------------------------------
files = (
    [os.path.join(BASE, 'index.html')] +
    glob.glob(os.path.join(BASE, '*/index.html'))
)

print("=== Updating HTML files ===")
for path in sorted(files):
    rel = os.path.relpath(path, BASE)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. Remove circular WhatsApp button from header
    content = re.sub(
        r'\s*<a href="[^"]*" class="nav__mobile-whatsapp"[^>]*>.*?</a>',
        '',
        content,
        flags=re.DOTALL
    )

    # 2. Replace footer (Book Appointment → WhatsApp bar + Book Now)
    if OLD_FOOTER_BLOCK in content:
        content = content.replace(OLD_FOOTER_BLOCK, NEW_FOOTER_BLOCK)
    else:
        # Footer might already have been partially updated — find and replace robustly
        content = re.sub(
            r'<div class="nav__mobile-footer">.*?</div>',
            NEW_FOOTER_BLOCK,
            content,
            flags=re.DOTALL
        )

    if content != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ {rel}")
    else:
        print(f"  — {rel} (no change)")

# ----------------------------------------------------------------
# Update style.css
# ----------------------------------------------------------------
print("\n=== Updating style.css ===")
css_path = os.path.join(BASE, 'style.css')
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Fix 1: nav__mobile — remove overflow-y: auto (body handles scrolling now)
css = css.replace(
    '  overflow-y: auto;\n  transform: translateX(110%);',
    '  overflow: hidden;\n  transform: translateX(110%);'
)

# Fix 2: nav__mobile-body — add min-height: 0 and overflow-y: auto
css = css.replace(
    '.nav__mobile-body { flex: 1; padding: 0.5rem 0; }',
    '.nav__mobile-body { flex: 1; min-height: 0; overflow-y: auto; padding: 0.5rem 0; -webkit-overflow-scrolling: touch; }'
)

# Fix 3: nav__mobile-footer — add flex layout for stacked buttons
css = css.replace(
    """.nav__mobile-footer {
  padding: 1.1rem 1.4rem;
  border-top: 1px solid #f0ebe4;
  flex-shrink: 0;
}""",
    """.nav__mobile-footer {
  padding: 1rem 1.4rem 1.4rem;
  border-top: 1px solid #f0ebe4;
  flex-shrink: 0;
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
}"""
)

# Fix 4: Remove old circular WhatsApp button CSS, add new full-width button CSS
# Keep existing .nav__mobile-whatsapp in case it's still referenced, just update it
# And add the new full-width style
if '.nav__mobile-wa-full' not in css:
    css += """
/* Mobile nav: full-width WhatsApp button in footer */
.nav__mobile-wa-full {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  padding: 0.85rem 1.25rem;
  background: #25D366;
  color: #fff;
  border-radius: 10px;
  font-family: var(--font-sans);
  font-size: 0.95rem;
  font-weight: 600;
  text-decoration: none;
  transition: background 0.2s;
  box-sizing: border-box;
}
.nav__mobile-wa-full:hover { background: #1ebe5d; }
.nav__mobile-wa-full svg { flex-shrink: 0; }
"""
    print("  ✓ WhatsApp full-button CSS added")

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)
print("  ✓ style.css saved")

print("\n=== Done ===")
