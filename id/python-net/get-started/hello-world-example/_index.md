---
title: Contoh Hello World menggunakan Python
linktitle: Contoh Hello World
type: docs
weight: 20
url: /id/python-net/hello-world-example/
description: Contoh ini menunjukkan cara membuat dokumen PDF sederhana dengan teks Hello World menggunakan Aspose.PDF untuk Python via .NET.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Contoh Hello World via Python
Abstract: Artikel ini menyediakan contoh Hello World menggunakan perpustakaan Aspose.PDF untuk Python via .NET untuk membuat dokumen PDF. Contoh tersebut menunjukkan langkah-langkah dasar penggunaan API Aspose.PDF dengan menghasilkan PDF berisi teks "Hello World!". Prosesnya melibatkan pembuatan objek `Document`, menambahkan `Page`, membuat objek `TextFragment`, menetapkan properti teks seperti ukuran font dan warna, serta menggunakan `TextBuilder` untuk menambahkan teks ke halaman. PDF yang dihasilkan kemudian disimpan sebagai "HelloWorld_out.pdf". Artikel ini menyertakan potongan kode Python lengkap yang mengilustrasikan langkah-langkah tersebut, berfungsi sebagai panduan pengantar penggunaan perpustakaan.
---

Contoh "Hello World" memperlihatkan sintaks paling sederhana dan program paling sederhana dalam bahasa pemrograman apa pun. Pengembang diperkenalkan kepada sintaks dasar bahasa pemrograman dengan belajar cara mencetak "Hello World" pada layar perangkat. Oleh karena itu, secara tradisional kami akan memulai perkenalan dengan perpustakaan kami dari contoh ini.

Dalam artikel ini, kami membuat dokumen PDF yang berisi teks "Hello World!". Setelah menginstal **Aspose.PDF untuk Python via .NET** di lingkungan Anda, Anda dapat menjalankan contoh kode di bawah ini untuk melihat cara kerja API Aspose.PDF.

Potongan kode di bawah ini mengikuti langkah-langkah berikut:

1. Membuat objek [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)
1. Menambahkan sebuah [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) ke objek dokumen
1. Membuat objek [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/)
1. Mengatur Warna Teks
1. Membuat Text Builder
1. Menambahkan [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) ke Page
1. [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) dokumen PDF yang dihasilkan

Potongan kode berikut adalah program "Hello World" yang menunjukkan fungsionalitas Aspose.PDF untuk Python via .NET API.

```python

from datetime import timedelta
import aspose.pdf as ap

def run_simple(self):
    # Initialize document object
    document = ap.Document()
    # Add page
    page = document.pages.add()
    # Add text to new page
    textFragment = ap.text.TextFragment("Hello, world!")
    textFragment.position = ap.text.Position(100, 600)

    textFragment.text_state.font_size = 12
    textFragment.text_state.font = ap.text.FontRepository.find_font(
        "TimesNewRoman"
    )
    textFragment.text_state.background_color = ap.Color.blue
    textFragment.text_state.foreground_color = ap.Color.yellow

    # Create TextBuilder object
    textBuilder = ap.text.TextBuilder(page)

    # Append the text fragment to the PDF page
    textBuilder.append_text(textFragment)

    document.save(self.data_dir + "HelloWorld_out.pdf")
```
