---
title: Cara Menggabungkan PDF menggunakan Python melalui C++
linktitle: Gabungkan file PDF
type: docs
weight: 10
url: id/python-cpp/merge-pdf-documents/
keywords: "gabungkan beberapa pdf menjadi satu pdf python, gabungkan beberapa pdf menjadi satu python, gabungkan beberapa pdf menjadi satu python"
description: Halaman ini menjelaskan cara menggabungkan dokumen PDF menjadi satu file PDF dengan Python.
lastmod: "2024-04-14"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Gabungkan atau kombinasikan beberapa PDF menjadi satu PDF dalam Python melalui C++

Dengan memanfaatkan Python dan pustaka C++ dari Aspose, Anda dapat dengan efisien menggabungkan beberapa file PDF menjadi satu PDF dengan mudah.

Untuk menggabungkan dua file PDF:

1. Buka dokumen pertama
1. Kemudian tambahkan halaman dari dokumen kedua ke yang pertama
1. Simpan file output yang telah digabungkan dengan metode 'document.save'.

Cuplikan kode berikut menunjukkan cara menggabungkan file PDF.

```python

    import AsposePDFPythonWrappers as apw
    import AsposePDFPython as apCore
    import os
    import os.path

    dataDir = os.path.join(os.getcwd(), "samples")
    input_file= os.path.join(dataDir , "sample0.pdf")
    output_file = os.path.join(dataDir , "results", "concatenated-files.pdf")

    # Buka dokumen pertama
    document1 = apw.Document(inputFile)
    document2 = apw.Document(inputFile)

    # Tambahkan halaman dari dokumen kedua ke yang pertama
    document1.pages.add(document2.pages)

    # Simpan file output yang telah digabungkan
    document1.save(output_file)
```