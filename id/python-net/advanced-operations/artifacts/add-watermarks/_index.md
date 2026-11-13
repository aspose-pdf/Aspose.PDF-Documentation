---
title: Menambahkan tanda air pada PDF dengan Python
linktitle: Menambahkan tanda air
type: docs
weight: 30
url: /id/python-net/add-watermarks/
description: Tambahkan artefak tanda air teks bergaya ke halaman PDF dalam Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Menambahkan tanda air pada PDF dengan Python
Abstract: Tambahkan artefak tanda air teks bergaya ke halaman PDF dalam Python.
---

Gunakan `WatermarkArtifact` untuk menambahkan tanda air teks ke halaman pertama sebuah PDF.

## Menambahkan tanda air ke PDF

Atur teks dan gaya, lalu konfigurasi perataan, rotasi, dan opasitas. Atur `is_background` untuk menempatkan tanda air di belakang konten halaman.

```python
import aspose.pdf as ap

def add_watermark_artifact(infile, outfile):
    with ap.Document(infile) as document:
        text_state = ap.text.TextState()
        text_state.font_size = 72
        text_state.foreground_color = ap.Color.blue_violet
        text_state.font_style = ap.text.FontStyles.BOLD
        text_state.font = ap.text.FontRepository.find_font("Arial")

        watermark = ap.WatermarkArtifact()
        watermark.set_text_and_state("WATERMARK", text_state)
        watermark.artifact_horizontal_alignment = ap.HorizontalAlignment.CENTER
        watermark.artifact_vertical_alignment = ap.VerticalAlignment.CENTER
        watermark.rotation = 60
        watermark.opacity = 0.2
        watermark.is_background = True

        document.pages[1].artifacts.append(watermark)
        document.save(outfile)
```

## Topik terkait

- [Mengekstrak detail tanda air](/pdf/id/python-net/extract-watermarks/)
- [Menghapus tanda air](/pdf/id/python-net/remove-watermarks/)
- [Artefak PDF](/pdf/id/python-net/artifacts/)
