---
title: Pemformatan Teks dalam PDF menggunakan Python
linktitle: Pemformatan Teks dalam PDF
type: docs
weight: 70
url: /id/python-net/text-formatting-inside-pdf/
description: Jelajahi opsi pemformatan teks dalam file PDF di Python menggunakan Aspose.PDF untuk penataan dokumen yang disesuaikan.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara mengedit Teks dalam PDF dengan Python
Abstract: Artikel ini memberikan panduan komprehensif tentang berbagai teknik pemformatan teks dalam dokumen PDF menggunakan Aspose.PDF untuk Python via .NET. Ini mencakup beragam fungsi termasuk menambahkan indentasi baris, membuat batas teks, menggarisbawahi teks, dan menambahkan teks coret, di antara lain.
---

## Baris dan Spasi Karakter

### Menggunakan Spasi Baris

#### Cara Memformat Teks dengan Spasi Baris Kustom di Python - Kasus Sederhana

Aspose.PDF untuk Python menggambarkan pendekatan sederhana untuk mengontrol tata letak teks dan keterbacaan melalui penyesuaian spasi baris.

Potongan kode kami menunjukkan cara mengontrol spasi baris dalam dokumen PDF. Ia membaca teks dari file (atau menggunakan pesan cadangan), menerapkan ukuran font dan spasi baris kustom, dan menambahkan teks yang diformat ke halaman baru dalam PDF.

1. Buat dokumen PDF baru.
1. Muat teks sumber.
1. Inisialisasi objek TextFragment dan tetapkan teks yang dimuat ke dalamnya.
1. Atur properti font dan spasi untuk teks. Nilai-nilai ini menentukan seberapa rapat atau longgar baris teks terlihat:
- Ukuran font: 12 poin
- Spasi baris: 16 poin
1. Sisipkan fragmen teks yang diformat ke dalam koleksi paragraf halaman.
1. Simpan dokumen.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def specify_line_spacing_simple_case(outfile):
    """
    Specify custom line spacing for text in a PDF document.

    Creates a PDF document with text that has custom line spacing applied.
    Loads text content from an external file and applies 16-point line spacing
    to improve readability and text layout.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Attempts to load text from "lorem.txt" file in DATA_DIR
        - Falls back to default message if file doesn't exist
        - Font size: 12 points
        - Line spacing: 16 points (increased from default for better readability)
        - Demonstrates basic line spacing control in PDF text formatting

    Example:
        >>> specify_line_spacing_simple_case("line_spacing.pdf")
        # Creates a PDF with custom 16-point line spacing
    """

    document = ap.Document()
    page = document.pages.add()

    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    text = (
        open(lorem_path, "r", encoding="utf-8").read()
        if os.path.exists(lorem_path)
        else "Lorem ipsum text not found."
    )

    text_fragment = ap.text.TextFragment(text)
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.line_spacing = 16
    page.paragraphs.add(text_fragment)

    document.save(outfile)
```

#### Cara Memformat Teks dengan Spasi Baris Kustom di Python - Kasus Spesifik

Mari kita lihat cara menerapkan berbagai mode spasi baris dalam dokumen PDF menggunakan font TrueType (TTF) kustom.
Ia memuat teks dari file, menyematkan font tertentu, dan merender teks yang sama dua kali pada halaman PDF—setiap kali menggunakan mode spasi baris yang berbeda:

- mode FONT_SIZE: Spasi baris sama dengan ukuran font.
- mode FULL_SIZE: Spasi baris memperhitungkan tinggi penuh font, termasuk ascender dan descender.

Contoh ini menunjukkan bagaimana perilaku spasi baris dapat bervariasi tergantung pada mode yang dipilih.

1. Buat dokumen PDF baru.
1. Tentukan jalur untuk file font kustom dan file sumber teks.
1. Muat konten teks.
1. Buka font kustom.
1. Buat dan konfigurasikan TextFragment pertama (mode FONT_SIZE). Atur line_spacing ke 'TextFormattingOptions.LineSpacingMode.FONT_SIZE', yang berarti spasi baris sama dengan ukuran font.
1. Buat dan konfigurasikan TextFragment kedua (mode FULL_SIZE). Atur line_spacing ke 'TextFormattingOptions.LineSpacingMode.FULL_SIZE', yang menggunakan tinggi penuh font.
1. Tambahkan kedua fragmen teks ke halaman PDF yang sama.
1. Simpan dokumen selesai ke lokasi output yang ditentukan.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def specify_line_spacing_specific_case(outfile):
    """
    Create a PDF document demonstrating different line spacing modes with custom font.
    This function creates a PDF with two text fragments using the same custom TTF font
    but different line spacing modes to demonstrate the visual differences between
    FONT_SIZE and FULL_SIZE line spacing options.
    Args:
        outfile (str): Path where the output PDF file will be saved.
    Notes:
        - Requires 'HPSimplified.ttf' font file in DATA_DIR
        - Requires 'lorem.txt' text file in DATA_DIR for content
        - Falls back to default text if lorem.txt is not found
        - First fragment uses FONT_SIZE line spacing mode
        - Second fragment uses FULL_SIZE line spacing mode
    Dependencies:
        - aspose.pdf (ap) library
        - os module for file path operations
        - DATA_DIR constant must be defined
    """

    document = ap.Document()
    page = document.pages.add()

    font_file = os.path.join(DATA_DIR, "HPSimplified.ttf")
    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    text = (
        open(lorem_path, "r", encoding="utf-8").read()
        if os.path.exists(lorem_path)
        else "Lorem ipsum text not found."
    )

    with open(font_file, "rb") as font_stream:
        font = ap.text.FontRepository.open_font(font_stream, ap.text.FontTypes.TTF)

        fragment1 = ap.text.TextFragment(text)
        fragment1.text_state.font = font
        fragment1.text_state.formatting_options = ap.text.TextFormattingOptions()
        fragment1.text_state.formatting_options.line_spacing = (
            ap.text.TextFormattingOptions.LineSpacingMode.FONT_SIZE
        )
        page.paragraphs.add(fragment1)

        fragment2 = ap.text.TextFragment(text)
        fragment2.text_state.font = font
        fragment2.text_state.formatting_options = ap.text.TextFormattingOptions()
        fragment2.text_state.formatting_options.line_spacing = (
            ap.text.TextFormattingOptions.LineSpacingMode.FULL_SIZE
        )
        page.paragraphs.add(fragment2)

    document.save(outfile)
```

![Dokumen PDF menampilkan teks dengan spasi baris kustom yang menunjukkan spasi 16 poin antar baris untuk meningkatkan keterbacaan dan pemformatan tata letak teks](line_spacing.png)

### Menggunakan Spasi Karakter

#### Cara mengontrol spasi karakter dalam teks PDF menggunakan kelas TextFragment

Spasi karakter menentukan jarak antara karakter individu dalam satu baris teks—berguna untuk penyetelan halus tampilan teks atau mencapai efek tipografi tertentu.

1. Menginisialisasi objek Document baru dan menambahkan halaman kosong untuk menempatkan teks.
1. Definisikan Fragment Generator. Mengimplementasikan fungsi bantuan make_fragment(spacing):
- buat TextFragment dengan teks contoh.
- atur font.
1. Tambahkan fragmen teks dengan nilai spasi yang berbeda.
1. Simpan Document.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def character_spacing_using_text_fragment(outfile):
    """
    Demonstrate character spacing control using TextFragment objects.

    Creates a PDF document showing different character spacing values applied
    to text fragments. Each line demonstrates progressively increased character
    spacing to illustrate the visual effect on text appearance.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Creates multiple TextFragment objects with varying character spacing
        - Character spacing values: 0, 1, 2, 3, and 4 points
        - Font: Times Roman, 12 points
        - Each fragment is positioned on a new line for comparison
        - Character spacing affects only horizontal letter spacing
        - Higher values create more space between individual characters

    Example:
        >>> character_spacing_using_text_fragment("char_spacing_fragment.pdf")
        # Creates a PDF showing progressive character spacing effects
    """
    document = ap.Document()
    page = document.pages.add()

    def make_fragment(spacing):
        fragment = ap.text.TextFragment("Sample Text with character spacing")
        fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
        fragment.text_state.font_size = 14
        fragment.text_state.character_spacing = spacing
        return fragment

    page.paragraphs.add(make_fragment(2.0))
    page.paragraphs.add(make_fragment(1.0))
    page.paragraphs.add(make_fragment(0.75))

    document.save(outfile)
```

![dokumen PDF yang menampilkan tiga baris teks identik Sample Text dengan jarak karakter yang menunjukkan secara bertahap jarak karakter yang lebih rapat dari atas ke bawah, dengan baris pertama memiliki jarak antar huruf yang lebih lebar, baris tengah memiliki jarak sedang, dan baris bawah memiliki jarak karakter terdekat, menggambarkan efek visual dari nilai jarak karakter yang berbeda dalam pemformatan teks PDF](character_spacing_simple.png)

#### Cara mengontrol jarak karakter dalam teks PDF menggunakan TextParagraph dan TextBuilder

Aspose.PDF memungkinkan penerapan jarak karakter khusus saat menambahkan teks ke dokumen PDF menggunakan TextParagraph dan TextBuilder.
Ini mendefinisikan area spesifik pada halaman, mengkonfigurasi pembungkus teks, dan merender fragmen teks dengan jarak antar karakter yang disesuaikan.

Menggunakan TextParagraph ideal ketika Anda memerlukan kontrol yang tepat atas penempatan dan tata letak teks, seperti saat membangun blok teks terstruktur atau multi-kolom.

1. Buat dokumen PDF baru.
1. Inisialisasi instance TextBuilder untuk halaman.
1. Buat dan konfigurasikan TextParagraph.
- Atur mode pembungkus kata ke 'TextFormattingOptions.WordWrapMode.BY_WORDS'.
1. Buat TextFragment dengan jarak karakter khusus.
- Buat TextFragment baru dan atur teksnya (misalnya, "Sample Text with character spacing").
- Tentukan atribut font seperti Arial dan ukuran font 14 pt.
- Terapkan jarak karakter = 2.0, yang meningkatkan ruang antar karakter.
1. Tambahkan TextFragment ke TextParagraph.
1. Tambahkan TextParagraph ke halaman.
1. Simpan dokumen PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def character_spacing_using_text_paragraph(outfile):
    """
    Demonstrate character spacing control using TextParagraph objects.

    Creates a PDF document with text paragraph that has custom character spacing
    applied. Shows how to set character spacing at the paragraph level and
    demonstrates the visual effect on text layout.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses TextParagraph for paragraph-level formatting
        - Character spacing: 2.0 points
        - Font: Times Roman, 12 points
        - Demonstrates paragraph-based character spacing control
        - Character spacing applies to all text within the paragraph
        - Alternative approach to fragment-based character spacing

    Example:
        >>> character_spacing_using_text_paragraph("char_spacing_paragraph.pdf")
        # Creates a PDF with paragraph-level character spacing
    """
    document = ap.Document()
    page = document.pages.add()

    builder = ap.text.TextBuilder(page)
    paragraph = ap.text.TextParagraph()
    paragraph.rectangle = ap.Rectangle(100, 700, 500, 750, True)
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    fragment = ap.text.TextFragment("Sample Text with character spacing")
    fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    fragment.text_state.font_size = 14
    fragment.text_state.character_spacing = 2.0

    paragraph.append_line(fragment)
    builder.append_paragraph(paragraph)
    document.save(outfile)
```

## Membuat Daftar

Saat bekerja dengan file PDF, Anda mungkin perlu menampilkan informasi terstruktur seperti daftar — apakah itu berbutir, bernomor, atau diformat dengan HTML atau LaTeX.
Aspose.PDF untuk Python via .NET menyediakan beberapa cara fleksibel untuk membuat dan memformat daftar langsung dalam dokumen PDF Anda, memberi Anda kontrol penuh atas tata letak, font, dan gaya.

Artikel ini menunjukkan berbagai pendekatan untuk membuat daftar dalam PDF, mulai dari pemformatan teks biasa hingga rendering HTML dan LaTeX tingkat lanjut. Setiap metode melayani kasus penggunaan tertentu — apakah Anda lebih menyukai kontrol programatik yang tepat atau penataan berbasis markup yang mudah.

Di akhir artikel ini, Anda akan mengetahui cara:

- Membuat daftar bullet dan bernomor kustom menggunakan TextParagraph dan TextBuilder.

- Gunakan fragmen HTML (HtmlFragment) untuk dengan mudah merender daftar '<ul>' dan '<ol>' dalam PDF.

- Manfaatkan fragmen LaTeX (TeXFragment) untuk pemformatan daftar matematika atau ilmiah.

- Kontrol pembungkus teks, gaya font, dan posisi tata letak dalam halaman.

- Memahami perbedaan antara konstruksi daftar manual dan pendekatan berbasis markup.

### Buat daftar bullet

Buat daftar berbutir kustom dalam PDF menggunakan TextParagraph dan TextBuilder, tanpa bergantung pada pemformatan HTML atau LaTeX.
Setiap item daftar diawali dengan karakter bullet (•) dan ditambahkan sebagai TextFragment terpisah.

1. Inisialisasi objek Document dan tambahkan halaman kosong.
1. Definisikan list Python berisi string yang akan dikonversi menjadi poin bullet.
1. Buat TextBuilder dan TextParagraph.
1. Gunakan 'TextBuilder' untuk menambahkan paragraf yang telah dikonfigurasi ke halaman.
1. Simpan dokumen PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_bullet_list(outfile):
    """
    Create a PDF document with a bullet list using plain text formatting.
    This function generates a PDF document containing a bullet list with predefined items.
    The list is formatted with bullet points, uses Times New Roman font, and includes
    text wrapping behavior for longer items.
    Args:
        outfile (str): The file path where the PDF document will be saved.
    Returns:
        None: The function saves the document to the specified file path.
    Note:
        The bullet list is positioned within a rectangle at coordinates (80, 200, 400, 800)
        and uses word wrapping mode for text formatting.
    """

    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item in the list",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]

    builder = ap.text.TextBuilder(page)
    paragraph = ap.text.TextParagraph()
    paragraph.rectangle = ap.Rectangle(80, 200, 400, 800, True)
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    for item in items:
        fragment = ap.text.TextFragment("• " + item)
        fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
        fragment.text_state.font_size = 12
        paragraph.append_line(fragment)

    builder.append_paragraph(paragraph)
    document.save(outfile)
```

### Buat daftar bernomor

Buat daftar bernomor (berurutan) kustom dalam PDF menggunakan TextParagraph dan TextBuilder, tanpa bergantung pada pemformatan HTML atau LaTeX.
Setiap item daftar diawali dengan nomornya (mis., 1., 2.) dan ditambahkan sebagai TextFragment terpisah.

1. Inisialisasi objek Document dan tambahkan halaman kosong.
1. Definisikan list Python berisi string yang akan dikonversi menjadi item daftar bernomor.
1. Buat TextBuilder dan TextParagraph.
1. Tambahkan setiap item sebagai TextFragment dengan nomor.
1. Gunakan TextBuilder untuk menambahkan paragraf yang telah dikonfigurasi ke halaman.
1. Simpan dokumen PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_numbered_list(outfile):
    """
    Create a numbered list in a PDF document using plain text formatting.
    This function generates a PDF document containing a numbered list with predefined
    items. The list is formatted with Times New Roman font and includes text wrapping
    by words within a specified rectangular area on the page.
    Args:
        outfile (str): The file path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified file path but does
              not return any value.
    Note:
        - Uses Aspose.PDF library (imported as 'ap')
        - List items are hardcoded within the function
        - Font: Times New Roman, size 12
        - Text wrapping: BY_WORDS mode
        - Rectangle bounds: (80, 200, 400, 800)
    """

    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item in the list",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]

    builder = ap.text.TextBuilder(page)
    paragraph = ap.text.TextParagraph()
    paragraph.rectangle = ap.Rectangle(80, 200, 400, 800, True)
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    for i, item in enumerate(items):
        fragment = ap.text.TextFragment(f"{i + 1}. {item}")
        fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
        fragment.text_state.font_size = 12
        paragraph.append_line(fragment)

    builder.append_paragraph(paragraph)
    document.save(outfile)
```

### Buat versi daftar bullet HTML

Perpustakaan kami menunjukkan cara membuat daftar berbutir (tidak berurutan) dalam dokumen PDF menggunakan fragmen HTML. Ini mengonversi list Python berisi string menjadi elemen HTML `<ul>` dan menyisipkannya ke halaman PDF sebagai HtmlFragment. Menggunakan fragmen HTML memungkinkan Anda memanfaatkan fitur pemformatan HTML (seperti daftar, tebal, miring) secara langsung di PDF.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Siapkan item-item daftar.
1. Konversi daftar menjadi daftar HTML tidak berurutan.
- Gunakan tag `<ul>` untuk daftar tidak berurutan (bullet).
- Bungkus setiap item dengan tag 'li' menggunakan list comprehension.
1. Buat sebuah HtmlFragment. Konversi string HTML menjadi objek HtmlFragment yang dapat ditambahkan ke halaman PDF.
1. Sisipkan HtmlFragment ke dalam koleksi paragraf halaman.
1. Simpan dokumen PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_bullet_list_html_version(outfile):
    """
    Create a bulleted list using HTML formatting in a PDF document.

    Generates a PDF with an unordered (bulleted) list created using HTML markup.
    Demonstrates how to use HtmlFragment to embed HTML list structures directly
    into PDF documents with proper formatting and styling.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses HTML <ul> and <li> tags for list structure
        - Items are predefined with sample content
        - HtmlFragment automatically handles HTML rendering
        - Lists maintain proper bullet formatting and indentation
        - Simpler alternative to manual list creation with TextFragments
        - Supports nested lists and HTML styling if needed

    Example:
        >>> create_bullet_list_html_version("bullet_list_html.pdf")
        # Creates a PDF with HTML-formatted bulleted list
    """

    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item in the list",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]
    html_list = "<ul>" + "".join([f"<li>{item}</li>" for item in items]) + "</ul>"
    html_fragment = ap.HtmlFragment(html_list)
    page.paragraphs.add(html_fragment)
    document.save(outfile)
```

![Daftar berpoin yang ditampilkan dalam dokumen PDF memperlihatkan empat item: Item pertama dalam daftar, Item kedua dengan teks lebih banyak untuk menunjukkan perilaku pembungkusan, Item ketiga, dan Item keempat. Setiap item diawali dengan titik peluru standar dan memperlihatkan rendering daftar berformat HTML di dalam struktur PDF dengan indentasi dan spasi yang tepat.](bullet_list_html.png)

### Buat versi daftar bernomor HTML

Buat daftar bernomor (ordered) dalam dokumen PDF menggunakan fragmen HTML. Ini mengonversi list Python berisi string menjadi elemen HTML `<ol>` dan menyisipkannya ke dalam halaman PDF sebagai HtmlFragment.

Menggunakan fragmen HTML memungkinkan Anda mengintegrasikan fitur pemformatan berbasis HTML, seperti daftar bernomor, tebal, miring, dan lainnya, langsung ke dalam PDF Anda.

1. Buat dokumen PDF baru dan tambahkan sebuah halaman.
1. Siapkan item-item daftar.
1. Konversi daftar menjadi daftar terurut HTML.
- Gunakan tag `<ol>` untuk daftar bernomor.
- Bungkus tiap item dengan tag 'li' menggunakan list comprehension.
1. Konversi string HTML menjadi objek HtmlFragment yang dapat ditambahkan ke halaman PDF.
1. Sisipkan HtmlFragment ke dalam koleksi paragraf halaman.
1. Simpan dokumen PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_numbered_list_html_version(outfile):
    """
    Create a numbered list using HTML formatting in a PDF document.

    Generates a PDF with an ordered (numbered) list created using HTML markup.
    Demonstrates how to use HtmlFragment to embed HTML ordered list structures
    directly into PDF documents with automatic numbering and formatting.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses HTML <ol> and <li> tags for ordered list structure
        - Items are predefined with sample content
        - HtmlFragment automatically handles HTML rendering and numbering
        - Lists maintain proper numeric formatting and indentation
        - Numbers are automatically generated (1, 2, 3, etc.)
        - Supports nested lists and custom numbering styles if needed

    Example:
        >>> create_numbered_list_html_version("numbered_list_html.pdf")
        # Creates a PDF with HTML-formatted numbered list
    """

    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item in the list",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]
    html_list = "<ol>" + "".join([f"<li>{item}</li>" for item in items]) + "</ol>"
    html_fragment = ap.HtmlFragment(html_list)
    page.paragraphs.add(html_fragment)
    document.save(outfile)
```

![Daftar bernomor yang ditampilkan dalam dokumen PDF memperlihatkan empat item yang secara otomatis dinomori: 1. Item pertama dalam daftar, 2. Item kedua dengan teks lebih banyak untuk menunjukkan perilaku pembungkusan, 3. Item ketiga, dan 4. Item keempat. Daftar ini memperlihatkan rendering daftar terurut berformat HTML dalam struktur PDF dengan urutan numerik yang tepat, indentasi, dan spasi antar item.](numbered_list_html.png)

### Buat versi daftar berpoin LaTeX

Buat daftar berpoin (tidak berurutan) dalam PDF menggunakan fragmen LaTeX (TeXFragment). Ini mengonversi list Python berisi string menjadi lingkungan LaTeX itemize dan menyisipkannya ke dalam halaman PDF. Menggunakan fragmen LaTeX ideal ketika Anda ingin menampilkan rumus matematika, simbol, atau daftar terstruktur dengan pemformatan yang presisi.

1. Buat dokumen PDF baru dan tambahkan sebuah halaman.
1. Tentukan list Python berisi string yang akan menjadi poin bullet dalam lingkungan LaTeX itemize.
1. Konversi list menjadi lingkungan LaTeX itemize:
- Bungkus item-item dengan \begin{itemize} dan \end{itemize}.
- Setiap item diawali dengan \item menggunakan list comprehension.
1. Konversi string LaTeX menjadi objek TeXFragment yang dapat dirender dalam PDF.
1. Tambahkan fragmen LaTeX ke halaman.
1. Simpan dokumen PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_bullet_list_latex_version(outfile):
    """
    Create a bulleted list using LaTeX formatting in a PDF document.

    Generates a PDF with an unordered list created using LaTeX markup.
    Demonstrates how to use TeXFragment to embed LaTeX itemize environments
    directly into PDF documents with proper mathematical and scientific formatting.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses LaTeX \\begin{itemize} and \\item commands
        - TeXFragment handles LaTeX compilation and rendering
        - Supports mathematical expressions and scientific notation
        - Lists maintain proper bullet formatting and indentation
        - More powerful than HTML for mathematical content
        - Can include LaTeX math modes and special symbols

    Example:
        >>> create_bullet_list_latex_version("bullet_list_latex.pdf")
        # Creates a PDF with LaTeX-formatted bulleted list
    """

    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]
    tex_list = (
        "Lists are easy to create: \\begin{itemize}"
        + "".join([f"\\item {i}" for i in items])
        + "\\end{itemize}"
    )
    tex_fragment = ap.TeXFragment(tex_list)
    page.paragraphs.add(tex_fragment)
    document.save(outfile)
```

![Daftar berpoin yang ditampilkan dalam PDF memperlihatkan pemformatan yang dirender LaTeX dengan teks Daftar mudah dibuat: diikuti oleh empat item berbullet: Item pertama, Item kedua dengan teks lebih banyak untuk menunjukkan perilaku pembungkusan, Item ketiga, dan Item keempat. Daftar ini memperlihatkan tipografi LaTeX profesional dengan format bullet yang tepat, spasi konsisten, dan kemampuan pembungkusan teks dalam tata letak dokumen PDF yang bersih.](bullet_list_latex.png)

### Buat versi daftar bernomor LaTeX

Buat daftar bernomor (ordered) dalam PDF menggunakan fragmen LaTeX (TeXFragment). Ini mengonversi list Python berisi string menjadi lingkungan LaTeX enumerate dan menyisipkannya ke dalam halaman PDF. Menggunakan fragmen LaTeX ideal ketika Anda menginginkan pemformatan yang presisi, daftar terstruktur, atau notasi matematika dalam PDF.

1. Buat dokumen PDF baru dan tambahkan sebuah halaman.
1. Tentukan list Python berisi string yang akan menjadi item bernomor dalam lingkungan LaTeX enumerate.
1. Konversi list menjadi lingkungan LaTeX enumerate.
1. Konversi string LaTeX menjadi objek TeXFragment yang dapat dirender dalam PDF.
1. Tambahkan fragmen LaTeX ke halaman.
1. Simpan dokumen PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_numbered_list_latex_version(outfile):
    """Create a numbered list using LaTeX."""

    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]
    tex_list = (
        "Lists are easy to create: \\begin{enumerate}"
        + "".join([f"\\item {i}" for i in items])
        + "\\end{enumerate}"
    )
    tex_fragment = ap.TeXFragment(tex_list)
    page.paragraphs.add(tex_fragment)
    document.save(outfile)
```

![Daftar bernomor yang ditampilkan dalam PDF memperlihatkan pemformatan yang dirender LaTeX dengan item 1. Item pertama, 2. Item kedua dengan teks lebih banyak untuk menunjukkan perilaku pembungkusan, 3. Item ketiga, dan 4. Item keempat, didahului oleh teks Daftar mudah dibuat](numbered_list_latex.png)

## Catatan Kaki dan Catatan Akhir

### Tambahkan Catatan Kaki

Catatan kaki digunakan untuk merujuk catatan di dalam tubuh dokumen dengan menempatkan nomor superskrip berurutan di sebelah teks yang relevan. Nomor-nomor ini sesuai dengan catatan rinci yang biasanya diindentasi dan diletakkan di bagian bawah halaman yang sama, memberikan konteks tambahan, sitasi, atau komentar.

Tambahkan catatan kaki ke fragmen teks dalam dokumen PDF menggunakan Aspose.PDF untuk Python via .NET. Catatan kaki berguna untuk memberikan informasi tambahan, sitasi, atau klarifikasi tanpa memadati konten utama. Metode ini memastikan catatan kaki terintegrasi secara visual dan struktural ke dalam tata letak PDF.

1. Buat Dokumen Baru.
1. Buat TextFragment dengan konten utama.
1. Tambahkan Teks Inline. Buat TextFragment lain yang melanjutkan dalam paragraf yang sama.
1. Simpan Dokumen.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_footnote(outfile):
    """Add footnote to a PDF document."""

    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with a footnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.foot_note = ap.Note("This is the footnote content.")
    page.paragraphs.add(text_fragment)

    inline_text = ap.text.TextFragment(
        " This is another text after footnote in the same paragraph."
    )
    inline_text.is_in_line_paragraph = True
    inline_text.text_state.font = ap.text.FontRepository.find_font("Arial")
    inline_text.text_state.font_size = 14
    page.paragraphs.add(inline_text)

    document.save(outfile)
```

### Tambahkan Catatan Kaki dengan Gaya Kustom dalam PDF

1. Inisialisasi dokumen PDF baru dan tambahkan halaman kosong.
1. Buat Fragmen Teks Utama.
1. Buat dan Gaya Catatan Kaki (Font, Ukuran, Warna, Gaya).
1. Sisipkan fragmen teks ber-gaya dengan catatan kaki ke dalam halaman.
1. Tambahkan fragmen teks lain tanpa catatan kaki.
1. Simpan Dokumen.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_footnote_custom_text_style(outfile):
    """Add footnote with custom text style."""

    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with a footnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14

    note = ap.Note("This is the footnote content with custom text style.")
    note.text_state = ap.text.TextState()
    note.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    note.text_state.font_size = 10
    note.text_state.foreground_color = ap.Color.red
    note.text_state.font_style = ap.text.FontStyles.ITALIC
    text_fragment.foot_note = note

    page.paragraphs.add(text_fragment)

    another_text = ap.text.TextFragment(" This is another text without footnote.")
    another_text.text_state.font = ap.text.FontRepository.find_font("Arial")
    another_text.text_state.font_size = 14
    page.paragraphs.add(another_text)

    document.save(outfile)
```

### Tambahkan Catatan Kaki dengan Simbol Kustom di PDF

Tambahkan catatan kaki ke fragmen teks dalam dokumen PDF menggunakan Aspose.PDF untuk Python via .NET, dengan kemampuan menyesuaikan simbol penanda catatan kaki.

1. Buat Dokumen PDF dan Halaman.
1. Tambahkan Fragmen Teks pertama dengan Simbol Catatan Kaki Kustom.
1. Tambahkan Fragmen Teks lainnya yang melanjutkan paragraf tanpa catatan kaki.
1. Tambahkan Fragmen Teks kedua dengan Catatan Kaki Default.
1. Simpan Dokumen.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_footnote_custom_text(outfile):
    """
    Add footnote with custom text marker to a PDF document.
    Creates a PDF document with text fragments that include footnotes with custom
    styling. The function demonstrates how to add footnotes with custom text markers
    and standard footnotes to different text fragments within the same document.
    Args:
        outfile (str): The output file path where the PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file.
    Example:
        add_footnote_custom_text("output_with_footnotes.pdf")
    Note:
        The document will contain:
        - Text with a custom footnote marker ("*")
        - Text without footnotes
        - Text with a standard footnote
    """

    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with a footnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14

    note = ap.Note("This is the footnote content with custom text style.")
    note.text = "*"
    text_fragment.foot_note = note
    page.paragraphs.add(text_fragment)

    another_text = ap.text.TextFragment(" This is another text without footnote.")
    another_text.text_state.font = ap.text.FontRepository.find_font("Arial")
    another_text.text_state.font_size = 14
    page.paragraphs.add(another_text)

    text_fragment = ap.text.TextFragment("This is a sample text with a footnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.foot_note = ap.Note("This is the footnote content.")
    page.paragraphs.add(text_fragment)

    document.save(outfile)
```

### Tambahkan Catatan Kaki dengan Gaya Garis Kustom di PDF

Sesuaikan tampilan visual garis catatan kaki dalam dokumen PDF menggunakan perpustakaan Python. Menyesuaikan garis catatan kaki meningkatkan kejelasan visual dan memungkinkan konsistensi gaya dalam dokumen seperti laporan, makalah akademik, dan publikasi beranotasi.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Tentukan gaya garis kustom untuk penghubung catatan kaki (warna, lebar, dan pola dash).
1. Tambahkan beberapa fragmen teks dengan catatan kaki.
1. Simpan dokumen akhir.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_footnote_with_custom_line_style(outfile):
    """
    Add footnotes with custom line style to a PDF document.
    Creates a PDF document with text fragments that have footnotes and applies
    a custom line style for the footnote separator line. The custom style includes
    red color, increased line width, and dashed pattern.
    Args:
        outfile (str): Path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file.
    Example:
        >>> add_footnote_with_custom_line_style("output.pdf")
        # Creates a PDF with footnoted text and custom separator line styling
    """

    document = ap.Document()
    page = document.pages.add()

    # Define custom line style
    graph_info = ap.GraphInfo()
    graph_info.line_width = 2
    graph_info.color = ap.Color.red
    graph_info.dash_array = [3]
    graph_info.dash_phase = 1
    page.note_line_style = graph_info

    # First text fragment with footnote
    text1 = ap.text.TextFragment("This is a sample text with a footnote.")
    text1.foot_note = ap.Note("foot note for text 1")
    page.paragraphs.add(text1)

    # Second text fragment with footnote
    text2 = ap.text.TextFragment("This is yet another sample text with a footnote.")
    text2.foot_note = ap.Note("foot note for text 2")
    page.paragraphs.add(text2)

    document.save(outfile)
```

### Tambahkan Catatan Kaki dengan Gambar dan Tabel di PDF

Bagaimana memperkaya catatan kaki dalam dokumen PDF dengan menyematkan gambar, teks bergaya, dan tabel menggunakan Aspose.PDF untuk Python via .NET?

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Tambahkan fragmen teks dengan catatan kaki yang terlampir.
1. Sematkan gambar, teks bergaya, dan tabel di dalam catatan kaki.
1. Simpan Dokumen.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_footnote_with_image_and_table(outfile):
    """
    Add a footnote containing an image and table to a PDF document.
    Creates a new PDF document with sample text that includes a footnote. The footnote
    contains three elements: an image (logo.jpg), descriptive text, and a simple table
    with two cells. The image is resized to 20x20 pixels and the footnote text uses
    a 20pt font size.
    Args:
        outfile (str): The file path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file.
    Note:
        - Requires the logo.jpg file to be present in the DATA_DIR directory
        - Uses the Aspose.PDF library (imported as 'ap')
        - The footnote is attached to the main text fragment on the page
    """

    document = ap.Document()
    page = document.pages.add()

    text = ap.text.TextFragment("This is a sample text with a footnote.")
    page.paragraphs.add(text)

    note = ap.Note()

    # Add image
    image_note = ap.Image()
    image_note.file = os.path.join(DATA_DIR, "logo.jpg")
    image_note.fix_height = 20
    image_note.fix_width = 20
    note.paragraphs.add(image_note)

    # Add text
    text_note = ap.text.TextFragment("This is the footnote content.")
    text_note.text_state.font_size = 20
    text_note.is_in_line_paragraph = True
    note.paragraphs.add(text_note)

    # Add table
    table = ap.Table()
    table.rows.add().cells.add("Cell 1,1")
    table.rows.add().cells.add("Cell 1,2")
    note.paragraphs.add(table)

    text.foot_note = note

    document.save(outfile)
```

### Menambahkan Catatan Akhir ke Dokumen PDF

Catatan Akhir adalah jenis sitasi yang mengarahkan pembaca ke bagian yang ditentukan di akhir dokumen, dimana mereka dapat menemukan referensi lengkap untuk kutipan, ide yang diparafrasekan, atau konten yang diringkas. Saat menggunakan catatan akhir, sebuah angka superskrip ditempatkan tepat setelah materi yang dirujuk, mengarahkan pembaca ke catatan yang bersesuaian di akhir makalah.

Potongan kode ini menunjukkan cara menambahkan catatan akhir ke fragmen teks dalam dokumen PDF. Tidak seperti catatan kaki, yang muncul dekat teks yang dirujuk, catatan akhir biasanya ditempatkan di akhir dokumen atau bagian. Metode ini juga mensimulasikan dokumen yang lebih panjang untuk memperlihatkan bagaimana catatan akhir berperilaku dalam konten yang diperluas.

1. Buat Dokumen PDF dan Halaman.
1. Tambahkan Fragmen Teks dengan Catatan Akhir.
1. Muat Konten Teks Eksternal.
1. Simulasikan Dokumen Panjang. Tambahkan teks yang dimuat berkali-kali untuk mensimulasikan dokumen yang lebih panjang.
1. Simpan Dokumen.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_endnote(outfile):
    """Add endnote to a PDF document.
    Creates a new PDF document with a text fragment containing an endnote,
    followed by additional lorem ipsum content to simulate a longer document.
    The endnote is attached to the first text fragment and will be displayed
    according to the PDF viewer's endnote handling.
    Args:
        outfile (str): The file path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file path.
    Note:
        This function requires the aspose-pdf library and assumes the existence
        of a DATA_DIR variable pointing to a directory containing 'lorem.txt'.
        If the lorem.txt file is not found, fallback text will be used.
    """

    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with an endnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.end_note = ap.Note("This is the EndNote content.")
    page.paragraphs.add(text_fragment)

    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    text_content = (
        open(lorem_path, encoding="utf-8").read()
        if os.path.exists(lorem_path)
        else "Lorem ipsum sample text not found."
    )

    # Simulate long text
    for _ in range(5):
        tf = ap.text.TextFragment(text_content)
        tf.text_state.font = ap.text.FontRepository.find_font("Arial")
        tf.text_state.font_size = 14
        page.paragraphs.add(tf)

    document.save(outfile)
```

### Tambahkan Catatan Akhir dengan Teks Penanda Kustom di PDF

Tambahkan catatan akhir ke fragmen teks dalam dokumen PDF, dengan simbol penanda kustom (misalnya "***"). Catatan akhir biasanya ditempatkan di akhir dokumen atau bagian dan berguna untuk memberikan konteks tambahan, sitasi, atau komentar.

1. Buat Dokumen PDF dan Halaman.
1. Tambahkan fragmen teks bergaya dengan catatan akhir.
1. Sesuaikan teks penanda catatan akhir.
1. Muat konten eksternal dari file .txt.
1. Simulasikan konten bentuk panjang untuk memperlihatkan penempatan catatan akhir.
1. Simpan dokumen PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_endnote_custom_text(outfile):
    """
    Add endnote with custom text marker to a PDF document.
    Creates a PDF document with a text fragment that contains an endnote with
    a custom marker ("***"). The document is populated with sample text content
    from a lorem.txt file, repeated multiple times to simulate a longer document.
    Args:
        outfile (str): Path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file path.
    Note:
        - Requires lorem.txt file in DATA_DIR for sample content
        - Falls back to default text if lorem.txt is not found
        - Uses Arial font with 14pt size for all text elements
        - The endnote marker is set to "***" instead of default numbering
    """

    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with an endnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.end_note = ap.Note("This is the EndNote content.")
    text_fragment.end_note.text = "***"
    page.paragraphs.add(text_fragment)

    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    text_content = (
        open(lorem_path, encoding="utf-8").read()
        if os.path.exists(lorem_path)
        else "Lorem ipsum sample text not found."
    )

    # Simulate long text
    for _ in range(5):
        tf = ap.text.TextFragment(text_content)
        tf.text_state.font = ap.text.FontRepository.find_font("Arial")
        tf.text_state.font_size = 14
        page.paragraphs.add(tf)

    document.save(outfile)
```

## Tata Letak & kontrol halaman

### Paksa Tabel Mulai pada Halaman Baru di PDF

Tambahkan konten spesifik untuk memulai pada halaman baru dalam dokumen PDF menggunakan Aspose.PDF untuk Python via .NET.
Dengan mengatur properti 'is_in_new_page', Anda dapat mengontrol tata letak dan struktur halaman secara tepat, memastikan bahwa bagian tertentu (seperti tabel, laporan, atau ringkasan) selalu dimulai pada halaman baru — ideal untuk pemformatan dokumen, laporan siap cetak, atau pembuatan output terorganisir.

1. Buat dan konfigurasikan tabel.
1. Tambahkan data ke tabel.
1. Paksa halaman baru untuk tabel. Ini memastikan tabel mulai di bagian atas halaman baru, bahkan jika ada konten yang sudah ada pada halaman saat ini.
1. Tambahkan tabel ke halaman. Gunakan 'page.paragraphs.add()' untuk menyertakan tabel dalam tata letak PDF.
1. Simpan dokumen.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def force_new_page(output_file_name):
    """
    Create a PDF document demonstrating forced page breaks with tables.

    Creates a PDF document with a table that is forced to start on a new page
    using the is_in_new_page property. This is useful for controlling page layout
    and ensuring specific content starts on fresh pages.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Creates a 3-column table with 5 rows of sample data
        - Table uses uniform column widths of 150 units each
        - All cells have borders for clear visual separation
        - is_in_new_page=True forces the table to start on a new page
        - Useful for reports, documents with sections, or content organization

    Example:
        >>> force_new_page("new_page_table.pdf")
        # Creates a PDF with a table that starts on a new page
    """
    # Create new PDF document
    document = ap.Document()
    page = document.pages.add()

    # Create a table
    table = ap.Table()
    table.column_widths = "150 150 150"
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL)

    # Add rows with sample data
    for i in range(5):
        row = table.rows.add()
        row.cells.add(f"Row {i + 1} - Col 1")
        row.cells.add(f"Row {i + 1} - Col 2")
        row.cells.add(f"Row {i + 1} - Col 3")

    # --- Key part: force table to start on a new PDF page ---
    table.is_in_new_page = True

    # Add table to page
    page.paragraphs.add(table)

    # Save the PDF
    document.save(output_file_name)
```

### Menggunakan Properti Inline Paragraph dalam PDF

Perpustakaan kami memungkinkan Anda menggunakan properti 'is_in_line_paragraph' untuk mengontrol alur inline antara teks dan gambar dalam PDF.
Biasanya, ketika Anda menambahkan elemen baru (seperti fragmen teks atau gambar), masing‑masing mulai pada baris baru atau paragraf baru.
Dengan mengatur 'is_in_line_paragraph = True', Anda dapat membuat elemen muncul pada baris yang sama atau dalam paragraf yang sama, menciptakan tata letak inline yang halus—sempurna untuk menggabungkan teks dan gambar secara inline, seperti menambahkan logo, ikon, atau simbol dalam kalimat.

Fragmen teks pertama, gambar, dan fragmen teks kedua muncul pada baris yang sama, membentuk paragraf inline yang berkelanjutan.
Fragmen teks ketiga memulai paragraf baru, menunjukkan perilaku pemutusan baris default.

1. Buat dokumen PDF baru.
1. Tambahkan fragmen teks pertama.
1. Sisipkan gambar inline.
1. Tambahkan teks inline lainnya.
1. Tambahkan paragraf baru.
1. Simpan PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def using_inline_paragraph_property(output_file_name):
    """
    Demonstrate inline paragraph behavior in PDF document layout.

    Creates a PDF document showing how the is_in_line_paragraph property affects
    the flow of text and images. Elements with this property continue the flow
    of the previous paragraph instead of starting a new one.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - First text fragment starts a new paragraph
        - Image with is_in_line_paragraph=True continues the same line
        - Second text fragment also continues the same paragraph line
        - Third text fragment starts a new paragraph (default behavior)
        - Demonstrates inline flow control for mixed content (text + images)
        - Image is resized to 30x30 pixels and flows inline with text

    Example:
        >>> using_inline_paragraph_property("inline_paragraph.pdf")
        # Creates a PDF demonstrating inline paragraph flow
    """
    # Create a PDF document
    document = ap.Document()
    page = document.pages.add()

    # --- First text fragment (normal paragraph) ---
    fragment1 = ap.text.TextFragment("This is the first part of the paragraph. ")
    fragment1.text_state.font = ap.text.FontRepository.find_font("Arial")
    fragment1.text_state.font_size = 14
    page.paragraphs.add(fragment1)

    # --- Inline image (continues same paragraph flow) ---
    image = ap.Image()
    image.is_in_line_paragraph = True  # Makes image inline with previous paragraph
    image.file = os.path.join(DATA_DIR, "logo.jpg")
    image.fix_height = 30
    image.fix_width = 30
    page.paragraphs.add(image)

    # --- Second inline text fragment (keeps same paragraph flow) ---
    fragment2 = ap.text.TextFragment("This is the second part of the same paragraph.")
    fragment2.is_in_line_paragraph = True
    fragment2.text_state.font = ap.text.FontRepository.find_font("Arial")
    fragment2.text_state.font_size = 14
    page.paragraphs.add(fragment2)

    # --- Third fragment (starts new paragraph automatically) ---
    fragment3 = ap.text.TextFragment("This is a new paragraph.")
    fragment3.text_state.font = ap.text.FontRepository.find_font("Arial")
    fragment3.text_state.font_size = 14
    page.paragraphs.add(fragment3)

    # Save PDF
    document.save(output_file_name)
```

### Buat PDF Multi-Kolom

Buat tata letak bergaya koran multi-kolom dalam PDF menggunakan Aspose.PDF untuk Python via .NET.
Ini menunjukkan cara menggabungkan teks, pemformatan HTML, dan grafik dalam FloatingBox, memungkinkan kontrol tata letak lanjutan serupa dengan desain majalah atau buletin multi-kolom.

1. Inisialisasi dokumen PDF.
1. Tambahkan garis pemisah horizontal di bagian atas.
1. Tambahkan judul HTML yang styled.
1. Buat FloatingBox untuk kontrol tata letak.
1. Konfigurasikan tata letak multi-kolom.
1. Tambahkan info penulis.
1. Gambar garis horizontal internal lainnya.
1. Tambahkan teks artikel.
1. Simpan PDF akhir.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_multi_column_pdf(output_file_name):
    """
    Create a PDF document with multi-column layout using FloatingBox.

    Creates a professional-looking PDF with a multi-column newspaper-style layout.
    Demonstrates advanced layout techniques including floating boxes, column
    configuration, and mixed content with graphics and text.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Document margins: 40 points left and right
        - Top horizontal line for visual separation
        - HTML-formatted heading with custom styling
        - FloatingBox with 2-column layout (105 units wide each)
        - Column spacing: 5 units between columns
        - Includes author attribution with italic styling
        - Internal horizontal line within the floating box
        - Long text content automatically flows between columns
        - Demonstrates professional document layout techniques

    Example:
        >>> create_multi_column_pdf("multi_column_layout.pdf")
        # Creates a PDF with newspaper-style multi-column layout
    """
    # Create PDF document
    document = ap.Document()

    # Set margins
    document.page_info.margin.left = 40
    document.page_info.margin.right = 40

    page = document.pages.add()

    #
    # Draw horizontal line at the top
    #
    graph1 = ap.drawing.Graph(500.0, 2.0)
    page.paragraphs.add(graph1)

    pos_arr = [1.0, 2.0, 500.0, 2.0]
    line1 = ap.drawing.Line(pos_arr)
    graph1.shapes.add(line1)

    #
    # Add HTML heading text
    #
    html = "<span style=\"font-family: 'Times New Roman'; font-size: 18px;\"><strong>How to Steer Clear of money scams</strong></span>"
    heading_text = ap.HtmlFragment(html)
    page.paragraphs.add(heading_text)

    #
    # Floating box: enables multi-column layout
    #
    box = ap.FloatingBox()

    box.column_info.column_count = 2  # Two columns
    box.column_info.column_spacing = "5"  # Space between columns
    box.column_info.column_widths = "105 105"  # Width of each column

    #
    # Add title text to the FloatingBox
    #
    text1 = ap.text.TextFragment("By A Googler (The Official Google Blog)")
    text1.text_state.font_size = 8
    text1.text_state.line_spacing = 2
    box.paragraphs.add(text1)

    text1.text_state.font_size = 10
    text1.text_state.font_style = ap.text.FontStyles.ITALIC

    #
    # Add another horizontal line inside the box
    #
    graph2 = ap.drawing.Graph(50.0, 10.0)

    pos_arr2 = [1.0, 10.0, 100.0, 10.0]
    line2 = ap.drawing.Line(pos_arr2)
    graph2.shapes.add(line2)

    box.paragraphs.add(graph2)

    #
    # Add long text content
    #
    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    lorem_text = (
        open(lorem_path, "r", encoding="utf-8").read()
        if os.path.exists(lorem_path)
        else "Lorem ipsum text not found."
    )
    text2 = ap.text.TextFragment(lorem_text * 5)
    box.paragraphs.add(text2)

    page.paragraphs.add(box)

    # Save PDF
    document.save(output_file_name)
```

### Tab Stop Kustom untuk Penyelarasan Teks di PDF

Buat tata letak teks mirip tabel dalam PDF menggunakan tab stop kustom — tanpa mengandalkan struktur tabel.
Dengan mendefinisikan posisi tab stop, penyelarasan, dan gaya leader, Anda dapat menyelaraskan teks secara tepat di seluruh kolom. Ini berguna untuk faktur, laporan, atau data teks terstruktur.

1. Buat dokumen PDF baru.
1. Tentukan tab stop kustom.
1. Gunakan placeholder #$TAB dalam teks.
1. Tambahkan teks ke PDF.
1. Simpan PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def custom_tab_stops(output_file_name):
    """
    Create a PDF document demonstrating custom tab stops for table-like formatting.

    Creates a PDF document that uses custom tab stops to format text in a table-like
    structure without using actual table elements. This demonstrates advanced text
    formatting with precise positioning and leader styles.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Tab stop 1: Position 100, right-aligned, solid leader line
        - Tab stop 2: Position 200, center-aligned, dashed leader line
        - Tab stop 3: Position 300, left-aligned, dotted leader line
        - Uses #$TAB placeholder for tab positions in text
        - Creates table-like structure with headers and data rows
        - Demonstrates mixing TextFragment and TextSegment approaches
        - Leader lines provide visual guides between columns
        - Alternative to HTML tables for precise text positioning

    Example:
        >>> custom_tab_stops("custom_tabs.pdf")
        # Creates a PDF with custom tab stop formatting
    """
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Define tab stops
    tab_stops = ap.text.TabStops()

    tab_stop1 = tab_stops.add(100)
    tab_stop1.alignment_type = ap.text.TabAlignmentType.RIGHT
    tab_stop1.leader_type = ap.text.TabLeaderType.SOLID

    tab_stop2 = tab_stops.add(200)
    tab_stop2.alignment_type = ap.text.TabAlignmentType.CENTER
    tab_stop2.leader_type = ap.text.TabLeaderType.DASH

    tab_stop3 = tab_stops.add(300)
    tab_stop3.alignment_type = ap.text.TabAlignmentType.LEFT
    tab_stop3.leader_type = ap.text.TabLeaderType.DOT

    # Create TextFragments with tab placeholders
    header = ap.text.TextFragment(
        "This is an example of forming table with TAB stops", tab_stops
    )
    text0 = ap.text.TextFragment("#$TABHead1 #$TABHead2 #$TABHead3", tab_stops)
    text1 = ap.text.TextFragment("#$TABdata11 #$TABdata12 #$TABdata13", tab_stops)

    text2 = ap.text.TextFragment("#$TABdata21 ", tab_stops)
    text2.segments.append(ap.text.TextSegment("#$TAB"))
    text2.segments.append(ap.text.TextSegment("data22 "))
    text2.segments.append(ap.text.TextSegment("#$TAB"))
    text2.segments.append(ap.text.TextSegment("data23"))

    # Add text fragments to page
    page.paragraphs.add(header)
    page.paragraphs.add(text0)
    page.paragraphs.add(text1)
    page.paragraphs.add(text2)

    # Save PDF document
    document.save(output_file_name)
```
