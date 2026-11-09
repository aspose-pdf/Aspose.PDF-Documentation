---
title: Menambahkan latar belakang pada PDF dengan Python
linktitle: Menambahkan latar belakang
type: docs
weight: 20
url: /id/python-net/add-backgrounds/
description: Tambahkan gambar dan latar belakang berwarna solid ke halaman PDF dalam Python serta sesuaikan opasitas gambar latar belakang.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Menambahkan latar belakang pada PDF dengan Python
Abstract: Tambahkan gambar dan latar belakang berwarna solid ke halaman PDF dalam Python serta sesuaikan opasitas gambar latar belakang.
---

Gunakan `BackgroundArtifact` untuk menempatkan gambar atau warna padat di belakang konten halaman PDF. Contoh-contoh ini memodifikasi halaman pertama.

## Menambahkan gambar latar belakang ke PDF

Isi properti `background_image` dengan aliran gambar, lalu tambahkan artefak ke halaman.

```python
from io import FileIO
import aspose.pdf as ap

def add_background_image_to_pdf(infile, imagefile, outfile, opacity=1.0):
    """Add a background image to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_image = FileIO(imagefile, "rb")
        artifact.opacity = opacity
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## Menambahkan gambar latar belakang dengan opasitas ke PDF

Berikan nilai opasitas antara 0 dan 1 ke fungsi yang sama. Gunakan `0.5` untuk membuat gambar semitransparan.

```python
add_background_image_to_pdf("input.pdf", "background.png", "output.pdf", opacity=0.5)
```

## Menambahkan warna latar belakang ke PDF

Atur properti `background_color` pada artefak untuk menerapkan warna solid.

```python
import aspose.pdf as ap

def add_background_color_to_pdf(infile, outfile):
    """Add a solid color background to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_color = ap.Color.dark_khaki
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## Topik terkait

- [Menghapus latar belakang](/pdf/id/python-net/remove-backgrounds/)
- [Artefak PDF](/pdf/id/python-net/artifacts/)
