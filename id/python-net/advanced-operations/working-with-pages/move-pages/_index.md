---
title: Memindahkan Halaman PDF secara Programatis dengan Python
linktitle: Memindahkan Halaman PDF
type: docs
weight: 100
url: /id/python-net/move-pages/
description: Coba pindahkan halaman ke lokasi yang diinginkan atau ke akhir berkas PDF menggunakan Aspose.PDF untuk Python via .NET.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Memindahkan Halaman antar dokumen PDF menggunakan Python
Abstract: Artikel ini menyediakan panduan komprehensif tentang memindahkan halaman antara dokumen PDF atau dalam satu dokumen PDF menggunakan Python, khususnya memanfaatkan pustaka Aspose.PDF. Ini merinci proses langkah demi langkah untuk tiga skenario - memindahkan satu halaman dari satu PDF ke PDF lain, mentransfer beberapa halaman, dan memindahkan kembali sebuah halaman dalam dokumen yang sama. Setiap skenario melibatkan pembuatan objek kelas `Document` untuk PDF sumber dan tujuan, memanipulasi halaman melalui kelas `PageCollection`, serta menggunakan metode `add`, `delete`, dan `save` untuk mencapai reorganisasi halaman yang diinginkan. Potongan kode disediakan untuk implementasi praktis, menunjukkan cara memindahkan halaman secara efisien menggunakan skrip Python.
---

## Memindahkan Halaman dari satu Dokumen PDF ke Dokumen Lain

Aspose.PDF untuk Python memungkinkan Anda memindahkan sebuah halaman (bukan hanya menyalinnya) dari satu PDF ke PDF lain. Itu menghapus halaman yang dipilih dari dokumen asli dan kemudian menambahkannya ke berkas PDF baru.

Anggap seperti memotong sebuah halaman dari satu buku dan menempelkannya ke buku lain — halaman tersebut tidak lagi ada di berkas asli setelah dipindahkan.

1. Buka dokumen PDF sumber menggunakan kelas [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Pilih halaman tertentu untuk dipindahkan (dalam hal ini, halaman 2) — ini merujuk pada [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Buat dokumen PDF baru (instansiasi [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) lainnya).
1. Tambahkan halaman yang dipilih ke dokumen PDF baru menggunakan [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) dokumen tujuan (misalnya, `another_document.pages.add(page)`).
1. Hapus halaman dari dokumen asli melalui [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)nya (misalnya, `document.pages.delete(index)`).
1. Simpan kedua dokumen.

Potongan kode berikut memperlihatkan cara memindahkan satu halaman.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def moving_page_from_one_document_to_another(input_file_name, output_file_name):
    """
    Move a single page from one PDF document to another.

    Parameters:
    - input_file_name (str): Path to the source PDF file.
    - output_file_name (str): Path to the destination PDF file after moving the page.
    """
    document = ap.Document(input_file_name)
    page = document.pages[2]
    another_document = ap.Document()
    another_document.pages.add(page)
    document.pages.delete(2)
    document.save(input_file_name.replace(".pdf","_new.pdf"))
    another_document.save(output_file_name)
```

## Memindahkan Sekelompok Halaman dari satu Dokumen PDF ke Dokumen Lain

Berbeda dengan menyalin, operasi ini memindahkan halaman yang dipilih — menghapusnya dari berkas sumber dan menyimpannya dalam PDF baru.

1. Buat dokumen tujuan baru yang kosong (`Document`).
1. Pilih beberapa halaman (dalam hal ini, halaman 1 dan 3) dari [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) dokumen sumber.
1. Lakukan perulangan pada halaman yang dipilih dan tambahkan masing-masing ke [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) dokumen tujuan.
1. Simpan dokumen tujuan yang berisi halaman yang dipindahkan.
1. Hapus halaman yang dipindahkan dari dokumen sumber menggunakan [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)nya.
1. Simpan dokumen sumber yang telah dimodifikasi dengan nama berkas baru untuk mempertahankan kedua versi.

Potongan kode berikut memperlihatkan cara menyisipkan halaman kosong di akhir berkas PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def moving_bunch_pages_from_one_document_to_another(input_file_name, output_file_name):
    """
    Move a set of pages from one PDF document to another.

    Parameters:
    - input_file_name (str): Path to the source PDF file.
    - output_file_name (str): Path to the destination PDF file where selected pages will be saved.
    """
    src_document = ap.Document(input_file_name)
    dst_document = ap.Document()
    pages = [1, 3]
    for page_index in pages:
        page = src_document.pages[page_index]
        dst_document.pages.add(page)
    # Save output files
    dst_document.save(output_file_name)
    src_document.pages.delete(pages)
    src_document.save(input_file_name.replace(".pdf","_new.pdf"))
```

## Memindahkan Halaman ke Lokasi Baru dalam Dokumen PDF Saat Ini

Ini menunjukkan cara memindahkan halaman tertentu ke posisi berbeda dalam dokumen yang sama — kebutuhan umum saat merestrukturisasi atau mengedit tata letak PDF.

1. Muat dokumen PDF input menggunakan kelas [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Pilih halaman yang ingin dipindahkan (halaman 2) — ini adalah sebuah [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Tambahkan ke akhir dokumen menggunakan [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) dokumen.
1. Hapus halaman asli dari lokasi sebelumnya melalui [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Simpan dokumen yang telah dimodifikasi sebagai berkas baru.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def moving_page_in_new_location_in_same_document(input_file_name, output_file_name):
    """
    Move a page to a new location within the same PDF document.

    Parameters:
    - input_file_name (str): Path to the source PDF file.
    - output_file_name (str): Path to the destination PDF file after moving the page.
    """
    srcDocument = ap.Document(input_file_name)

    page = srcDocument.pages[2]
    srcDocument.pages.add(page)
    srcDocument.pages.delete(2)

    # Save output file
    srcDocument.save(output_file_name)
```


