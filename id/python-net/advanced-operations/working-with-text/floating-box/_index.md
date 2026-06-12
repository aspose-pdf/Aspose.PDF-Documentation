---
title: Gunakan FloatingBox untuk Tata Letak PDF di Python
linktitle: Menggunakan FloatingBox
type: docs
weight: 30
url: /id/python-net/floating-box/
description: Pelajari cara menggunakan FloatingBox untuk tata letak teks, konten multi‑kolom, dan penempatan yang presisi dalam dokumen PDF dengan Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Buat dan tempatkan kontainer FloatingBox bergaya dalam PDF dengan Python
Abstract: Artikel ini menjelaskan cara menggunakan FloatingBox di Aspose.PDF for Python via .NET. Pelajari cara menempatkan teks dan konten lainnya dalam wadah mengambang yang bergaya, mengontrol tata letak, batas, perataan, dan pemotongan, serta membangun desain halaman PDF yang lebih terstruktur dalam Python.
---

## Penggunaan Dasar FloatingBox

The [`FloatingBox`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/) kelas adalah wadah untuk menempatkan teks dan konten lain pada halaman PDF. Ini memberi Anda kontrol yang lebih kuat atas tata letak, batas, dan gaya dibandingkan paragraf teks biasa. Jika konten melebihi ukuran kotak, perilaku pemotongan dikendalikan oleh pengaturan kotak.

Gunakan halaman ini ketika Anda membutuhkan kontainer teks terstruktur, tata letak multi‑kolom, dan penempatan yang tepat dalam dokumen PDF dengan Aspose.PDF for Python via .NET.

1. Buat yang baru [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Tambahkan sebuah [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) ke dokumen.
1. Buat sebuah [`FloatingBox`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/).
1. Atur batas kotak menggunakan [`BorderInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderinfo/) dan [`BorderSide`](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderside/).
1. Pengulangan kotak kontrol dengan [`is_need_repeating`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) property.
1. Tambahkan konten teks menggunakan [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/).
1. Tambahkan `FloatingBox` ke [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Simpan dokumen PDF akhir menggunakan [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python
import aspose.pdf as ap

def create_and_add_floating_box(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        # Create and fill box
        box = ap.FloatingBox(400, 30)
        box.border = ap.BorderInfo(ap.BorderSide.ALL, 1.5, ap.Color.dark_green)
        box.is_need_repeating = False
        phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi."
        box.paragraphs.add(ap.text.TextFragment(phrase))
        # Add box
        page.paragraphs.add(box)
        document.save(outfile)
```

Dalam contoh di atas, `FloatingBox` dibuat dengan lebar 400 pt dan tinggi 30 pt.
Teks secara sengaja melebihi tinggi yang tersedia, sehingga sebagian terpotong.

![Gambar 1](image01.png)

The [`is_need_repeating`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) properti dengan nilai `False` membatasi render teks ke satu halaman.

Jika Anda mengatur properti ini menjadi `True`, teks mengalir ke halaman berikutnya pada posisi yang sama.

![Gambar 2](image02.png)

## Fitur FloatingBox Lanjutan

### Dukungan multi-kolom

#### Tata letak multi-kolom (kasus sederhana)

`FloatingBox` mendukung tata letak multi-kolom. Untuk membuat tata letak seperti itu, Anda harus menentukan nilai-nilai dari [`ColumnInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/columninfo/) properti.

* `column_widths` adalah string yang mendefinisikan lebar setiap kolom dalam poin.
* `column_spacing` adalah string yang mendefinisikan lebar celah antara kolom.
* `column_count` adalah jumlah kolom.

```python
import sys
import aspose.pdf as ap
from os import path

def multi_column_layout(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        # Set margin settings
        page.page_info.margin = ap.MarginInfo(36, 18, 36, 18)
        column_count = 3
        spacing = 10
        width = (
            page.page_info.width
            - page.page_info.margin.left
            - page.page_info.margin.right
            - (column_count - 1) * spacing
        )
        column_width = width / 3
        # Create FloatingBox
        box = ap.FloatingBox()
        box.is_need_repeating = True
        box.column_info.column_widths = f"{column_width} {column_width} {column_width}"
        box.column_info.column_spacing = f"{spacing}"
        box.column_info.column_count = 3
        phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi."
        paragraphs = [
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
        ]
        for paragraph in paragraphs:
            box.paragraphs.add(ap.text.TextFragment(paragraph))
        # Add a box to a page
        page.paragraphs.add(box)
        # Save PDF document
        document.save(outfile)
```

Contoh ini menghasilkan paragraf contoh dan menempatkannya ke dalam tiga kolom. Konten berlanjut ke halaman tambahan sampai semua paragraf ditampilkan.

#### Tata letak multi-kolom dengan memaksa awal kolom

Contoh ini menggunakan pengaturan multi-kolom yang sama, tetapi memaksa setiap paragraf yang ditambahkan untuk mulai di kolom baru. Untuk melakukannya, set `is_first_paragraph_in_column = True` pada setiap `TextFragment` sebelum menambahkannya ke `FloatingBox`.

```python
import sys
import aspose.pdf as ap
from os import path

def multi_column_layout_2(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        # Set margin settings
        page.page_info.margin = ap.MarginInfo(36, 18, 36, 18)
        column_count = 3
        spacing = 10
        width = (
            page.page_info.width
            - page.page_info.margin.left
            - page.page_info.margin.right
            - (column_count - 1) * spacing
        )
        column_width = width / 3
        # Create FloatingBox
        box = ap.FloatingBox()
        box.is_need_repeating = True
        box.column_info.column_widths = f"{column_width} {column_width} {column_width}"
        box.column_info.column_spacing = f"{spacing}"
        box.column_info.column_count = 3
        phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi."
        paragraphs = [
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
        ]
        for paragraph in paragraphs:
            text = ap.text.TextFragment(paragraph)
            text.is_first_paragraph_in_column = True
            box.paragraphs.add(text)
        # Add a box to a page
        page.paragraphs.add(box)
        # Save PDF document
        document.save(outfile)
```

### Dukungan latar belakang

Terapkan warna latar belakang pada `FloatingBox` dalam dokumen PDF menggunakan Aspose.PDF for Python via .NET.
Dengan menetapkan sebuah [`Color`](https://reference.aspose.com/pdf/python-net/aspose.pdf/color/) ke `background_color`, Anda dapat menyorot konten untuk header, panggilan, atau bagian yang bergaya.

Cuplikan kode ini menunjukkan cara membuat kotak teks berwarna hijau muda sederhana dengan konten contoh.

```python
import sys
import aspose.pdf as ap
from os import path

def background_support(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        # Create and fill box
        box = ap.FloatingBox(400, 30)
        box.background_color = ap.Color.light_green
        box.is_need_repeating = False
        box.paragraphs.add(ap.text.TextFragment("text example"))
        # Add box
        page.paragraphs.add(box)
        # Save PDF document
        document.save(outfile)
```

### Dukungan penempatan

Posisi sebuah `FloatingBox` di halaman dikendalikan oleh `positioning_mode`, `left`, dan `top`.
Kapan `positioning_mode` adalah:

* [`ParagraphPositioningMode.DEFAULT`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paragraphpositioningmode/) (bawaan)

Lokasi tergantung pada elemen yang telah ditambahkan sebelumnya. Menambahkan paragraf baru memengaruhi alur elemen selanjutnya. Jika [`left`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) atau [`top`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) bernilai tidak nol, mereka juga diterapkan.

* [`ParagraphPositioningMode.ABSOLUTE`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paragraphpositioningmode/)

Lokasinya ditetapkan oleh `left` dan `top`; itu tidak tergantung pada elemen sebelumnya dan tidak memengaruhi alur elemen selanjutnya.

```python
import sys
import aspose.pdf as ap
from os import path

def offset_support(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        # Create and fill box
        box = ap.FloatingBox(400, 30)
        box.top = 45
        box.left = 15
        box.positioning_mode = ap.ParagraphPositioningMode.ABSOLUTE
        box.border = ap.BorderInfo(ap.BorderSide.ALL, 1.5, ap.Color.dark_green)
        box.paragraphs.add(ap.text.TextFragment("text example 1"))
        page.paragraphs.add(ap.text.TextFragment("text example 2"))
        # Add the box to the page
        page.paragraphs.add(box)
        page.paragraphs.add(ap.text.TextFragment("text example 3"))
        document.save(outfile)
```

### Menyelaraskan Kotak Mengambang dengan Penjajaran Vertikal dan Horizontal dalam PDF

Ratakan `FloatingBox` elemen pada halaman PDF menggunakan [`VerticalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/verticalalignment/) dan [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) di Aspose.PDF for Python via .NET. Ini membantu Anda menempatkan kontainer mengambang di posisi atas, tengah, atau bawah untuk tata letak halaman, blok header/footer, atau catatan samping.

1. Buat dokumen PDF baru.
1. Tambahkan halaman ke dokumen.
1. Tambahkan yang pertama `FloatingBox` dengan perataan kanan bawah.
1. Tambahkan yang kedua `FloatingBox` dengan perataan tengah-kanan.
1. Tambahkan yang ketiga `FloatingBox` dengan perataan kanan atas.
1. Simpan dokumen.

```python
import sys
import aspose.pdf as ap
from os import path

def align_text_to_float(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()

        # Create float box
        float_box = ap.FloatingBox(100, 100)
        # Set settings to float box
        float_box.vertical_alignment = ap.VerticalAlignment.BOTTOM
        float_box.horizontal_alignment = ap.HorizontalAlignment.RIGHT
        float_box.paragraphs.add(ap.text.TextFragment("FloatingBox_bottom"))
        float_box.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.blue)
        # Add float box
        page.paragraphs.add(float_box)

        # Create float box
        float_box_2 = ap.FloatingBox(100, 100)
        # Set settings to float box
        float_box_2.vertical_alignment = ap.VerticalAlignment.CENTER
        float_box_2.horizontal_alignment = ap.HorizontalAlignment.RIGHT
        float_box_2.paragraphs.add(ap.text.TextFragment("FloatingBox_center"))
        float_box_2.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.blue)
        # Add float box
        page.paragraphs.add(float_box_2)

        # Create float box
        float_box_3 = ap.FloatingBox(100, 100)
        # Set settings to float box
        float_box_3.vertical_alignment = ap.VerticalAlignment.TOP
        float_box_3.horizontal_alignment = ap.HorizontalAlignment.RIGHT
        float_box_3.paragraphs.add(ap.text.TextFragment("FloatingBox_top"))
        float_box_3.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.blue)
        # Add float box
        page.paragraphs.add(float_box_3)

        # Save the document
        document.save(outfile)
```

## Topik Teks Terkait

* [Bekerja dengan teks dalam PDF menggunakan Python](/pdf/id/python-net/working-with-text/)
* [Menambahkan teks ke PDF](/pdf/id/python-net/add-text-to-pdf-file/)
* [Format teks PDF di Python](/pdf/id/python-net/text-formatting-inside-pdf/)
* [Tambahkan tooltip ke teks PDF di Python](/pdf/id/python-net/pdf-tooltip/)
