/* ==========================================================
   SITE SETTINGS: edit these values, everything updates.
   ========================================================== */
const SITE = {
  phone: '000 000 0000',          // shown on the site
  phoneLink: '0000000000',        // digits for tap-to-call, e.g. +27821234567
  email: 'hello@example.com',
  serviceArea: 'Your service area',
  hours: 'Mon–Sat, 7:30–17:30',
  // Where estimate requests go. Paste a form endpoint (e.g. https://formspree.io/f/xxxx).
  // Left empty, the form opens the visitor's email app with the request filled in.
  formEndpoint: '',
};

(() => {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const reduceMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Apply settings
  $$('[data-cfg]').forEach(el => { el.textContent = SITE[el.dataset.cfg]; });
  $$('[data-cfg-href="tel"]').forEach(a => { a.href = `tel:${SITE.phoneLink}`; });
  $$('[data-cfg-href="mailto"]').forEach(a => { a.href = `mailto:${SITE.email}`; });
  $$('[data-year]').forEach(el => { el.textContent = new Date().getFullYear(); });

  // Mobile menu
  const toggle = $('.menu-toggle');
  const nav = $('#site-nav');
  const header = $('.header');
  const setMenu = open => {
    document.body.classList.toggle('nav-open', open);
    toggle.setAttribute('aria-expanded', String(open));
    toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    if (open) nav.style.top = `${header.getBoundingClientRect().bottom}px`;
  };
  toggle.addEventListener('click', () => setMenu(!document.body.classList.contains('nav-open')));
  nav.addEventListener('click', e => { if (e.target.closest('a')) setMenu(false); });
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape' && document.body.classList.contains('nav-open')) { setMenu(false); toggle.focus(); }
  });

  // Mobile sticky bar appears once the hero form is out of view
  const form = $('#estimate-form');
  const hero = $('.hero');
  new IntersectionObserver(([e]) => {
    document.body.classList.toggle('show-bar', !e.isIntersecting);
  }, { threshold: 0.05 }).observe(hero);

  // Active nav link
  const links = $$('.nav a[href^="#"]:not(.btn)');
  const sections = links.map(a => $(a.getAttribute('href'))).filter(Boolean);
  const navObs = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) links.forEach(a => a.classList.toggle('is-current', a.getAttribute('href') === `#${e.target.id}`));
    });
  }, { rootMargin: '-45% 0px -50% 0px' });
  sections.forEach(s => navObs.observe(s));

  // Any "free estimate" CTA: scroll to the form, focus the first choice, flash it
  $$('a[href="#estimate"]').forEach(a => a.addEventListener('click', e => {
    e.preventDefault();
    $('#estimate').scrollIntoView({ behavior: reduceMotion ? 'auto' : 'smooth', block: 'start' });
    history.replaceState(null, '', '#estimate');
    const first = $('.step.is-active input, .step.is-active button', form);
    setTimeout(() => {
      first && first.focus({ preventScroll: true });
      form.classList.remove('is-flash'); void form.offsetWidth; form.classList.add('is-flash');
    }, reduceMotion ? 0 : 450);
  }));

  /* ---------- Estimate form ---------- */
  const steps = $$('.step', form);
  const bar = $('.progress__bar', form);
  const stepNum = $('[data-step-num]', form);
  const stepLabel = $('.estimate__step', form);

  const show = key => {
    steps.forEach(s => {
      const on = s.dataset.step === key;
      s.hidden = !on;
      s.classList.toggle('is-active', on);
    });
    const n = key === '1' ? 1 : 2;
    bar.style.width = key === 'done' ? '100%' : `${n * 50}%`;
    stepNum.textContent = n;
    stepLabel.hidden = key === 'done';
  };

  const setError = (input, errEl, msg) => {
    errEl.textContent = msg;
    if (input) input.setAttribute('aria-invalid', msg ? 'true' : 'false');
    return !msg;
  };

  const errProject = $('#err-project');
  $('[data-next]', form).addEventListener('click', () => {
    const chosen = form.project.value;
    if (!setError(null, errProject, chosen ? '' : 'Please choose the kind of project.')) {
      $('input[name="project"]', form).focus();
      return;
    }
    show('2');
    $('#f-name').focus();
  });
  $$('input[name="project"]', form).forEach(r => r.addEventListener('change', () => {
    setError(null, errProject, '');
  }));
  // Double-click / Enter on a tile moves straight on
  $$('.tile', form).forEach(t => t.addEventListener('dblclick', () => $('[data-next]', form).click()));

  $('[data-back]', form).addEventListener('click', () => {
    show('1');
    ($('input[name="project"]:checked', form) || $('input[name="project"]', form)).focus();
  });

  const name = $('#f-name');
  const phone = $('#f-phone');
  const validateName = () => setError(name, $('#err-name'), name.value.trim().length >= 2 ? '' : 'Please enter your name.');
  const validatePhone = () => {
    const digits = phone.value.replace(/\D/g, '');
    return setError(phone, $('#err-phone'), digits.length >= 7 ? '' : 'Please enter a phone number we can call you on (at least 7 digits).');
  };
  name.addEventListener('blur', () => name.value && validateName());
  phone.addEventListener('blur', () => phone.value && validatePhone());
  name.addEventListener('input', () => name.getAttribute('aria-invalid') === 'true' && validateName());
  phone.addEventListener('input', () => phone.getAttribute('aria-invalid') === 'true' && validatePhone());

  form.addEventListener('submit', async e => {
    e.preventDefault();
    if ($('.step[data-step="1"]', form).classList.contains('is-active')) { $('[data-next]', form).click(); return; }
    const okName = validateName();
    const okPhone = validatePhone();
    if (!okName || !okPhone) { (okName ? phone : name).focus(); return; }

    const data = {
      project: form.project.value,
      name: name.value.trim(),
      phone: phone.value.trim(),
      details: form.details.value.trim(),
    };
    const btn = $('[data-submit]', form);
    btn.classList.add('is-loading'); btn.disabled = true;

    try {
      if (SITE.formEndpoint) {
        const res = await fetch(SITE.formEndpoint, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
          body: JSON.stringify({ ...data, _subject: `Free estimate request: ${data.project}` }),
        });
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
      } else {
        const body = `Project: ${data.project}\nName: ${data.name}\nPhone: ${data.phone}\n\n${data.details}`;
        window.location.href = `mailto:${SITE.email}?subject=${encodeURIComponent(`Free estimate request: ${data.project}`)}&body=${encodeURIComponent(body)}`;
      }
      $('[data-done-name]', form).textContent = data.name.split(' ')[0];
      show('done');
      $('.step--done', form).focus();
    } catch (err) {
      setError(null, $('#err-phone'), `Sorry, something went wrong sending your request. Please try again, or call us on ${SITE.phone}.`);
    } finally {
      btn.classList.remove('is-loading'); btn.disabled = false;
    }
  });

  /* ---------- Gallery video ---------- */
  $$('.g--video').forEach(fig => {
    const video = $('video', fig);
    const btn = $('.g__play', fig);
    const pauseIcon = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 5h4v14H7zM13 5h4v14h-4z"/></svg>';
    const playIcon = btn.innerHTML;
    btn.addEventListener('click', () => {
      if (video.paused) { video.play(); } else { video.pause(); }
    });
    video.addEventListener('play', () => { fig.classList.add('is-playing'); btn.innerHTML = pauseIcon; btn.setAttribute('aria-label', 'Pause video'); });
    video.addEventListener('pause', () => { fig.classList.remove('is-playing'); btn.innerHTML = playIcon; btn.setAttribute('aria-label', 'Play video'); });
  });

  /* ---------- Reveal on scroll ---------- */
  if (!reduceMotion && 'IntersectionObserver' in window) {
    const els = $$('.section-head, .svc, .ba__copy, .pair__item, .g, .about__media, .about__copy, .steps li, .review, .cta-band__inner');
    const io = new IntersectionObserver(entries => {
      entries.forEach(e => {
        if (!e.isIntersecting) return;
        e.target.classList.add('is-in');
        io.unobserve(e.target);
      });
    }, { rootMargin: '0px 0px -8% 0px' });
    els.forEach(el => {
      const siblings = [...el.parentElement.children];
      el.style.transitionDelay = `${Math.min(siblings.indexOf(el), 5) * 50}ms`;
      el.classList.add('reveal');
      io.observe(el);
    });
  }
})();
