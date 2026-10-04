import "./style.css";
import "./glass.css";
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import Lenis from "lenis";

gsap.registerPlugin(ScrollTrigger);

/* ==========================================================
   SITE SETTINGS: contact details used across the page.
   ========================================================== */
const SITE = {
  phone: "084 927 0101",
  phoneLink: "+27849270101",
  whatsapp: "27849270101",
  whatsappText: "Hi Lawgical Labour, I'd like to enquire about a labour matter.",
  whatsappCcmaText: "Hi Lawgical Labour, I've received a CCMA referral and need assistance.",
  email: "louise@lawgical.co.za",
  area: "All of South Africa",
  // Formspree: create a form that delivers to louise@lawgical.co.za, then paste its endpoint here (e.g. "https://formspree.io/f/abcdwxyz").
  // While empty, the form opens the visitor's email app addressed to `email`.
  formEndpoint: "",
  // Set at build time for the hosted preview: shows the thank-you message without sending.
  preview: import.meta.env.VITE_PREVIEW === "1",
};

const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => [...r.querySelectorAll(s)];

const reduceMotion = matchMedia("(prefers-reduced-motion: reduce)").matches;
// Scrubbed video + pins only on larger, pointer devices (skill: mobile fallback).
const fullMotion = !reduceMotion && matchMedia("(hover: hover) and (min-width: 769px)").matches;

/* ---------- Contact details ---------- */
const wa = (text) => `https://wa.me/${SITE.whatsapp}?text=${encodeURIComponent(text)}`;
$$("[data-cfg='phone']").forEach((el) => (el.textContent = SITE.phone));
$$("[data-cfg='email']").forEach((el) => (el.textContent = SITE.email));
$$("[data-cfg='area']").forEach((el) => (el.textContent = SITE.area));
$$("[data-cfg-href='tel']").forEach((a) => (a.href = `tel:${SITE.phoneLink}`));
$$("[data-cfg-href='mailto']").forEach((a) => (a.href = `mailto:${SITE.email}`));
$$("[data-cfg-href='wa']").forEach((a) => (a.href = wa(SITE.whatsappText)));
$$("[data-cfg-href='wa-ccma']").forEach((a) => (a.href = wa(SITE.whatsappCcmaText)));
$$("[data-year]").forEach((el) => (el.textContent = new Date().getFullYear()));

/* ---------- Lenis smooth scroll, driven by GSAP's ticker ---------- */
const lenis = new Lenis({ duration: 1.15, smoothWheel: !reduceMotion });
lenis.on("scroll", ScrollTrigger.update);
gsap.ticker.add((time) => lenis.raf(time * 1000));
gsap.ticker.lagSmoothing(0);

/* ---------- Nav ---------- */
const nav = $(".nav");
const toggle = $(".nav__toggle");
const setMenu = (open) => {
  document.body.classList.toggle("nav-open", open);
  toggle.setAttribute("aria-expanded", String(open));
  toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
};
toggle.addEventListener("click", () => setMenu(!document.body.classList.contains("nav-open")));
document.addEventListener("keydown", (e) => {
  if (e.key === "Escape" && document.body.classList.contains("nav-open")) { setMenu(false); toggle.focus(); }
});

// In-page links: smooth scroll with Lenis, offset for the fixed nav.
$$('a[href^="#"]').forEach((a) =>
  a.addEventListener("click", (e) => {
    const id = a.getAttribute("href");
    const target = id.length > 1 && $(id);
    if (!target) return;
    e.preventDefault();
    setMenu(false);
    lenis.scrollTo(target, { offset: id === "#home" ? 0 : -70, duration: reduceMotion ? 0 : 1.4 });
    try { history.replaceState(null, "", id); } catch (_) {}
    if (id === "#book") setTimeout(() => $("#f-name").focus({ preventScroll: true }), reduceMotion ? 0 : 1400);
  })
);

// Active nav link
const navLinks = $$(".nav__links a[href^='#']:not(.btn)");
navLinks.forEach((a) => {
  const sec = $(a.getAttribute("href"));
  if (!sec) return;
  ScrollTrigger.create({
    trigger: sec, start: "top 55%", end: "bottom 45%",
    onToggle: (self) => self.isActive && navLinks.forEach((l) => l.classList.toggle("is-current", l === a)),
  });
});

/* ---------- Scroll progress bar + nav background ---------- */
const bar = $(".scroll-progress span");
lenis.on("scroll", ({ scroll, limit }) => {
  bar.style.transform = `scaleX(${limit ? scroll / limit : 0})`;
  nav.classList.toggle("is-scrolled", scroll > 40);
});

/* ---------- Impact: pinned word-by-word reveal ---------- */
let impactST = null;
function setupImpact() {
  const head = $("[data-words]");
  const keys = new Set(["employers.", "Only", "protect"]);
  head.innerHTML = head.textContent
    .trim()
    .split(/\s+/)
    .map((w) => `<span class="word${keys.has(w) ? " is-key" : ""}">${w}</span>`)
    .join(" ");
  if (!fullMotion) return;

  const words = $$(".word", head);
  const render = (p) =>
    words.forEach((word, i) => {
      const start = (i / words.length) * 0.72;
      const o = gsap.utils.clamp(0, 1, (p - start) / 0.12);
      word.style.opacity = 0.12 + o * 0.88;
      word.style.filter = `blur(${(1 - o) * 8}px)`;
      word.style.transform = `translateY(${(1 - o) * 18}px)`;
    });
  render(0);
  impactST = ScrollTrigger.create({
    trigger: "#impact",
    start: "top top",
    end: () => "+=" + innerHeight * 1.6,
    pin: ".impact__pin",
    scrub: 1,
    invalidateOnRefresh: true,
    onUpdate: (self) => render(self.progress),
  });
}

/* ---------- Background video: scrubbed by scroll ---------- */
const bgVideo = $("#bgv");
let lastVideoT = -1;
function scrubVideo() {
  if (!bgVideo.duration) return;
  // Slow the video while pinned sections play, so the three video phases
  // line up with the page story (recipe 8 in the skill).
  const k = 0.18;
  let eff = lenis.scroll;
  let removed = 0;
  for (const st of [impactST]) {
    if (!st) continue;
    const len = st.end - st.start;
    if (lenis.scroll >= st.end) { eff -= len * (1 - k); removed += len * (1 - k); }
    else if (lenis.scroll > st.start) { eff -= (lenis.scroll - st.start) * (1 - k); removed += len * (1 - k); }
    else removed += len * (1 - k);
  }
  const p = gsap.utils.clamp(0, 1, eff / Math.max(1, lenis.limit - removed));
  const t = p * (bgVideo.duration - 0.05);
  if (Math.abs(t - lastVideoT) > 0.008) {
    bgVideo.currentTime = t;
    lastVideoT = t;
  }
}
function setupVideo() {
  if (!fullMotion) { bgVideo.removeAttribute("src"); bgVideo.load(); return; }
  bgVideo.pause();
  const ready = () => { bgVideo.pause(); scrubVideo(); };
  bgVideo.addEventListener("loadedmetadata", ready, { once: true });
  if (bgVideo.readyState >= 1) ready();
  lenis.on("scroll", scrubVideo);
}

/* ---------- Reveals and parallax ---------- */
function setupReveals() {
  if (reduceMotion) return;
  $$(".reveal").forEach((el) => {
    if (el.closest(".hero")) return; // hero has its own entrance below
    gsap.from(el, {
      y: 40, opacity: 0, duration: 1.1, ease: "power3.out",
      scrollTrigger: { trigger: el, start: "top 88%", once: true },
    });
  });
  // Hero entrance
  gsap.from(".hero .reveal", { y: 30, opacity: 0, duration: 1.2, ease: "power3.out", stagger: 0.12, delay: 0.15 });
  // Gentle parallax on the detail lines
  if (fullMotion) {
    $$("[data-parallax]").forEach((el) => {
      gsap.fromTo(el, { xPercent: Number(el.dataset.parallax) / 4 }, {
        xPercent: -Number(el.dataset.parallax) / 4, ease: "none",
        scrollTrigger: { trigger: ".showcase", start: "top bottom", end: "bottom top", scrub: 1 },
      });
    });
  }
}

/* ---------- Consultation form ---------- */
function setupForm() {
  const form = $("#book-form");
  const status = $(".form-status", form);
  const fields = {
    name: [$("#f-name"), $("#e-name"), (v) => v.trim().length >= 2 || "Please enter your name."],
    company: [$("#f-company"), $("#e-company"), (v) => v.trim().length >= 2 || "Please enter your company name."],
    phone: [$("#f-phone"), $("#e-phone"), (v) => v.replace(/\D/g, "").length >= 9 || "Please enter a phone number we can reach you on, e.g. 082 123 4567."],
    matter: [$("#f-matter"), $("#e-matter"), (v) => !!v || "Please choose what you need help with."],
  };
  const check = (key) => {
    const [input, err, rule] = fields[key];
    const res = rule(input.value);
    const msg = res === true ? "" : res;
    err.textContent = msg;
    input.setAttribute("aria-invalid", msg ? "true" : "false");
    return !msg;
  };
  Object.keys(fields).forEach((k) => {
    const [input] = fields[k];
    input.addEventListener("blur", () => input.value && check(k));
    input.addEventListener("input", () => input.getAttribute("aria-invalid") === "true" && check(k));
  });

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const bad = Object.keys(fields).filter((k) => !check(k));
    if (bad.length) { fields[bad[0]][0].focus(); return; }
    const data = Object.fromEntries(new FormData(form).entries());
    const btn = $("[data-submit]", form);
    btn.classList.add("is-loading");
    status.textContent = "";
    try {
      if (SITE.preview) {
        await new Promise((r) => setTimeout(r, 500));
      } else if (SITE.formEndpoint) {
        const res = await fetch(SITE.formEndpoint, {
          method: "POST",
          headers: { "Content-Type": "application/json", Accept: "application/json" },
          body: JSON.stringify({ ...data, _subject: `Consultation request: ${data.matter} (${data.company})` }),
        });
        if (!res.ok) throw new Error(res.status);
      } else {
        const body = Object.entries(data).map(([k, v]) => `${k}: ${v}`).join("\n");
        location.href = `mailto:${SITE.email}?subject=${encodeURIComponent(`Consultation request: ${data.matter}`)}&body=${encodeURIComponent(body)}`;
      }
      form.reset();
      status.textContent = `Thank you, ${data.name.split(" ")[0]}. We will contact you shortly.`;
    } catch {
      status.textContent = `Sorry, your request didn't send. Please call or WhatsApp ${SITE.phone}.`;
    } finally {
      btn.classList.remove("is-loading");
    }
  });
}

/* ---------- Init ---------- */
setupImpact();
setupVideo();
setupReveals();
setupForm();
addEventListener("load", () => ScrollTrigger.refresh());
document.fonts?.ready.then(() => ScrollTrigger.refresh());

if (import.meta.env.DEV) {
  window.__lenis = lenis;
  window.__ST = ScrollTrigger;
  window.__bgv = bgVideo;
}
