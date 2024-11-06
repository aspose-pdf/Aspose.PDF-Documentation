---
title: Buka dokumen PDF secara programatis
linktitle: Buka PDF
type: docs
weight: 20
url: id/python-net/open-pdf-document/
description: Pelajari cara membuka file PDF di Python Aspose.PDF untuk pustaka Python via .NET. Anda dapat membuka PDF yang sudah ada, dokumen dari stream, dan dokumen PDF terenkripsi.
lastmod: "2022-12-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Buka dokumen PDF yang sudah ada

Ada beberapa cara untuk membuka dokumen. Cara termudah adalah dengan menentukan nama file.

```python

    import aspose.pdf as ap

    # Buka dokumen
    document = ap.Document(input_pdf)
    print("Halaman: " + str(len(document.pages)))
```

## Buka dokumen PDF yang sudah ada dari stream

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    stream = io.FileIO(input_pdf, 'r')
    # Buka dokumen
    document = ap.Document(stream)
    print("Halaman: " + str(len(document.pages)))
```

## Buka dokumen PDF terenkripsi

```python

    import aspose.pdf as ap

    # Buka dokumen
    document = ap.Document(input_pdf, password)
    print("Halaman: " + str(len(document.pages)))
```