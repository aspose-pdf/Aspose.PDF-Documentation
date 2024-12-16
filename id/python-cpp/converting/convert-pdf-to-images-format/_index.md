---
title: Mengubah PDF ke Berbagai Format Gambar di Python
linktitle: Mengubah PDF ke Gambar
type: docs
weight: 70
url: /id/python-cpp/convert-pdf-to-images-format/
lastmod: "2023-06-23"
description: Topik ini menunjukkan kepada Anda bagaimana menggunakan Aspose.PDF untuk Python untuk mengubah PDF ke berbagai format gambar seperti TIFF, BMP, EMF, JPEG, PNG, GIF, SVG dengan beberapa baris kode.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Ikhtisar

Artikel ini menjelaskan cara mengubah PDF ke berbagai format gambar menggunakan Python. Ini mencakup topik-topik berikut.

## Python Mengubah PDF ke Gambar

### Python Mengubah PDF ke PNG

1. Impor modul AsposePdfPython, yang menyediakan pembungkus Python untuk pustaka Aspose.PDF.
2. Buka dokumen PDF menggunakan fungsi `document_open`, yang mengambil nama file sebagai argumen dan mengembalikan objek Dokumen.
3. Dapatkan halaman-halaman dokumen menggunakan fungsi `document_get_pages`, yang mengambil objek Dokumen sebagai argumen dan mengembalikan objek PageCollection.

1. Dapatkan halaman yang diinginkan dari dokumen menggunakan fungsi `page_collection_get_page`, yang mengambil objek PageCollection dan indeks sebagai argumen dan mengembalikan objek Page.
1. Buat objek PngDevice menggunakan fungsi `png_device_create`, yang tidak memerlukan argumen. Objek ini dapat mengonversi halaman PDF menjadi gambar PNG dengan parameter default.
1. Simpan halaman yang diinginkan dari dokumen sebagai gambar PNG menggunakan fungsi `png_device_save_page_to_file`, yang mengambil objek PngDevice, objek Page dan nama file sebagai argumen.
1. Tutup handle dari objek PngDevice dan Document menggunakan fungsi `close_handle`, yang mengambil objek sebagai argumen dan melepaskan sumber dayanya.

```python

from AsposePdfPython import *

doc = document_open("blank_pdf_document.pdf")
pages = document_get_pages(doc)
page = page_collection_get_page(pages,1)

pngDevice = png_device_create()
png_device_save_page_to_file(pngDevice,page,"test.png")

```

### Python Mengonversi PDF ke JPEG

1. Buka dokumen PDF menggunakan fungsi `document_open`, yang mengambil nama file sebagai argumen dan mengembalikan objek Document.
1. Dapatkan halaman dokumen menggunakan fungsi `document_get_pages`, yang mengambil objek Document sebagai argumen dan mengembalikan objek PageCollection.
1. Dapatkan halaman yang diinginkan dari dokumen menggunakan fungsi `page_collection_get_page`, yang mengambil objek PageCollection dan indeks sebagai argumen dan mengembalikan objek Page.
1. Buat objek Resolution menggunakan fungsi `resolution_create`, yang mengambil nilai resolusi dalam dot per inci (DPI) sebagai argumen.
1. Buat objek JpegDevice menggunakan fungsi `jpeg_device_create_from_width_height_resolution`, yang mengambil nilai lebar, tinggi dan resolusi sebagai argumen. Objek ini dapat mengonversi halaman PDF ke gambar JPEG dengan parameter yang ditentukan.

1. Simpan halaman yang diinginkan dari dokumen sebagai gambar JPEG menggunakan fungsi `jpeg_device_save_page_to_file`, yang membutuhkan objek JpegDevice, objek Page, dan nama file sebagai argumen.
1. Tutup handle dari objek JpegDevice dan Document menggunakan fungsi `close_handle`, yang membutuhkan sebuah objek sebagai argumen dan melepaskan sumber dayanya.

```python

    from AsposePdfPython import *

    doc = document_open("blank_pdf_document.pdf")
    pages = document_get_pages(doc)
    page = page_collection_get_page(pages,1)

    res = resolution_create(300)
    jpegDevice = jpeg_device_create_from_width_height_resolution(1239,1754,res)
    jpeg_device_save_page_to_file(jpegDevice,page,"test.jpeg")
```