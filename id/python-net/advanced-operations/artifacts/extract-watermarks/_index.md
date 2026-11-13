---
title: Mengekstrak detail tanda air pada PDF dengan Python
linktitle: Mengekstrak detail tanda air
type: docs
weight: 50
url: /id/python-net/extract-watermarks/
description: Baca teks dan persegi pembatas artefak tanda air pada halaman pertama PDF dengan Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Mengekstrak detail tanda air pada PDF dengan Python
Abstract: Baca teks dan persegi pembatas artefak tanda air pada halaman pertama PDF dengan Python.
---

Baca teks dan persegi pembatas artefak tanda air pada halaman pertama PDF dengan Python.

## Membaca teks dan batas tanda air

Cetak teks dan persegi panjang pembatas setiap artefak paginasi dengan subtipe `WATERMARK`.

```python
import aspose.pdf as ap

def extract_watermark_from_pdf(infile):
    with ap.Document(infile) as document:
        watermarks = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and artifact.subtype == ap.Artifact.ArtifactSubtype.WATERMARK
        ]

        for watermark in watermarks:
            print(f"{watermark.text} {watermark.rectangle}")
```

## Topik terkait

- [Menambahkan tanda air](/pdf/id/python-net/add-watermarks/)
- [Menghapus tanda air](/pdf/id/python-net/remove-watermarks/)
- [Artefak PDF](/pdf/id/python-net/artifacts/)
