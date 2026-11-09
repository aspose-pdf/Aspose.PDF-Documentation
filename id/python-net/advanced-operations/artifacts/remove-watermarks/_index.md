---
title: Menghapus tanda air dari PDF dengan Python
linktitle: Menghapus tanda air
type: docs
weight: 90
url: /id/python-net/remove-watermarks/
description: Hapus artefak tanda air dari halaman pertama PDF dalam Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Menghapus tanda air dari PDF dengan Python
Abstract: Hapus artefak tanda air dari halaman pertama PDF dalam Python.
---

Hapus artefak tanda air dari halaman pertama PDF dalam Python.

## Menghapus artefak tanda air

Contoh ini hanya menghapus artefak bertipe `PAGINATION` dan bersubtipe `WATERMARK` dari halaman pertama. Tanda air yang terlihat dan tersimpan sebagai teks biasa pada halaman, gambar, atau anotasi tetap ada dalam PDF.

```python
import aspose.pdf as ap

def delete_watermark_artifact(infile, outfile):
    with ap.Document(infile) as document:
        watermarks = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and artifact.subtype == ap.Artifact.ArtifactSubtype.WATERMARK
        ]

        for watermark in watermarks:
            document.pages[1].artifacts.delete(watermark)

        document.save(outfile)
```

## Topik terkait

- [Menambahkan tanda air](/pdf/id/python-net/add-watermarks/)
- [Mengekstrak detail tanda air](/pdf/id/python-net/extract-watermarks/)
- [Artefak PDF](/pdf/id/python-net/artifacts/)
