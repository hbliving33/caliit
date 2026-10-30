// Cali IT site script: menu, reveal on scroll, testimonial rotator, IT health check, contact form, visit counter.
(() => {
  const SB_URL = "https://mefvxxoytleyfjbwtxix.supabase.co";   // Supabase project "valve-partners" (shared by all Valve Partners sites)
  const SB_KEY = "sb_publishable_Ex6vMImvvkTdQsFYprve7g_awiuqxEs";   // public key: can only add form entries and count visits
  const MAIL_TO = "[email removed]";
  const W3F_KEY = "b88fef65-1434-4f2b-8b2d-9b9cb760e7f0";   // Web3Forms access key for [email removed] (public by design; it can only send to that address)
  const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;

  // mobile menu
  const btn = document.querySelector(".burger"), nav = document.getElementById("nav");
  if (btn && nav) {
    btn.addEventListener("click", () => { const open = nav.classList.toggle("open"); btn.setAttribute("aria-expanded", open); });
    addEventListener("keydown", (e) => { if (e.key === "Escape" && nav.classList.contains("open")) { nav.classList.remove("open"); btn.setAttribute("aria-expanded", "false"); btn.focus(); } });
  }

  // reveal on scroll
  const io = "IntersectionObserver" in window && !reduce ? new IntersectionObserver((es) => es.forEach((e) => { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } }), { rootMargin: "0px 0px -8% 0px" }) : null;
  document.querySelectorAll(".reveal").forEach((el) => (io ? io.observe(el) : el.classList.add("in")));

  // services list steers the cube; the cube's tour lights up the matching row
  const list = document.getElementById("svcList"), picker = document.getElementById("picker");
  if (list && picker) {
    const rows = [...list.querySelectorAll("li")];
    const byName = (n) => rows.find((r) => r.dataset.name === n);
    const light = () => { const on = picker.querySelector('[aria-pressed="true"]'); rows.forEach((r) => r.classList.toggle("lit", !!on && r.dataset.name === on.textContent.trim())); };
    new MutationObserver(light).observe(picker, { subtree: true, attributes: true, attributeFilter: ["aria-pressed"] });
    rows.forEach((r) => {
      const go = () => { if (!window.dcCube) return; const i = window.dcCube.names.indexOf(r.dataset.name); if (i >= 0) window.dcCube.select(i); };
      r.addEventListener("pointerenter", go); r.querySelector("a").addEventListener("focus", go);
    });
  }

  // map chips: each one cycles through the technologies we support
  const chips = [...document.querySelectorAll(".chip[data-words]")];
  if (chips.length && !reduce) {
    chips.forEach((c, i) => {
      const words = c.dataset.words.split("|"); let n = 0;
      setTimeout(() => setInterval(() => {
        c.classList.add("swap");
        setTimeout(() => { n = (n + 1) % words.length; c.textContent = words[n]; c.classList.remove("swap"); }, 250);
      }, 3600), 4200 + i * 700);
    });
  }

  // security news and Microsoft 365 status: assets/data/news.json is refreshed hourly by a GitHub Action
  const newsList = document.getElementById("newsList"), m365 = document.getElementById("m365Status");
  if (newsList || m365) {
    const ago = (iso) => { const m = Math.round((Date.now() - new Date(iso)) / 60000); if (!(m >= 0)) return ""; if (m < 60) return m <= 1 ? "just now" : m + " minutes ago"; const h = Math.round(m / 60); if (h < 24) return h + (h === 1 ? " hour ago" : " hours ago"); const d = Math.round(h / 24); return d + (d === 1 ? " day ago" : " days ago"); };
    fetch("assets/data/news.json?t=" + Math.floor(Date.now() / 600000)).then((r) => r.json()).then((data) => {
      if (newsList) {
        const items = (data.items || []).slice(0, +newsList.dataset.limit || 6);
        newsList.textContent = "";
        if (!items.length) { const li = document.createElement("li"); li.className = "news-empty"; li.textContent = "Headlines will appear here shortly."; newsList.appendChild(li); }
        items.forEach((it) => {
          const li = document.createElement("li"), a = document.createElement("a"), meta = document.createElement("span");
          a.href = it.link; a.target = "_blank"; a.rel = "noopener"; a.textContent = it.title;
          meta.className = "news-meta"; meta.textContent = it.source + "  \u00b7  " + ago(it.date);
          li.append(meta, a); newsList.appendChild(li);
        });
      }
      if (m365 && data.m365) {
        const st = (data.m365.status || "Unknown"), ok = /^available$/i.test(st), t = m365.querySelector(".m365-t");
        m365.classList.add(ok ? "ok" : st === "Unknown" ? "unk" : "warn");
        t.textContent = ok ? "No widespread incidents reported" + (data.m365.checked ? ", checked " + ago(data.m365.checked) : "") + "." : st === "Unknown" ? "Status unavailable right now.  Open Microsoft's status page." : "Microsoft reports: " + st + ".  Open the status page for details.";
      }
    }).catch(() => { if (newsList) newsList.innerHTML = '<li class="news-empty">Headlines are unavailable right now.</li>'; });
  }

  // testimonial rotator
  const rot = document.getElementById("quoteRot");
  if (rot) {
    const items = [...rot.querySelectorAll("figure")]; let i = 0, paused = false;
    rot.addEventListener("pointerenter", () => (paused = true)); rot.addEventListener("pointerleave", () => (paused = false));
    if (items.length > 1 && !reduce) setInterval(() => { if (paused) return; items[i].classList.remove("on"); i = (i + 1) % items.length; items[i].classList.add("on"); }, 7000);
  }

  // IT health check (runs only in the browser; nothing is sent unless the visitor chooses to)
  const qs = document.getElementById("questions");
  if (qs) {
    const answers = {}; const total = qs.querySelectorAll("li").length;
    const num = document.getElementById("gaugeNum"), title = document.getElementById("verdictTitle"), text = document.getElementById("verdictText"), cta = document.getElementById("checkCta");
    qs.addEventListener("click", (e) => {
      const b = e.target.closest("button"); if (!b) return;
      const li = b.closest("li"); li.querySelectorAll("button").forEach((x) => x.setAttribute("aria-pressed", x === b));
      answers[li.dataset.q] = b.dataset.v === "1";
      const done = Object.keys(answers).length, yes = Object.values(answers).filter(Boolean).length;
      num.innerHTML = `${yes}<small> of ${total}</small>`;
      if (done < total) { title.textContent = `${total - done} to go`; text.textContent = "Keep going to see where you stand."; return; }
      const gaps = total - yes;
      title.textContent = gaps === 0 ? "In good shape" : gaps <= 2 ? "A few gaps to close" : "Worth a closer look";
      text.textContent = gaps === 0 ? "Nice work.  A second set of eyes can still confirm it holds up." : `You answered "No" ${gaps} time${gaps > 1 ? "s" : ""}.  Each one is a gap worth closing, and most are quick to fix.`;
      const missed = [...qs.querySelectorAll("li")].filter((li) => answers[li.dataset.q] === false).map((li) => "- " + li.querySelector("p").textContent.trim());
      const msg = `IT health check: ${yes} of ${total}.` + (missed.length ? `\nAnswered "No" to:\n${missed.join("\n")}` : "");
      cta.href = "contact.html?topic=" + encodeURIComponent("IT and security assessment") + "&msg=" + encodeURIComponent(msg);
      cta.hidden = false;
    });
  }

  // contact form: save to the database and email a copy, then go to the thank-you page
  const form = document.getElementById("contactForm");
  if (form) {
    const p = new URLSearchParams(location.search);
    if (p.get("topic")) { const s = form.elements.topic; [...s.options].forEach((o) => { if (o.value === p.get("topic")) s.value = o.value; }); }
    if (p.get("msg")) form.elements.message.value = p.get("msg");
    const out = document.getElementById("formMsg");
    form.addEventListener("submit", async (e) => {
      e.preventDefault();
      if (!form.reportValidity()) return;
      const f = form.elements;
      if (f._honey.value) { location.href = "thanks.html"; return; }   // bots fill hidden fields
      const send = form.querySelector("button[type=submit]"); send.disabled = true; send.textContent = "Sending...";
      out.hidden = true;
      const row = { site: "caliit", name: f.name.value.trim(), company: f.company.value.trim() || null, email: f.email.value.trim(), phone: f.phone.value.trim() || null,
        topic: f.topic.value || null, company_size: f.size.value || null, message: f.message.value.trim(), page: location.pathname };
      const db = fetch(`${SB_URL}/rest/v1/contact_requests`, { method: "POST", headers: { apikey: SB_KEY, "Content-Type": "application/json", Prefer: "return=minimal" }, body: JSON.stringify(row) })
        .then((r) => r.ok).catch(() => false);
      const fields = { Name: row.name, Company: row.company || "", Email: row.email, Phone: row.phone || "", Topic: row.topic || "", "Company size": row.company_size || "", Message: row.message };
      const mail = (W3F_KEY
        ? fetch("https://api.web3forms.com/submit", { method: "POST", headers: { "Content-Type": "application/json", Accept: "application/json" },
            body: JSON.stringify({ access_key: W3F_KEY, subject: "New Cali IT website message", from_name: "Cali IT website", replyto: row.email, ...fields }) })
        : fetch(`https://formsubmit.co/ajax/${MAIL_TO}`, { method: "POST", headers: { "Content-Type": "application/json", Accept: "application/json" },
            body: JSON.stringify({ _subject: "New Cali IT website message", _template: "table", _captcha: "false", _replyto: row.email, ...fields }) }))
        .then((r) => r.ok).catch(() => false);
      const [a, b] = await Promise.all([db, mail]);
      if (a || b) { location.href = "thanks.html"; return; }
      send.disabled = false; send.textContent = "Send message";
      out.hidden = false; out.className = "form-msg err";
      out.textContent = "Sorry, the message didn't go through.  Please try again in a minute.";
    });
  }

  // visit counter: one count per page per browser session.  No cookies, no personal data.
  if (!/^(localhost|127\.)/.test(location.hostname)) {
    const path = location.pathname.replace(/index\.html$/, "") || "/";
    let seen = false; try { const k = "cali-hit:" + path; seen = !!sessionStorage.getItem(k); sessionStorage.setItem(k, "1"); } catch (e) {}
    if (!seen) fetch(`${SB_URL}/rest/v1/rpc/count_hit`, { method: "POST", keepalive: true, headers: { apikey: SB_KEY, "Content-Type": "application/json" }, body: JSON.stringify({ p_site: "caliit", p_path: path }) }).catch(() => {});
  }
})();
