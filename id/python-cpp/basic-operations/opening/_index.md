---
title: Buka dokumen PDF secara terprogram
linktitle: Buka PDF
type: docs
weight: 20
url: id/python-cpp/open-pdf-document/
description: Pelajari cara membuka file PDF di Python Aspose.PDF untuk Python melalui pustaka C++. Anda dapat membuka PDF yang ada, dokumen dari stream, dan dokumen PDF terenkripsi.
lastmod: "2022-12-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Buka dokumen PDF yang ada

Ada beberapa cara untuk membuka dokumen. Cara termudah adalah dengan menentukan nama file.

```python

    import AsposePDFPythonWrappers sebagai ap
    # Buka dokumen
    document = ap.Document("sample.pdf")
    count = document.pages.count()
    print("Halaman: " + str(count))
```

## Buka dokumen PDF terenkripsi

```python

    import AsposePDFPythonWrappers sebagai ap
    # Buka dokumen
    document = ap.Document("sample.pdf","password")
    count = document.pages.count()
    print("Halaman: " + str(count))
```