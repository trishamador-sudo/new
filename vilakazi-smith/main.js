/* Vilakazi Smith Inc. — site behaviour (no dependencies). */

// Paste the Formspree (or similar) endpoint here once the firm's enquiry email is confirmed.
const FORM_ENDPOINT = '';

(function () {
  // Mobile menu
  const toggle = document.querySelector('.menu-toggle');
  const nav = document.getElementById('site-nav');
  if (toggle && nav) {
    const setOpen = (open) => {
      if (open) nav.style.top = toggle.closest('.header').getBoundingClientRect().bottom + 'px';
      toggle.setAttribute('aria-expanded', String(open));
      toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
      nav.classList.toggle('is-open', open);
      document.body.classList.toggle('menu-open', open);
    };
    toggle.addEventListener('click', () => setOpen(toggle.getAttribute('aria-expanded') !== 'true'));
    nav.addEventListener('click', (e) => { if (e.target.closest('a')) setOpen(false); });
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape') setOpen(false); });
  }

  // Testimonials carousel
  document.querySelectorAll('[data-carousel]').forEach((root) => {
    const track = root.querySelector('.carousel__track');
    const prev = root.querySelector('[data-dir="prev"]');
    const next = root.querySelector('[data-dir="next"]');
    if (!track || !prev || !next) return;
    const step = () => (track.firstElementChild ? track.firstElementChild.getBoundingClientRect().width + 24 : track.clientWidth);
    const update = () => {
      prev.disabled = track.scrollLeft < 4;
      next.disabled = track.scrollLeft + track.clientWidth >= track.scrollWidth - 4;
    };
    prev.addEventListener('click', () => track.scrollBy({ left: -step(), behavior: 'smooth' }));
    next.addEventListener('click', () => track.scrollBy({ left: step(), behavior: 'smooth' }));
    track.addEventListener('scroll', update, { passive: true });
    window.addEventListener('resize', update);
    update();
  });

  // Maps load only when asked for, so Google Maps doesn't slow the page down
  document.querySelectorAll('[data-map]').forEach((btn) => {
    btn.addEventListener('click', () => {
      const box = btn.closest('.map');
      const frame = document.createElement('iframe');
      frame.src = 'https://www.google.com/maps?output=embed&q=' + encodeURIComponent(btn.dataset.map);
      frame.title = btn.dataset.title || 'Map';
      frame.loading = 'lazy';
      frame.referrerPolicy = 'no-referrer-when-downgrade';
      box.replaceChildren(frame);
    });
  });

  // Consultation form
  const form = document.querySelector('form[data-enquiry]');
  if (form) {
    const status = form.querySelector('.form__status');
    const say = (msg, state) => { status.textContent = msg; status.dataset.state = state; };
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      if (!form.reportValidity()) return;
      if (form.querySelector('.hp input').value) return; // spam trap
      if (!FORM_ENDPOINT) {
        say('Online requests are not switched on yet. Please call 012 492 5505 (Centurion) or 010 979 4130 (Sandton).', 'error');
        return;
      }
      const btn = form.querySelector('button[type="submit"]');
      btn.disabled = true;
      say('Sending your request…', '');
      try {
        const res = await fetch(FORM_ENDPOINT, { method: 'POST', body: new FormData(form), headers: { Accept: 'application/json' } });
        if (!res.ok) throw new Error(String(res.status));
        form.reset();
        say('Request sent. We will contact you to arrange your consultation.', 'ok');
      } catch (err) {
        say('Your request was not sent. Please try again, or call 012 492 5505.', 'error');
      } finally {
        btn.disabled = false;
      }
    });
  }

  const y = document.querySelector('[data-year]');
  if (y) y.textContent = new Date().getFullYear();
})();
