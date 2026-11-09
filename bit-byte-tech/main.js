/* Bit Byte Tech. The contact form sends to Formspree (FORM_ENDPOINT below);
   messages arrive at the email address that owns the Formspree form. */
const FORM_ENDPOINT = 'https://formspree.io/f/xaeerwne';

(() => {
  const $ = (s, r = document) => r.querySelector(s);
  document.querySelectorAll('[data-year]').forEach(el => { el.textContent = new Date().getFullYear(); });

  // Mobile menu
  const toggle = $('.menu-toggle');
  const setMenu = open => {
    document.body.classList.toggle('nav-open', open);
    toggle.setAttribute('aria-expanded', String(open));
    toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
  };
  toggle.addEventListener('click', () => setMenu(!document.body.classList.contains('nav-open')));
  $('#site-nav').addEventListener('click', e => { if (e.target.closest('a')) setMenu(false); });
  document.addEventListener('keydown', e => { if (e.key === 'Escape') setMenu(false); });

  // Contact form (mock-up only)
  const form = $('#quote');
  if (!form) return;
  const rules = {
    name: v => v.trim().length >= 2 ? '' : 'Please enter your name.',
    phone: v => v.replace(/\D/g, '').length >= 10 ? '' : 'Please enter a phone number with 10 digits.',
    message: v => v.trim().length >= 5 ? '' : 'Please tell me a little about what you need.',
  };
  const check = name => {
    const el = form.elements[name];
    const msg = rules[name](el.value);
    $(`#err-${name}`).textContent = msg;
    el.setAttribute('aria-invalid', msg ? 'true' : 'false');
    return !msg;
  };
  form.addEventListener('input', e => { if (rules[e.target.name] && e.target.getAttribute('aria-invalid') === 'true') check(e.target.name); });
  form.addEventListener('submit', async e => {
    e.preventDefault();
    const bad = Object.keys(rules).filter(n => !check(n));
    const status = $('.form__status', form);
    status.classList.remove('form__status--err');
    if (bad.length) { status.textContent = ''; form.elements[bad[0]].focus(); return; }
    if ($('[name="_gotcha"]', form)?.value) return; // spam trap
    const btn = $('[type="submit"]', form);
    btn.disabled = true;
    status.textContent = 'Sending…';
    try {
      const data = new FormData(form);
      data.append('_subject', `Bit Byte Tech enquiry from ${data.get('name')}`);
      const res = await fetch(FORM_ENDPOINT, { method: 'POST', body: data, headers: { Accept: 'application/json' } });
      if (!res.ok) throw new Error(res.status);
      form.reset();
      status.textContent = "Thanks! Your message has been sent. I'll get back to you with a free quote soon.";
    } catch {
      status.classList.add('form__status--err');
      status.textContent = 'Sorry, your message could not be sent. Please call or WhatsApp 076 803 0406.';
    } finally {
      btn.disabled = false;
    }
  });
})();
