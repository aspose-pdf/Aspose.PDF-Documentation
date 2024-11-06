---
title: Memutar Halaman PDF Menggunakan Python via C++
linktitle: Memutar Halaman PDF
type: docs
weight: 20
url: id/python-cpp/rotate-pages/
description: Topik ini menjelaskan cara memutar orientasi halaman dalam file PDF yang ada secara programatik dengan Python via C++.
lastmod: "2024-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Terkadang, halaman PDF mungkin memiliki orientasi yang salah karena masalah pemindaian atau pembuatan. Memutar halaman memastikan bahwa mereka ditampilkan dalam orientasi yang benar untuk memudahkan membaca dan melihat.
Memutar halaman PDF membantu menjaga pengalaman melihat yang konsisten di berbagai perangkat dan platform.

Memutar halaman PDF dapat memudahkan tugas pengeditan seperti menambahkan anotasi, komentar, atau tanda tangan. Dengan memutar halaman ke orientasi yang diinginkan, Anda dapat membuat proses pengeditan dan peninjauan lebih efisien.

Selain itu, saat mencetak dokumen PDF, penting untuk memastikan bahwa halaman berorientasi dengan benar untuk menghindari masalah penyelarasan atau pemotongan.
 Memutar halaman sesuai kebutuhan sebelum mencetak membantu mengoptimalkan output pencetakan dan memastikan bahwa konten ditampilkan sebagaimana yang diinginkan. Memutar halaman PDF adalah fitur berguna yang membantu meningkatkan keterbacaan, konsistensi, dan presentasi dokumen di berbagai konteks dan tujuan.

Topik ini menjelaskan cara memperbarui atau mengubah orientasi halaman dari halaman dalam file PDF yang sudah ada secara programatis dengan Python.

## Ubah Orientasi Halaman

Aspose.PDF untuk Python melalui dukungan C++ memiliki fitur hebat seperti mengubah orientasi halaman

1. Buat objek dokumen dari file input
1. Dapatkan koleksi halaman dari dokumen menggunakan 'apCore.document_get_pages'
1. Dapatkan halaman pertama dari koleksi halaman dengan 'apCore.page_collection_get_page'
1. Memutar halaman sebesar 90 derajat searah jarum jam menggunakan 'apCore.page_set_rotate'
1. Simpan dokumen yang telah dimodifikasi ke file output dengan metode 'document.save'

```python

    import AsposePDFPython as apCore
    import os
    import os.path

    # Membuat jalur ke direktori yang berisi file sampel
    dataDir = os.path.join(os.getcwd(), "samples")

    # Membuat jalur ke file input dan output
    input_file = os.path.join(dataDir, "sample0.pdf")
    output_file = os.path.join(dataDir, "results", "rotated_document.pdf")

    # Membuat objek dokumen dengan memuat file input
    doc = apCore.document_create_from_file(inputFile)

    # Mendapatkan koleksi halaman dalam dokumen
    pages = apCore.document_get_pages(doc)

    # Mendapatkan halaman pertama dari koleksi
    page = apCore.page_collection_get_page(pages, 1)

    # Memutar halaman sebesar 90 derajat searah jarum jam
    apCore.page_set_rotate(page, apCore.Rotation(apCore.on90))

    # Menyimpan dokumen yang telah dimodifikasi ke file output
    apCore.document_save(doc, output_file)

    # Menutup handle dokumen untuk melepaskan sumber daya
    apCore.close_handle(doc)
```