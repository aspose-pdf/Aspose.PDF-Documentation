---
title: Menambahkan Cap Teks dalam PDF via Python
linktitle: Cap Teks di File PDF
type: docs
weight: 20
url: /id/python-net/text-stamps-in-the-pdf-file/
description: Tambahkan cap teks ke dokumen PDF menggunakan kelas TextStamp dengan perpustakaan Aspose.PDF untuk Python.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara menambahkan cap teks dalam PDF menggunakan Python
Abstract: Artikel ini memberikan panduan komprehensif tentang menambahkan cap teks ke file PDF menggunakan perpustakaan Aspose.PDF untuk Python. Artikel ini menjelaskan penggunaan kelas `TextStamp` untuk membuat cap teks yang dapat disesuaikan dengan properti seperti ukuran font, gaya, warna, dan perataan. Artikel ini menyertakan potongan kode yang menunjukkan cara menambahkan cap teks sederhana, mengonfigurasi perataan teks, dan menerapkan mode rendering lanjutan seperti teks isi goresan. Bagian pertama menjelaskan pembuatan objek `Document` dan `TextStamp`, mengatur properti teks, dan menambahkan cap ke halaman tertentu. Bagian kedua memperkenalkan properti `text_alignment` untuk meratakan teks secara horizontal dan vertikal, menyediakan contoh kode untuk memusatkan teks pada halaman PDF. Bagian akhir membahas mode rendering, menunjukkan cara menambahkan teks isi goresan menggunakan objek `TextState` untuk mengatur warna goresan dan mode rendering sebelum mengikat ke cap. Setiap bagian disertai contoh praktis untuk memudahkan pemahaman dan implementasi.
---

## Menambahkan Cap Teks dengan Python

Anda dapat menggunakan kelas [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) untuk menambahkan cap teks dalam file PDF. Kelas [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) menyediakan properti yang diperlukan untuk membuat cap berbasis teks seperti ukuran font, gaya font, dan warna font, dll. Untuk menambahkan cap teks, Anda perlu membuat objek Document dan objek TextStamp menggunakan properti yang diperlukan. Setelah itu, Anda dapat memanggil metode [add_stamp()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) dari Page untuk menambahkan cap ke PDF. Potongan kode berikut menunjukkan cara menambahkan cap teks dalam file PDF. Ini berguna untuk menambahkan anotasi, watermark, atau label ke halaman PDF.

1. Buka dokumen PDF.
1. Buat objek TextStamp.
1. Atur perilaku latar belakang cap.
1. Tempatkan cap pada halaman.
1. Putar cap jika diperlukan.
1. Atur properti teks.
1. Tambahkan cap ke sebuah halaman.
1. Simpan dokumen PDF yang telah dimodifikasi.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

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
    text_stamp.text_state.font_style = ap.text.FontStyles.BOLD
    text_stamp.text_state.font_style = ap.text.FontStyles.ITALIC
    text_stamp.text_state.foreground_color = ap.Color.dark_green
    # Add stamp to particular page
    document.pages[1].add_stamp(text_stamp)

    document.save(output_file_name)
```

