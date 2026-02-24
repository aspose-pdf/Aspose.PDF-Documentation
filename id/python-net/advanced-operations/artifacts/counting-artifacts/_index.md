---
title: Menghitung Artefak Tipe Tertentu dalam Python via .NET
linktitle: Menghitung Artefak
type: docs
weight: 40
url: /id/python-net/counting-artifacts/
description: Artikel ini menjelaskan cara memeriksa artefak paginasi dalam dokumen PDF menggunakan Aspose.PDF untuk Python via .NET.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Menghitung Artefak dalam PDF menggunakan Python
Abstract: Artefak paginasi seperti watermark, latar belakang, header, dan footer biasanya digunakan dalam dokumen PDF untuk memberikan struktur, merek, dan identifikasi. Contoh ini menunjukkan cara memeriksa dan menghitung artefak tersebut secara programatik menggunakan Aspose.PDF untuk Python via .NET. Dengan memfilter artefak pada sebuah halaman dan mengelompokkannya berdasarkan subtipe, pengembang dapat dengan cepat menganalisis komposisi dokumen dan memverifikasi keberadaan elemen tertentu. Kode yang disediakan menggambarkan cara membuka PDF, mengekstrak artefak paginasi dari halaman pertama, menghitung setiap subtipe, dan menampilkan hasilnya, memberikan pendekatan praktis untuk audit dan validasi dokumen.
---

## Menghitung Artefak Tipe Tertentu

Memeriksa dan menghitung artefak paginasi dalam PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) menggunakan Aspose.PDF untuk Python via .NET. Artefak paginasi mencakup elemen seperti watermark, latar belakang, header, dan footer yang diterapkan pada halaman untuk tujuan tata letak dan identifikasi. Dengan memfilter objek [`Artifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/) pada sebuah [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) dan mengelompokkannya berdasarkan subtipe (`Artifact.ArtifactSubtype`), pengembang dapat dengan cepat menganalisis struktur dokumen dan memverifikasi keberadaan elemen tertentu.

Untuk menghitung total jumlah artefak dari tipe tertentu (misalnya, total jumlah watermark), gunakan kode berikut. Contoh ini memfilter koleksi [`Artifacts`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) halaman (sebuah [`ArtifactCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/)) berdasarkan [`Artifact.ArtifactType`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/#properties) dan kemudian menghitung subtipe (`Artifact.ArtifactSubtype`).

1. Buka dokumen PDF (lihat [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)).
1. Filter artefak paginasi menggunakan koleksi [`Artifacts`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) halaman.
1. Hitung artefak berdasarkan subtipe (`Artifact.ArtifactSubtype`).
1. Cetak hasil.

```python

import aspose.pdf as ap

def count_pagination_artifacts(path_infile):
    # Open the PDF document
    with ap.Document(path_infile) as document:
        
        # Extract pagination artifacts from the first page
        pagination_artifacts = [
            artifact for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
        ]

        # Count artifacts by subtype
        watermarks = sum(1 for artifact in pagination_artifacts 
                         if artifact.subtype == ap.Artifact.ArtifactSubtype.WATERMARK)
        backgrounds = sum(1 for artifact in pagination_artifacts 
                          if artifact.subtype == ap.Artifact.ArtifactSubtype.BACKGROUND)
        headers = sum(1 for artifact in pagination_artifacts 
                      if artifact.subtype == ap.Artifact.ArtifactSubtype.HEADER)
        footers = sum(1 for artifact in pagination_artifacts 
                      if artifact.subtype == ap.Artifact.ArtifactSubtype.FOOTER)

        # Display results
        print(f"Watermarks: {watermarks}")
        print(f"Backgrounds: {backgrounds}")
        print(f"Headers: {headers}")
        print(f"Footers: {footers}")
```

