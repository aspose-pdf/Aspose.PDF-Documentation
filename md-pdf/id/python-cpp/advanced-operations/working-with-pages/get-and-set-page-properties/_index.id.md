---
title: Setel Ukuran PDF menggunakan python via C++
linktitle: Setel Ukuran PDF
type: docs
weight: 30
url: /python-cpp/get-and-set-page-properties/
description: Bagian ini menunjukkan cara mendapatkan atau menyetel properti halaman PDF seperti ukuran dokumen menggunakan Python via C++.
lastmod: "2024-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Setel Ukuran file PDF

Aspose.PDF untuk Python via C++ memungkinkan Anda membaca dan menyetel properti halaman dalam file PDF di aplikasi Python Anda.

Cuplikan kode berikut membuka file PDF, mengubah ukuran halaman pertama dengan menyesuaikan **Kotak Pangkas** (kotak pangkas adalah ukuran "halaman" di mana dokumen PDF Anda ditampilkan di Adobe Acrobat), dan menyimpan dokumen yang dimodifikasi ke file baru.

1. Buat objek dokumen dari file input
1. Dapatkan koleksi halaman dari dokumen menggunakan [document_get_pages](https://reference.aspose.com/pdf/python-cpp/core/document_get_pages/)

1. Dapatkan halaman pertama dari koleksi halaman dengan [page_collection_get_page](https://reference.aspose.com/pdf/python-cpp/core/page_collection_get_page/)
1. Dapatkan kotak pangkas dari halaman menggunakan [page_get_rectangle](https://reference.aspose.com/pdf/python-cpp/core/page_get_rectangle/)
1. Hitung koordinat baru untuk kotak pangkas
1. Perbarui koordinat kotak pangkas dengan nilai baru
1. Simpan dokumen yang telah dimodifikasi ke file keluaran dengan metode 'document.save'

```python

    import AsposePDFPython as apCore
    import os
    import os.path

    # Dapatkan direktori kerja saat ini dan buat jalur ke direktori "samples"
    dataDir = os.path.join(os.getcwd(), "samples")

    # Buat jalur file input dan output
    input_file = os.path.join(dataDir, "sample0.pdf")
    output_file = os.path.join(dataDir, "results", "resized_document.pdf")

    # Buat objek dokumen dari file input
    doc = apCore.document_create_from_file(inputFile)

    # Dapatkan koleksi halaman dari dokumen
    pages = apCore.document_get_pages(doc)

    # Dapatkan halaman pertama dari koleksi halaman
    page = apCore.page_collection_get_page(pages, 1)

    # Dapatkan kotak pangkas dari halaman
    crop_box = apCore.page_get_rectangle(page)

    # Hitung koordinat baru untuk kotak pangkas
    LLX = apCore.rectangle_get_LLX(crop_box) + 10
    LLY = apCore.rectangle_get_LLY(crop_box) + 10
    URX = apCore.rectangle_get_URX(crop_box) - 10
    URY = apCore.rectangle_get_URY(crop_box) - 10

    # Perbarui koordinat kotak pangkas dengan nilai baru
    apCore.rectangle_set_LLX(crop_box, LLX)
    apCore.rectangle_set_LLY(crop_box, LLY)
    apCore.rectangle_set_URX(crop_box, URX)
    apCore.rectangle_set_URY(crop_box, URY)

    # Simpan dokumen yang telah dimodifikasi ke file keluaran
    apCore.document_save(doc, output_file)

    # Tutup handle dokumen
    apCore.close_handle(doc)
```