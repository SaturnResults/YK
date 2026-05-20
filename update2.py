#!/usr/bin/env python3
"""
Update pass 2:
  - Fix info@ email → hello@ykwellness.co.uk everywhere
  - Add About Us dropdown to desktop nav
  - Add About accordion to mobile nav
  - Add green WhatsApp button to mobile header
  - Create about/index.html
  - Update main.js active nav for About dropdown
  - Add CSS for mobile WhatsApp button
"""
import os, glob

BASE = "/Users/harrybingham/Desktop/New Folder With Items 2/Buisness Mac/Saturn Results/Claud/YK WELLNESS OFFICIAL SITE"
FRESHA = "https://www.fresha.com/a/yk-wellness-london-westway-sports-fitness-centre-uk-1-crowthorne-road-git4ohyh"
WA = "https://api.whatsapp.com/send/?phone=%2B447910007933&text&type=phone_number&app_absent=0"

WA_SVG = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>'

# ------------------------------------------------------------------
# STRINGS TO REPLACE  (must match exactly what restructure.py wrote)
# ------------------------------------------------------------------

OLD_TEAM_NAV = """        <a href="/team/">Our Team</a>
        <a href="/contact/">Contact</a>
      </div>"""

NEW_ABOUT_NAV = """        <div class="nav__dropdown">
          <a href="/about/">About &#9662;</a>
          <div class="nav__dropdown-menu">
            <a href="/about/" class="nav__dropdown-item">
              <span class="nav__dropdown-item-title">About Us</span>
              <span class="nav__dropdown-item-desc">Our story, values and approach to wellness</span>
            </a>
            <a href="/team/" class="nav__dropdown-item">
              <span class="nav__dropdown-item-title">Meet the Team</span>
              <span class="nav__dropdown-item-desc">The therapists and practitioners behind YK Wellness</span>
            </a>
          </div>
        </div>
        <a href="/contact/">Contact</a>
      </div>"""

OLD_TEAM_MOBILE = """    <a href="/team/" class="nav__mobile-link">Our Team</a>
    <a href="/contact/" class="nav__mobile-link">Contact</a>"""

NEW_ABOUT_MOBILE = """    <div class="nav__mobile-accordion" id="aboutAccordion">
      <button class="nav__mobile-accordion-trigger">
        About
        <svg class="nav__mobile-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg>
      </button>
      <div class="nav__mobile-accordion-body">
        <a href="/about/" class="nav__mobile-sub-link">About Us</a>
        <a href="/team/" class="nav__mobile-sub-link">Meet the Team</a>
      </div>
    </div>
    <a href="/contact/" class="nav__mobile-link">Contact</a>"""

# WhatsApp button — inserted before the close button
OLD_CLOSE_BTN = """    <button class="nav__mobile-close" id="mobileClose" aria-label="Close menu">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
    </button>"""

NEW_CLOSE_WITH_WA = f"""    <a href="{WA}" class="nav__mobile-whatsapp" aria-label="WhatsApp" target="_blank">{WA_SVG}</a>
    <button class="nav__mobile-close" id="mobileClose" aria-label="Close menu">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
    </button>"""


def transform(content):
    # About dropdown (desktop)
    if OLD_TEAM_NAV in content:
        content = content.replace(OLD_TEAM_NAV, NEW_ABOUT_NAV)
    else:
        print("    ⚠ about desktop not found")

    # About accordion (mobile)
    if OLD_TEAM_MOBILE in content:
        content = content.replace(OLD_TEAM_MOBILE, NEW_ABOUT_MOBILE)
    else:
        print("    ⚠ about mobile not found")

    # WhatsApp button in mobile header
    if OLD_CLOSE_BTN in content:
        content = content.replace(OLD_CLOSE_BTN, NEW_CLOSE_WITH_WA)
    else:
        print("    ⚠ mobile close btn not found — WA button not added")

    # Fix email
    content = content.replace('info@ykwellness.co.uk', 'hello@ykwellness.co.uk')

    return content


# Collect all HTML files to update
html_files = (
    [os.path.join(BASE, 'index.html')] +
    glob.glob(os.path.join(BASE, '*/index.html'))
)
# Skip the old .html files at root (they'll be deleted before push)

print("=== Updating HTML files ===")
for path in sorted(html_files):
    rel = os.path.relpath(path, BASE)
    print(f"  {rel}")
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content = transform(content)
    if new_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"    ✓ updated")
    else:
        print(f"    — no changes")


# ------------------------------------------------------------------
# main.js — update active nav for About dropdown
# ------------------------------------------------------------------
print("\n=== Updating main.js ===")
js_path = os.path.join(BASE, 'main.js')
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

OLD_ACTIVE = """// Set active nav link (clean URL version)
(function () {
  const path = location.pathname;
  const treatmentPaths = [
    '/massage-therapy/', '/deep-tissue/', '/sports-massage/',
    '/swedish-massage/', '/cbd-massage/', '/lymphatic-drainage/'
  ];

  // Highlight direct nav links
  document.querySelectorAll('.nav__links > a').forEach(a => {
    if (a.getAttribute('href') === path) a.classList.add('active');
  });

  // Highlight Treatments dropdown trigger for any treatment sub-page
  if (treatmentPaths.includes(path)) {
    const trigger = document.querySelector('.nav__dropdown > a');
    if (trigger) trigger.classList.add('active');
    document.getElementById('treatmentsAccordion')?.classList.add('open');
  }
})();"""

NEW_ACTIVE = """// Set active nav link (clean URL version)
(function () {
  const path = location.pathname;
  const treatmentPaths = [
    '/massage-therapy/', '/deep-tissue/', '/sports-massage/',
    '/swedish-massage/', '/cbd-massage/', '/lymphatic-drainage/'
  ];
  const aboutPaths = ['/about/', '/team/'];

  // Highlight direct nav links
  document.querySelectorAll('.nav__links > a').forEach(a => {
    if (a.getAttribute('href') === path) a.classList.add('active');
  });

  // Highlight dropdown triggers
  document.querySelectorAll('.nav__dropdown > a').forEach(trigger => {
    const href = trigger.getAttribute('href');
    if (href === '/massage-therapy/' && treatmentPaths.includes(path)) {
      trigger.classList.add('active');
      document.getElementById('treatmentsAccordion')?.classList.add('open');
    }
    if (href === '/about/' && aboutPaths.includes(path)) {
      trigger.classList.add('active');
      document.getElementById('aboutAccordion')?.classList.add('open');
    }
  });
})();"""

if OLD_ACTIVE in js:
    js = js.replace(OLD_ACTIVE, NEW_ACTIVE)
    print("  ✓ Active nav updated")
else:
    print("  ⚠ Could not find old active nav block — skipping")

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)


# ------------------------------------------------------------------
# style.css — add WhatsApp button styles
# ------------------------------------------------------------------
print("\n=== Updating style.css ===")
css_path = os.path.join(BASE, 'style.css')
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

WA_CSS = """
/* Mobile nav WhatsApp button */
.nav__mobile-whatsapp {
  display: flex;
  align-items: center;
  justify-content: center;
  background: #25D366;
  color: #fff;
  border-radius: 50%;
  width: 36px;
  height: 36px;
  flex-shrink: 0;
  margin-left: auto;
  transition: background 0.2s;
}
.nav__mobile-whatsapp:hover { background: #1ebe5d; }
.nav__mobile-whatsapp svg {
  width: 18px;
  height: 18px;
  fill: #fff;
}
"""

if '.nav__mobile-whatsapp' not in css:
    css += WA_CSS
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)
    print("  ✓ WhatsApp CSS added")
else:
    print("  — WhatsApp CSS already present")


# ------------------------------------------------------------------
# ABOUT US page
# ------------------------------------------------------------------
print("\n=== Creating about/index.html ===")

about_dir = os.path.join(BASE, 'about')
os.makedirs(about_dir, exist_ok=True)

about_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>About Us | YK Wellness — West London</title>
  <meta name="description" content="About YK Wellness — over 400 five-star reviews, expert therapists and personalised treatments at Westway Sports Centre, West London." />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=DM+Sans:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <link rel="icon" href="../LOGOYKW.png" type="image/png" />
  <link rel="stylesheet" href="../style.css" />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="https://saturnresults.github.io/about/" />
  <meta property="og:title" content="About Us | YK Wellness West London" />
  <meta property="og:description" content="Over 400 five-star reviews. Expert therapists. Personalised treatments at Westway Sports Centre, West London." />
  <meta property="og:image" content="https://saturnresults.github.io/Cover_IMAGE.jpg" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:image" content="https://saturnresults.github.io/Cover_IMAGE.jpg" />
</head>
<body>

<!-- NAVIGATION -->
<nav class="nav" id="nav">
  <div class="container">
    <div class="nav__inner">
      <a href="/" class="nav__logo"><img src="../LOGOYKW.png" alt="YK Wellness" class="nav__logo-img"></a>
      <div class="nav__links">
        <a href="/">Home</a>
        <div class="nav__dropdown">
          <a href="/massage-therapy/">Treatments &#9662;</a>
          <div class="nav__dropdown-menu">
            <a href="/massage-therapy/" class="nav__dropdown-item">
              <span class="nav__dropdown-item-title">All Massage Therapy</span>
              <span class="nav__dropdown-item-desc">View our full range of massage treatments</span>
            </a>
            <div class="nav__dropdown-divider"></div>
            <a href="/deep-tissue/" class="nav__dropdown-item">
              <span class="nav__dropdown-item-title">Deep Tissue Massage</span>
              <span class="nav__dropdown-item-desc">Relief for chronic tension &amp; deeper muscle layers</span>
            </a>
            <a href="/sports-massage/" class="nav__dropdown-item">
              <span class="nav__dropdown-item-title">Sports Massage</span>
              <span class="nav__dropdown-item-desc">Performance, recovery &amp; injury prevention</span>
            </a>
            <a href="/swedish-massage/" class="nav__dropdown-item">
              <span class="nav__dropdown-item-title">Swedish Massage</span>
              <span class="nav__dropdown-item-desc">Full-body relaxation &amp; stress relief</span>
            </a>
            <a href="/cbd-massage/" class="nav__dropdown-item">
              <span class="nav__dropdown-item-title">CBD Massage</span>
              <span class="nav__dropdown-item-desc">Anti-inflammatory CBD oil combined with therapeutic massage</span>
            </a>
            <a href="/lymphatic-drainage/" class="nav__dropdown-item">
              <span class="nav__dropdown-item-title">Lymphatic Drainage</span>
              <span class="nav__dropdown-item-desc">Gentle rhythmic massage to stimulate the lymphatic system</span>
            </a>
          </div>
        </div>
        <a href="/specialised-treatments/">Specialised Treatments</a>
        <a href="/osteopathy/">Osteopathy</a>
        <div class="nav__dropdown">
          <a href="/about/">About &#9662;</a>
          <div class="nav__dropdown-menu">
            <a href="/about/" class="nav__dropdown-item">
              <span class="nav__dropdown-item-title">About Us</span>
              <span class="nav__dropdown-item-desc">Our story, values and approach to wellness</span>
            </a>
            <a href="/team/" class="nav__dropdown-item">
              <span class="nav__dropdown-item-title">Meet the Team</span>
              <span class="nav__dropdown-item-desc">The therapists and practitioners behind YK Wellness</span>
            </a>
          </div>
        </div>
        <a href="/contact/">Contact</a>
      </div>
      <a href="{FRESHA}" target="_blank" class="btn btn-primary nav__cta">Book Now</a>
      <button class="nav__hamburger" id="hamburger" aria-label="Open menu">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</nav>

<!-- MOBILE NAV OVERLAY -->
<div class="nav__mobile-overlay" id="mobileOverlay"></div>

<!-- MOBILE NAV DRAWER -->
<div class="nav__mobile" id="mobileNav">
  <div class="nav__mobile-header">
    <a href="/"><img src="../LOGOYKW.png" alt="YK Wellness" class="nav__mobile-logo"></a>
    <a href="{WA}" class="nav__mobile-whatsapp" aria-label="WhatsApp" target="_blank">{WA_SVG}</a>
    <button class="nav__mobile-close" id="mobileClose" aria-label="Close menu">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
    </button>
  </div>
  <div class="nav__mobile-body">
    <a href="/" class="nav__mobile-link">Home</a>
    <div class="nav__mobile-accordion" id="treatmentsAccordion">
      <button class="nav__mobile-accordion-trigger">
        Treatments
        <svg class="nav__mobile-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg>
      </button>
      <div class="nav__mobile-accordion-body">
        <a href="/massage-therapy/" class="nav__mobile-sub-link">All Massage Therapy</a>
        <a href="/deep-tissue/" class="nav__mobile-sub-link">Deep Tissue Massage</a>
        <a href="/sports-massage/" class="nav__mobile-sub-link">Sports Massage</a>
        <a href="/swedish-massage/" class="nav__mobile-sub-link">Swedish Massage</a>
        <a href="/cbd-massage/" class="nav__mobile-sub-link">CBD Massage</a>
        <a href="/lymphatic-drainage/" class="nav__mobile-sub-link">Lymphatic Drainage</a>
      </div>
    </div>
    <a href="/specialised-treatments/" class="nav__mobile-link">Specialised Treatments</a>
    <a href="/osteopathy/" class="nav__mobile-link">Osteopathy</a>
    <div class="nav__mobile-accordion" id="aboutAccordion">
      <button class="nav__mobile-accordion-trigger">
        About
        <svg class="nav__mobile-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg>
      </button>
      <div class="nav__mobile-accordion-body">
        <a href="/about/" class="nav__mobile-sub-link">About Us</a>
        <a href="/team/" class="nav__mobile-sub-link">Meet the Team</a>
      </div>
    </div>
    <a href="/contact/" class="nav__mobile-link">Contact</a>
  </div>
  <div class="nav__mobile-footer">
    <a href="{FRESHA}" target="_blank" class="btn btn-primary">Book Appointment</a>
  </div>
</div>

<div class="page-hero" style="background:linear-gradient(135deg,#1a0f08,#2d1c10);">
  <div class="container page-hero__content">
    <p class="eyebrow">West London's Trusted Clinic</p>
    <h1>About YK Wellness</h1>
    <p>Over 400 five-star reviews on Fresha and 140 on Google. A clinic built on genuine expertise, personalised care, and a relentless commitment to results.</p>
    <div class="page-hero__actions">
      <a href="{FRESHA}" target="_blank" class="btn btn-primary">Book an Appointment</a>
      <a href="/team/" class="btn btn-outline" style="color:#fff;border-color:rgba(255,255,255,0.35);">Meet the Team</a>
    </div>
  </div>
</div>

<!-- WHO WE ARE -->
<section class="bg-white">
  <div class="container">
    <div class="intro-split">
      <div class="intro-split__visual">
        <div class="intro-split__box" style="background:linear-gradient(135deg,#2a1a0e,#3d2a18);display:flex;align-items:center;justify-content:center;">
          <img src="../LOGOYKW.png" alt="YK Wellness" style="width:80%;height:auto;object-fit:contain;padding:1rem;" />
        </div>
        <div class="intro-split__badge">
          <div class="intro-split__badge-num">400+</div>
          <div class="intro-split__badge-label">five-star reviews</div>
        </div>
      </div>
      <div class="intro-split__text fade-up">
        <p class="eyebrow">Our Story</p>
        <div class="divider"></div>
        <h2>West London's top-rated wellness clinic</h2>
        <p>YK Wellness is a top-rated massage, osteopathy and wellness clinic with over 400 five-star reviews on Fresha and 140 on Google. We have built our reputation not through marketing, but through results — through clients who come back, and who send their friends.</p>
        <p>Every member of our team has trained at prestigious institutions and continues to advance their skills through ongoing professional development. Our practitioners specialise in various therapeutic disciplines, from advanced massage techniques to osteopathy and sports therapy.</p>
        <p>What sets our team apart is their commitment to personalised care — taking time to understand each client's unique needs before crafting a bespoke treatment plan. We do not believe in one-size-fits-all therapy. Every body is different, every presentation is different, and every session reflects that.</p>
        <div style="background:var(--sage-light);border-radius:var(--radius-md);padding:1.25rem 1.5rem;margin:1.5rem 0;border-left:3px solid var(--sage);">
          <p style="font-style:italic;font-size:1.05rem;color:var(--charcoal);margin:0;">"I only work with practitioners I would want to be treated by."</p>
          <p style="font-size:0.82rem;color:var(--mid);margin:0.5rem 0 0;font-weight:600;text-transform:uppercase;letter-spacing:0.06em;">YK Wellness founder</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- WHAT WE DO -->
<section class="bg-ivory">
  <div class="container--narrow">
    <div class="section-header section-header--center fade-up">
      <p class="eyebrow">What We Do</p>
      <div class="divider divider--center"></div>
      <h2>Bespoke treatments built around you</h2>
    </div>
    <div class="fade-up" style="max-width:700px;margin:0 auto;text-align:center;">
      <p>Over the years, we have become known for creating bespoke massage treatments and personalised therapy plans, individually tailored to suit each client's needs on the day of their visit. For this reason, our appointments typically begin with a brief consultation, allowing clients to share their expectations, health conditions, areas of pain or tension, or any other relevant information while the therapist provides their professional recommendations.</p>
      <p>We offer a range of disciplines, from the deeply relaxing Swedish Massage and the general Deep Tissue Massage to the more clinical Sports Massage, Remedial Massage and Osteopathy for injury recovery and pain relief. Our high recruitment standards ensure that our clients are always in expert hands.</p>
    </div>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:1.5rem;margin-top:3rem;" class="fade-up">
      <div style="text-align:center;padding:2rem 1.5rem;background:var(--white);border-radius:var(--radius-lg);border:1px solid var(--sand);">
        <div style="font-size:2.5rem;margin-bottom:1rem;">💆</div>
        <h4 style="margin-bottom:0.5rem;">Massage Therapy</h4>
        <p style="font-size:0.88rem;">Deep tissue, sports, Swedish, CBD and lymphatic drainage — each performed to the highest clinical standard.</p>
        <a href="/massage-therapy/" style="font-size:0.85rem;color:var(--sage-dark);font-weight:600;">View treatments &rarr;</a>
      </div>
      <div style="text-align:center;padding:2rem 1.5rem;background:var(--white);border-radius:var(--radius-lg);border:1px solid var(--sand);">
        <div style="font-size:2.5rem;margin-bottom:1rem;">🦴</div>
        <h4 style="margin-bottom:0.5rem;">Osteopathy</h4>
        <p style="font-size:0.88rem;">Structural, hands-on treatment addressing the root cause of pain and dysfunction — not just the symptom.</p>
        <a href="/osteopathy/" style="font-size:0.85rem;color:var(--sage-dark);font-weight:600;">Learn more &rarr;</a>
      </div>
      <div style="text-align:center;padding:2rem 1.5rem;background:var(--white);border-radius:var(--radius-lg);border:1px solid var(--sand);">
        <div style="font-size:2.5rem;margin-bottom:1rem;">⚡</div>
        <h4 style="margin-bottom:0.5rem;">Specialised Treatments</h4>
        <p style="font-size:0.88rem;">Cupping, dry needling, CBD massage and lymphatic drainage — advanced therapies for complex presentations.</p>
        <a href="/specialised-treatments/" style="font-size:0.85rem;color:var(--sage-dark);font-weight:600;">Explore &rarr;</a>
      </div>
    </div>
  </div>
</section>

<!-- FIND US -->
<section class="bg-white">
  <div class="container">
    <div class="intro-split" style="direction:rtl;">
      <div class="intro-split__visual" style="direction:ltr;">
        <div class="intro-split__box" style="background:linear-gradient(135deg,#1a2030,#2a3545);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:0.5rem;color:rgba(255,255,255,0.9);padding:2rem;">
          <div style="font-size:3rem;margin-bottom:0.5rem;">📍</div>
          <div style="font-weight:700;font-size:1.1rem;text-align:center;">Westway Sports &amp; Fitness Centre</div>
          <div style="font-size:0.9rem;text-align:center;opacity:0.8;">1 Crowthorne Road<br>London W10 6RP</div>
          <div style="font-size:0.8rem;margin-top:0.5rem;opacity:0.7;text-align:center;">Latimer Road &amp; White City Tube<br>Ample free parking available</div>
        </div>
      </div>
      <div class="intro-split__text fade-up" style="direction:ltr;">
        <p class="eyebrow">Find Us</p>
        <div class="divider"></div>
        <h2>Convenient, accessible, purpose-built</h2>
        <p>We are trusted by clients seeking bespoke massage treatments across West London. Conveniently located just minutes from Latimer Road and White City Tube Stations (Circle and Hammersmith &amp; City lines) and the renowned Westfield Shopping Centre, we are easily accessible from across London.</p>
        <p>Our purpose-built treatment rooms are situated within the popular Westway Sports &amp; Fitness Centre and feature facilities specifically designed for massage and osteopathy treatments. Plenty of parking is available for those driving to their appointment.</p>
        <p>All our practitioners hold qualifications from some of the most prestigious massage and osteopathy schools in the UK and worldwide, and each maintains active membership of their relevant professional bodies.</p>
        <div style="display:flex;gap:0.75rem;flex-wrap:wrap;margin-top:1.5rem;">
          <a href="{FRESHA}" target="_blank" class="btn btn-primary">Book Online</a>
          <a href="/contact/" class="btn btn-outline">Get in Touch</a>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- FAQ -->
<section class="bg-ivory">
  <div class="container--narrow">
    <div class="section-header section-header--center fade-up">
      <p class="eyebrow">FAQ</p>
      <div class="divider divider--center"></div>
      <h2>Common questions</h2>
    </div>
    <div class="faq-list fade-up">
      <div class="faq-item">
        <div class="faq-question">What qualifications do your therapists hold?
          <svg width="20" height="20" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M12 4v16m8-8H4"/></svg>
        </div>
        <div class="faq-answer"><p>Every practitioner at YK Wellness holds professional qualifications from recognised and prestigious institutions. All therapists maintain ongoing continuing professional development and are registered with their relevant professional bodies. We have consistently high recruitment standards — we only work with practitioners we would personally want to be treated by.</p></div>
      </div>
      <div class="faq-item">
        <div class="faq-question">How long are your treatment sessions?
          <svg width="20" height="20" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M12 4v16m8-8H4"/></svg>
        </div>
        <div class="faq-answer"><p>Sessions typically last between 30 and 90 minutes depending on the treatment and your specific needs. Each appointment begins with a brief consultation so your therapist can understand your goals and tailor the session accordingly. The consultation time is included within your booked appointment.</p></div>
      </div>
      <div class="faq-item">
        <div class="faq-question">Do you treat non-sports injuries and general wellness?
          <svg width="20" height="20" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M12 4v16m8-8H4"/></svg>
        </div>
        <div class="faq-answer"><p>Absolutely. While we specialise in sports and therapeutic massage, a significant proportion of our clients come to us for stress relief, relaxation, postural work, office-related tension, and general wellness maintenance. You do not need a sports injury or medical condition to benefit from our treatments.</p></div>
      </div>
      <div class="faq-item">
        <div class="faq-question">Is parking available?
          <svg width="20" height="20" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M12 4v16m8-8H4"/></svg>
        </div>
        <div class="faq-answer"><p>Yes — Westway Sports Centre has ample on-site parking, which is free to use when visiting for a treatment. The centre is also a short walk from Latimer Road Tube Station (Circle and Hammersmith &amp; City lines) and accessible from White City as well.</p></div>
      </div>
      <div class="faq-item">
        <div class="faq-question">How do I book?
          <svg width="20" height="20" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M12 4v16m8-8H4"/></svg>
        </div>
        <div class="faq-answer"><p>Booking is available online through Fresha, where you can view availability, select your preferred practitioner, and schedule appointments at your convenience. You can also contact us directly by phone, email, or WhatsApp and we will be happy to help you find the right appointment.</p></div>
      </div>
    </div>
  </div>
</section>

<div class="cta-band">
  <div class="container">
    <p class="eyebrow" style="color:rgba(255,255,255,0.6);margin-bottom:0.75rem;">West London's trusted clinic.</p>
    <h2>Book your appointment today</h2>
    <p>Over 400 five-star reviews and counting. Find out why our clients keep coming back.</p>
    <div style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;">
      <a href="{FRESHA}" target="_blank" class="btn btn-white">Book Online Now</a>
      <a href="/team/" class="btn btn-outline" style="color:#fff;border-color:rgba(255,255,255,0.4);">Meet the Team</a>
    </div>
  </div>
</div>

<footer>
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <a href="/" class="footer-logo"><img src="../LOGOYKW.png" alt="YK Wellness" style="height:56px;width:auto;"></a>
        <p>Expert massage therapy and osteopathy in West London. Bespoke treatments at Westway Sports Centre, tailored to your individual needs.</p>
        <div class="footer-social">
          <a href="#" class="social-btn" aria-label="Facebook">
            <svg viewBox="0 0 24 24"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg>
          </a>
          <a href="https://www.instagram.com/ykwellness/" target="_blank" class="social-btn" aria-label="Instagram">
            <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
          </a>
          <a href="{WA}" class="social-btn" aria-label="WhatsApp">
            <svg viewBox="0 0 24 24"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>
          </a>
        </div>
      </div>
      <div class="footer-col">
        <h5>Treatments</h5>
        <ul>
          <li><a href="/deep-tissue/">Deep Tissue Massage</a></li>
          <li><a href="/sports-massage/">Sports Massage</a></li>
          <li><a href="/swedish-massage/">Swedish Massage</a></li>
          <li><a href="/osteopathy/">Osteopathy</a></li>
          <li><a href="/specialised-treatments/">Cupping Therapy</a></li>
          <li><a href="/specialised-treatments/">Dry Needling</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h5>Information</h5>
        <ul>
          <li><a href="/about/">About Us</a></li>
          <li><a href="/team/">Meet the Team</a></li>
          <li><a href="/massage-therapy/">All Treatments</a></li>
          <li><a href="/contact/">Contact Us</a></li>
          <li><a href="{FRESHA}" target="_blank">Book Online</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h5>Contact</h5>
        <ul>
          <li><a href="tel:07910007933">07910 007933</a></li>
          <li><a href="mailto:hello@ykwellness.co.uk">hello@ykwellness.co.uk</a></li>
          <li><a href="#">Westway Sports Centre</a></li>
          <li><a href="#">1 Crowthorne Road, W10 6RP</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2025 The Wellness Well Ltd trading as YK Wellness. Company Reg. 12345040.</span>
      <div style="display:flex;gap:1.5rem;">
        <a href="/privacy-policy/">Privacy Policy</a>
        <a href="/terms/">Terms &amp; Conditions</a>
      </div>
    </div>
  </div>
</footer>
<!-- BACK TO TOP -->
<button class="back-to-top" id="backToTop" aria-label="Back to top">
  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="18 15 12 9 6 15"/></svg>
</button>
<script src="../main.js"></script>
</body>
</html>"""

with open(os.path.join(about_dir, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(about_html)
print("  ✓ about/index.html created")

print("\n=== All done ===")
