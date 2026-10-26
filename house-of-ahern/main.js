/* House of Ahern (concept). The enquiry form shows a thank-you message only;
   connect it to Formspree or similar when the site goes live. */
(() => {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  $$('[data-year]').forEach(el => { el.textContent = new Date().getFullYear(); });

  // Header background once the page scrolls
  const header = $('.header');
  const onScroll = () => header.classList.toggle('is-scrolled', window.scrollY > 40);
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

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

  // Puppy carousel
  const slides = $$('.carousel__slide');
  let i = 0;
  const show = n => { slides[i].classList.remove('is-active'); i = (n + slides.length) % slides.length; slides[i].classList.add('is-active'); };
  $('.carousel__btn--prev').addEventListener('click', () => show(i - 1));
  $('.carousel__btn--next').addEventListener('click', () => show(i + 1));

  // Enquiry form (concept: no data is sent)
  const form = $('#enquiry');
  form.addEventListener('submit', e => {
    e.preventDefault();
    let first = null;
    [form.name, form.email].forEach(el => {
      const bad = el.name === 'email' ? !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(el.value.trim()) : el.value.trim().length < 2;
      el.setAttribute('aria-invalid', bad ? 'true' : 'false');
      if (bad && !first) first = el;
    });
    const status = $('.enquiry__status', form);
    if (first) { status.textContent = 'Please add your name and a valid email address.'; first.focus(); return; }
    form.reset();
    status.textContent = 'Thank you! We have received your enquiry and will be in touch about upcoming litters.';
  });
})();
