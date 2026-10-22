/* Sahil Samlal Attorneys Inc.
   SITE.formEndpoint: paste a Formspree URL (e.g. https://formspree.io/f/xxxx) to receive bookings by email.
   While it is empty (mock-up), the form shows the success message without sending anything. */
const SITE = {
  formEndpoint: '',
};

(() => {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  $$('[data-year]').forEach(el => { el.textContent = new Date().getFullYear(); });

  /* Mobile menu */
  const toggle = $('.menu-toggle');
  const header = $('.header');
  if (toggle) {
    const setMenu = open => {
      document.body.classList.toggle('nav-open', open);
      toggle.setAttribute('aria-expanded', String(open));
      toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
      if (open) $('#site-nav').style.setProperty('--nav-top', `${header.getBoundingClientRect().bottom}px`);
    };
    toggle.addEventListener('click', () => setMenu(!document.body.classList.contains('nav-open')));
    $('#site-nav').addEventListener('click', e => { if (e.target.closest('a')) setMenu(false); });
    document.addEventListener('keydown', e => { if (e.key === 'Escape') setMenu(false); });
  }

  /* Booking form */
  const form = $('#booking-form');
  if (!form) return;

  // Pre-select the practice area from links like contact.html?area=divorce#book
  const area = new URLSearchParams(location.search).get('area');
  if (area && form.area.querySelector(`option[value="${CSS.escape(area)}"]`)) form.area.value = area;

  const setErr = (name, msg) => {
    const out = $(`#err-${name}`);
    if (out) out.textContent = msg;
    const el = form.elements[name];
    if (el && el.setAttribute && !(el instanceof RadioNodeList)) el.setAttribute('aria-invalid', msg ? 'true' : 'false');
    return !msg;
  };
  const rules = {
    name: v => v.trim().length >= 2 ? '' : 'Please enter your full name.',
    cell: v => v.replace(/\D/g, '').length >= 10 ? '' : 'Please enter a cell number with 10 digits.',
    email: v => /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v.trim()) ? '' : 'Please enter a valid email address.',
    area: v => v ? '' : 'Please choose the type of matter.',
    details: v => v.trim().length >= 10 ? '' : 'Please describe your matter in a few words.',
    platform: v => v ? '' : 'Please choose in-office or virtual.',
    availability: v => v.trim() ? '' : 'Please tell us when you are available.',
  };
  form.addEventListener('input', e => { if (rules[e.target.name] && e.target.getAttribute('aria-invalid') === 'true') setErr(e.target.name, rules[e.target.name](e.target.value)); });
  form.addEventListener('change', e => { if (e.target.name === 'platform') setErr('platform', ''); if (e.target.name === 'consent') setErr('consent', ''); });

  form.addEventListener('submit', async e => {
    e.preventDefault();
    let first = null;
    Object.entries(rules).forEach(([name, rule]) => {
      const ok = setErr(name, rule(form.elements[name].value));
      if (!ok && !first) first = name === 'platform' ? form.querySelector('[name="platform"]') : form.elements[name];
    });
    if (!form.consent.checked) { setErr('consent', 'Please agree to the privacy notice so we can contact you.'); first = first || form.consent; }
    if (first) { first.focus(); return; }

    const status = $('.form-status', form);
    const btn = $('[type="submit"]', form);
    btn.disabled = true;
    try {
      if (SITE.formEndpoint) {
        const res = await fetch(SITE.formEndpoint, { method: 'POST', headers: { Accept: 'application/json' }, body: new FormData(form) });
        if (!res.ok) throw new Error(res.status);
      } else {
        await new Promise(r => setTimeout(r, 500));
      }
      form.reset();
      status.className = 'form-status form-status--ok';
      status.textContent = 'Thank you. We have received your request and will contact you to confirm your consultation.';
    } catch {
      status.className = 'form-status';
      status.textContent = 'Sorry, something went wrong. Please call (034) 315 5315 or WhatsApp 082 762 5716.';
    } finally {
      btn.disabled = false;
    }
  });
})();
