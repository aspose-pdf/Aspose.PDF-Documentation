---
title: Tambahkan Text Stamps ke PDF dengan Python
linktitle: Text stamps pada File PDF
type: docs
weight: 20
url: /id/python-net/text-stamps-in-the-pdf-file/
description: Pelajari cara menambahkan text stamps ke dokumen PDF dalam Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara menambahkan Text stamps ke PDF menggunakan Python
Abstract: Artikel ini memberikan panduan komprehensif tentang menambahkan text stamps ke file PDF menggunakan pustaka Aspose.PDF untuk Python. Artikel ini menjelaskan penggunaan kelas `TextStamp` untuk membuat text stamps yang dapat disesuaikan dengan properti seperti ukuran font, gaya, warna, dan perataan. Artikel ini menyertakan potongan kode yang menunjukkan cara menambahkan text stamp sederhana, mengonfigurasi perataan teks, dan menerapkan mode rendering lanjutan seperti teks fill stroke. Bagian pertama menjelaskan pembuatan objek `Document` dan `TextStamp`, mengatur properti teks, dan menambahkan stempel ke halaman tertentu. Bagian kedua memperkenalkan properti `text_alignment` untuk meratakan teks secara horizontal dan vertikal, dengan contoh kode menempatkan teks di tengah halaman PDF. Bagian terakhir membahas mode rendering, menunjukkan cara menambahkan teks fill stroke menggunakan objek `TextState` untuk mengatur warna stroke dan mode rendering sebelum mengikatnya ke stempel. Setiap bagian disertai contoh praktis untuk memudahkan pemahaman dan implementasi.
---

## Menambahkan Text Stamp dengan Python

Anda dapat menggunakan [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) kelas untuk menambahkan stempel teks dalam file PDF. [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) kelas menyediakan properti yang diperlukan untuk membuat stempel berbasis teks seperti ukuran font, gaya font, dan warna font, dll. Untuk menambahkan stempel teks, Anda perlu membuat objek Document dan objek TextStamp menggunakan properti yang dibutuhkan. Setelah itu, Anda dapat memanggil [add_stamp()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) metode Page untuk menambahkan stempel dalam PDF. Potongan kode berikut menunjukkan cara menambahkan stempel teks dalam file PDF. Ini berguna untuk menambahkan anotasi, watermark, atau label ke halaman PDF.

1. Buka dokumen PDF.
1. Buat objek TextStamp.
1. Atur perilaku latar belakang stempel.
1. Posisikan stempel pada halaman.
1. Putar stempel jika diperlukan.
1. Atur properti teks.
1. Tambahkan stempel ke halaman.
1. Simpan dokumen PDF yang dimodifikasi.

```python
import sys
import aspose.pdf as ap
from os import path

def add_text_stamp(input_file_name, output_file_name):
    document = ap.Document(input_file_name)

    # Create text stamp
    text_stamp = ap.TextStamp("Sample Stamp")
    # Set whether stamp is background
    text_stamp.background = True
    # Set origin
    text_stamp.x_indent = 100
    text_stamp.y_indent = 100
    # Rotate stamp
    text_stamp.rotate = ap.Rotation.ON90
    # Set text properties
    text_stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_stamp.text_state.font_size = 14.0
    text_stamp.text_state.font_style = (
        ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    )
    text_stamp.text_state.foreground_color = ap.Color.dark_green
    # Add stamp to particular page
    document.pages[1].add_stamp(text_stamp)

    document.save(output_file_name)
```

## Topik Stamping Terkait

- [Stempel halaman PDF menggunakan Python](/pdf/id/python-net/stamping/)
- [Tambahkan cap halaman ke PDF di Python](/pdf/id/python-net/page-stamps-in-the-pdf-file/)
- [Tambahkan cap gambar ke PDF di Python](/pdf/id/python-net/image-stamps-in-pdf-page/)
- [Tambahkan nomor halaman ke PDF di Python](/pdf/id/python-net/add-page-number/)