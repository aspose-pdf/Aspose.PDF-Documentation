---
title: Tambahkan Nomor Halaman ke PDF dengan Python
linktitle: Menambahkan Nomor Halaman
type: docs
weight: 30
url: /id/python-net/add-page-number/
description: Pelajari cara menambahkan stempel nomor halaman ke dokumen PDF menggunakan Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara menambahkan Nomor Halaman ke PDF menggunakan Python
Abstract: Artikel ini membahas pentingnya menambahkan nomor halaman ke dokumen untuk memudahkan navigasi dan memperkenalkan pustaka Aspose.PDF for Python via .NET sebagai alat untuk mencapai hal ini pada file PDF. Pustaka tersebut menggunakan kelas PageNumberStamp, yang menyediakan properti untuk menyesuaikan stempel nomor halaman, termasuk format, margin, perataan, dan nomor mulai. Prosesnya melibatkan pembuatan objek Document dan objek PageNumberStamp, mengkonfigurasi properti yang diinginkan, dan menerapkan stempel ke halaman PDF menggunakan metode add_stamp(). Artikel ini menyediakan contoh kode Python yang menunjukkan cara menyiapkan dan menerapkan stempel nomor halaman dengan atribut font yang dapat disesuaikan.
---

Semua dokumen harus memiliki nomor halaman di dalamnya. Nomor halaman memudahkan pembaca untuk menemukan bagian-bagian berbeda dari dokumen.

**Aspose.PDF for Python via .NET** memungkinkan Anda menambahkan nomor halaman dengan [PageNumberStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/).

## Menambahkan Stempel Nomor Halaman ke PDF

Tambahkan stempel nomor halaman dinamis ke PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) menggunakan Aspose.PDF for Python. The [`PageNumberStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/) objek memungkinkan Anda untuk secara otomatis menampilkan nomor halaman saat ini bersama dengan total jumlah halaman. Contoh menunjukkan cara membuat stempel nomor halaman, menyesuaikan tampilannya (font, ukuran, gaya, warna, perataan, dan margin) menggunakan [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/), dan menerapkannya ke spesifik [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) di PDF melalui [`Page.add_stamp()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) metode. Nilai perataan berasal dari [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) enum, dan warna/font/gaya tersedia melalui [`Color`](https://reference.aspose.com/pdf/python-net/aspose.pdf/color/) dan [`FontStyles`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/fontstyles/) (font yang ditemukan melalui [`FontRepository.find_font()`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/fontrepository/#methods)) . Fungsionalitas ini berguna untuk menghasilkan dokumen profesional yang bernomor dan mengotomatisasi penomoran halaman dalam alur kerja PDF.

1. Buka dokumen PDF.
1. Buat stempel nomor halaman.
1. Atur properti stempel.
1. Sesuaikan gaya teks.
1. Terapkan stempel ke halaman.
1. Simpan PDF yang telah dimodifikasi.

```python
import sys
import aspose.pdf as ap
from os import path

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
    page_number_stamp.text_state.font_style = (
        ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    )
    page_number_stamp.text_state.foreground_color = ap.Color.blue_violet

    # Add stamp to particular page
    document.pages[1].add_stamp(page_number_stamp)

    # Save output document
    document.save(output_file_name)
```

## Menambahkan Nomor Halaman Romawi ke PDF

Tambahkan nomor halaman dalam format angka Romawi ke semua halaman dokumen PDF. Nomor halaman ditambahkan sebagai stempel menggunakan [`PageNumberStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/), dengan font, ukuran, gaya, warna, dan perataan yang dapat disesuaikan. Gunakan [`NumberingStyle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/numberingstyle/) enum untuk memilih angka Romawi atau skema penomoran lainnya. Penomoran juga dapat dimulai dari nilai yang ditentukan.

1. Buka dokumen PDF.
1. Buat stempel nomor halaman.
1. Konfigurasikan properti stempel.
1. Atur tampilan teks.
1. Terapkan stempel ke semua halaman.
1. Simpan PDF yang telah dimodifikasi.

```python
import sys
import aspose.pdf as ap
from os import path

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

[Tambahkan nomor halaman PDF](https://products.aspose.app/pdf/page-number) adalah aplikasi web gratis online yang memungkinkan Anda menyelidiki cara kerja penambahan fungsi nomor halaman.

[![Cara menambahkan nomor halaman pada PDF menggunakan Python](page_number.png)](https://products.aspose.app/pdf/page-number)

## Topik Stamping Terkait

- [Cap halaman PDF dengan Python](/pdf/id/python-net/stamping/)
- [Tambahkan cap halaman ke PDF dengan Python](/pdf/id/python-net/page-stamps-in-the-pdf-file/)
- [Tambahkan cap gambar ke PDF di Python](/pdf/id/python-net/image-stamps-in-pdf-page/)
- [Tambahkan cap teks ke PDF di Python](/pdf/id/python-net/text-stamps-in-the-pdf-file/)