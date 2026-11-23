# Panduan artikel blog konveksihasan.com

Dipakai oleh scheduled task posting otomatis (Senin, Selasa, Kamis, Sabtu) dan siapa pun yang menulis artikel.

## Pembaca

Kepala sekolah TK/PAUD, guru, komite sekolah, dan orang tua yang mengurus pengadaan seragam. Tujuan akhir setiap artikel: pembaca menghubungi WhatsApp untuk pesan seragam.

## Fakta bisnis yang BOLEH dipakai (hanya ini)

| Hal | Fakta |
|---|---|
| Nama | Konveksi Hasan |
| Produk | Seragam TK dan PAUD: seragam nasional, seragam muslim (kerudung, peci), seragam PAUD, seragam olahraga, dan model kotak-kotak; warna dan model bisa disesuaikan dengan seragam sekolah |
| Contoh model nasional | Kemeja putih lengan pendek, rompi biru dengan badge TK, dasi atau dasi kupu-kupu, rok lipit (putri) atau celana pendek (putra), topi putih-biru |
| Harga | Kisaran Rp70.000 sampai Rp100.000 per set (atasan dan bawahan), berlaku juga untuk model lain; harga pasti via WhatsApp |
| Minimal order | 25 pcs (semua model) |
| Lama produksi | 3 minggu sampai 1 bulan, tergantung antrean order |
| Ukuran | Tersedia beberapa pilihan, detail via WhatsApp (JANGAN menulis daftar ukuran) |
| Kontak | WhatsApp 0812-8765-8415 |
| Alamat | Bawan RT.02/RW.10, Dusun IV, Mrisen, Kec. Juwiring, Kab. Klaten, Jawa Tengah 57472 (boleh ditulis "Juwiring, Klaten") |
| Jam buka | Setiap hari, 09.00 sampai 19.00 WIB |
| Tempat produksi | Dijahit sendiri di alamat Klaten di atas (boleh menulis "kami menjahit") |

Belum diketahui, JANGAN ditulis atau ditebak: area pengiriman, ongkos kirim, jenis bahan atau kain, garansi, testimoni, jumlah klien, tahun berdiri, diskon.

## Aturan isi

1. Tidak mengarang fakta, angka, statistik, testimoni, atau nama klien.
2. Aturan atau regulasi pemerintah hanya boleh disebut bila ada sumber primer resmi (situs pemerintah) yang dibuka saat menulis; cantumkan tautannya di artikel. Bila tidak yakin, jangan sebut regulasi.
3. Pengetahuan umum yang stabil (cara mengukur badan anak, cara mencuci dan menyetrika seragam, cara menyusun rekap ukuran, perencanaan jadwal pengadaan) boleh ditulis tanpa sumber.
4. Tidak menyebut nama pesaing.
5. Bahasa Indonesia yang ramah dan jelas, kalimat aktif, sapaan "Anda" atau netral. Tidak berlebihan dan tidak menjual secara agresif.
6. Satu artikel = satu topik dan satu keyword utama. Tidak boleh mengulang topik atau keyword artikel yang sudah ada di `content/posts/`.

## Aturan copywriting (antislop)

Diadaptasi dari antislop copywriting skill (MIT): https://github.com/miqdadbadjuber/anti-slop/blob/main/skills/antislop-copywriting/SKILL.md . Tujuannya: tulisan terdengar seperti ditulis orang, bukan mesin, dan tidak memuat fakta karangan.

Yang dilarang:
- Fakta, angka, nama, tanggal, testimoni, atau klaim yang tidak ada di tabel fakta bisnis di atas. Bila kalimat butuh detail yang tidak ada, tulis versi sederhana tanpa detail itu.
- Klaim tanpa bukti: "terpercaya", "terbaik", "berkualitas tinggi", "dijamin", "ribuan sekolah", "nomor satu".
- Kata kosong: "revolusioner", "inovatif", "solusi terbaik", "next level", dan sejenisnya. Tulis manfaat yang spesifik.
- Pembuka klise waktu: "Di era digital...", "Di zaman serba cepat...". Mulai langsung dari pokok bahasan.
- Kalimat pengumuman: "Artikel ini membahas...", "Mari kita bahas...", "Simak ulasannya...". Langsung tulis isinya.
- Paralelisme negatif: "bukan sekadar X, melainkan Y", "tidak hanya X tetapi juga Y".
- Penegasan teatrikal dan penutup gaya chatbot: "Ingat baik-baik", "Semoga bermanfaat!", "Jangan ragu untuk...". Akhiri dengan fakta konkret terakhir.
- Em dash (—) dan en dash (–). Pakai titik, koma, titik dua, kurung, atau kata "sampai" untuk rentang.
- Butir daftar yang diawali label tebal ("- **Harga:** ..."), emoji di judul, huruf kapital untuk penekanan, dan teks tebal berlebihan (maksimal 6 per artikel).
- Kelompok tiga yang dipaksakan. Daftar berisi sebanyak yang memang dibutuhkan isinya.
- Kalimat pasif tanpa pelaku bila pelakunya jelas. Tulis "Kami kirim penawaran", bukan "Penawaran akan dikirimkan".
- Ajakan (CTA) umum seperti "Pelajari lebih lanjut". Tulis tindakannya: "Minta penawaran via WhatsApp".

Yang dijaga:
- Suara yang ramah dan jelas untuk kepala sekolah, guru, komite, dan orang tua. Variasikan panjang kalimat.
- Pakai kata yang paling jelas berulang kali, jangan berganti-ganti sinonim hanya untuk menghindari pengulangan.

Sebelum terbit, jalankan dua cek: `python3 tools/copy_check.py` (otomatis) lalu baca ulang dan jawab dua pertanyaan: "Bagian mana yang terdengar seperti tulisan mesin?" dan "Apakah ada fakta, nama, angka, atau tanggal yang tidak ada di tabel fakta bisnis?" Perbaiki sampai jawabannya "tidak ada".

## Gambar artikel

Setiap artikel otomatis mendapat dua gambar dari foto asli seragam Konveksi Hasan:

1. Sampul 1200x630 berisi judul artikel dan satu foto, dibuat oleh `tools/cover.py` saat build. Sampul dipakai di atas artikel, di daftar blog, sebagai gambar saat link dibagikan (og:image), dan di schema.
2. Satu foto di dalam artikel, otomatis diletakkan sebelum subjudul kedua, lengkap dengan keterangan.

Pilih foto yang paling cocok dengan topik lewat frontmatter `foto` (sampul) dan `foto_isi` (di dalam artikel). Bila tidak diisi, build memilih sendiri. Jangan memakai gambar dari internet, gambar buatan AI, atau foto yang tidak ada di daftar ini, karena pembaca akan menganggapnya produk Konveksi Hasan.

| File | Isi foto |
|---|---|
| `produk.webp` | Satu set seragam nasional TK putri: kemeja putih, rompi biru berbadge TK, dasi kupu-kupu, dan rok lipit |
| `seragam-tk-1.webp` | Seragam TK putri dengan dasi, rok lipit, dan topi putih-biru |
| `seragam-tk-2.webp` | Seragam TK putra dengan dasi, celana pendek, dan topi putih-biru |
| `seragam-tk-3.webp` | Seragam TK putri dengan dasi kupu-kupu dan topi putih-biru |
| `seragam-tk-4.webp` | Topi seragam TK putih-biru dengan logo TK |
| `video-1.webp` | Rompi biru dan dasi pada seragam TK putri |
| `video-2.webp` | Seragam TK dengan rompi biru, dasi, dan badge TK dilihat dari samping |
| `video-3.webp` | Seragam TK putra: rompi biru, dasi, dan celana pendek |
| `video-4.webp` | Detail rompi biru dan dasi seragam TK |
| `video-5.webp` | Detail badge TK di dada rompi biru |
| `video-6.webp` | Detail kerah kemeja putih dan rompi biru seragam TK |
| `video-7.webp` | Seragam TK putri lengkap dengan topi, dasi, dan rok lipit |
| `video-8.webp` | Seragam TK dengan dasi kupu-kupu dan badge TK |
| `video-9.webp` | Seragam TK dengan dasi kupu-kupu dan topi putih-biru |
| `video-10.webp` | Seragam TK putri dengan rompi biru, rok lipit, dan topi putih-biru |
| `video-11.webp` | Rompi biru dan rok lipit seragam TK |
| `video-12.webp` | Topi putih-biru dan rompi seragam TK |
| `seragam-tk-muslim-putri-kotak-oranye.webp` | Seragam TK muslim putri motif kotak-kotak oranye dengan rok lipit dan kerudung oranye |
| `seragam-tk-muslim-putra-kotak-oranye.webp` | Seragam TK muslim putra motif kotak-kotak oranye dengan celana panjang dan peci |
| `seragam-paud-kuning-kerah-pelaut.webp` | Seragam PAUD kuning dengan kerah pelaut, dasi, dan celana panjang kotak-kotak merah |
| `seragam-tk-muslim-putri-kotak-biru-muda.webp` | Seragam TK muslim putri kemeja kotak-kotak biru muda dengan rok dan kerudung biru |
| `seragam-tk-rompi-kotak-biru-putri.webp` | Seragam TK putri: kemeja kotak-kotak biru muda, rompi biru berbadge TK, dasi kupu-kupu, dan rok lipit |
| `seragam-tk-rompi-kotak-biru-putra.webp` | Seragam TK putra: kemeja kotak-kotak biru muda, rompi biru berbadge TK, dasi kupu-kupu, dan celana pendek |
| `seragam-tk-rompi-lengan-panjang.webp` | Seragam TK kemeja lengan panjang biru muda dengan rompi biru dan celana panjang |
| `seragam-paud-hijau-rok-kotak.webp` | Seragam PAUD kemeja hijau dengan dasi dan rok lipit kotak-kotak biru |
| `seragam-paud-hijau-celana-kotak.webp` | Seragam PAUD kemeja hijau dengan dasi dan celana pendek kotak-kotak biru |
| `seragam-tk-biru-muda-celana-kotak.webp` | Seragam TK kemeja biru muda dengan kerah kotak-kotak dan celana pendek kotak-kotak |
| `seragam-tk-biru-muda-rok-kotak.webp` | Seragam TK kemeja biru muda dengan kerah kotak-kotak dan rok lipit kotak-kotak |
| `seragam-tk-muslim-putra-kotak-biru.webp` | Seragam TK muslim putra kotak-kotak biru dengan peci dan celana panjang |
| `seragam-olahraga-tk-merah-kuning.webp` | Seragam olahraga TK merah-kuning dengan celana training |
| `seragam-olahraga-tk-muslim-merah-kuning.webp` | Seragam olahraga TK muslim merah-kuning dengan kerudung dan celana training |
| `seragam-tk-muslim-putri-kotak-biru.webp` | Seragam TK muslim putri kotak-kotak biru dengan rok lipit dan kerudung biru |
| `seragam-tk-muslim-putih-hijau.webp` | Seragam TK muslim putih-hijau dengan kerudung dan celana panjang hijau |
| `seragam-tk-muslim-kuning-cokelat.webp` | Seragam TK muslim kuning lengan panjang dengan celana panjang cokelat |
| `seragam-tk-putri-kotak-hijau-kerah-lebar.webp` | Seragam TK putri kotak-kotak hijau dengan kerah lebar, dasi kupu-kupu, dan rok lipit hijau |
| `seragam-tk-merah-pita-kotak.webp` | Seragam TK merah dengan kerah dan pita kotak-kotak serta celana pendek kotak-kotak |

Foto baru dari Hasan disimpan di `assets/img/foto/` (format .webp) lalu ditambahkan ke `assets/img/foto/katalog.json` beserta keterangan yang sesuai isi foto.

## Format file

Lokasi: `content/posts/<slug>.md`. Slug huruf kecil dengan tanda hubung, mengandung keyword utama, maksimal sekitar 6 kata.

```
---
title: Judul H1 yang mengandung keyword utama
description: 120–160 karakter, mengandung keyword, menjelaskan manfaat membaca.
date: YYYY-MM-DD (tanggal hari ini, zona Asia/Jakarta)
seo_title: Judul untuk <title>, maksimal 60 karakter (opsional bila title sudah ≤ 47 karakter)
keyword: keyword utama
foto: nama file dari tabel Gambar artikel (opsional)
foto_isi: nama file lain dari tabel yang sama (opsional)
---
```

Isi (Markdown):
- 750–1.400 kata. Utamakan isi yang berguna, jangan menambah kalimat hanya untuk memenuhi jumlah kata.
- Paragraf pembuka 2–3 kalimat yang langsung menjawab inti pertanyaan pembaca.
- 4–7 subjudul `##` (boleh `###` di bawahnya). Jangan memakai `#` (H1 sudah dari title).
- Minimal satu tabel atau daftar bernomor/berpoin yang benar-benar berguna.
- Minimal satu tautan internal ke `/#produk` atau `/#cara-pesan`, dan satu tautan ke artikel lain di `/blog/<slug>/` bila relevan.
- Bagian tanya-jawab singkat (2–4 pertanyaan) di akhir bila cocok, memakai `###` per pertanyaan.
- Jangan menulis kotak ajakan WhatsApp sendiri; template sudah menambahkannya.

## Alur terbit

1. `pip install --break-system-packages -q markdown pillow`
2. `python3 tools/build.py`
3. `python3 tools/seo_check.py` dan `python3 tools/copy_check.py` harus lolos (0 masalah). Bila gagal, perbaiki artikel; jangan mengubah aturan cek.
4. Commit semua perubahan (artikel + file hasil build) ke `main`, lalu push.
5. Cron Job di cPanel menarik dan men-deploy dalam ≤ 15 menit.

## Artikel yang sudah ditulis lebih dulu

Artikel boleh ditulis lebih awal dengan `date` di masa depan. `tools/build.py` hanya menerbitkan artikel dengan tanggal hari ini (WIB) atau sebelumnya, jadi artikel itu baru tayang setelah build pada tanggalnya. Run terjadwal pada tanggal tersebut cukup menjalankan build, cek SEO, commit, dan push.

Jadwal yang sudah terisi: 14, 16, 17, 19, 21, 23, 24, 26, 28, dan 30 November 2026, serta 3, 5, 7, dan 8 Desember 2026.

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
