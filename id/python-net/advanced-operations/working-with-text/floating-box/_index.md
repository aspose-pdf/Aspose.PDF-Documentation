---
title: Menggunakan FloatingBox untuk menghasilkan teks dengan Python
linktitle: Menggunakan FloatingBox
type: docs
weight: 30
url: /id/python-net/floating-box/
description: Halaman ini menjelaskan cara memformat teks di dalam kotak mengambang.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Alat FloatingBox untuk menghasilkan teks
Abstract: Artikel ini memberikan panduan komprehensif tentang penggunaan alat FloatingBox dalam Aspose.PDF untuk Python, yang memungkinkan pengembang menempatkan teks dan konten lain dalam wadah yang dapat dipindahkan dan bergaya pada halaman PDF. Artikel ini mencakup penggunaan dasar maupun lanjutan, menunjukkan cara membuat floating box, menerapkan border dan warna latar belakang, mengontrol tata letak multi-kolom, mengelola posisi paragraf, serta menyelaraskan kotak secara vertikal dan horizontal. Artikel ini juga menyoroti fitur utama seperti pemotongan teks, konten yang diulang di beberapa halaman, penempatan absolut, dan kontrol tata letak yang ditingkatkan, memungkinkan penyesuaian PDF yang tepat. Melalui contoh kode praktis, pembaca belajar cara membuat PDF yang menarik secara visual dan terstruktur dengan baik yang memanfaatkan seluruh kemampuan kontainer FloatingBox.
---

## Dasar-dasar menggunakan alat FloatingBox

Alat [`FloatingBox`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/) adalah wadah khusus untuk menempatkan teks dan konten lain pada halaman PDF. Fitur utamanya adalah pemotongan teks ketika konten melebihi batas kotak. Buat dan tambahkan `FloatingBox` ke sebuah [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) menggunakan Aspose.PDF untuk Python. `FloatingBox` berfungsi sebagai wadah teks yang dapat dipindahkan, memungkinkan kontrol yang lebih besar atas posisi tata letak, border, dan gaya dibandingkan paragraf teks biasa.

1. Buat [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) baru.
1. Tambahkan [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) ke dokumen.
1. Buat [`FloatingBox`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/).
1. Atur border kotak menggunakan [`BorderInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderinfo/) dan [`BorderSide`](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderside/).
1. Kendalikan pengulangan kotak dengan properti [`is_need_repeating`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties).
1. Tambahkan konten teks menggunakan [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/).
1. Tambahkan `FloatingBox` ke [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Simpan dokumen PDF akhir menggunakan [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

import math
import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def create_and_add_floating_box(outfile):
    """
    Create and add a basic floating box to a PDF document.

    Demonstrates the fundamental usage of FloatingBox to create a bordered
    text container with Lorem ipsum content. Shows basic box creation,
    styling, and text content addition.

    Args:
        outfile (str): Path where the PDF with floating box will be saved.

    Returns:
        None: The function creates and saves a PDF file with a floating box.

    Note:
        - Creates a FloatingBox with dimensions 400x30
        - Applies dark green border with 1.5 width
        - Sets is_need_repeating to False for single occurrence
        - Contains Lorem ipsum text fragment
        - Demonstrates basic floating box functionality

    Example:
        >>> create_and_add_floating_box("basic_floating_box.pdf")
        # Creates a PDF with a simple bordered floating text box
    """

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

Pada contoh di atas, kami membuat FloatingBox dengan lebar 400 pt dan tinggi 30 pt.
Selain itu, dalam contoh ini, lebih banyak teks sengaja dibuat daripada yang dapat muat dalam ukuran yang diberikan.
Akibatnya, teks terpotong.

![Image 1](image01.png)

Properti [`is_need_repeating`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) dengan nilai `False` membatasi teks ke satu halaman.

Jika kita mengatur properti ini ke `True` teks akan mengalir ke halaman berikutnya di posisi yang sama.

![Image 2](image02.png)

## Fitur lanjutan FloatingBox

### Dukungan multi-kolom

#### Tata letak multi-kolom (kasus sederhana)

`FloatingBox` mendukung tata letak multi-kolom. Untuk membuat tata letak seperti itu, Anda harus mendefinisikan nilai properti [`ColumnInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/columninfo/).

* `column_widths` adalah string dengan enumerasi lebar dalam pt.
* `column_spacing` adalah string dengan lebar celah antara kolom.
* `column_count` adalah jumlah kolom.

```python

import math
import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def multi_column_layout(outfile):
    """
    Create a multi-column layout using FloatingBox.

    Demonstrates advanced layout capabilities by creating a three-column
    text layout within a floating box. Shows dynamic width calculation
    and column spacing configuration.

    Args:
        outfile (str): Path where the PDF with multi-column layout will be saved.

    Returns:
        None: The function creates and saves a PDF file with multi-column text.

    Note:
        - Creates 3 equal-width columns with 10-unit spacing
        - Calculates column width based on page margins and spacing
        - Uses is_need_repeating for content continuation across columns
        - Adds multiple Lorem ipsum paragraphs for column demonstration
        - Automatically distributes content across columns

    Example:
        >>> multi_column_layout("multi_column.pdf")
        # Creates a PDF with text arranged in three columns
    """
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

Kami menggunakan pustaka tambahan LoremNET dalam contoh di atas dan membuat 20 paragraf. Paragraf-paragraf ini dibagi menjadi tiga kolom dan mengisi halaman-halaman berikut hingga teks habis.

#### Tata letak multi-kolom dengan mulai kolom paksa

Kami akan melakukan hal yang sama dengan contoh berikut seperti sebelumnya. Perbedaannya adalah kami membuat 3 paragraf. Kami dapat memaksa FloatingBox untuk menampilkan setiap paragraf pada kolom baru. Untuk melakukannya, kami perlu mengatur `is_first_paragraph_in_column` saat menambahkan teks ke objek FloatingBox.

```python

import math
import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def multi_column_layout_2(outfile):
    """
    Create a multi-column layout with paragraph column control.

    Demonstrates advanced multi-column layout with explicit control over
    paragraph positioning within columns. Uses is_first_paragraph_in_column
    to control text flow and column breaks.

    Args:
        outfile (str): Path where the PDF with controlled multi-column layout will be saved.

    Returns:
        None: The function creates and saves a PDF file with controlled column text.

    Note:
        - Creates 3 equal-width columns with 10-unit spacing
        - Uses is_first_paragraph_in_column for explicit column control
        - Calculates column width dynamically based on page dimensions
        - Demonstrates precise paragraph positioning within columns
        - Shows advanced column layout management techniques

    Example:
        >>> multi_column_layout_2("controlled_columns.pdf")
        # Creates a PDF with precisely controlled multi-column text flow
    """

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

Terapkan warna latar belakang ke FloatingBox dalam dokumen PDF menggunakan Aspose.PDF untuk Python via .NET.
`FloatingBox` adalah wadah untuk teks atau elemen lain, dan dengan menetapkan sebuah [`Color`](https://reference.aspose.com/pdf/python-net/aspose.pdf/color/) sebagai warna latar belakang, Anda dapat membuat konten menonjol secara visual — berguna untuk header, sorotan, atau bagian bergaya.

Potongan kode ini menunjukkan cara membuat kotak teks hijau muda sederhana dengan konten contoh.

```python

import math
import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def background_support(outfile):
    """
    Demonstrate FloatingBox background color support.

    Shows how to apply background colors to floating boxes to create
    visually distinct text containers. Demonstrates basic styling
    capabilities for enhanced visual presentation.

    Args:
        outfile (str): Path where the PDF with colored background box will be saved.

    Returns:
        None: The function creates and saves a PDF file with a colored floating box.

    Note:
        - Applies light green background color to the floating box
        - Creates a 400x30 box with sample text content
        - Sets is_need_repeating to False for single occurrence
        - Demonstrates visual styling options for floating boxes
        - Shows how background colors enhance text presentation

    Example:
        >>> background_support("colored_background.pdf")
        # Creates a PDF with a light green background floating box
    """

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

Lokasi FloatingBox pada halaman yang dihasilkan ditentukan oleh properti `positioning_mode`, `left`, `top`.
Ketika nilai `positioning_mode` adalah

* [`ParagraphPositioningMode.DEFAULT`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paragraphpositioningmode/) (nilai default)

Lokasi ditentukan oleh elemen yang ditempatkan sebelumnya; menambahkan elemen memengaruhi lokasi elemen berikutnya. Jika [`Left`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) atau [`Top`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) tidak nol, mereka juga dipertimbangkan, tetapi logika gabungan dapat tidak jelas.

* [`ParagraphPositioningMode.ABSOLUTE`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paragraphpositioningmode/)

Lokasi ditentukan oleh nilai `Left` dan `Top`; tidak bergantung pada elemen sebelumnya dan tidak memengaruhi lokasi elemen setelahnya.

```python

import math
import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def offset_support(outfile):
    """
    Demonstrate FloatingBox positioning and offset support.

    Shows how to position floating boxes at specific coordinates using
    absolute positioning mode. Demonstrates integration of floating boxes
    with regular text content and precise layout control.

    Args:
        outfile (str): Path where the PDF with positioned floating box will be saved.

    Returns:
        None: The function creates and saves a PDF file with positioned floating box.

    Note:
        - Uses absolute positioning mode for precise box placement
        - Sets box position to top=45, left=15 coordinates
        - Creates bordered box with dark green border
        - Integrates floating box with regular text paragraphs
        - Demonstrates layered content with mixed positioning

    Example:
        >>> offset_support("positioned_box.pdf")
        # Creates a PDF with a floating box at specific coordinates
    """

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

### Menyelaraskan Kotak Mengapung dengan Penjajaran Vertikal dan Horizontal dalam PDF

Menyelaraskan elemen `FloatingBox` dalam halaman PDF menggunakan opsi [`VerticalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/verticalalignment/) dan [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) yang berbeda di Aspose.PDF untuk Python via .NET. Ini menunjukkan cara mengontrol posisi tata letak (atas, tengah, bawah, kiri, kanan) untuk mencapai penjajaran visual yang tepat pada kontainer mengapung. Setiap kotak mengapung diberikan posisi yang berbeda untuk menampilkan fleksibilitas penjajaran bagi tata letak halaman, penempatan header/footer, atau anotasi sisi.

1. Buat Dokumen PDF Baru.
1. Tambahkan Halaman ke Dokumen.
1. Buat FloatingBox Pertama (Penjajaran Bawah-Kanan).
1. Buat FloatingBox Kedua (Penjajaran Tengah-Kanan).
1. Buat FloatingBox Ketiga (Penjajaran Atas-Kanan).
1. Simpan Dokumen.

```python

import math
import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def align_text_to_float(outfile):
    """
    Demonstrate text alignment options for FloatingBox elements.

    Shows different vertical and horizontal alignment options for floating
    boxes. Creates multiple boxes with different alignment settings to
    demonstrate positioning flexibility.

    Args:
        outfile (str): Path where the PDF with aligned floating boxes will be saved.

    Returns:
        None: The function creates and saves a PDF file with variously aligned boxes.

    Note:
        - Creates three 100x100 floating boxes with different alignments
        - First box: bottom-right alignment
        - Second box: center-right alignment
        - Third box: top-right alignment
        - All boxes have blue borders for visual distinction
        - Demonstrates comprehensive alignment control options

    Example:
        >>> align_text_to_float("aligned_boxes.pdf")
        # Creates a PDF with floating boxes in different alignment positions
    """
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
