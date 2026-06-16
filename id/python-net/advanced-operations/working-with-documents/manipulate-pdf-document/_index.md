---
title: Manipulasi Dokumen PDF dengan Python
linktitle: Manipulasi Dokumen PDF
type: docs
weight: 20
url: /id/python-net/manipulate-pdf-document/
description: Pelajari cara memvalidasi, menyusun, dan memodifikasi dokumen PDF dalam Python, termasuk pengelolaan TOC dan pemeriksaan PDF/A.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Panduan tentang memanipulasi dokumen PDF menggunakan Python
Abstract: Artikel ini menyediakan panduan komprehensif tentang manipulasi dokumen PDF menggunakan Python, khususnya dengan pustaka Aspose.PDF. Ini mencakup beberapa fungsionalitas, termasuk memvalidasi dokumen PDF untuk kepatuhan PDF/A-1a dan PDF/A-1b menggunakan metode `validate` dari kelas `Document`. Artikel ini juga merinci cara menambahkan, menyesuaikan, dan mengelola Table of Contents (TOC) dalam file PDF, seperti mengatur berbagai TabLeaderTypes, menyembunyikan nomor halaman, dan menyesuaikan penomoran halaman dengan awalan. Selain itu, artikel menjelaskan cara menetapkan tanggal kedaluwarsa untuk dokumen PDF dengan menyematkan JavaScript untuk pembatasan akses dan cara meratakan formulir yang dapat diisi dalam PDF agar tidak dapat diedit. Setiap bagian disertai dengan potongan kode yang menunjukkan implementasi fitur-fitur ini menggunakan Aspose.PDF di Python.
---

Halaman ini berguna ketika Anda perlu memvalidasi kepatuhan PDF, membuat atau menyesuaikan daftar isi, mengatur perilaku kedaluwarsa dokumen, atau meratakan PDF yang dapat diisi dalam alur kerja Python.

## Manipulasi Dokumen PDF dalam Python

## Validasi Dokumen PDF untuk Standar PDF A (A 1A dan A 1B)

Untuk memvalidasi dokumen PDF agar kompatibel dengan PDF/A-1a atau PDF/A-1b, gunakan [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) kelas [validasi](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) metode. Metode ini memungkinkan Anda untuk menentukan nama file tempat hasil disimpan dan tipe validasi yang diperlukan berupa enumerasi PdfFormat : PDF_A_1A atau PDF_A_1B.

Potongan kode berikut menunjukkan cara memvalidasi dokumen PDF untuk PDF/A-1A.

```python
import sys
from os import path
import aspose.pdf as ap


def validate_pdfa_standard_a1a(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    document.validate(output_pdf, ap.PdfFormat.PDF_A_1A)
```

Potongan kode berikut menunjukkan cara memvalidasi dokumen PDF untuk PDF/A-1b.

```python
import sys
from os import path
import aspose.pdf as ap


def validate_pdfa_standard_a1b(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    document.validate(output_pdf, ap.PdfFormat.PDF_A_1B)
```

## Bekerja dengan TOC

### Tambahkan TOC ke PDF yang Ada

TOC dalam PDF adalah singkatan dari "Table of Contents." Ini adalah fitur yang memungkinkan pengguna untuk dengan cepat menavigasi dokumen dengan menyediakan gambaran mengenai bagian-bagian dan judul-judulnya. 

Untuk menambahkan TOC ke file PDF yang ada, gunakan kelas Heading di [Aspose.PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf/) namespace. The [Aspose.PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf/) namespace dapat membuat file PDF baru dan memanipulasi file PDF yang sudah ada. Untuk menambahkan TOC ke PDF yang ada, gunakan namespace Aspose.Pdf. Potongan kode berikut menunjukkan cara membuat daftar isi di dalam file PDF yang sudah ada menggunakan Python via .NET.

```python
import sys
from os import path
import aspose.pdf as ap


def add_table_of_contents(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    toc_page = document.pages.insert(1)
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.title = title
    toc_page.toc_info = toc_info

    titles = ["First page", "Second page"]
    for index, title_text in enumerate(titles[:2]):
        heading = ap.Heading(1)
        segment = ap.text.TextSegment(title_text)
        heading.toc_page = toc_page
        heading.segments.append(segment)
        destination_page = document.pages[index + 2]
        heading.destination_page = destination_page
        heading.top = destination_page.rect.height
        toc_page.paragraphs.add(heading)

    document.save(output_pdf)
```

### Atur TabLeaderType yang berbeda untuk tingkat TOC yang berbeda

Aspose.PDF for Python juga memungkinkan pengaturan TabLeaderType yang berbeda untuk level TOC yang berbeda. Anda perlu mengatur [garis_putus](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) milik [InfoDaftarIsi](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/).

```python
import sys
from os import path
import aspose.pdf as ap


def set_toc_levels(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    toc_page = document.pages.add()
    toc_info = ap.TocInfo()
    toc_info.line_dash = ap.text.TabLeaderType.SOLID
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 30
    toc_info.title = title
    toc_page.toc_info = toc_info

    toc_info.format_array_length = 4
    toc_info.format_array[0].margin.left = 0
    toc_info.format_array[0].margin.right = 30
    toc_info.format_array[0].line_dash = ap.text.TabLeaderType.DOT
    toc_info.format_array[0].text_state.font_style = (
        ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    )
    toc_info.format_array[1].margin.left = 10
    toc_info.format_array[1].margin.right = 30
    toc_info.format_array[1].line_dash = 3
    toc_info.format_array[1].text_state.font_size = 10
    toc_info.format_array[2].margin.left = 20
    toc_info.format_array[2].margin.right = 30
    toc_info.format_array[2].text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.format_array[3].line_dash = ap.text.TabLeaderType.SOLID
    toc_info.format_array[3].margin.left = 30
    toc_info.format_array[3].margin.right = 30
    toc_info.format_array[3].text_state.font_style = ap.text.FontStyles.BOLD

    page = document.pages.add()
    for level in range(1, 5):
        heading = ap.Heading(level)
        heading.is_auto_sequence = True
        heading.toc_page = toc_page
        heading.text_state.font = ap.text.FontRepository.find_font("Arial")
        segment = ap.text.TextSegment(f"Sample Heading{level}")
        heading.segments.append(segment)
        heading.is_in_list = True
        page.paragraphs.add(heading)

    document.save(output_pdf)
```

### Sembunyikan Nomor Halaman di TOC

Jika Anda tidak ingin menampilkan nomor halaman, bersama dengan judul dalam TOC, Anda dapat menggunakan [tampilkan_nomor_halaman](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) milik [InfoDaftarIsi](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) Kelas sebagai false. Silakan periksa cuplikan kode berikut untuk menyembunyikan nomor halaman dalam daftar isi:

```python
import sys
from os import path
import aspose.pdf as ap


def hide_page_numbers_in_toc(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    toc_page = document.pages.add()
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.title = title
    toc_info.is_show_page_numbers = False
    toc_page.toc_info = toc_info

    toc_info.format_array_length = 4
    toc_info.format_array[0].margin.right = 0
    toc_info.format_array[0].text_state.font_style = (
        ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    )
    toc_info.format_array[1].margin.left = 30
    toc_info.format_array[1].text_state.underline = True
    toc_info.format_array[1].text_state.font_size = 10
    toc_info.format_array[2].text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.format_array[3].text_state.font_style = ap.text.FontStyles.BOLD

    page = document.pages.add()
    for level in range(1, 2):
        heading = ap.Heading(level)
        heading.toc_page = toc_page
        heading.is_auto_sequence = True
        heading.is_in_list = True
        segment = ap.text.TextSegment(f"this is heading of level {level}")
        heading.segments.append(segment)
        page.paragraphs.add(heading)

    document.save(output_pdf)
```

### Sesuaikan Nomor Halaman saat menambahkan TOC

Umumnya, halaman penomoran dalam TOC dapat disesuaikan saat menambahkan TOC dalam dokumen PDF. Misalnya, kita mungkin perlu menambahkan prefiks sebelum nomor halaman seperti P1, P2, P3, dan seterusnya. Dalam kasus seperti itu, Aspose.PDF for Python menyediakan [awalan_nomor_halaman](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) milik [InfoDaftarIsi](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) kelas yang dapat digunakan untuk menyesuaikan nomor halaman seperti yang ditunjukkan dalam contoh kode berikut.

```python
import sys
from os import path
import aspose.pdf as ap


def customize_page_numbers_in_toc(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    toc_page = document.pages.insert(1)
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.title = title
    toc_info.page_numbers_prefix = "P"
    toc_page.toc_info = toc_info

    for index, page in enumerate(document.pages, start=1):
        heading = ap.Heading(1)
        heading.toc_page = toc_page
        heading.destination_page = page
        heading.top = page.rect.height
        segment = ap.text.TextSegment(f"Page {index}")
        heading.segments.append(segment)
        toc_page.paragraphs.add(heading)

    document.save(output_pdf)
```

## Cara mengatur tanggal kedaluwarsa PDF

Kami menerapkan hak akses pada file PDF sehingga sekelompok pengguna tertentu dapat mengakses fitur/objek tertentu dari dokumen PDF. Untuk membatasi akses file PDF, kami biasanya menerapkan enkripsi dan mungkin ada kebutuhan untuk menetapkan kedaluwarsa file PDF, sehingga pengguna yang mengakses/menampilkan dokumen mendapatkan prompt yang valid mengenai kedaluwarsa file PDF.

```python
import sys
from os import path
import aspose.pdf as ap


def set_pdf_expiry_date(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    document.pages.add()
    document.pages[1].paragraphs.add(ap.text.TextFragment("Hello World..."))
    script = ap.annotations.JavascriptAction(
        "var year=2017;"
        "var month=5;"
        "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());"
        "expiry = new Date(year, month);"
        "if (today.getTime() > expiry.getTime())"
        "app.alert('The file is expired. You need a new one.');"
    )
    document.open_action = script
    document.save(output_pdf)
```

## Ratakan PDF yang dapat diisi di Python

Dokumen PDF sering menyertakan formulir dengan widget interaktif yang dapat diisi seperti tombol radio, kotak centang, kotak teks, daftar, dll. Agar tidak dapat diedit untuk berbagai keperluan aplikasi, kita perlu meratakan file PDF.
Aspose.PDF menyediakan fungsi untuk meratakan PDF Anda di Python dengan hanya beberapa baris kode:

```python
import sys
from os import path
import aspose.pdf as ap


def flatten_fillable_pdf(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    if document.form and document.form.fields:
        for field in document.form.fields:
            field.flatten()
    document.save(output_pdf)
```

## Topik Dokumen Terkait

- [Bekerja dengan dokumen PDF di Python](/pdf/id/python-net/working-with-documents/)
- [Format dokumen PDF dalam Python](/pdf/id/python-net/formatting-pdf-document/)
- [Buat file PDF di Python](/pdf/id/python-net/create-pdf-document/)
- [Optimalkan file PDF dalam Python](/pdf/id/python-net/optimize-pdf/)
