import "./style.css";
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
  whatsappText: "Hi Louise, I'd like to enquire about a labour matter.",
  email: "louise@lawgical.co.za",
  // Paste your Formspree endpoint here (e.g. "https://formspree.io/f/abcdwxyz").
  // While empty, the form opens the visitor's email app addressed to `email`.
  formEndpoint: "",
  preview: import.meta.env.VITE_PREVIEW === "1",
};

const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => [...r.querySelectorAll(s)];
const reduceMotion = matchMedia("(prefers-reduced-motion: reduce)").matches;

/* ---------- Contact links ---------- */
$$("[data-cfg-href='tel']").forEach((a) => (a.href = `tel:${SITE.phoneLink}`));
$$("[data-cfg-href='mailto']").forEach((a) => (a.href = `mailto:${SITE.email}`));
$$("[data-cfg-href='wa']").forEach((a) => (a.href = `https://wa.me/${SITE.whatsapp}?text=${encodeURIComponent(SITE.whatsappText)}`));
$$("[data-year]").forEach((el) => (el.textContent = new Date().getFullYear()));

/* ---------- Smooth scroll ---------- */
const lenis = new Lenis({ duration: 1.1, smoothWheel: !reduceMotion });
lenis.on("scroll", ScrollTrigger.update);
gsap.ticker.add((t) => lenis.raf(t * 1000));
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
lenis.on("scroll", ({ scroll }) => nav.classList.toggle("is-scrolled", scroll > 20));

$$('a[href^="#"]').forEach((a) =>
  a.addEventListener("click", (e) => {
    const id = a.getAttribute("href");
    const target = id.length > 1 && $(id);
    if (!target) return;
    e.preventDefault();
    setMenu(false);
    lenis.scrollTo(target, { offset: id === "#top" || id === "#home" ? -200 : -100, duration: reduceMotion ? 0 : 1.2 });
    try { history.replaceState(null, "", id); } catch (_) {}
    if (id === "#consult") setTimeout(() => $("#f-name").focus({ preventScroll: true }), reduceMotion ? 0 : 1200);
  })
);

const navLinks = $$(".nav__links a[href^='#']:not(.btn)");
navLinks.forEach((a) => {
  const sec = $(a.getAttribute("href"));
  if (!sec) return;
  ScrollTrigger.create({
    trigger: sec, start: "top 50%", end: "bottom 50%",
    onToggle: (self) => self.isActive && navLinks.forEach((l) => l.classList.toggle("is-current", l === a)),
  });
});

/* ---------- Services carousel ---------- */
const track = $(".carousel__track");
const barFill = $(".carousel__bar span");
const updateBar = () => {
  const max = track.scrollWidth - track.clientWidth;
  const visible = track.clientWidth / track.scrollWidth;
  barFill.style.width = `${Math.max(12, visible * 100)}%`;
  barFill.style.transform = `translateX(${max ? (track.scrollLeft / max) * ((1 / visible) - 1) * 100 : 0}%)`;
};
track.addEventListener("scroll", updateBar, { passive: true });
addEventListener("resize", updateBar);
updateBar();
$$("[data-dir]").forEach((b) =>
  b.addEventListener("click", () => {
    const card = $(".svc", track);
    const step = card.getBoundingClientRect().width + 18;
    track.scrollBy({ left: Number(b.dataset.dir) * step, behavior: reduceMotion ? "auto" : "smooth" });
  })
);

/* ---------- Blog slider ---------- */
const posts = $$(".post");
const postN = $("[data-post-n]");
let current = 0;
const showPost = (i) => {
  current = (i + posts.length) % posts.length;
  posts.forEach((p, k) => {
    p.classList.toggle("is-active", k === current);
    p.setAttribute("aria-hidden", k === current ? "false" : "true");
  });
  postN.textContent = current + 1;
};
$$("[data-post]").forEach((b) => b.addEventListener("click", () => showPost(current + Number(b.dataset.post))));
showPost(0);

/* ---------- Gentle motion ---------- */
if (!reduceMotion) {
  // Hero entrance
  gsap.from(".hero__triad span:not(.sr-only)", { y: 24, opacity: 0, duration: 1.1, ease: "power3.out", stagger: 0.18, delay: 0.1 });
  gsap.from([".rule", ".hero__slogan", ".hero__sub", ".hero__ctas"], { y: 16, opacity: 0, duration: 1, ease: "power3.out", stagger: 0.1, delay: 0.6 });
  gsap.from(".arch--back", { yPercent: -8, opacity: 0, duration: 1.4, ease: "power3.out" });
  gsap.from(".arch--front", { yPercent: 8, opacity: 0, duration: 1.4, ease: "power3.out", delay: 0.15 });
  // Subtle parallax on the arches
  $$("[data-speed]").forEach((el) =>
    gsap.to(el, { yPercent: Number(el.dataset.speed) * 100, ease: "none", scrollTrigger: { trigger: ".hero", start: "top top", end: "bottom top", scrub: true } })
  );
  // Section reveals
  $$(".reveal").forEach((el) =>
    gsap.from(el, { y: 32, opacity: 0, duration: 1, ease: "power3.out", scrollTrigger: { trigger: el, start: "top 88%", once: true } })
  );
  // Services cards
  gsap.from(".svc", { y: 30, opacity: 0, duration: 0.9, ease: "power3.out", stagger: 0.07, scrollTrigger: { trigger: ".carousel", start: "top 85%", once: true } });
  // Line under section headings draws in
  $$(".head-line__rule").forEach((el) =>
    gsap.from(el, { scaleX: 0, transformOrigin: "0 50%", duration: 1.4, ease: "power3.out", scrollTrigger: { trigger: el, start: "top 90%", once: true } })
  );
}

/* ---------- Consultation form ---------- */
const form = $("#consult");
const status = $(".form-status", form);
const fields = {
  name: [$("#f-name"), $("#e-name"), (v) => v.trim().length >= 2 || "Please enter your name."],
  company: [$("#f-company"), $("#e-company"), (v) => v.trim().length >= 2 || "Please enter your company name."],
  phone: [$("#f-phone"), $("#e-phone"), (v) => v.replace(/\D/g, "").length >= 9 || "Please enter a phone number we can reach you on, e.g. 082 123 4567."],
  matter: [$("#f-matter"), $("#e-matter"), (v) => !!v || "Please choose how we can help."],
};
const check = (k) => {
  const [input, err, rule] = fields[k];
  const r = rule(input.value);
  const msg = r === true ? "" : r;
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
    status.textContent = `Thank you, ${data.name.split(" ")[0]}. Louise will contact you shortly.`;
  } catch {
    status.textContent = `Sorry, your request didn't send. Please call or WhatsApp ${SITE.phone}.`;
  } finally {
    btn.classList.remove("is-loading");
  }
});

addEventListener("load", () => ScrollTrigger.refresh());
document.fonts?.ready.then(() => ScrollTrigger.refresh());
