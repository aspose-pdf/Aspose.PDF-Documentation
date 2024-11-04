---
title: Membagi PDF secara programatis dalam Python
linktitle: Membagi file PDF
type: docs
weight: 20
url: /python-cpp/split-pdf-document/
keywords: membagi pdf menjadi beberapa file, membagi pdf menjadi pdf terpisah, membagi pdf python
description: Topik ini menunjukkan cara membagi halaman PDF menjadi file PDF individual dalam aplikasi Python melalui C++ Anda.
lastmod: "2024-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Membagi halaman PDF dapat menjadi fitur yang berguna bagi mereka yang ingin memisahkan file besar menjadi halaman-halaman terpisah atau kelompok halaman.

## Contoh Langsung

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) adalah aplikasi web gratis online yang memungkinkan Anda untuk menyelidiki bagaimana fungsi pemisahan presentasi bekerja.

[![Aspose Split PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

Topik ini menunjukkan cara membagi halaman PDF menjadi file PDF individual dalam aplikasi Python C++ Anda. Untuk membagi halaman PDF menjadi file PDF satu halaman menggunakan Python, langkah-langkah berikut dapat diikuti:

Potongan kode mengatur direktori dan jalur file yang diperlukan, membuka dokumen PDF, dan kemudian mengulangi setiap halaman dari dokumen.
 Untuk setiap halaman, ini membuat dokumen baru, menyalin halaman saat ini ke dokumen baru, dan menyimpan dokumen baru sebagai file PDF terpisah dengan konvensi penamaan tertentu.

1. Buka dokumen input
1. Inisialisasi jumlah halaman
1. Loop melalui semua halaman dokumen

## Memisahkan PDF menjadi beberapa file atau PDF terpisah dalam Python

Cuplikan kode Python berikut menunjukkan cara memisahkan halaman PDF menjadi file PDF individual.

```python

    import AsposePDFPythonWrappers as apw
    import AsposePDFPython as apCore
    import os
    import os.path

    dataDir = os.path.join(os.getcwd(), "samples")
    input_file= os.path.join(dataDir , "sample.pdf")
    outputFolder = os.path.join(dataDir , "results")
    # Buka dokumen
    document = apw.Document(inputFile)

    pageCount = 1

    # Loop melalui semua halaman

    while (pageCount <= document.pages.count()):
        page = document.pages[pageCount]    
        newDocument = apw.Document()
        newDocument.pages.copy_page(page)
        newDocument.save(os.path.join(outputFolder,"page_" + str(pageCount) + "_out" + ".pdf"))
        pageCount += 1
```