/* ==========================================================
   CONFIGURAÇÃO DO SITE: edite aqui, tudo se atualiza.
   ========================================================== */
const SITE = {
  phone: '(19) 4009-0659',
  phoneLink: '+551940090659',
  whatsapp: '5511993719036',
  whatsappDisplay: '(11) 99371-9036',
  whatsappText: 'Olá, D\'Mais! Gostaria de mais informações sobre o fornecimento de combustíveis.',
  email: 'contato@dmais-distribuidora.com',
  // Canal de Denúncias: endereço do formulário Formspree que entrega em diretoria@dmais-distribuidora.com.
  // Ex.: 'https://formspree.io/f/abcdwxyz'. Enquanto estiver vazio, abre o e-mail do visitante (sem anonimato).
  denunciaEndpoint: '',
  denunciaEmail: 'diretoria@dmais-distribuidora.com',
  // Endereço das HTTP Functions do Wix (Velo), SEM barra no final.
  // Ex.: 'https://dmaisdistribuidora.wixsite.com/dmais/_functions'
  // Enquanto estiver vazio, os formulários abrem o e-mail do visitante como alternativa.
  wixFunctionsUrl: '',
  // Ativado na versão de pré-visualização: mostra a mensagem de sucesso sem enviar nada.
  preview: false,
};

(() => {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];

  /* ---------- Contatos ---------- */
  $$('[data-cfg-href="tel"]').forEach(a => { a.href = `tel:${SITE.phoneLink}`; });
  $$('[data-cfg-href="mailto"]').forEach(a => { a.href = `mailto:${SITE.email}`; });
  $$('[data-cfg-href="wa"]').forEach(a => { a.href = `https://wa.me/${SITE.whatsapp}?text=${encodeURIComponent(SITE.whatsappText)}`; });
  $$('[data-year]').forEach(el => { el.textContent = new Date().getFullYear(); });

  /* ---------- Menu móvel ---------- */
  const toggle = $('.menu-toggle');
  const nav = $('#site-nav');
  const header = $('.header');
  if (toggle && nav) {
    const setMenu = open => {
      document.body.classList.toggle('nav-open', open);
      toggle.setAttribute('aria-expanded', String(open));
      toggle.setAttribute('aria-label', open ? 'Fechar menu' : 'Abrir menu');
      if (open) nav.style.setProperty('--nav-top', `${header.getBoundingClientRect().bottom}px`);
    };
    toggle.addEventListener('click', () => setMenu(!document.body.classList.contains('nav-open')));
    nav.addEventListener('click', e => { if (e.target.closest('a')) setMenu(false); });
    document.addEventListener('keydown', e => {
      if (e.key === 'Escape' && document.body.classList.contains('nav-open')) { setMenu(false); toggle.focus(); }
    });
  }

  /* ---------- Validação ---------- */
  const digits = v => v.replace(/\D/g, '');
  const isCNPJ = v => {
    const c = digits(v);
    if (c.length !== 14 || /^(\d)\1+$/.test(c)) return false;
    const calc = len => {
      let sum = 0, pos = len - 7;
      for (let i = len; i >= 1; i--) { sum += +c[len - i] * pos--; if (pos < 2) pos = 9; }
      const r = sum % 11;
      return r < 2 ? 0 : 11 - r;
    };
    return calc(12) === +c[12] && calc(13) === +c[13];
  };
  const isEmail = v => /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v.trim());
  const isPhone = v => digits(v).length >= 10;

  // Máscaras simples
  $$('[data-mask="cnpj"]').forEach(i => i.addEventListener('input', () => {
    const d = digits(i.value).slice(0, 14);
    i.value = d.replace(/^(\d{2})(\d)/, '$1.$2').replace(/^(\d{2})\.(\d{3})(\d)/, '$1.$2.$3').replace(/\.(\d{3})(\d)/, '.$1/$2').replace(/(\d{4})(\d)/, '$1-$2');
  }));
  $$('[data-mask="phone"]').forEach(i => i.addEventListener('input', () => {
    const d = digits(i.value).slice(0, 11);
    i.value = d.length > 10 ? d.replace(/^(\d{2})(\d{5})(\d{0,4})/, '($1) $2-$3') : d.replace(/^(\d{2})(\d{0,4})(\d{0,4})/, (m, a, b, c) => `(${a}) ${b}${c ? '-' + c : ''}`).replace(/\($/, '');
  }));

  /* ---------- Campos condicionais ---------- */
  const syncConditionals = form => {
    $$('[data-show-when]', form).forEach(box => {
      const rules = box.dataset.showWhen.split('|'); // "name=valor|name=valor"
      const on = rules.some(r => {
        const [name, val] = r.split('=');
        return $$(`[name="${name}"]`, form).some(i => i.checked && i.value === val);
      });
      box.hidden = !on;
      $$('input, textarea, select', box).forEach(i => { i.required = on && !i.hasAttribute('data-optional'); if (!on) { i.value = ''; i.removeAttribute('aria-invalid'); } });
    });
  };

  const setErr = (el, msg) => {
    const id = el.dataset.err || `err-${el.name}`;
    const out = document.getElementById(id);
    if (out) out.textContent = msg;
    if (el.setAttribute && el.type !== 'radio' && el.type !== 'checkbox') el.setAttribute('aria-invalid', msg ? 'true' : 'false');
    return !msg;
  };

  const validate = form => {
    let first = null;
    const fail = (el, msg) => { setErr(el, msg); if (!first) first = el; };
    // Campos de texto
    $$('input, textarea, select', form).forEach(el => {
      if (el.closest('[hidden]') || el.type === 'radio' || el.type === 'checkbox' || el.classList.contains('hp-input')) return;
      if (el.type === 'file') {
        const f = el.files[0];
        if (el.required && !f) return fail(el, 'Anexe o seu currículo.');
        if (f && f.size > 5 * 1024 * 1024) return fail(el, 'O arquivo deve ter no máximo 5 MB.');
        if (f && !/\.(pdf|docx?)$/i.test(f.name)) return fail(el, 'Envie o currículo em PDF ou Word (.doc, .docx).');
        return setErr(el, '');
      }
      const v = el.value.trim();
      if (el.required && !v) return fail(el, 'Campo obrigatório.');
      if (v && el.dataset.validate === 'cnpj' && !isCNPJ(v)) return fail(el, 'CNPJ inválido. Confira os números.');
      if (v && el.type === 'email' && !isEmail(v)) return fail(el, 'Informe um e-mail válido.');
      if (v && el.dataset.mask === 'phone' && !isPhone(v)) return fail(el, 'Informe o telefone com DDD.');
      setErr(el, '');
    });
    // Grupos de opção (radio / checkbox obrigatórios)
    $$('[data-group-required]', form).forEach(fs => {
      const inputs = $$('input', fs);
      const ok = inputs.some(i => i.checked);
      const out = document.getElementById(fs.dataset.groupRequired);
      if (out) out.textContent = ok ? '' : 'Selecione pelo menos uma opção.';
      if (!ok && !first) first = inputs[0];
    });
    // Consentimento LGPD
    const consent = $('[name="consentimento_lgpd"]', form);
    if (consent) {
      const out = document.getElementById('err-consent-' + form.id);
      if (out) out.textContent = consent.checked ? '' : 'Para enviar, é necessário aceitar o uso dos seus dados conforme a LGPD.';
      if (!consent.checked && !first) first = consent;
    }
    if (first) first.focus();
    return !first;
  };

  const collect = form => {
    const data = {};
    new FormData(form).forEach((v, k) => {
      if (v instanceof File) return;
      if (k in data) data[k] = [].concat(data[k], v); else data[k] = v;
    });
    $$('fieldset[data-multi]', form).forEach(fs => {
      const name = fs.dataset.multi;
      data[name] = $$(`input[name="${name}"]:checked`, form).map(i => i.value);
    });
    delete data._gotcha;
    if ($('[name="consentimento_lgpd"]', form)) data.consentimento_lgpd = true;
    data.pagina = location.pathname;
    return data;
  };

  const postJSON = async (path, body) => {
    const res = await fetch(`${SITE.wixFunctionsUrl}/${path}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
      body: JSON.stringify(body),
    });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return res.json().catch(() => ({}));
  };

  // Envio do currículo para a Mídia do Wix: pede um link de upload ao backend e envia o arquivo direto para ele.
  const uploadCV = async file => {
    const info = await postJSON('uploadUrl', { fileName: file.name, mimeType: file.type || 'application/octet-stream' });
    const fd = new FormData();
    fd.append('upload_token', info.uploadToken);
    fd.append('file', file, file.name);
    const res = await fetch(info.uploadUrl, { method: 'POST', body: fd });
    if (!res.ok) throw new Error(`Upload HTTP ${res.status}`);
    const out = await res.json().catch(() => null);
    const item = Array.isArray(out) ? out[0] : out;
    return (item && (item.file_url || item.fileUrl || item.url)) || '';
  };

  $$('form[data-form]').forEach(form => {
    syncConditionals(form);
    form.addEventListener('change', () => {
      syncConditionals(form);
      $$('[data-group-required]', form).forEach(fs => {
        if ($$('input', fs).some(i => i.checked)) { const out = document.getElementById(fs.dataset.groupRequired); if (out) out.textContent = ''; }
      });
    });
    form.addEventListener('input', e => { if (e.target.getAttribute('aria-invalid') === 'true') setErr(e.target, ''); });

    form.addEventListener('submit', async e => {
      e.preventDefault();
      const status = $('.form-status', form);
      status.className = 'form-status';
      status.textContent = '';
      if ($('.hp-input', form)?.value) return; // anti-spam
      if (!validate(form)) return;

      const kind = form.dataset.form; // "cliente" | "curriculo"
      const data = collect(form);
      const btn = $('[type="submit"]', form);
      btn.classList.add('is-loading');
      btn.disabled = true;
      try {
        if (SITE.preview) {
          await new Promise(r => setTimeout(r, 600));
        } else if (kind === 'denuncia') {
          if (SITE.denunciaEndpoint) {
            const res = await fetch(SITE.denunciaEndpoint, {
              method: 'POST',
              headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
              body: JSON.stringify({ _subject: `Canal de Denúncias: ${data.categoria} (${data.identificacao})`, ...data }),
            });
            if (!res.ok) throw new Error(`HTTP ${res.status}`);
          } else {
            const body = Object.entries(data).map(([k, v]) => `${k}: ${v}`).join('\n');
            location.href = `mailto:${SITE.denunciaEmail}?subject=${encodeURIComponent(`Canal de Denúncias: ${data.categoria}`)}&body=${encodeURIComponent(body)}`;
          }
        } else if (SITE.wixFunctionsUrl) {
          if (kind === 'curriculo') {
            const file = $('input[type="file"]', form).files[0];
            data.curriculoUrl = await uploadCV(file);
            data.curriculoNome = file.name;
            await postJSON('curriculos', data);
          } else {
            await postJSON('clientes', data);
          }
        } else {
          // Alternativa sem Wix configurado: abre o e-mail do visitante com os dados.
          const subject = kind === 'curriculo' ? `Trabalhe Conosco: ${data.nome || ''} (${data.cargo || ''})` : `Seja Cliente D'Mais: ${data.razao_social || ''}`;
          const body = Object.entries(data).map(([k, v]) => `${k}: ${Array.isArray(v) ? v.join(', ') : v}`).join('\n')
            + (kind === 'curriculo' ? '\n\n(Anexe o seu currículo a este e-mail.)' : '');
          location.href = `mailto:${SITE.email}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
        }
        form.reset();
        syncConditionals(form);
        status.classList.add('form-status--ok');
        status.textContent = {
          curriculo: 'Obrigado! Recebemos o seu currículo e entraremos em contato caso haja uma oportunidade compatível.',
          denuncia: 'Denúncia enviada à diretoria. Obrigado por nos ajudar a manter a D\'Mais íntegra e segura.',
        }[kind] || 'Obrigado! Recebemos o seu cadastro. Nossa equipe comercial entrará em contato em breve.';
      } catch (err) {
        status.classList.add('form-status--err');
        status.textContent = `Não foi possível enviar agora. Tente novamente ou fale conosco pelo WhatsApp ${SITE.whatsappDisplay}.`;
      } finally {
        btn.classList.remove('is-loading');
        btn.disabled = false;
      }
    });
  });
})();
