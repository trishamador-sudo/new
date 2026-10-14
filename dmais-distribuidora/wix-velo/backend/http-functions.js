/* ==========================================================
   D'Mais Distribuidora: HTTP Functions (Wix Velo)
   Cole este arquivo em: Wix Editor > Dev Mode > Backend > http-functions.js
   Endpoints (https://SEU-SITE-WIX/_functions/...):
     POST /clientes   -> grava na coleção "ClientesDmais"
     POST /curriculos -> grava na coleção "CurriculosDmais"
     POST /uploadUrl  -> devolve um link para enviar o currículo à Mídia do Wix
   ========================================================== */
import { ok, badRequest, serverError, response } from 'wix-http-functions';
import wixData from 'wix-data';
import { mediaManager } from 'wix-media-backend';

const ALLOWED_ORIGINS = [
  'https://www.dmais-distribuidora.com',
  'https://dmais-distribuidora.com',
];

const cors = request => {
  const origin = request.headers.origin || request.headers.Origin || '';
  return {
    'Access-Control-Allow-Origin': ALLOWED_ORIGINS.includes(origin) ? origin : ALLOWED_ORIGINS[0],
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type, Accept',
    'Access-Control-Max-Age': '86400',
    'Content-Type': 'application/json',
    Vary: 'Origin',
  };
};

const preflight = request => response({ status: 204, headers: cors(request) });
export const options_clientes = preflight;
export const options_curriculos = preflight;
export const options_uploadUrl = preflight;

const str = (v, max = 500) => (typeof v === 'string' ? v.trim().slice(0, max) : '');
const list = v => (Array.isArray(v) ? v : v ? [v] : []).map(x => str(x, 100)).filter(Boolean);
const isEmail = v => /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v);
const isCNPJ = v => {
  const c = v.replace(/\D/g, '');
  if (c.length !== 14 || /^(\d)\1+$/.test(c)) return false;
  const calc = len => {
    let sum = 0, pos = len - 7;
    for (let i = len; i >= 1; i--) { sum += +c[len - i] * pos--; if (pos < 2) pos = 9; }
    const r = sum % 11;
    return r < 2 ? 0 : 11 - r;
  };
  return calc(12) === +c[12] && calc(13) === +c[13];
};

const readJSON = async request => {
  try { return await request.body.json(); } catch (e) { return null; }
};
const fail = (request, msg) => badRequest({ headers: cors(request), body: { ok: false, error: msg } });

export async function post_clientes(request) {
  const b = await readJSON(request);
  if (!b) return fail(request, 'JSON inválido');
  const item = {
    razaoSocial: str(b.razao_social, 200),
    cnpj: str(b.cnpj, 20),
    inscricaoEstadual: str(b.inscricao_estadual, 30),
    endereco: str(b.endereco, 300),
    email: str(b.email, 200),
    telefone: str(b.telefone, 30),
    responsavel: str(b.responsavel, 200),
    cargo: str(b.cargo, 120),
    vinculo: str(b.vinculo, 60),
    vinculoOutro: str(b.vinculo_outro, 200),
    comoConheceu: list(b.como_conheceu).join(', '),
    nomeVendedor: str(b.nome_vendedor, 200),
    comoConheceuDetalhe: str(b.como_conheceu_detalhe, 300),
    consentimentoLgpd: b.consentimento_lgpd === true,
    pagina: str(b.pagina, 200),
  };
  const required = ['razaoSocial', 'cnpj', 'inscricaoEstadual', 'endereco', 'email', 'telefone', 'responsavel', 'cargo', 'vinculo', 'comoConheceu'];
  const missing = required.filter(k => !item[k]);
  if (missing.length) return fail(request, `Campos obrigatórios: ${missing.join(', ')}`);
  if (!isCNPJ(item.cnpj)) return fail(request, 'CNPJ inválido');
  if (!isEmail(item.email)) return fail(request, 'E-mail inválido');
  if (!item.consentimentoLgpd) return fail(request, 'Consentimento LGPD obrigatório');
  try {
    await wixData.insert('ClientesDmais', item, { suppressAuth: true });
    return ok({ headers: cors(request), body: { ok: true } });
  } catch (e) {
    console.error('clientes', e);
    return serverError({ headers: cors(request), body: { ok: false } });
  }
}

export async function post_curriculos(request) {
  const b = await readJSON(request);
  if (!b) return fail(request, 'JSON inválido');
  const item = {
    nome: str(b.nome, 120),
    sobrenome: str(b.sobrenome, 120),
    email: str(b.email, 200),
    telefone: str(b.telefone, 30),
    dataNascimento: str(b.data_nascimento, 10),
    cidade: str(b.cidade, 120),
    cargo: str(b.cargo, 120),
    curriculoUrl: str(b.curriculoUrl, 1000),
    curriculoNome: str(b.curriculoNome, 200),
    consentimentoLgpd: b.consentimento_lgpd === true,
    pagina: str(b.pagina, 200),
  };
  const missing = ['nome', 'email', 'telefone', 'cargo', 'curriculoUrl'].filter(k => !item[k]);
  if (missing.length) return fail(request, `Campos obrigatórios: ${missing.join(', ')}`);
  if (!isEmail(item.email)) return fail(request, 'E-mail inválido');
  if (!item.consentimentoLgpd) return fail(request, 'Consentimento LGPD obrigatório');
  try {
    await wixData.insert('CurriculosDmais', item, { suppressAuth: true });
    return ok({ headers: cors(request), body: { ok: true } });
  } catch (e) {
    console.error('curriculos', e);
    return serverError({ headers: cors(request), body: { ok: false } });
  }
}

const CV_TYPES = {
  pdf: 'application/pdf',
  doc: 'application/msword',
  docx: 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
};

export async function post_uploadUrl(request) {
  const b = await readJSON(request);
  const name = str(b && b.fileName, 150).replace(/[^\w.\- ]+/g, '_');
  const ext = (name.split('.').pop() || '').toLowerCase();
  if (!CV_TYPES[ext]) return fail(request, 'Envie PDF ou Word (.doc, .docx)');
  try {
    const { uploadUrl, uploadToken } = await mediaManager.getUploadUrl('/curriculos', {
      mediaOptions: { mimeType: CV_TYPES[ext], mediaType: 'document' },
      metadataOptions: { isPrivate: false, isVisitorUpload: true, context: { origem: 'trabalhe-conosco' } },
    });
    return ok({ headers: cors(request), body: { uploadUrl, uploadToken } });
  } catch (e) {
    console.error('uploadUrl', e);
    return serverError({ headers: cors(request), body: { ok: false } });
  }
}
