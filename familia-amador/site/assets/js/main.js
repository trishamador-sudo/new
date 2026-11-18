/* Família Amador Construções: menu, WhatsApp chooser and quote form. */
(() => {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];

  // Mobile menu
  const toggle = $('.menu-toggle');
  if (toggle) {
    const set = open => {
      document.body.classList.toggle('nav-open', open);
      toggle.setAttribute('aria-expanded', String(open));
      toggle.setAttribute('aria-label', open ? toggle.dataset.labelClose : toggle.dataset.labelOpen);
    };
    toggle.addEventListener('click', () => set(!document.body.classList.contains('nav-open')));
    $('#site-nav').addEventListener('click', e => { if (e.target.closest('a')) set(false); });
    document.addEventListener('keydown', e => { if (e.key === 'Escape') set(false); });
  }

  // WhatsApp chooser: the floating button and any [data-wa-open] link open it
  const panel = $('#wa-panel');
  const waBtn = $('[data-wa-toggle]');
  if (panel && waBtn) {
    const open = show => {
      panel.hidden = !show;
      waBtn.setAttribute('aria-expanded', String(show));
      if (show) $('a', panel).focus();
    };
    waBtn.addEventListener('click', e => { e.preventDefault(); open(panel.hidden); });
    $$('[data-wa-open]').forEach(a => a.addEventListener('click', e => { e.preventDefault(); open(true); }));
    document.addEventListener('click', e => { if (!panel.hidden && !e.target.closest('[data-wa]') && !e.target.closest('[data-wa-open]')) open(false); });
    document.addEventListener('keydown', e => { if (e.key === 'Escape' && !panel.hidden) { open(false); waBtn.focus(); } });
  }

  // Quote form: sends to Formspree with fetch, then goes to the thank-you page.
  // Without JavaScript the form still posts to Formspree normally.
  $$('form[data-quote]').forEach(form => {
    const pt = form.dataset.lang === 'pt';
    const status = $('.form__status', form);
    form.addEventListener('submit', async e => {
      e.preventDefault();
      status.textContent = '';
      let first = null;
      ['name', 'phone', 'message'].forEach(n => {
        const el = form.elements[n];
        const bad = n === 'phone' ? el.value.replace(/\D/g, '').length < 9 : !el.value.trim();
        el.setAttribute('aria-invalid', bad ? 'true' : 'false');
        if (bad && !first) first = el;
      });
      if (first) {
        status.textContent = pt ? 'Preencha o nome, o telemóvel e a descrição do trabalho.' : 'Please fill in your name, phone number and a description of the job.';
        first.focus();
        return;
      }
      if (form.elements._gotcha.value) return;
      const service = form.elements.service.value;
      const town = form.elements.town.value;
      form.elements._subject.value = `${pt ? 'Novo pedido de orçamento' : 'New quote request'} - ${service} - ${town}`;
      form.elements.page.value = location.href;
      const btn = $('[type="submit"]', form);
      btn.disabled = true;
      try {
        const res = await fetch(form.action, { method: 'POST', body: new FormData(form), headers: { Accept: 'application/json' } });
        if (!res.ok) throw new Error(res.status);
        location.href = form.dataset.thanks;
      } catch {
        status.textContent = pt ? 'Não foi possível enviar. Tente novamente ou fale connosco por WhatsApp.' : 'Sorry, it could not be sent. Please try again or message us on WhatsApp.';
        btn.disabled = false;
      }
    });
  });

  $$('[data-year]').forEach(el => { el.textContent = new Date().getFullYear(); });
})();
