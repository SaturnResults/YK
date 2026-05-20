// Hero slider
(function () {
  const slider = document.getElementById('heroSlider');
  if (!slider) return;

  const slides = slider.querySelectorAll('.hero-slide');
  const dots   = slider.querySelectorAll('.hero-slider__dot');
  let current  = 0;
  let timer;

  function goTo(index) {
    slides[current].classList.remove('active');
    dots[current].classList.remove('active');
    current = (index + slides.length) % slides.length;
    slides[current].classList.add('active');
    dots[current].classList.add('active');
  }

  function next() { goTo(current + 1); }
  function prev() { goTo(current - 1); }

  function startTimer() {
    clearInterval(timer);
    timer = setInterval(next, 8000);
  }

  slider.querySelector('.hero-slider__arrow--next')?.addEventListener('click', () => { next(); startTimer(); });
  slider.querySelector('.hero-slider__arrow--prev')?.addEventListener('click', () => { prev(); startTimer(); });
  dots.forEach((dot, i) => dot.addEventListener('click', () => { goTo(i); startTimer(); }));

  startTimer();
})();

// Nav scroll — hide after 10px down (even slow), show after 80px up on mobile
const nav = document.getElementById('nav');
let lastScrollY = window.scrollY;
let scrollDownFrom = window.scrollY; // point where downward scroll began
let hideScrollY = 0;                 // y position when nav was hidden

window.addEventListener('scroll', () => {
  const y = window.scrollY;
  const isMobile = window.innerWidth <= 768;
  const upThreshold = isMobile ? 80 : 0;
  nav?.classList.toggle('scrolled', y > 40);

  if (y <= 80) {
    // Near top — always show
    nav?.classList.remove('nav--hidden');
    scrollDownFrom = y;
    hideScrollY = 0;
  } else if (y > lastScrollY) {
    // Scrolling down — reset upward reference, hide after 10px cumulative
    scrollDownFrom = Math.min(scrollDownFrom, y);
    if (y > scrollDownFrom + 10) {
      nav?.classList.add('nav--hidden');
      hideScrollY = y;
    }
  } else if (y < lastScrollY) {
    // Scrolling up — reset downward reference
    scrollDownFrom = y;
    if (hideScrollY > 0 && y < hideScrollY - upThreshold) {
      nav?.classList.remove('nav--hidden');
      hideScrollY = 0;
    }
  }

  lastScrollY = y;
}, { passive: true });

// Mobile nav drawer
const hamburger = document.getElementById('hamburger');
const mobileNav = document.getElementById('mobileNav');
const mobileOverlay = document.getElementById('mobileOverlay');
const mobileClose = document.getElementById('mobileClose');

function openMobileNav() {
  mobileNav?.classList.add('open');
  mobileOverlay?.classList.add('open');
  document.body.style.overflow = 'hidden';
  // Hide chatbot launcher while menu is open
  const launcher = document.querySelector('.ykc-launcher');
  if (launcher) launcher.style.display = 'none';
}
function closeMobileNav() {
  mobileNav?.classList.remove('open');
  mobileOverlay?.classList.remove('open');
  document.body.style.overflow = '';
  // Restore chatbot launcher
  const launcher = document.querySelector('.ykc-launcher');
  if (launcher) launcher.style.display = '';
}

hamburger?.addEventListener('click', openMobileNav);
mobileClose?.addEventListener('click', closeMobileNav);
mobileOverlay?.addEventListener('click', closeMobileNav);
// Close drawer when any link inside is clicked
mobileNav?.querySelectorAll('a').forEach(a => a.addEventListener('click', closeMobileNav));

// Mobile accordion (Treatments sub-menu)
document.querySelectorAll('.nav__mobile-accordion-trigger').forEach(trigger => {
  trigger.addEventListener('click', () => {
    const accordion = trigger.closest('.nav__mobile-accordion');
    accordion.classList.toggle('open');
  });
});

// Fade-up on scroll
const observer = new IntersectionObserver(entries => {
  entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('visible'); } });
}, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
document.querySelectorAll('.fade-up').forEach(el => observer.observe(el));

// FAQ accordion
document.querySelectorAll('.faq-question').forEach(q => {
  q.addEventListener('click', () => {
    const item = q.closest('.faq-item');
    const isOpen = item.classList.contains('open');
    document.querySelectorAll('.faq-item').forEach(i => i.classList.remove('open'));
    if (!isOpen) item.classList.add('open');
  });
});

// Treatment quiz
(function () {
  // [q1][q2][q3] → { primary, also }
  const map = {
    pain: {
      chronic:     { upper: {p:'osteo',   a:'deep'},   lower: {p:'deep',   a:'osteo'},  whole: {p:'deep',   a:'osteo'},  posture: {p:'osteo',  a:'deep'}   },
      recent:      { upper: {p:'deep',    a:'sports'},  lower: {p:'sports', a:'deep'},   whole: {p:'deep',   a:'sports'}, posture: {p:'osteo',  a:'deep'}   },
      acute:       { upper: {p:'sports',  a:'osteo'},   lower: {p:'sports', a:'deep'},   whole: {p:'sports', a:'deep'},   posture: {p:'osteo',  a:'sports'} },
      maintenance: { upper: {p:'deep',    a:'swedish'}, lower: {p:'deep',   a:'sports'}, whole: {p:'swedish',a:'deep'},   posture: {p:'osteo',  a:'deep'}   },
    },
    tension: {
      chronic:     { upper: {p:'deep',    a:'osteo'},   lower: {p:'deep',   a:'sports'}, whole: {p:'deep',   a:'swedish'},posture: {p:'osteo',  a:'deep'}   },
      recent:      { upper: {p:'deep',    a:'sports'},  lower: {p:'sports', a:'deep'},   whole: {p:'deep',   a:'swedish'},posture: {p:'deep',   a:'osteo'}  },
      acute:       { upper: {p:'sports',  a:'deep'},    lower: {p:'sports', a:'deep'},   whole: {p:'sports', a:'swedish'},posture: {p:'deep',   a:'osteo'}  },
      maintenance: { upper: {p:'deep',    a:'swedish'}, lower: {p:'deep',   a:'sports'}, whole: {p:'swedish',a:'cbd'},    posture: {p:'deep',   a:'swedish'} },
    },
    relax: {
      chronic:     { upper: {p:'swedish', a:'cbd'},     lower: {p:'swedish',a:'lymph'},  whole: {p:'swedish',a:'cbd'},    posture: {p:'osteo',  a:'swedish'} },
      recent:      { upper: {p:'swedish', a:'cbd'},     lower: {p:'swedish',a:'lymph'},  whole: {p:'cbd',    a:'swedish'},posture: {p:'swedish',a:'osteo'}  },
      acute:       { upper: {p:'swedish', a:'cbd'},     lower: {p:'lymph',  a:'swedish'},whole: {p:'swedish',a:'lymph'}, posture: {p:'swedish',a:'deep'}   },
      maintenance: { upper: {p:'swedish', a:'cbd'},     lower: {p:'swedish',a:'lymph'},  whole: {p:'cbd',    a:'swedish'},posture: {p:'swedish',a:'osteo'}  },
    },
    performance: {
      chronic:     { upper: {p:'sports',  a:'osteo'},   lower: {p:'sports', a:'osteo'},  whole: {p:'sports', a:'deep'},   posture: {p:'osteo',  a:'sports'} },
      recent:      { upper: {p:'sports',  a:'deep'},    lower: {p:'sports', a:'deep'},   whole: {p:'sports', a:'deep'},   posture: {p:'sports', a:'osteo'}  },
      acute:       { upper: {p:'sports',  a:'deep'},    lower: {p:'sports', a:'deep'},   whole: {p:'sports', a:'swedish'},posture: {p:'osteo',  a:'sports'} },
      maintenance: { upper: {p:'sports',  a:'deep'},    lower: {p:'sports', a:'deep'},   whole: {p:'sports', a:'swedish'},posture: {p:'sports', a:'osteo'}  },
    },
    skin: {
      chronic:     { upper: {p:'lymph',   a:'cbd'},     lower: {p:'cellulite',a:'lymph'},whole: {p:'lymph',  a:'cellulite'},posture:{p:'lymph', a:'cbd'}    },
      recent:      { upper: {p:'lymph',   a:'cbd'},     lower: {p:'cellulite',a:'lymph'},whole: {p:'lymph',  a:'cbd'},    posture: {p:'lymph',  a:'cbd'}    },
      acute:       { upper: {p:'lymph',   a:'swedish'}, lower: {p:'lymph',  a:'cellulite'},whole:{p:'lymph', a:'swedish'},posture:{p:'lymph',  a:'cbd'}    },
      maintenance: { upper: {p:'cbd',     a:'lymph'},   lower: {p:'cellulite',a:'lymph'},whole: {p:'lymph',  a:'cbd'},    posture: {p:'cbd',    a:'lymph'}  },
    },
    structure: {
      chronic:     { upper: {p:'osteo',   a:'deep'},    lower: {p:'osteo',  a:'deep'},   whole: {p:'osteo',  a:'deep'},   posture: {p:'osteo',  a:'deep'}   },
      recent:      { upper: {p:'osteo',   a:'sports'},  lower: {p:'osteo',  a:'sports'}, whole: {p:'osteo',  a:'deep'},   posture: {p:'osteo',  a:'deep'}   },
      acute:       { upper: {p:'osteo',   a:'sports'},  lower: {p:'osteo',  a:'sports'}, whole: {p:'osteo',  a:'deep'},   posture: {p:'osteo',  a:'sports'} },
      maintenance: { upper: {p:'osteo',   a:'deep'},    lower: {p:'osteo',  a:'deep'},   whole: {p:'osteo',  a:'swedish'},posture: {p:'osteo',  a:'deep'}   },
    },
    other: {
      chronic:     { upper: {p:'deep',    a:'swedish'}, lower: {p:'deep',   a:'sports'}, whole: {p:'swedish',a:'deep'},   posture: {p:'osteo',  a:'deep'}   },
      recent:      { upper: {p:'deep',    a:'swedish'}, lower: {p:'sports', a:'deep'},   whole: {p:'swedish',a:'deep'},   posture: {p:'deep',   a:'swedish'} },
      acute:       { upper: {p:'sports',  a:'deep'},    lower: {p:'sports', a:'deep'},   whole: {p:'sports', a:'swedish'},posture: {p:'osteo',  a:'deep'}   },
      maintenance: { upper: {p:'swedish', a:'cbd'},     lower: {p:'swedish',a:'deep'},   whole: {p:'swedish',a:'cbd'},    posture: {p:'swedish',a:'deep'}   },
    },
  };

  const T = {
    deep:      { badge: 'Best for tension & pain',      title: 'Deep Tissue Massage',        desc: 'Works into the deeper muscle layers to relieve chronic tension, reduce pain and restore full movement. Ideal for persistent aches, postural problems and desk-related strain.',              link: '/deep-tissue-massage-west-london/' },
    swedish:   { badge: 'Best for relaxation',          title: 'Swedish Massage',            desc: 'Long, flowing strokes that improve circulation, ease tension and calm the nervous system. The perfect choice if you want genuine rest, better sleep or a full-body reset.',              link: '/swedish-massage/' },
    sports:    { badge: 'Best for performance',         title: 'Sports Massage',             desc: 'Advanced techniques designed for active people. Accelerate recovery, prevent injury and keep your body performing at its best, whether you train competitively or just stay active.',   link: '/sports-massage-west-london/' },
    osteo:     { badge: 'Best for structural care',     title: 'Osteopathy',                 desc: 'A hands-on, whole-body approach that looks beyond the symptom to the root cause. Ideal for joint pain, postural issues, sciatica and conditions that haven\u2019t responded elsewhere.', link: '/osteopathy-services/' },
    cbd:       { badge: 'Best for deep relaxation',     title: 'CBD Massage',                desc: 'Therapeutic massage combined with premium CBD oil for enhanced anti-inflammatory relief, deeper relaxation and accelerated recovery. A step up from Swedish for mind and body.',       link: '/cbd-massage/' },
    lymph:     { badge: 'Best for circulation',         title: 'Lymphatic Drainage',         desc: 'Gentle, rhythmic massage that stimulates the lymphatic system, reduces fluid retention and supports recovery. Ideal after surgery, illness or for general immune support.',            link: '/lymphatic-drainage-massage/' },
    cellulite: { badge: 'Best for skin health',         title: 'Anti-Cellulite Massage',     desc: 'Combines lymphatic drainage and targeted deep-tissue techniques to improve circulation, reduce the appearance of cellulite and restore skin texture and firmness over time.',         link: '/anti-cellulite-massage/' },
  };

  // Q2 question text changes based on Q1
  const q2Questions = {
    pain:        'How long have you been experiencing this?',
    tension:     'How would you describe it?',
    relax:       'What kind of session suits you best?',
    performance: 'Where are you in your training cycle?',
    skin:        'What best describes your situation?',
    structure:   'How long has this been affecting you?',
    other:       "What best describes what you’re looking for?",
  };
  const q2Labels = {
    pain:        ['chronic','recent','acute','maintenance'],
    tension:     ['chronic','recent','acute','maintenance'],
    relax:       ['maintenance','maintenance','maintenance','maintenance'],
    performance: ['chronic','recent','acute','maintenance'],
    skin:        ['chronic','recent','acute','maintenance'],
    structure:   ['chronic','recent','acute','maintenance'],
    other:       ['chronic','recent','acute','maintenance'],
  };

  let ans = {};
  const progressBar = document.getElementById('quizProgress');

  function updateDots(step) {
    [1,2,3].forEach(i => {
      const d = document.getElementById('qDot' + i);
      if (!d) return;
      d.classList.toggle('active', i <= step);
      d.classList.toggle('done', i < step);
    });
  }

  function showStep(id) {
    document.querySelectorAll('.quiz-step').forEach(s => s.classList.remove('active'));
    const el = document.getElementById(id);
    if (el) { el.classList.add('active'); el.scrollIntoView({behavior:'smooth', block:'nearest'}); }
    if (id === 'quizStep1') { progressBar.style.width = '0%';    updateDots(1); }
    if (id === 'quizStep2') { progressBar.style.width = '50%';   updateDots(2); }
    if (id === 'quizStep3') { progressBar.style.width = '80%';   updateDots(3); }
    if (id === 'quizResult'){ progressBar.style.width = '100%';  updateDots(3); showResult(); }
  }

  function showResult() {
    const row  = (map[ans.q1] || map.pain)[ans.q2] || (map[ans.q1] || map.pain).chronic;
    const cell = row[ans.q3] || row.upper || {p:'deep', a:null};
    const t    = T[cell.p] || T.deep;
    const also = cell.a && T[cell.a];

    document.getElementById('quizResultBadge').textContent = t.badge;
    document.getElementById('quizResultTitle').textContent = t.title;
    document.getElementById('quizResultDesc').textContent  = t.desc;
    const learnBtn = document.getElementById('quizLearnBtn');
    if (learnBtn) learnBtn.href = t.link;

    const alsoRow  = document.getElementById('quizResultAlso');
    const alsoLink = document.getElementById('quizAlsoLink');
    if (also && alsoRow && alsoLink) {
      alsoLink.textContent = also.title;
      alsoLink.href = also.link;
      alsoRow.style.display = '';
    } else if (alsoRow) {
      alsoRow.style.display = 'none';
    }
  }

  document.querySelectorAll('#quizStep1 .quiz-opt').forEach(btn => {
    btn.addEventListener('click', () => {
      ans.q1 = btn.dataset.val;
      // "Other" skips Q2 — default q2 to maintenance and go straight to Q3
      if (ans.q1 === 'other') {
        ans.q2 = 'maintenance';
        showStep('quizStep3');
        return;
      }
      // Update Q2 question text
      const qEl = document.getElementById('quiz2Q');
      if (qEl) qEl.textContent = q2Questions[ans.q1] || q2Questions.pain;
      showStep('quizStep2');
    });
  });
  document.querySelectorAll('#quizStep2 .quiz-opt').forEach(btn => {
    btn.addEventListener('click', () => { ans.q2 = btn.dataset.val; showStep('quizStep3'); });
  });
  document.querySelectorAll('#quizStep3 .quiz-opt').forEach(btn => {
    btn.addEventListener('click', () => { ans.q3 = btn.dataset.val; showStep('quizResult'); });
  });
  document.querySelectorAll('.quiz-back').forEach(btn => {
    btn.addEventListener('click', () => {
      let target = btn.dataset.back;
      // If going back to Q2 but Q1 was "other" (Q2 was skipped), go to Q1 instead
      if (target === 'quizStep2' && ans.q1 === 'other') {
        target = 'quizStep1';
        ans.q1 = undefined;
        ans.q2 = undefined;
      } else {
        if (target === 'quizStep1') { ans.q1 = undefined; }
        if (target === 'quizStep2') { ans.q2 = undefined; }
      }
      showStep(target);
    });
  });

  document.getElementById('quizRestart')?.addEventListener('click', () => {
    ans = {};
    showStep('quizStep1');
  });
})();

// Back to top button
const backToTop = document.getElementById('backToTop');
if (backToTop) {
  window.addEventListener('scroll', () => {
    backToTop.classList.toggle('visible', window.scrollY > 400);
  });
  backToTop.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
}

// Cookie banner
(function () {
  const banner = document.getElementById('cookieBanner');
  if (!banner) return;
  if (localStorage.getItem('yk_cookies')) return;

  // Slight delay so it slides up after page load
  setTimeout(() => banner.classList.add('show'), 800);

  function dismiss() {
    banner.classList.remove('show');
    banner.addEventListener('transitionend', () => banner.remove(), { once: true });
  }

  document.getElementById('cookieAccept')?.addEventListener('click', () => {
    localStorage.setItem('yk_cookies', 'accepted');
    dismiss();
  });
  document.getElementById('cookieDecline')?.addEventListener('click', () => {
    localStorage.setItem('yk_cookies', 'declined');
    dismiss();
  });
})();

// Set active nav link (clean URL version)
(function () {
  const path = location.pathname;
  const treatmentPaths = [
    '/massage-therapy/', '/deep-tissue/', '/sports-massage/',
    '/swedish-massage/', '/cbd-massage/', '/lymphatic-drainage-massage/'
  ];
  const aboutPaths = ['/about-us/', '/team/'];

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
    if (href === '/about-us/' && aboutPaths.includes(path)) {
      trigger.classList.add('active');
      document.getElementById('aboutAccordion')?.classList.add('open');
    }
  });
})();

// On bfcache restore (back/forward), reset animation so page isn't invisible
window.addEventListener('pageshow', function (e) {
  if (e.persisted) {
    document.body.classList.remove('page-exit');
    document.body.style.animation = 'none';
    requestAnimationFrame(function () { document.body.style.animation = ''; });
  }
});

// Page transitions — brief fade out then navigate
document.addEventListener('click', function (e) {
  const link = e.target.closest('a[href]');
  if (!link) return;

  const href = link.getAttribute('href');
  if (!href || href.startsWith('http') || href.startsWith('#') ||
      href.startsWith('mailto:') || href.startsWith('tel:') ||
      href.startsWith('javascript') || link.target === '_blank') return;

  e.preventDefault();
  document.body.classList.add('page-exit');
  setTimeout(() => { window.location.href = href; }, 140);
});

// Treatment finder teaser card — smooth scroll to quiz
document.querySelector('.js-scroll-to-quiz')?.addEventListener('click', function (e) {
  e.preventDefault();
  document.getElementById('quiz')?.scrollIntoView({ behavior: 'smooth', block: 'start' });
});

// Reviews "View More" button
(function () {
  const btn = document.getElementById('reviewsMoreBtn');
  const wrap = document.getElementById('reviewsMoreWrap');
  if (!btn) return;
  btn.addEventListener('click', function () {
    document.querySelectorAll('.testimonial-card--hidden').forEach(function (card) {
      card.classList.remove('testimonial-card--hidden');
      requestAnimationFrame(() => card.classList.add('visible'));
    });
    wrap.style.display = 'none';
  });
})();
