---
title: Menambahkan Nomor Halaman ke PDF dengan Python
linktitle: Menambahkan Nomor Halaman
type: docs
weight: 30
url: /id/python-net/add-page-number/
description: Aspose.PDF for Python via .NET memungkinkan Anda menambahkan Cap Nomor Halaman ke file PDF Anda menggunakan kelas PageNumber Stamp.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara menambahkan Nomor Halaman ke PDF menggunakan Python
Abstract: Artikel ini membahas pentingnya menambahkan nomor halaman ke dokumen untuk memudahkan navigasi dan memperkenalkan pustaka Aspose.PDF for Python via .NET sebagai alat untuk mencapai hal ini dalam file PDF. Pustaka ini menggunakan kelas PageNumberStamp, yang menyediakan properti untuk menyesuaikan cap nomor halaman, termasuk format, margin, perataan, dan nomor mulai. Prosesnya melibatkan pembuatan objek Document dan objek PageNumberStamp, mengonfigurasi properti yang diinginkan, dan menerapkan cap ke halaman PDF menggunakan metode add_stamp(). Artikel ini menyediakan contoh kode Python yang menunjukkan cara menyiapkan dan menerapkan cap nomor halaman dengan atribut font yang dapat disesuaikan.
---

Semua dokumen harus memiliki nomor halaman. Nomor halaman memudahkan pembaca menemukan bagian-bagian berbeda dari dokumen.

**Aspose.PDF for Python via .NET** memungkinkan Anda menambahkan nomor halaman dengan [PageNumberStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/).

## Menambahkan Cap Nomor Halaman ke PDF

Tambahkan cap nomor halaman dinamis ke PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) menggunakan Aspose.PDF for Python. Objek [`PageNumberStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/) memungkinkan Anda secara otomatis menampilkan nomor halaman saat ini bersama dengan total jumlah halaman. Contoh ini menunjukkan cara membuat cap nomor halaman, menyesuaikan tampilannya (font, ukuran, gaya, warna, perataan, dan margin) menggunakan [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/), dan menerapkannya ke [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) tertentu dalam PDF melalui metode [`Page.add_stamp()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods). Nilai perataan diambil dari enum [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/), dan warna/font/gaya tersedia melalui [`Color`](https://reference.aspose.com/pdf/python-net/aspose.pdf/color/) dan [`FontStyles`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/fontstyles/) (font ditemukan melalui [`FontRepository.find_font()`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/fontrepository/#methods)). Fungsionalitas ini berguna untuk menghasilkan dokumen profesional yang bernomor dan mengotomatiskan penomoran halaman dalam alur kerja PDF.

1. Buka dokumen PDF.
1. Buat cap nomor halaman.
1. Atur properti cap.
1. Sesuaikan gaya teks.
1. Terapkan cap ke halaman.
1. Simpan PDF yang telah dimodifikasi.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_page_num_stamp(input_file_name, output_file_name):
    # Open document
    document = ap.Document(input_file_name)

    # Create page number stamp
    page_number_stamp = ap.PageNumberStamp()
    # Whether the stamp is background
    page_number_stamp.background = False
    page_number_stamp.format = "Page # of " + str(len(document.pages))
    page_number_stamp.bottom_margin = 10
    page_number_stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    page_number_stamp.starting_number = 1
    # Set text properties
    page_number_stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    page_number_stamp.text_state.font_size = 14.0
    page_number_stamp.text_state.font_style = ap.text.FontStyles.BOLD
    page_number_stamp.text_state.font_style = ap.text.FontStyles.ITALIC
    page_number_stamp.text_state.foreground_color = ap.Color.blue_violet

    # Add stamp to particular page
    document.pages[1].add_stamp(page_number_stamp)

    # Save output document
    document.save(output_file_name)
```

## Menambahkan Nomor Halaman Romawi ke PDF

Tambahkan nomor halaman dalam format angka Romawi ke semua halaman dokumen PDF. Nomor halaman ditambahkan sebagai cap menggunakan [`PageNumberStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/), dengan font, ukuran, gaya, warna, dan perataan yang dapat disesuaikan. Gunakan enum [`NumberingStyle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/numberingstyle/) untuk memilih angka Romawi atau skema penomoran lainnya. Penomoran juga dapat dimulai dari nilai yang ditentukan.

1. Buka dokumen PDF.
1. Buat cap nomor halaman.
1. Konfigurasikan properti cap.
1. Atur tampilan teks.
1. Terapkan cap ke semua halaman.
1. Simpan PDF yang telah dimodifikasi.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_page_num_stamp_roman(input_file_name, output_file_name):
    # Open document
    document = ap.Document(input_file_name)

    # Create page number stamp
    page_number_stamp = ap.PageNumberStamp()
    # Whether the stamp is background
    page_number_stamp.background = False
    page_number_stamp.bottom_margin = 10
    page_number_stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    page_number_stamp.starting_number = 42
    page_number_stamp.numbering_style = ap.NumberingStyle.NUMERALS_ROMAN_UPPERCASE

    # Set text properties
    page_number_stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    page_number_stamp.text_state.font_size = 14.0
    page_number_stamp.text_state.font_style = ap.text.FontStyles.BOLD
    page_number_stamp.text_state.foreground_color = ap.Color.blue_violet

    # Add stamp to particular page
    for page in document.pages:
        page.add_stamp(page_number_stamp)

    # Save output document
    document.save(output_file_name)
```

## Contoh Langsung

[Tambahkan nomor halaman PDF](https://products.aspose.app/pdf/page-number) adalah aplikasi web gratis daring yang memungkinkan Anda menyelidiki cara kerja penambahan fungsi nomor halaman.

[![Cara menambahkan nomor halaman dalam pdf menggunakan Python](page_number.png)](https://products.aspose.app/pdf/page-number)


