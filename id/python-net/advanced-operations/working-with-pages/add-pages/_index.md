---
title: Menambahkan Halaman dalam PDF dengan Python
linktitle: Menambahkan Halaman
type: docs
weight: 10
url: /id/python-net/add-pages/
description: Temukan cara menambahkan halaman ke dokumen PDF dalam Python menggunakan Aspose.PDF untuk pembuatan dan pengeditan dokumen yang fleksibel.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara menambahkan Halaman dalam PDF menggunakan Python
Abstract: Artikel ini menyediakan panduan tentang penggunaan Aspose.PDF untuk Python via .NET API untuk memanipulasi halaman dalam dokumen PDF. Artikel ini menekankan fleksibilitas yang ditawarkan oleh API, terutama melalui kelas `PageCollection`, yang mengelola semua halaman dalam sebuah PDF. Dokumen ini merinci prosedur untuk menambahkan atau menyisipkan halaman pada lokasi tertentu dalam file PDF. Dijelaskan dua operasi utama - menyisipkan halaman kosong pada lokasi yang diinginkan dalam dokumen dan menambahkan halaman kosong di akhir dokumen. Untuk kedua operasi, proses melibatkan pembuatan objek `Document`, menggunakan metode `insert` atau `add` dari `PageCollection`, dan menyimpan dokumen yang dimodifikasi. Artikel ini menyertakan cuplikan kode yang menunjukkan tugas-tugas ini, memperlihatkan betapa mudahnya memanipulasi dokumen PDF menggunakan Python dengan API ini.
---

Aspose.PDF untuk Python via .NET API menyediakan fleksibilitas penuh untuk bekerja dengan halaman dalam dokumen PDF menggunakan Python. API ini menyimpan semua halaman dokumen PDF dalam [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) yang dapat digunakan untuk bekerja dengan halaman PDF.
Aspose.PDF untuk Python via .NET memungkinkan Anda menyisipkan halaman ke sebuah [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) di lokasi manapun dalam file serta menambahkan halaman ke akhir file PDF. Bagian ini menunjukkan cara menambahkan halaman ke PDF menggunakan Python.

## Menambahkan atau Menyisipkan Halaman dalam File PDF

Aspose.PDF untuk Python via .NET memungkinkan Anda menyisipkan halaman ke sebuah [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) di lokasi manapun dalam file serta menambahkan halaman ke akhir file PDF.

### Menyisipkan Halaman Kosong dalam File PDF

Untuk menyisipkan halaman kosong dalam file PDF:

1. Buka sebuah [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) yang ada menggunakan metode yang tepat.
1. Sisipkan halaman kosong baru pada indeks tertentu menggunakan metode `insert()` pada [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Simpan [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) yang telah dimodifikasi ke jalur output yang diinginkan.

Sisipkan halaman kosong ke dalam file PDF yang ada pada posisi yang ditentukan:

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def insert_empty_page(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    document.pages.insert(2)
    document.save(output_file_name)
```

### Menambahkan Halaman Kosong di Akhir File PDF

Terkadang, Anda ingin memastikan bahwa dokumen berakhir pada halaman kosong. Topik ini menjelaskan cara menyisipkan halaman kosong di akhir dokumen PDF.

Untuk menyisipkan halaman kosong di akhir file PDF:

1. Buka sebuah [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) yang ada menggunakan metode yang tepat.
1. Tambahkan halaman kosong baru ke akhir dokumen menggunakan metode `add()` pada [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Simpan [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) yang telah diperbarui.

Cuplikan kode berikut menunjukkan cara menyisipkan halaman kosong di akhir file PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_empty_page_to_end(input_file_name, output_file_name):
    # Open document
    document = ap.Document(input_file_name)

    # Insert an empty page at the end of a PDF file
    document.pages.add()

    # Save output file
    document.save(output_file_name)
```

### Menambahkan Halaman dari Dokumen PDF Lain

Dengan pustaka Aspose.PDF untuk Python, Anda membuat sebuah [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) baru, menambahkan halaman awal, dan kemudian mengimpor halaman dari PDF lain ke dalamnya.

1. Buat sebuah [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) baru.
1. Tambahkan sebuah [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) kosong baru dan tuliskan beberapa teks di atasnya menggunakan [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/).
1. Buka sebuah [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) lain yang ada.
1. Salin sebuah [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) dari dokumen tersebut.
1. Tempelkan halaman yang disalin ke dokumen utama Anda menggunakan [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Simpan file yang digabungkan.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_page_from_another_document(input_file_name, output_file_name):
    # Open document
    document = ap.Document()
    page = document.pages.add()
    text_fragment = ap.text.TextFragment("This is first page!")
    page.paragraphs.add(text_fragment)

    another_document = ap.Document(input_file_name)
    document.pages.add(another_document.pages[1])

    # Save output file
    document.save(output_file_name)
```
