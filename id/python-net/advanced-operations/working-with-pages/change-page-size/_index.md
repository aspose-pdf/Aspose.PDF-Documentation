---
title: Mengubah Ukuran Halaman dengan Python
linktitle: Mengubah Ukuran Halaman
type: docs
weight: 40
url: /id/python-net/change-page-size/
description: Ubah Ukuran Halaman dari dokumen PDF Anda menggunakan Aspose.PDF untuk Python via .NET library.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Mengubah Ukuran Halaman menggunakan Python
Abstract: Artikel ini menunjukkan cara membaca dan memodifikasi dimensi halaman PDF menggunakan Aspose.PDF. Contoh Get Page Size mengambil lebar dan tinggi dari halaman PDF tertentu, memungkinkan pengguna untuk memeriksa tata letak halaman, memvalidasi format, atau menganalisis struktur dokumen. Contoh Set Page Size menunjukkan cara mengubah dimensi halaman—seperti mengonversi halaman pertama ke ukuran A4—sementara juga menampilkan properti kotak (CropBox, TrimBox, ArtBox, BleedBox, MediaBox) sebelum dan sesudah modifikasi.
---

Aspose.PDF untuk Python via .NET memungkinkan Anda mengubah ukuran halaman PDF dengan baris kode sederhana. Topik ini menunjukkan cara memperbarui dimensi halaman menggunakan API [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) dan [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).

{{% alert color="primary" %}}

Harap perhatikan bahwa properti tinggi dan lebar menggunakan poin sebagai satuan dasar, di mana 1 inci = 72 poin dan 1 cm = 1/2,54 inci = 0,3937 inci = 28,3 poin.

{{% /alert %}}

### Atur Ukuran Halaman PDF ke A4

Contoh ini memperbarui ukuran halaman pertama dalam dokumen PDF ke dimensi standar A4. Ini juga mencetak dimensi kotak halaman (CropBox, TrimBox, ArtBox, BleedBox, MediaBox) sebelum dan sesudah mengubah ukuran sehingga Anda dapat memverifikasi perubahan.

Potongan kode berikut menunjukkan cara mengubah dimensi halaman PDF ke ukuran A4:

1. Akses [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) pertama dari [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Tampilkan ukuran kotak halaman sebelum modifikasi (CropBox, TrimBox, ArtBox, BleedBox, MediaBox).
1. Terapkan dimensi A4 (597.6 × 842.4 poin) menggunakan API halaman.
1. Tampilkan ukuran kotak halaman yang telah diperbarui.
1. Simpan [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) yang telah dimodifikasi ke jalur output yang ditentukan.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def set_page_size(input_file_name, output_file_name):
    """
    Set the size of the first page in the PDF document to A4 and save the updated document.

    Parameters:
    - input_file_name (str): Path to the input PDF file.
    - output_file_name (str): Path to save the output PDF file.
    """
    # Open the PDF document using the Document class
    document = ap.Document(input_file_name)
    # Get particular page (Page API)
    page = document.pages[1]

    # Set the page size as A4 (8.3 x 11.7 in). In Aspose.PDF 1 inch = 72 points.
    # A4 dimensions in points are (597.6, 842.4) for portrait orientation
    print("Before set")
    print(f"CropBox: {page.crop_box.width} x {page.crop_box.height}")
    print(f"TrimBox: {page.trim_box.width} x {page.trim_box.height}")
    print(f"ArtBox: {page.art_box.width} x {page.art_box.height}")
    print(f"BleedBox: {page.bleed_box.width} x {page.bleed_box.height}")
    print(f"MediaBox: {page.media_box.width} x {page.media_box.height}")

    # Use the Page API to set page size
    page.set_page_size(597.6, 842.4)
    print("After set")
    print(f"CropBox: {page.crop_box.width} x {page.crop_box.height}")
    print(f"TrimBox: {page.trim_box.width} x {page.trim_box.height}")
    print(f"ArtBox: {page.art_box.width} x {page.art_box.height}")
    print(f"BleedBox: {page.bleed_box.width} x {page.bleed_box.height}")
    print(f"MediaBox: {page.media_box.width} x {page.media_box.height}")

    # Save the updated document
    document.save(output_file_name)
```

## Dapatkan Ukuran Halaman PDF

Potongan kode ini membaca sebuah PDF dan mengambil dimensi (lebar dan tinggi) halaman pertama. Ini menggunakan API [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) untuk mengekstrak [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) pembatas halaman dan mencetak ukurannya ke konsol. Ini berguna untuk memeriksa tata letak halaman, memverifikasi format, atau menyiapkan dokumen untuk pemrosesan lebih lanjut.

1. Muat PDF sebagai [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Akses [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) pertama.
1. Ambil persegi panjang pembatas halaman menggunakan `get_page_rect()`.
1. Ekstrak nilai lebar dan tinggi.
1. Cetak dimensi halaman.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_size(input_file_name, output_file_name):
    # Open document (Document API)
    document = ap.Document(input_file_name)

    # Get particular page (Page API)
    page = document.pages[1]
    rectangle = page.get_page_rect(True)
    print(f"{rectangle.width} : {rectangle.height}")
```

### Dapatkan Ukuran Halaman PDF Sebelum dan Sesudah Rotasi

Ambil dimensi halaman PDF sebelum dan sesudah menerapkan rotasi 90°. Ini menunjukkan bagaimana rotasi memengaruhi lebar dan tinggi serta cara menggunakan `get_page_rect()` dengan atau tanpa mempertimbangkan rotasi.

1. Buka PDF sebagai [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Akses [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) pertama.
1. Terapkan rotasi 90° menggunakan `page.rotate = ap.Rotation.ON90` (lihat enum [`Rotation`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rotation/)).
1. Ambil persegi panjang halaman tanpa rotasi menggunakan `get_page_rect(False)` dan cetak lebar serta tingginya.
1. Ambil persegi panjang halaman dengan mempertimbangkan rotasi menggunakan `get_page_rect(True)` dan cetak lebar serta tingginya.
1. Bandingkan bagaimana dimensi berubah akibat rotasi.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_size_rotation(input_file_name, output_file_name):
    # Open document (Document API)
    document = ap.Document(input_file_name)
    # Get particular page (Page API)
    page = document.pages[1]
    # Apply rotation using Rotation enum
    page.rotate = ap.Rotation.ON90
    rectangle = page.get_page_rect(False)
    print(f"{rectangle.width} : {rectangle.height}")
    rectangle = page.get_page_rect(True)
    print(f"{rectangle.width} : {rectangle.height}")
```
