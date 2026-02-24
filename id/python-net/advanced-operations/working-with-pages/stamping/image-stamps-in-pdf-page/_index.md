---
title: Menambahkan Cap Gambar dalam PDF menggunakan Python
linktitle: Cap gambar dalam File PDF
type: docs
weight: 10
url: /id/python-net/image-stamps-in-pdf-page/
description: Tambahkan Cap Gambar dalam dokumen PDF Anda menggunakan kelas ImageStamp dengan pustaka Aspose.PDF untuk Python.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara menambahkan Cap Gambar dalam PDF menggunakan Python
Abstract: Artikel ini menyediakan panduan lengkap tentang menambahkan cap gambar ke file PDF menggunakan pustaka Aspose.PDF untuk Python. Artikel ini menjelaskan penggunaan kelas `ImageStamp`, yang memungkinkan kostumisasi cap berbasis gambar termasuk properti seperti tinggi, lebar, opasitas, dan rotasi. Prosesnya melibatkan pembuatan objek `Document` dan objek `ImageStamp` dengan properti yang diinginkan, kemudian menambahkan cap ke halaman tertentu dari PDF menggunakan metode `add_stamp()`. Artikel ini menyertakan contoh kode Python yang menunjukkan cara menerapkan cap gambar ke PDF dan mengontrol kualitasnya menggunakan properti `quality`, yang mengatur kualitas gambar dalam persentase. Selain itu, artikel ini menjelaskan cara menggunakan cap gambar sebagai latar belakang dalam kotak mengambang dengan kelas `FloatingBox`, menyediakan contoh kode lain untuk menunjukkan bagaimana hal ini dapat diimplementasikan. Panduan ini menjadi sumber daya yang berguna bagi pengembang yang ingin meningkatkan PDF dengan cap gambar menggunakan Aspose.PDF.
---

## Menambahkan Cap Gambar dalam File PDF

Anda dapat menggunakan kelas [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) untuk menambahkan cap gambar ke file PDF. Kelas [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) menyediakan properti yang diperlukan untuk membuat cap berbasis gambar, seperti tinggi, lebar, opasitas, dan sebagainya. Cap dapat diposisikan, diubah ukurannya, diputar, dan dibuat sebagian transparan, memungkinkan untuk watermark, branding, atau anotasi.

Potongan kode berikut menunjukkan cara menambahkan cap gambar dalam file PDF.

1. Muat PDF menggunakan 'ap.Document()'.
1. Buat cap gambar dengan 'ImageStamp()'.
1. Konfigurasikan properti cap.
1. Tambahkan cap ke halaman target.
1. Simpan PDF yang telah dimodifikasi.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_image_stamp(infile, input_image_file, outfile):
    document = ap.Document(infile)
    image_stamp = ap.ImageStamp(input_image_file)
    image_stamp.background = True
    image_stamp.x_indent = 100
    image_stamp.y_indent = 100
    image_stamp.height = 300
    image_stamp.width = 300
    image_stamp.rotate = ap.Rotation.ON270
    image_stamp.opacity = 0.5

    document.pages[1].add_stamp(image_stamp)
    document.save(outfile)
```

## Mengontrol Kualitas Gambar saat Menambahkan Cap

Ketika menambahkan gambar sebagai objek cap, Anda dapat mengontrol kualitas gambar. Properti [quality](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/#properties) dari kelas [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) digunakan untuk tujuan ini. Properti ini menunjukkan kualitas gambar dalam persentase (nilai yang valid adalah 0..100).
Dengan mengatur properti kualitas, Anda dapat mengurangi resolusi gambar untuk mengoptimalkan ukuran PDF atau mempertahankan fidelitas lebih tinggi untuk kejelasan.

1. Buka dokumen PDF.
1. Buat cap gambar.
1. Atur kualitas gambar.
1. Tambahkan cap ke halaman target.
1. Simpan PDF yang telah dimodifikasi.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_image_stamp_image_control_image_quality(infile, input_image_file, outfile):
    document = ap.Document(infile)

    image_stamp = ap.ImageStamp(input_image_file)
    image_stamp.quality = 10

    document.pages[1].add_stamp(image_stamp)
    document.save(outfile)
```

## Cap Gambar sebagai Latar Belakang dalam Kotak Mengambang

Buat sebuah [FloatingBox](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/) dalam PDF dan terapkan gambar sebagai latar belakangnya. Ini juga menunjukkan cara menambahkan teks, mengatur batas, warna latar belakang, dan memposisikan kotak secara tepat pada halaman. Ini berguna untuk membuat konten PDF yang kaya visual seperti callout, banner, atau bagian yang disorot dengan teks di atas gambar.

1. Buka atau buat dokumen PDF.
1. Buat objek 'FloatingBox'.
1. Tambahkan konten teks ke kotak.
1. Atur batas kotak dan warna latar belakang.
1. Tambahkan gambar latar belakang.
1. Tambahkan FloatingBox ke halaman.
1. Simpan dokumen PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_image_as_background_in_floating_box(infile, input_image_file, outfile):

    document = ap.Document(infile)
    # Add page to PDF document
    page = document.pages.add()
    # Create FloatingBox object
    box = ap.FloatingBox(200.0, 100.0)
    # Set left position for FloatingBox
    box.left = 40
    # Set Top position for FloatingBox
    box.top = 80
    # Set the Horizontal alignment for FloatingBox
    box.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # Add text fragment to paragraphs collection of FloatingBox
    box.paragraphs.add(ap.text.TextFragment("Text in Floating Box"))
    # Set border for FloatingBox
    box.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)

    img = ap.Image()
    img.file = input_image_file
    # Add background image
    box.background_image = img
    # Set background color for FloatingBox
    box.background_color = ap.Color.yellow
    # Add FloatingBox to paragraphs collection of page object
    page.paragraphs.add(box)
    # Save the PDF document
    document.save(outfile)
```


