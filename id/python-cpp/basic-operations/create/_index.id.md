---
title: Membuat Dokumen PDF
linktitle: Membuat PDF
type: docs
weight: 10
url: /python-cpp/create-document/
description: Halaman ini menjelaskan cara membuat dokumen PDF dari awal menggunakan Aspose.PDF untuk Python melalui pustaka C++.
---

Bagi pengembang, ada banyak skenario di mana menjadi perlu untuk secara programatis menghasilkan file PDF. Anda mungkin perlu secara programatis menghasilkan laporan PDF dan file PDF lainnya dalam perangkat lunak Anda. Sangat panjang dan tidak efisien untuk menulis kode dan fungsi Anda sendiri dari awal. Untuk membuat file PDF dengan Python, ada solusi yang lebih baik - **Aspose.PDF untuk Python melalui C++**.

## Membuat File PDF menggunakan Python

Untuk membuat file PDF menggunakan Python, langkah-langkah berikut dapat digunakan.

* impor semua kelas dan metode dari pustaka Aspose.PDF untuk Python melalui C++.
* Buat objek Dokumen baru yang mewakili dokumen PDF kosong menggunakan [document_create](https://reference.aspose.com/pdf/python-cpp/core/document_create/)

* Dapatkan objek [document_get_pages](https://reference.aspose.com/pdf/python-cpp/core/document_get_pages/) yang berisi semua halaman dalam dokumen.
* Tambahkan halaman baru ke akhir koleksi halaman [page_collection_add_page](https://reference.aspose.com/pdf/python-cpp/core/page_collection_add_page/) dan mengembalikan objek Halaman yang mewakili halaman yang ditambahkan.
* Simpan dokumen ke file dengan nama yang ditentukan di direktori kerja saat ini.
* Menutup pegangan ke dokumen dan melepaskan sumber daya apa pun yang terkait dengannya.

```python

    from AsposePDFPython import *

    doc = document_create()
    pages = document_get_pages(doc)
    page = page_collection_add_page(pages)
    document_save(doc, "blank_pdf_document.pdf")
    close_handle(doc)
```


## Membuat File PDF berdasarkan DOM

```python

    from AsposePDFPythonWrappers import *

    doc = Document()
    page = doc.pages.add()
    doc.save("blank_pdf_document1.pdf")
```