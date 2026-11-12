#!/usr/bin/env python3
"""Pemeriksaan SEO untuk semua halaman hasil build.

Jalankan setelah tools/build.py. Keluar dengan kode 1 bila ada pelanggaran,
supaya artikel baru tidak terbit dengan SEO yang kurang.

  python3 tools/seo_check.py
"""
import html
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://konveksihasan.com"

TITLE_MIN, TITLE_MAX = 30, 60
DESC_MIN, DESC_MAX = 120, 160


def halaman():
    hasil = [ROOT / "index.html", ROOT / "blog/index.html", ROOT / "404.html"]
    hasil += sorted((ROOT / "blog").glob("*/index.html"))
    return hasil


def url_dari_file(p: Path) -> str:
    rel = p.relative_to(ROOT).as_posix()
    if rel == "404.html":
        return "/404.html"
    return "/" + rel[: -len("index.html")]


def ada_file_untuk(path: str) -> bool:
    path = path.split("#")[0].split("?")[0]
    if not path or path == "/":
        return (ROOT / "index.html").exists()
    target = ROOT / path.lstrip("/")
    if path.endswith("/"):
        return (target / "index.html").exists()
    return target.exists()


def cek(p: Path):
    s = p.read_text(encoding="utf-8")
    galat, peringatan = [], []
    path = url_dari_file(p)
    is404 = path == "/404.html"

    t = re.search(r"<title>(.*?)</title>", s, re.S)
    title = html.unescape(t.group(1).strip()) if t else ""
    if not title:
        galat.append("title kosong")
    elif not is404 and not (TITLE_MIN <= len(title) <= TITLE_MAX):
        galat.append(f"panjang title {len(title)} (harus {TITLE_MIN}-{TITLE_MAX}): {title}")

    d = re.search(r'<meta name="description" content="(.*?)"', s)
    desc = html.unescape(d.group(1)) if d else ""
    if not desc:
        galat.append("meta description kosong")
    elif not is404 and not (DESC_MIN <= len(desc) <= DESC_MAX):
        galat.append(f"panjang description {len(desc)} (harus {DESC_MIN}-{DESC_MAX})")

    h1 = len(re.findall(r"<h1[\s>]", s))
    if h1 != 1:
        galat.append(f"jumlah h1 = {h1} (harus 1)")

    c = re.search(r'<link rel="canonical" href="(.*?)"', s)
    if not c:
        galat.append("canonical tidak ada")
    elif c.group(1) != SITE + path:
        galat.append(f"canonical {c.group(1)} tidak sama dengan {SITE + path}")

    for wajib in ('property="og:title"', 'property="og:description"', 'property="og:image"',
                  'name="twitter:card"', '<html lang="id">', 'name="viewport"'):
        if wajib not in s:
            galat.append(f"tidak ada {wajib}")

    robots = re.search(r'<meta name="robots" content="(.*?)"', s)
    if robots and "noindex" in robots.group(1) and not is404:
        galat.append("halaman diberi noindex")

    for img in re.findall(r"<img\b[^>]*>", s):
        if not re.search(r'\salt="[^"]+"', img):
            galat.append(f"gambar tanpa alt: {img[:80]}")
        if "width=" not in img or "height=" not in img:
            peringatan.append(f"gambar tanpa width/height: {img[:80]}")

    for blok in re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
        try:
            json.loads(blok)
        except json.JSONDecodeError as e:
            galat.append(f"JSON-LD tidak valid: {e}")

    for href in re.findall(r'href="(/[^"]*)"', s):
        if href.startswith("//"):
            continue
        if not ada_file_untuk(href):
            galat.append(f"link internal rusak: {href}")

    for src in re.findall(r'src="(/[^"]*)"', s):
        if not ada_file_untuk(src):
            galat.append(f"file tidak ditemukan: {src}")

    # struktur heading: tidak loncat dari h1 langsung ke h3 di dalam main
    main = re.search(r"<main>(.*)</main>", s, re.S)
    if main:
        level = [int(x) for x in re.findall(r"<h([1-6])[\s>]", main.group(1))]
        for a, b in zip(level, level[1:]):
            if b > a + 1:
                peringatan.append(f"heading meloncat h{a} -> h{b}")
                break

    return path, title, desc, galat, peringatan


def cek_sitemap():
    galat = []
    sm = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    for loc in re.findall(r"<loc>(.*?)</loc>", sm):
        u = urlparse(loc)
        if u.netloc != urlparse(SITE).netloc:
            galat.append(f"sitemap berisi domain lain: {loc}")
        elif not ada_file_untuk(u.path):
            galat.append(f"sitemap menunjuk halaman yang tidak ada: {loc}")
    return galat


def main():
    total_galat = 0
    judul_terlihat, desk_terlihat = {}, {}
    for p in halaman():
        if not p.exists():
            continue
        path, title, desc, galat, peringatan = cek(p)
        if path != "/404.html":
            if title in judul_terlihat:
                galat.append(f"title sama dengan {judul_terlihat[title]}")
            if desc in desk_terlihat:
                galat.append(f"description sama dengan {desk_terlihat[desc]}")
            judul_terlihat[title] = path
            desk_terlihat[desc] = path
        status = "OK " if not galat else "GAGAL"
        print(f"[{status}] {path}  (title {len(title)}, desc {len(desc)})")
        for g in galat:
            print(f"   x {g}")
        for w in peringatan:
            print(f"   ! {w}")
        total_galat += len(galat)
    sg = cek_sitemap()
    for g in sg:
        print(f"   x {g}")
    total_galat += len(sg)
    print(f"\n{total_galat} masalah ditemukan." if total_galat else "\nSemua halaman lolos pemeriksaan SEO.")
    sys.exit(1 if total_galat else 0)


if __name__ == "__main__":
    main()
