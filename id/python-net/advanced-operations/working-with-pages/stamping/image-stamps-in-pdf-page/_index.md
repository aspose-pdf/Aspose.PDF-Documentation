---
title: Tambahkan Cap Gambar ke PDF dalam Python
linktitle: Cap gambar dalam File PDF
type: docs
weight: 10
url: /id/python-net/image-stamps-in-pdf-page/
description: Pelajari cara menambahkan cap gambar ke halaman PDF di Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara menambahkan Cap Gambar dalam PDF menggunakan Python
Abstract: Artikel ini menyediakan panduan komprehensif tentang menambahkan stempel gambar ke file PDF menggunakan pustaka Aspose.PDF untuk Python. Ini merinci penggunaan kelas `ImageStamp`, yang memungkinkan kustomisasi stempel berbasis gambar termasuk properti seperti tinggi, lebar, opasitas, dan rotasi. Prosesnya melibatkan pembuatan objek `Document` dan objek `ImageStamp` dengan properti yang diinginkan, kemudian menambahkan stempel ke halaman tertentu dari PDF menggunakan metode `add_stamp()`. Artikel ini menyertakan potongan kode Python yang menunjukkan cara menerapkan stempel gambar ke PDF dan mengontrol kualitasnya menggunakan properti `quality`, yang mengatur kualitas gambar dalam persentase. Selain itu, artikel ini menjelaskan cara menggunakan stempel gambar sebagai latar belakang dalam kotak mengambang dengan kelas `FloatingBox`, menyediakan contoh kode lain untuk menunjukkan cara implementasinya. Panduan ini berfungsi sebagai sumber yang berguna bagi pengembang yang ingin meningkatkan PDF dengan stempel gambar menggunakan Aspose.PDF.
---

## Menambahkan Image Stamp pada File PDF

Anda dapat menggunakan [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) kelas untuk menambahkan image stamp ke file PDF. The [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) kelas menyediakan properti yang diperlukan untuk membuat stempel berbasis gambar, seperti tinggi, lebar, opasitas, dan sebagainya. Stempel dapat diposisikan, diubah ukurannya, diputar, dan dibuat sebagian transparan, memungkinkan penambahan watermark, branding, atau anotasi.

Potongan kode berikut menunjukkan cara menambahkan stempel gambar dalam file PDF.

1. Muat PDF menggunakan 'ap.Document()'.
1. Buat stempel gambar dengan 'ImageStamp()'.
1. Konfigurasikan properti stempel.
1. Tambahkan stempel ke halaman target.
1. Simpan PDF yang telah dimodifikasi.

```python
import sys
import aspose.pdf as ap
from os import path

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

## Kontrol Kualitas Gambar saat Menambahkan Stempel

Saat menambahkan gambar sebagai objek stamp, Anda dapat mengontrol kualitas gambar. The [kualitas](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/#properties) properti dari [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) kelas digunakan untuk tujuan ini. Ini menunjukkan kualitas gambar dalam persen (nilai yang valid adalah 0..100).
Dengan mengatur properti kualitas, Anda dapat mengurangi resolusi gambar untuk mengoptimalkan ukuran PDF atau mempertahankan fidelitas yang lebih tinggi untuk kejelasan.

1. Buka dokumen PDF.
1. Buat stempel gambar.
1. Atur kualitas gambar.
1. Tambahkan stempel ke halaman target.
1. Simpan PDF yang telah dimodifikasi.

```python
import sys
import aspose.pdf as ap
from os import path

def add_image_stamp_with_quality_control(infile, input_image_file, outfile):
    document = ap.Document(infile)

    image_stamp = ap.ImageStamp(input_image_file)
    image_stamp.quality = 10

    document.pages[1].add_stamp(image_stamp)
    document.save(outfile)
```

## Image Stamp sebagai Latar Belakang di Floating Box

Buat sebuah [FloatingBox](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/) di dalam PDF dan menerapkan gambar sebagai latar belakangnya. Ini juga menunjukkan cara menambahkan teks, mengatur batas, warna latar belakang, dan memposisikan kotak secara tepat pada halaman. Hal ini berguna untuk membuat konten PDF yang visualnya kaya seperti penanda, spanduk, atau bagian yang disorot dengan teks di atas gambar.

1. Buka atau buat dokumen PDF.
1. Buat objek 'FloatingBox'.
1. Tambahkan konten teks ke kotak.
1. Atur batas kotak dan warna latar belakang.
1. Tambahkan gambar latar belakang.
1. Tambahkan FloatingBox ke halaman.
1. Simpan dokumen PDF.

```python
import sys
import aspose.pdf as ap
from os import path

def add_image_as_background_in_floating_box(infile, input_image_file, outfile):
    document = ap.Document(infile)
    page = document.pages[1]
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

## Topik Stamping Terkait

- [Cap halaman PDF dengan Python](/pdf/id/python-net/stamping/)
- [Tambahkan cap halaman ke PDF dengan Python](/pdf/id/python-net/page-stamps-in-the-pdf-file/)
- [Tambahkan cap teks ke PDF di Python](/pdf/id/python-net/text-stamps-in-the-pdf-file/)
- [Tambahkan nomor halaman ke PDF dengan Python](/pdf/id/python-net/add-page-number/)