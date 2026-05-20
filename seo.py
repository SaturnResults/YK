#!/usr/bin/env python3
"""
SEO pass — YK Wellness
Adds: canonical URLs, JSON-LD schema, better titles/descriptions,
      fixed OG tags, robots.txt, sitemap.xml
"""
import os, re, glob, json

BASE   = "/Users/harrybingham/Desktop/New Folder With Items 2/Buisness Mac/Saturn Results/Claud/YK WELLNESS OFFICIAL SITE"
DOMAIN = "https://ykwellness.co.uk"
IMG    = f"{DOMAIN}/Cover_IMAGE.jpg"

# ── Page-level SEO data ──────────────────────────────────────────────
PAGES = {
    "index.html": {
        "path":  "/",
        "title": "Massage Therapy & Osteopathy West London | YK Wellness",
        "desc":  "Expert massage therapy and osteopathy at Westway Sports Centre, West London. Deep tissue, sports, Swedish, CBD massage. 400+ five-star reviews. Book online.",
        "schema_type": "home",
    },
    "massage-therapy/index.html": {
        "path":  "/massage-therapy/",
        "title": "Massage Therapy West London | Deep Tissue, Sports & Swedish | YK Wellness",
        "desc":  "Professional massage therapy in West London. Deep tissue, sports, Swedish, CBD and lymphatic drainage at Westway Sports Centre, W10. Same-week appointments.",
        "schema_type": "service",
        "service_name": "Massage Therapy",
        "service_desc": "Professional massage therapy including deep tissue, sports, Swedish, CBD and lymphatic drainage massage at Westway Sports Centre, West London.",
    },
    "deep-tissue/index.html": {
        "path":  "/deep-tissue/",
        "title": "Deep Tissue Massage West London | Chronic Pain Relief | YK Wellness",
        "desc":  "Deep tissue massage at Westway Sports Centre, W10. Relieve chronic back pain, neck tension and muscle tightness. Expert therapists. 400+ five-star reviews. Book now.",
        "schema_type": "service",
        "service_name": "Deep Tissue Massage",
        "service_desc": "Deep tissue massage targeting chronic muscle tension, back pain and postural issues at Westway Sports Centre, West London.",
        "has_faq": True,
    },
    "sports-massage/index.html": {
        "path":  "/sports-massage/",
        "title": "Sports Massage West London | Injury Recovery & Performance | YK Wellness",
        "desc":  "Sports massage in West London. Accelerate recovery, prevent injury and improve performance at Westway Sports Centre, W10. Book online today.",
        "schema_type": "service",
        "service_name": "Sports Massage",
        "service_desc": "Sports massage for injury recovery, prevention and athletic performance at Westway Sports Centre, West London.",
        "has_faq": True,
    },
    "swedish-massage/index.html": {
        "path":  "/swedish-massage/",
        "title": "Swedish Massage West London | Relaxation & Stress Relief | YK Wellness",
        "desc":  "Swedish massage in West London at Westway Sports Centre. Full-body relaxation, improved circulation and stress relief. Expert therapists. Book online.",
        "schema_type": "service",
        "service_name": "Swedish Massage",
        "service_desc": "Swedish massage for full-body relaxation, stress relief and improved circulation at Westway Sports Centre, West London.",
        "has_faq": True,
    },
    "cbd-massage/index.html": {
        "path":  "/cbd-massage/",
        "title": "CBD Massage London | Anti-Inflammatory Therapy | YK Wellness West London",
        "desc":  "CBD massage therapy using premium THC-free CBD oil at Westway Sports Centre, West London. Anti-inflammatory, deeply relaxing. Book online today.",
        "schema_type": "service",
        "service_name": "CBD Massage",
        "service_desc": "CBD massage therapy using premium THC-free CBD oil for anti-inflammatory relief and deep relaxation at Westway Sports Centre, West London.",
    },
    "lymphatic-drainage-massage/index.html": {
        "path":  "/lymphatic-drainage-massage/",
        "title": "Lymphatic Drainage Massage London | Post-Surgery Recovery | YK Wellness",
        "desc":  "Manual lymphatic drainage in West London. Reduce swelling, support post-surgical recovery and boost immunity at Westway Sports Centre, W10. Book online.",
        "schema_type": "service",
        "service_name": "Lymphatic Drainage Massage",
        "service_desc": "Manual lymphatic drainage massage for swelling reduction, post-surgical recovery and immune support at Westway Sports Centre, West London.",
    },
    "osteopathy/index.html": {
        "path":  "/osteopathy/",
        "title": "Osteopath West London | GOsC Registered | YK Wellness Westway",
        "desc":  "GOsC-registered osteopaths in West London at Westway Sports Centre, W10. Hands-on structural treatment for back pain, neck pain and injury. Book online.",
        "schema_type": "service",
        "service_name": "Osteopathy",
        "service_desc": "GOsC-registered osteopathy for back pain, neck pain, joint issues and injury at Westway Sports Centre, West London.",
        "has_faq": True,
    },
    "specialised-treatments/index.html": {
        "path":  "/specialised-treatments/",
        "title": "Cupping & Dry Needling West London | Specialised Treatments | YK Wellness",
        "desc":  "Cupping therapy, dry needling, CBD massage and lymphatic drainage in West London. Advanced specialised treatments at Westway Sports Centre, W10.",
        "schema_type": "service",
        "service_name": "Specialised Treatments",
        "service_desc": "Specialised treatments including cupping therapy, dry needling, CBD massage and lymphatic drainage at Westway Sports Centre, West London.",
    },
    "about-us/index.html": {
        "path":  "/about-us/",
        "title": "About YK Wellness | Massage & Osteopathy West London",
        "desc":  "YK Wellness — West London's top-rated massage and osteopathy clinic. 400+ five-star Fresha reviews. Expert therapists at Westway Sports Centre, W10.",
        "schema_type": "about",
    },
    "contact-us/index.html": {
        "path":  "/contact-us/",
        "title": "Book Massage West London | Contact YK Wellness | Westway Sports Centre",
        "desc":  "Book a massage or osteopathy appointment at YK Wellness, Westway Sports Centre, West London. Call 07910 007933 or book online via Fresha. Free parking.",
        "schema_type": "contact",
    },
    "team/index.html": {
        "path":  "/team/",
        "title": "Meet the Team | Expert Therapists West London | YK Wellness",
        "desc":  "Meet the expert massage therapists and osteopaths at YK Wellness, Westway Sports Centre, West London. Fully qualified, experienced and highly rated.",
        "schema_type": "about",
    },
}

# ── Shared JSON-LD: LocalBusiness (injected on every page) ──────────
def local_biz_schema(page_url):
    return {
        "@context": "https://schema.org",
        "@type": ["HealthAndBeautyBusiness", "MassageTherapist"],
        "@id": f"{DOMAIN}/#business",
        "name": "YK Wellness",
        "description": "Expert massage therapy and osteopathy clinic in West London, offering deep tissue, sports, Swedish, CBD and lymphatic drainage massage, plus osteopathy and specialised treatments.",
        "url": DOMAIN,
        "telephone": "+447910007933",
        "email": "hello@ykwellness.co.uk",
        "image": IMG,
        "priceRange": "££",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "Westway Sports and Fitness Centre, 1 Crowthorne Road",
            "addressLocality": "London",
            "postalCode": "W10 6RP",
            "addressCountry": "GB"
        },
        "geo": {
            "@type": "GeoCoordinates",
            "latitude": 51.5162,
            "longitude": -0.2226
        },
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": "4.9",
            "reviewCount": "400",
            "bestRating": "5"
        },
        "sameAs": [
            "https://www.instagram.com/ykwellness/",
            "https://www.facebook.com/ykwellness.london/"
        ],
        "hasMap": "https://maps.google.com/?q=Westway+Sports+Centre+1+Crowthorne+Road+London+W10+6RP"
    }

def service_schema(page_url, service_name, service_desc):
    return {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": service_name,
        "description": service_desc,
        "url": page_url,
        "provider": {
            "@type": "HealthAndBeautyBusiness",
            "@id": f"{DOMAIN}/#business",
            "name": "YK Wellness"
        },
        "areaServed": {
            "@type": "City",
            "name": "London"
        },
        "serviceType": service_name,
        "availableChannel": {
            "@type": "ServiceChannel",
            "serviceUrl": "https://www.fresha.com/a/yk-wellness-london-westway-sports-fitness-centre-uk-1-crowthorne-road-git4ohyh"
        }
    }

def build_schema_block(page_data, page_url):
    schemas = [local_biz_schema(page_url)]
    if page_data.get("schema_type") == "service":
        schemas.append(service_schema(
            page_url,
            page_data.get("service_name", ""),
            page_data.get("service_desc", "")
        ))
    lines = []
    for s in schemas:
        lines.append(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>')
    return "\n  ".join(lines)

def extract_faq_items(html):
    """Pull question/answer pairs from faq-question / faq-answer divs."""
    pairs = []
    questions = re.findall(r'class="faq-question"[^>]*>(.*?)<svg', html, re.DOTALL)
    answers   = re.findall(r'class="faq-answer"><p>(.*?)</p>', html, re.DOTALL)
    for q, a in zip(questions, answers):
        q = re.sub(r'<[^>]+>', '', q).strip()
        a = re.sub(r'<[^>]+>', '', a).strip()
        if q and a:
            pairs.append({"@type": "Question",
                          "name": q,
                          "acceptedAnswer": {"@type": "Answer", "text": a}})
    return pairs

# ── Process each page ───────────────────────────────────────────────
print("=== SEO pass ===")
for rel_path, data in PAGES.items():
    path = os.path.join(BASE, rel_path)
    if not os.path.exists(path):
        print(f"  ! MISSING: {rel_path}")
        continue
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    page_url = DOMAIN + data["path"]

    # 1. Title
    html = re.sub(r'<title>.*?</title>', f'<title>{data["title"]}</title>', html)

    # 2. Meta description
    html = re.sub(
        r'<meta name="description" content="[^"]*"',
        f'<meta name="description" content="{data["desc"]}"',
        html
    )

    # 3. Canonical
    if 'rel="canonical"' not in html:
        html = html.replace(
            '<meta name="description"',
            f'<link rel="canonical" href="{page_url}" />\n  <meta name="description"'
        )
    else:
        html = re.sub(r'<link rel="canonical" href="[^"]*"', f'<link rel="canonical" href="{page_url}"', html)

    # 4. OG tags — update url, title, description, image
    html = re.sub(r'<meta property="og:url" content="[^"]*"',
                  f'<meta property="og:url" content="{page_url}"', html)
    html = re.sub(r'<meta property="og:title" content="[^"]*"',
                  f'<meta property="og:title" content="{data["title"]}"', html)
    html = re.sub(r'<meta property="og:description" content="[^"]*"',
                  f'<meta property="og:description" content="{data["desc"]}"', html)
    html = re.sub(r'<meta property="og:image" content="[^"]*"',
                  f'<meta property="og:image" content="{IMG}"', html)

    # If OG tags are missing entirely, add them
    if 'og:url' not in html:
        og_block = f'''  <meta property="og:type" content="website" />
  <meta property="og:url" content="{page_url}" />
  <meta property="og:title" content="{data['title']}" />
  <meta property="og:description" content="{data['desc']}" />
  <meta property="og:image" content="{IMG}" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />'''
        html = html.replace('</head>', og_block + '\n</head>')

    # 5. Remove old schema, insert new
    html = re.sub(r'\s*<script type="application/ld\+json">.*?</script>', '', html, flags=re.DOTALL)

    schema_block = build_schema_block(data, page_url)

    # FAQ schema
    if data.get("has_faq"):
        faq_items = extract_faq_items(html)
        if faq_items:
            faq_schema = {"@context": "https://schema.org", "@type": "FAQPage",
                          "mainEntity": faq_items}
            schema_block += f'\n  <script type="application/ld+json">{json.dumps(faq_schema, ensure_ascii=False)}</script>'

    html = html.replace('</head>', f'  {schema_block}\n</head>')

    # 6. Add twitter card meta if missing
    if 'twitter:card' not in html:
        twitter = '  <meta name="twitter:card" content="summary_large_image" />'
        html = html.replace('</head>', twitter + '\n</head>')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  ✓ {rel_path}")

# ── robots.txt ──────────────────────────────────────────────────────
print("\n=== robots.txt ===")
robots = f"""User-agent: *
Allow: /
Disallow: /privacy-policy/
Disallow: /terms/

Sitemap: {DOMAIN}/sitemap.xml
"""
with open(os.path.join(BASE, 'robots.txt'), 'w') as f:
    f.write(robots)
print("  ✓ robots.txt created")

# ── sitemap.xml ─────────────────────────────────────────────────────
print("\n=== sitemap.xml ===")
from datetime import date
today = date.today().isoformat()

sitemap_urls = []
for rel, data in PAGES.items():
    priority = "1.0" if data["path"] == "/" else ("0.9" if "index" not in rel.replace("index.html","") else "0.8")
    if data["path"] == "/": priority = "1.0"
    elif data["schema_type"] == "service": priority = "0.9"
    else: priority = "0.7"
    sitemap_urls.append(f"""  <url>
    <loc>{DOMAIN}{data['path']}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>{priority}</priority>
  </url>""")

sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(sitemap_urls)}
</urlset>
"""
with open(os.path.join(BASE, 'sitemap.xml'), 'w') as f:
    f.write(sitemap)
print("  ✓ sitemap.xml created")

print("\n=== SEO pass complete ===")
