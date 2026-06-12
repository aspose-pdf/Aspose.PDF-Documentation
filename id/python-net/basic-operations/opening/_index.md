---
title: Buka dokumen PDF secara programatik
linktitle: Buka PDF
type: docs
weight: 20
url: /id/python-net/open-pdf-document/
description: Pelajari cara membuka file PDF di Python menggunakan pustaka Aspose.PDF for Python via .NET. Anda dapat membuka PDF yang sudah ada, dokumen dari aliran, dan dokumen PDF yang terenkripsi.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Membuka dokumen PDF menggunakan pustaka Aspose.PDF di Python
Abstract: Artikel ini memberikan panduan tentang membuka dokumen PDF yang ada menggunakan perpustakaan Aspose.PDF dalam Python. Ini menjelaskan tiga metode untuk mencapai hal ini - membuka PDF dengan menentukan nama file, membuka PDF dari stream, dan membuka PDF terenkripsi dengan menyediakan kata sandi. Setiap metode menyertakan potongan kode yang menunjukkan cara memanfaatkan perpustakaan Aspose.PDF untuk mengakses PDF dan mencetak jumlah halaman yang dimilikinya. Contoh-contoh ini menggambarkan fleksibilitas dan fungsionalitas Aspose.PDF untuk menangani berbagai skenario akses file PDF.
---

## Buka dokumen PDF yang ada

Ada beberapa cara untuk membuka dokumen. Yang paling mudah adalah dengan menentukan nama file.

```python
import aspose.pdf as ap

def open_document_from_file(infile):

    # Open document
    document = ap.Document(infile)
    print("Pages: " + str(len(document.pages)))
```

## Buka dokumen PDF yang sudah ada dari aliran

```python
import aspose.pdf as ap
import io

def open_document_from_stream(infile):
    with io.FileIO(infile, "r") as stream:
        # Open document
        document = ap.Document(stream)
        print("Pages: " + str(len(document.pages)))
```

## Buka dokumen PDF terenkripsi

```python
import aspose.pdf as ap

def open_document_encrypted(infile):
    password = "P@ssw0rd"
    # Open document
    document = ap.Document(infile, password)
    print("Pages: " + str(len(document.pages)))
```
