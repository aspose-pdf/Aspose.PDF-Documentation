---
title: Cari dan Dapatkan Teks dari Halaman PDF
linktitle: Cari dan Dapatkan Teks
type: docs
weight: 60
url: /id/python-net/search-and-get-text-from-pdf/
description: Pelajari cara mencari dan mengekstrak teks dari dokumen PDF dalam Python menggunakan Aspose.PDF untuk analisis dokumen.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara Mencari dan Mendapatkan Teks dari Halaman dalam PDF
Abstract: Artikel ini memberikan eksplorasi mendalam tentang kemampuan ekstraksi dan manipulasi teks dalam dokumen PDF menggunakan Aspose.PDF untuk Python via .NET library. Artikel ini memperkenalkan kelas TextFragmentAbsorber, yang memungkinkan pengembang mencari melalui seluruh dokumen atau halaman tertentu untuk frasa yang ditentukan atau pola ekspresi reguler. Halaman ini memaparkan berbagai skenario praktis—seperti mengambil konten teks, menentukan posisinya (termasuk koordinat dan nilai indent), dan mengekstrak properti font seperti nama, ukuran, status embed, dan warna—dari fragmen teks yang cocok. Contoh kode terperinci menunjukkan proses langkah demi langkah, memudahkan pengembang untuk mengintegrasikan kemampuan pencarian teks ke dalam aplikasi mereka.
---

## Cari Teks dari PDF

Cari dan ekstrak teks dari area persegi panjang yang ditentukan dalam dokumen PDF menggunakan kelas TextAbsorber. Ini menggunakan mode pemformatan teks murni untuk output teks bersih dan tidak terformat, menjadikannya ideal untuk mengekstrak konten dari wilayah terstruktur seperti header, footer, atau area tabel. Dengan menggabungkan TextExtractionOptions dan TextSearchOptions dengan batas persegi panjang, contoh ini memberi Anda kontrol yang tepat tentang di mana dan bagaimana teks diekstrak dari dokumen.

1. Muat file PDF menggunakan 'ap.Document'.
1. Konfigurasikan Opsi Ekstraksi Teks.
1. Tentukan Area Pencarian dengan Batas Persegi Panjang.
1. Buat dan Konfigurasikan TextAbsorber.
1. Proses Semua Halaman dalam Dokumen.
1. Ambil dan Tampilkan Teks yang Diekstrak.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_absorber_search(input_file_path):
    """
    Search and extract text from PDF using TextAbsorber with area constraints.

    Demonstrates basic text extraction from a PDF document using TextAbsorber
    with pure text formatting mode and rectangular boundary constraints.
    Extracts text from all pages within the specified rectangular area.

    Args:
        input_file_path (str): Path to the input PDF file to search.

    Returns:
        None: Prints extracted text to console.

    Note:
        - Uses PURE text formatting mode for clean text extraction
        - Constrains search to rectangle (0, 0, 842, 250)
        - Processes all pages in the document
        - TextAbsorber provides high-level text extraction capabilities
        - Good for extracting text content without detailed positioning

    Example:
        >>> text_absorber_search("document.pdf")
        # Prints all text found in the specified rectangular area across all pages
    """
    # Open PDF document
    document = ap.Document(input_file_path)

    text_extraction_options = ap.text.TextExtractionOptions(
        ap.text.TextExtractionOptions.TextFormattingMode.PURE
    )
    text_search_options = ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))

    absorber = ap.text.TextAbsorber(text_extraction_options, text_search_options)

    # Process all pages
    document.pages.accept(absorber)

    print(f"Text fragments found: {absorber.text}")
```

## Cari Teks dari Halaman PDF Tertentu

Cari dan ekstrak teks dari halaman dan wilayah tertentu dalam PDF menggunakan TextAbsorber dari Aspose.PDF. Ini menargetkan halaman 2 dokumen dan hanya mengekstrak teks yang ditemukan dalam area persegi panjang yang ditentukan.
Dengan menggabungkan TextExtractionOptions (untuk kontrol pemformatan) dan TextSearchOptions (untuk pembatasan area), Anda dapat melakukan ekstraksi teks yang tepat dan spesifik halaman secara efisien.

1. Muat Dokumen PDF.
1. Siapkan Opsi Ekstraksi Teks.
1. Batasi ekstraksi teks ke area persegi panjang tertentu pada halaman.
1. Buat dan Konfigurasikan TextAbsorber.
1. Proses Halaman Tertentu.
1. Ambil dan Tampilkan Teks yang Diekstrak.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_absorber_search_page(input_file_path):
    """
    Search and extract text from a specific PDF page using TextAbsorber.

    Demonstrates targeted text extraction from a single page (page 2) using
    TextAbsorber with area constraints. Shows how to limit search scope to
    specific pages and rectangular regions.

    Args:
        input_file_path (str): Path to the input PDF file to search.

    Returns:
        None: Prints extracted text from page 2 to console.

    Note:
        - Targets only page 2 of the document (document.pages[2])
        - Uses PURE text formatting mode for clean extraction
        - Constrains search to rectangle (0, 0, 842, 250)
        - Useful for page-specific text extraction
        - More efficient than processing entire document when targeting specific pages

    Example:
        >>> text_absorber_search_page("document.pdf")
        # Prints text found in the specified area on page 2 only
    """
    document = ap.Document(input_file_path)

    text_extraction_options = ap.text.TextExtractionOptions(
        ap.text.TextExtractionOptions.TextFormattingMode.PURE
    )
    text_search_options = ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))

    absorber = ap.text.TextAbsorber(text_extraction_options, text_search_options)

    # Only page 2
    document.pages[2].accept(absorber)

    print(f"Text fragments found: {absorber.text}")

```

## Analisis dan Ekstrak Properti Fragmen Teks Detail dari PDF

Berbeda dengan TextAbsorber, yang mengekstrak teks mentah, TextFragmentAbsorber menyediakan informasi terperinci dan tingkat rendah tentang setiap fragmen teks—seperti posisinya, atribut font, warna, dan detail embedding.

1. Muat Dokumen PDF.
1. Inisialisasi TextFragmentAbsorber.
1. Proses Semua Halaman dalam Dokumen.
1. Iterasi Melalui Fragmen Teks yang Diekstrak.
1. Cetak Informasi Teks Dasar.
1. Cetak Detail Font dan Pemformatan.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search(input_file_path):
    """
    Search and analyze all text fragments in a PDF with detailed properties.

    Demonstrates comprehensive text fragment analysis using TextFragmentAbsorber
    to extract all text with detailed positioning, font, and formatting information.
    Provides low-level access to text properties for detailed analysis.

    Args:
        input_file_path (str): Path to the input PDF file to analyze.

    Returns:
        None: Prints detailed text fragment information to console.

    Note:
        - Extracts all text fragments from all pages
        - Provides detailed properties: position, font info, colors, sizes
        - Shows font accessibility, embedding, and subset information
        - Useful for detailed text analysis and formatting inspection
        - TextFragmentAbsorber offers more granular control than TextAbsorber

    Example:
        >>> text_fragment_absorber_search("document.pdf")
        # Prints comprehensive details about every text fragment in the document
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    document.pages.accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
        print("XIndent:", fragment.position.x_indent)
        print("YIndent:", fragment.position.y_indent)
        print("Font - Name:", fragment.text_state.font.font_name)
        print("Font - IsAccessible:", fragment.text_state.font.is_accessible)
        print("Font - IsEmbedded:", fragment.text_state.font.is_embedded)
        print("Font - IsSubset:", fragment.text_state.font.is_subset)
        print("Font Size:", fragment.text_state.font_size)
        print("Foreground Color:", fragment.text_state.foreground_color)
```

## Cari Frasa Teks Spesifik pada Satu Halaman PDF

Cari frasa teks spesifik dalam satu halaman dokumen PDF menggunakan TextFragmentAbsorber. Berbeda dengan pencarian seluruh dokumen, pendekatan ini membatasi pencarian hanya pada satu halaman, sehingga lebih efisien untuk memastikan keberadaan dan lokasi teks di area target seperti header, footer, atau bagian konten tertentu.

1. Muat Dokumen PDF.
1. Inisialisasi TextFragmentAbsorber dengan Frasa Pencarian.
1. Terapkan Absorber ke Halaman Tertentu.
1. Iterasi Melalui Fragmen yang Ditemukan.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_page(input_file_path):
    """
    Search for specific text phrase on a particular PDF page.

    Demonstrates targeted text search for a specific phrase ("whale") on
    a single page. Shows how to combine phrase searching with page-specific
    scope for efficient and focused text location.

    Args:
        input_file_path (str): Path to the input PDF file to search.

    Returns:
        None: Prints matching text fragments and their positions to console.

    Note:
        - Searches for the phrase "whale" on page 2 only
        - Returns text fragments with position information
        - More efficient than document-wide search when targeting specific pages
        - Useful for validating content presence in specific document sections
        - Provides exact positioning coordinates for found text

    Example:
        >>> text_fragment_absorber_search_page("document.pdf")
        # Prints all instances of "whale" found on page 2 with their positions
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber("whale")
    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## Pencarian Teks Berurutan Halaman-per-Halaman dengan Hasil Kumulatif

Cari teks secara bertahap melintasi beberapa halaman dokumen PDF menggunakan TextFragmentAbsorber dari Aspose.PDF.
Berbeda dengan pencarian satu halaman atau seluruh dokumen, pendekatan ini memungkinkan Anda memproses halaman secara berurutan, mengumpulkan hasil secara progresif, dan menganalisis fragmen teks dengan konteks spesifik halaman. Metode ini ideal untuk dokumen besar atau alur kerja pemrosesan progresif.

1. Muat Dokumen PDF.
1. Inisialisasi TextFragmentAbsorber dan Tetapkan Frasa Pencarian.
1. Proses Halaman Pertama. Cari hanya halaman 1. Mencetak teks, nomor halaman, dan posisi. Menyediakan hasil terisolasi spesifik halaman untuk kejelasan.
1. Proses Halaman Berikutnya Secara Berurutan. Pindah ke halaman 2 dan secara opsional lanjutkan melalui sisa dokumen. 'absorber.visit()' memastikan akumulasi hasil dari semua halaman yang dikunjungi. Mencetak hasil pencarian kumulatif, menampilkan baik teks maupun lokasi.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_sequential_search(input_file_path):
    """
    Demonstrate sequential page-by-page text search with cumulative results.

    Shows how to perform incremental text searches across multiple pages,
    accumulating results from each page. Demonstrates both individual page
    processing and document-wide search continuation.

    Args:
        input_file_path (str): Path to the input PDF file to search.

    Returns:
        None: Prints text fragments from sequential page searches to console.

    Note:
        - Searches for "whale" on page 1, then continues to page 2
        - Uses absorber.visit(document) to process remaining pages
        - Demonstrates incremental search accumulation
        - Shows page numbers for found fragments
        - Useful for progressive document processing and result accumulation

    Example:
        >>> text_fragment_absorber_sequential_search("document.pdf")
        # Prints "whale" instances from page 1, then from all remaining pages
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    absorber.phrase = "whale"

    # First page
    document.pages[1].accept(absorber)
    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Page:", fragment.page.number)
        print("Position:", fragment.position)

    print("--")

    # Continue to next page
    document.pages[2].accept(absorber)
    absorber.visit(document)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Page:", fragment.page.number)
        print("Position:", fragment.position)
```

## Pencarian Frasa Terarah dalam Area Persegi Panjang

Cari frasa tertentu dalam PDF sambil membatasi pencarian ke area persegi panjang tertentu pada satu halaman.
Dengan menggabungkan pencarian frasa dengan batasan spasial, Anda dapat menemukan konten secara tepat di wilayah yang ditentukan tanpa memindai seluruh halaman atau dokumen. Ini sangat berguna untuk formulir, header, footer, atau laporan terstruktur di mana konten muncul di lokasi yang dapat diprediksi.

1. Muat Dokumen PDF.
1. Inisialisasi TextFragmentAbsorber dengan Frasa dan Batasan Persegi Panjang
1. Terapkan Absorber ke Halaman 2. Membatasi pemrosesan ke halaman 2, mengurangi perhitungan yang tidak perlu. Memastikan pencarian spesifik per halaman.
1. Iterasi Melalui Fragmen yang Ditemukan dan Cetak

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_phrase(input_file_path):
    """
    Search for specific phrase within a rectangular area constraint.

    Demonstrates targeted phrase searching with both text matching and
    spatial constraints. Combines phrase search with rectangular boundary
    limitations for precise content location.

    Args:
        input_file_path (str): Path to the input PDF file to search.

    Returns:
        None: Prints matching text fragments and positions to console.

    Note:
        - Searches for "elephant" phrase on page 2
        - Constrains search to rectangle (0, 0, 842, 250)
        - Combines text matching with spatial filtering
        - Useful for finding content in specific document regions
        - More precise than page-wide or document-wide searches

    Example:
        >>> text_fragment_absorber_search_phrase("document.pdf")
        # Prints "elephant" instances found within the specified rectangular area on page 2
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber(
        "elephant", ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))
    )

    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## Pencarian Pola Teks dalam PDF Menggunakan Ekspresi Reguler

Cari pola teks dalam PDF menggunakan ekspresi reguler. Dengan mengaktifkan mode regex pada TextFragmentAbsorber, Anda dapat menemukan pola kompleks seperti angka, tanggal, harga, koordinat, atau format teks khusus. Fungsi ini membatasi pencarian ke halaman tertentu, menjadikannya efisien untuk ekstraksi terarah data terstruktur.

1. Muat Dokumen PDF.
1. Inisialisasi TextFragmentAbsorber dengan Pola Regex.
1. Terapkan Absorber ke Halaman 2. Membatasi pencarian ke halaman 2 untuk efisiensi dan presisi. Hanya teks pada halaman ini yang dianalisis.
1. Iterasi Melalui Fragmen yang Ditemukan. Mencetak fragmen teks yang cocok beserta koordinatnya. Menyediakan informasi lokasi yang tepat untuk pola yang diekstrak.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_regex(input_file_path):
    """
    Search for text patterns using regular expressions.

    Demonstrates advanced text searching using regular expression patterns
    to find complex text structures like numbers, dates, or custom formats.
    Shows how to enable regex mode in TextFragmentAbsorber.

    Args:
        input_file_path (str): Path to the input PDF file to search.

    Returns:
        None: Prints matching text fragments and positions to console.

    Note:
        - Uses regex pattern r"\\d+\\.\\d+" to find decimal numbers
        - Enables regex mode with is_regular_expression_used=True
        - Searches on page 2 only
        - Powerful for finding formatted data like prices, coordinates, dates
        - Regular expressions provide flexible pattern matching capabilities

    Example:
        >>> text_fragment_absorber_search_regex("document.pdf")
        # Prints all decimal numbers (e.g., "12.34", "0.99") found on page 2
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber(r"\d+\.\d+", ap.text.TextSearchOptions(is_regular_expression_used=True))

    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## Mengonversi Kecocokan Teks menjadi Tautan Hipertaut di PDF Menggunakan TextFragmentAbsorber

Cari frasa teks tertentu dalam PDF dan konversi menjadi tautan yang dapat diklik. Dengan menggunakan TextFragmentAbsorber bersama pola regex, ia menemukan kata target dan menerapkan gaya visual (warna dan garis bawah) bersama tautan interaktif.

1. Muat Dokumen PDF.
1. Inisialisasi TextFragmentAbsorber dengan Pola Regex.
1. Terapkan Absorber ke Halaman 1.
1. Gaya dan Tambahkan Tautan Hipertaut ke Kecocokan.
1. Simpan PDF yang Dimodifikasi.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_and_add_hyperlink(input_file_path):
    """
    Search for text and convert matches to hyperlinks with styling.

    Demonstrates advanced text processing by finding specific words and
    converting them into clickable hyperlinks with visual styling. Shows
    how to combine text search with document modification.

    Args:
        input_file_path (str): Path to the input PDF file to process.

    Returns:
        None: Saves modified PDF with hyperlinks to output file.

    Note:
        - Searches for "whale|elephant" using regex pattern on page 1
        - Converts found text to Wikipedia hyperlinks
        - Applies blue color and underline styling to hyperlinks
        - Creates new output file with "_out.pdf" suffix
        - Demonstrates practical text enhancement and interactivity
        - Combines search, styling, and hyperlinking in one operation

    Example:
        >>> text_fragment_absorber_search_and_add_hyperlink("document_in.pdf")
        # Creates "document_out.pdf" with "whale" and "elephant" as clickable Wikipedia links
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber("whale|elephant")
    absorber.text_search_options = ap.text.TextSearchOptions(True)

    absorber.visit(document.pages[1])

    for fragment in absorber.text_fragments:
        fragment.text_state.foreground_color = ap.Color.blue
        fragment.text_state.underline = True
        fragment.hyperlink = ap.WebHyperlink(
            f"https://en.wikipedia.org/wiki/{fragment.text}"
        )

    output = input_file_path.replace("in.pdf", "out.pdf")
    document.save(output)
```

## Cari dan Identifikasi Teks Bergaya dalam PDF Menggunakan TextFragmentAbsorber

Cari fragmen teks dalam PDF berdasarkan properti pemformatannya, bukan kontennya. Dengan menggunakan TextFragmentAbsorber, ia mengidentifikasi teks dengan gaya tertentu, seperti teks tebal.

1. Muat Dokumen PDF.
1. Inisialisasi TextFragmentAbsorber.
1. Terapkan Absorber ke Halaman 1.
1. Periksa Fragmen Teks Berdasarkan Pemformatan. Memeriksa gaya font untuk pemformatan tebal.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_styled_text(input_file_path):
    """
    Search and identify text based on formatting properties.

    Demonstrates how to find text fragments based on their formatting
    characteristics rather than content. Shows detection of bold text
    and invisible text within the document.

    Args:
        input_file_path (str): Path to the input PDF file to analyze.

    Returns:
        None: Prints formatted text findings to console.

    Note:
        - Searches all text fragments on page 1
        - Identifies text with FontStyles.BOLD formatting
        - Detects invisible/hidden text using text_state.invisible
        - Useful for formatting analysis and hidden content detection
        - Demonstrates text property-based filtering capabilities

    Example:
        >>> text_fragment_absorber_search_styled_text("document.pdf")
        # Prints all bold text and any hidden/invisible text found on page 1
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    absorber.text_search_options = ap.text.TextSearchOptions(True)

    absorber.visit(document.pages[1])

    for fragment in absorber.text_fragments:
        if fragment.text_state.font_style == ap.text.FontStyles.BOLD:
            print(f"Bold: {fragment.text}")
```

Mendeteksi teks tersembunyi atau tidak terlihat dalam dokumen PDF dengan menganalisis properti pemformatan teks:

1. Muat Dokumen PDF.
1. Inisialisasi TextFragmentAbsorber.
1. Terapkan Absorber ke Halaman 1.
1. Periksa Fragmen Teks Berdasarkan Pemformatan. Periksa 'fragment.text_state.invisible' untuk teks tersembunyi.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_styled_text(input_file_path):
    """
    Search and identify text based on formatting properties.

    Demonstrates how to find text fragments based on their formatting
    characteristics rather than content. Shows detection of bold text
    and invisible text within the document.

    Args:
        input_file_path (str): Path to the input PDF file to analyze.

    Returns:
        None: Prints formatted text findings to console.

    Note:
        - Searches all text fragments on page 1
        - Identifies text with FontStyles.BOLD formatting
        - Detects invisible/hidden text using text_state.invisible
        - Useful for formatting analysis and hidden content detection
        - Demonstrates text property-based filtering capabilities

    Example:
        >>> text_fragment_absorber_search_styled_text("document.pdf")
        # Prints all bold text and any hidden/invisible text found on page 1
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    absorber.text_search_options = ap.text.TextSearchOptions(True)

    absorber.visit(document.pages[1])

    for fragment in absorber.text_fragments:
        if fragment.text_state.invisible:
            print(f"Invisible: {fragment.text}")
```

## Penyorotan Teks Visual di Halaman PDF

Fungsi ini menggabungkan pengenalan teks dan rendering menjadi satu alur kerja. Tidak hanya mengekstrak teks tetapi juga memvisualisasikannya dengan menyorot fragmen, segmen, dan karakter dalam kotak berwarna pada gambar PNG setiap halaman.

Contoh kami melakukan visualisasi teks tingkat lanjut pada PDF dengan:

- mencari semua fragmen teks yang terlihat menggunakan ekspresi reguler
- merender setiap halaman PDF menjadi gambar PNG resolusi tinggi
- menggambar kotak berwarna di sekitar fragmen teks, segmen teks, dan karakter individual

1. Atur Resolusi Gambar Output. Setiap halaman PDF dikonversi menjadi gambar PNG 150 DPI.
1. Buka PDF dan Inisialisasi Text Absorber.
1. Proses Setiap Halaman. Terapkan absorber ke setiap halaman. Kumpulkan semua fragmen teks yang terdeteksi dan posisi geometrisnya.
1. Konversi Halaman ke Aliran PNG.
1. Siapkan Objek Grafik untuk Menggambar.
1. Terapkan Transformasi Koordinat. Konversi koordinat PDF ke piksel gambar.
1. Gambar Kotak untuk Elemen Teks.
1. Simpan Hasil.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_and_highlight(infile):
    """
    Search text and create visual highlighting with PNG output.

    Advanced function that combines text search with visual highlighting.
    Converts PDF pages to PNG images and draws colored rectangles around
    found text fragments, segments, and individual characters.

    Args:
        infile (str): Path to the input PDF file to process.

    Returns:
        None: Saves highlighted PNG images for each page.

    Note:
        - Uses regex pattern r"[\\S]+" to find all non-whitespace sequences
        - Converts each page to 150 DPI PNG image using PngDevice
        - Draws yellow rectangles around text fragments
        - Draws green rectangles around text segments
        - Draws black rectangles around individual characters
        - Creates detailed visual analysis of text structure
        - Output files named with page numbers: "filename1_out.png", etc.
        - Complex coordinate transformation for proper overlay positioning

    Example:
        >>> text_fragment_absorber_search_and_highlight("document_in.pdf")
        # Creates PNG files with visual highlighting of all text elements
    """
    resolution = 150
    png_device = ap.devices.PngDevice(ap.devices.Resolution(resolution, resolution))

    # Open PDF document
    document = ap.Document(infile)
    absorber = ap.text.TextFragmentAbsorber(r"[\S]+")
    absorber.text_search_options.is_regular_expression_used = True

    for page in document.pages:
        page.accept(absorber)
        stream = io.BytesIO()
        png_device.process(page, stream)
        with drawing.Bitmap.from_stream(stream) as bmp:
            with drawing.Graphics.from_image(bmp) as gr:
                scale = resolution / 72
                gr.transform = drawing.drawing2d.Matrix(
                    float(scale),
                    float(0),
                    float(0),
                    float(-scale),
                    float(0),
                    float(bmp.height),
                )
                text_fragment_collection = absorber.text_fragments
                # Loop through the fragments
                for text_fragment in text_fragment_collection:
                    gr.draw_rectangle(
                        drawing.Pens.yellow,
                        float(text_fragment.position.x_indent),
                        float(text_fragment.position.y_indent),
                        float(text_fragment.rectangle.width),
                        float(text_fragment.rectangle.height),
                    )
                    for seg_num in range(1, len(text_fragment.segments) + 1):
                        segment = text_fragment.segments[seg_num]
                        for char_num in range(1, len(segment.characters) + 1):
                            character_info = segment.characters[char_num]
                            rect = page.get_page_rect(True)
                            print(
                                f"TextFragment = {text_fragment.text}"
                                + f" Page URY = {rect.ury}"
                                + f" TextFragment URY = {text_fragment.rectangle.ury}"
                            )
                            gr.draw_rectangle(
                                drawing.Pens.black,
                                float(character_info.rectangle.llx),
                                float(character_info.rectangle.lly),
                                float(character_info.rectangle.width),
                                float(character_info.rectangle.height),
                            )
                        gr.draw_rectangle(
                            drawing.Pens.green,
                            float(segment.rectangle.llx),
                            float(segment.rectangle.lly),
                            float(segment.rectangle.width),
                            float(segment.rectangle.height),
                        )

                # Save result
                bmp.save(
                    infile.replace("_in.pdf", str(page.number) + "_out.png"),
                    drawing.imaging.ImageFormat.png,
                )
```
