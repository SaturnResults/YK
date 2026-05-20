#!/usr/bin/env python3
"""
YK Wellness full site restructure:
  - Convert all .html pages to directory/index.html (clean URLs)
  - Update nav: CBD + Lymphatic in dropdown, Specialised Treatments standalone
  - Update footer: proper /privacy-policy/ and /terms/ links
  - Update all internal links to absolute /page/ paths
  - Create new pages: cbd-massage, lymphatic-drainage, privacy-policy, terms
  - Update specialised-treatments cards with Read More buttons
  - Update main.js: clean-URL active nav + quiz links
"""

import os, re

BASE = "/Users/harrybingham/Desktop/New Folder With Items 2/Buisness Mac/Saturn Results/Claud/YK WELLNESS OFFICIAL SITE"

FRESHA = "https://www.fresha.com/a/yk-wellness-london-westway-sports-fitness-centre-uk-1-crowthorne-road-git4ohyh"

# -----------------------------------------------------------------------
# NAV BLOCK  (prefix = '' for root, '../' for subdirs)
# -----------------------------------------------------------------------
def nav_block(prefix='../'):
    return f"""<!-- NAVIGATION -->
<nav class="nav" id="nav">
  <div class="container">
    <div class="nav__inner">
      <a href="/" class="nav__logo"><img src="{prefix}LOGOYKW.png" alt="YK Wellness" class="nav__logo-img"></a>
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
        <a href="/team/">Our Team</a>
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
    <a href="/"><img src="{prefix}LOGOYKW.png" alt="YK Wellness" class="nav__mobile-logo"></a>
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
    <a href="/team/" class="nav__mobile-link">Our Team</a>
    <a href="/contact/" class="nav__mobile-link">Contact</a>
  </div>
  <div class="nav__mobile-footer">
    <a href="{FRESHA}" target="_blank" class="btn btn-primary">Book Appointment</a>
  </div>
</div>"""

# -----------------------------------------------------------------------
# FOOTER BLOCK  (prefix = '' for root, '../' for subdirs)
# -----------------------------------------------------------------------
def footer_block(prefix='../'):
    return f"""<footer>
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <a href="/" class="footer-logo"><img src="{prefix}LOGOYKW.png" alt="YK Wellness" style="height:56px;width:auto;"></a>
        <p>Expert massage therapy and osteopathy in West London. Bespoke treatments at Westway Sports Centre, tailored to your individual needs.</p>
        <div class="footer-social">
          <a href="#" class="social-btn" aria-label="Facebook">
            <svg viewBox="0 0 24 24"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg>
          </a>
          <a href="https://www.instagram.com/ykwellness/" target="_blank" class="social-btn" aria-label="Instagram">
            <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
          </a>
          <a href="https://api.whatsapp.com/send/?phone=%2B447910007933&text&type=phone_number&app_absent=0" class="social-btn" aria-label="WhatsApp">
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
</footer>"""

# -----------------------------------------------------------------------
# TRANSFORM: apply to any existing page's HTML
# -----------------------------------------------------------------------

# Exact old desktop nav links (identical on every existing page)
OLD_NAV_LINKS = """      <div class="nav__links">
        <a href="index.html">Home</a>
        <div class="nav__dropdown">
          <a href="massage-therapy.html">Treatments &#9662;</a>
          <div class="nav__dropdown-menu">
            <a href="massage-therapy.html" class="nav__dropdown-item">
              <span class="nav__dropdown-item-title">All Massage Therapy</span>
              <span class="nav__dropdown-item-desc">View our full range of massage treatments</span>
            </a>
            <div class="nav__dropdown-divider"></div>
            <a href="deep-tissue.html" class="nav__dropdown-item">
              <span class="nav__dropdown-item-title">Deep Tissue Massage</span>
              <span class="nav__dropdown-item-desc">Relief for chronic tension &amp; deeper muscle layers</span>
            </a>
            <a href="sports-massage.html" class="nav__dropdown-item">
              <span class="nav__dropdown-item-title">Sports Massage</span>
              <span class="nav__dropdown-item-desc">Performance, recovery &amp; injury prevention</span>
            </a>
            <a href="swedish-massage.html" class="nav__dropdown-item">
              <span class="nav__dropdown-item-title">Swedish Massage</span>
              <span class="nav__dropdown-item-desc">Full-body relaxation &amp; stress relief</span>
            </a>
            <a href="specialised-treatments.html" class="nav__dropdown-item">
              <span class="nav__dropdown-item-title">Specialised Treatments</span>
              <span class="nav__dropdown-item-desc">CBD massage, cupping, dry needling &amp; more</span>
            </a>
          </div>
        </div>
        <a href="osteopathy.html">Osteopathy</a>
        <a href="team.html">Our Team</a>
        <a href="contact.html">Contact</a>
      </div>"""

NEW_NAV_LINKS = """      <div class="nav__links">
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
        <a href="/team/">Our Team</a>
        <a href="/contact/">Contact</a>
      </div>"""

OLD_MOBILE_BODY = """  <div class="nav__mobile-body">
    <a href="index.html" class="nav__mobile-link">Home</a>
    <div class="nav__mobile-accordion" id="treatmentsAccordion">
      <button class="nav__mobile-accordion-trigger">
        Treatments
        <svg class="nav__mobile-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg>
      </button>
      <div class="nav__mobile-accordion-body">
        <a href="massage-therapy.html" class="nav__mobile-sub-link">All Massage Therapy</a>
        <a href="deep-tissue.html" class="nav__mobile-sub-link">Deep Tissue Massage</a>
        <a href="sports-massage.html" class="nav__mobile-sub-link">Sports Massage</a>
        <a href="swedish-massage.html" class="nav__mobile-sub-link">Swedish Massage</a>
        <a href="specialised-treatments.html" class="nav__mobile-sub-link">Specialised Treatments</a>
      </div>
    </div>
    <a href="osteopathy.html" class="nav__mobile-link">Osteopathy</a>
    <a href="team.html" class="nav__mobile-link">Our Team</a>
    <a href="contact.html" class="nav__mobile-link">Contact</a>
  </div>"""

NEW_MOBILE_BODY = """  <div class="nav__mobile-body">
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
    <a href="/team/" class="nav__mobile-link">Our Team</a>
    <a href="/contact/" class="nav__mobile-link">Contact</a>
  </div>"""


def transform(content, is_subdir=False):
    """Apply all transformations to a page's HTML."""
    prefix = '../' if is_subdir else ''

    # --- Nav desktop links ---
    if OLD_NAV_LINKS in content:
        content = content.replace(OLD_NAV_LINKS, NEW_NAV_LINKS)
    else:
        print("  WARNING: OLD_NAV_LINKS not found — nav links NOT updated")

    # --- Nav desktop logo link ---
    content = content.replace('href="index.html" class="nav__logo"', 'href="/" class="nav__logo"')

    # --- Mobile nav logo href ---
    content = content.replace(
        '<a href="index.html"><img src="LOGOYKW.png" alt="YK Wellness" class="nav__mobile-logo">',
        '<a href="/"><img src="LOGOYKW.png" alt="YK Wellness" class="nav__mobile-logo">'
    )

    # --- Mobile nav body ---
    if OLD_MOBILE_BODY in content:
        content = content.replace(OLD_MOBILE_BODY, NEW_MOBILE_BODY)
    else:
        print("  WARNING: OLD_MOBILE_BODY not found — mobile nav NOT updated")

    # --- All internal .html links in body / footer ---
    link_map = [
        ('href="index.html"',              'href="/"'),
        ('href="massage-therapy.html"',    'href="/massage-therapy/"'),
        ('href="deep-tissue.html"',        'href="/deep-tissue/"'),
        ('href="sports-massage.html"',     'href="/sports-massage/"'),
        ('href="swedish-massage.html"',    'href="/swedish-massage/"'),
        ('href="specialised-treatments.html"', 'href="/specialised-treatments/"'),
        ('href="osteopathy.html"',         'href="/osteopathy/"'),
        ('href="team.html"',               'href="/team/"'),
        ('href="contact.html"',            'href="/contact/"'),
        # OG URL cleanup
        ('.github.io/massage-therapy.html',    '.github.io/massage-therapy/'),
        ('.github.io/deep-tissue.html',        '.github.io/deep-tissue/'),
        ('.github.io/sports-massage.html',     '.github.io/sports-massage/'),
        ('.github.io/swedish-massage.html',    '.github.io/swedish-massage/'),
        ('.github.io/specialised-treatments.html', '.github.io/specialised-treatments/'),
        ('.github.io/osteopathy.html',         '.github.io/osteopathy/'),
        ('.github.io/team.html',               '.github.io/team/'),
        ('.github.io/contact.html',            '.github.io/contact/'),
    ]
    for old, new in link_map:
        content = content.replace(old, new)

    # --- Footer privacy / terms links ---
    content = content.replace('<a href="#">Privacy Policy</a>', '<a href="/privacy-policy/">Privacy Policy</a>')
    content = content.replace('<a href="#">Terms &amp; Conditions</a>', '<a href="/terms/">Terms &amp; Conditions</a>')

    # --- Asset paths for subdirectory pages ---
    if is_subdir:
        content = content.replace('href="style.css"',           f'href="{prefix}style.css"')
        content = content.replace('src="main.js"',              f'src="{prefix}main.js"')
        content = content.replace('href="LOGOYKW.png" type="image/png"', f'href="{prefix}LOGOYKW.png" type="image/png"')
        content = content.replace('src="LOGOYKW.png"',          f'src="{prefix}LOGOYKW.png"')

    return content


def process_existing(src_filename, dest_dir=None):
    src_path = os.path.join(BASE, src_filename)
    with open(src_path, 'r', encoding='utf-8') as f:
        content = f.read()

    is_subdir = (dest_dir is not None)
    content = transform(content, is_subdir=is_subdir)

    if dest_dir:
        dest = os.path.join(BASE, dest_dir)
        os.makedirs(dest, exist_ok=True)
        out_path = os.path.join(dest, 'index.html')
    else:
        out_path = src_path

    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  OK  {out_path}")


# -----------------------------------------------------------------------
# PAGE HEAD / FOOT helpers for NEW pages
# -----------------------------------------------------------------------

def head(title, description, og_path, og_title, og_desc, prefix='../'):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{description}" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=DM+Sans:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <link rel="icon" href="{prefix}LOGOYKW.png" type="image/png" />
  <link rel="stylesheet" href="{prefix}style.css" />
  <!-- Open Graph / WhatsApp preview -->
  <meta property="og:type" content="website" />
  <meta property="og:url" content="https://saturnresults.github.io{og_path}" />
  <meta property="og:title" content="{og_title}" />
  <meta property="og:description" content="{og_desc}" />
  <meta property="og:image" content="https://saturnresults.github.io/Cover_IMAGE.jpg" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:image" content="https://saturnresults.github.io/Cover_IMAGE.jpg" />
</head>
<body>"""

def script_tag(prefix='../'):
    return f'<script src="{prefix}main.js"></script>'

def cookie_banner():
    return """<!-- COOKIE BANNER -->
<div class="cookie-banner" id="cookieBanner">
  <p>We use cookies to improve your experience. By continuing to use this site, you accept our <a href="/privacy-policy/">privacy policy</a>.</p>
  <div class="cookie-banner__actions">
    <button id="cookieAccept" class="btn btn-primary" style="font-size:0.82rem;padding:0.5rem 1.2rem;">Accept</button>
    <button id="cookieDecline" class="btn btn-outline" style="font-size:0.82rem;padding:0.5rem 1.2rem;color:#fff;border-color:rgba(255,255,255,0.35);">Decline</button>
  </div>
</div>"""

def back_to_top():
    return """<!-- BACK TO TOP -->
<button class="back-to-top" id="backToTop" aria-label="Back to top">
  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="18 15 12 9 6 15"/></svg>
</button>"""

# -----------------------------------------------------------------------
# CBD MASSAGE PAGE
# -----------------------------------------------------------------------

cbd_page = head(
    title="CBD Massage | YK Wellness — West London",
    description="CBD massage therapy using premium THC-free CBD oil in West London. Anti-inflammatory, deeply relaxing and entirely legal. Book at Westway Sports Centre.",
    og_path="/cbd-massage/",
    og_title="CBD Massage | YK Wellness West London",
    og_desc="Premium THC-free CBD massage for anti-inflammatory relief and deep relaxation at Westway Sports Centre, West London.",
) + "\n" + nav_block('../') + """

<div class="page-hero" style="background:linear-gradient(135deg,#0d1a10,#1e3a22);">
  <div class="container page-hero__content">
    <p class="eyebrow">Specialised Treatment</p>
    <h1>CBD Massage</h1>
    <p>Expert therapeutic massage combined with premium, THC-free CBD oil — delivering deeper anti-inflammatory relief, accelerated recovery, and a level of relaxation that conventional massage alone cannot achieve.</p>
    <div class="page-hero__actions">
      <a href="https://www.fresha.com/a/yk-wellness-london-westway-sports-fitness-centre-uk-1-crowthorne-road-git4ohyh" target="_blank" class="btn btn-primary">Book an Appointment</a>
      <a href="/contact/" class="btn btn-outline" style="color:#fff;border-color:rgba(255,255,255,0.35);">Ask a Question</a>
    </div>
  </div>
</div>

<!-- WHAT IS IT -->
<section class="bg-white">
  <div class="container">
    <div class="intro-split">
      <div class="intro-split__visual">
        <div class="intro-split__box" style="background:linear-gradient(135deg,#1e3a22,#2d5c30);display:flex;align-items:center;justify-content:center;font-size:5rem;">🌿</div>
        <div class="intro-split__badge">
          <div class="intro-split__badge-num">CBD</div>
          <div class="intro-split__badge-label">pricing on enquiry</div>
        </div>
      </div>
      <div class="intro-split__text fade-up">
        <p class="eyebrow">The Treatment</p>
        <div class="divider"></div>
        <h2>Cannabidiol massage — what it actually does</h2>
        <p>CBD massage integrates high-quality, THC-free cannabidiol oil into a skilled therapeutic massage session. CBD — short for cannabidiol — is a naturally occurring compound derived from the hemp plant. Unlike THC, it has no psychoactive effect whatsoever. What it does have is a growing body of clinical research behind its anti-inflammatory and analgesic properties.</p>
        <p>When applied topically during massage, CBD absorbs through the skin and interacts with the endocannabinoid receptors present in muscle tissue, fascia, and nerve endings. The result is a measurably deeper reduction in inflammation and muscle tension than massage alone — particularly valuable for chronic pain conditions, sports recovery, and stress-related tightness.</p>
        <p>At YK Wellness we use only lab-tested, licensed CBD products that meet strict quality standards. Every session is tailored to your specific needs and concerns.</p>

        <div style="background:var(--sage-light);border-radius:var(--radius-md);padding:1.5rem;margin:1.5rem 0;">
          <h4 style="font-family:var(--font-sans);font-size:0.82rem;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;color:var(--sage-dark);margin-bottom:0.8rem;">CBD massage can help with…</h4>
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:0.4rem;">
            <span style="font-size:0.9rem;color:var(--charcoal);">✓ Chronic pain &amp; arthritis</span>
            <span style="font-size:0.9rem;color:var(--charcoal);">✓ Muscle tension &amp; soreness</span>
            <span style="font-size:0.9rem;color:var(--charcoal);">✓ Sports recovery</span>
            <span style="font-size:0.9rem;color:var(--charcoal);">✓ Stress &amp; anxiety</span>
            <span style="font-size:0.9rem;color:var(--charcoal);">✓ Inflammation &amp; fibromyalgia</span>
            <span style="font-size:0.9rem;color:var(--charcoal);">✓ Sleep difficulties</span>
          </div>
        </div>

        <p style="font-size:0.9rem;color:var(--light);margin-bottom:1.5rem;">Pricing on enquiry — contact us for details.</p>
        <a href="/contact/" class="btn btn-primary">Enquire About CBD Massage</a>
      </div>
    </div>
  </div>
</section>

<!-- WHO IS IT FOR -->
<section class="bg-ivory">
  <div class="container--narrow">
    <div class="section-header section-header--center fade-up">
      <p class="eyebrow">Who It Suits</p>
      <div class="divider divider--center"></div>
      <h2>Natural relief for body and mind</h2>
      <p>CBD massage is suitable for most adults and particularly effective for:</p>
    </div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;margin-top:2rem;" class="fade-up">
      <div style="background:var(--white);border-radius:var(--radius-md);padding:1.75rem;border:1px solid var(--sand);">
        <div style="font-size:2rem;margin-bottom:1rem;">💪</div>
        <h4 style="margin-bottom:0.5rem;">Active individuals &amp; athletes</h4>
        <p style="font-size:0.9rem;">CBD's anti-inflammatory properties make it a powerful addition to any recovery routine. Reduce post-training soreness faster and get back to training sooner.</p>
      </div>
      <div style="background:var(--white);border-radius:var(--radius-md);padding:1.75rem;border:1px solid var(--sand);">
        <div style="font-size:2rem;margin-bottom:1rem;">🧘</div>
        <h4 style="margin-bottom:0.5rem;">Stress, anxiety &amp; poor sleep</h4>
        <p style="font-size:0.9rem;">CBD has calming properties that work alongside the parasympathetic relaxation response triggered by massage — making this an especially effective combination for those carrying stress in the body.</p>
      </div>
      <div style="background:var(--white);border-radius:var(--radius-md);padding:1.75rem;border:1px solid var(--sand);">
        <div style="font-size:2rem;margin-bottom:1rem;">🦴</div>
        <h4 style="margin-bottom:0.5rem;">Chronic pain conditions</h4>
        <p style="font-size:0.9rem;">Those managing arthritis, fibromyalgia, or persistent muscular pain often find CBD massage offers relief that outlasts a standard treatment, due to the sustained anti-inflammatory action of the oil.</p>
      </div>
      <div style="background:var(--white);border-radius:var(--radius-md);padding:1.75rem;border:1px solid var(--sand);">
        <div style="font-size:2rem;margin-bottom:1rem;">🌱</div>
        <h4 style="margin-bottom:0.5rem;">Natural wellness seekers</h4>
        <p style="font-size:0.9rem;">If you prefer plant-based, non-pharmaceutical approaches to wellness and recovery, CBD massage offers a clinically supported option that aligns with that philosophy.</p>
      </div>
    </div>
  </div>
</section>

<!-- FAQ -->
<section class="bg-white">
  <div class="container--narrow">
    <div class="section-header section-header--center fade-up">
      <p class="eyebrow">FAQ</p>
      <div class="divider divider--center"></div>
      <h2>Common questions</h2>
    </div>
    <div class="faq-list fade-up">
      <div class="faq-item">
        <div class="faq-question">Will CBD massage make me feel "high"?
          <svg width="20" height="20" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M12 4v16m8-8H4"/></svg>
        </div>
        <div class="faq-answer"><p>No, not at all. The CBD products we use are completely THC-free. THC is the psychoactive compound in cannabis — CBD is an entirely different compound and has no mind-altering effect whatsoever. You will feel relaxed after your treatment, but that is the massage, not any intoxicating effect.</p></div>
      </div>
      <div class="faq-item">
        <div class="faq-question">Is CBD massage legal?
          <svg width="20" height="20" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M12 4v16m8-8H4"/></svg>
        </div>
        <div class="faq-answer"><p>Completely. All of our CBD products are licensed, lab-tested, and fully compliant with UK law. CBD derived from hemp (which our products are) is entirely legal in the United Kingdom, provided THC content is within the permitted trace limits — which ours is.</p></div>
      </div>
      <div class="faq-item">
        <div class="faq-question">How quickly will I notice the benefits?
          <svg width="20" height="20" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M12 4v16m8-8H4"/></svg>
        </div>
        <div class="faq-answer"><p>Many clients notice immediate relaxation and reduced muscle tension during and directly after the treatment. The anti-inflammatory effects develop over the following hours and can continue to work for a day or two after the session — so CBD massage often feels more effective the morning after than right when you leave.</p></div>
      </div>
      <div class="faq-item">
        <div class="faq-question">Can I drive after a CBD massage?
          <svg width="20" height="20" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M12 4v16m8-8H4"/></svg>
        </div>
        <div class="faq-answer"><p>Yes, completely. With zero THC there is no motor function impairment of any kind. You may feel pleasantly relaxed after your treatment — as you would after any good massage — but there is absolutely no psychoactive effect that would affect your ability to drive.</p></div>
      </div>
      <div class="faq-item">
        <div class="faq-question">Which conditions benefit most from CBD massage?
          <svg width="20" height="20" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M12 4v16m8-8H4"/></svg>
        </div>
        <div class="faq-answer"><p>CBD massage tends to deliver the greatest additional benefit for those dealing with chronic pain, arthritis, fibromyalgia, persistent muscle tension, stress, anxiety, inflammation, and sleep difficulties. For straightforward relaxation, a Swedish massage may be equally effective — CBD massage really shines for those with ongoing physical complaints.</p></div>
      </div>
    </div>
  </div>
</section>

<div class="cta-band">
  <div class="container">
    <p class="eyebrow" style="color:rgba(255,255,255,0.6);margin-bottom:0.75rem;">Deeper relief. Natural recovery.</p>
    <h2>Book a CBD massage today</h2>
    <p>Not sure if CBD massage is right for you? Get in touch and we will talk you through it — no obligation, no pressure.</p>
    <div style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;">
      <a href="/contact/" class="btn btn-white">Enquire Now</a>
      <a href="/specialised-treatments/" class="btn btn-outline" style="color:#fff;border-color:rgba(255,255,255,0.4);">All Specialised Treatments</a>
    </div>
  </div>
</div>

""" + footer_block('../') + "\n" + back_to_top() + "\n" + cookie_banner() + "\n" + script_tag('../') + """
</body>
</html>"""

# -----------------------------------------------------------------------
# LYMPHATIC DRAINAGE PAGE
# -----------------------------------------------------------------------

lymph_page = head(
    title="Lymphatic Drainage Massage | YK Wellness — West London",
    description="Manual lymphatic drainage massage in West London. Reduce swelling, support post-surgical recovery and boost immunity at Westway Sports Centre.",
    og_path="/lymphatic-drainage/",
    og_title="Lymphatic Drainage Massage | YK Wellness West London",
    og_desc="Gentle manual lymphatic drainage at Westway Sports Centre, West London. Reduce swelling, support recovery and detoxify naturally.",
) + "\n" + nav_block('../') + """

<div class="page-hero" style="background:linear-gradient(135deg,#0d1820,#1a2e42);">
  <div class="container page-hero__content">
    <p class="eyebrow">Specialised Treatment</p>
    <h1>Lymphatic Drainage</h1>
    <p>Gentle, rhythmic massage following the natural pathways of the lymphatic system — supporting detoxification, reducing swelling, boosting immunity, and promoting full-body healing at a cellular level.</p>
    <div class="page-hero__actions">
      <a href="https://www.fresha.com/a/yk-wellness-london-westway-sports-fitness-centre-uk-1-crowthorne-road-git4ohyh" target="_blank" class="btn btn-primary">Book an Appointment</a>
      <a href="/contact/" class="btn btn-outline" style="color:#fff;border-color:rgba(255,255,255,0.35);">Ask a Question</a>
    </div>
  </div>
</div>

<!-- WHAT IS IT -->
<section class="bg-white">
  <div class="container">
    <div class="intro-split">
      <div class="intro-split__visual">
        <div class="intro-split__box" style="background:linear-gradient(135deg,#1a2e42,#2a4a6b);display:flex;align-items:center;justify-content:center;font-size:5rem;">💧</div>
        <div class="intro-split__badge">
          <div class="intro-split__badge-num">MLD</div>
          <div class="intro-split__badge-label">pricing on enquiry</div>
        </div>
      </div>
      <div class="intro-split__text fade-up">
        <p class="eyebrow">The Treatment</p>
        <div class="divider"></div>
        <h2>Manual lymphatic drainage — how it works</h2>
        <p>Manual lymphatic drainage (MLD) is a highly specialised form of gentle massage that works with — rather than against — the body's own lymphatic system. Unlike traditional massage techniques that target muscle tissue with pressure and depth, MLD uses very light, rhythmic strokes that follow the precise anatomical pathways of the lymphatic vessels just beneath the skin.</p>
        <p>The lymphatic system is the body's primary waste disposal network, responsible for removing toxins, excess fluid, cellular debris, and pathogens. When it becomes sluggish or overwhelmed — through illness, injury, surgery, or simply inactivity — fluid can accumulate in the tissues, resulting in swelling, puffiness, fatigue, and reduced immune function.</p>
        <p>MLD uses gentle, directional strokes to manually stimulate lymphatic flow, encouraging the movement of stagnant lymph fluid back into circulation. Sessions are deeply relaxing despite the light touch — many clients fall asleep during treatment.</p>

        <div style="background:var(--sage-light);border-radius:var(--radius-md);padding:1.5rem;margin:1.5rem 0;">
          <h4 style="font-family:var(--font-sans);font-size:0.82rem;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;color:var(--sage-dark);margin-bottom:0.8rem;">Lymphatic drainage can help with…</h4>
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:0.4rem;">
            <span style="font-size:0.9rem;color:var(--charcoal);">✓ Post-surgical swelling</span>
            <span style="font-size:0.9rem;color:var(--charcoal);">✓ Lymphoedema</span>
            <span style="font-size:0.9rem;color:var(--charcoal);">✓ Chronic fatigue</span>
            <span style="font-size:0.9rem;color:var(--charcoal);">✓ Immune support</span>
            <span style="font-size:0.9rem;color:var(--charcoal);">✓ Fluid retention</span>
            <span style="font-size:0.9rem;color:var(--charcoal);">✓ Detoxification</span>
          </div>
        </div>

        <p style="font-size:0.9rem;color:var(--light);margin-bottom:1.5rem;">Pricing on enquiry — contact us for details.</p>
        <a href="/contact/" class="btn btn-primary">Enquire About Lymphatic Drainage</a>
      </div>
    </div>
  </div>
</section>

<!-- AFTER SURGERY / IMPORTANT INFO -->
<section class="bg-ivory">
  <div class="container--narrow">
    <div class="section-header section-header--center fade-up">
      <p class="eyebrow">Who It Suits</p>
      <div class="divider divider--center"></div>
      <h2>Supporting recovery and long-term wellness</h2>
    </div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;margin-top:2rem;" class="fade-up">
      <div style="background:var(--white);border-radius:var(--radius-md);padding:1.75rem;border:1px solid var(--sand);">
        <div style="font-size:2rem;margin-bottom:1rem;">🏥</div>
        <h4 style="margin-bottom:0.5rem;">Post-surgical recovery</h4>
        <p style="font-size:0.9rem;">Lymphatic drainage is widely recommended after cosmetic and orthopaedic surgery to reduce post-operative swelling, bruising and discomfort, and to accelerate the healing process. It can be adapted to work safely around surgical sites.</p>
      </div>
      <div style="background:var(--white);border-radius:var(--radius-md);padding:1.75rem;border:1px solid var(--sand);">
        <div style="font-size:2rem;margin-bottom:1rem;">🤒</div>
        <h4 style="margin-bottom:0.5rem;">Lymphoedema management</h4>
        <p style="font-size:0.9rem;">For those living with lymphoedema — chronic swelling resulting from lymphatic damage or removal of lymph nodes — regular MLD is one of the primary treatment methods recommended by the medical community alongside compression therapy.</p>
      </div>
      <div style="background:var(--white);border-radius:var(--radius-md);padding:1.75rem;border:1px solid var(--sand);">
        <div style="font-size:2rem;margin-bottom:1rem;">⚡</div>
        <h4 style="margin-bottom:0.5rem;">Chronic fatigue &amp; immunity</h4>
        <p style="font-size:0.9rem;">When the lymphatic system is not functioning efficiently, it often manifests as persistent fatigue, brain fog, and a tendency to pick up illness. MLD can help restore normal lymphatic activity, supporting immune function and energy levels.</p>
      </div>
      <div style="background:var(--white);border-radius:var(--radius-md);padding:1.75rem;border:1px solid var(--sand);">
        <div style="font-size:2rem;margin-bottom:1rem;">✨</div>
        <h4 style="margin-bottom:0.5rem;">General detoxification &amp; wellness</h4>
        <p style="font-size:0.9rem;">You do not need a diagnosed condition to benefit from lymphatic drainage. Regular sessions support the body's natural detoxification processes, reduce puffiness and fluid retention, and leave you feeling lighter, clearer and more energised.</p>
      </div>
    </div>
    <div style="background:var(--sage-light);border-radius:var(--radius-md);padding:1.5rem;margin-top:2rem;" class="fade-up">
      <h4 style="font-family:var(--font-sans);font-size:0.85rem;font-weight:700;letter-spacing:0.06em;text-transform:uppercase;color:var(--sage-dark);margin-bottom:0.6rem;">After your session</h4>
      <p style="font-size:0.9rem;margin:0;">Drink plenty of water after your treatment. Hydration is important — the lymphatic system depends on adequate fluid intake to transport lymph effectively, and drinking water after your session will enhance and prolong the detoxification benefits.</p>
    </div>
  </div>
</section>

<!-- FAQ -->
<section class="bg-white">
  <div class="container--narrow">
    <div class="section-header section-header--center fade-up">
      <p class="eyebrow">FAQ</p>
      <div class="divider divider--center"></div>
      <h2>Common questions</h2>
    </div>
    <div class="faq-list fade-up">
      <div class="faq-item">
        <div class="faq-question">How is this different from a regular massage?
          <svg width="20" height="20" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M12 4v16m8-8H4"/></svg>
        </div>
        <div class="faq-answer"><p>Lymphatic drainage uses a very light, almost feather-light touch with specific directional strokes that follow the lymphatic pathways just under the skin. Traditional massage targets muscle tissue with firm pressure — MLD works at a completely different level of the body. It can feel deceptively gentle, but the effects on swelling and fluid balance can be significant.</p></div>
      </div>
      <div class="faq-item">
        <div class="faq-question">Is it safe during pregnancy?
          <svg width="20" height="20" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M12 4v16m8-8H4"/></svg>
        </div>
        <div class="faq-answer"><p>Yes, with appropriate adaptations. Lymphatic drainage can be a helpful treatment during pregnancy, particularly for managing swelling and fluid retention in the legs and ankles. Please inform us during booking that you are pregnant so we can adapt the session accordingly and ensure it is appropriate for your stage of pregnancy.</p></div>
      </div>
      <div class="faq-item">
        <div class="faq-question">How often should I have treatment?
          <svg width="20" height="20" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M12 4v16m8-8H4"/></svg>
        </div>
        <div class="faq-answer"><p>For acute issues such as post-surgical swelling or significant fluid retention, weekly sessions are typically recommended until the condition stabilises. For general wellness maintenance, monthly sessions are usually sufficient. Your therapist will advise you on the most appropriate schedule for your specific situation.</p></div>
      </div>
      <div class="faq-item">
        <div class="faq-question">What will I feel like after treatment?
          <svg width="20" height="20" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M12 4v16m8-8H4"/></svg>
        </div>
        <div class="faq-answer"><p>Most clients feel deeply relaxed and energised after lymphatic drainage. Some experience a mild fatigue or heaviness for a few hours as the body processes the increased lymphatic activity — this is entirely normal and a sign the treatment is working. Drinking water after your session helps ease this and accelerates the detoxification process.</p></div>
      </div>
      <div class="faq-item">
        <div class="faq-question">What conditions benefit most?
          <svg width="20" height="20" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M12 4v16m8-8H4"/></svg>
        </div>
        <div class="faq-answer"><p>Lymphatic drainage delivers the most marked results for swelling, post-surgical recovery, lymphoedema, chronic fatigue, skin conditions (such as acne or rosacea with an inflammatory component), immune system support, and general detoxification. It can also help with fluid retention associated with hormonal changes.</p></div>
      </div>
    </div>
  </div>
</section>

<div class="cta-band">
  <div class="container">
    <p class="eyebrow" style="color:rgba(255,255,255,0.6);margin-bottom:0.75rem;">Support your body's natural healing.</p>
    <h2>Book a lymphatic drainage session today</h2>
    <p>Unsure whether lymphatic drainage is the right treatment for you? Get in touch and we will be happy to advise.</p>
    <div style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;">
      <a href="/contact/" class="btn btn-white">Enquire Now</a>
      <a href="/specialised-treatments/" class="btn btn-outline" style="color:#fff;border-color:rgba(255,255,255,0.4);">All Specialised Treatments</a>
    </div>
  </div>
</div>

""" + footer_block('../') + "\n" + back_to_top() + "\n" + cookie_banner() + "\n" + script_tag('../') + """
</body>
</html>"""

# -----------------------------------------------------------------------
# PRIVACY POLICY PAGE
# -----------------------------------------------------------------------

privacy_page = head(
    title="Privacy Policy | YK Wellness — West London",
    description="Privacy policy for YK Wellness (The Wellness Well Ltd). Learn how we collect, use and protect your personal data.",
    og_path="/privacy-policy/",
    og_title="Privacy Policy | YK Wellness",
    og_desc="Privacy policy for YK Wellness — The Wellness Well Ltd, Company No. 12345040.",
) + "\n" + nav_block('../') + """

<div class="page-hero" style="background:linear-gradient(135deg,#1a0f08,#2d1c10);">
  <div class="container page-hero__content">
    <p class="eyebrow">Legal</p>
    <h1>Privacy Policy</h1>
    <p>Last updated: October 2025</p>
  </div>
</div>

<section class="bg-white">
  <div class="container--narrow">
    <div style="max-width:760px;margin:0 auto;" class="fade-up">

      <div style="background:var(--sage-light);border-radius:var(--radius-md);padding:1.25rem 1.5rem;margin-bottom:2.5rem;">
        <p style="margin:0;font-size:0.9rem;"><strong>Company:</strong> THE WELLNESS WELL LTD &nbsp;|&nbsp; <strong>Trading as:</strong> YK Wellness &nbsp;|&nbsp; <strong>Reg. No:</strong> 12345040 &nbsp;|&nbsp; Registered in England and Wales &nbsp;|&nbsp; <a href="mailto:info@ykwellness.co.uk">info@ykwellness.co.uk</a></p>
      </div>

      <h2 style="font-size:1.4rem;margin-bottom:1rem;">Introduction</h2>
      <p>YK Wellness ("we," "our," or "us") is committed to protecting your privacy. This Privacy Policy explains how we collect, use, disclose, and safeguard your information when you visit our website or use our services. Please read this policy carefully. By using our website or services, you agree to the collection and use of information in accordance with this policy.</p>

      <h2 style="font-size:1.4rem;margin:2rem 0 1rem;">Information we collect</h2>
      <h3 style="font-size:1.1rem;margin-bottom:0.75rem;">Personal information you provide</h3>
      <p>When you book appointments, contact us, or use our services, we may collect:</p>
      <ul style="margin:0.75rem 0 1rem 1.25rem;line-height:1.8;">
        <li><strong>Contact information:</strong> name, email address, phone number, postal address</li>
        <li><strong>Health information:</strong> medical history, current conditions, injuries, allergies, medications, and other health-related information necessary for treatment</li>
        <li><strong>Booking information:</strong> appointment dates, times, service preferences, treatment history</li>
        <li><strong>Payment information:</strong> billing address and payment details (processed securely through third-party payment providers)</li>
        <li><strong>Communication records:</strong> correspondence with us via email, phone, or contact forms</li>
      </ul>
      <h3 style="font-size:1.1rem;margin-bottom:0.75rem;">Information automatically collected</h3>
      <p>When you visit our website, we may automatically collect device information (IP address, browser type, operating system), usage data (pages visited, time on pages, links clicked), and cookies. See the Cookie Policy section below.</p>

      <h2 style="font-size:1.4rem;margin:2rem 0 1rem;">How we use your information</h2>
      <p>We use the information we collect to deliver and tailor our services, manage appointments and send reminders, maintain accurate health records for safe treatment, respond to enquiries and provide customer support, process payments, send marketing communications (with your consent), comply with legal obligations, and improve our website.</p>

      <h2 style="font-size:1.4rem;margin:2rem 0 1rem;">Legal basis for processing (UK GDPR)</h2>
      <p>We process your personal data based on: your consent; the performance of our service agreement; legal obligations; and our legitimate business interests (where these do not override your rights). For health information, we rely on your explicit consent and our obligations as healthcare providers.</p>

      <h2 style="font-size:1.4rem;margin:2rem 0 1rem;">Sharing your information</h2>
      <p>We do not sell your personal information. We may share it with:</p>
      <ul style="margin:0.75rem 0 1rem 1.25rem;line-height:1.8;">
        <li><strong>Booking platforms:</strong> Fresha, Treatwell (for appointment scheduling)</li>
        <li><strong>Payment processors:</strong> secure third-party payment gateway providers</li>
        <li><strong>Email and hosting services:</strong> technical service providers who help us operate our business</li>
        <li><strong>Legal requirements:</strong> where required by law, to protect our rights or safety, or to prevent fraud</li>
        <li><strong>Other healthcare providers:</strong> with your explicit consent, or where required by professional standards</li>
      </ul>

      <h2 style="font-size:1.4rem;margin:2rem 0 1rem;">Data retention</h2>
      <ul style="margin:0.75rem 0 1rem 1.25rem;line-height:1.8;">
        <li><strong>Health records:</strong> minimum 8 years from last treatment</li>
        <li><strong>Financial records:</strong> 6 years (for tax and accounting purposes)</li>
        <li><strong>Marketing consent:</strong> until you withdraw consent</li>
      </ul>
      <p>After these periods, we securely delete or anonymise your information.</p>

      <h2 style="font-size:1.4rem;margin:2rem 0 1rem;">Your rights under UK GDPR</h2>
      <p>You have the right to access, rectify, erase, restrict, or port your personal data, to object to processing, and to withdraw consent at any time. You also have the right to complain to the Information Commissioner's Office (ICO) at <a href="https://ico.org.uk" target="_blank">ico.org.uk</a> or on 0303 123 1113. To exercise any of these rights, contact us at <a href="mailto:info@ykwellness.co.uk">info@ykwellness.co.uk</a>.</p>

      <h2 style="font-size:1.4rem;margin:2rem 0 1rem;">Cookie policy</h2>
      <p>Cookies are small text files stored on your device. We use:</p>
      <ul style="margin:0.75rem 0 1rem 1.25rem;line-height:1.8;">
        <li><strong>Essential cookies:</strong> required for the website to function (session management, security)</li>
        <li><strong>Analytics cookies:</strong> Google Analytics (anonymised data) to understand how our site is used</li>
        <li><strong>Functional cookies:</strong> to remember your preferences</li>
        <li><strong>Marketing cookies (with consent):</strong> social media integration and conversion tracking</li>
      </ul>
      <p>You can control cookies through your browser settings or our cookie consent tool. Blocking essential cookies may affect website functionality.</p>

      <h2 style="font-size:1.4rem;margin:2rem 0 1rem;">Data security</h2>
      <p>We implement appropriate technical and organisational measures including SSL/TLS encryption, access controls, secure storage, regular security audits, and staff training. However, no transmission or storage method is 100% secure.</p>

      <h2 style="font-size:1.4rem;margin:2rem 0 1rem;">Children's privacy</h2>
      <p>Our services are not intended for individuals under 16. We do not knowingly collect information from children. If you believe we have, please contact us and we will delete it promptly.</p>

      <h2 style="font-size:1.4rem;margin:2rem 0 1rem;">Changes to this policy</h2>
      <p>We may update this Privacy Policy periodically. Changes will be posted on this page with an updated date. Your continued use of our services after changes constitutes acceptance.</p>

      <h2 style="font-size:1.4rem;margin:2rem 0 1rem;">Contact us</h2>
      <p><strong>THE WELLNESS WELL LTD</strong> trading as YK Wellness<br>
      Company No. 12345040<br>
      Email: <a href="mailto:info@ykwellness.co.uk">info@ykwellness.co.uk</a><br>
      Westway Sports &amp; Fitness Centre, 1 Crowthorne Road, London W10 6RP</p>

    </div>
  </div>
</section>

""" + footer_block('../') + "\n" + script_tag('../') + """
</body>
</html>"""

# -----------------------------------------------------------------------
# TERMS & CONDITIONS PAGE
# -----------------------------------------------------------------------

terms_page = head(
    title="Terms & Conditions | YK Wellness — West London",
    description="Terms of use for YK Wellness (The Wellness Well Ltd). Booking terms, cancellation policy, and website terms of use.",
    og_path="/terms/",
    og_title="Terms & Conditions | YK Wellness",
    og_desc="Terms of use for YK Wellness — The Wellness Well Ltd, Company No. 12345040.",
) + "\n" + nav_block('../') + """

<div class="page-hero" style="background:linear-gradient(135deg,#1a0f08,#2d1c10);">
  <div class="container page-hero__content">
    <p class="eyebrow">Legal</p>
    <h1>Terms &amp; Conditions</h1>
    <p>Last updated: October 2025</p>
  </div>
</div>

<section class="bg-white">
  <div class="container--narrow">
    <div style="max-width:760px;margin:0 auto;" class="fade-up">

      <div style="background:var(--sage-light);border-radius:var(--radius-md);padding:1.25rem 1.5rem;margin-bottom:2.5rem;">
        <p style="margin:0;font-size:0.9rem;"><strong>Company:</strong> THE WELLNESS WELL LTD &nbsp;|&nbsp; <strong>Trading as:</strong> YK Wellness &nbsp;|&nbsp; <strong>Reg. No:</strong> 12345040 &nbsp;|&nbsp; Registered in England and Wales &nbsp;|&nbsp; <a href="mailto:info@ykwellness.co.uk">info@ykwellness.co.uk</a></p>
      </div>

      <h2 style="font-size:1.4rem;margin-bottom:1rem;">Introduction</h2>
      <p>Welcome to the YK Wellness website. These Terms of Use govern your access to and use of our website and services. By accessing or using our website, you agree to be bound by these Terms. If you do not agree, please do not use our website or services.</p>

      <h2 style="font-size:1.4rem;margin:2rem 0 1rem;">Booking and appointments</h2>
      <p>Appointments can be booked through our website, authorised third-party platforms (Fresha, Treatwell), or directly by phone or email. When booking, you must provide accurate and complete information, disclose any relevant health conditions, be at least 18 years old (or have parental or guardian consent), and agree to our cancellation and payment terms.</p>
      <p>You must inform us of any current medical conditions or injuries, allergies or sensitivities, medications you are taking, previous surgeries, pregnancy or recent childbirth, and any other factors that may affect treatment safety. Failure to disclose relevant health information may affect the safety and effectiveness of your treatment.</p>

      <h2 style="font-size:1.4rem;margin:2rem 0 1rem;">Cancellation policy</h2>
      <div style="background:var(--ivory);border-radius:var(--radius-md);padding:1.5rem;border:1px solid var(--sand);margin:1rem 0 1.5rem;">
        <ul style="margin:0;padding-left:1.25rem;line-height:2;">
          <li>A minimum of <strong>24 hours' notice</strong> is required for cancellations or changes to appointments.</li>
          <li>Cancellations with less than 24 hours' notice may incur a <strong>50% charge</strong>.</li>
          <li>Failure to attend without notice may result in a <strong>100% charge</strong>.</li>
          <li>Repeated no-shows may result in booking privileges being suspended.</li>
        </ul>
      </div>
      <p>We may cancel or reschedule appointments due to practitioner illness, facility issues, or circumstances beyond our control. In such cases we will notify you as soon as possible, offer alternative appointment times, and provide a full refund if rescheduling is not suitable.</p>

      <h2 style="font-size:1.4rem;margin:2rem 0 1rem;">Payment terms</h2>
      <p>Prices are displayed on our website and booking platforms in British Pounds (GBP) and include VAT where applicable. Payment is typically required at the time of booking or service and is processed securely through third-party providers. We do not store full payment card details. Prices may change without notice, though this will not affect existing confirmed bookings.</p>
      <p>Refunds are provided for cancellations made within our policy terms, if we cancel your appointment, or in exceptional circumstances at our discretion. Refunds are processed within 5 to 10 business days.</p>

      <h2 style="font-size:1.4rem;margin:2rem 0 1rem;">Nature of our services</h2>
      <p>Our services are delivered by qualified massage therapists, osteopaths, and sports therapists. Treatments are tailored to individual client needs based on professional assessment and are subject to practitioner discretion.</p>
      <p>Our services are complementary wellness treatments. We do not diagnose medical conditions, and our services do not replace medical care or advice. We recommend consulting a healthcare professional for medical concerns. We may decline to carry out a treatment if we believe medical care is more appropriate.</p>
      <p>While we strive for the best results, individual outcomes vary and we cannot guarantee specific results. Some conditions may require multiple sessions to respond, and some may not respond to our treatments.</p>

      <h2 style="font-size:1.4rem;margin:2rem 0 1rem;">Use of our website</h2>
      <p>You may use our website to browse information about our services, book appointments, contact us, and access educational content. You must not use the website for unlawful purposes, attempt to gain unauthorised access to our systems, transmit viruses or harmful code, scrape or reproduce content without permission, or interfere with the website's functionality or security.</p>

      <h2 style="font-size:1.4rem;margin:2rem 0 1rem;">Intellectual property</h2>
      <p>All content on this website — including text, images, graphics, logos, branding, design, and multimedia — is owned by or licensed to THE WELLNESS WELL LTD and is protected by copyright and other intellectual property laws. You may view content for personal, non-commercial purposes and share links on social media. You may not copy, reproduce, or use our content or branding for commercial purposes without permission.</p>

      <h2 style="font-size:1.4rem;margin:2rem 0 1rem;">Limitation of liability</h2>
      <p>Our website is provided "as is" without warranties. To the fullest extent permitted by law, our liability is limited to the amount paid for the service in question. We are not liable for indirect, consequential, or incidental damages, or for losses caused by factors beyond our control. Nothing in these Terms excludes liability for death or personal injury caused by negligence, fraud, or any other liability that cannot be excluded by law.</p>

      <h2 style="font-size:1.4rem;margin:2rem 0 1rem;">Client conduct</h2>
      <p>When attending appointments, please arrive on time, follow practitioner instructions, treat staff and other clients with respect and courtesy, and follow facility rules at Westway Sports &amp; Fitness Centre. We reserve the right to refuse service or terminate treatment if conduct is unacceptable, and to ban clients who violate our policies.</p>

      <h2 style="font-size:1.4rem;margin:2rem 0 1rem;">Complaints</h2>
      <p>If you are unhappy with our service, please contact us at <a href="mailto:info@ykwellness.co.uk">info@ykwellness.co.uk</a>. We aim to acknowledge complaints promptly and resolve them within 14 days. We encourage informal resolution through communication before any formal action is taken.</p>

      <h2 style="font-size:1.4rem;margin:2rem 0 1rem;">Governing law</h2>
      <p>These Terms are governed by the laws of England and Wales. Any disputes will be subject to the exclusive jurisdiction of the courts of England and Wales.</p>

      <h2 style="font-size:1.4rem;margin:2rem 0 1rem;">Changes to these terms</h2>
      <p>We may update these Terms periodically. Changes will be posted on this page with an updated date. Your continued use of our website after changes constitutes acceptance of the new Terms.</p>

      <h2 style="font-size:1.4rem;margin:2rem 0 1rem;">Contact us</h2>
      <p><strong>THE WELLNESS WELL LTD</strong> trading as YK Wellness<br>
      Company No. 12345040<br>
      Email: <a href="mailto:info@ykwellness.co.uk">info@ykwellness.co.uk</a><br>
      Westway Sports &amp; Fitness Centre, 1 Crowthorne Road, London W10 6RP</p>

    </div>
  </div>
</section>

""" + footer_block('../') + "\n" + script_tag('../') + """
</body>
</html>"""

# -----------------------------------------------------------------------
# MAIN — run all transformations
# -----------------------------------------------------------------------

def write_new_page(dir_name, html_content):
    dest = os.path.join(BASE, dir_name)
    os.makedirs(dest, exist_ok=True)
    out = os.path.join(dest, 'index.html')
    with open(out, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"  CREATED  {out}")


print("\n=== 1. Transform existing pages ===")
PAGES = [
    ('index.html',                   None),               # root — stays in place
    ('massage-therapy.html',         'massage-therapy'),
    ('deep-tissue.html',             'deep-tissue'),
    ('sports-massage.html',          'sports-massage'),
    ('swedish-massage.html',         'swedish-massage'),
    ('specialised-treatments.html',  'specialised-treatments'),
    ('osteopathy.html',              'osteopathy'),
    ('team.html',                    'team'),
    ('contact.html',                 'contact'),
]
for src, dest in PAGES:
    print(f"  Processing {src} ...")
    process_existing(src, dest)

print("\n=== 2. Create new pages ===")
write_new_page('cbd-massage',       cbd_page)
write_new_page('lymphatic-drainage', lymph_page)
write_new_page('privacy-policy',    privacy_page)
write_new_page('terms',             terms_page)

print("\n=== 3. Update specialised-treatments: add Read More buttons ===")
sp_path = os.path.join(BASE, 'specialised-treatments', 'index.html')
with open(sp_path, 'r', encoding='utf-8') as f:
    sp = f.read()

# Replace the CBD card footer
OLD_CBD_BTN = '<a href="/contact/" class="btn btn-outline">Enquire Now</a>\n      </div>'
NEW_CBD_BTN = """<div style="display:flex;gap:0.75rem;flex-wrap:wrap;">
          <a href="/cbd-massage/" class="btn btn-primary">Read More</a>
          <a href="/contact/" class="btn btn-outline">Enquire Now</a>
        </div>
      </div>"""
if OLD_CBD_BTN in sp:
    # Only replace first occurrence (CBD card)
    sp = sp.replace(OLD_CBD_BTN, NEW_CBD_BTN, 1)
    print("  CBD card updated")
else:
    print("  WARNING: CBD card button not found (may already be updated)")

# Replace the Lymphatic card footer
OLD_LYMPH_BTN = '<a href="/contact/" class="btn btn-outline">Enquire Now</a>\n      </div>\n    </div>'
NEW_LYMPH_BTN = """<div style="display:flex;gap:0.75rem;flex-wrap:wrap;">
          <a href="/lymphatic-drainage/" class="btn btn-primary">Read More</a>
          <a href="/contact/" class="btn btn-outline">Enquire Now</a>
        </div>
      </div>
    </div>"""
if OLD_LYMPH_BTN in sp:
    sp = sp.replace(OLD_LYMPH_BTN, NEW_LYMPH_BTN, 1)
    print("  Lymphatic card updated")
else:
    print("  WARNING: Lymphatic card button not found (may already be updated)")

with open(sp_path, 'w', encoding='utf-8') as f:
    f.write(sp)
print(f"  Saved {sp_path}")

print("\n=== 4. Update main.js ===")
js_path = os.path.join(BASE, 'main.js')
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Quiz treatment links
js_replacements = [
    ("link: 'deep-tissue.html'",     "link: '/deep-tissue/'"),
    ("link: 'swedish-massage.html'", "link: '/swedish-massage/'"),
    ("link: 'sports-massage.html'",  "link: '/sports-massage/'"),
    ("link: 'osteopathy.html'",      "link: '/osteopathy/'"),
]
for old, new in js_replacements:
    js = js.replace(old, new)

# Active nav logic — replace old function with new path-based version
OLD_ACTIVE_NAV = """// Set active nav link
(function () {
  const currentPage = location.pathname.split('/').pop() || 'index.html';
  const treatmentPages = ['massage-therapy.html', 'deep-tissue.html', 'sports-massage.html',
                          'swedish-massage.html', 'specialised-treatments.html'];

  // Mark direct links active
  document.querySelectorAll('.nav__links > a').forEach(a => {
    if (a.getAttribute('href') === currentPage) a.classList.add('active');
  });

  // Mark the Treatments dropdown trigger active if on any treatment sub-page
  if (treatmentPages.includes(currentPage)) {
    const trigger = document.querySelector('.nav__dropdown > a');
    if (trigger) trigger.classList.add('active');
    // Auto-open accordion in mobile drawer
    document.getElementById('treatmentsAccordion')?.classList.add('open');
  }
})();"""

NEW_ACTIVE_NAV = """// Set active nav link (clean URL version)
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

if OLD_ACTIVE_NAV in js:
    js = js.replace(OLD_ACTIVE_NAV, NEW_ACTIVE_NAV)
    print("  Active nav JS updated")
else:
    print("  WARNING: old active nav block not found — skipping")

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)
print(f"  Saved {js_path}")

print("\n=== All done! ===")
print("New directories created:")
for d in ['massage-therapy','deep-tissue','sports-massage','swedish-massage',
          'specialised-treatments','osteopathy','team','contact',
          'cbd-massage','lymphatic-drainage','privacy-policy','terms']:
    p = os.path.join(BASE, d, 'index.html')
    exists = os.path.exists(p)
    print(f"  {'OK' if exists else 'MISSING'}  {d}/index.html")
