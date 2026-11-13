#!/usr/bin/env python3
"""Cek copywriting (aturan antislop, versi bahasa Indonesia) untuk artikel dan teks beranda.

Sumber aturan: antislop copywriting skill (MIT, Miqdad Badjuber)
https://github.com/miqdadbadjuber/anti-slop/blob/main/skills/antislop-copywriting/SKILL.md

Cek otomatis ini hanya menangkap pola yang bisa dikenali mesin. Pola lain
(rule of three yang dipaksakan, klaim tanpa bukti, kalimat pasif tanpa pelaku)
tetap harus diperiksa saat membaca ulang, sesuai docs/panduan-artikel.md.

  python3 tools/copy_check.py      # keluar dengan kode 1 bila ada pelanggaran
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

ATURAN = [
    (r"—", "em dash (R-02): ganti dengan titik, koma, titik dua, atau kurung"),
    (r"–", "en dash: tulis rentang dengan kata 'sampai' atau tanda hubung"),
    (r"\b[Aa]rtikel ini (membahas|menjelaskan|berisi|membantu|merangkum|akan)\b",
     "kalimat pengumuman (signposting): langsung tulis isinya"),
    (r"\b(Mari kita|Yuk,? kita|Simak (ulasan|penjelasan)|Tanpa basa-basi)\b",
     "kalimat pengumuman (signposting)"),
    (r"\b[Dd]i (era|zaman) (digital|modern|sekarang|serba)\b|\b[Dd]i dunia yang (serba|semakin)\b",
     "pembuka klise waktu (temporal runway)"),
    (r"\b(bukan sekadar|tidak hanya\b[^.]{0,80}\btetapi juga)\b",
     "paralelisme negatif ('bukan sekadar X', 'tidak hanya X tetapi juga Y')"),
    (r"\b(Semoga (bermanfaat|artikel ini)|Jangan ragu untuk|Sampai jumpa)\b",
     "penutup gaya chatbot"),
    (r"\b(Masa depan (cerah|terlihat)|Ingat baik-baik|Camkan)\b",
     "penutup atau penegasan teatrikal"),
    (r"\b(terpercaya|terbaik di|nomor satu|no\. ?1|berkualitas tinggi|kualitas terbaik|termurah|"
     r"paling murah|dijamin|garansi|bergaransi|ribuan (sekolah|pelanggan|klien)|ratusan (sekolah|pelanggan|klien))\b",
     "klaim tanpa bukti (R-36): hapus atau minta data asli ke Hasan"),
    (r"\b(revolusioner|inovatif|canggih|mutakhir|tak tertandingi|kelas dunia|solusi terbaik|next level)\b",
     "kata kosong/buzzword (R-16)"),
    (r"^\s*(?:-|\d+\.)\s+\*\*[^*\n]+\*\*", "butir daftar diawali label tebal (inline-header list)"),
    (r"^#{1,6} .*[\U0001F300-\U0001FAFF☀-➿]", "emoji di judul"),
    (r"\b(DAPATKAN|SEGERA|SEKARANG JUGA|PROMO|GRATIS)\b", "huruf kapital untuk penekanan"),
]


def berkas():
    hasil = sorted((ROOT / "content/posts").glob("*.md"))
    hasil.append(ROOT / "templates/home.html")
    return hasil


def main():
    total = 0
    for f in berkas():
        teks = f.read_text(encoding="utf-8")
        temuan = []
        for no, baris in enumerate(teks.splitlines(), 1):
            if f.suffix == ".html" and ("<path" in baris or "<svg" in baris):
                continue
            for pola, pesan in ATURAN:
                if re.search(pola, baris, re.I if pola.startswith(r"\b(terpercaya") else 0):
                    temuan.append(f"   x baris {no}: {pesan}\n     {baris.strip()[:110]}")
        bold = len(re.findall(r"\*\*[^*\n]+\*\*", teks))
        if f.suffix == ".md" and bold > 6:
            temuan.append(f"   x {bold} teks tebal: kurangi penebalan (maksimal 6 per artikel)")
        status = "OK " if not temuan else "GAGAL"
        print(f"[{status}] {f.relative_to(ROOT)}")
        for t in temuan:
            print(t)
        total += len(temuan)
    print(f"\n{total} masalah copywriting." if total else "\nSemua teks lolos cek copywriting.")
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
