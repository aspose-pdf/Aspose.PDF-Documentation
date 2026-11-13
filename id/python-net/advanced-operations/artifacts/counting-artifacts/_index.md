---
title: Menghitung artefak paginasi pada PDF dengan Python
linktitle: Menghitung artefak paginasi
type: docs
weight: 40
url: /id/python-net/counting-artifacts/
description: Hitung tanda air, latar belakang, header, dan footer berdasarkan subtipe artefak paginasi pada halaman PDF dalam Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Menghitung artefak paginasi pada PDF dengan Python
Abstract: Hitung artefak paginasi pada halaman PDF untuk memeriksa tanda air, latar belakang, header, dan footer.
---

Hitung artefak paginasi pada halaman PDF untuk memeriksa tanda air, latar belakang, header, dan footer.

## Menghitung artefak berdasarkan subtipe

Saring koleksi `artifacts` pada halaman pertama berdasarkan tipe `PAGINATION`, lalu hitung artefak per subtipe. Contoh ini mencetak nol jika suatu subtipe tidak ditemukan.

```python
from collections import Counter
import aspose.pdf as ap

def count_pdf_artifacts(infile):
    """Count and display artifacts of different types on the first page."""
    with ap.Document(infile) as document:
        pagination_artifacts = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
        ]

        subtypes = [artifact.subtype for artifact in pagination_artifacts]
        counts = Counter(subtypes)

        print(f"Watermarks: {counts.get(ap.Artifact.ArtifactSubtype.WATERMARK, 0)}")
        print(f"Backgrounds: {counts.get(ap.Artifact.ArtifactSubtype.BACKGROUND, 0)}")
        print(f"Headers: {counts.get(ap.Artifact.ArtifactSubtype.HEADER, 0)}")
        print(f"Footers: {counts.get(ap.Artifact.ArtifactSubtype.FOOTER, 0)}")
```

## Topik terkait

- [Artefak PDF](/pdf/id/python-net/artifacts/)
- [Mengekstrak detail tanda air](/pdf/id/python-net/extract-watermarks/)
- [Menghapus tanda air](/pdf/id/python-net/remove-watermarks/)
- [Menghapus latar belakang](/pdf/id/python-net/remove-backgrounds/)
- [Menghapus header dan footer](/pdf/id/python-net/remove-headers-footers/)
