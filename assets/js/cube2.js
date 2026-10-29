// Preview: a cube whose tiles ARE the services.  The front face carries nine services, the top face carries the tenth.
// Drag to spin, click a tile to open that service.  The side faces show technologies we support.
(() => {
  const root = document.getElementById("cube2");
  if (!root) return;
  const data = JSON.parse(document.getElementById("cube2-data").textContent);
  const panel = document.getElementById("cube2-panel");
  const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;

  // faces: name, transform, tiles
  const faces = {
    front: data.front, top: data.top,
    right: data.techs.slice(0, 9), left: data.techs.slice(9, 18), back: data.techs.slice(18, 27), bottom: data.techs.slice(27, 36)
  };
  const tf = { front: "translateZ(var(--h))", back: "rotateY(180deg) translateZ(var(--h))", right: "rotateY(90deg) translateZ(var(--h))",
               left: "rotateY(-90deg) translateZ(var(--h))", top: "rotateX(90deg) translateZ(var(--h))", bottom: "rotateX(-90deg) translateZ(var(--h))" };
  const tiles = [];
  for (const [name, list] of Object.entries(faces)) {
    const f = document.createElement("div");
    f.className = "c2-face c2-" + name; f.style.transform = tf[name];
    for (let i = 0; i < 9; i++) {
      const it = list[i];
      const t = document.createElement(it && it.slug ? "a" : "div");
      t.className = "c2-tile" + (it && it.slug ? " svc" : " tech");
      if (it && it.slug) {
        t.href = it.slug + ".html";
        t.innerHTML = `<b>${it.code}</b><span>${it.name}</span>`;
        t.setAttribute("aria-label", it.name);
        t.addEventListener("pointerenter", () => show(it, t));
        t.addEventListener("focus", () => show(it, t));
        tiles.push(t);
      } else {
        t.innerHTML = `<span>${it ? it : ""}</span>`;
      }
      f.appendChild(t);
    }
    root.appendChild(f);
  }

  function show(it, t) {
    tiles.forEach((x) => x.classList.toggle("on", x === t));
    panel.innerHTML = `<p class="c2-k">${it.name}</p><p class="c2-d">${it.short}</p><a class="link" href="${it.slug}.html">Open ${it.name}</a>`;
  }

  // rotation: drag to spin, idle drift, ease back toward the front face so the services stay readable
  let rx = -18, ry = -28, vx = 0, vy = 0, drag = false, moved = 0, lx = 0, ly = 0, last = performance.now(), idle = 0;
  const stage = root.parentElement;
  stage.addEventListener("pointerdown", (e) => { drag = true; moved = 0; lx = e.clientX; ly = e.clientY; stage.setPointerCapture(e.pointerId); });
  stage.addEventListener("pointermove", (e) => {
    if (!drag) return;
    const dx = e.clientX - lx, dy = e.clientY - ly; lx = e.clientX; ly = e.clientY; moved += Math.abs(dx) + Math.abs(dy);
    ry += dx * .45; rx -= dy * .45; vy = dx * .45; vx = -dy * .45; idle = 0;
  });
  const end = () => { drag = false; };
  stage.addEventListener("pointerup", end); stage.addEventListener("pointercancel", end);
  // a drag is not a click
  root.addEventListener("click", (e) => { if (moved > 8) { e.preventDefault(); e.stopPropagation(); } }, true);

  function frame(now) {
    const dt = Math.min(50, now - last) / 16.7; last = now;
    if (!drag) {
      idle += dt;
      rx += vx * dt; ry += vy * dt; vx *= .92; vy *= .92;
      if (idle > 90 && !reduce) {
        // settle back so the front face (the services) faces the viewer, with a gentle sway
        const tx = -16 + Math.sin(now / 2400) * 6, ty = -24 + Math.sin(now / 3100) * 14;
        const near = (a, b) => a + ((((b - a) % 360) + 540) % 360 - 180);
        rx += (near(rx, tx) - rx) * .03 * dt; ry += (near(ry, ty) - ry) * .03 * dt;
      }
    }
    root.style.transform = `rotateX(${rx}deg) rotateY(${ry}deg)`;
    requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);
  if (tiles[4]) show(data.front[4], tiles[4]);
})();
