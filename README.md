# konveksihasan.com

Website statis Konveksi Hasan (seragam nasional TK).

## Struktur

- `templates/home.html` — isi beranda
- `content/posts/*.md` — artikel blog (frontmatter: `title`, `description`, `date` YYYY-MM-DD, opsional `slug`, `keyword`, `status: draft`)
- `tools/build.py` — membangun `index.html`, `blog/`, `404.html`, `sitemap.xml`, `robots.txt`
- `assets/` — CSS dan gambar. Foto produk: simpan sebagai `assets/img/produk.jpg` (atau `.webp`/`.png`) lalu build ulang
- `.cpanel.yml` — perintah deploy cPanel ke `/home/konvek17/public_html/`

## Menambah artikel

1. Buat `content/posts/<slug>.md`
2. `pip install markdown && python3 tools/build.py`
3. Commit dan push ke `main`. cPanel menarik perubahan dan menjalankan deploy.

Artikel bertanggal di masa depan tidak ikut terbit sampai build berikutnya pada/setelah tanggal itu.
