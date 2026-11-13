# Panduan artikel blog konveksihasan.com

Dipakai oleh scheduled task posting otomatis (Senin, Selasa, Kamis, Sabtu) dan siapa pun yang menulis artikel.

## Pembaca

Kepala sekolah TK/PAUD, guru, komite sekolah, dan orang tua yang mengurus pengadaan seragam. Tujuan akhir setiap artikel: pembaca menghubungi WhatsApp untuk pesan seragam.

## Fakta bisnis yang BOLEH dipakai (hanya ini)

| Hal | Fakta |
|---|---|
| Nama | Konveksi Hasan |
| Produk | Seragam nasional TK |
| Contoh model | Kemeja putih lengan pendek, rompi biru dengan badge TK, dasi atau dasi kupu-kupu, rok lipit (putri) atau celana pendek (putra), topi putih-biru |
| Harga | Kisaran Rp70.000–Rp100.000 per pcs; harga pasti via WhatsApp |
| Minimal order | 25 pcs |
| Lama produksi | 3 minggu – 1 bulan, tergantung antrean order |
| Ukuran | Tersedia beberapa pilihan, detail via WhatsApp (JANGAN menulis daftar ukuran) |
| Kontak | WhatsApp 0812-8765-8415 |

Belum diketahui, JANGAN ditulis atau ditebak: alamat, jam operasional, area pengiriman, ongkos kirim, jenis bahan atau kain, garansi, testimoni, jumlah klien, tahun berdiri, diskon.

## Aturan isi

1. Tidak mengarang fakta, angka, statistik, testimoni, atau nama klien.
2. Aturan atau regulasi pemerintah hanya boleh disebut bila ada sumber primer resmi (situs pemerintah) yang dibuka saat menulis; cantumkan tautannya di artikel. Bila tidak yakin, jangan sebut regulasi.
3. Pengetahuan umum yang stabil (cara mengukur badan anak, cara mencuci dan menyetrika seragam, cara menyusun rekap ukuran, perencanaan jadwal pengadaan) boleh ditulis tanpa sumber.
4. Tidak menyebut nama pesaing.
5. Bahasa Indonesia yang ramah dan jelas, kalimat aktif, sapaan "Anda" atau netral. Tidak berlebihan dan tidak menjual secara agresif.
6. Satu artikel = satu topik dan satu keyword utama. Tidak boleh mengulang topik atau keyword artikel yang sudah ada di `content/posts/`.

## Format file

Lokasi: `content/posts/<slug>.md`. Slug huruf kecil dengan tanda hubung, mengandung keyword utama, maksimal sekitar 6 kata.

```
---
title: Judul H1 yang mengandung keyword utama
description: 120–160 karakter, mengandung keyword, menjelaskan manfaat membaca.
date: YYYY-MM-DD (tanggal hari ini, zona Asia/Jakarta)
seo_title: Judul untuk <title>, maksimal 60 karakter (opsional bila title sudah ≤ 47 karakter)
keyword: keyword utama
---
```

Isi (Markdown):
- 900–1.400 kata.
- Paragraf pembuka 2–3 kalimat yang langsung menjawab inti pertanyaan pembaca.
- 4–7 subjudul `##` (boleh `###` di bawahnya). Jangan memakai `#` (H1 sudah dari title).
- Minimal satu tabel atau daftar bernomor/berpoin yang benar-benar berguna.
- Minimal satu tautan internal ke `/#produk` atau `/#cara-pesan`, dan satu tautan ke artikel lain di `/blog/<slug>/` bila relevan.
- Bagian tanya-jawab singkat (2–4 pertanyaan) di akhir bila cocok, memakai `###` per pertanyaan.
- Jangan menulis kotak ajakan WhatsApp sendiri; template sudah menambahkannya.

## Alur terbit

1. `pip install --break-system-packages -q markdown`
2. `python3 tools/build.py`
3. `python3 tools/seo_check.py` harus lolos (0 masalah). Bila gagal, perbaiki artikel; jangan mengubah aturan cek.
4. Commit semua perubahan (artikel + file hasil build) ke `main`, lalu push.
5. Cron Job di cPanel menarik dan men-deploy dalam ≤ 15 menit.

## Ide topik awal (riset keyword tetap wajib sebelum memilih)

- Ukuran seragam TK: cara mengukur badan anak
- Kapan waktu ideal memesan seragam untuk tahun ajaran baru
- Cara menyusun rekap ukuran seragam per kelas
- Perlengkapan seragam nasional TK: rompi, dasi, topi
- Cara merawat seragam TK agar awet dan tetap putih
- Seragam TK putra vs putri: perbedaan model
- Tips komite sekolah mengelola pengadaan seragam
- Menghitung anggaran seragam TK per kelas
- Seragam PAUD dan TK: hal yang perlu disiapkan sekolah baru
