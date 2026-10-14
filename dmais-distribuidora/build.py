#!/usr/bin/env python3
"""Gera as páginas HTML do site D'Mais em ./site a partir de um cabeçalho/rodapé comum.

Uso: python3 build.py
Edite os textos aqui e rode o script de novo. As páginas geradas são o que vai para a hospedagem.
"""
import json
import datetime
from pathlib import Path

ROOT = Path(__file__).parent / "site"
DOMAIN = "https://www.dmais-distribuidora.com"
TODAY = datetime.date.today().isoformat()
REVIEW_URL = "https://g.page/r/Cbg4QoJDhWQmEAE/review"
WA = "https://wa.me/5511993719036"
SOCIAL = {
    "WhatsApp": WA,
    "Instagram": "https://www.instagram.com/dmaisdistribuidorapetroleo/",
    "LinkedIn": "https://www.linkedin.com/company/dmais-distribuidora/",
    "Facebook": "https://www.facebook.com/profile.php?id=100094870415622",
}
ADDRESS = {"street": "Av. Senador Onofre Quinan, 763, Sala 02, Cascata", "city": "Paulínia", "region": "SP", "country": "BR"}

ICONS = """
<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">
  <defs>
    <symbol id="i-phone" viewBox="0 0 24 24"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></symbol>
    <symbol id="i-wa" viewBox="0 0 24 24"><path fill="currentColor" stroke="none" d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413Z"/></symbol>
    <symbol id="i-mail" viewBox="0 0 24 24"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/></symbol>
    <symbol id="i-pin" viewBox="0 0 24 24"><path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></symbol>
    <symbol id="i-clock" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></symbol>
    <symbol id="i-arrow" viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></symbol>
    <symbol id="i-check" viewBox="0 0 24 24"><path d="M20 6 9 17l-5-5"/></symbol>
    <symbol id="i-menu" viewBox="0 0 24 24"><path d="M4 6h16M4 12h16M4 18h16"/></symbol>
    <symbol id="i-x" viewBox="0 0 24 24"><path d="M18 6 6 18M6 6l12 12"/></symbol>
    <symbol id="i-alert" viewBox="0 0 24 24"><path d="M7.9 2h8.2L22 7.9v8.2L16.1 22H7.9L2 16.1V7.9z"/><path d="M12 8v5M12 16.5h.01"/></symbol>
    <symbol id="i-shield" viewBox="0 0 24 24"><path d="M20 13c0 5-3.5 7.5-7.7 9a1 1 0 0 1-.7 0C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.2-2.7a1.2 1.2 0 0 1 1.6 0C14.5 3.8 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/></symbol>
    <symbol id="i-bolt" viewBox="0 0 24 24"><path d="M13 2 3 14h9l-1 8 10-12h-9z"/></symbol>
    <symbol id="i-hand" viewBox="0 0 24 24"><path d="m11 17 2 2a1 1 0 1 0 3-3"/><path d="m14 14 2.5 2.5a1 1 0 1 0 3-3l-3.9-3.9a3 3 0 0 0-4.2 0l-.9.9a1 1 0 1 1-3-3l2.8-2.8a5.8 5.8 0 0 1 7.1-.9l.5.3a2 2 0 0 0 1.4.2L21 4"/><path d="m21 3 1 11h-2M3 3 2 14l6.5 6.5a1 1 0 1 0 3-3M3 4h8"/></symbol>
    <symbol id="i-truck" viewBox="0 0 24 24"><path d="M14 18V6a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v11a1 1 0 0 0 1 1h2M15 18H9M19 18h2a1 1 0 0 0 1-1v-3.6a1 1 0 0 0-.2-.6l-3.5-4.4A1 1 0 0 0 17.5 8H14"/><circle cx="17" cy="18" r="2"/><circle cx="7" cy="18" r="2"/></symbol>
    <symbol id="i-gps" viewBox="0 0 24 24"><circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3"/><circle cx="12" cy="12" r="7"/></symbol>
    <symbol id="i-wrench" viewBox="0 0 24 24"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.8-3.8a6 6 0 0 1-7.9 7.9l-6.9 6.9a2.1 2.1 0 0 1-3-3l6.9-6.9a6 6 0 0 1 7.9-7.9z"/></symbol>
    <symbol id="i-users" viewBox="0 0 24 24"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/></symbol>
    <symbol id="i-star" viewBox="0 0 24 24"><path d="m12 2 3.1 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8 5.8 21l1.2-6.8-5-4.9 6.9-1z"/></symbol>
    <symbol id="i-ig" viewBox="0 0 24 24"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><path d="M17.5 6.5h.01"/></symbol>
    <symbol id="i-in" viewBox="0 0 24 24"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-4 0v7h-4v-7a6 6 0 0 1 6-6zM2 9h4v12H2z"/><circle cx="4" cy="4" r="2"/></symbol>
    <symbol id="i-fb" viewBox="0 0 24 24"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></symbol>
    <symbol id="i-file" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h5"/></symbol>
    <symbol id="i-leaf" viewBox="0 0 24 24"><path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.5 19 2c1 2 2 4.2 2 8 0 5.5-4.8 10-10 10z"/><path d="M2 21c0-3 1.9-5.4 5.2-6"/></symbol>
  </defs>
</svg>"""

NAV = [
    ("/#produtos", "Produtos", None),
    ("/#sobre", "Sobre nós", None),
    ("/rede-de-postos", "Rede de Postos", "rede"),
    ("/fornecedores", "Fornecedores", "fornecedores"),
    ("/transportadora", "Transportadora", "transportadora"),
    ("/perguntas-frequentes", "Perguntas Frequentes", "faq"),
    ("/trabalhe-conosco", "Trabalhe Conosco", "trabalhe"),
]


def ic(name, cls="ic"):
    return f'<svg class="{cls}" aria-hidden="true"><use href="#i-{name}"/></svg>'


def head(page):
    url = DOMAIN + page["path"]
    schema = json.dumps({"@context": "https://schema.org", "@graph": page["schema"]}, ensure_ascii=False, indent=2).replace("</", "<\\/")
    preload = page.get("preload", "")
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{page['title']}</title>
  <meta name="description" content="{page['description']}">
  <link rel="canonical" href="{url}">
  <meta name="theme-color" content="#021358">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="pt_BR">
  <meta property="og:site_name" content="D'Mais Distribuidora de Petróleo">
  <meta property="og:url" content="{url}">
  <meta property="og:title" content="{page['title']}">
  <meta property="og:description" content="{page['description']}">
  <meta property="og:image" content="{DOMAIN}/assets/img/og.jpg">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="/favicon.ico" sizes="any">
  <link rel="icon" type="image/png" sizes="32x32" href="/assets/img/favicon-32.png">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <link rel="manifest" href="/site.webmanifest">
  <link rel="preload" href="/assets/fonts/inter.woff2" as="font" type="font/woff2" crossorigin>
{preload}  <link rel="stylesheet" href="/assets/css/styles.css">
  <script src="/assets/js/main.js" defer></script>
  <script type="application/ld+json">
{schema}
  </script>
</head>
"""


CUR = ' aria-current="page"'


def header(active):
    links = "\n".join(
        f'        <a href="{href}"{CUR if key == active else ""}>{label}</a>' for href, label, key in NAV
    )
    return f"""<body>
  <a class="skip-link" href="#main">Pular para o conteúdo</a>
{ICONS}
  <div class="topbar">
    <div class="container topbar__inner">
      <a data-cfg-href="wa" href="{WA}" target="_blank" rel="noopener">{ic('wa')}Suporte 24h: (11) 99371-9036</a>
      <a class="topbar__hide-sm" data-cfg-href="tel" href="tel:+551940090659">{ic('phone')}(19) 4009-0659</a>
      <a class="topbar__hide-sm" data-cfg-href="mailto" href="mailto:contato@dmais-distribuidora.com">{ic('mail')}contato@dmais-distribuidora.com</a>
      <span class="topbar__push topbar__hide-sm">{ic('clock')}Seg–Sex 6h–18h · Sáb 6h–11h</span>
    </div>
  </div>

  <header class="header">
    <div class="container header__inner">
      <a class="brand" href="/" aria-label="D'Mais Distribuidora de Petróleo, página inicial">
        <img src="/assets/img/logo-dplus.webp" width="345" height="202" alt="Logo D+ da D'Mais Distribuidora">
        <span class="brand__text"><span class="brand__name">D'MAIS DISTRIBUIDORA</span><span class="brand__sub">Distribuidora de Petróleo · São Paulo</span></span>
      </a>
      <nav class="nav" id="site-nav" aria-label="Principal">
{links}
        <a class="btn btn--blue" href="/#seja-cliente">Seja Cliente</a>
      </nav>
      <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="Abrir menu">
        {ic('menu', 'ic ic-open')}{ic('x', 'ic ic-close')}
      </button>
    </div>
  </header>
"""


def footer():
    soc = "".join(
        f'<a href="{u}" target="_blank" rel="noopener" aria-label="D\'Mais no {n}">{ic({"WhatsApp": "wa", "Instagram": "ig", "LinkedIn": "in", "Facebook": "fb"}[n])}</a>'
        for n, u in SOCIAL.items()
    )
    return f"""
  <section class="cta" aria-labelledby="cta-title">
    <div class="container cta__inner">
      <div>
        <h2 id="cta-title">Seja você também um cliente D'Mais</h2>
        <p>Combustível de qualidade, logística própria e atendimento próximo para o seu posto.</p>
      </div>
      <div class="cta__actions">
        <a class="btn btn--blue btn--lg" href="/#seja-cliente">Quero ser cliente {ic('arrow')}</a>
        <a class="btn btn--ghost btn--lg" data-cfg-href="wa" href="{WA}" target="_blank" rel="noopener">{ic('wa')}WhatsApp</a>
      </div>
    </div>
  </section>

  <footer class="footer">
    <div class="container footer__grid">
      <div class="footer__brand">
        <img src="/assets/img/logo-dplus.webp" width="345" height="202" alt="Logo D+ da D'Mais Distribuidora" loading="lazy">
        <p class="footer__slogan">"Qualidade é o nosso combustível &amp; sua segurança é o nosso motor."</p>
        <div class="social">{soc}</div>
      </div>
      <div>
        <h2>Contato</h2>
        <ul>
          <li><a data-cfg-href="tel" href="tel:+551940090659">(19) 4009-0659</a></li>
          <li><a data-cfg-href="wa" href="{WA}" target="_blank" rel="noopener">WhatsApp (11) 99371-9036</a></li>
          <li><a data-cfg-href="mailto" href="mailto:contato@dmais-distribuidora.com">contato@dmais-distribuidora.com</a></li>
          <li><address>Av. Senador Onofre Quinan, 763, Sala 02<br>Cascata, Paulínia - SP</address></li>
        </ul>
      </div>
      <div>
        <h2>Navegação</h2>
        <ul>
          <li><a href="/#produtos">Produtos</a></li>
          <li><a href="/#sobre">Sobre nós</a></li>
          <li><a href="/rede-de-postos">Rede de Postos</a></li>
          <li><a href="/fornecedores">Fornecedores</a></li>
          <li><a href="/transportadora">Transportadora</a></li>
          <li><a href="/perguntas-frequentes">Perguntas Frequentes</a></li>
          <li><a href="/trabalhe-conosco">Trabalhe Conosco</a></li>
          <li><a href="/canal-de-denuncias">Canal de Denúncias</a></li>
          <li><a href="/politica-de-privacidade">Política de Privacidade (LGPD)</a></li>
        </ul>
      </div>
      <div>
        <h2>Horários</h2>
        <dl class="hours">
          <div><dt>Segunda a sexta</dt><dd>6h às 18h</dd></div>
          <div><dt>Sábado</dt><dd>6h às 11h</dd></div>
          <div><dt>Suporte WhatsApp</dt><dd>24 horas</dd></div>
        </dl>
        <p style="margin-top:16px">Sua avaliação é muito importante para nós. <a href="{REVIEW_URL}" target="_blank" rel="noopener"><strong>Avalie nosso serviço no Google</strong></a>.</p>
      </div>
    </div>
    <div class="container">
      <div class="report-band">
        <span class="report-band__icon">{ic('shield')}</span>
        <div>
          <h2>Canal de Denúncias</h2>
          <p>Presenciou alguma irregularidade, fraude, assédio ou risco à segurança? Relate de forma anônima ou identificada. As denúncias vão direto para a diretoria e são tratadas com sigilo.</p>
        </div>
        <a class="btn btn--yellow" href="/canal-de-denuncias">Fazer uma denúncia {ic('arrow')}</a>
      </div>
    </div>
    <div class="container footer__bottom">
      <p>© <span data-year>2026</span> D'Mais Distribuidora de Petróleo Ltda. Todos os direitos reservados.</p>
      <a href="/politica-de-privacidade">Política de Privacidade (LGPD)</a>
    </div>
  </footer>

  <div class="float-stack">
    <a class="float-btn float-btn--mail" data-cfg-href="mailto" href="mailto:contato@dmais-distribuidora.com" aria-label="Enviar e-mail para a D'Mais"><span class="float-btn__tip">E-mail</span>{ic('mail')}</a>
    <a class="float-btn float-btn--phone" data-cfg-href="tel" href="tel:+551940090659" aria-label="Ligar para a D'Mais: (19) 4009-0659"><span class="float-btn__tip">(19) 4009-0659</span>{ic('phone')}</a>
    <a class="float-btn float-btn--wa" data-cfg-href="wa" href="{WA}" target="_blank" rel="noopener" aria-label="Falar com a D'Mais pelo WhatsApp"><span class="float-btn__tip">WhatsApp 24h</span>{ic('wa')}</a>
  </div>
  <nav class="mbar" aria-label="Contato rápido">
    <a data-cfg-href="tel" href="tel:+551940090659">{ic('phone')}Ligar</a>
    <a data-cfg-href="wa" href="{WA}" target="_blank" rel="noopener">{ic('wa')}WhatsApp</a>
    <a data-cfg-href="mailto" href="mailto:contato@dmais-distribuidora.com">{ic('mail')}E-mail</a>
    <a class="mbar__primary" href="/#seja-cliente">{ic('arrow')}Seja Cliente</a>
  </nav>
</body>
</html>
"""


def consent(form_id):
    return f"""          <label class="consent"><input type="checkbox" name="consentimento_lgpd" value="sim" required>
            <span>Autorizo a D'Mais Distribuidora a usar os dados informados para responder a esta solicitação, conforme a Lei Geral de Proteção de Dados (LGPD, Lei nº 13.709/2018) e a nossa <a href="/politica-de-privacidade">Política de Privacidade</a>. <span class="req">*</span></span></label>
          <p class="field-error" id="err-consent-{form_id}" role="alert"></p>"""


def field(name, label, type_="text", auto="", extra="", full=False, required=True):
    req = ' <span class="req" aria-hidden="true">*</span>' if required else ""
    ac = f' autocomplete="{auto}"' if auto else ""
    style = ' style="grid-column:1/-1"' if full else ""
    return f"""            <div class="field"{style}><label for="f-{name}">{label}{req}</label><input class="input" id="f-{name}" name="{name}" type="{type_}"{ac}{' required' if required else ''} aria-describedby="err-{name}"{extra}><p class="field-error" id="err-{name}"></p></div>"""


# ---------------------------------------------------------------- Dados
PRODUCTS = [
    {
        "id": "gasolina-comum", "name": "Gasolina comum", "img": "gota-gasolina-comum", "drop": "gota laranja",
        "short": "Para automóveis, motos e embarcações, com índice antidetonante mínimo de 87 e mistura de etanol anidro conforme a lei.",
        "long": "É a gasolina utilizada em automóveis, motos e embarcações aquáticas, com índice antidetonante (IAD) maior ou igual a 87, conforme as especificações da ANP. Segundo as normas da ANP, esta gasolina deve ser preparada pela distribuidora, que recebe a gasolina do tipo A, fornecida pelas refinarias, e adiciona o etanol anidro. A porcentagem de etanol anidro na gasolina final é definida pela legislação vigente: atualmente 32% do volume (Lei nº 14.993/2024, a Lei do Combustível do Futuro, e resolução do CNPE em vigor desde 1º de agosto de 2026).",
    },
    {
        "id": "gasolina-aditivada", "name": "Gasolina aditivada", "img": "gota-gasolina-aditivada", "drop": "gota azul",
        "short": "Enriquecida com aditivos que mantêm limpos bicos injetores, válvulas e câmara de combustão.",
        "long": "A gasolina aditivada é enriquecida com produtos aditivos que conferem características especiais. Esses aditivos têm a finalidade de manter limpos todos os componentes em contato com o combustível, como bicos injetores, válvulas, câmara, cabeçote e carburador. Essa abordagem única assegura que a gasolina aditivada mantenha a qualidade superior da gasolina comum, sendo uma escolha que contribui para o bom funcionamento e a longevidade do motor.",
    },
    {
        "id": "etanol", "name": "Etanol", "img": "gota-etanol", "drop": "gota verde",
        "short": "Combustível renovável, extraído da cana-de-açúcar, que combina eficiência e respeito ao meio ambiente.",
        "long": "O etanol hidratado é um combustível de origem não petrolífera. Extraído através da fermentação da cana-de-açúcar em usinas sucroalcooleiras, seu processo resulta em um produto final incolor. Como alternativa sustentável, o etanol contribui para um futuro mais limpo, combinando eficiência e respeito pelo meio ambiente.",
    },
    {
        "id": "diesel-s10", "name": "Diesel S10", "img": "gota-diesel-s10", "drop": "gota âmbar",
        "short": "Baixo teor de enxofre, mais cetano e menos emissões, ideal para veículos fabricados a partir de 2012.",
        "long": "O Diesel S-10, que sucede o S-50, se destaca por possuir um menor teor de enxofre, resultando em benefícios ambientais substanciais. Esse diesel de baixo teor de enxofre é especialmente eficaz em veículos fabricados a partir de 2012, equipados com tecnologia avançada de redução de emissões veiculares, alinhados com as diretrizes do Programa de Controle da Poluição do Ar por Veículos Automotores (Proconve), na fase P7. Além do teor de enxofre reduzido, o Diesel S-10 apresenta um número de cetano mais alto, resultando em melhor partida a frio, redução de fumaça branca, menor formação de depósitos e maior vida útil do óleo lubrificante. Esses aprimoramentos oferecem vantagens visíveis, perceptíveis pelos motoristas, inclusive em motores mais antigos, anteriores a 2012.",
    },
    {
        "id": "diesel-s500", "name": "Diesel S500", "img": "gota-diesel-s500", "drop": "gota vermelha",
        "short": "Energia confiável para transporte, máquinas e motores a diesel de todos os portes.",
        "long": "O óleo diesel S500 desempenha um papel crucial no setor de transportes do Brasil, alimentando uma diversidade de aplicações em motores de combustão interna e ignição por compressão. Encontrado em veículos que variam de automóveis a grandes máquinas industriais, este combustível é uma força motriz que impulsiona a economia do país. Através do diesel S500, oferecemos uma fonte confiável de energia, assegurando sua qualidade, clareza e pureza para otimizar o desempenho e prolongar a vida útil dos motores.",
    },
]

STATIONS = [
    ("Auto Posto D+ II", "Estr. Fernando Nobre, 749 - 3 - Parque Rincão", "Cotia - SP", "(11) 4612-3687", "+551146123687"),
    ("Auto Posto Caucaia", "Av. Roque Celestino Pires, 1142 - Centro (Caucaia do Alto)", "Cotia - SP", "(11) 4611-7887", "+551146117887"),
    ("Auto Posto Trilha do Verde", "Av. Ivo Mário Isaac Pires - Tijuco Preto", "Vargem Grande Paulista - SP", "(11) 4158-4560", "+551141584560"),
    ("Auto Posto Rota 66", "Av. Roque Celestino Pires, 959 - Caucaia do Alto", "Cotia - SP", "(11) 4611-4909", "+551146114909"),
    ("Auto Posto V12", "Av. Guilherme Cotching - Vila Maria", "São Paulo - SP", "(11) 2954-4435", "+551129544435"),
    ("Auto Posto D+", "Av. José Giorgi, 280 - Granja Viana", "Cotia - SP", "(11) 4702-3922", "+551147023922"),
]

BASES = [
    ("Matriz", "Base Atlanta D'Mais", "Paulínia - SP", True,
     [("Gasolina", "REPLAN (Refinaria de Paulínia)"), ("Diesel S10 e S500", "REPLAN (Refinaria de Paulínia)"), ("Biodiesel", "Cargill"), ("Etanol", "Copersucar e Usina Santa Isabel")]),
    ("Filial", "Base Baguar", "Guarulhos - SP", False,
     [("Gasolina", "REVAP (Refinaria do Vale do Paraíba, SJC)"), ("Diesel S10 e S500", "REVAP (Refinaria do Vale do Paraíba, SJC)"), ("Biodiesel", "Cargill"), ("Etanol", "Copersucar e Usina Santa Isabel")]),
    ("Filial", "Base BAVAP", "São José dos Campos - SP", False,
     [("Gasolina", "REVAP (Refinaria do Vale do Paraíba, SJC)"), ("Diesel S10 e S500", "REVAP (Refinaria do Vale do Paraíba, SJC)"), ("Biodiesel", "Cargill"), ("Etanol", "Copersucar e Usina Santa Isabel")]),
]

REVIEWS = [
    ("Excelente atendimento.", "Posto Nova São Joa", ""),
    ("Atendimento rápido e com qualidade de bombeio BR.", "Marcelo R.", ""),
    ("Excelente distribuidora, parceria de uns 15 anos. Ótimo atendimento, super recomendo.", "Allan R.", ""),
]

ORG = {
    "@type": ["Organization", "LocalBusiness"],
    "@id": DOMAIN + "/#empresa",
    "name": "D'Mais Distribuidora de Petróleo Ltda.",
    "alternateName": ["D'Mais Distribuidora", "D+ Distribuidora"],
    "url": DOMAIN + "/",
    "logo": DOMAIN + "/assets/img/icon-512.png",
    "image": DOMAIN + "/assets/img/og.jpg",
    "slogan": "Qualidade é o nosso combustível & sua segurança é o nosso motor.",
    "description": "Distribuidora de combustíveis para postos bandeira branca no estado de São Paulo: gasolina comum e aditivada, etanol, diesel S10 e S500, com logística própria.",
    "telephone": "+55-19-4009-0659",
    "email": "contato@dmais-distribuidora.com",
    "address": {"@type": "PostalAddress", "streetAddress": ADDRESS["street"], "addressLocality": ADDRESS["city"], "addressRegion": ADDRESS["region"], "addressCountry": ADDRESS["country"]},
    "areaServed": {"@type": "State", "name": "São Paulo"},
    "foundingDate": "2005",
    "openingHoursSpecification": [
        {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "06:00", "closes": "18:00"},
        {"@type": "OpeningHoursSpecification", "dayOfWeek": "Saturday", "opens": "06:00", "closes": "11:00"},
    ],
    "contactPoint": [
        {"@type": "ContactPoint", "contactType": "customer support", "telephone": "+55-11-99371-9036", "availableLanguage": "pt-BR", "hoursAvailable": {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "00:00", "closes": "23:59"}},
        {"@type": "ContactPoint", "contactType": "sales", "telephone": "+55-19-4009-0659", "email": "contato@dmais-distribuidora.com", "availableLanguage": "pt-BR"},
    ],
    "employee": {"@id": DOMAIN + "/#diretor"},
    "sameAs": [SOCIAL["Instagram"], SOCIAL["LinkedIn"], SOCIAL["Facebook"]],
    "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Combustíveis", "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Product", "name": p["name"], "description": p["short"]}} for p in PRODUCTS]},
}
DIRECTOR = {"@type": "Person", "@id": DOMAIN + "/#diretor", "name": "José Luis Fernandes Velho", "jobTitle": "Diretor Presidente", "worksFor": {"@id": DOMAIN + "/#empresa"}}
WEBSITE = {"@type": "WebSite", "@id": DOMAIN + "/#site", "url": DOMAIN + "/", "name": "D'Mais Distribuidora de Petróleo", "inLanguage": "pt-BR", "publisher": {"@id": DOMAIN + "/#empresa"}}


def crumbs(name, path):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Início", "item": DOMAIN + "/"},
        {"@type": "ListItem", "position": 2, "name": name, "item": DOMAIN + path}]}


def page_hero(eyebrow, h1, text, crumb):
    return f"""  <main id="main">
    <section class="page-hero">
      <div class="container">
        <nav class="breadcrumb" aria-label="Você está em"><a href="/">Início</a> / {crumb}</nav>
        <p class="eyebrow">{eyebrow}</p>
        <h1>{h1}</h1>
        <p>{text}</p>
      </div>
    </section>
"""


# ---------------------------------------------------------------- Página inicial
def home():
    vinculo = "".join(f'<label class="choice"><input type="radio" name="vinculo" value="{v}" required>{v}</label>' for v in ["Colaborador com registro", "Procurador", "Proprietário", "Outro"])
    origem = "".join(f'<label class="choice"><input type="checkbox" name="como_conheceu" value="{v}">{v}</label>' for v in ["Rede social", "Indicação de cliente", "Televendas", "Indicação de vendedor", "Outros"])
    prods = "\n".join(f"""        <article class="prod">
          <div class="prod__media"><img src="/assets/img/{p['img']}.webp" width="400" height="500" alt="{p['name']}: {p['drop']} de combustível" loading="lazy"></div>
          <div class="prod__body">
            <h3>{p['name']}</h3>
            <p>{p['short']}</p>
            <a class="prod__link" href="/perguntas-frequentes#{p['id']}">Saiba mais<span class="sr-only"> sobre {p['name']}</span> {ic('arrow')}</a>
          </div>
        </article>""" for p in PRODUCTS)
    reviews = "\n".join(f"""        <figure class="review">
          <div class="review__stars" aria-label="5 de 5 estrelas">★★★★★</div>
          <blockquote>“{t}”</blockquote>
          <figcaption><strong>{n}</strong>Avaliação no Google</figcaption>
        </figure>""" for t, n, _ in REVIEWS)
    body = f"""  <main id="main">
    <!-- HERO + FORMULÁRIO SEJA CLIENTE -->
    <section class="hero" id="seja-cliente" aria-labelledby="hero-title">
      <img class="hero__img" src="/assets/img/hero.webp" srcset="/assets/img/hero-960.webp 960w, /assets/img/hero.webp 1672w" sizes="100vw" width="1672" height="941" alt="Caminhão-tanque da D'Mais Distribuidora em frente aos tanques de armazenamento de combustível ao pôr do sol" fetchpriority="high">
      <div class="container hero__grid">
        <div class="hero__copy">
          <p class="hero__badge">Distribuidora de combustíveis · Postos bandeira branca · SP</p>
          <h1 id="hero-title">Qualidade é o nosso combustível e <span>sua segurança, o nosso motor.</span></h1>
          <p class="hero__lead">Distribuidora de combustíveis para postos bandeira branca no estado de São Paulo: gasolina, etanol e diesel com garantia de origem, logística própria e atendimento próximo, com consistência, rapidez e parceria para garantir previsibilidade e confiança no seu abastecimento.</p>
          <div class="hero__ctas">
            <a class="btn btn--yellow btn--lg" href="#form-cliente">Quero ser cliente {ic('arrow')}</a>
            <a class="btn btn--ghost btn--lg" href="#produtos">Ver produtos</a>
          </div>
          <ul class="hero__points" aria-label="Vantagens">
            <li><span class="dot" aria-hidden="true"></span><div><strong>Consistência no fornecimento</strong><span>Menos rupturas e mais previsibilidade operacional.</span></div></li>
            <li><span class="dot" aria-hidden="true"></span><div><strong>Rapidez e flexibilidade</strong><span>Respostas ágeis para as necessidades do dia a dia.</span></div></li>
            <li><span class="dot" aria-hidden="true"></span><div><strong>Parceiro local</strong><span>Conhecimento do negócio e suporte próximo.</span></div></li>
          </ul>
        </div>

        <form class="form-card form-card--glass" id="form-cliente" data-form="cliente" novalidate>
          <h2 class="form-card__title">Seja você também um cliente D'Mais</h2>
          <p class="form-card__sub">Preencha o formulário e nossa equipe comercial entrará em contato. Todos os campos são obrigatórios.</p>
          <div class="hp" aria-hidden="true"><label>Não preencha<input class="hp-input" name="_gotcha" tabindex="-1" autocomplete="off"></label></div>
          <div class="grid-2">
{field('razao_social', 'Razão Social', auto='organization')}
{field('cnpj', 'CNPJ', extra=' inputmode="numeric" data-mask="cnpj" data-validate="cnpj" placeholder="00.000.000/0000-00"')}
{field('inscricao_estadual', 'Inscrição Estadual')}
{field('endereco', 'Endereço', auto='street-address')}
{field('email', 'E-mail', 'email', 'email')}
{field('telefone', 'Telefone', 'tel', 'tel', ' inputmode="tel" data-mask="phone" placeholder="(11) 99999-9999"')}
{field('responsavel', 'Responsável pelo contato', auto='name')}
{field('cargo', 'Cargo na empresa', auto='organization-title')}
          </div>
          <fieldset class="fieldset" data-group-required="err-vinculo">
            <legend>Selecione uma opção abaixo <span class="req">*</span></legend>
            <div class="choices">{vinculo}</div>
            <p class="field-error" id="err-vinculo" role="alert"></p>
            <div class="conditional field" data-show-when="vinculo=Outro" hidden><label for="f-vinculo_outro">Especifique <span class="req">*</span></label><input class="input" id="f-vinculo_outro" name="vinculo_outro" aria-describedby="err-vinculo_outro"><p class="field-error" id="err-vinculo_outro"></p></div>
          </fieldset>
          <fieldset class="fieldset" data-group-required="err-como_conheceu" data-multi="como_conheceu">
            <legend>Por onde nos conheceu? <span class="req">*</span></legend>
            <div class="choices">{origem}</div>
            <p class="field-error" id="err-como_conheceu" role="alert"></p>
            <div class="conditional field" data-show-when="como_conheceu=Indicação de vendedor" hidden><label for="f-nome_vendedor">Nome do vendedor <span class="req">*</span></label><input class="input" id="f-nome_vendedor" name="nome_vendedor" aria-describedby="err-nome_vendedor"><p class="field-error" id="err-nome_vendedor"></p></div>
            <div class="conditional field" data-show-when="como_conheceu=Outros|como_conheceu=Indicação de cliente" hidden><label for="f-como_conheceu_detalhe">Especifique (quem indicou ou outro meio) <span class="req">*</span></label><input class="input" id="f-como_conheceu_detalhe" name="como_conheceu_detalhe" aria-describedby="err-como_conheceu_detalhe"><p class="field-error" id="err-como_conheceu_detalhe"></p></div>
          </fieldset>
{consent('form-cliente')}
          <div class="form-actions"><button class="btn btn--blue btn--lg btn--block" type="submit">Enviar cadastro {ic('arrow')}</button></div>
          <p class="form-status" role="status" aria-live="polite"></p>
        </form>
      </div>
    </section>

    <!-- CONTATO -->
    <section class="contact-strip" aria-label="Contato e horários">
      <div class="container contact-strip__grid">
        <a class="c-tile" data-cfg-href="wa" href="{WA}" target="_blank" rel="noopener"><span class="c-tile__icon">{ic('wa')}</span><div><strong>WhatsApp · Suporte 24h</strong><span>(11) 99371-9036</span><small>Atendimento personalizado</small></div></a>
        <a class="c-tile" data-cfg-href="tel" href="tel:+551940090659"><span class="c-tile__icon">{ic('phone')}</span><div><strong>Telefone</strong><span>(19) 4009-0659</span><small>Comercial e atendimento</small></div></a>
        <a class="c-tile" data-cfg-href="mailto" href="mailto:contato@dmais-distribuidora.com"><span class="c-tile__icon">{ic('mail')}</span><div><strong>E-mail</strong><span>contato@dmais-distribuidora.com</span><small>E-mail oficial da D'Mais</small></div></a>
        <div class="c-tile"><span class="c-tile__icon">{ic('clock')}</span><div><strong>Horário de funcionamento</strong><span>Seg a sex: 6h às 18h</span><span>Sábado: 6h às 11h</span></div></div>
      </div>
    </section>

    <!-- VANTAGENS + ALERTA DE FRAUDE -->
    <section class="section section--soft" aria-labelledby="vantagens-title">
      <div class="container split">
        <div>
          <p class="eyebrow">Por que escolher a D'Mais</p>
          <h2 class="h2" id="vantagens-title">Uma operação montada para proteger a reputação do seu posto</h2>
          <p class="lead">Combustível com padrão e garantia de qualidade, entrega ágil e atendimento humano para postos bandeira branca.</p>
          <div class="adv-grid" style="margin-top:28px">
            <article class="adv"><span class="adv__icon">{ic('shield')}</span><span class="adv__tag">Qualidade</span><h3>Produto com padrão e confiança</h3><p>Saiba exatamente o produto que está fornecendo ao seu cliente, com bombeio Petrobras.</p></article>
            <article class="adv"><span class="adv__icon">{ic('bolt')}</span><span class="adv__tag">Agilidade</span><h3>Entregas e resposta rápida</h3><p>Velocidade e flexibilidade para atender urgências e ajustes de demanda.</p></article>
            <article class="adv"><span class="adv__icon">{ic('hand')}</span><span class="adv__tag">Parceria</span><h3>Suporte próximo ao cliente</h3><p>Atendimento humano, direto e focado na melhoria contínua.</p></article>
            <article class="adv"><span class="adv__icon">{ic('truck')}</span><span class="adv__tag">Logística própria</span><h3>Segurança no abastecimento</h3><p>Frota rastreada e manutenção preventiva gerida pela D'Mais.</p></article>
          </div>
        </div>
        <aside class="alert" aria-labelledby="fraude-title">
          <div class="alert__head"><span class="alert__icon">{ic('alert')}</span><h3 id="fraude-title">Alerta de fraude: fique atento!</h3></div>
          <p><strong>Prezados clientes,</strong> identificamos uma tentativa de golpe envolvendo o envio de boletos falsos em nome da D'Mais, via WhatsApp, alegando "reajuste de imposto".</p>
          <p>Reforçamos que:</p>
          <ul>
            <li>A D'Mais <strong>nunca</strong> envia boletos por WhatsApp.</li>
            <li>Todos os boletos são emitidos junto com as respectivas notas fiscais.</li>
            <li>O envio é feito exclusivamente pelo nosso e-mail oficial: <strong>@dmais-distribuidora.com</strong></li>
          </ul>
          <p>Caso receba qualquer mensagem suspeita ou boleto fora do nosso padrão, <strong>NÃO PAGUE</strong> e entre em contato imediatamente com o nosso time.</p>
          <a class="btn btn--blue" data-cfg-href="tel" href="tel:+551940090659" style="margin-top:8px">{ic('phone')}Confirmar com a D'Mais</a>
        </aside>
      </div>
    </section>

    <!-- PRODUTOS -->
    <section class="section" id="produtos" aria-labelledby="produtos-title">
      <div class="container">
        <div class="section-head section-head--center">
          <p class="eyebrow">Nossos produtos</p>
          <h2 class="h2" id="produtos-title">Combustíveis com garantia de origem</h2>
          <p class="lead">Apesar de o combustível ser uma commodity, prezamos pela qualidade de produtos de bombeio Petrobras, do tanque da base ao tanque do seu posto.</p>
        </div>
        <div class="prod-grid">
{prods}
        </div>
        <div class="petro-note"><p>Dúvidas sobre especificações, mistura de etanol ou qual diesel usar?</p><a class="btn btn--yellow" href="/perguntas-frequentes">Ver perguntas frequentes {ic('arrow')}</a></div>
      </div>
    </section>

    <!-- SOBRE NÓS -->
    <section class="section section--deep" id="sobre" aria-labelledby="sobre-title">
      <div class="container">
        <div class="about">
          <div class="about__text">
            <p class="eyebrow">Sobre nós</p>
            <h2 class="h2" id="sobre-title">Mais de 20 anos distribuindo confiança</h2>
            <p class="lead">Há mais de 20 anos, a D'Mais atua no mercado de combustíveis com excelência, confiabilidade e compromisso, construindo relações baseadas em responsabilidade e respeito aos seus clientes.</p>
            <p style="margin-top:18px">Tudo teve início quando, em 1968, o Sr. Moisés de Matos Velho ingressou no ramo de revenda de combustíveis e, ao montar o Auto Posto Caucaia, em 1978, em Caucaia do Alto, distrito de Cotia-SP, iniciou a história da marca que mudou nossas vidas: a D+. A Rede de Postos D+ conta hoje com seis postos consolidados. Para mais informações, acesse a <a href="/rede-de-postos">Rede de Postos</a>.</p>
            <p>Ao longo dos anos, nossa dedicação incansável ao progresso floresceu em sucessos notáveis. Em 2005, a D+ abriu novos horizontes ao entrar no setor de distribuição de petróleo, consolidada pela interligação com a REPLAN. Com o tempo, crescemos e expandimos nossa presença em Guarulhos, através da REVAP, e, em 2008, selamos nosso primeiro contrato de venda de gasolina e diesel. Logo depois, expandimos nossas operações para São José dos Campos, em 2012, e fomos honrados com o reconhecimento da Petrobras pelo desempenho exemplar da distribuidora.</p>
            <ol class="timeline" aria-label="Linha do tempo">
              <li><strong>1968</strong><span>Sr. Moisés de Matos Velho ingressa na revenda de combustíveis.</span></li>
              <li><strong>1978</strong><span>Inauguração do Auto Posto Caucaia, em Caucaia do Alto (Cotia-SP): nasce a marca D+.</span></li>
              <li><strong>2005</strong><span>Entrada na distribuição de petróleo, com interligação à REPLAN.</span></li>
              <li><strong>2008</strong><span>Expansão em Guarulhos via REVAP e primeiro contrato de venda de gasolina e diesel.</span></li>
              <li><strong>2012</strong><span>Operação em São José dos Campos e reconhecimento da Petrobras.</span></li>
            </ol>
          </div>
          <div class="where">
            <h3>Onde operamos</h3>
            <p>A D'Mais atua no estado de São Paulo com unidades estrategicamente distribuídas para garantir agilidade e proximidade com o seu negócio.</p>
            <img src="/assets/img/mapa-sp.webp" width="740" height="560" alt="Mapa do estado de São Paulo com a matriz em Paulínia e as filiais em Guarulhos e São José dos Campos" loading="lazy">
            <ul>
              <li><span class="pin pin--matriz" aria-hidden="true"></span>Matriz: Base Atlanta, Paulínia</li>
              <li><span class="pin pin--filial" aria-hidden="true"></span>Filial: BAGUAR, Guarulhos</li>
              <li><span class="pin pin--filial" aria-hidden="true"></span>Filial: BAVAP, São José dos Campos</li>
            </ul>
            <a class="btn btn--outline" href="/fornecedores" style="margin-top:16px">Bases e fornecedores {ic('arrow')}</a>
          </div>
        </div>

        <article class="director" aria-labelledby="diretor-title">
          <div><div class="director__mark" aria-hidden="true">“</div><h3 id="diretor-title">O Diretor e a D'Mais</h3></div>
          <blockquote>
            <p>Se eu ficasse amargo com tudo que acontecesse de negativo, contaminaria a todos na empresa.</p>
            <p>Porque sou importante? Nada disso. Porque cada um de nós é parte integrante da empresa, e uma parte envenenada modifica um todo, por pouco que seja.</p>
            <p>Por essa razão, todos, vendedores, diretores, motoristas, operadores, clientes, meio ambiente etc., somos igualmente importantes.</p>
            <p>Enfrentamos problemas, fizemos conquistas, nos organizamos, encontramos desejo de destruição e vingança em uma pessoa, mas em outras vimos esforço de transformação, devoção, carinho e vontade de aprender.</p>
            <p class="director__big">“MAS PODE SER MELHOR”</p>
            <p>Acredito que, através da implementação de uma política de gestão integrada com diretrizes de Qualidade, Segurança, Meio Ambiente, Saúde e Responsabilidade Social, conseguiremos alcançar todos os objetivos desejados.</p>
            <p>A princípio pode parecer extremamente difícil, encontraremos muitos obstáculos, mas se dermos um passo real nessa direção, terá valido a pena acreditar.</p>
            <footer><strong>José Luis Fernandes Velho</strong>Diretor Presidente, D'Mais Distribuidora de Petróleo Ltda.</footer>
          </blockquote>
        </article>
      </div>
    </section>

    <!-- AVALIAÇÕES -->
    <section class="section section--light" id="avaliacoes" aria-labelledby="avaliacoes-title">
      <div class="container">
        <div class="section-head section-head--center">
          <p class="eyebrow">Avaliações no Google</p>
          <h2 class="h2" id="avaliacoes-title">Os nossos clientes no centro de tudo</h2>
          <p class="lead">Avaliações reais de clientes que confiam diariamente na D'Mais Distribuidora.</p>
        </div>
        <div class="reviews">
{reviews}
        </div>
        <div class="reviews-cta">
          <a class="btn btn--blue btn--lg" href="{REVIEW_URL}" target="_blank" rel="noopener">{ic('star')}Deixe sua avaliação</a>
        </div>
      </div>
    </section>
  </main>
"""
    return {
        "path": "/", "file": "index.html", "active": None,
        "title": "D'Mais Distribuidora de Petróleo | Combustíveis para Postos Bandeira Branca em SP",
        "description": "Distribuidora de combustíveis para postos bandeira branca em SP: gasolina, etanol, diesel S10 e S500 com bombeio Petrobras e logística própria.",
        "preload": '  <link rel="preload" as="image" href="/assets/img/hero.webp" imagesrcset="/assets/img/hero-960.webp 960w, /assets/img/hero.webp 1672w" imagesizes="100vw">\n',
        "schema": [ORG, DIRECTOR, WEBSITE],
        "body": body,
    }


def rede():
    cards = []
    for i, (name, street, city, phone, tel) in enumerate(STATIONS):
        img = "posto-1" if i % 2 == 0 else "posto-2"
        w, h = (1200, 675) if img == "posto-1" else (1200, 900)
        maps = "https://www.google.com/maps/search/?api=1&query=" + (f"{name} {street} {city}").replace(" ", "+")
        cards.append(f"""        <article class="station">
          <div class="station__media"><img src="/assets/img/{img}.webp" width="{w}" height="{h}" alt="Posto de combustíveis da Rede D+ com cobertura amarela e azul" loading="lazy"></div>
          <div class="station__body">
            <h2>{name}</h2>
            <p>{ic('pin')}<span>{street}<br>{city}</span></p>
            <p>{ic('phone')}<a class="tel" href="tel:{tel}">{phone}</a><span class="sr-only"> (WhatsApp/Telefone)</span></p>
            <div class="station__actions">
              <a class="btn btn--blue" href="{maps}" target="_blank" rel="noopener">{ic('pin')}Como chegar</a>
              <a class="btn btn--outline" href="tel:{tel}">{ic('phone')}Ligar</a>
            </div>
          </div>
        </article>""")
    body = page_hero("Rede de Postos D+", "Rede de Postos <span>D+</span>",
                     "Venha conhecer a nossa Rede de Postos D+, que hoje conta com seis postos de combustíveis consolidados no mercado há mais de 45 anos. Nossa longa trajetória reflete o nosso compromisso inabalável com qualidade, confiança e excelência.",
                     "Rede de Postos") + f"""
    <section class="section section--soft" aria-label="Lista de postos">
      <div class="container">
        <div class="stations">
{chr(10).join(cards)}
        </div>
        <p style="margin-top:28px;text-align:center">Para saber mais, acesse <a href="https://www.postosdmais.com" target="_blank" rel="noopener"><strong>www.postosdmais.com</strong></a>.</p>
      </div>
    </section>
  </main>
"""
    items = [{"@type": "ListItem", "position": i + 1, "item": {"@type": "GasStation", "name": n, "telephone": t, "brand": {"@type": "Brand", "name": "D+"},
              "address": {"@type": "PostalAddress", "streetAddress": s, "addressLocality": c.split(' - ')[0], "addressRegion": "SP", "addressCountry": "BR"}}}
             for i, (n, s, c, p, t) in enumerate(STATIONS)]
    return {
        "path": "/rede-de-postos", "file": "rede-de-postos.html", "active": "rede",
        "title": "Rede de Postos D+ | Postos de Combustíveis em Cotia, Vargem Grande Paulista e São Paulo",
        "description": "Conheça os 6 postos da Rede D+ em Cotia, Caucaia do Alto, Granja Viana, Vargem Grande Paulista e São Paulo: endereços, telefones e como chegar.",
        "schema": [{"@type": "ItemList", "name": "Rede de Postos D+", "itemListElement": items}, crumbs("Rede de Postos", "/rede-de-postos")],
        "body": body,
    }


def fornecedores():
    cards = "\n".join(f"""        <article class="base{' base--matriz' if m else ''}">
          <span class="base__tag">{tag}</span>
          <h2>{name} · {city}</h2>
          <dl>{''.join(f'<div><dt>{p}</dt><dd>{s}</dd></div>' for p, s in rows)}</dl>
        </article>""" for tag, name, city, m, rows in BASES)
    body = page_hero("Fornecedores", "Principais <span>fornecedores</span> da D'Mais",
                     "Combustíveis com garantia de origem: gasolina e diesel das refinarias Petrobras REPLAN e REVAP, biodiesel Cargill e etanol Copersucar e Usina Santa Isabel, distribuídos a partir das nossas três bases em São Paulo.",
                     "Fornecedores") + f"""
    <section class="section section--soft" aria-label="Fornecedores por base">
      <div class="container">
        <div class="bases">
{cards}
        </div>
      </div>
    </section>
  </main>
"""
    return {
        "path": "/fornecedores", "file": "fornecedores.html", "active": "fornecedores",
        "title": "Fornecedores | REPLAN, REVAP, Cargill e Copersucar | D'Mais Distribuidora",
        "description": "Origem dos combustíveis D'Mais: gasolina e diesel da REPLAN e REVAP (Petrobras), biodiesel Cargill e etanol Copersucar e Usina Santa Isabel.",
        "schema": [crumbs("Fornecedores", "/fornecedores")],
        "body": body,
    }


def transportadora():
    body = page_hero("Transportadora", "Transporte seguro com a <span>RECAR</span>",
                     "Logística sob a gestão de risco da D'Mais, para o combustível chegar ao seu posto com segurança e no prazo.",
                     "Transportadora") + f"""
    <section class="section section--soft" aria-label="RECAR Transportes">
      <div class="container">
        <div class="partner">
          <img src="/assets/img/logo-recar.webp" width="1300" height="500" alt="Logo da RECAR Transportes" loading="lazy">
          <div>
            <h2>RECAR Transportes</h2>
            <p>A RECAR é a transportadora que opera sob a nossa gestão de risco. O transporte é garantido pela D'Mais, com veículos rastreados e motoristas de total confiança.</p>
            <ul class="checklist">
              <li>{ic('check')}Transportadora sob a gestão de risco da D'Mais</li>
              <li>{ic('check')}Transporte garantido pela D'Mais</li>
              <li>{ic('check')}Veículos rastreados por GPS</li>
              <li>{ic('check')}Manutenção preventiva gerida pela D'Mais</li>
              <li>{ic('check')}Motoristas 100% de confiança</li>
            </ul>
            <p>Fez um pedido para entrega conosco e tem preferência de que seja pela RECAR? Fale conosco para verificar a viabilidade.</p>
            <div class="hero__ctas" style="margin-top:18px">
              <a class="btn btn--wa btn--lg" data-cfg-href="wa" href="{WA}" target="_blank" rel="noopener">{ic('wa')}Falar no WhatsApp</a>
              <a class="btn btn--outline btn--lg" data-cfg-href="tel" href="tel:+551940090659">{ic('phone')}(19) 4009-0659</a>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>
"""
    return {
        "path": "/transportadora", "file": "transportadora.html", "active": "transportadora",
        "title": "Transportadora RECAR | Transporte de Combustíveis Rastreado | D'Mais Distribuidora",
        "description": "Transporte de combustíveis com a RECAR Transportes, sob a gestão de risco da D'Mais: veículos rastreados por GPS, manutenção preventiva e motoristas de confiança.",
        "schema": [crumbs("Transportadora", "/transportadora")],
        "body": body,
    }


FAQ_GENERAL = [
    ("A D'Mais atende postos bandeira branca?", "Sim. A D'Mais é parceira estratégica de postos bandeira branca, com combustíveis de qualidade, segurança no abastecimento, logística própria e atendimento próximo para proprietários, gestores e compradores de postos independentes no estado de São Paulo."),
    ("Em quais regiões a D'Mais atua?", "Atuamos no estado de São Paulo, com matriz em Paulínia (Base Atlanta) e filiais em Guarulhos (BAGUAR) e São José dos Campos (BAVAP)."),
    ("Qual é a origem dos combustíveis?", "Gasolina e diesel S10 e S500 vêm das refinarias Petrobras REPLAN (Paulínia) e REVAP (Vale do Paraíba), com bombeio Petrobras. O biodiesel vem da Cargill e o etanol da Copersucar e da Usina Santa Isabel. Veja os detalhes por base na página de Fornecedores."),
    ("Qual é o percentual de etanol na gasolina comum?", "A mistura obrigatória de etanol anidro na gasolina C é definida pela legislação vigente. Desde 1º de agosto de 2026, o percentual é de 32% (Lei nº 14.993/2024, a Lei do Combustível do Futuro, e resolução do CNPE)."),
    ("Como faço para me tornar cliente D'Mais?", "Preencha o formulário \"Seja você também um cliente D'Mais\" na página inicial, ou fale conosco pelo WhatsApp (11) 99371-9036 ou pelo telefone (19) 4009-0659. Nossa equipe comercial entra em contato em seguida."),
    ("A D'Mais envia boletos por WhatsApp?", "Não. A D'Mais nunca envia boletos por WhatsApp. Todos os boletos são emitidos junto com as respectivas notas fiscais e enviados exclusivamente pelo nosso e-mail oficial (@dmais-distribuidora.com). Se receber algo suspeito, não pague e fale conosco."),
    ("Quais são os horários de atendimento?", "Funcionamos de segunda a sexta, das 6h às 18h, e aos sábados, das 6h às 11h. O suporte pelo WhatsApp (11) 99371-9036 funciona 24 horas."),
]


def faq():
    prod_items = "\n".join(f"""          <details id="{p['id']}">
            <summary>{p['name']}: o que é e quando usar?</summary>
            <div class="faq__a"><p>{p['long']}</p></div>
          </details>""" for p in PRODUCTS)
    gen_items = "\n".join(f"""          <details>
            <summary>{q}</summary>
            <div class="faq__a"><p>{a}</p></div>
          </details>""" for q, a in FAQ_GENERAL)
    body = page_hero("Perguntas Frequentes", "Perguntas <span>frequentes</span>",
                     "Tire suas dúvidas sobre os nossos combustíveis (gasolina comum e aditivada, etanol, diesel S10 e S500) e sobre como trabalhar com a D'Mais.",
                     "Perguntas Frequentes") + f"""
    <section class="section" aria-label="Perguntas e respostas">
      <div class="container">
        <div class="faq-group">
          <h2>Produtos</h2>
          <div class="faq">
{prod_items}
          </div>
        </div>
        <div class="faq-group">
          <h2>Sobre a D'Mais</h2>
          <div class="faq">
{gen_items}
          </div>
        </div>
        <div class="soon">
          <h2>Insights e blog</h2>
          <p>Em breve: conteúdos sobre o mercado de combustíveis, legislação e gestão de postos.</p>
        </div>
      </div>
    </section>
  </main>
"""
    qa = [{"@type": "Question", "name": f"{p['name']}: o que é e quando usar?", "acceptedAnswer": {"@type": "Answer", "text": p["long"]}} for p in PRODUCTS]
    qa += [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ_GENERAL]
    return {
        "path": "/perguntas-frequentes", "file": "perguntas-frequentes.html", "active": "faq",
        "title": "Perguntas Frequentes | Gasolina, Etanol, Diesel S10 e S500 | D'Mais Distribuidora",
        "description": "Diferenças entre gasolina comum e aditivada, etanol, diesel S10 e diesel S500, mistura de etanol na gasolina, origem dos combustíveis e como ser cliente D'Mais.",
        "schema": [{"@type": "FAQPage", "mainEntity": qa}, crumbs("Perguntas Frequentes", "/perguntas-frequentes")],
        "body": body,
    }


def trabalhe():
    body = page_hero("Trabalhe Conosco", "Trabalhe <span>conosco</span>",
                     "Quer fazer parte da D'Mais? Preencha o cadastro com as informações necessárias e envie o seu currículo.",
                     "Trabalhe Conosco") + f"""
    <section class="section section--deep" aria-labelledby="carreira-title">
      <div class="container job-grid">
        <div>
          <p class="eyebrow">Carreiras</p>
          <h2 class="h2" id="carreira-title">Cada pessoa é parte integrante da empresa</h2>
          <p class="lead">Vendedores, diretores, motoristas, operadores: todos somos igualmente importantes. Buscamos pessoas comprometidas com qualidade, segurança, meio ambiente, saúde e responsabilidade social.</p>
          <ul class="job-perks">
            <li>{ic('users')}<div><strong>Mais de 20 anos de mercado</strong><br>Uma empresa sólida no setor de distribuição de combustíveis.</div></li>
            <li>{ic('shield')}<div><strong>Gestão integrada</strong><br>Qualidade, segurança, meio ambiente e saúde no dia a dia.</div></li>
            <li>{ic('pin')}<div><strong>Unidades em SP</strong><br>Paulínia, Guarulhos e São José dos Campos.</div></li>
          </ul>
        </div>

        <form class="form-card" id="form-curriculo" data-form="curriculo" novalidate>
          <h2 class="form-card__title">Cadastre seu currículo</h2>
          <p class="form-card__sub">Campos com <span class="req">*</span> são obrigatórios.</p>
          <div class="hp" aria-hidden="true"><label>Não preencha<input class="hp-input" name="_gotcha" tabindex="-1" autocomplete="off"></label></div>
          <div class="grid-2">
{field('nome', 'Nome', auto='given-name')}
{field('sobrenome', 'Sobrenome', auto='family-name', required=False)}
{field('email', 'E-mail', 'email', 'email', full=True)}
{field('telefone', 'Telefone', 'tel', 'tel', ' inputmode="tel" data-mask="phone" placeholder="(11) 99999-9999"')}
{field('data_nascimento', 'Data de nascimento', 'date', 'bday', required=False)}
{field('cidade', 'Cidade de residência', auto='address-level2', required=False, full=True)}
{field('cargo', 'Cargo pretendido', full=True)}
          </div>
          <div class="field file-input" style="margin-top:14px">
            <label for="f-curriculo">Currículo (PDF ou Word, até 5 MB) <span class="req">*</span></label>
            <input id="f-curriculo" name="curriculo" type="file" accept=".pdf,.doc,.docx,application/pdf,application/msword,application/vnd.openxmlformats-officedocument.wordprocessingml.document" required aria-describedby="err-curriculo" data-err="err-curriculo">
            <p class="field-error" id="err-curriculo"></p>
          </div>
{consent('form-curriculo')}
          <div class="form-actions"><button class="btn btn--blue btn--lg btn--block" type="submit">Enviar currículo {ic('arrow')}</button></div>
          <p class="form-status" role="status" aria-live="polite"></p>
        </form>
      </div>
    </section>
  </main>
"""
    return {
        "path": "/trabalhe-conosco", "file": "trabalhe-conosco.html", "active": "trabalhe",
        "title": "Trabalhe Conosco | Vagas na D'Mais Distribuidora de Petróleo",
        "description": "Envie seu currículo para a D'Mais Distribuidora de Petróleo. Oportunidades em Paulínia, Guarulhos e São José dos Campos, no setor de distribuição de combustíveis.",
        "schema": [crumbs("Trabalhe Conosco", "/trabalhe-conosco")],
        "body": body,
    }


def privacidade():
    body = page_hero("LGPD", "Política de <span>privacidade</span>",
                     "Como a D'Mais Distribuidora de Petróleo Ltda. trata os dados pessoais enviados por este site, conforme a Lei Geral de Proteção de Dados (Lei nº 13.709/2018).",
                     "Política de Privacidade") + """
    <section class="section section--light">
      <div class="container legal">
        <h2>Quais dados coletamos</h2>
        <p>Coletamos apenas os dados que você informa nos formulários do site:</p>
        <ul>
          <li><strong>Seja cliente:</strong> razão social, CNPJ, inscrição estadual, endereço, e-mail, telefone, nome e cargo do responsável, vínculo com a empresa e como nos conheceu.</li>
          <li><strong>Trabalhe Conosco:</strong> nome, sobrenome, e-mail, telefone, data de nascimento, cidade, cargo pretendido e o currículo enviado.</li>
          <li><strong>Canal de Denúncias:</strong> o relato enviado e, somente se você escolher se identificar, nome, e-mail e telefone. Esses dados são usados apenas para apurar a denúncia e são acessados somente pela diretoria.</li>
        </ul>
        <h2>Para que usamos</h2>
        <ul>
          <li>Responder à sua solicitação.</li>
          <li>Avaliar o cadastro comercial e entrar em contato.</li>
          <li>Considerar a sua candidatura em processos seletivos.</li>
        </ul>
        <p>A base legal é o seu consentimento e, no caso de clientes, os procedimentos preliminares a um contrato.</p>
        <h2>Compartilhamento e armazenamento</h2>
        <p>Os dados são armazenados com segurança na plataforma Wix, nossa fornecedora de banco de dados. Não vendemos os seus dados e não os compartilhamos para fins de marketing. Os currículos são mantidos pelo tempo necessário ao processo seletivo ou até que você peça a exclusão.</p>
        <h2>Seus direitos</h2>
        <p>Você pode:</p>
        <ul>
          <li>confirmar se tratamos os seus dados e acessá-los;</li>
          <li>corrigir os seus dados;</li>
          <li>pedir a anonimização ou a exclusão dos seus dados;</li>
          <li>revogar o seu consentimento;</li>
          <li>pedir informações sobre o compartilhamento.</li>
        </ul>
        <p>Para isso, escreva para <a href="mailto:contato@dmais-distribuidora.com">contato@dmais-distribuidora.com</a>. Você também pode apresentar reclamação à Autoridade Nacional de Proteção de Dados (ANPD).</p>
        <h2>Contato</h2>
        <p>D'Mais Distribuidora de Petróleo Ltda.<br>Av. Senador Onofre Quinan, 763, Sala 02, Cascata, Paulínia - SP<br>(19) 4009-0659 · contato@dmais-distribuidora.com</p>
      </div>
    </section>
  </main>
"""
    return {
        "path": "/politica-de-privacidade", "file": "politica-de-privacidade.html", "active": None,
        "title": "Política de Privacidade (LGPD) | D'Mais Distribuidora de Petróleo",
        "description": "Saiba como a D'Mais Distribuidora de Petróleo trata os dados pessoais enviados pelos formulários do site, conforme a LGPD (Lei nº 13.709/2018).",
        "schema": [crumbs("Política de Privacidade", "/politica-de-privacidade")],
        "body": body,
    }


def denuncias():
    cats = "".join(f'<option value="{c}">{c}</option>' for c in [
        "Fraude, corrupção ou suborno", "Assédio moral ou sexual", "Discriminação",
        "Segurança, saúde ou meio ambiente", "Qualidade ou adulteração de combustível",
        "Conflito de interesses", "Uso indevido de bens ou informações", "Outro assunto"])
    ident = "".join(f'<label class="choice"><input type="radio" name="identificacao" value="{v}" required>{t}</label>' for v, t in [("Anônima", "Quero ficar anônimo"), ("Identificada", "Quero me identificar")])
    body = page_hero("Canal de Denúncias", "Canal de <span>denúncias</span>",
                     "Um canal seguro para relatar irregularidades, de forma anônima ou identificada. Cada denúncia é recebida diretamente pela diretoria da D'Mais.",
                     "Canal de Denúncias") + f"""
    <section class="section section--deep" aria-labelledby="den-title">
      <div class="container job-grid">
        <div>
          <p class="eyebrow">Ética e transparência</p>
          <h2 class="h2" id="den-title">Sua denúncia faz diferença</h2>
          <p class="lead">Use este canal para relatar condutas contrárias à lei, à ética ou às políticas da D'Mais, envolvendo colaboradores, clientes, fornecedores ou parceiros.</p>
          <ul class="job-perks">
            <li>{ic('shield')}<div><strong>Anonimato garantido</strong><br>Se escolher ficar anônimo, não pedimos nome, e-mail nem telefone.</div></li>
            <li>{ic('users')}<div><strong>Direto para a diretoria</strong><br>O relato é enviado somente para a diretoria e tratado com sigilo.</div></li>
            <li>{ic('check')}<div><strong>Sem retaliação</strong><br>A D'Mais não tolera retaliação contra quem denuncia de boa-fé.</div></li>
          </ul>
        </div>

        <form class="form-card" id="form-denuncia" data-form="denuncia" novalidate>
          <h2 class="form-card__title">Fazer uma denúncia</h2>
          <p class="form-card__sub">Campos com <span class="req">*</span> são obrigatórios. Descreva os fatos com o máximo de detalhes possível.</p>
          <div class="hp" aria-hidden="true"><label>Não preencha<input class="hp-input" name="_gotcha" tabindex="-1" autocomplete="off"></label></div>
          <fieldset class="fieldset" style="margin-top:0" data-group-required="err-identificacao">
            <legend>Como deseja enviar? <span class="req">*</span></legend>
            <div class="choices choices--2">{ident}</div>
            <p class="field-error" id="err-identificacao" role="alert"></p>
          </fieldset>
          <div class="conditional grid-2" data-show-when="identificacao=Identificada" hidden>
{field('den_nome', 'Nome', auto='name', full=True)}
{field('den_email', 'E-mail', 'email', 'email')}
{field('den_telefone', 'Telefone', 'tel', 'tel', ' inputmode="tel" data-mask="phone" placeholder="(11) 99999-9999" data-optional', required=False)}
          </div>
          <div class="grid-2" style="margin-top:14px">
            <div class="field" style="grid-column:1/-1"><label for="f-categoria">Assunto <span class="req" aria-hidden="true">*</span></label><select class="input" id="f-categoria" name="categoria" required aria-describedby="err-categoria"><option value="">Selecione o assunto</option>{cats}</select><p class="field-error" id="err-categoria"></p></div>
{field('envolvidos', 'Pessoas ou áreas envolvidas', required=False, full=True)}
{field('quando_onde', 'Quando e onde aconteceu', required=False, full=True, extra=' placeholder="Ex.: março de 2026, base de Paulínia"')}
            <div class="field" style="grid-column:1/-1"><label for="f-descricao">Descrição dos fatos <span class="req" aria-hidden="true">*</span></label><textarea class="input" id="f-descricao" name="descricao" rows="6" required aria-describedby="err-descricao" placeholder="O que aconteceu, quem estava envolvido e se há provas ou testemunhas."></textarea><p class="field-error" id="err-descricao"></p></div>
          </div>
          <p class="form-note">Os dados informados são usados apenas para apurar a denúncia, conforme a nossa <a href="/politica-de-privacidade">Política de Privacidade</a>.</p>
          <div class="form-actions"><button class="btn btn--blue btn--lg btn--block" type="submit">Enviar denúncia {ic('arrow')}</button></div>
          <p class="form-status" role="status" aria-live="polite"></p>
        </form>
      </div>
    </section>
  </main>
"""
    return {
        "path": "/canal-de-denuncias", "file": "canal-de-denuncias.html", "active": None,
        "title": "Canal de Denúncias | D'Mais Distribuidora de Petróleo",
        "description": "Canal de denúncias da D'Mais Distribuidora: relate irregularidades de forma anônima ou identificada, com sigilo e envio direto à diretoria.",
        "schema": [crumbs("Canal de Denúncias", "/canal-de-denuncias")],
        "body": body,
    }


def notfound():
    body = page_hero("Erro 404", "Página <span>não encontrada</span>", "O endereço que você procurou não existe ou mudou de lugar.", "Página não encontrada") + """
    <section class="section"><div class="container"><a class="btn btn--yellow btn--lg" href="/">Voltar para a página inicial</a></div></section>
  </main>
"""
    return {"path": "/404", "file": "404.html", "active": None, "noindex": True,
            "title": "Página não encontrada | D'Mais Distribuidora", "description": "A página que você procurou não foi encontrada no site da D'Mais Distribuidora de Petróleo.",
            "schema": [WEBSITE], "body": body}


PAGES = [home(), rede(), fornecedores(), transportadora(), faq(), trabalhe(), denuncias(), privacidade(), notfound()]


def main():
    for p in PAGES:
        html = head(p)
        if p.get("noindex"):
            html = html.replace('<meta name="theme-color"', '<meta name="robots" content="noindex">\n  <meta name="theme-color"')
        html += header(p["active"]) + p["body"] + footer()
        assert html.count("<h1") == 1, f"{p['file']}: deve ter exatamente um H1"
        (ROOT / p["file"]).write_text(html, encoding="utf-8")
    urls = "\n".join(f"""  <url>
    <loc>{DOMAIN}{p['path']}</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>{'weekly' if p['path'] == '/' else 'monthly'}</changefreq>
    <priority>{'1.0' if p['path'] == '/' else '0.7'}</priority>
  </url>""" for p in PAGES if not p.get("noindex"))
    (ROOT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n', encoding="utf-8")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n", encoding="utf-8")
    print("Páginas geradas:", ", ".join(p["file"] for p in PAGES))


if __name__ == "__main__":
    main()
