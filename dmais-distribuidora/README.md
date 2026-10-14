# D'Mais Distribuidora: site

Site estático e rápido (HTML, CSS e um pouco de JavaScript), em português (pt-BR).

- **Domínio:** https://www.dmais-distribuidora.com
- **Formulários:** gravam no banco de dados do Wix pelo Velo.

## Estrutura

| Caminho | O que é |
|---|---|
| `build.py` | Gera todas as páginas: cabeçalho, rodapé, SEO, schema, `sitemap.xml` e `robots.txt`. Textos, postos, bases, avaliações e perguntas ficam aqui. |
| `site/` | Pasta que vai para o ar. Publique **o conteúdo desta pasta**. |
| `site/assets/css/styles.css` | Design. As cores da marca são variáveis no topo do arquivo. |
| `site/assets/js/main.js` | Configurações (`SITE`), menu, máscaras, validação e envio dos formulários |
| `site/_headers` | HSTS, cabeçalhos de segurança e cache (Cloudflare Pages) |
| `wix-velo/backend/http-functions.js` | Código do backend Wix que grava os formulários |
| `assets/references/` | Imagens originais enviadas pelo cliente. Não vão para o ar. |

### Páginas

| Página | Endereço |
|---|---|
| Início | `/` |
| Rede de Postos | `/rede-de-postos` |
| Fornecedores | `/fornecedores` |
| Transportadora | `/transportadora` |
| Perguntas Frequentes | `/perguntas-frequentes` |
| Trabalhe Conosco | `/trabalhe-conosco` |
| Política de Privacidade (LGPD) | `/politica-de-privacidade` |
| Página de erro | `404.html` (fora do sitemap) |

## Editar o conteúdo

1. Altere os textos ou dados em `build.py`.
2. Rode `python3 build.py`. As páginas em `site/` são recriadas, e a data do `sitemap.xml` é atualizada.
3. O script confere se cada página tem exatamente um `<h1>`.

Os contatos (telefone, WhatsApp e e-mail) dos botões ficam em `SITE`, no topo de `site/assets/js/main.js`.

## Publicar (Cloudflare Pages)

1. **Criar o projeto:** Cloudflare > Workers & Pages > Criar > Pages > Enviar arquivos (ou conectar o GitHub). A pasta de saída é `site`, sem comando de build.
2. **Domínio personalizado:** adicione `www.dmais-distribuidora.com` e `dmais-distribuidora.com`.
3. **Canonicalização (sempre `https://www.`):**
   - **SSL/TLS > Edge Certificates:** ative **Always Use HTTPS**. Isso faz `http` → `https`.
   - **Rules > Redirect Rules:** crie a regra "Redirect from root to WWW" para `dmais-distribuidora.com/*`, que redireciona para `https://www.dmais-distribuidora.com/${1}` com código 301.
   - Os endereços sem `.html` são o padrão do Cloudflare Pages. A tag `canonical` de cada página já aponta para a versão `https://www.` sem `.html`.
4. **HSTS:**
   - O arquivo `_headers` já envia `Strict-Transport-Security: max-age=31536000; includeSubDomains`.
   - Se preferir, ative também em SSL/TLS > Edge Certificates > HTTP Strict Transport Security (HSTS).
   - Só ative depois de confirmar que o HTTPS funciona em todos os subdomínios.
5. **Depois de publicar:**
   - Cadastre o site no Google Search Console.
   - Envie `https://www.dmais-distribuidora.com/sitemap.xml`.

## Formulários no banco de dados do Wix (Velo)

### 1. Criar as coleções
No Editor Wix, ative o **Dev Mode** e vá em Databases > Create Collection.

**`ClientesDmais`** (formulário "Seja Cliente"):
- Campos de texto: `razaoSocial`, `cnpj`, `inscricaoEstadual`, `endereco`, `email`, `telefone`, `responsavel`, `cargo`, `vinculo`, `vinculoOutro`, `comoConheceu`, `nomeVendedor`, `comoConheceuDetalhe`, `pagina`.
- Campo booleano: `consentimentoLgpd`.

**`CurriculosDmais`** (formulário "Trabalhe Conosco"):
- Campos de texto: `nome`, `sobrenome`, `email`, `telefone`, `dataNascimento`, `cidade`, `cargo`, `curriculoNome`, `pagina`.
- Campo URL: `curriculoUrl`.
- Campo booleano: `consentimentoLgpd`.

Permissões das duas coleções:
- **Leitura:** apenas administradores. Os dados são pessoais (LGPD).
- **Gravação:** o backend grava com `suppressAuth`, então o público não precisa de permissão.

### 2. Colar o backend
1. Em **Backend**, crie o arquivo `http-functions.js`.
2. Cole o conteúdo de `wix-velo/backend/http-functions.js`.
3. Publique o site Wix.

### 3. Ligar o site
Em `site/assets/js/main.js`, preencha `wixFunctionsUrl` com o endereço das funções, **sem barra no final**. Exemplos:
- Site Wix gratuito: `https://CONTA.wixsite.com/SITE/_functions`
- Domínio próprio no Wix: `https://DOMINIO/_functions`

Enquanto `wixFunctionsUrl` estiver vazio, os formulários abrem o e-mail do visitante com os dados preenchidos, como alternativa.

### 4. Testar (importante)
1. Envie um cadastro "Seja Cliente" de teste e confira se ele aparece em `ClientesDmais`.
2. Envie um currículo em PDF de teste pelo "Trabalhe Conosco". O arquivo deve aparecer em Media Manager > `curriculos`, e o registro deve aparecer em `CurriculosDmais` com o link do arquivo.
3. O envio do currículo usa o link de upload do Wix (`mediaManager.getUploadUrl`). Se o registro chegar com `curriculoUrl` vazio, verifique a resposta do upload no console do navegador. O formato da resposta do Wix pode variar, e a leitura do link fica em `uploadCV`, no `main.js`.

## SEO

Cada página tem:
- título e meta description próprios, palavras-chave e `canonical`;
- Open Graph com endereços absolutos e `twitter:card`;
- um único `<h1>`;
- `alt` em todas as imagens.

Schema (JSON-LD):
- **Início:** Organization/LocalBusiness e WebSite.
- **Rede de Postos:** lista dos postos (GasStation).
- **Perguntas Frequentes:** FAQPage.
- **Páginas internas:** BreadcrumbList.

Desempenho:
- Fonte Inter hospedada no próprio site (sem Google Fonts).
- CSS único e JavaScript com `defer`.
- Imagens WebP com `width`/`height`.
- Sem scripts de terceiros nem mapas embutidos. Os botões "Ver no mapa" abrem o Google Maps.

Itens do relatório de SEO:
- `sitemap.xml`, favicon, canonicalização, meta descriptions e `<h1>` único;
- recursos que bloqueiam a renderização;
- `alt` nas imagens;
- tempo de execução de JavaScript.

## Conteúdo a confirmar
- **Mistura de etanol na gasolina:** o site informa **32%**, em vigor desde 1º/08/2026 (resolução do CNPE, com base na Lei 14.993/2024 "Combustível do Futuro"). Atualize em `build.py` se o percentual mudar.
- **Nome de uma avaliação:** "Posto Nova São Joa" parece cortado no print. Confirme o nome completo.
- **Blog / Insights:** há um espaço reservado na página de Perguntas Frequentes. Quando houver artigos, cada um vira uma página nova (com `BlogPosting`) e entra no `sitemap.xml`.
