/* ==========================================================
   SITE SETTINGS: edit these values, everything updates.
   ========================================================== */
const SITE = {
  phone: '084 927 0101',          // shown on the site
  phoneLink: '+27849270101',      // used for tap-to-call
  whatsapp: '27849270101',        // international format, no +
  whatsappText: "Hi Louise, I'd like to enquire about a legal matter.",
  email: 'louise@minnaar-law.co.za',
  area: 'West Rand, Gauteng',
  // Consultation requests are sent here. Create a free form at https://formspree.io,
  // then paste its endpoint, e.g. 'https://formspree.io/f/abcdwxyz'.
  // While empty, the form opens the visitor's email app addressed to `email`.
  formEndpoint: '',
  // Set by the preview build. Shows the thank-you message without sending anything.
  preview: false,
};

(() => {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const reduceMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.documentElement.classList.add('js');

  // Apply settings
  $$('[data-cfg]').forEach(el => { el.textContent = SITE[el.dataset.cfg]; });
  $$('[data-cfg-href="tel"]').forEach(a => { a.href = `tel:${SITE.phoneLink}`; });
  $$('[data-cfg-href="mailto"]').forEach(a => { a.href = `mailto:${SITE.email}`; });
  $$('[data-cfg-href="wa"]').forEach(a => { a.href = `https://wa.me/${SITE.whatsapp}?text=${encodeURIComponent(SITE.whatsappText)}`; });
  $$('[data-year]').forEach(el => { el.textContent = new Date().getFullYear(); });

  // Mobile menu
  const toggle = $('.menu-toggle');
  const nav = $('#site-nav');
  const header = $('.header');
  const setMenu = open => {
    document.body.classList.toggle('nav-open', open);
    toggle.setAttribute('aria-expanded', String(open));
    toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    if (open) nav.style.setProperty('--nav-top', `${header.getBoundingClientRect().bottom}px`);
  };
  toggle.addEventListener('click', () => setMenu(!document.body.classList.contains('nav-open')));
  nav.addEventListener('click', e => { if (e.target.closest('a')) setMenu(false); });
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape' && document.body.classList.contains('nav-open')) { setMenu(false); toggle.focus(); }
  });

  // Mobile action bar appears after the hero
  new IntersectionObserver(([e]) => {
    document.body.classList.toggle('show-bar', !e.isIntersecting);
  }, { threshold: 0.05 }).observe($('.hero'));

  // Active nav link
  const links = $$('.nav a[href^="#"]:not(.btn)');
  const sections = links.map(a => $(a.getAttribute('href'))).filter(Boolean);
  const navObs = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) links.forEach(a => a.classList.toggle('is-current', a.getAttribute('href') === `#${e.target.id}`));
    });
  }, { rootMargin: '-45% 0px -50% 0px' });
  sections.forEach(s => navObs.observe(s));

  // "Book" CTAs focus the first form field after scrolling
  $$('a[href="#contact"]').forEach(a => a.addEventListener('click', () => {
    setTimeout(() => $('#f-name').focus({ preventScroll: true }), reduceMotion ? 0 : 700);
  }));

  // Scroll reveals
  const revealObs = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (!e.isIntersecting) return;
      e.target.classList.add('is-in');
      revealObs.unobserve(e.target);
    });
  }, { rootMargin: '0px 0px -8% 0px' });
  $$('.reveal').forEach((el, i) => {
    // Stagger items that sit side by side
    const sibs = [...el.parentElement.children].filter(c => c.classList.contains('reveal'));
    if (sibs.length > 2) el.style.transitionDelay = `${(sibs.indexOf(el) % 3) * 90}ms`;
    revealObs.observe(el);
  });

  /* ---------- Consultation form ---------- */
  const form = $('#consult');
  const status = $('.form-status', form);
  const fields = {
    name: [$('#f-name'), $('#e-name'), v => v.trim().length >= 2 || 'Please enter your name.'],
    phone: [$('#f-phone'), $('#e-phone'), v => v.replace(/\D/g, '').length >= 9 || 'Please enter a phone number we can reach you on, e.g. 082 123 4567.'],
    email: [$('#f-email'), $('#e-email'), v => !v.trim() || /^\S+@\S+\.\S+$/.test(v.trim()) || 'Please check your email address.'],
    matter: [$('#f-matter'), $('#e-matter'), v => !!v || 'Please choose what your matter is about.'],
  };
  const check = k => {
    const [input, err, rule] = fields[k];
    const r = rule(input.value);
    const msg = r === true ? '' : r;
    err.textContent = msg;
    input.setAttribute('aria-invalid', msg ? 'true' : 'false');
    return !msg;
  };
  Object.keys(fields).forEach(k => {
    const [input] = fields[k];
    input.addEventListener('blur', () => input.value && check(k));
    input.addEventListener('input', () => input.getAttribute('aria-invalid') === 'true' && check(k));
  });

  form.addEventListener('submit', async e => {
    e.preventDefault();
    const bad = Object.keys(fields).filter(k => !check(k));
    if (bad.length) { fields[bad[0]][0].focus(); return; }
    const data = Object.fromEntries(new FormData(form).entries());
    const btn = $('[data-submit]', form);
    btn.classList.add('is-loading');
    btn.disabled = true;
    status.textContent = '';
    try {
      if (SITE.preview) {
        await new Promise(r => setTimeout(r, 500));
      } else if (SITE.formEndpoint) {
        const res = await fetch(SITE.formEndpoint, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
          body: JSON.stringify({ ...data, _subject: `Consultation request: ${data.matter} (${data.name})`, ...(data.email ? { _replyto: data.email } : {}) }),
        });
        if (!res.ok) throw new Error(res.status);
      } else {
        const body = Object.entries(data).filter(([, v]) => v).map(([k, v]) => `${k}: ${v}`).join('\n');
        location.href = `mailto:${SITE.email}?subject=${encodeURIComponent(`Consultation request: ${data.matter}`)}&body=${encodeURIComponent(body)}`;
      }
      form.reset();
      status.textContent = `Thank you, ${data.name.trim().split(' ')[0]}. Louise will contact you shortly.`;
    } catch {
      status.textContent = `Sorry, your request didn't send. Please call or WhatsApp ${SITE.phone}.`;
    } finally {
      btn.classList.remove('is-loading');
      btn.disabled = false;
    }
  });
})();
