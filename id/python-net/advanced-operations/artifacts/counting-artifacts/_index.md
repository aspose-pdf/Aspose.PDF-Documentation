---
title: Hitung Artefak PDF dalam Python
linktitle: Menghitung Artefak
type: docs
weight: 40
url: /id/python-net/counting-artifacts/
description: Pelajari cara memeriksa dan menghitung artefak paginasi dalam dokumen PDF menggunakan Python dengan Aspose.PDF for Python via .NET.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Menghitung Artefak dalam PDF menggunakan Python
Abstract: Artefak paginasi seperti watermark, latar belakang, header, dan footer biasanya digunakan dalam dokumen PDF untuk memberikan struktur, merek, dan identifikasi. Contoh ini menunjukkan cara memeriksa dan menghitung artefak tersebut secara programatik menggunakan Aspose.PDF for Python via .NET. Dengan menyaring artefak pada sebuah halaman dan mengelompokkannya berdasarkan subtipe, pengembang dapat dengan cepat menganalisis komposisi dokumen dan memverifikasi keberadaan elemen tertentu. Kode yang disediakan mengilustrasikan cara membuka PDF, mengekstrak artefak paginasi dari halaman pertama, menghitung setiap subtipe, dan menampilkan hasilnya, menawarkan pendekatan praktis untuk audit dan validasi dokumen.
---

## Menghitung Artefak dari Tipe Tertentu

Periksa dan hitung artefak paginasi dalam PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) menggunakan Aspose.PDF for Python via .NET. Artefak paginasi mencakup elemen seperti watermark, latar belakang, header, dan footer yang diterapkan pada halaman untuk tujuan tata letak dan identifikasi. Dengan memfilter [`Artifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/) objek pada sebuah [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) dan mengelompokkannya berdasarkan subtipe (`Artifact.ArtifactSubtype`), pengembang dapat dengan cepat menganalisis struktur dokumen dan memverifikasi keberadaan elemen tertentu.

Untuk menghitung jumlah total artefak dari tipe tertentu (misalnya, total watermark), gunakan kode berikut. Contoh ini memfilter halaman [`Artifacts`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) koleksi (sebuah [`ArtifactCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/)) oleh [`Artifact.ArtifactType`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/#properties) dan kemudian menghitung subtipe (`Artifact.ArtifactSubtype`).

1. Buka dokumen PDF (lihat [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)).
1. Filter artefak paginasi menggunakan halaman [`Artifacts`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) koleksi.
1. Hitung artefak berdasarkan subtipe (`Artifact.ArtifactSubtype`).
1. Cetak hasil.

```python

from os import path
from collections import Counter
import sys
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

## Topik Artefak Terkait

- [Bekerja dengan artefak PDF dalam Python](/pdf/id/python-net/artifacts/)
- [Menambahkan watermark ke PDF dalam Python](/pdf/id/python-net/add-watermarks/)
- [Tambahkan latar belakang PDF di Python](/pdf/id/python-net/add-backgrounds/)
- [Menambahkan penomoran Bates ke PDF dalam Python](/pdf/id/python-net/add-bates-numbering/)
