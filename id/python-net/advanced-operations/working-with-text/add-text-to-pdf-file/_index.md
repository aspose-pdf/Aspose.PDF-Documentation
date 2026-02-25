---
title: Menambahkan Teks ke PDF
linktitle: Tambah Teks ke PDF
type: docs
weight: 10
url: /id/python-net/add-text-to-pdf-file/
description: Artikel ini menjelaskan berbagai aspek bekerja dengan teks di Aspose.PDF. Pelajari cara menambahkan teks ke PDF, menambahkan fragmen HTML, atau menggunakan font OTF khusus.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Menambahkan Teks ke PDF menggunakan Python
Abstract: Artikel ini memberikan panduan komprehensif tentang memanipulasi dokumen PDF menggunakan library Aspose.PDF dalam Python. Ini mencakup berbagai teknik untuk menambahkan dan memformat teks, termasuk mengatur properti teks seperti ukuran font, jenis, warna, dan posisi.
---

Panduan ini menjelaskan cara menambahkan konten teks ke dokumen PDF menggunakan Aspose.PDF untuk Python via .NET. Anda akan mempelajari teknik dasar penyisipan teks—dari menempatkan fragmen teks sederhana pada posisi tertentu, hingga menata gaya (font, ukuran, warna, gaya), menangani bahasa kanan-ke-kiri (RTL), menyematkan hyperlink, dan bekerja dengan tata letak paragraf, daftar, serta efek transparansi. Artikel ini juga mencakup skenario lanjutan seperti menggunakan fragmen HTML atau LaTeX, font khusus, dan opsi pemformatan teks seperti spasi baris dan spasi karakter.

Apakah Anda membangun anotasi sederhana atau tata letak tipografi yang kaya, sumber daya ini membekali Anda dengan blok bangunan dasar untuk bekerja dengan teks dalam PDF menggunakan Aspose.PDF.

## Penyisipan teks dasar

Aspose.PDF untuk Python via .NET menyediakan API yang kuat dan fleksibel untuk menangani teks di dalam file PDF.
Apakah Anda memerlukan label statis sederhana, konten berformat kaya, teks multibahasa, atau hyperlink interaktif, toolkit ini memungkinkan Anda melakukan semuanya dengan kode Python yang singkat.

### Tambah Teks Kasus Sederhana

Aspose.PDF untuk Python via .NET menunjukkan cara menambahkan fragmen teks sederhana ke posisi tertentu pada halaman. Anda akan belajar cara membuat dokumen PDF baru, menambahkan halaman, menyisipkan teks pada koordinat yang diberikan, dan menyimpan file yang dihasilkan.

1. Buat objek [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) baru.
1. Gunakan `document.pages.add()` untuk membuat [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) kosong baru.
1. Buat [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) dengan konten teks.
1. Atur posisi teks menggunakan kelas [`Position`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/position/). Jika Anda menentukan `Position`, teks akan ditempatkan dalam dokumen Anda dari kiri ke kanan dan bergeser ke bawah.
1. Sesuaikan penampilan teks. Anda dapat mengatur ukuran font, warna, gaya font, dan lainnya melalui [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/).
1. Tambahkan `TextFragment` ke koleksi paragraf halaman dengan `page.paragraphs.add(text_fragment)`.
1. Simpan dokumen.

Cuplikan kode berikut menunjukkan cara menambahkan teks dalam file PDF yang ada:

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_simple_case(outfile):
    """
    Add simple text to a PDF document.
    Creates a new PDF document with a single page and adds a text fragment
    "Hello, Aspose!" at position (100, 600) on the page.
    Args:
        outfile (str): The file path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file.
    Example:
        >>> add_text_simple_case("output.pdf")
        # Creates a PDF file named "output.pdf" with "Hello, Aspose!" text
    """

    # Create a new document
    document = ap.Document()
    page = document.pages.add()

    # Add a text fragment at a specific position
    text_fragment = ap.text.TextFragment("Hello, Aspose!")
    text_fragment.position = ap.text.Position(100, 600)

    page.paragraphs.add(text_fragment)
    document.save(outfile)
```

Contoh kode ini menggunakan TextFragment. Tetapi Anda juga dapat menambahkan teks ke halaman PDF menggunakan TextParagraph. Mari kita jelajahi perbedaannya.
**[TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/)** adalah satu potongan teks. TextFragment mewakili unit teks tunggal — pada dasarnya, satu string teks yang dapat ditempatkan, diberikan gaya, dan diposisikan secara independen. Ini ideal ketika Anda perlu menambahkan teks sederhana dalam jumlah kecil.

**[TextParagraph](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/)** adalah kumpulan TextFragment. Itu dapat menambahkan beberapa baris teks. TextParagraph adalah wadah atau koleksi satu atau lebih objek TextFragment. Ini ideal ketika Anda perlu mengelompokkan beberapa fragmen — misalnya, untuk membuat blok teks dengan beberapa baris, kata, atau elemen berformat.
TextParagraph juga mengelola perataan teks, spasi baris, dan tata letak otomatis pada halaman. Penggunaan garis merah hanya dimungkinkan dengan TextParagraph.

Untuk informasi lebih lanjut tentang Bekerja dengan Teks, silakan periksa bagian dokumentasi [Text Formatting inside PDF](/pdf/python-net/text-formatting-inside-pdf/) dan [Extract Text from PDF using Python](/pdf/python-net/extract-text-from-pdf/).

### Tambah Teks menggunakan TextParagraph

Aspose.PDF untuk Python via .NET dapat menambahkan paragraf teks menggunakan [`TextBuilder`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textbuilder/) dan [`TextParagraph`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/) dengan opsi pembungkusan.

1. Buat [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) baru dan [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) kosong menggunakan `document.pages.add()`.
1. Baca teks dari file atau gunakan teks default.
1. Buat [`TextBuilder`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textbuilder/) untuk menambahkan konten tingkat paragraf dengan kontrol tata letak dan pembungkusan.
1. Buat [`TextParagraph`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/) dan atur mode pembungkusan (contoh menggunakan `DISCRETIONARY_HYPHENATION`).
1. Buat [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/), terapkan gaya, dan tambahkan fragmen ke paragraf.
1. Tambahkan paragraf ke halaman menggunakan `TextBuilder`.
1. Simpan dokumen.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_paragraph(outfile):
    """
    Add formatted text paragraph with indentation and wrapping to a PDF document.

    Creates a PDF document with a text paragraph that demonstrates advanced text
    formatting including first line indentation, text wrapping with discretionary
    hyphenation, and loading text content from an external file.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Attempts to load text from "lorem.txt" file in DATA_DIR
        - Falls back to default message if file doesn't exist
        - Uses Times New Roman font at 12pt size
        - First line indent: 20 points
        - Rectangle bounds: (80, 800, 400, 200)
        - Text wrapping: DISCRETIONARY_HYPHENATION mode for better line breaks

    Example:
        >>> add_text_paragraph("paragraph_text.pdf")
        # Creates a PDF with formatted paragraph text
    """
    document = ap.Document()
    page = document.pages.add()

    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    if os.path.exists(lorem_path):
        with open(lorem_path, "r", encoding="utf-8") as file:
            text = file.read()
    else:
        text = "Lorem ipsum sample text not found."

    builder = ap.text.TextBuilder(page)
    paragraph = ap.text.TextParagraph()
    paragraph.first_line_indent = 20
    paragraph.rectangle = ap.Rectangle(80, 800, 400, 200, True)
    # paragraph.formatting_options.wrap_mode = TextFormattingOptions.WordWrapMode.BY_WORDS
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.DISCRETIONARY_HYPHENATION
    )

    fragment = ap.text.TextFragment(text)
    fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    fragment.text_state.font_size = 12

    paragraph.append_line(fragment)
    builder.append_paragraph(paragraph)

    document.save(outfile)
```

![Tambah Teks menggunakan TextParagraph](text_paragraph.png)

### Tambah Paragraf dengan Inden di PDF

Cuplikan kode berikut menunjukkan cara membuat dokumen PDF baru dan menambahkan dua paragraf teks dengan gaya indentasi yang berbeda:

- Paragraf pertama menunjukkan indentasi baris pertama (hanya baris pertama yang diindentasi).

- Paragraf kedua menunjukkan indentasi baris selanjutnya (semua baris setelah yang pertama diindentasi).

Ini menggunakan kelas 'TextParagraph', 'TextBuilder', dan 'TextFragment' dari Aspose.PDF untuk mengontrol tata letak dan pemformatan secara tepat.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_paragraphs_indents(output_file_name):
    """Add text with indents to a PDF document.
    Creates a PDF document with two text paragraphs demonstrating different
    indent styles. The first paragraph uses first line indent, while the
    second paragraph uses subsequent lines indent. Text content is loaded
    from a lorem.txt file if available, otherwise uses a fallback message.
    Args:
        output_file_name (str): The file path where the PDF document will be saved.
    Returns:
        None: The function saves the PDF document to the specified output file.
    Note:
        - Uses Times New Roman font at 12pt size
        - Text wrapping is set to wrap by words
        - First paragraph: 20pt first line indent, positioned at (80, 800, 300, 50)
        - Second paragraph: 20pt subsequent lines indent, positioned at (320, 800, 500, 50)
    """

    document = ap.Document()
    page = document.pages.add()

    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    if os.path.exists(lorem_path):
        with open(lorem_path, "r", encoding="utf-8") as file:
            text = file.read()
    else:
        text = "Lorem ipsum sample text not found."

    fragment = ap.text.TextFragment(text)
    fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    fragment.text_state.font_size = 12

    builder = ap.text.TextBuilder(page)
    paragraph1 = ap.text.TextParagraph()
    paragraph1.first_line_indent = 20
    paragraph1.rectangle = ap.Rectangle(80, 800, 300, 50, True)
    paragraph1.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    paragraph1.append_line(fragment)
    builder.append_paragraph(paragraph1)

    paragraph2 = ap.text.TextParagraph()
    paragraph2.subsequent_lines_indent = 20
    paragraph2.rectangle = ap.Rectangle(320, 800, 500, 50, True)
    paragraph2.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    paragraph2.append_line(fragment)
    builder.append_paragraph(paragraph2)
    document.save(output_file_name)
```

### Tambah Baris Teks Baru di PDF

Aspose.PDF untuk Python via .NET memungkinkan Anda menyisipkan teks berbaris banyak ke dalam dokumen PDF menggunakan kelas TextFragment, TextParagraph, dan TextBuilder.

1. Buat dokumen baru.
1. Tentukan TextFragment yang berisi karakter newline.
1. Atur gaya teks.
1. Tambahkan fragmen ke paragraf.
1. Tentukan posisi paragraf.
1. Render paragraf pada halaman.
1. Simpan dokumen.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_new_line(output_file):
    """Add a new line of text to a PDF document."""
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Initialize new TextFragment with text containing required newline markers
    text_fragment = ap.text.TextFragment("Applicant Name: " + os.linesep + " Joe Smoe")

    # Set text fragment properties if necessary
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
    text_fragment.text_state.background_color = ap.Color.light_gray
    text_fragment.text_state.foreground_color = ap.Color.red

    # Create TextParagraph object
    par = ap.text.TextParagraph()

    # Add new TextFragment to paragraph
    par.append_line(text_fragment)

    # Set paragraph position
    par.position = ap.text.Position(100, 600)

    # Create TextBuilder object
    text_builder = ap.text.TextBuilder(page)

    # Add the TextParagraph using TextBuilder
    text_builder.append_paragraph(par)

    # Save PDF document
    document.save(output_file)
```

### Tentukan Pemotongan Baris dan Catat Notifikasi dalam PDF

Ini menunjukkan cara membuat dokumen PDF yang berisi beberapa fragmen teks dan mengaktifkan pencatatan notifikasi Aspose.PDF untuk memantau peristiwa tata letak — seperti pemotongan baris dan pembungkusan teks — selama proses rendering.

1. Buat dokumen PDF baru.
1. Aktifkan pencatatan notifikasi.
1. Gunakan document.pages.add() untuk membuat halaman pertama.
1. Tambahkan beberapa fragmen teks.
1. Gunakan page.paragraphs.add(text) untuk merender setiap fragmen teks.
1. Simpan dokumen.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def determine_line_break(output_file):
    """Create a PDF document with multiple text fragments and log notifications."""
    # Create PDF document
    document = ap.Document()

    # Enable notification logging
    document.enable_notification_logging = True

    page = document.pages.add()

    for i in range(4):
        text = ap.text.TextFragment(
            "Lorem ipsum \r\ndolor sit amet, consectetur adipiscing elit, "
            "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
            "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris "
            "nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in "
            "reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla "
            "pariatur. Excepteur sint occaecat cupidatat non proident, sunt in "
            "culpa qui officia deserunt mollit anim id est laborum."
        )
        text.text_state.font_size = 20
        page.paragraphs.add(text)

    # Save PDF document
    document.save(output_file)

    notifications = document.pages[1].get_notifications()
    print(notifications)
```

### Ukur Lebar Teks secara Dinamis dalam PDF

Ukur secara dinamis lebar karakter dan string dalam font tertentu menggunakan Aspose.PDF untuk Python via .NET. Ini menggunakan metode 'Font.measure_string()' dan 'TextState.measure_string()' untuk memverifikasi bahwa lebar string yang diukur konsisten dan akurat.

1. Gunakan 'FontRepository.find_font()' untuk mengambil objek font Arial dari repositori.
1. Buat objek TextState untuk mengelola properti font.
1. Ukur Karakter Individual.
1. Bandingkan hasil kedua metode untuk semua karakter antara 'A' dan 'z'.
1. Pastikan kedua pendekatan pengukuran menghasilkan hasil yang sama.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_text_width_dynamically(output_file):

    font = ap.text.FontRepository.find_font("Arial")
    ts = ap.text.TextState()
    ts.font = font
    ts.font_size = 14

    if math.fabs(font.measure_string("A", 14) - 9.337) > 0.001:
        print("Unexpected font string measure!")

    if math.fabs(ts.measure_string("z") - 7.0) > 0.001:
        print("Unexpected font string measure!")

    c_code = ord("A")
    while c_code <= ord("z"):
        c = chr(c_code)

        fn_measure = font.measure_string(str(c), 14)
        ts_measure = ts.measure_string(str(c))

        if math.fabs(fn_measure - ts_measure) > 0.001:
            print("Font and state string measuring doesn't match!")

        c_code += 1
```

### Tambahkan Teks dengan Tautan Hiper

Tambahkan tautan hiper yang dapat diklik ke teks dalam PDF menggunakan Aspose.PDF untuk Python via .NET. Perpustakaan kami menunjukkan cara menambahkan beberapa segmen teks dalam satu TextFragment dan menerapkan tautan hiper ke segmen tertentu, serta menata segmen teks secara individual (misalnya, warna, font miring).

1. Buat dokumen dan halaman baru menggunakan 'Document()', dan 'document.pages.add()' untuk menambahkan halaman kosong.
1. Buat sebuah TextFragment.
1. Tambahkan beberapa objek TextSegment. Setiap segmen dapat memiliki konten dan gaya masing-masing. Misalnya teks biasa atau teks tautan hiper.
1. Terapkan tautan hiper ke sebuah segmen. Buat objek WebHyperlink dengan URL yang diinginkan.
1. Atur gaya segmen. Sesuaikan warna, gaya font, ukuran, dll., menggunakan text_state.
1. Tambahkan fragmen ke halaman menggunakan 'page.paragraphs.add()'.
1. Simpan PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_with_hyperlink(outfile):
    """
    Add text with embedded hyperlinks to a PDF document.

    Creates a PDF document with a text fragment containing multiple segments,
    including one with a hyperlink to Aspose. Demonstrates how to create
    clickable links within PDF text content with different formatting.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Creates 4 text segments within a single text fragment
        - One segment contains a hyperlink to "https://products.aspose.com/pdf"
        - Hyperlinked text is styled in blue italic font
        - Other segments are regular text without links

    Example:
        >>> add_text_with_hyperlink("hyperlink_text.pdf")
        # Creates a PDF with clickable Aspose link in the text
    """

    document = ap.Document()
    page = document.pages.add()

    fragment = ap.text.TextFragment(
        "Sample Text Fragment"
    )

    segment = ap.text.TextSegment(" ... Text Segment 1...")
    fragment.segments.append(segment)

    segment = ap.text.TextSegment("Link to Aspose")
    fragment.segments.append(segment)
    segment.hyperlink = ap.WebHyperlink("https://products.aspose.com/pdf")
    segment.text_state.foreground_color = ap.Color.blue
    segment.text_state.font_style = ap.text.FontStyles.ITALIC

    segment = ap.text.TextSegment("TextSegment without hyperlink")
    fragment.segments.append(segment)

    page.paragraphs.add(fragment)
    document.save(outfile)
```

![Fragmen teks yang ditampilkan dalam PDF menunjukkan konten campuran dengan Sample Text Fragment diikuti oleh Text Segment 1, kemudian teks berwarna biru dengan tautan hiper bertuliskan Link to Aspose (menautkan ke https://products.aspose.com/pdf), dan diakhiri dengan TextSegment tanpa tautan dalam format teks hitam biasa](hyperlink_text.png)

### Tambahkan Teks Right-to-Left (RTL) ke Dokumen PDF

RTL (Right To Left) adalah properti yang menunjukkan arah penulisan teks, di mana teks ditulis dari kanan ke kiri.
Aspose.PDF untuk Python via .NET. menunjukkan cara menambahkan teks Right-to-Left (RTL), seperti Bahasa Arab atau Ibrani, ke dokumen PDF.

1. Buat dokumen dan halaman baru menggunakan 'Document()', dan 'document.pages.add()' untuk menambahkan halaman kosong.
1. Buat sebuah TextFragment dengan konten RTL. Masukkan teks Bahasa Arab, Ibrani, atau bahasa RTL lain sebagai konten fragmen.
Atur font dan gaya. Pilih font yang mendukung skrip RTL (mis., Tahoma, Arial Unicode MS). Atur font_size dan foreground_color sesuai kebutuhan.
1. Atur perataan horizontal ke kanan menggunakan 'text_fragment.horizontal_alignment'.
1. Tambahkan fragmen teks ke halaman.
1. Simpan dokumen PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_with_rtl_text(outfile):
    """
    Add right-to-left (RTL) text to a PDF document.

    Creates a PDF document with Arabic text that demonstrates right-to-left text
    rendering and alignment. The text uses the Tahoma font which supports Arabic
    characters and is aligned to the right side of the page.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses Tahoma font at 14pt size for proper Arabic character support
        - Text color is set to blue
        - Horizontal alignment is set to RIGHT for proper RTL display
        - The Arabic text describes Nasreddin Hodja, a folklore character

    Example:
        >>> add_text_with_rtl_text("arabic_text.pdf")
        # Creates a PDF with right-to-left Arabic text
    """

    document = ap.Document()
    page = document.pages.add()
    # Styled text fragment
    text_fragment = ap.text.TextFragment(
        "يعتبر خوجا نصر الدين شخصية فولكلورية من الشرق الإسلامي وبعض شعوب البحر الأبيض المتوسط ​​والبلقان، وهو بطل القصص والحكايات القصيرة الفكاهية والساخرة، وأحيانًا الحكايات اليومية."
    )
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Tahoma")
    text_fragment.text_state.font_size = 14
    text_fragment.text_state.foreground_color = ap.Color.blue
    text_fragment.horizontal_alignment = ap.HorizontalAlignment.RIGHT

    page.paragraphs.add(text_fragment)
    document.save(outfile)
```

![Teks Right-to-Left](rtl_text.png)

## Penataan teks

### Tambahkan Teks dengan Penataan Font

Ini adalah contoh yang lebih maju yang menunjukkan penataan teks, penyesuaian font, dan teks dengan format campuran (menggunakan segmen teks subskrip). Aspose.PDF menjelaskan cara menerapkan properti font seperti keluarga font, ukuran, warna, tebal, miring, dan garis bawah ke sebuah fragmen teks.
Selain itu, potongan kode ini menunjukkan cara menggunakan beberapa segmen teks dalam satu fragmen untuk membuat ekspresi teks kompleks — misalnya, menyertakan karakter subskrip atau superskrip, yang sering diperlukan dalam rumus atau notasi ilmiah.

1. Buat dokumen dan halaman baru menggunakan 'Document()', dan 'document.pages.add()' untuk menambahkan halaman kosong.
1. Buat sebuah TextFragment untuk teks bergaya sederhana.
1. Tentukan konten teks.
1. Atur posisi menggunakan koordinat Position(x, y).
1. Terapkan gaya melalui properti 'text_state' - font, font_size, foreground_color, font_style, underline.
1. Buat ekspresi kompleks dengan beberapa objek TextSegment. Setiap TextSegment mewakili bagian teks yang dapat memiliki gaya sendiri. Ini memungkinkan Anda membuat ekspresi, seperti rumus matematika atau kimia.
1. Definisikan beberapa objek TextState. Satu untuk teks utama (text_state_letters). Lainnya untuk teks subskrip atau superskrip (text_state_index).
1. Gabungkan segmen teks. Tambahkan setiap segmen ke 'TextFragment' menggunakan 'segments.append()'.
1. Tambahkan kedua objek teks ke halaman. Gunakan 'page.paragraphs.add()' untuk menempatkannya dalam dokumen.
1. Simpan dokumen akhir.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_with_font_styling(outfile):
    """
    Add styled text fragments to a PDF document.
    Creates a new PDF document with a single page and adds a styled text fragment
    "Hello, Aspose!" at position (100, 600) and a formula with styled segments at position (100, 500).
    Args:
        outfile (str): The file path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file.
    Example:
        >>> add_text_with_font_styling("styled_text.pdf")
        # Creates a PDF file named "styled_text.pdf" with styled text and a formula
    """

    document = ap.Document()
    page = document.pages.add()

    # Initialize an empty TextFragment to build a formula using segments
    formula = ap.text.TextFragment()
    text_fragment = ap.text.TextFragment("Hello, Aspose!")
    text_fragment.position = ap.text.Position(100, 600)
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.text_state.foreground_color = ap.Color.blue
    text_fragment.text_state.font_style = (
        ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    )
    text_fragment.text_state.underline = True
    text_fragment.horizontal_alignment = ap.HorizontalAlignment.LEFT

    text_state_letters = ap.text.TextState()
    text_state_letters.font = ap.text.FontRepository.find_font("Arial")
    text_state_letters.font_size = 14
    text_state_letters.foreground_color = ap.Color.blue
    text_state_letters.font_style = ap.text.FontStyles.BOLD

    text_state_index = ap.text.TextState()
    text_state_index.font = ap.text.FontRepository.find_font("Arial")
    text_state_index.font_size = 14
    text_state_index.foreground_color = ap.Color.dark_red
    # text_state_index.superscript = True
    text_state_index.subscript = True

    position = ap.text.Position(100, 500)

    # Helper function to add segments
    def add_segment(text, state):
        seg = ap.text.TextSegment(text)
        seg.text_state = state
        seg.position = position
        formula.segments.append(seg)

    add_segment("S = a", text_state_letters)
    add_segment("2n", text_state_index)
    add_segment(" + a", text_state_letters)
    add_segment("2n+1", text_state_index)
    add_segment(" + a", text_state_letters)
    add_segment("2n+2", text_state_index)
    formula.horizontal_alignment = ap.HorizontalAlignment.LEFT

    page.paragraphs.add(text_fragment)
    page.paragraphs.add(formula)
    document.save(outfile)
```

![Fragmen teks yang ditampilkan dengan font Arial miring biru yang berisi teks Hello, Aspose! diikuti oleh formula matematika yang menunjukkan S = a subskrip 2n + a subskrip 2n+1 + a subskrip 2n+2 dengan teks utama biru dan format subskrip merah](styled_text.png)

## Tambahkan Teks transparan

Tambahkan bentuk semi-transparan dan teks ke dokumen PDF menggunakan Aspose.PDF untuk Python.
Ini membuat persegi panjang berwarna dengan opasitas parsial dan menimpa TextFragment dengan warna latar depan transparan.

1. Inisialisasi objek Document dan tambahkan halaman kosong untuk menggambar konten.
1. Gunakan 'ap.drawing.Graph' untuk membuat kanvas yang memungkinkan Anda menggambar bentuk.
1. Tambahkan persegi panjang dengan isi semi-transparan.
1. Cegah pergeseran posisi kanvas.
1. Tambahkan kanvas ke halaman. Sisipkan bentuk grafis ke dalam koleksi paragraf halaman.
1. Buat fragmen teks transparan.
1. Sisipkan fragmen teks ke dalam koleksi paragraf halaman.
1. Simpan dokumen PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_transparent(outfile):
    """
    Add transparent text over a semi-transparent background to a PDF document.

    Creates a PDF document with a semi-transparent filled rectangle as background
    and transparent green text overlaid on top. This demonstrates how to create
    transparency effects in PDF documents using ARGB color values.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Background rectangle: 128 alpha, light purple color (0xC5, 0xB5, 0xFF)
        - Text transparency: 30 alpha, green color (0, 255, 0)
        - The canvas is set to not change position to prevent layout shifts

    Example:
        >>> add_text_transparent("transparent_output.pdf")
        # Creates a PDF with transparent text effects
    """

    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Create Graph object
    canvas = ap.drawing.Graph(100.0, 400.0)

    # Create rectangle with semi-transparent fill
    rect = ap.drawing.Rectangle(100, 100, 400, 400)
    rect.graph_info.fill_color = ap.Color.from_argb(128, 0xC5, 0xB5, 0xFF)
    canvas.shapes.add(rect)

    # Prevent position shift
    canvas.is_change_position = False
    page.paragraphs.add(canvas)

    # Create transparent text
    text = ap.text.TextFragment(
        "This is the transparent text. "
        "This is the transparent text. "
        "This is the transparent text."
    )
    text.text_state.foreground_color = ap.Color.from_argb(30, 0, 255, 0)
    page.paragraphs.add(text)

    document.save(outfile)
```

### Tambahkan Teks Tak Terlihat ke PDF

Contoh ini menunjukkan cara membuat dokumen PDF yang berisi teks terlihat dan tidak terlihat. Teks tidak terlihat tetap menjadi bagian dari struktur dokumen tetapi disembunyikan dari tampilan, membuatnya berguna untuk menyematkan metadata, tag aksesibilitas, atau konten yang dapat dicari tanpa memengaruhi tata letak.

1. Buat Dokumen PDF dan Halaman.
1. Buat fragmen teks dengan konten terlihat yang berulang.
1. Tambahkan fragmen teks kedua dan tandai sebagai tidak terlihat.
1. Simpan Dokumen.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_invisible(outfile):
    """
    Creates a PDF document with both visible and invisible text.
    This function generates a PDF file containing two text fragments:
    one visible text that will be displayed normally, and one invisible
    text that will be hidden from view but still present in the document.
    Args:
        outfile (str): The file path where the PDF document will be saved.
    Returns:
        None: The function saves the PDF to the specified file path.
    Example:
        add_text_invisible("output.pdf")
    """

    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Add visible text
    text1 = ap.text.TextFragment(
        "This is the visible text. "
        "This is the visible text. "
        "This is the visible text."
    )
    page.paragraphs.add(text1)

    # Create transparent text
    text2 = ap.text.TextFragment(
        "This is the invisible text. "
        "This is the invisible text. "
        "This is the invisible text."
    )
    text2.text_state.invisible = True
    page.paragraphs.add(text2)

    document.save(outfile)
```

### Tambahkan Teks dengan Gaya Border di PDF

Pustaka Aspose.PDF menunjukkan cara membuat dokumen PDF yang berisi fragmen teks bergaya dengan border yang terlihat. Metode ini menerapkan warna latar belakang dan latar depan, pengaturan font, serta garis (border) di sekitar persegi panjang teks untuk meningkatkan penekanan visual.

1. Buat Dokumen PDF dan Halaman.
1. Buat dan Tempatkan Fragmen Teks. Tambahkan fragmen teks dengan pesan dan atur posisinya.
1. Terapkan Gaya Teks. Atur font ke Times New Roman, ukuran 12. Terapkan latar belakang abu-abu terang dan warna latar depan (teks) merah.
1. Konfigurasikan Gaya Border.
1. Tambahkan Teks ke Halaman. Gunakan TextBuilder untuk menambahkan teks bergaya ke halaman.
1. Simpan Dokumen.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_border(output_file_name):
    """
    Add text with border styling to a PDF document.

    Creates a PDF document with a text fragment that has border styling applied.
    The text includes background color, foreground color, and a configurable
    border (stroke) around the text rectangle.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Text: "This is sample text with border."
        - Font: Times New Roman, 12pt
        - Background: Light gray
        - Foreground: Red text
        - Border: Dark red stroke around text rectangle
        - Position: (10, 700)
        - Border is only visible when draw_text_rectangle_border is True

    Example:
        >>> add_text_border("bordered_text.pdf")
        # Creates a PDF with bordered text styling
    """
    # Create PDF document
    document = ap.Document()
    # Get particular page
    page = document.pages.add()
    # Create text fragment
    text_fragment = ap.text.TextFragment("This is sample text with border.")
    text_fragment.position = ap.text.Position(10, 700)

    # Set text properties
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.background_color = ap.Color.light_gray
    text_fragment.text_state.foreground_color = ap.Color.red
    # Set StrokingColor property for drawing border (stroking) around text rectangle.
    # Note: This only affects the border if draw_text_rectangle_border is set to True.
    text_fragment.text_state.stroking_color = ap.Color.dark_red
    # Enable drawing of the text rectangle border
    text_fragment.text_state.draw_text_rectangle_border = True

    text_builder = ap.text.TextBuilder(page)
    text_builder.append_text(text_fragment)

    # Save PDF document
    document.save(output_file_name)
```

### Tambahkan Teks Coret di PDF

Tambahkan format coret (strikethrough) pada fragmen teks dalam dokumen PDF. Teks yang dicoret berguna untuk menunjukkan penghapusan, revisi, atau penekanan dalam dokumen yang dianotasi.

1. Buat dokumen dan halaman baru menggunakan 'Document()', serta 'document.pages.add()' untuk menambahkan halaman kosong.
1. Buat dan Gaya Fragmen Teks.
1. Terapkan Warna dan Format Coret. Atur latar belakang menjadi abu-abu terang, warna teks menjadi merah, dan aktifkan coret.
1. Tempatkan Teks.
1. Gunakan 'TextBuilder' untuk menambahkan teks bergaya ke halaman.
1. Simpan Dokumen.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_strikeout_text(output_file_name):
    """
    Add text with strikeout (strikethrough) formatting to a PDF document.

    Creates a PDF document with a text fragment that has strikeout formatting applied.
    The text appears with a line through it, along with additional styling including
    background color, foreground color, and bold font style.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Text: "This is sample strikeout text."
        - Font: Times New Roman, 12pt, Bold
        - Background: Light gray
        - Foreground: Red text
        - Strikeout: Enabled (line through text)
        - Position: (100, 600)

    Example:
        >>> add_strikeout_text("strikeout_text.pdf")
        # Creates a PDF with strikethrough text formatting
    """
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Create text fragment
    text_fragment = ap.text.TextFragment("This is sample strikeout text.")
    # Set text properties
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
    text_fragment.text_state.background_color = ap.Color.light_gray
    text_fragment.text_state.foreground_color = ap.Color.red
    text_fragment.text_state.strike_out = True
    text_fragment.text_state.font_style = ap.text.FontStyles.BOLD
    text_fragment.position = ap.text.Position(100, 600)

    # Create TextBuilder object
    text_builder = ap.text.TextBuilder(page)
    text_builder.append_text(text_fragment)

    # Save PDF document
    document.save(output_file_name)
```

## Efek warna lanjutan

### Menerapkan Gradien Aksial pada Teks di PDF

Aspose.PDF untuk Python via .NET memperlihatkan cara menerapkan efek gradien linear pada teks dalam dokumen PDF. Gradien aksial bertransisi secara halus dari merah ke biru di seluruh teks, menciptakan judul yang menarik secara visual. Teknik ini ideal untuk judul bergaya, branding, atau elemen dekoratif dalam tata letak dokumen PDF.

1. Inisialisasi dokumen baru dan tambahkan halaman kosong.
1. Buat dan Gaya Fragmen Teks. Tambahkan judul, atur posisi, font, dan ukuran.
1. Terapkan Shading Gradien Aksial dengan 'GradientAxialShading'. Atur warna latar depan menggunakan GradientAxialShading dari merah ke biru.
1. Tambahkan Gaya Garis Bawah.
1. Sisipkan fragmen teks bergaya ke dalam halaman.
1. Simpan Dokumen.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def apply_gradient_axial_shading_to_text(output_file_name):
    """
    Apply axial gradient shading to text in a PDF document.

    Creates a PDF document with large title text that has an axial (linear) gradient
    effect applied. The gradient transitions from red to blue in a linear fashion
    across the text. This demonstrates advanced text styling with gradient effects.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Text: "PDF TITLE"
        - Font: Arial Bold, 36pt
        - Position: (100, 600)
        - Gradient: Linear gradient from red to blue
        - Additional styling: Underlined text
        - Uses GradientAxialShading for linear gradient effect

    Example:
        >>> apply_gradient_axial_shading_to_text("gradient_axial.pdf")
        # Creates a PDF with linear gradient text effect
    """
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("PDF TITLE")
    text_fragment.position = ap.text.Position(100, 600)
    text_fragment.text_state.font_size = 36
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial Bold")

    text_fragment.text_state.foreground_color = ap.Color()
    text_fragment.text_state.foreground_color.pattern_color_space = (
        ap.drawing.GradientAxialShading(ap.Color.red, ap.Color.blue)
    )
    text_fragment.text_state.underline = True

    page.paragraphs.add(text_fragment)
    document.save(output_file_name)
```

### Menerapkan Gradien Radial pada Teks di PDF

Gradien radial menciptakan transisi warna melingkar yang memancar keluar dari pusat teks, menawarkan opsi gaya visual yang dinamis untuk judul, header, atau elemen dekoratif.

1. Inisialisasi dokumen baru dan tambahkan halaman kosong.
1. Buat dan Gaya Fragmen Teks. Tambahkan judul, atur posisi, font, dan ukuran.
1. Terapkan Gradien Radial dengan 'GradientRadialShading'. Atur warna latar depan menggunakan GradientRadialShading dari merah ke biru.
1. Tambahkan Gaya Garis Bawah.
1. Sisipkan fragmen teks yang telah digaya ke dalam halaman.
1. Simpan Dokumen.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def apply_gradient_radial_shading_to_text(output_file_name):
    """
    Apply radial gradient shading to text in a PDF document.

    Creates a PDF document with large title text that has a radial (circular) gradient
    effect applied. The gradient radiates from the center outward, transitioning from
    red to blue. This demonstrates advanced text styling with radial gradient effects.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Text: "PDF TITLE"
        - Font: Arial Bold, 36pt
        - Position: (100, 600)
        - Gradient: Radial gradient from red to blue
        - Additional styling: Underlined text
        - Uses GradientRadialShading for circular gradient effect

    Example:
        >>> apply_gradient_radial_shading_to_text("gradient_radial.pdf")
        # Creates a PDF with radial gradient text effect
    """
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("PDF TITLE")
    text_fragment.position = ap.text.Position(100, 600)
    text_fragment.text_state.font_size = 36
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial Bold")

    # Apply radial gradient shading (red to blue)
    text_fragment.text_state.foreground_color = ap.Color()
    text_fragment.text_state.foreground_color.pattern_color_space = (
        ap.drawing.GradientRadialShading(ap.Color.red, ap.Color.blue)
    )
    text_fragment.text_state.underline = True

    page.paragraphs.add(text_fragment)
    document.save(output_file_name)
```

![Terapkan gradasi radial shading](gradient_radial_shading.png)

## Fragmen HTML dan LaTeX

### Tambahkan Teks HTML ke Dokumen PDF

Pustaka Aspose.PDF untuk Python via .NET memungkinkan Anda menyisipkan konten berformat HTML ke dalam dokumen PDF menggunakan kelas HtmlFragment. Dengan menggunakan tag HTML Anda dapat merender teks yang bergaya, terstruktur, atau mirip rumus secara langsung dalam PDF.

1. Buat dokumen dan halaman baru menggunakan 'Document()', dan 'document.pages.add()' untuk menambahkan halaman kosong.
1. Buat sebuah instance dari kelas HtmlFragment dan berikan string HTML Anda sebagai parameter.
1. Tambahkan fragmen ke halaman menggunakan 'page.paragraphs.add()' untuk menyisipkan konten HTML.
1. Simpan PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_html_fragment(outfile):
    """
    Add HTML fragment with mathematical notation to a PDF document.

    Creates a PDF document containing an HTML fragment that displays mathematical
    notation using HTML tags including subscript and superscript elements.
    This demonstrates how to embed formatted HTML content directly into PDF.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses HTML <pre> tags to preserve formatting
        - Includes <sub> for subscript (2n) and <sup> for superscript (2)
        - Formula displayed: S=a₂ₙ+a²
        - HTML is rendered as formatted content within the PDF

    Example:
        >>> add_text_html_fragment("html_math.pdf")
        # Creates a PDF with HTML mathematical notation
    """

    # Create a new document
    document = ap.Document()
    page = document.pages.add()

    # Add a text fragment at a specific position
    text_fragment = ap.HtmlFragment("<pre>S=a<sub>2n</sub>+a<sup>2</sup><pre>")

    page.paragraphs.add(text_fragment)
    document.save(outfile)
```

![Tambah Teks HTML ke Dokumen PDF](html_fragment.png)

### Tambahkan fragmen HTML bergaya dengan berbagai format ke dokumen PDF

Kita dapat mendefinisikan sebuah fragmen HTML dan mengatur gaya teks secara langsung menggunakan tag HTML. Sematkan konten HTML bergaya ke dalam dokumen PDF. Potongan kode ini membuat file PDF baru, menambahkan halaman, menyisipkan fragmen HTML dengan berbagai elemen format (judul, paragraf, tautan, dan gaya inline), dan menyimpan hasilnya ke jalur yang ditentukan.

1. Menginisialisasi objek Document baru untuk merepresentasikan PDF.
1. Menambahkan halaman kosong ke dokumen tempat konten HTML akan ditempatkan.
1. Siapkan Konten HTML. String HTML berisi judul h1, paragraf berwarna hijau dengan teks tebal, miring, dan bergaris bawah, serta hyperlink ke situs web dengan ukuran font yang ditingkatkan.
1. Buat Fragmen HTML. Bungkus string HTML dalam objek HtmlFragment.
1. Sisipkan HTML ke Halaman. Menambahkan fragmen HTML ke koleksi paragraf halaman, merender HTML sebagai konten PDF asli.
1. Simpan Dokumen.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_html_fragment(outfile):
    """
    Add styled HTML fragment with various formatting to a PDF document.

    Creates a PDF document containing rich HTML content including headings,
    paragraphs with inline formatting, colored text, and hyperlinks.
    Demonstrates comprehensive HTML rendering capabilities in PDF.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Includes HTML heading (h1) with blue color styling
        - Contains paragraph with bold, italic, and underlined text
        - Features green-colored paragraph text
        - Includes styled hyperlink to Aspose website
        - All HTML styling is preserved in the PDF output

    Example:
        >>> add_html_fragment("rich_html.pdf")
        # Creates a PDF with various HTML formatting elements
    """

    document = ap.Document()
    page = document.pages.add()
    html_content = """
        <h1 style='color:blue;'>Hello, Aspose!</h1>
        <p>This is a sample paragraph with <b>bold</b>, <i>italic</i>, and <u>underlined</u> text.</p>
        <p style='color:green;'>This paragraph is green.</p>
        <a href='https://www.aspose.com' style='font-size:16px;'>Visit Aspose</a>
    """
    html_fragment = ap.HtmlFragment(html_content)
    page.paragraphs.add(html_fragment)
    document.save(outfile)
```

![Tambah Konten HTML ke Dokumen PDF](html_content.png)

### Tambahkan Fragmen HTML dengan keadaan teks yang ditimpa

Seperti yang kita lihat pada contoh sebelumnya, memungkinkan untuk mengatur gaya secara langsung dalam kode HTML. Hal ini memiliki keuntungannya, tetapi juga beberapa kekurangan. Misalkan kita bekerja dengan HTML milik pelanggan dan ingin menyatukan tampilan output kita.
Dalam kasus ini, kita dapat menimpa gaya pelanggan dengan menggunakan TextState kita sendiri, seperti yang ditunjukkan pada contoh berikut.

1. Buat dokumen dan halaman baru menggunakan 'Document()', dan 'document.pages.add()' untuk menambahkan halaman kosong.
1. Siapkan Konten HTML. String HTML berisi judul h1 dengan font Verdana, paragraf berwarna hijau dengan teks tebal, miring, dan bergaris bawah, serta hyperlink ke situs web dengan ukuran font yang lebih besar.
1. Buat Fragmen HTML. Bungkus string HTML dalam objek HtmlFragment.
1. Timpa format teks. Buat objek TextState dan atur Font, Ukuran Font, serta Warna Teks.
1. Tambahkan fragmen HTML ke koleksi paragraf halaman.
1. Simpan Dokumen.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_html_fragment_override_text_state(outfile):
    """
    Add HTML fragment with overridden text styling to a PDF document.

    Creates a PDF document with HTML content where the default text styling
    is overridden using TextState properties. This demonstrates how to apply
    global text formatting that supersedes HTML styling for consistent appearance.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - HTML includes heading, paragraphs, and links with original styling
        - TextState override applies: Arial font, 14pt size, red color
        - Override styling takes precedence over HTML inline styles
        - Useful for enforcing consistent document-wide text appearance
        - Original HTML styling is replaced by the TextState properties

    Example:
        >>> add_html_fragment_override_text_state("html_override.pdf")
        # Creates a PDF where HTML styling is overridden with red Arial text
    """

    document = ap.Document()
    page = document.pages.add()
    html_content = """
        <h1 style='color:blue;font-family:Verdana'>Hello, Aspose!</h1>
        <p>This is a sample paragraph with <b>bold</b>, <i>italic</i>, and <u>underlined</u> text.</p>
        <p style='color:green;'>This paragraph is green.</p>
        <a href='https://www.aspose.com' style='font-size:16px;'>Visit Aspose</a>
    """
    html_fragment = ap.HtmlFragment(html_content)
    html_fragment.text_state = ap.text.TextState()
    html_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    html_fragment.text_state.font_size = 14
    html_fragment.text_state.foreground_color = ap.Color.red

    page.paragraphs.add(html_fragment)
    document.save(outfile)
```

![Tambah fragmen HTML timpa keadaan teks](html_override.png)

### Tambahkan Teks LaTeX ke Dokumen PDF

Tambahkan ekspresi matematika berformat LaTeX ke dokumen PDF menggunakan kelas TeXFragment dalam Aspose.PDF untuk Python via .NET.
LaTeX adalah sistem penataan yang kuat yang banyak digunakan untuk membuat dokumen ilmiah dan matematika. Dengan menggunakan TeXFragment, Anda dapat langsung merender notasi dan simbol matematika LaTeX di dalam halaman PDF.

1. Buat dokumen dan halaman baru menggunakan 'Document()', dan 'document.pages.add()' untuk menambahkan halaman kosong.
1. Gunakan kelas TeXFragment untuk merender sintaks LaTeX secara langsung.
1. Tambahkan konten LaTeX ke tata letak PDF dengan 'page.paragraphs.add()'.
1. Simpan PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_latex_fragment(outfile):
    """
    Add LaTeX mathematical expression to a PDF document.

    Creates a PDF document containing a complex mathematical expression rendered
    from LaTeX markup. This demonstrates advanced mathematical typesetting
    capabilities using LaTeX syntax within PDF documents.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses LaTeX TeXFragment for mathematical expression rendering
        - Expression includes overbrace and underbrace notation
        - Formula: (a+b)⁶ · (c+d)⁷ with braces and labels = 42
        - LaTeX commands: \\overbrace, \\underbrace, \\text, \\cdot
        - Provides professional mathematical typography

    Example:
        >>> add_text_latex_fragment("latex_math.pdf")
        # Creates a PDF with complex LaTeX mathematical expression
    """

    # Create a new document
    document = ap.Document()
    page = document.pages.add()

    # Add a text fragment at a specific position
    text_fragment = ap.TeXFragment(
        "\\underbrace{\\overbrace{a+b}^6 \\cdot \\overbrace{c+d}^7}_\\text{example of text} = 42"
    )

    page.paragraphs.add(text_fragment)
    document.save(outfile)
```

![Ekspresi matematika kompleks yang ditampilkan dalam PDF menunjukkan rumus LaTeX dengan notasi overbrace di atas (a+b)⁶, notasi underbrace di bawah seluruh ekspresi (a+b)⁶ · (c+d)⁷, berlabel sebagai contoh teks, dan sama dengan 42. Rumus ini menunjukkan penataan matematika tingkat lanjut dengan spasi yang tepat dan gaya kurung khas render LaTeX](latex_fragment.png)

## Font khusus

### Gunakan Font khusus dari file

Contoh ini memungkinkan Anda menambahkan teks ke file PDF menggunakan font OpenType khusus di Aspose.PDF untuk Python via .NET. Ini menunjukkan cara membuat dokumen PDF baru, menempatkan teks secara tepat pada halaman, dan menerapkan pemformatan khusus seperti jenis font, ukuran, warna, dan gaya miring.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Tentukan konten teks yang ingin Anda tambahkan ke PDF.
1. Atur posisi teks.
1. Tambahkan TextFragment ke halaman.
1. Simpan dokumen PDF.

Fungsi ini tidak hanya bekerja dengan font OTF tetapi juga dengan font TTF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def use_custom_font_from_file(outfile):
    """
    Creates a PDF document with text using a custom font loaded from a file.
    This function demonstrates how to load a custom OpenType font (.otf) from the file system
    and apply it to text in a PDF document. The text is styled with blue color, italic style,
    and positioned at specific coordinates on the page.
    Args:
        outfile (str): The output file path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file path.
    Note:
        - Requires the "BriosoPro Italic.otf" font file to be present in the DATA_DIR directory
        - Uses Aspose.PDF library for PDF generation and text manipulation
        - The text fragment is positioned at coordinates (100, 600) on the page
        - Font size is set to 24 points with blue foreground color and italic style
    """

    font_path = os.path.join(DATA_DIR, "BriosoPro Italic.otf")
    document = ap.Document()
    page = document.pages.add()

    fragment = ap.text.TextFragment("Hello, Aspose!")
    fragment.position = ap.text.Position(100, 600)
    fragment.text_state.font = ap.text.FontRepository.open_font(font_path)
    fragment.text_state.font_size = 24
    fragment.text_state.foreground_color = ap.Color.blue
    fragment.text_state.font_style = ap.text.FontStyles.ITALIC

    page.paragraphs.add(fragment)
    document.save(outfile)
```

![Potongan teks yang ditampilkan dalam dokumen PDF menunjukkan Hello, Aspose! yang dirender dengan font BriosoPro miring biru, menunjukkan integrasi font OpenType khusus dan kemampuan styling dalam pemformatan teks PDF](custom_font.png)

### Gunakan Font khusus dari aliran

Potongan kode ini menunjukkan cara menambahkan teks ke dokumen PDF menggunakan font OpenType (OTF) khusus yang disematkan dengan Aspose.PDF untuk Python via .NET. Ini memperlihatkan cara membuka file font sebagai aliran, menyematkannya ke dalam PDF untuk memastikan ketersediaan font di berbagai sistem, dan menerapkan pemformatan teks seperti ukuran font, warna, dan gaya miring. Pendekatan ini ideal untuk membuat PDF yang konsisten secara visual yang mempertahankan tipografi bahkan ketika dibagikan atau dilihat pada perangkat yang tidak memiliki font yang diinstal.

1. Muat file font sebagai aliran biner.
1. Buka dan sematkan font menggunakan 'FontRepository.open_font'.
1. Buat dokumen PDF baru dan tambahkan halaman.
1. Tambahkan potongan teks bergaya dengan:
- Font khusus yang disematkan.
- Gaya miring dan warna biru.
- Ukuran font dan posisi tertentu.
1. Simpan dokumen akhir ke jalur output yang ditentukan.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def use_custom_font_from_stream(outfile):
    """Use custom font from stream."""

    font_path = os.path.join(DATA_DIR, "BriosoPro Italic.otf")
    with open(font_path, "rb") as font_stream:
        font = ap.text.FontRepository.open_font(font_stream, ap.text.FontTypes.OTF)
        font.is_embedded = True

        document = ap.Document()
        page = document.pages.add()

        fragment = ap.text.TextFragment("Hello, Aspose!")
        fragment.position = ap.text.Position(100, 600)
        fragment.text_state.font = font
        fragment.text_state.font_size = 14
        fragment.text_state.foreground_color = ap.Color.blue
        fragment.text_state.font_style = ap.text.FontStyles.ITALIC

        page.paragraphs.add(fragment)
        document.save(outfile)
```

Menyematkan font memastikan rendering yang konsisten di semua platform, menjadikan pendekatan ini ideal untuk branding, fidelitas desain, dan dukungan multibahasa.

