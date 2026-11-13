# konveksihasan.com

Website statis Konveksi Hasan (seragam nasional TK).

## Struktur

- `templates/home.html` — isi beranda
- `content/posts/*.md` — artikel blog (frontmatter: `title` = H1, `description` 120–160 karakter, `date` YYYY-MM-DD, opsional `seo_title` maks 60 karakter, `slug`, `keyword`, `status: draft`)
- `tools/seo_check.py` — cek SEO semua halaman (title 30–60, description 120–160, 1 H1, canonical, OG, alt gambar, JSON-LD, link internal, sitemap)
- `tools/build.py` — membangun `index.html`, `blog/`, `404.html`, `sitemap.xml`, `robots.txt`
- `assets/` — CSS dan gambar. Foto produk: simpan sebagai `assets/img/produk.jpg` (atau `.webp`/`.png`) lalu build ulang
- `docs/panduan-artikel.md` — aturan dan format artikel otomatis
- `tools/cron-deploy.sh` — dijalankan Cron Job cPanel tiap 15 menit: git pull + deploy bila ada commit baru
- `.cpanel.yml` — perintah deploy cPanel ke `/home/konvek17/public_html/`

## Menambah artikel

1. Buat `content/posts/<slug>.md`
2. `pip install markdown && python3 tools/build.py && python3 tools/seo_check.py` (wajib lolos)
3. Commit dan push ke `main`. cPanel menarik perubahan dan menjalankan deploy.

Artikel bertanggal di masa depan tidak ikut terbit sampai build berikutnya pada/setelah tanggal itu.
