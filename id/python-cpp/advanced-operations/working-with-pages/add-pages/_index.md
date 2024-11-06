---
title: Tambahkan Halaman di PDF dengan Python via C++
linktitle: Tambahkan Halaman
type: docs
weight: 10
url: id/python-cpp/add-pages/
description: Artikel ini mengajarkan cara menyisipkan (menambahkan) halaman pada lokasi yang diinginkan di file PDF menggunakan Python dengan C++.
lastmod: "2024-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Sisipkan Halaman Kosong di File PDF pada Lokasi yang Diinginkan

Cuplikan kode membuka dokumen PDF, menambahkan halaman kosong padanya, dan menyimpan dokumen yang dimodifikasi sebagai file PDF baru.

Untuk menyisipkan halaman kosong di file PDF:

1. Buka dokumen PDF
1. Tambahkan halaman kosong baru ke dokumen
1. Simpan dokumen yang dimodifikasi ke file output dengan metode 'document.save'

Cuplikan kode berikut menunjukkan cara menyisipkan halaman di file PDF:

```python

    import AsposePDFPythonWrappers as apw
    import AsposePDFPython as apCore
    import os
    import os.path

    # Atur path direktori tempat file PDF sampel berada
    dataDir = os.path.join(os.getcwd(), "samples")

    # Atur path file input
    input_file = os.path.join(dataDir, "sample0.pdf")

    # Atur path file output
    output_file = os.path.join(dataDir, "results", "blank_pdf_document.pdf")

    # Buka dokumen PDF
    document = apw.Document(input_file)

    # Tambahkan halaman kosong baru ke dokumen
    document.pages.add()

    # Simpan dokumen yang dimodifikasi ke file output
    document.save(output_file)
```