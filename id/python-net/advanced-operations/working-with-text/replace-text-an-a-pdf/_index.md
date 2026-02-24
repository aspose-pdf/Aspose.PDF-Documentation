---
title: Ganti Teks di PDF dengan Python
linktitle: Ganti Teks di PDF
type: docs
weight: 40
url: /id/python-net/replace-text-in-pdf/
description: Pelajari lebih lanjut tentang berbagai cara mengganti dan menghapus teks dari pustaka Aspose.PDF untuk Python via .NET.
lastmod: "2025-10-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
aliases: 
    - /python-net/replace-text-in-a-pdf-document/
TechArticle: true
AlternativeHeadline: Cara mengganti Teks di PDF menggunakan Python
Abstract: Artikel ini menyediakan panduan komprehensif tentang berbagai teknik manipulasi teks dalam dokumen PDF menggunakan Aspose.PDF untuk Python via .NET. Artikel ini mencakup beberapa strategi penggantian teks, termasuk mengganti teks di semua halaman, dalam wilayah halaman tertentu, dan menggunakan ekspresi reguler. Artikel juga menjelaskan cara mengganti font dalam PDF, memastikan font yang tidak terpakai dihapus, serta cara mengelola penggantian teks untuk secara otomatis menyusun ulang konten halaman. Selain itu, artikel membahas render simbol yang dapat diganti selama pembuatan PDF, termasuk penggunaannya di area header/footer, untuk meningkatkan kustomisasi dokumen. Akhirnya, artikel merinci metode untuk menghapus semua teks dari dokumen PDF, mengoptimalkan operasi untuk skenario di mana penghapusan total teks diperlukan. Setiap bagian dilengkapi dengan potongan kode dalam Python dan bahasa lain yang didukung untuk menunjukkan implementasi praktis.
---

Contoh-contoh ini menunjukkan cara **memodifikasi atau menghapus teks dalam PDF yang ada**.

## Ganti teks yang ada

### Ganti Teks di semua halaman dokumen PDF

{{% alert color="primary" %}}

Anda dapat mencoba mencari dan mengganti teks dalam dokumen menggunakan Aspose.PDF dan melihat hasilnya secara online melalui [tautan](https://products.aspose.app/pdf/redaction)

{{% /alert %}}

Penggantian teks adalah kebutuhan umum saat memperbarui atau memperbaiki konten dalam dokumen PDF yang ada — misalnya, mengubah nama produk, memperbaiki typo, atau memperbarui terminologi di banyak halaman.

Aspose.PDF untuk Python via .NET menawarkan metode yang kuat dan efisien untuk mencari dan mengganti teks secara programatis melalui kelas [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/).

Contoh ini menunjukkan cara menemukan semua kemunculan frasa tertentu (dalam kasus ini, "Black cat") dan menggantinya dengan frasa baru ("White dog") di seluruh dokumen PDF.

1. Tentukan Frasa Pencarian dan Penggantian. Atur teks yang ingin Anda temukan dan teks yang ingin menggantikannya.
1. Muat Dokumen PDF.
1. Buat Text Absorber. TextFragmentAbsorber diinisialisasi dengan frasa pencarian. Ia memindai dokumen untuk semua kemunculan frasa tersebut.
1. Terapkan Absorber ke Semua Halaman. Ini iterasi melalui semua halaman dan mengumpulkan fragmen teks yang cocok dengan frasa.
1. Ganti setiap fragmen yang ditemukan. Setiap kemunculan "Black cat" harus diubah menjadi "White dog".
1. Simpan PDF yang Diperbarui.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_on_all_pages(infile, outfile):
    """
    Replace text on all pages of a PDF document.

    Searches for a specific text phrase throughout all pages of a PDF document
    and replaces all occurrences with a new phrase. This function demonstrates
    global text replacement using TextFragmentAbsorber.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Replaces "Black cat" with "White dog" as demonstration
        - Searches across all pages in the document
        - Preserves original formatting and layout
        - Uses TextFragmentAbsorber for efficient text search

    Example:
        >>> replace_text_on_all_pages("input.pdf", "output.pdf")
        # Replaces all instances of "Black cat" with "White dog"
    """
    search_phrase = "Black cat"
    replace_phrase = "White dog"

    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(search_phrase)
        document.pages.accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = replace_phrase

        document.save(outfile)
```

### Ganti Teks di wilayah halaman tertentu

Terkadang, Anda mungkin perlu mengganti teks hanya dalam area tertentu dari halaman PDF alih-alih mencari di seluruh dokumen — misalnya, memperbarui header, footer, atau sel tabel pada posisi yang diketahui.

Pustaka Aspose.PDF untuk Python via .NET memungkinkan fungsi ini dengan memanfaatkan [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) bersamaan dengan pencarian teks berbasis wilayah.

Contoh ini menunjukkan cara menemukan dan mengganti semua kemunculan frasa target dalam wilayah persegi panjang yang ditentukan pada halaman tertentu.

1. Tentukan Frasa Pencarian dan Penggantian.
1. Muat Dokumen PDF.
1. Buat Text Absorber untuk Pencarian. Inisialisasi TextFragmentAbsorber untuk menemukan teks yang diinginkan.
1. Batasi Area Pencarian. Persegi panjang menentukan batas koordinat x dan y pada halaman.
1. Terapkan Absorber ke Halaman Tertentu. Ini melakukan pencarian dan mengumpulkan fragmen teks yang cocok dalam area yang ditentukan.
1. Ganti Teks yang Ditemukan. Setiap kemunculan 'doc' dalam wilayah yang ditentukan menjadi 'DOC'.
1. Simpan PDF yang Diperbarui.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_in_particular_page_region(infile, outfile):
    """
    Replace text in a particular region of a page.

    Performs targeted text replacement within a specific rectangular region
    on the first page of a PDF document. This allows for precise control
    over which text gets replaced based on its location.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Replaces "doc" with "DOC" within the specified region
        - Only affects text within coordinates (300, 442, 500, 742)
        - Uses limit_to_page_bounds for precise region control
        - Only processes the first page (pages[1])

    Example:
        >>> replace_text_in_particular_page_region("input.pdf", "output.pdf")
        # Replaces "doc" with "DOC" only in the specified rectangular area
    """
    search_phrase = "doc"
    replace_phrase = "DOC"

    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(search_phrase)
        absorber.text_search_options.limit_to_page_bounds = True
        absorber.text_search_options.rectangle = ap.Rectangle(300, 442, 500, 742, True)
        document.pages[1].accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = replace_phrase

        document.save(outfile)
```

### Ubah Ukuran dan Pindahkan Teks Tanpa Mengubah Ukuran Font

Saat mengganti teks dalam PDF, terkadang Anda ingin menyesuaikan atau memposisikan kembali teks baru dalam area tertentu tanpa mengubah ukuran font.
Aspose.PDF untuk Python via .NET menyediakan opsi untuk mengatur tata letak dan spasi teks sambil mempertahankan ukuran font asli.

1. Muat Dokumen PDF.
1. Kumpulkan semua fragmen teks pada halaman menggunakan 'TextFragmentAbsorber'.
1. Pilih Fragmen yang Akan Diubah.
1. Pindahkan dan ubah ukuran persegi panjang teks.
1. Sesuaikan Spasi Teks. Aktifkan penyesuaian spasi untuk menyesuaikan teks dalam persegi panjang yang telah diubah.
1. Ganti teks fragmen.
1. Simpan PDF yang Diperbarui.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_and_resize_and_shift_without_changing_font_size(infile, outfile):
    """
    Resize and shift text without changing the font size.

    Demonstrates how to replace text content while adjusting its position
    and width within a modified rectangular area. The font size remains
    unchanged, but spacing is adjusted to fit the new content.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Targets the second text fragment on the first page
        - Narrows the text rectangle by 50 units on each side
        - Duplicates the original text content
        - Uses ADJUST_SPACE_WIDTH for proper spacing
        - Maintains original font size and style

    Example:
        >>> replace_text_and_resize_and_shift_without_changing_font_size("input.pdf", "output.pdf")
        # Duplicates text in a narrower space with adjusted spacing
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        rect = fragment.rectangle
        rect.llx += 50
        rect.urx -= 50
        fragment.replace_options.rectangle = rect
        fragment.replace_options.replace_adjustment_action = (
             ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### Ubah Ukuran dan Pindahkan Paragraf dalam PDF

Saat bekerja dengan PDF, kadang-kadang Anda perlu mengganti atau memperluas sebuah paragraf sambil menjaga keselarasan visual dengan tata letak halaman. Aspose.PDF memungkinkan Anda mengubah ukuran persegi pembatas paragraf dan menyesuaikan spasi agar cocok dengan teks baru, semuanya tanpa mengubah ukuran font.

1. Muat Dokumen PDF.
1. Gunakan 'TextFragmentAbsorber' untuk mengumpulkan semua fragmen teks pada halaman.
1. Pilih Fragmen yang Akan Diubah.
1. Ubah Ukuran dan Pindahkan Paragraf. Gunakan media box halaman untuk menentukan batas dan menyesuaikan persegi.
1. Sesuaikan Spasi. Ini mengubah spasi antar kata/huruf alih-alih mengubah ukuran font.
1. Ganti teks fragmen.
1. Simpan PDF yang telah Diubah.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_and_resize_and_shift_paragraph(infile, outfile):
    """
    Resize and shift a paragraph in the document.

    Demonstrates paragraph-level text replacement with automatic resizing
    to fit within the page's media box boundaries. Adjusts the text area
    to provide margins while duplicating content.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses page media box as base rectangle
        - Adds 20-unit margins on left, right, and top
        - Targets the second text fragment on the first page
        - Duplicates original text content
        - Automatically adjusts space width for proper fit

    Example:
        >>> replace_text_and_resize_and_shift_paragraph("input.pdf", "output.pdf")
        # Resizes paragraph to fit within page margins with duplicated text
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        rect = document.pages[1].media_box
        rect.llx += 20
        rect.urx -= 20
        rect.ury -= 20
        fragment.replace_options.rectangle = rect
        fragment.replace_options.replace_adjustment_action = (
             ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### Ganti Teks dan Secara Otomatis Memperluas Font untuk Mengisi Area Target

Ganti teks dalam PDF sambil secara otomatis mengubah ukuran dan memperluas font untuk mengisi area persegi tertentu. Menggunakan pustaka Aspose.PDF untuk Python via .NET, kode secara dinamis menyesuaikan ukuran font dan spasi sehingga konten teks baru pas secara sempurna dalam kotak pembatas yang ditentukan — tanpa perhitungan font manual.

1. Muat PDF.
1. Tangkap Fragmen Teks.
1. Pilih Fragmen Spesifik.
1. Tentukan Persegi Target.
1. Aktifkan Opsi Penyesuaian Teks.
1. Ganti Teks.
1. Simpan Dokumen.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_and_resize_and_expand_font(infile, outfile):
    """
    Resize and expand font to fill target area.

    Demonstrates automatic font scaling to fill a specified rectangular area.
    The font size is dynamically adjusted to make the text content fit
    perfectly within the defined target rectangle.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Defines target rectangle at coordinates (100, 300, 512, 692)
        - Uses SCALE_TO_FILL for automatic font size adjustment
        - Duplicates original text content
        - Adjusts space width for optimal text distribution
        - Font size scales up or down to fill the entire rectangle

    Example:
        >>> replace_text_and_resize_and_expand_font("input.pdf", "output.pdf")
        # Scales font to completely fill the specified rectangular area
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        fragment.replace_options.rectangle = ap.Rectangle(100, 300, 512, 692, True)
        fragment.replace_options.replace_adjustment_action = (
             ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.replace_options.font_size_adjustment_action = (
            ap.text.TextReplaceOptions.FontSizeAdjustment.SCALE_TO_FILL
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)

```

### Ganti Teks dan Sesuaikan ke dalam Persegi

Ganti teks dalam dokumen PDF sambil memastikan konten baru cocok dalam area persegi asli teks dengan secara otomatis mengurangi ukuran font bila diperlukan.

Menggunakan pustaka Aspose.PDF untuk Python via .NET, fungsi ini menyesuaikan tata letak teks dan ukuran font secara dinamis, mempertahankan struktur dokumen sambil mencegah overflow.

1. Buat objek TextFragmentAbsorber untuk mengekstrak semua fragmen teks dari halaman pertama.
1. Akses Fragmen Teks Spesifik.
1. Tetapkan Area Pengganti.
1. Konfigurasikan Opsi Penyesuaian Teks. Atur dua opsi penggantian utama:
- Penyesuaian ukuran font - 'SHRINK_TO_FIT' secara otomatis mengurangi ukuran font jika teks baru terlalu panjang.
- Penyesuaian spasi - 'ADJUST_SPACE_WIDTH' menjaga spasi tetap proporsional.
1. Ganti Teks.
1. Simpan PDF yang Telah Diubah.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_and_fit_text_into_rectangle(infile, outfile):
    """
    Fit text into a rectangle by adjusting font size.

    Demonstrates how to ensure text content fits within its original
    rectangle by automatically shrinking the font size when the new
    content is longer than the original.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses original text fragment rectangle as target area
        - Employs SHRINK_TO_FIT to reduce font size if needed
        - Duplicates original text content (making it longer)
        - Adjusts space width for proper text distribution
        - Prevents text overflow by automatic font scaling

    Example:
        >>> replace_text_and_fit_text_into_rectangle("input.pdf", "output.pdf")
        # Shrinks font size to fit doubled text content in original space
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        fragment.replace_options.rectangle = fragment.rectangle
        fragment.replace_options.font_size_adjustment_action = (
            ap.text.TextReplaceOptions.FontSizeAdjustment.SHRINK_TO_FIT
        )
        fragment.replace_options.replace_adjustment_action = (
            ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH

        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### Secara Otomatis Ganti Teks Placeholder dan Atur Ulang Tata Letak PDF

Ganti teks placeholder dalam PDF (misalnya, templat atau formulir) dengan data nyata seperti nama atau informasi perusahaan.
Ini secara otomatis menyesuaikan tata letak halaman agar cocok dengan teks baru sambil menerapkan pemformatan khusus (font, warna, ukuran).

1. Impor dan Muat PDF.
1. Buat Text Absorber untuk Placeholder.
1. Terapkan Absorber ke Semua Halaman.
1. Loop Melalui Fragmen Teks yang Ditemukan.
1. Terapkan Pemformatan Teks Kustom.
1. Simpan Dokumen yang Diperbarui.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def automatically_rearrange_page_contents(input_file, output_file):
    """
    Replace placeholder text in PDF with actual content.

    Demonstrates how to replace long placeholder text with actual content
    and automatically rearrange page layout. Shows dynamic content replacement
    with custom formatting applied to the new text.

    Args:
        input_file (str): Path to the input PDF file containing placeholders.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Searches for "[Long_placeholder_Long_placeholder]" placeholders
        - Replaces with either "John Smith" or extended version with studio info
        - Applies Calibri font, size 12, navy blue color
        - Automatically adjusts page layout to accommodate content changes
        - Demonstrates real-world template filling scenarios

    Example:
        >>> automatically_rearrange_page_contents("template.pdf", "filled.pdf")
        # Replaces placeholders with formatted actual content
    """
    document = ap.Document(input_file)

    absorber = ap.text.TextFragmentAbsorber("[Long_placeholder_Long_placeholder]")
    document.pages.accept(absorber)

    for text_fragment in absorber.text_fragments:
        # text_fragment.text = "John Smith"
        text_fragment.text = "John Smith, South Development Studio"
        text_fragment.text_state.font = ap.text.FontRepository.find_font("Calibri")
        text_fragment.text_state.font_size = 12
        text_fragment.text_state.foreground_color = ap.Color.navy

    # Save PDF document
    document.save(output_file)
```

### Ganti Teks Berdasarkan Ekspresi Reguler

Saat bekerja dengan dokumen PDF, Anda mungkin perlu mengganti teks yang mengikuti pola tertentu bukan frasa spesifik — misalnya, nomor telepon, kode, atau format seperti tanggal.

Aspose.PDF untuk Python via .NET memungkinkan Anda melakukan penggantian semacam itu menggunakan ekspresi reguler (regex) dengan kelas TextFragmentAbsorber.

Contoh ini menunjukkan cara menemukan pola teks (dalam kasus ini, teks apa pun yang cocok dengan format ####-####, seperti 1234-5678) dan menggantinya dengan string terformat 'ABC1-2XZY'. Ini juga menunjukkan cara menyesuaikan font, warna, dan ukuran teks yang diganti.

Potongan kode berikut menunjukkan cara mengganti teks berdasarkan ekspresi reguler.

1. Muat Dokumen PDF.
1. Buat Regex-Based Text Absorber. Inisialisasi TextFragmentAbsorber dengan pola ekspresi reguler.
1. Aktifkan Mode Ekspresi Reguler. Parameter 'True' mengaktifkan mode pencarian ekspresi reguler.
1. Terapkan Absorber ke Halaman. Ini memindai halaman untuk semua fragmen teks yang cocok dengan pola regex yang ditentukan.
1. Ganti setiap kecocokan dengan teks baru dan terapkan styling kustom.
1. Simpan Dokumen yang Telah Diubah.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_based_on_regex(infile, outfile):
    """
    Replace text based on a regular expression pattern.

    Demonstrates pattern-based text replacement using regular expressions
    to find and replace text that matches specific formats. Also shows
    how to apply formatting changes to the replaced text.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses regex pattern r"\\d{4}-\\d{4}" to find 4-digit-4-digit patterns
        - Replaces matched patterns with "ABC1-2XZY"
        - Applies custom formatting: Verdana font, size 12, blue text
        - Sets light green background color for replaced text
        - Enables regex mode with TextSearchOptions(True)

    Example:
        >>> replace_text_based_on_regex("input.pdf", "output.pdf")
        # Replaces patterns like "1234-5678" with formatted "ABC1-2XZY"
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(r"\d{4}-\d{4}")
        absorber.text_search_options = ap.text.TextSearchOptions(True)
        document.pages[1].accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = "ABC1-2XZY"
            fragment.text_state.font = ap.text.FontRepository.find_font("Verdana")
            fragment.text_state.font_size = 12
            fragment.text_state.foreground_color = ap.Color.blue
            fragment.text_state.background_color = ap.Color.light_green

        document.save(outfile)
```

## Ganti font atau hapus font yang tidak digunakan

### Ganti font dalam file PDF yang ada

Kadang-kadang, Anda perlu menstandarkan atau memperbarui font di seluruh PDF — misalnya, mengganti font yang usang atau proprietary dengan yang lebih mudah diakses. Perpustakaan Aspose.PDF untuk Python via .NET memungkinkan Anda mendeteksi dan mengganti font secara programatik, memastikan tipografi yang konsisten serta kompatibilitas dokumen.

Contoh ini menunjukkan cara mengganti semua kemunculan font tertentu (misalnya, 'Arial-BoldMT') dengan font lain (misalnya, 'Verdana') di seluruh dokumen PDF.

Potongan kode berikut menunjukkan cara mengganti font di dalam dokumen PDF:

1. Buka Dokumen PDF.
1. Inisialisasi TextFragmentAbsorber.
1. Gunakan Absorber untuk mengekstrak fragmen teks dari setiap halaman dalam dokumen.
1. Identifikasi dan Ganti Font. Skrip memeriksa apakah font saat ini pada fragmen adalah 'Arial-BoldMT'. Jika ya, skrip menggantinya dengan font 'Verdana' menggunakan metode FontRepository.find_font().
1. Simpan Dokumen yang telah Dimodifikasi.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_fonts(infile, outfile):
    """
    Replace specific fonts in a PDF document.

    Demonstrates how to find and replace specific fonts throughout a PDF
    document. Searches for text using a particular font and changes it
    to a different font while preserving the text content.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Searches for text using "Arial-BoldMT" font
        - Replaces font with "Verdana" while keeping text content
        - Processes all text fragments across all pages
        - Maintains original text size and formatting properties
        - Useful for font standardization across documents

    Example:
        >>> replace_fonts("input.pdf", "output.pdf")
        # Changes all Arial-BoldMT text to use Verdana font instead
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        document.pages.accept(absorber)

        for fragment in absorber.text_fragments:
            if fragment.text_state.font.font_name == "Arial-BoldMT":
                fragment.text_state.font = ap.text.FontRepository.find_font("Verdana")

        document.save(outfile)
```

### Hapus font yang tidak terpakai

Seiring waktu, dokumen PDF dapat mengumpulkan font yang tidak terpakai atau tertanam yang meningkatkan ukuran file dan memperlambat pemrosesan. Font yang tidak terpakai ini sering tetap ada bahkan setelah penyuntingan atau penggantian teks, terutama saat bekerja dengan PDF yang besar atau kompleks.

Perpustakaan Aspose.PDF untuk Python via .NET menyediakan cara yang efisien untuk menghapus font berlebih tersebut menggunakan kelas TextEditOptions. Ini tidak hanya mengoptimalkan dokumen Anda tetapi juga memastikan hanya font yang benar‑benar diterapkan pada teks yang terlihat yang digunakan.

Metode 'remove_unused_fonts()' adalah cara yang sederhana namun kuat untuk mengoptimalkan file PDF dengan menghapus data font yang berlebih.

Contoh ini menunjukkan cara:

- Memindai PDF untuk font yang tidak terpakai.
- Menghapusnya dengan aman.
- Menetapkan kembali fragmen teks aktif ke font yang konsisten (misalnya, Times New Roman).

1. Buka Dokumen PDF.
1. Konfigurasikan Opsi Penyuntingan Teks. Ini memberi instruksi pada mesin untuk menghilangkan semua font tertanam yang tidak sedang digunakan dalam teks yang terlihat.
1. Buat Text Absorber dengan Opsi. TextFragmentAbsorber mengekstrak fragmen teks dari dokumen untuk penyuntingan.
1. Tetapkan kembali Font Standar. Setelah absorber mengumpulkan semua fragmen, iterasi melalui mereka dan terapkan font yang konsisten.
1. Simpan PDF yang Dibersihkan.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def remove_unused_fonts(input_file, output_file):
    """
    Remove unused fonts from a PDF document.

    Optimizes PDF file size by removing fonts that are embedded but not
    actually used in the document. Also demonstrates how to standardize
    all text to use a specific font family.

    Args:
        input_file (str): Path to the input PDF file to optimize.
        output_file (str): Path where the optimized PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses REMOVE_UNUSED_FONTS option for optimization
        - Changes all text to use TimesNewRoman font
        - Processes all text fragments across the document
        - Reduces file size by eliminating unnecessary font data
        - Useful for PDF optimization and standardization

    Example:
        >>> remove_unused_fonts("input.pdf", "optimized.pdf")
        # Removes unused fonts and standardizes text to TimesNewRoman
    """

    # Open PDF document
    document = ap.Document(input_file)

    # Initialize text edit options to remove unused fonts
    options = ap.text.TextEditOptions(ap.text.TextEditOptions.FontReplace.REMOVE_UNUSED_FONTS)

    # Create a TextFragmentAbsorber with the specified options
    absorber = ap.text.TextFragmentAbsorber(options)
    document.pages.accept(absorber)

    # Iterate through all TextFragments
    for text_fragment in absorber.text_fragments:
        text_fragment.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")

    # Save the updated PDF document
    document.save(output_file)
```

## Hapus Semua Teks

### Hapus Teks dari PDF

Hapus semua konten teks dari file PDF sambil mempertahankan gambar, bentuk, dan struktur tata letak tetap utuh.
Dengan menggunakan TextFragmentAbsorber, kode secara efisien memindai seluruh dokumen dan menghapus setiap fragmen teks yang ditemukan pada masing‑masing halaman.

1. Muat Dokumen PDF.
1. Objek TextFragmentAbsorber dibuat untuk mendeteksi dan menangani fragmen teks dalam PDF.
1. Hapus Semua Konten Teks. Metode 'absorber.remove_all_text()' menghapus setiap elemen teks dari dokumen yang dimuat, meninggalkan komponen non‑teks tidak tersentuh.
1. Simpan Dokumen yang Diperbarui.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def remove_all_text_using_absorber1(infile, outfile):
    """
    Remove all text from a PDF using TextFragmentAbsorber.

    Demonstrates complete text removal from an entire PDF document,
    leaving only non-text elements like images, shapes, and layout
    structures intact.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the text-free PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Removes all text content from the entire document
        - Preserves images, graphics, and page structure
        - Uses document-level text removal for complete cleanup
        - Useful for creating templates or removing sensitive text
        - Maintains page layout and non-text elements

    Example:
        >>> remove_all_text_using_absorber1("input.pdf", "no_text.pdf")
        # Creates a PDF with all text removed but graphics preserved
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(document)
        document.save(outfile)
```

### Hapus Semua Teks dari Halaman Spesifik

Hapus semua teks dari satu halaman dokumen PDF menggunakan kelas TextFragmentAbsorber dalam Aspose.PDF.
Berbeda dengan penghapusan seluruh dokumen, metode ini melakukan pembersihan teks pada tingkat halaman, menghapus teks hanya dari halaman yang dipilih sementara halaman lainnya tetap tidak berubah.

1. Muat File PDF.
1. Buat Instance TextFragmentAbsorber.
1. Hapus Semua Teks dari Halaman Pertama.
1. Simpan PDF yang Dimodifikasi.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def remove_all_text_using_absorber2(infile, outfile):
    """
    Remove all text from page using TextFragmentAbsorber.

    Demonstrates text removal from a specific page while leaving text
    on other pages intact. Useful for selective text cleanup or
    creating mixed-content documents.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Removes text only from the first page (pages[1])
        - Preserves text content on all other pages
        - Maintains page structure and non-text elements
        - Useful for page-specific text removal operations
        - Images and graphics on the target page remain intact

    Example:
        >>> remove_all_text_using_absorber2("input.pdf", "first_page_clean.pdf")
        # Removes all text from first page only
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(document.pages[1])
        document.save(outfile)
```

### Hapus Semua Teks dari Area Tertentu pada Halaman PDF

Hapus semua teks dari area persegi panjang tertentu pada sebuah halaman menggunakan TextFragmentAbsorber dari Aspose.PDF.
Alih-alih membersihkan seluruh halaman, metode ini melakukan penghapusan teks yang ditargetkan, memungkinkan kontrol presisi atas bagian halaman mana yang terpengaruh.

1. Muat Dokumen PDF.
1. Buat TextFragmentAbsorber.
1. Tentukan Area Target (Persegi Panjang).
1. Hapus Teks dari Wilayah yang Ditetapkan.
1. Pertahankan Sisanya Dokumen.
1. Simpan PDF yang Dimodifikasi.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def remove_all_text_using_absorber3(infile, outfile):
    """
    Remove all text from particular area on PDF page using TextFragmentAbsorber.

    Demonstrates precise text removal from a specific rectangular region
    on a page. Allows for surgical text removal while preserving text
    outside the target area.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Removes text only within rectangle (10, 200, 120, 600)
        - Targets the first page only (pages[1])
        - Preserves text outside the specified rectangle
        - Maintains all non-text elements in the region
        - Useful for removing watermarks, headers, or specific sections

    Example:
        >>> remove_all_text_using_absorber3("input.pdf", "region_clean.pdf")
        # Removes text only from the specified rectangular area
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(document.pages[1], ap.Rectangle(10, 200, 120, 600))
        document.save(outfile)
```

### Hapus Semua Teks tersembunyi dari dokumen PDF

Hapus semua teks dari area persegi panjang tertentu pada sebuah halaman menggunakan TextFragmentAbsorber dari Aspose.PDF.
Alih-alih membersihkan seluruh halaman, metode ini melakukan penghapusan teks yang ditargetkan, memungkinkan kontrol presisi atas bagian halaman mana yang terpengaruh.

1. Muat Dokumen PDF.
1. Buat TextFragmentAbsorber.
1. Tentukan Area Target (Persegi Panjang).
1. Hapus Teks dari Wilayah yang Ditentukan.
1. Pertahankan Sisanya Dokumen.
1. Simpan PDF yang Dimodifikasi.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def remove_hidden_text(infile, outfile):
    """
    Remove all hidden (invisible) text from a PDF document.

    Identifies and removes text that has been marked as invisible while
    preserving all visible text content. Useful for cleaning documents
    that may contain hidden tracking text or metadata.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the cleaned PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Detects text fragments with invisible text state
        - Replaces hidden text with empty strings
        - Uses NONE replacement adjustment to prevent layout shifts
        - Preserves all visible text and document structure
        - Useful for privacy and security document cleanup

    Example:
        >>> remove_hidden_text("input.pdf", "no_hidden_text.pdf")
        # Removes all invisible text while keeping visible content intact
    """
    # Open PDF document
    with ap.Document(infile) as document:
        text_absorber = ap.text.TextFragmentAbsorber()
        # This option can be used to prevent other text fragments from moving after hidden text replacement
        text_absorber.text_replace_options = ap.text.TextReplaceOptions(ap.text.TextReplaceOptions.ReplaceAdjustment.NONE)
        document.pages.accept(text_absorber)
        # Remove hidden text
        for fragment in text_absorber.text_fragments:
            if fragment.text_state.invisible:
                fragment.text = ""
        # Save PDF document
        document.save(outfile)
```
