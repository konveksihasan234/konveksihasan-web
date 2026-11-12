#!/usr/bin/env python3
"""Build situs statis konveksihasan.com.

Sumber:
  templates/home.html      isi beranda
  content/posts/*.md       artikel blog (frontmatter + markdown)
Hasil (di root repo, ikut di-commit dan di-deploy cPanel):
  index.html, blog/index.html, blog/<slug>/index.html, 404.html, sitemap.xml, robots.txt

Pakai:  python3 tools/build.py
Butuh:  pip install markdown
"""
import html
import json
import re
from datetime import date, datetime
from pathlib import Path
from urllib.parse import quote

import markdown

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://konveksihasan.com"
NAMA = "Konveksi Hasan"
WA_NOMOR = "6281287658415"
WA_TAMPIL = "0812-8765-8415"
WA_PESAN = "Halo Konveksi Hasan, saya ingin tanya pesanan seragam TK."
WA_LINK = f"https://wa.me/{WA_NOMOR}?text={quote(WA_PESAN)}"

WA_ICON = (
    '<svg class="ikon-wa" viewBox="0 0 24 24" aria-hidden="true" fill="currentColor">'
    '<path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38'
    'c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91S17.5 2 12.04 2zm5.8 14.06c-.24.68'
    '-1.42 1.31-1.96 1.36-.5.05-1.13.07-1.83-.11-.42-.13-.96-.31-1.65-.61-2.9-1.25-4.79-4.17'
    '-4.94-4.36-.14-.19-1.18-1.57-1.18-3s.75-2.13 1.02-2.42c.26-.29.58-.36.77-.36h.55c.18 0 '
    '.42-.07.65.5.24.58.82 2.01.89 2.15.07.15.12.32.02.51-.1.19-.14.31-.29.48-.14.17-.3.37'
    '-.43.5-.14.14-.29.3-.13.59.17.29.74 1.22 1.59 1.98 1.09.97 2.01 1.27 2.3 1.42.29.14.46'
    '.12.62-.07.17-.19.72-.84.91-1.13.19-.29.38-.24.65-.14.26.1 1.68.79 1.97.94.29.14.48.22'
    '.55.34.07.12.07.7-.17 1.38z"/></svg>'
)

LOGO = (
    '<svg width="40" height="40" viewBox="0 0 40 40" aria-hidden="true">'
    '<circle cx="20" cy="20" r="19" fill="#1F3A68"/>'
    '<path d="M11 14 L16 11 Q20 14 24 11 L29 14 L33 19 L30 22 L27 20 L27 30 L13 30 L13 20 '
    'L10 22 L7 19 Z" fill="#fff"/>'
    '<path d="M16 11 Q20 14 24 11 L23 16 L20 14 L17 16 Z" fill="#FFC845"/>'
    '<path d="M15 27 h10" stroke="#E2403A" stroke-width="1.6" stroke-dasharray="2 2"/>'
    '</svg>'
)

BULAN = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli",
         "Agustus", "September", "Oktober", "November", "Desember"]


def tanggal_id(d: date) -> str:
    return f"{d.day} {BULAN[d.month - 1]} {d.year}"


def esc(s: str) -> str:
    return html.escape(s, quote=True)


# ---------- layout ----------

def layout(*, title, description, path, body, aktif="", jsonld=None, og_type="website"):
    url = SITE + path
    nav = [("/", "Beranda", "beranda"), ("/#produk", "Produk", "produk"),
           ("/#cara-pesan", "Cara pesan", "cara"), ("/blog/", "Blog", "blog")]
    nav_html = "".join(
        f'<a href="{href}"{" aria-current=\"page\"" if key == aktif else ""}>{label}</a>'
        for href, label, key in nav
    )
    ld = ""
    for obj in (jsonld or []):
        ld += f'<script type="application/ld+json">{json.dumps(obj, ensure_ascii=False)}</script>\n'
    tahun = date.today().year
    return f"""<!doctype html>
<html lang="id">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="id_ID">
<meta property="og:site_name" content="{NAMA}">
<meta name="theme-color" content="#1F3A68">
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@600;700;800&family=Figtree:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/style.css">
{ld}</head>
<body>
<header class="kepala">
  <div class="wadah">
    <a class="merek" href="/">{LOGO}<span class="merek-nama">Konveksi Hasan<small>Seragam sekolah TK</small></span></a>
    <nav class="nav" aria-label="Menu utama">{nav_html}
      <a class="tombol tombol-wa tombol-kecil" href="{WA_LINK}" target="_blank" rel="noopener">{WA_ICON} WhatsApp</a>
    </nav>
  </div>
</header>
<main>
{body}
</main>
<footer class="kaki">
  <div class="wadah">
    <div class="kaki-grid">
      <div>
        <h3>Konveksi Hasan</h3>
        <p>Konveksi seragam nasional untuk TK dan PAUD. Minimal order 25 pcs.</p>
      </div>
      <div>
        <h3>Kontak</h3>
        <ul>
          <li>WhatsApp: <a href="{WA_LINK}" target="_blank" rel="noopener">{WA_TAMPIL}</a></li>
          <li>Alamat: <span class="placeholder">segera diperbarui</span></li>
          <li>Jam buka: <span class="placeholder">segera diperbarui</span></li>
        </ul>
      </div>
      <div>
        <h3>Menu</h3>
        <ul>
          <li><a href="/#produk">Produk</a></li>
          <li><a href="/#cara-pesan">Cara pesan</a></li>
          <li><a href="/blog/">Blog</a></li>
          <li><a href="/#faq">Pertanyaan umum</a></li>
        </ul>
      </div>
    </div>
    <p class="kaki-bawah">© {tahun} Konveksi Hasan. konveksihasan.com</p>
  </div>
</footer>
<a class="wa-mengambang" href="{WA_LINK}" target="_blank" rel="noopener" aria-label="Chat WhatsApp Konveksi Hasan">{WA_ICON}</a>
</body>
</html>
"""


# ---------- artikel ----------

FM = re.compile(r"^---\s*\n(.*?)\n---\s*\n(.*)$", re.S)


def baca_post(p: Path):
    teks = p.read_text(encoding="utf-8")
    m = FM.match(teks)
    if not m:
        raise SystemExit(f"Frontmatter tidak ditemukan: {p}")
    meta = {}
    for baris in m.group(1).splitlines():
        if ":" in baris:
            k, v = baris.split(":", 1)
            meta[k.strip()] = v.strip().strip('"').strip("'")
    for wajib in ("title", "description", "date"):
        if wajib not in meta:
            raise SystemExit(f"{p.name}: field '{wajib}' wajib ada")
    meta["date"] = datetime.strptime(meta["date"], "%Y-%m-%d").date()
    meta["slug"] = meta.get("slug") or p.stem
    meta["isi_html"] = markdown.markdown(m.group(2), extensions=["tables", "sane_lists"])
    meta["status"] = meta.get("status", "publish")
    return meta


def kartu_post(post):
    return (
        f'<li class="artikel-item"><a href="/blog/{post["slug"]}/">'
        f'<time datetime="{post["date"].isoformat()}">{tanggal_id(post["date"])}</time>'
        f'<h3>{esc(post["title"])}</h3><p>{esc(post["description"])}</p></a></li>'
    )


def daftar_post(posts):
    if not posts:
        return '<p class="artikel-kosong">Artikel pertama segera terbit.</p>'
    return '<ul class="daftar-artikel">' + "".join(kartu_post(p) for p in posts) + "</ul>"


def halaman_post(post):
    path = f"/blog/{post['slug']}/"
    body = f"""<article class="artikel">
  <div class="wadah">
    <div class="artikel-isi">
      <nav class="remah" aria-label="Remah roti"><a href="/">Beranda</a> / <a href="/blog/">Blog</a></nav>
      <h1>{esc(post['title'])}</h1>
      <p class="artikel-meta">Diterbitkan <time datetime="{post['date'].isoformat()}">{tanggal_id(post['date'])}</time> oleh Konveksi Hasan</p>
      {post['isi_html']}
      <div class="kotak-cta">
        <p>Butuh seragam TK untuk sekolah? Minimal order 25 pcs, kisaran Rp70–100 ribu per pcs.</p>
        <a class="tombol tombol-wa" href="{WA_LINK}" target="_blank" rel="noopener">{WA_ICON} Tanya via WhatsApp</a>
      </div>
    </div>
  </div>
</article>"""
    jsonld = [{
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": post["title"],
        "description": post["description"],
        "datePublished": post["date"].isoformat(),
        "dateModified": post.get("updated", post["date"].isoformat()) if isinstance(post.get("updated"), str) else post["date"].isoformat(),
        "author": {"@type": "Organization", "name": NAMA, "url": SITE},
        "publisher": {"@type": "Organization", "name": NAMA, "url": SITE},
        "mainEntityOfPage": SITE + path,
        "inLanguage": "id-ID",
    }, {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Beranda", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": SITE + "/blog/"},
            {"@type": "ListItem", "position": 3, "name": post["title"], "item": SITE + path},
        ],
    }]
    return path, layout(title=f"{post['title']} | {NAMA}", description=post["description"],
                        path=path, body=body, aktif="blog", jsonld=jsonld, og_type="article")


# ---------- foto produk ----------

def foto_produk():
    for nama in ("produk.webp", "produk.jpg", "produk.png"):
        if (ROOT / "assets/img" / nama).exists():
            return (f'<img src="/assets/img/{nama}" alt="Seragam nasional TK buatan Konveksi Hasan" '
                    f'width="540" height="704" loading="lazy" style="border-radius:18px;width:100%;height:auto">')
    # ilustrasi sementara sampai foto produk dikirim
    return """<svg viewBox="0 0 360 300" role="img" aria-label="Ilustrasi tumpukan seragam terlipat">
  <rect x="40" y="210" width="280" height="56" rx="10" fill="#fff" stroke="#1F3A68" stroke-width="3"/>
  <path d="M150 210 l30 18 l30 -18" fill="#1F3A68"/>
  <rect x="56" y="150" width="248" height="58" rx="10" fill="#fff" stroke="#1F3A68" stroke-width="3"/>
  <path d="M152 150 l28 18 l28 -18" fill="#1F3A68"/>
  <rect x="72" y="92" width="216" height="56" rx="10" fill="#fff" stroke="#1F3A68" stroke-width="3"/>
  <path d="M154 92 l26 17 l26 -17" fill="#1F3A68"/>
  <path d="M84 132 h192 M68 192 h224 M52 250 h256" stroke="#C9D3E3" stroke-width="2" stroke-dasharray="6 6"/>
  <g transform="translate(262 70) rotate(12)">
    <rect x="0" y="0" width="64" height="40" rx="6" fill="#FFC845" stroke="#1F3A68" stroke-width="2"/>
    <circle cx="12" cy="20" r="4" fill="#DCE6F5" stroke="#1F3A68" stroke-width="1.5"/>
    <path d="M24 15 h30 M24 25 h20" stroke="#1F3A68" stroke-width="2.5" stroke-linecap="round"/>
  </g>
  <path d="M30 60 q40 -30 80 0 t80 0" fill="none" stroke="#E2403A" stroke-width="3" stroke-dasharray="5 6" stroke-linecap="round"/>
</svg>"""


# ---------- build ----------

def tulis(path_url: str, isi: str):
    rel = path_url.strip("/")
    out = ROOT / rel / "index.html" if rel else ROOT / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(isi, encoding="utf-8")


def main():
    hari_ini = date.today()
    semua = [baca_post(p) for p in sorted((ROOT / "content/posts").glob("*.md"))]
    # hanya terbitkan artikel berstatus publish dan bertanggal hari ini atau sebelumnya
    posts = sorted([p for p in semua if p["status"] == "publish" and p["date"] <= hari_ini],
                   key=lambda p: (p["date"], p["slug"]), reverse=True)

    slug_terlihat = set()
    for p in posts:
        if p["slug"] in slug_terlihat:
            raise SystemExit(f"Slug ganda: {p['slug']}")
        slug_terlihat.add(p["slug"])

    # beranda
    home = (ROOT / "templates/home.html").read_text(encoding="utf-8")
    home = (home.replace("{{WA_LINK}}", WA_LINK).replace("{{WA_ICON}}", WA_ICON)
                .replace("{{LATEST_POSTS}}", daftar_post(posts[:3]))
                .replace("{{PRODUCT_PHOTO}}", foto_produk()))
    org = {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": NAMA,
        "url": SITE,
        "telephone": "+" + WA_NOMOR,
        "description": "Konveksi seragam nasional untuk TK dan PAUD. Minimal order 25 pcs.",
        "contactPoint": {"@type": "ContactPoint", "telephone": "+" + WA_NOMOR,
                         "contactType": "sales", "availableLanguage": "id"},
    }
    tulis("/", layout(
        title="Konveksi Seragam TK — Min. Order 25 pcs | Konveksi Hasan",
        description="Konveksi seragam nasional TK dan PAUD. Harga Rp70–100 ribu per pcs, minimal order 25 pcs, produksi 3 minggu–1 bulan. Tanya via WhatsApp.",
        path="/", body=home, aktif="beranda", jsonld=[org]))

    # blog index
    blog_body = f"""<section class="halaman-kepala">
  <div class="wadah">
    <nav class="remah" aria-label="Remah roti"><a href="/">Beranda</a> / Blog</nav>
    <h1>Blog seragam TK</h1>
    <p>Panduan memesan, memilih ukuran, dan merawat seragam TK untuk sekolah dan orang tua.</p>
  </div>
</section>
<section class="bagian bagian-putih" style="padding-top:48px">
  <div class="wadah">{daftar_post(posts)}</div>
</section>"""
    tulis("/blog/", layout(title=f"Blog Seragam TK | {NAMA}",
                           description="Artikel seputar seragam TK: cara pesan, ukuran, bahan, dan perawatan dari Konveksi Hasan.",
                           path="/blog/", body=blog_body, aktif="blog"))

    # halaman artikel
    for p in posts:
        path, isi = halaman_post(p)
        tulis(path, isi)

    # 404
    body404 = f"""<section class="halaman-kepala"><div class="wadah">
<h1>Halaman tidak ditemukan</h1>
<p>Alamat yang kamu buka tidak ada. Kembali ke beranda atau tanya langsung lewat WhatsApp.</p>
<p><a class="tombol tombol-garis" href="/">Ke beranda</a></p>
</div></section>"""
    (ROOT / "404.html").write_text(
        layout(title=f"Halaman tidak ditemukan | {NAMA}", description="Halaman tidak ditemukan.",
               path="/404.html", body=body404).replace(
            '<meta name="description"', '<meta name="robots" content="noindex">\n<meta name="description"'),
        encoding="utf-8")

    # sitemap + robots
    urls = [(SITE + "/", hari_ini), (SITE + "/blog/", posts[0]["date"] if posts else hari_ini)]
    urls += [(f"{SITE}/blog/{p['slug']}/", p["date"]) for p in posts]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    sm += [f"  <url><loc>{u}</loc><lastmod>{d.isoformat()}</lastmod></url>" for u, d in urls]
    sm.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(sm) + "\n", encoding="utf-8")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")

    print(f"Build selesai: {len(posts)} artikel terbit, {len(semua) - len(posts)} terjadwal/draft.")


if __name__ == "__main__":
    main()
