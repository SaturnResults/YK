#!/usr/bin/env python3
"""
Update pass 4:
  - Rename: about → about-us, contact → contact-us, lymphatic-drainage → lymphatic-drainage-massage
  - Update all internal links sitewide for renames
  - British English rewrites: CBD, lymphatic, specialised-treatments, home (no em dashes, no AI phrases)
  - Homepage reviews: 3 visible + 2 new hidden behind "View More"
  - Add "Built by Saturn Results" subtle footer credit on all pages
  - CSS/JS updates for reviews + "Built by" style
"""
import os, re, glob, shutil

BASE = "/Users/harrybingham/Desktop/New Folder With Items 2/Buisness Mac/Saturn Results/Claud/YK WELLNESS OFFICIAL SITE"

# ----------------------------------------------------------------
# 1. RENAME DIRECTORIES
# ----------------------------------------------------------------
renames = [
    ('about',              'about-us'),
    ('contact',            'contact-us'),
    ('lymphatic-drainage', 'lymphatic-drainage-massage'),
]
print("=== 1. Renaming directories ===")
for old, new in renames:
    src = os.path.join(BASE, old)
    dst = os.path.join(BASE, new)
    if os.path.isdir(src) and not os.path.isdir(dst):
        shutil.move(src, dst)
        print(f"  {old}/ → {new}/")
    elif os.path.isdir(dst):
        print(f"  {new}/ already exists")
    else:
        print(f"  SKIP {old}/ (not found)")

# ----------------------------------------------------------------
# 2. SITEWIDE LINK UPDATES (all HTML + main.js)
# ----------------------------------------------------------------
link_map = [
    ('/about/',              '/about-us/'),
    ('/contact/',            '/contact-us/'),
    ('/lymphatic-drainage/', '/lymphatic-drainage-massage/'),
    # OG urls
    ('.github.io/about/',              '.github.io/about-us/'),
    ('.github.io/contact/',            '.github.io/contact-us/'),
    ('.github.io/lymphatic-drainage/', '.github.io/lymphatic-drainage-massage/'),
]

def apply_link_renames(content):
    for old, new in link_map:
        content = content.replace(old, new)
    return content

all_html = (
    [os.path.join(BASE, 'index.html')] +
    glob.glob(os.path.join(BASE, '*/index.html'))
)
print("\n=== 2. Updating links in all HTML files ===")
for path in sorted(all_html):
    if 'landing' in path:
        continue
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    new_c = apply_link_renames(c)
    if new_c != c:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_c)
        print(f"  ✓ {os.path.relpath(path, BASE)}")

# Update main.js
js_path = os.path.join(BASE, 'main.js')
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()
new_js = apply_link_renames(js)
if new_js != js:
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(new_js)
    print(f"  ✓ main.js")

# ----------------------------------------------------------------
# 3. BRITISH ENGLISH TEXT FIXES
# ----------------------------------------------------------------
print("\n=== 3. British English rewrites ===")

def fix(content, replacements):
    for old, new in replacements:
        content = content.replace(old, new)
    return content

# --- CBD MASSAGE ---
cbd_path = os.path.join(BASE, 'cbd-massage/index.html')
with open(cbd_path, 'r', encoding='utf-8') as f:
    cbd = f.read()

cbd = fix(cbd, [
    # Hero subtitle
    ('CBD oil — delivering deeper anti-inflammatory relief, accelerated recovery, and a level of relaxation that conventional massage alone cannot achieve.',
     'CBD oil, for deeper anti-inflammatory relief, faster recovery, and a level of relaxation that conventional massage alone cannot achieve.'),
    # Section heading
    ('<h2>Cannabidiol massage — what it actually does</h2>',
     '<h2>What CBD massage actually does</h2>'),
    # CBD definition
    ('CBD — short for cannabidiol — is a naturally occurring compound',
     'CBD (short for cannabidiol) is a naturally occurring compound'),
    # "The result is..."
    ('than massage alone — particularly valuable for chronic pain conditions',
     'than massage alone, particularly valuable for chronic pain conditions'),
    # Pricing
    ('Pricing on enquiry — contact us for details.',
     'Pricing on enquiry. Get in touch for details.'),
    # Stress card
    ('triggered by massage — making this an especially effective combination for those carrying stress in the body.',
     'triggered by massage, making this a particularly effective combination for those who carry stress in the body.'),
    # FAQ 1
    ("You will feel relaxed after your treatment, but that is the massage, not any intoxicating effect.",
     "You will feel relaxed after your treatment, but that is down to the massage itself, not any intoxicating effect."),
    ("You will feel relaxed after your treatment — but that is the massage, not any intoxicating effect.",
     "You will feel relaxed after your treatment, but that is down to the massage itself, not any intoxicating effect."),
    # FAQ 2 (legal)
    ('CBD derived from hemp (which our products are) is entirely legal in the United Kingdom, provided THC content is within the permitted trace limits — which ours is.',
     'CBD derived from hemp (which our products are) is entirely legal in the United Kingdom, provided THC content is within the permitted trace limits, as ours is.'),
    # FAQ 3 (how quickly)
    ('CBD massage often feels more effective the morning after than right when you leave',
     'CBD massage often feels more effective the morning after than immediately when you leave'),
    # FAQ 4 (can drive)
    ('You may feel pleasantly relaxed after your treatment — as you would after any good massage — but there is absolutely no psychoactive effect',
     'You may feel pleasantly relaxed after your treatment, as you would after any good massage, but there is absolutely no psychoactive effect'),
    # FAQ 5 (which conditions)
    ('For straightforward relaxation, a Swedish massage may be equally effective — CBD massage really shines for those with ongoing physical complaints.',
     'For straightforward relaxation, a Swedish massage may be equally effective. CBD massage delivers the greatest additional benefit for those with ongoing physical complaints.'),
    # CTA
    ('Get in touch and we will talk you through it — no obligation, no pressure.',
     'Get in touch and we will talk you through it. No obligation, no pressure.'),
])

with open(cbd_path, 'w', encoding='utf-8') as f:
    f.write(cbd)
print("  ✓ cbd-massage/index.html")

# --- LYMPHATIC DRAINAGE MASSAGE ---
lymph_path = os.path.join(BASE, 'lymphatic-drainage-massage/index.html')
with open(lymph_path, 'r', encoding='utf-8') as f:
    lymph = f.read()

lymph = fix(lymph, [
    # Hero subtitle
    ('Gentle, rhythmic massage following the natural pathways of the lymphatic system — supporting detoxification, reducing swelling, boosting immunity, and promoting full-body healing at a cellular level.',
     'Gentle, rhythmic massage following the natural pathways of the lymphatic system, supporting detoxification, reducing swelling, boosting immunity, and promoting full-body healing.'),
    # Section heading
    ('<h2>Manual lymphatic drainage — how it works</h2>',
     '<h2>How manual lymphatic drainage works</h2>'),
    # "works with — rather than against —"
    ('that works with — rather than against — the body\'s own lymphatic system.',
     "that works with the body's own lymphatic system rather than against it."),
    # "sluggish or overwhelmed —"
    ('When it becomes sluggish or overwhelmed — through illness, injury, surgery, or simply inactivity —',
     'When it becomes sluggish or overwhelmed through illness, injury, surgery, or simply inactivity,'),
    # "light touch —"
    ('Sessions are deeply relaxing despite the light touch — many clients fall asleep during treatment.',
     'Sessions are deeply relaxing despite the light touch; many clients fall asleep during treatment.'),
    # Pricing
    ('Pricing on enquiry — contact us for details.',
     'Pricing on enquiry. Get in touch for details.'),
    # Lymphoedema section
    ('chronic swelling resulting from lymphatic damage or removal of lymph nodes — regular MLD is one of the primary treatment methods',
     'chronic swelling resulting from lymphatic damage or removal of lymph nodes. Regular MLD is one of the primary treatment methods'),
    # Hydration tip
    ('Hydration is important — the lymphatic system depends on adequate fluid intake',
     'Hydration matters. The lymphatic system depends on adequate fluid intake'),
    # FAQ 1
    ('Traditional massage targets muscle tissue with firm pressure — MLD works at a completely different level of the body.',
     'Traditional massage targets muscle tissue with firm pressure. MLD works at a completely different level of the body.'),
    # FAQ 4
    ('Some experience a mild fatigue or heaviness for a few hours as the body processes the increased lymphatic activity — this is entirely normal and a sign the treatment is working.',
     'Some experience a mild fatigue or heaviness for a few hours as the body processes the increased lymphatic activity; this is entirely normal and a sign the treatment is working.'),
    # CTA
    ('Unsure whether lymphatic drainage is the right treatment for you? Get in touch and we will be happy to advise.',
     'Not sure if lymphatic drainage is right for you? Get in touch and we will be happy to advise.'),
])

with open(lymph_path, 'w', encoding='utf-8') as f:
    f.write(lymph)
print("  ✓ lymphatic-drainage-massage/index.html")

# --- SPECIALISED TREATMENTS ---
spec_path = os.path.join(BASE, 'specialised-treatments/index.html')
with open(spec_path, 'r', encoding='utf-8') as f:
    spec = f.read()

spec = fix(spec, [
    # Hero subtitle
    ('Powerful, targeted therapies that go beyond traditional massage — combining ancient wisdom with modern clinical technique to unlock deep healing and lasting results.',
     'Powerful, targeted therapies that go beyond traditional massage, combining time-tested technique with modern clinical knowledge for deep, lasting results.'),
    # Cupping intro
    ('One of the oldest therapeutic techniques in the world — reimagined with modern clinical precision.',
     'One of the oldest therapeutic techniques in the world, reimagined with modern clinical precision.'),
    # Cupping "hands alone"
    ('promoting deep healing in a way that hands alone cannot achieve.',
     'promoting deep healing in a way that hands-only treatment cannot achieve.'),
    # Dry needling trigger points
    ('myofascial trigger points — the hyperirritable spots within muscle tissue that refer pain',
     'myofascial trigger points: the hyperirritable spots within muscle tissue that refer pain'),
    # Dry needling distinct
    ('Dry needling is distinct from traditional acupuncture — it is a Western clinical technique',
     'Dry needling is distinct from traditional acupuncture. It is a Western clinical technique'),
    # CBD card
    ('making it a powerful complement to therapeutic massage — particularly for inflammation',
     'making it a powerful complement to therapeutic massage, particularly for inflammation'),
    # Lymphatic card
    ('stimulates the lymphatic system — the body\'s natural waste disposal network.',
     "stimulates the lymphatic system, the body's natural waste disposal network."),
    # FAQ 1
    ('Cupping often leaves circular discolouration on the skin — these are not bruises but a result',
     'Cupping often leaves circular marks on the skin; these are not bruises but a result'),
    # FAQ 2
    ('Both use the same style of thin, sterile needle — but the philosophy and application differ significantly.',
     'Both use the same style of thin, sterile needle, but the philosophy and application differ significantly.'),
    # FAQ 4
    ("just get in touch — we're happy to chat through your symptoms",
     "just get in touch and we will be happy to chat through your symptoms"),
    ("There's no obligation, and no such thing as a silly question.",
     "There is no obligation, and no such thing as a silly question."),
])

with open(spec_path, 'w', encoding='utf-8') as f:
    f.write(spec)
print("  ✓ specialised-treatments/index.html")

# --- HOME PAGE: scan for em dashes in body content ---
home_path = os.path.join(BASE, 'index.html')
with open(home_path, 'r', encoding='utf-8') as f:
    home = f.read()

home = fix(home, [
    # Any em dashes in body text (titles are fine)
    (" — ", ", "),   # broad fallback; most occurrences in body copy
])
# Revert any title/heading em dashes that look intentional (none expected)
with open(home_path, 'w', encoding='utf-8') as f:
    f.write(home)
print("  ✓ index.html (em dashes removed)")

# ----------------------------------------------------------------
# 4. HOMEPAGE REVIEWS: 3 visible + 2 new (hidden behind View More)
# ----------------------------------------------------------------
print("\n=== 4. Homepage reviews update ===")
with open(home_path, 'r', encoding='utf-8') as f:
    home = f.read()

NEW_TESTIMONIALS = """<!-- TESTIMONIALS -->
<section class="testimonials">
  <div class="container">
    <div class="section-header section-header--center fade-up">
      <p class="eyebrow">Client Stories</p>
      <div class="divider divider--center" style="background:var(--sage)"></div>
      <h2>Our clients say it best</h2>
    </div>
    <div class="testimonials-grid" id="reviewsGrid">

      <div class="testimonial-card fade-up">
        <div class="testimonial-card__stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
        <p class="testimonial-card__quote">"Yury is hands down the best massage therapist I have tried in London. He is very knowledgeable, adapts his methods to your needs and performs the most relaxing yet therapeutic massages."</p>
        <div class="testimonial-card__author">
          <div class="testimonial-card__avatar">M</div>
          <div>
            <div class="testimonial-card__name">Mounir Boustany</div>
            <div class="testimonial-card__via">Google Review</div>
          </div>
        </div>
      </div>

      <div class="testimonial-card fade-up">
        <div class="testimonial-card__stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
        <p class="testimonial-card__quote">"After a long term shoulder operation, I was nervous about getting massage therapy. But Yury made me feel completely at ease from the very first minute. The results have been incredible."</p>
        <div class="testimonial-card__author">
          <div class="testimonial-card__avatar">H</div>
          <div>
            <div class="testimonial-card__name">Harry Young</div>
            <div class="testimonial-card__via">Google Review</div>
          </div>
        </div>
      </div>

      <div class="testimonial-card fade-up">
        <div class="testimonial-card__stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
        <p class="testimonial-card__quote">"I had one of the best deep tissue massages from here! My therapist, Christos, was friendly and put me at ease from the moment I walked in. Already booked my next session."</p>
        <div class="testimonial-card__author">
          <div class="testimonial-card__avatar">M</div>
          <div>
            <div class="testimonial-card__name">Maxwell Grant</div>
            <div class="testimonial-card__via">Google Review</div>
          </div>
        </div>
      </div>

      <div class="testimonial-card fade-up testimonial-card--hidden" id="extraReview1">
        <div class="testimonial-card__stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
        <p class="testimonial-card__quote">"Yury is as good as it gets. Professional, caring, about the details, and he gets the details spot on. You will not be disappointed!!"</p>
        <div class="testimonial-card__author">
          <div class="testimonial-card__avatar">N</div>
          <div>
            <div class="testimonial-card__name">Nichey Store</div>
            <div class="testimonial-card__via">Google Review</div>
          </div>
        </div>
      </div>

      <div class="testimonial-card fade-up testimonial-card--hidden" id="extraReview2">
        <div class="testimonial-card__stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
        <p class="testimonial-card__quote">"Yuri is categorically the best sports massage therapist I've ever had. He connects with the muscle fibres so well, almost as if he can see where every adhesion is without you needing to say a word. He makes osteopathy seem like an art. Without him my back wouldn't have improved so much. Definitely recommend, you won't regret it."</p>
        <div class="testimonial-card__author">
          <div class="testimonial-card__avatar">A</div>
          <div>
            <div class="testimonial-card__name">Azaan Rehan</div>
            <div class="testimonial-card__via">Google Review</div>
          </div>
        </div>
      </div>

    </div>
    <div class="testimonials-more fade-up" id="reviewsMoreWrap">
      <button class="testimonials-more-btn" id="reviewsMoreBtn">View more reviews</button>
    </div>
  </div>
</section>"""

# Replace old testimonials section
old_section_pattern = re.compile(
    r'<!-- TESTIMONIALS -->.*?</section>',
    re.DOTALL
)
if old_section_pattern.search(home):
    home = old_section_pattern.sub(NEW_TESTIMONIALS, home, count=1)
    print("  ✓ Reviews section replaced")
else:
    print("  ⚠ Reviews section not found by regex")

with open(home_path, 'w', encoding='utf-8') as f:
    f.write(home)

# ----------------------------------------------------------------
# 5. "BUILT BY" FOOTER ON ALL PAGES
# ----------------------------------------------------------------
print("\n=== 5. Adding Built by attribution ===")

OLD_FOOTER_BOTTOM_END = """    <div class="footer-bottom">
      <span>&copy; 2025 The Wellness Well Ltd trading as YK Wellness. Company Reg. 12345040.</span>
      <div style="display:flex;gap:1.5rem;">
        <a href="/privacy-policy/">Privacy Policy</a>
        <a href="/terms/">Terms &amp; Conditions</a>
      </div>
    </div>
  </div>
</footer>"""

NEW_FOOTER_BOTTOM_END = """    <div class="footer-bottom">
      <span>&copy; 2025 The Wellness Well Ltd trading as YK Wellness. Company Reg. 12345040.</span>
      <div style="display:flex;gap:1.5rem;">
        <a href="/privacy-policy/">Privacy Policy</a>
        <a href="/terms/">Terms &amp; Conditions</a>
      </div>
    </div>
    <div class="footer-built">Built by <a href="https://saturnresults.co.uk" target="_blank" rel="noopener">Saturn Results</a></div>
  </div>
</footer>"""

all_html = (
    [os.path.join(BASE, 'index.html')] +
    glob.glob(os.path.join(BASE, '*/index.html'))
)
count = 0
for path in sorted(all_html):
    if 'landing' in path:
        continue
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    if OLD_FOOTER_BOTTOM_END in c:
        c = c.replace(OLD_FOOTER_BOTTOM_END, NEW_FOOTER_BOTTOM_END)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(c)
        count += 1
print(f"  ✓ Added to {count} pages")

# ----------------------------------------------------------------
# 6. CSS UPDATES: reviews hidden state, view-more button, built-by
# ----------------------------------------------------------------
print("\n=== 6. CSS updates ===")
css_path = os.path.join(BASE, 'style.css')
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

EXTRA_CSS = """
/* Testimonials: hidden extras + View More button */
.testimonial-card--hidden { display: none; }
.testimonials-more {
  text-align: center;
  margin-top: 2.5rem;
}
.testimonials-more-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 2rem;
  background: transparent;
  border: 1.5px solid var(--sage);
  border-radius: 9px;
  color: var(--sage-dark);
  font-family: var(--font-sans);
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.2s, color 0.2s;
  letter-spacing: 0.02em;
}
.testimonials-more-btn:hover {
  background: var(--sage);
  color: #fff;
}

/* Footer: built by */
.footer-built {
  text-align: center;
  padding: 0.6rem 0 0.2rem;
  font-size: 0.7rem;
  color: rgba(255,255,255,0.18);
  border-top: 1px solid rgba(255,255,255,0.06);
  margin-top: 0.5rem;
}
.footer-built a {
  color: rgba(255,255,255,0.22);
  text-decoration: none;
  transition: color 0.2s;
}
.footer-built a:hover { color: rgba(255,255,255,0.5); }
"""

if '.testimonial-card--hidden' not in css:
    css += EXTRA_CSS
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)
    print("  ✓ CSS added")
else:
    print("  — CSS already present")

# ----------------------------------------------------------------
# 7. MAIN.JS: add View More handler + update nav paths
# ----------------------------------------------------------------
print("\n=== 7. main.js update ===")
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

VIEW_MORE_JS = """
// Reviews "View More" button
(function () {
  const btn = document.getElementById('reviewsMoreBtn');
  const wrap = document.getElementById('reviewsMoreWrap');
  if (!btn) return;
  btn.addEventListener('click', function () {
    document.querySelectorAll('.testimonial-card--hidden').forEach(function (card) {
      card.style.display = '';
      // Trigger fade-up animation if not yet visible
      requestAnimationFrame(() => card.classList.add('visible'));
    });
    wrap.style.display = 'none';
  });
})();
"""

if 'reviewsMoreBtn' not in js:
    js += VIEW_MORE_JS
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(js)
    print("  ✓ View More JS added")
else:
    print("  — View More JS already present")

print("\n=== All done ===")

# Quick summary
print("\nDirectories now at:")
for d in ['about-us','contact-us','lymphatic-drainage-massage']:
    p = os.path.join(BASE, d, 'index.html')
    print(f"  {'OK' if os.path.exists(p) else 'MISSING'}  /{d}/")
