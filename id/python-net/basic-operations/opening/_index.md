---
title: Membuka dokumen PDF secara programatik
linktitle: Buka PDF
type: docs
weight: 20
url: /id/python-net/open-pdf-document/
description: Pelajari cara membuka file PDF di Python Aspose.PDF untuk Python via .NET library. Anda dapat membuka PDF yang sudah ada, dokumen dari stream, dan dokumen PDF terenkripsi.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Membuka dokumen PDF menggunakan library Aspose.PDF di Python
Abstract: Artikel ini memberikan panduan tentang membuka dokumen PDF yang sudah ada menggunakan library Aspose.PDF di Python. Artikel ini menjelaskan tiga metode untuk melakukannya - membuka PDF dengan menyebutkan nama file, membuka PDF dari stream, dan membuka PDF terenkripsi dengan menyediakan kata sandi. Setiap metode menyertakan potongan kode yang memperlihatkan cara menggunakan library Aspose.PDF untuk mengakses PDF dan mencetak jumlah halaman yang dimilikinya. Contoh-contoh ini menggambarkan fleksibilitas dan fungsionalitas Aspose.PDF dalam menangani berbagai skenario akses file PDF.
---

## Membuka dokumen PDF yang ada

Ada beberapa cara untuk membuka dokumen. Yang paling mudah adalah dengan menyebutkan nama file.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    print("Pages: " + str(len(document.pages)))
```

## Membuka dokumen PDF yang ada dari stream

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    stream = io.FileIO(input_pdf, 'r')
    # Open document
    document = ap.Document(stream)
    print("Pages: " + str(len(document.pages)))
```

## Membuka dokumen PDF terenkripsi

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf, password)
    print("Pages: " + str(len(document.pages)))
```

