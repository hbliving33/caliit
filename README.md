# caliit.com

Cali IT Consulting website, hosted on GitHub Pages.

- `python3 build/site2_build.py` rebuilds every public page (layout).  Content lives in `build/site_build.py`.
- Styles: `assets/css/cali.css`.  Scripts: `assets/js/site.js` (menu, health check, contact form, visit counter), `cube.js` and `heroswap.js` (home page cube).
- Logo files (high-resolution PNG and vector PDF): `assets/brand/`.
- Contact form saves to the Supabase project "caliit" (table `contact_requests`) and emails a copy through FormSubmit.
- Review pages (not linked, noindex): `logos.html`, `focus.html`, `pick.html`.
