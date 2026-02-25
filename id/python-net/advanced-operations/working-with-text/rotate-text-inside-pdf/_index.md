---
title: Putar Teks Di Dalam PDF Menggunakan Python
linktitle: Putar Teks Di Dalam PDF
type: docs
weight: 50
url: /id/python-net/rotate-text-inside-pdf/
description: Jelajahi cara memutar teks di dalam dokumen PDF menggunakan Python untuk format dokumen yang fleksibel dengan Aspose.PDF untuk Python.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara Memutar Teks di PDF dengan Python
Abstract: Artikel ini menyediakan panduan terperinci tentang cara memutar teks dalam dokumen PDF menggunakan pustaka Aspose.PDF untuk Python via .NET. Artikel ini menjelaskan penggunaan properti `Rotation` dari kelas `TextFragment` untuk mencapai rotasi teks pada berbagai sudut, yang berguna dalam berbagai skenario pembuatan dokumen. Menunjukkan cara membuat fragmen teks dengan sudut rotasi tertentu dan menambahkannya ke halaman PDF menggunakan `TextBuilder`. Mengilustrasikan cara menambahkan fragmen teks yang diputar ke `TextParagraph` dan kemudian menambahkan paragraf tersebut ke halaman PDF. Menunjukkan cara menambahkan fragmen teks yang diputar langsung ke koleksi paragraf halaman. Menjelaskan memutar seluruh paragraf dengan banyak fragmen teks.
---

Putar fragmen teks dalam dokumen PDF menggunakan Aspose.PDF untuk Python via .NET. Ini menunjukkan cara mengontrol posisi dan rotasi elemen teks secara tepat dengan menggabungkan kelas 'TextFragment', 'TextState', dan 'TextBuilder'. Dengan menyesuaikan sudut rotasi untuk setiap fragmen teks, Anda dapat membuat tata letak visual yang dinamis, seperti header diagonal, label vertikal, atau anotasi yang diputar.

## Putar Fragmen Teks Menggunakan TextBuilder di PDF

Membuat file PDF bernama rotated_fragments.pdf yang berisi tiga fragmen teks yang disejajarkan secara horizontal:

- teks pertama tidak diputar
- teks kedua diputar 45°
- teks ketiga diputar 90°

1. Buat Dokumen PDF Baru.
1. Sisipkan halaman baru untuk menampung teks yang diputar.
1. Buat Fragmen Teks Pertama - Tanpa Rotasi.
1. Buat Fragmen Teks Kedua - Rotasi 45°.
1. Buat Fragmen Teks Ketiga - Rotasi 90°.
1. Tambahkan Fragmen Teks Menggunakan TextBuilder.
1. Simpan Dokumen.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def rotate_text_inside_pdf_1(outfile):
    """
    Implement text rotation using TextFragment and TextBuilder.

    Demonstrates basic text rotation techniques by creating multiple text
    fragments with different rotation angles. Shows how to position and
    rotate individual text elements using TextBuilder for precise control.

    Args:
        outfile (str): Path where the PDF with rotated text will be saved.

    Returns:
        None: The function creates and saves a PDF file with rotated text fragments.

    Note:
        - Creates three text fragments with 0°, 45°, and 90° rotations
        - Uses Position class for precise text placement
        - Applies TimesNewRoman font with 12pt size
        - TextBuilder provides low-level control over text placement
        - Demonstrates individual fragment rotation capabilities

    Example:
        >>> rotate_text_inside_pdf_1("rotated_fragments.pdf")
        # Creates a PDF with text fragments at different rotation angles
    """

    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("main text")
        text_fragment_1.position = ap.text.Position(100, 600)
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Create rotated text fragment
        text_fragment_2 = ap.text.TextFragment("rotated text")
        text_fragment_2.position = ap.text.Position(200, 600)
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        text_fragment_2.text_state.rotation = 45
        # Create rotated text fragment
        text_fragment_3 = ap.text.TextFragment("rotated text")
        text_fragment_3.position = ap.text.Position(300, 600)
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        text_fragment_3.text_state.rotation = 90
        # create TextBuilder object
        builder = ap.text.TextBuilder(page)
        # Append the text fragment to the PDF page
        builder.append_text(text_fragment_1)
        builder.append_text(text_fragment_2)
        builder.append_text(text_fragment_3)

        # Save the document
        document.save(outfile)
```

## Putar Fragmen Teks Individual Di Dalam Paragraf di PDF

Putar fragmen teks individual dalam sebuah paragraf. Ini menunjukkan cara membuat paragraf multi-baris (TextParagraph) yang berisi beberapa fragmen (TextFragment), masing-masing dengan sudut rotasinya sendiri. Teknik ini berguna untuk membuat dokumen visual yang kaya yang menggabungkan teks berorientasi horizontal dan diagonal — misalnya, header bergaya, diagram, atau label beranotasi.

Membuat PDF bernama rotated_paragraph_fragments.pdf yang berisi paragraf dengan tiga baris teks, masing-masing baris diputar secara berbeda:

- baris pertama diputar 45°
- baris kedua tetap horizontal (0°)
- baris ketiga diputar -45°

1. Buat Dokumen PDF Baru.
1. Tambahkan halaman kosong tempat teks yang diputar akan muncul.
1. Buat TextParagraph.
1. Buat dan Konfigurasikan Fragmen Teks Pertama - Rotasi 45°.
1. Buat Fragmen Teks Kedua - Tanpa Rotasi.
1. Buat Fragmen Teks Ketiga - Rotasi 45°.
1. Tambahkan Fragmen Teks ke Paragraf.
1. Tambahkan Paragraf ke Halaman Menggunakan TextBuilder.
1. Simpan Dokumen.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def rotate_text_inside_pdf_2(outfile):
    """
    Implement text rotation using TextParagraph and TextBuilder with rotated fragments.

    Demonstrates how to create multi-line paragraphs containing individually
    rotated text fragments. Shows the combination of paragraph structure
    with fragment-level rotation control.

    Args:
        outfile (str): Path where the PDF with rotated paragraph fragments will be saved.

    Returns:
        None: The function creates and saves a PDF file with a paragraph containing rotated fragments.

    Note:
        - Creates a TextParagraph containing multiple text fragments
        - Individual fragments have different rotations: 45°, 0°, and -45°
        - Uses append_line to structure fragments within the paragraph
        - Demonstrates mixed rotation within a single paragraph
        - TextBuilder handles paragraph-level placement and rendering

    Example:
        >>> rotate_text_inside_pdf_2("rotated_paragraph_fragments.pdf")
        # Creates a PDF with a paragraph containing individually rotated text fragments
    """

    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        paragraph = ap.text.TextParagraph()
        paragraph.position = ap.text.Position(200, 600)
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Set rotation
        text_fragment_1.text_state.rotation = 45
        # Create text fragment
        text_fragment_2 = ap.text.TextFragment("main text")
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Create text fragment
        text_fragment_3 = ap.text.TextFragment("another rotated text")
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Set rotation
        text_fragment_3.text_state.rotation = -45
        # Append the text fragments to the paragraph
        paragraph.append_line(text_fragment_1)
        paragraph.append_line(text_fragment_2)
        paragraph.append_line(text_fragment_3)
        # Create TextBuilder object
        text_builder = ap.text.TextBuilder(page)
        # Append the text paragraph to the PDF page
        text_builder.append_paragraph(paragraph)

        # Save the document
        document.save(outfile)
```

## Putar Teks Menggunakan Paragraf Halaman di PDF

Metode sederhana untuk memutar teks dalam PDF menggunakan Aspose.PDF untuk Python via .NET.
Berbeda dengan pendekatan tingkat rendah menggunakan TextBuilder atau TextParagraph, metode ini menambahkan fragmen teks yang diputar langsung ke koleksi paragraf halaman (page.paragraphs). Metode ini ideal untuk kasus di mana Anda membutuhkan rotasi teks dasar tetapi tidak memerlukan penempatan yang tepat atau struktur paragraf. Pendekatan ini menyederhanakan pembuatan tata letak, secara otomatis menangani penempatan teks pada halaman sambil tetap memungkinkan kontrol rotasi teks individual.

Menghasilkan file bernama 'simple_rotated_text.pdf' yang berisi:

- fragmen teks horizontal utama dengan rotasi 0°
- fragmen diputar 315°
- fragmen diputar 270°

1. Inisialisasi dokumen PDF baru.
1. Buat halaman tempat teks yang diputar akan ditempatkan.
1. Buat Fragmen Teks Pertama - Tanpa Rotasi.
1. Buat Fragmen Teks Kedua - Rotasi 315°.
1. Buat Fragmen Teks Ketiga - Rotasi 270°.
1. Tambahkan Fragmen Teks secara Langsung ke Paragraf Halaman.
1. Simpan Dokumen PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def rotate_text_inside_pdf_3(outfile):
    """
    Implement text rotation using TextFragment and Page.Paragraphs.

    Demonstrates a simplified approach to text rotation by adding rotated
    text fragments directly to the page's paragraph collection. Shows
    high-level text placement without TextBuilder complexity.

    Args:
        outfile (str): Path where the PDF with rotated text will be saved.

    Returns:
        None: The function creates and saves a PDF file with rotated text using page paragraphs.

    Note:
        - Uses Page.Paragraphs for direct text fragment addition
        - Creates fragments with 0°, 315°, and 270° rotations
        - Simpler approach compared to TextBuilder method
        - Demonstrates automatic layout with rotated text elements
        - Good for basic rotation without precise positioning needs

    Example:
        >>> rotate_text_inside_pdf_3("simple_rotated_text.pdf")
        # Creates a PDF with rotated text using the simplified page paragraphs approach
    """

    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("main text")
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Create text fragment
        text_fragment_2 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Set rotation
        text_fragment_2.text_state.rotation = 315
        # Create text fragment
        text_fragment_3 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Set rotation
        text_fragment_3.text_state.rotation = 270
        page.paragraphs.add(text_fragment_1)
        page.paragraphs.add(text_fragment_2)
        page.paragraphs.add(text_fragment_3)

        # Save the document
        document.save(outfile)
```

## Putar Seluruh Paragraf dalam PDF

Perpustakaan kami menampilkan rotasi teks tingkat paragraf lanjutan dalam PDF. Tidak seperti rotasi tingkat fragmen (di mana setiap potongan teks diputar secara terpisah), metode ini memutar seluruh paragraf sebagai blok terpadu pada berbagai sudut.
Setiap paragraf berisi beberapa fragmen teks yang bergaya, dan seluruh paragraf diputar pada sudut tertentu — memungkinkan transformasi tata letak yang kompleks dan konsisten.
Ini ideal untuk tata letak artistik, watermark, atau PDF dengan desain berat di mana seluruh bagian teks perlu diarahkan ke berbagai arah.

Membuat 'rotated_paragraphs.pdf', yang berisi empat paragraf yang sepenuhnya bergaya dan diputar:

- masing-masing diputar pada sudut unik (45°, 135°, 225°, dan 315°)
- setiap paragraf memiliki tiga baris teks dengan latar belakang berwarna, garis bawah, dan gaya yang konsisten

1. Buat Dokumen PDF Baru.
1. Tambahkan halaman kosong untuk menampung paragraf yang diputar.
1. Iterasi untuk Membuat Beberapa Paragraf.
1. Buat dan Tempatkan Paragraf.
1. Buat Fragmen Teks dengan Pemformatan.
1. Terapkan Pemformatan Teks.
1. Tambahkan Fragmen Teks ke Paragraf.
1. Tambahkan Paragraf ke Halaman dengan Menggunakan TextBuilder.
1. Ulangi untuk Semua Empat Rotasi.
1. Simpan Dokumen PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def rotate_text_inside_pdf_4(outfile):
    """
    Implement whole paragraph rotation using TextParagraph and TextBuilder.

    Demonstrates advanced text rotation by rotating entire paragraphs at
    different angles. Creates multiple styled paragraphs with comprehensive
    formatting and rotates each paragraph as a complete unit.

    Args:
        outfile (str): Path where the PDF with rotated paragraphs will be saved.

    Returns:
        None: The function creates and saves a PDF file with fully rotated paragraphs.

    Note:
        - Creates 4 paragraphs rotated at 45°, 135°, 225°, and 315°
        - Each paragraph contains multiple formatted text fragments
        - Applies comprehensive styling: colors, backgrounds, underlines
        - Demonstrates paragraph-level rotation vs. fragment-level rotation
        - Shows complex multi-line content with consistent rotation
        - Uses loop to create systematic rotation pattern

    Example:
        >>> rotate_text_inside_pdf_4("rotated_paragraphs.pdf")
        # Creates a PDF with complete paragraphs rotated at different angles
    """

    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        for i in range(4):
            paragraph = ap.text.TextParagraph()
            paragraph.position = ap.text.Position(200, 600)
            # Specify rotation
            paragraph.rotation = i * 90 + 45
            # Create text fragment
            text_fragment_1 = ap.text.TextFragment("Paragraph Text")
            # Create text fragment
            text_fragment_1.text_state.font_size = 12
            text_fragment_1.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
            text_fragment_1.text_state.background_color = ap.Color.light_gray
            text_fragment_1.text_state.foreground_color = ap.Color.blue
            # Create text fragment
            text_fragment_2 = ap.text.TextFragment("Second line of text")
            # Set text properties
            text_fragment_2.text_state.font_size = 12
            text_fragment_2.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
            text_fragment_2.text_state.background_color = ap.Color.light_gray
            text_fragment_2.text_state.foreground_color = ap.Color.blue
            # Create text fragment
            text_fragment_3 = ap.text.TextFragment("And some more text...")
            # Set text properties
            text_fragment_3.text_state.font_size = 12
            text_fragment_3.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
            text_fragment_3.text_state.background_color = ap.Color.light_gray
            text_fragment_3.text_state.foreground_color = ap.Color.blue
            text_fragment_3.text_state.underline = True
            paragraph.append_line(text_fragment_1)
            paragraph.append_line(text_fragment_2)
            paragraph.append_line(text_fragment_3)
            # Create TextBuilder object
            builder = ap.text.TextBuilder(page)
            # Append the text fragment to the PDF page
            builder.append_paragraph(paragraph)

        # Save the document
        document.save(outfile)
```
