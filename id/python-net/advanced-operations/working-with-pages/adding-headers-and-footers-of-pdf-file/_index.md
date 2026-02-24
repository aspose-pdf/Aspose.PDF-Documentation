---
title: Menambahkan Header dan Footer ke PDF menggunakan Python
linktitle: Menambahkan Header dan Footer ke PDF
type: docs
weight: 50
url: /id/python-net/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF untuk Python via .NET memungkinkan Anda menambahkan header dan footer ke file PDF Anda menggunakan kelas TextStamp.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara menambahkan Header dan Footer ke PDF menggunakan Python
Abstract: Artikel ini menyediakan panduan komprehensif tentang penggunaan **Aspose.PDF for Python via .NET** untuk menambahkan header dan footer ke file PDF, dengan kemampuan untuk memasukkan teks atau gambar. Artikel ini dimulai dengan menjelaskan penggunaan kelas `TextStamp` untuk menyisipkan teks ke header dokumen PDF. Properti utama seperti ukuran font, gaya, dan warna dapat disesuaikan, dan metode penambahan teks ke header ditunjukkan dengan cuplikan kode Python. Artikel ini juga menjelaskan cara menambahkan teks ke footer, mengikuti langkah prosedural yang sama. Untuk menambahkan gambar, kelas `ImageStamp` digunakan, dan prosesnya dijelaskan untuk header dan footer, kembali didukung oleh contoh kode Python. Selain itu, artikel ini membahas penambahan beberapa header dalam satu file PDF. Ini meliputi pembuatan beberapa objek `TextStamp`, masing‑masing dengan format yang berbeda, dan menerapkannya ke halaman yang berbeda. Penjelasan ini dilengkapi dengan cuplikan kode terperinci yang menunjukkan fungsionalitas ini.
---

Halaman ini menyediakan ikhtisar singkat tentang menambahkan header dan footer ke dokumen PDF menggunakan Aspose.PDF for Python via .NET, mencakup pendekatan berbasis teks, HTML, LaTeX, gambar, dan tabel serta penomoran halaman dinamis dan beberapa header per‑halaman; menjelaskan cara membuat dan menata objek [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) (menggunakan [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/), [`HtmlFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlfragment/), [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/), [`Image`](https://reference.aspose.com/pdf/python-net/aspose.pdf/image/), [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/), dll.), menyesuaikan [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) dan [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) untuk penempatan yang tepat, dan melampirkan hasilnya ke halaman dengan contoh kode Python yang praktis.

**Aspose.PDF for Python via .NET** memungkinkan Anda menambahkan header dan footer dalam [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). Anda dapat menambahkan gambar atau teks ke dokumen PDF. Juga, coba tambahkan header yang berbeda dalam satu File PDF dengan Python.

## Menambahkan Header dan Footer sebagai Fragmen Teks

Tambahkan header dan footer teks sederhana ke semua halaman dalam PDF. Ini membuat objek [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/), menyisipkan elemen [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/) ke dalamnya, mengatur [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) untuk penempatan yang tepat, dan melampirkannya ke setiap halaman dalam dokumen. Hasilnya adalah PDF dimana setiap halaman menampilkan teks header dan footer yang konsisten.

Cuplikan kode berikut menunjukkan cara menambahkan header dan footer sebagai fragmen teks dalam PDF menggunakan Python:

1. Buat fragmen teks untuk header dan footer.
1. Buat objek HeaderFooter dan tambahkan fragmen teks ke dalamnya.
1. Tentukan pengaturan margin untuk mengontrol penempatan header dan footer.
1. Muat dokumen PDF dari file masukan.
1. Iterasi melalui semua halaman dalam dokumen.
1. Tetapkan header dan footer ke setiap halaman.
1. Simpan PDF yang telah dimodifikasi ke file keluaran.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_header_and_footer_as_text(input_file, output_file):
    """
    Add simple text headers and footers to all pages of a PDF document.

    Creates basic text-based headers and footers that appear on every page
    of the PDF document. Headers show "header" text and footers show "footer" text.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Adds identical headers and footers to all pages
        - Sets margins of 50 units left and 20 units top
        - Uses simple TextFragment elements for content
        - Headers and footers are created separately for each page

    Example:
        >>> add_header_and_footer_as_text("input.pdf", "output.pdf")
        # Adds text headers and footers to all pages
    """
    # Create header text
    header_text = ap.text.TextFragment("Demo header")
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_text)

    # Create footer text
    footer_text = ap.text.TextFragment("Demo footer")

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_text)

    # Set header margin
    margin = ap.MarginInfo()
    margin.left = 50
    margin.top = 20
    header.margin = margin

    # Set footer margin
    footer.margin = margin

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

Metode ini berguna untuk menambahkan judul konsisten, indikator halaman, atau penafian hukum di bagian atas dan bawah setiap halaman. Anda juga dapat memperluasnya untuk menyertakan gambar atau konten dinamis, seperti nomor halaman.

## Menambahkan Header dan Footer untuk Penomoran Halaman

Tambahkan penomoran halaman otomatis ke header dan footer dokumen PDF menggunakan Aspose.PDF untuk Python. Dengan menggunakan variabel bawaan $p (nomor halaman saat ini) dan $P (jumlah total halaman), skrip secara dinamis menyisipkan penomoran halaman pada setiap halaman. Header menampilkan format 'Page X from Y', sementara footer menunjukkan 'Page X / Y'. [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) memastikan penempatan yang tepat pada setiap halaman.

1. Buat TextFragment untuk header menggunakan "Page $p from $P" untuk menampilkan halaman saat ini dan total halaman.
1. Buat objek HeaderFooter dan tambahkan teks header ke dalamnya.
1. Buat TextFragment untuk footer menggunakan "Page $p / $P" untuk gaya penomoran alternatif.
1. Buat objek Footer dan tambahkan teks footer.
1. Tentukan pengaturan margin (kiri = 50, atas = 20) dan terapkan ke header dan footer.
1. Buka dokumen PDF dari file masukan.
1. Lakukan perulangan melalui semua halaman dan tetapkan header serta footer ke setiap halaman.
1. Simpan PDF yang diperbarui ke jalur keluaran.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def using_header_and_footer_for_page_numbering(input_file, output_file):
    """
    Add page numbering headers and footers to all pages of a PDF document.

    Creates headers and footers with dynamic page numbering using special variables.
    The $p variable represents the current page number and $P represents the total
    number of pages in the document.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses $p for current page number and $P for total pages
        - Header shows "Page X from Y" format
        - Footer shows "Page X / Y" format
        - Variables are automatically replaced by Aspose.PDF
        - Sets margins of 50 units left and 20 units top
        - Page numbering updates dynamically for each page

    Example:
        >>> using_header_and_footer_for_page_numbering("input.pdf", "output.pdf")
        # Adds page numbering headers and footers to all pages
    """
    # Create header text
    header_text = ap.text.TextFragment("Page $p from $P")
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_text)

    # Create footer text
    footer_text = ap.text.TextFragment("Page $p / $P")

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_text)

    # Create margins
    margin = ap.MarginInfo()
    margin.left = 50
    margin.top = 20

    # Set header margin
    header.margin = margin
    # Set footer margin
    footer.margin = margin

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## Menambahkan Header dan Footer sebagai Fragmen HTML

Terapkan header dan footer berformat HTML ke setiap halaman dokumen PDF menggunakan Aspose.PDF untuk Python. Dengan menggunakan [`HtmlFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlfragment/), skrip memungkinkan gaya teks kaya—seperti tebal dan miring—muncul di header dan footer. [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) diterapkan untuk penempatan yang tepat, dan elemen berformat yang sama dilampirkan ke setiap halaman dalam dokumen.

Cuplikan kode berikut menunjukkan cara menambahkan header dan footer sebagai fragmen HTML ke PDF menggunakan Python:

1. Buat cuplikan header HTML menggunakan HtmlFragment—termasuk teks bergaya seperti '<strong>' untuk tebal.
1. Buat objek HeaderFooter dan tambahkan header HTML ke dalamnya.
1. Buat cuplikan footer HTML menggunakan '<i>' untuk gaya miring.
1. Buat objek Footer dan tambahkan HTML footer ke dalamnya.
1. Konfigurasikan margin (kiri = 50, atas = 20) dan tetapkan ke header serta footer.
1. Muat dokumen PDF menggunakan 'ap.Document()'.
1. Lakukan perulangan melalui semua halaman dan tetapkan header serta footer ke masing‑masing.
1. Simpan PDF yang telah dimodifikasi ke jalur keluaran yang ditentukan.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_header_and_footer_as_html(input_file, output_file):
    """
    Add HTML-formatted headers and footers to all pages of a PDF document.

    Creates rich HTML-based headers and footers with formatting like bold
    and italic text. Demonstrates how to use HtmlFragment for styled content.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses HtmlFragment for rich text formatting
        - Header includes HTML with <strong> tag for bold text
        - Footer includes HTML with <i> tag for italic text
        - Sets margins of 50 units left and 20 units top
        - HTML tags are rendered properly in the PDF

    Example:
        >>> add_header_and_footer_as_html("input.pdf", "output.pdf")
        # Adds HTML-formatted headers and footers to all pages
    """
    # Create header HTML
    header_html = ap.HtmlFragment("This is an HTML <strong>Header</strong>")
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_html)

    # Create footer HTML
    footer_html = ap.HtmlFragment("Powered by <i>Aspose.PDF</i>")

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_html)

    # Set header margin
    margin = ap.MarginInfo()
    margin.left = 50
    margin.top = 20
    header.margin = margin

    # Set footer margin
    footer.margin = margin

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

Menggunakan HtmlFragment memungkinkan pemformatan kaya dengan gaya inline atau markup HTML, memberi Anda fleksibilitas desain lebih dibandingkan teks biasa.

## Menambahkan Header dan Footer sebagai Gambar

Tambahkan header dan footer berbasis gambar ke setiap halaman dokumen PDF menggunakan Aspose.PDF untuk Python. File gambar yang sama digunakan untuk header dan footer pada setiap halaman. [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) menempatkan gambar, dan gambar secara otomatis menyesuaikan agar muat dalam area header/footer.

Potongan kode berikut menunjukkan cara menambahkan header dan footer sebagai gambar ke PDF menggunakan Python:

1. Muat gambar ke dalam objek 'ap.Image' dan siapkan untuk digunakan sebagai header.
1. Buat objek HeaderFooter dan lampirkan gambar header ke dalamnya.
1. Muat gambar yang sama lagi untuk digunakan sebagai footer.
1. Buat objek Footer dan tambahkan gambar footer ke dalamnya.
1. Muat dokumen PDF input menggunakan 'ap.Document()'.
1. Iterasi melalui semua halaman dokumen.
1. Terapkan margin (kiri = 50) untuk memposisikan header dan footer.
1. Tetapkan header dan footer ke setiap halaman dalam PDF.
1. Simpan PDF yang diperbarui ke file output yang ditentukan.

Teknik ini ideal untuk memberi merek dokumen dengan logo atau watermark di area header/footer.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_header_and_footer_as_image(input_file, image_file, output_file):
    """
    Add image-based headers and footers to all pages of a PDF document.

    Creates headers and footers using image files. The same image is used
    for both header and footer positioning on each page.

    Args:
        input_file (str): Path to the input PDF file.
        image_file (str): Path to the image file to use for headers and footers.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses the same image file for both header and footer
        - Creates separate Image objects for header and footer
        - Sets margin of 50 units left for positioning
        - Image files should be in supported formats (PNG, JPG, etc.)
        - Images are automatically sized to fit header/footer areas

    Example:
        >>> add_header_and_footer_as_image("input.pdf", "logo.png", "output.pdf")
        # Adds image headers and footers using logo.png
    """

    # Create header image
    header_image = ap.Image()
    header_image.file = image_file
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_image)

    # Create footer image
    footer_image = ap.Image()
    footer_image.file = image_file

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_image)

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Set header margin
            margin = ap.MarginInfo()
            margin.left = 50
            header.margin = margin

            # Set footer margin
            footer.margin = margin

            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## Menambahkan Header dan Footer sebagai Tabel

Tambahkan header dan footer berbasis tabel yang terstruktur ke semua halaman dokumen PDF menggunakan Aspose.PDF untuk Python. [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) objek memberikan kontrol tata letak yang lebih baik, perataan, dan pemformatan konsisten untuk header dan footer yang kompleks. Teks header dipusatkan sementara teks footer diratakan ke kiri, keduanya menggunakan font Arial 12pt. Lebar kolom dihitung secara dinamis berdasarkan dimensi halaman untuk memastikan penempatan yang tepat.

Potongan kode ini menambahkan header dan footer (menggunakan tabel) ke setiap halaman dokumen PDF dengan Aspose.PDF untuk Python melalui .NET.

1. Tentukan gaya teks menggunakan [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) untuk header dan footer (font, ukuran, perataan).
1. Buat objek [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) untuk header dan footer.
1. Bangun [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) header dengan satu baris dan sel yang berisi teks header.
1. Bangun [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) footer dengan satu baris dan sel yang berisi teks footer.
1. Tambahkan tabel ke objek [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) yang sesuai.
1. Atur [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) footer untuk penempatan horizontal yang tepat.
1. Buka [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) menggunakan metode yang sesuai.
1. Iterasi melalui semua halaman dan tetapkan header serta footer berbasis tabel ke setiap halaman.
1. Simpan [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) yang dimodifikasi ke file output.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_header_and_footer_as_table(input_file, output_file):
    """
    Add table-based headers and footers to all pages of a PDF document.

    Creates headers and footers using table structures for better layout
    control and alignment. Demonstrates advanced formatting with text states.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses Table objects for structured layout
        - Header table has centered Arial 12pt text
        - Footer table has left-aligned Arial 12pt text
        - Column width calculated based on page width minus margins
        - Provides more precise control over text positioning

    Example:
        >>> add_header_and_footer_as_table("input.pdf", "output.pdf")
        # Adds table-structured headers and footers to all pages
    """
    text_state_header = ap.text.TextState()
    text_state_header.font = ap.text.FontRepository.find_font("Arial")
    text_state_header.font_size = 12
    text_state_header.horizontal_alignment = ap.HorizontalAlignment.CENTER
    text_state_footer = ap.text.TextState()
    text_state_footer.font = ap.text.FontRepository.find_font("Arial")
    text_state_footer.font_size = 12
    text_state_footer.horizontal_alignment = ap.HorizontalAlignment.LEFT
    # Create header
    header = ap.HeaderFooter()
    # Create footer
    footer = ap.HeaderFooter()
    # Create header Table
    table_header = ap.Table()
    table_header.column_widths = str(594 - header.margin.left - header.margin.right)
    header_row = table_header.rows.add()
    header_row.cells.add("This is a Table Header", text_state_header)
    # Create footer Table
    table = ap.Table()
    table.column_widths = str(594 - footer.margin.left - footer.margin.right)
    table.rows.add().cells.add("Powered by Aspose.PDF", text_state_footer)
    header.paragraphs.add(table_header)
    footer.paragraphs.add(table)
    # Set footer margin
    footer.margin.left = 150

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## Menambahkan Header dan Footer sebagai LaTeX

Tambahkan header dan footer yang berisi konten berformat LaTeX ke semua halaman dokumen PDF menggunakan Aspose.PDF untuk Python. LaTeX memungkinkan render simbol matematika, tanggal, tanda hak cipta, dan format lanjutan lainnya. Header mencakup tanggal dinamis, sedangkan footer menampilkan simbol hak cipta bersama nomor halaman saat ini dan total jumlah halaman.

Potongan kode berikut menunjukkan cara menggunakan [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) dalam header dan footer untuk PDF menggunakan Aspose.PDF untuk Python melalui .NET.

1. Buka [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) menggunakan metode yang sesuai.
1. Tentukan total jumlah halaman untuk digunakan dalam footer dinamis.
1. Iterasi melalui semua halaman dokumen.
1. Buat objek [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) untuk header.
1. Buat [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) untuk teks header yang berisi perintah LaTeX (mis., `\\today\\`).
1. Buat objek [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) untuk footer.
1. Buat [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) untuk teks footer yang mencakup simbol LaTeX dan penomoran halaman.
1. Tambahkan [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) ke objek header/footer yang bersesuaian.
1. Kaitkan header dan footer ke halaman saat ini.
1. Simpan [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) yang dimodifikasi ke file output.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_header_and_footer_as_latex(input_file, output_file):
    """
    Add LaTeX-formatted headers and footers to all pages of a PDF document.

    Creates headers and footers using LaTeX markup for mathematical expressions,
    symbols, and advanced formatting. Demonstrates TeXFragment usage.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses TeXFragment for LaTeX rendering
        - Header includes LaTeX date command (\\today\\)
        - Footer includes copyright symbol and page numbering
        - LaTeX commands are processed and rendered properly
        - Page count is dynamically calculated and inserted

    Example:
        >>> add_header_and_footer_as_latex("input.pdf", "output.pdf")
        # Adds LaTeX-formatted headers and footers with symbols and page numbers
    """
    # Open PDF document
    with ap.Document(input_file) as document:
        page_count = len(document.pages)
        for i in range(1, page_count + 1):
            # Create header
            header = ap.HeaderFooter()
            h_latex_text = "This is a LaTex Header. \\today\\"
            h_l_text = ap.TeXFragment(h_latex_text, True)
            # Create footer
            footer = ap.HeaderFooter()
            f_latex_text = f"\\copyright\\ 2025 My Company -- Page \\thepage\\ is {page_count}"
            f_l_text = ap.TeXFragment(f_latex_text, True)

            header.paragraphs.add(h_l_text)
            footer.paragraphs.add(f_l_text)
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```
