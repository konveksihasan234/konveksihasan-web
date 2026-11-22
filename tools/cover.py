#!/usr/bin/env python3
"""Gambar sampul artikel (1200x630) dari foto asli seragam + judul artikel.

Dipanggil oleh tools/build.py. Hasil: assets/img/blog/<slug>.jpg
Dipakai sebagai gambar utama artikel, og:image, thumbnail di daftar blog, dan gambar di schema.
Butuh: pip install pillow
"""
import hashlib
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parent.parent
FOTO = ROOT / "assets/img/foto"
OUT = ROOT / "assets/img/blog"
FONT_JUDUL = str(ROOT / "tools/fonts/Baloo2-ExtraBold.ttf")
FONT_TEKS = str(ROOT / "tools/fonts/Figtree-SemiBold.ttf")

BIRU = (31, 58, 104)
KUNING = (255, 200, 69)
PUTIH = (255, 255, 255)
BIRU_MUDA = (220, 230, 245)
W, H, PANEL = 1200, 630, 660


def katalog():
    return json.loads((FOTO / "katalog.json").read_text(encoding="utf-8"))


def pilih_foto(slug, nama=None, kecuali=()):
    """Foto dari frontmatter `foto`, atau dipilih tetap berdasarkan slug."""
    kat = katalog()
    if nama:
        if nama not in kat:
            raise SystemExit(f"{slug}: foto '{nama}' tidak ada di assets/img/foto/katalog.json")
        return nama
    pilihan = [k for k in sorted(kat) if k not in kecuali] or sorted(kat)
    return pilihan[int(hashlib.md5(slug.encode()).hexdigest(), 16) % len(pilihan)]


def _bungkus(draw, teks, font, lebar):
    baris, kini = [], ""
    for kata in teks.split():
        coba = f"{kini} {kata}".strip()
        if draw.textlength(coba, font=font) <= lebar:
            kini = coba
        else:
            baris.append(kini)
            kini = kata
    if kini:
        baris.append(kini)
    return baris


def buat(slug, judul, foto):
    OUT.mkdir(parents=True, exist_ok=True)
    tujuan = OUT / f"{slug}.jpg"

    img = Image.new("RGB", (W, H), BIRU)
    ft = ImageOps.fit(Image.open(FOTO / foto).convert("RGB"), (W - PANEL, H), centering=(0.5, 0.3))
    img.paste(ft, (PANEL, 0))
    d = ImageDraw.Draw(img)

    d.text((64, 58), "Blog Konveksi Hasan", font=ImageFont.truetype(FONT_TEKS, 30), fill=KUNING)
    for ukuran in (64, 58, 52, 46, 42):
        f = ImageFont.truetype(FONT_JUDUL, ukuran)
        baris = _bungkus(d, judul, f, PANEL - 128)
        if len(baris) <= 5:
            break
    y = 120
    tinggi = int(ukuran * 1.12)
    for b in baris[:5]:
        d.text((60, y), b, font=f, fill=PUTIH)
        y += tinggi
    d.rectangle((64, H - 96, 64 + 72, H - 90), fill=KUNING)
    d.text((64, H - 76), "konveksihasan.com", font=ImageFont.truetype(FONT_TEKS, 28), fill=BIRU_MUDA)
    d.rectangle((0, H - 12, PANEL, H), fill=KUNING)

    img.save(tujuan, "JPEG", quality=84, optimize=True, progressive=True)
    return tujuan
