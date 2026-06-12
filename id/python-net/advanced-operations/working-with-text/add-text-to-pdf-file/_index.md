---
title: Tambahkan Teks ke PDF dengan Python
linktitle: Tambahkan Teks ke PDF
type: docs
weight: 10
url: /id/python-net/add-text-to-pdf-file/
description: Pelajari cara menambahkan teks, fragmen HTML, daftar, tautan, dan font khusus ke dokumen PDF dalam Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tambahkan teks, tautan, HTML, dan font ke file PDF dengan Python
Abstract: Artikel ini menjelaskan cara menambahkan dan memformat teks dalam dokumen PDF menggunakan Aspose.PDF for Python via .NET. Ini mencakup teknik inti seperti memposisikan teks, menerapkan pengaturan font dan gaya, menyisipkan tautan dan daftar, serta menggunakan HTML, LaTeX, dan font khusus dalam alur kerja Python.
---

Panduan ini menjelaskan cara menambahkan konten teks ke dokumen PDF menggunakan Aspose.PDF for Python via .NET. Anda akan mempelajari teknik penyisipan teks inti—mulai dari menempatkan fragmen teks sederhana pada posisi tertentu, hingga menata tampilannya (font, ukuran, warna, gaya), menangani bahasa right-to-left (RTL), menyematkan hyperlink, dan bekerja dengan tata letak paragraf, daftar, serta efek transparansi. Artikel ini juga mencakup skenario lanjutan seperti menggunakan fragmen HTML atau LaTeX, font kustom, dan opsi pemformatan teks seperti spasi baris dan spasi karakter.

Apakah Anda sedang membuat anotasi sederhana atau tata letak tipografi yang kaya, sumber daya ini membekali Anda dengan blok bangunan dasar untuk bekerja dengan teks dalam PDF menggunakan Aspose.PDF.

## Penyisipan teks dasar

Aspose.PDF for Python via .NET menyediakan API yang kuat dan fleksibel untuk menangani teks di dalam file PDF.
Apakah Anda membutuhkan label statis sederhana, konten yang diformat secara kaya, teks multibahasa, atau hyperlink interaktif, toolkit memungkinkan Anda melakukan semuanya dengan kode Python yang singkat.

### Tambahkan Teks Kasus Sederhana

Aspose.PDF for Python via .NET menunjukkan cara menambahkan fragmen teks sederhana ke posisi tertentu pada halaman. Anda akan belajar cara membuat dokumen PDF baru, menambahkan halaman, menyisipkan teks pada koordinat yang diberikan, dan menyimpan file hasilnya.

1. Buat yang baru [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objek.
1. Gunakan `document.pages.add()` untuk membuat yang kosong baru [Halaman](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Buat sebuah [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) dengan konten teks.
1. Atur posisi teks menggunakan [`Position`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/position/) kelas. Jika Anda menentukan `Position`, teks akan berada di dokumen Anda dari kiri ke kanan dan bergeser ke bawah.
1. Sesuaikan tampilan teks. Anda dapat mengatur ukuran font, warna, gaya font, dan lainnya melalui [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/).
1. Tambahkan `TextFragment` ke koleksi paragraf halaman dengan `page.paragraphs.add(text_fragment)`.
1. Simpan dokumen.

Potongan kode berikut menunjukkan cara menambahkan teks dalam file PDF yang sudah ada:

```python
import math
import sys
import os
import aspose.pdf as ap

# region Basic text insertion
def add_text_simple_case(output_file_name):
    # Create a new document
    document = ap.Document()
    page = document.pages.add()

    # Add a text fragment at a specific position
    text_fragment = ap.text.TextFragment("Hello, Aspose!")
    text_fragment.position = ap.text.Position(100, 600)

    page.paragraphs.add(text_fragment)
    document.save(output_file_name)
```

Contoh kode ini menggunakan TextFragment. Anda juga dapat menambahkan teks ke halaman PDF menggunakan TextParagraph.
The **[TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/)** adalah satu potongan teks. Itu mewakili satu string teks yang dapat ditempatkan, digaya, dan diposisikan secara independen. Ini ideal ketika Anda perlu menambahkan konten teks kecil dan sederhana.

The **[Paragraf Teks](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/)** adalah sekelompok TextFragments. Ini dapat menambahkan beberapa baris teks. TextParagraph adalah wadah atau kumpulan satu atau lebih objek TextFragment. Ini ideal ketika Anda perlu mengelompokkan beberapa fragmen — misalnya, untuk membuat blok teks dengan beberapa baris, kata, atau elemen yang diformat.
Sebuah TextParagraph juga mengelola perataan teks, jarak antar baris, dan tata letak otomatis pada halaman. Penggunaan garis merah hanya dapat dilakukan dengan TextParagraph.

Untuk informasi lebih lanjut tentang bekerja dengan teks, lihat [Pemformatan Teks dalam PDF](/pdf/id/python-net/text-formatting-inside-pdf/) dan [Cari dan Dapatkan Teks dari PDF](/pdf/id/python-net/search-and-get-text-from-pdf/).

### Tambahkan Teks menggunakan TextParagraph

Aspose.PDF for Python via .NET dapat menambahkan paragraf teks menggunakan [`TextBuilder`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textbuilder/) dan [`TextParagraph`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/) dengan opsi pembungkusan.

1. Buat yang baru [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) dan kosong [Halaman](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) menggunakan `document.pages.add()`.
1. Baca teks dari file atau gunakan teks default.
1. Buat sebuah [`TextBuilder`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textbuilder/) untuk menambahkan konten tingkat paragraf dengan kontrol tata letak dan pembungkusan.
1. Buat sebuah [`TextParagraph`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/) dan atur mode bungkus (contoh menggunakan `DISCRETIONARY_HYPHENATION`).
1. Buat sebuah [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/), terapkan gaya, dan tambahkan fragmen ke paragraf.
1. Tambahkan paragraf ke halaman menggunakan `TextBuilder`.
1. Simpan dokumen.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_paragraph(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    lorem_path = LOREM_PATH
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

    document.save(output_file_name)
```

![Tambahkan Teks menggunakan TextParagraph](text_paragraph.png)

### Tambahkan Paragraf dengan Inden dalam PDF

Potongan kode berikut menunjukkan cara membuat dokumen PDF baru dan menambahkan dua paragraf teks dengan gaya indentasi yang berbeda:

- Paragraf pertama menunjukkan indent baris pertama (hanya baris pertama yang diindentasi).

- Paragraf kedua menunjukkan indentasi baris berikutnya (semua baris setelah yang pertama diindentasi).

Ini menggunakan kelas 'TextParagraph', 'TextBuilder', dan 'TextFragment' dari Aspose.PDF untuk mengontrol tata letak dan pemformatan dengan tepat.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_paragraphs_indents(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    lorem_path = LOREM_PATH
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

### Tambah Baris Teks Baru dalam PDF

Aspose.PDF for Python via .NET memungkinkan Anda menyisipkan teks multi-baris ke dalam dokumen PDF menggunakan kelas TextFragment, TextParagraph, dan TextBuilder.

1. Buat dokumen baru.
1. Definisikan sebuah TextFragment yang berisi karakter baris baru.
1. Atur gaya teks.
1. Tambahkan fragmen ke paragraf.
1. Posisikan paragraf.
1. Render paragraf pada halaman.
1. Simpan dokumen.

```python
import math
import sys
import os
import aspose.pdf as ap

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

### Tentukan Pemutusan Baris dan Catat Notifikasi dalam PDF

Ini menunjukkan cara membuat dokumen PDF yang berisi beberapa fragmen teks dan mengaktifkan pencatatan notifikasi Aspose.PDF untuk memantau peristiwa tata letak — seperti pemecahan baris dan pembungkus teks — selama proses rendering.

1. Buat dokumen PDF baru.
1. Aktifkan pencatatan notifikasi.
1. Gunakan document.pages.add() untuk membuat halaman pertama.
1. Tambahkan beberapa fragmen teks.
1. Gunakan page.paragraphs.add(text) untuk merender setiap fragmen teks.
1. Simpan dokumen.

```python
import math
import sys
import os
import aspose.pdf as ap

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

### Ukur Lebar Teks Secara Dinamis di PDF

Mengukur lebar karakter dan string secara dinamis dalam font tertentu menggunakan Aspose.PDF for Python via .NET. Ini menggunakan metode 'Font.measure_string()' dan 'TextState.measure_string()' untuk memverifikasi bahwa lebar string yang diukur konsisten dan akurat.

1. Gunakan 'FontRepository.find_font()' untuk mengambil objek font Arial dari repositori.
1. Buat objek TextState untuk mengelola properti font.
1. Ukur Karakter Individu.
1. Bandingkan hasil kedua metode untuk semua karakter antara 'A' dan 'z'.
1. Pastikan kedua pendekatan pengukuran menghasilkan hasil yang sama.

```python
import math
import sys
import os
import aspose.pdf as ap

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

### Tambahkan Teks dengan Tautan

Tambahkan hyperlink yang dapat diklik ke teks dalam PDF menggunakan Aspose.PDF for Python via .NET. Perpustakaan kami menunjukkan cara menambahkan beberapa segmen teks dalam satu TextFragment dan menerapkan hyperlink ke segmen tertentu, serta menata segmen teks secara individual (mis., warna, font miring).

1. Buat dokumen baru dan halaman menggunakan 'Document()', dan 'document.pages.add()' untuk menambahkan halaman kosong.
1. Buat TextFragment.
1. Tambahkan beberapa objek TextSegment. Setiap segmen dapat memiliki konten dan gaya tersendiri. Misalnya teks biasa atau teks hyperlink.
1. Terapkan hyperlink pada segmen. Buat objek WebHyperlink dengan URL yang diinginkan.
1. Gaya segmen. Sesuaikan warna, gaya font, ukuran, dll., menggunakan text_state.
1. Tambahkan fragmen ke halaman menggunakan 'page.paragraphs.add()'.
1. Simpan PDF.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_with_hyperlink(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    fragment = ap.text.TextFragment("Sample Text Fragment")

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
    document.save(output_file_name)
```

![Fragmen teks yang ditampilkan dalam PDF menunjukkan konten campuran dengan Sample Text Fragment diikuti oleh Text Segment 1, kemudian teks biru berhipertaut yang membaca Link to Aspose (menautkan ke https://products.aspose.com/pdf), dan diakhiri dengan TextSegment tanpa hyperlink dalam format teks hitam biasa](hyperlink_text.png)

### Tambahkan Teks Right-to-Left (RTL) ke Dokumen PDF

RTL (from Right To Left) adalah properti yang menunjukkan arah penulisan teks, di mana teks ditulis dari kanan ke kiri.
Aspose.PDF for Python via .NET. menunjukkan cara menambahkan teks Right-to-Left (RTL), seperti bahasa Arab atau Ibrani, ke dokumen PDF.

1. Buat dokumen baru dan halaman menggunakan 'Document()', dan 'document.pages.add()' untuk menambahkan halaman kosong.
1. Buat TextFragment dengan konten RTL. Masukkan teks Arab, Ibrani, atau bahasa RTL lainnya sebagai konten fragmen.
Atur font dan styling. Pilih font yang mendukung skrip RTL (mis., Tahoma, Arial Unicode MS). Atur font_size dan foreground_color sesuai kebutuhan.
1. Atur perataan horizontal ke kanan menggunakan 'text_fragment.horizontal_alignment'.
1. Tambahkan fragmen teks ke halaman.
1. Simpan dokumen PDF.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_with_rtl_text(output_file_name):
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
    document.save(output_file_name)
```

![Teks Dari Kanan ke Kiri](rtl_text.png)

## Pemformatan teks

### Tambahkan Teks dengan Gaya Font

Ini adalah contoh yang lebih maju yang menunjukkan penataan teks, penyesuaian font, dan teks berformat campuran (menggunakan segmen teks subskrip). Aspose.PDF menjelaskan cara menerapkan properti font seperti keluarga font, ukuran, warna, tebal, miring, dan garis bawah ke fragmen teks.
Selain itu, cuplikan kode ini menunjukkan cara menggunakan beberapa segmen teks dalam satu fragmen untuk membuat ekspresi teks yang kompleks — misalnya, termasuk karakter subskrip atau superskrip, yang sering diperlukan dalam rumus atau notasi ilmiah.

1. Buat dokumen baru dan halaman menggunakan 'Document()', dan 'document.pages.add()' untuk menambahkan halaman kosong.
1. Buat TextFragment untuk teks bergaya sederhana.
1. Definisikan konten teks.
1. Atur posisi menggunakan koordinat Position(x, y).
1. Terapkan gaya melalui properti 'text_state' - font, font_size, foreground_color, font_style, underline.
1. Buat sebuah ekspresi kompleks dengan beberapa objek TextSegment. Setiap TextSegment mewakili bagian teks yang dapat memiliki gaya sendiri. Ini memungkinkan Anda membangun ekspresi, seperti rumus matematika atau kimia.
1. Definisikan beberapa objek TextState. Satu untuk teks utama (text_state_letters). Lainnya untuk teks subskrip atau superskrip (text_state_index).
1. Gabungkan segmen teks. Tambahkan setiap segmen ke 'TextFragment' menggunakan 'segments.append()'.
1. Tambahkan kedua objek teks ke halaman. Gunakan 'page.paragraphs.add()' untuk menempatkannya di dokumen.
1. Simpan dokumen akhir.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_with_font_styling(output_file_name):
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
    document.save(output_file_name)
```

![Fragmen teks ditampilkan dengan font Arial miring berwarna biru yang berisi teks Hello, Aspose! diikuti oleh formula matematika yang menunjukkan S = a subscript 2n + a subscript 2n+1 + a subscript 2n+2 dengan teks utama berwarna biru dan subskrip berwarna merah](styled_text.png)

## Tambahkan Teks transparan

Tambahkan bentuk semi-transparan dan teks ke dokumen PDF menggunakan Aspose.PDF for Python.
Ini membuat persegi panjang berwarna dengan opasitas parsial dan menimpa TextFragment dengan warna latar depan transparan.

1. Inisialisasi objek Document dan tambahkan halaman kosong untuk menggambar konten.
1. Gunakan 'ap.drawing.Graph' untuk membuat kanvas yang memungkinkan Anda menggambar bentuk.
1. Tambahkan persegi panjang dengan isi semi-transparan.
1. Cegah pergeseran posisi kanvas.
1. Tambahkan kanvas ke halaman. Sisipkan bentuk grafis ke dalam koleksi paragraf halaman.
1. Buat fragmen teks transparan.
1. Masukkan fragmen teks ke dalam koleksi paragraf halaman.
1. Simpan dokumen PDF.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_transparent(output_file_name):
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

    document.save(output_file_name)
```

### Tambahkan Teks Tidak Terlihat ke PDF

Contoh ini menunjukkan cara membuat dokumen PDF yang berisi teks yang terlihat dan tidak terlihat. Teks yang tidak terlihat tetap menjadi bagian dari struktur dokumen tetapi disembunyikan dari tampilan, menjadikannya berguna untuk menyisipkan metadata, tag aksesibilitas, atau konten yang dapat dicari tanpa memengaruhi tata letak.

1. Buat Dokumen PDF dan Halaman.
1. Buat fragmen teks dengan konten yang terlihat berulang.
1. Tambahkan fragmen teks kedua dan tandai sebagai tidak terlihat.
1. Simpan Dokumen.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_invisible(output_file_name):
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Add visible text
    text1 = ap.text.TextFragment(
        "This is the visible text. This is the visible text. This is the visible text."
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

    document.save(output_file_name)
```

### Tambahkan Teks dengan Gaya Garis Batas di PDF

Perpustakaan Aspose.PDF menunjukkan cara membuat dokumen PDF yang berisi fragmen teks bergaya dengan batas yang terlihat. Metode ini menerapkan warna latar belakang dan latar depan, pengaturan Font, serta goresan (batas) di sekitar persegi panjang teks untuk meningkatkan penekanan visual.

1. Buat Dokumen PDF dan Halaman.
1. Buat dan Posisikan Fragmen Teks. Tambahkan fragmen teks dengan pesan dan atur posisinya.
1. Terapkan Gaya Teks. Atur font menjadi Times New Roman, ukuran 12. Terapkan latar belakang abu-abu terang dan warna latar depan (teks) merah.
1. Konfigurasikan Gaya Border.
1. Tambahkan Teks ke Halaman. Gunakan TextBuilder untuk menambahkan teks yang bergaya ke halaman.
1. Simpan Dokumen.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_border(output_file_name):
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

### Tambahkan Teks Coret ke PDF

Tambahkan pemformatan strikeout (strikethrough) pada fragmen teks dalam dokumen PDF. Teks strikeout berguna untuk menunjukkan penghapusan, revisi, atau penekanan dalam dokumen yang dianotasi.

1. Buat dokumen baru dan halaman menggunakan 'Document()', dan 'document.pages.add()' untuk menambahkan halaman kosong.
1. Buat dan Atur Gaya Fragmen Teks.
1. Terapkan Pemformatan Warna dan Coret. Atur latar belakang menjadi abu-abu terang, warna teks menjadi merah, dan aktifkan coretan.
1. Posisikan Teks.
1. Gunakan 'TextBuilder' untuk menambahkan teks bergaya ke halaman.
1. Simpan Dokumen.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_strikeout_text(output_file_name):
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

### Menerapkan Gradien Aksial pada Teks dalam PDF

Aspose.PDF for Python via .NET mendemonstrasikan cara menerapkan efek gradien linear pada teks dalam dokumen PDF. Gradien aksial secara mulus bertransisi dari merah ke biru sepanjang teks, menciptakan judul yang visualnya mencolok. Teknik ini ideal untuk judul bergaya, branding, atau elemen dekoratif dalam tata letak dokumen PDF.

1. Inisialisasi dokumen baru dan tambahkan halaman kosong.
1. Buat dan Gayakan Text Fragment. Tambahkan judul, atur posisi, font, dan ukuran.
1. Terapkan Shading Gradien Aksial dengan ‘GradientAxialShading’. Atur warna latar depan menggunakan GradientAxialShading dari merah ke biru.
1. Tambahkan Gaya Garis Bawah.
1. Masukkan fragmen teks bergaya ke dalam halaman.
1. Simpan Dokumen.

```python
import math
import sys
import os
import aspose.pdf as ap

def apply_gradient_axial_shading_to_text(output_file_name):
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

Gradien radial menciptakan transisi warna melingkar yang memancar ke luar dari pusat teks, menawarkan opsi gaya visual yang dinamis untuk judul, header, atau elemen dekoratif.

1. Inisialisasi dokumen baru dan tambahkan halaman kosong.
1. Buat dan Gayakan Text Fragment. Tambahkan judul, atur posisi, font, dan ukuran.
1. Terapkan Gradien Radial dengan 'GradientRadialShading'. Atur warna latar depan menggunakan GradientRadialShading dari merah ke biru.
1. Tambahkan Gaya Garis Bawah.
1. Masukkan fragmen teks bergaya ke dalam halaman.
1. Simpan Dokumen.

```python
import math
import sys
import os
import aspose.pdf as ap

def apply_gradient_radial_shading_to_text(output_file_name):
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

![Terapkan shading gradien radial](gradient_radial_shading.png)

## Fragmen HTML dan LaTeX

### Tambahkan Teks HTML ke Dokumen PDF

Pustaka Aspose.PDF for Python via .NET memungkinkan Anda menyisipkan konten berformat HTML ke dalam dokumen PDF menggunakan kelas HtmlFragment. Dengan menggunakan tag HTML, Anda dapat menampilkan teks yang bergaya, terstruktur, atau mirip rumus secara langsung di PDF.

1. Buat dokumen baru dan halaman menggunakan 'Document()', dan 'document.pages.add()' untuk menambahkan halaman kosong.
1. Buat sebuah instance dari kelas HtmlFragment dan lewati string HTML Anda sebagai parameter.
1. Tambahkan fragmen ke halaman menggunakan 'page.paragraphs.add()' untuk menyisipkan konten HTML.
1. Simpan PDF.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_html_fragment(output_file_name):
    # Create a new document
    document = ap.Document()
    page = document.pages.add()

    # Add a text fragment at a specific position
    text_fragment = ap.HtmlFragment("<pre>S=a<sub>2n</sub>+a<sup>2</sup><pre>")

    page.paragraphs.add(text_fragment)
    document.save(output_file_name)
```

![Tambahkan Teks HTML ke Dokumen PDF](html_fragment.png)

### Tambahkan fragmen HTML bergaya dengan berbagai format ke dokumen PDF

Kita dapat mendefinisikan fragmen HTML dan mengatur gaya teks secara langsung menggunakan tag HTML. Menyematkan konten HTML yang bergaya ke dalam dokumen PDF. Potongan kode ini membuat file PDF baru, menambahkan sebuah halaman, menyisipkan fragmen HTML dengan berbagai elemen pemformatan (judul, paragraf, tautan, dan gaya inline), dan menyimpan hasilnya ke jalur yang ditentukan.

1. Menginisialisasi objek Document baru untuk merepresentasikan PDF.
1. Menambahkan halaman kosong ke dokumen di mana konten HTML akan ditempatkan.
1. Siapkan Konten HTML. String HTML berisi judul h1, paragraf berwarna hijau dengan teks tebal, miring, dan bergaris bawah, serta tautan ke sebuah situs web dengan ukuran font yang diperbesar.
1. Buat Fragmen HTML. Bungkus string HTML dalam objek HtmlFragment.
1. Sisipkan HTML ke Halaman. Menambahkan fragmen HTML ke koleksi paragraf halaman, merender HTML sebagai konten PDF asli.
1. Simpan Dokumen.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_html_fragment(output_file_name):
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
    document.save(output_file_name)
```

![Tambahkan Konten HTML ke Dokumen PDF](html_content.png)

### Tambahkan HTML Fragment dengan status teks yang ditimpa

Seperti yang kita lihat pada contoh sebelumnya, memungkinkan untuk mengatur gaya secara langsung di kode HTML. Ini memiliki keuntungannya, tetapi juga beberapa kelemahan. Misalkan kita bekerja dengan HTML pelanggan dan ingin menyatukan tampilan output kita.
Dalam kasus ini, kita dapat mengubah gaya pelanggan dengan menggunakan TextState kita sendiri, seperti yang ditunjukkan dalam contoh berikut.

1. Buat dokumen baru dan halaman menggunakan 'Document()', dan 'document.pages.add()' untuk menambahkan halaman kosong.
1. Siapkan Konten HTML. String HTML berisi heading h1 dengan font Verdana, paragraf berwarna hijau dengan teks tebal, miring, dan bergaris bawah, serta hyperlink ke situs web dengan ukuran font yang lebih besar.
1. Buat Fragmen HTML. Bungkus string HTML dalam objek HtmlFragment.
1. Timpa format teks. Buat objek TextState dan atur Font, Font Size, dan Text Color.
1. Tambahkan fragmen HTML ke koleksi paragraf halaman.
1. Simpan Dokumen.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_html_fragment_override_text_state(output_file_name):
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
    document.save(output_file_name)
```

![Tambahkan status teks override fragmen HTML](html_override.png)

### Tambahkan Teks LaTeX ke Dokumen PDF

Tambahkan ekspresi matematika berformat LaTeX ke dokumen PDF menggunakan kelas TeXFragment dalam Aspose.PDF for Python via .NET.
LaTeX adalah sistem typesetting yang kuat yang banyak digunakan untuk membuat dokumen ilmiah dan matematika. Dengan menggunakan TeXFragment, Anda dapat langsung merender notasi matematika dan simbol LaTeX di dalam halaman PDF.

1. Buat dokumen baru dan halaman menggunakan 'Document()', dan 'document.pages.add()' untuk menambahkan halaman kosong.
1. Gunakan kelas TeXFragment untuk merender sintaks LaTeX secara langsung.
1. Tambahkan konten LaTeX ke tata letak PDF dengan 'page.paragraphs.add()'.
1. Simpan PDF.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_latex_fragment(output_file_name):
    # Create a new document
    document = ap.Document()
    page = document.pages.add()

    # Add a text fragment at a specific position
    text_fragment = ap.TeXFragment(
        "\\underbrace{\\overbrace{a+b}^6 \\cdot \\overbrace{c+d}^7}_\\text{example of text} = 42"
    )

    page.paragraphs.add(text_fragment)
    document.save(output_file_name)
```

![Ekspresi matematika kompleks yang ditampilkan dalam PDF menunjukkan formula LaTeX dengan notasi overbrace di atas (a+b)⁶, notasi underbrace di bawah seluruh ekspresi (a+b)⁶ · (c+d)⁷, diberi label sebagai contoh teks, dan sama dengan 42. Formula tersebut menunjukkan penataan tipe matematika lanjutan dengan spasi yang tepat dan gaya tanda kurung khas rendering LaTeX.](latex_fragment.png)

## Font khusus

### Gunakan Font khusus dari file

Contoh ini memungkinkan Anda menambahkan teks ke file PDF menggunakan font OpenType khusus dalam Aspose.PDF for Python via .NET. Ini menunjukkan cara membuat dokumen PDF baru, menempatkan teks secara tepat pada halaman, dan menerapkan pemformatan khusus seperti jenis font, ukuran, warna, dan gaya miring.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Tentukan konten teks yang ingin Anda tambahkan ke PDF.
1. Atur posisi teks.
1. Tambahkan TextFragment ke halaman.
1. Simpan dokumen PDF.

Fungsi ini tidak hanya bekerja dengan font OTF tetapi juga dengan font TTF.

```python
import math
import sys
import os
import aspose.pdf as ap

def use_custom_font_from_file(output_file_name):
    font_path = os.path.join(FONT_DIR, "BriosoPro Italic.otf")
    document = ap.Document()
    page = document.pages.add()

    fragment = ap.text.TextFragment("Hello, Aspose!")
    fragment.position = ap.text.Position(100, 600)
    fragment.text_state.font = ap.text.FontRepository.open_font(font_path)
    fragment.text_state.font_size = 24
    fragment.text_state.foreground_color = ap.Color.blue
    fragment.text_state.font_style = ap.text.FontStyles.ITALIC

    page.paragraphs.add(fragment)
    document.save(output_file_name)
```

![Fragmen teks yang ditampilkan dalam dokumen PDF menampilkan Hello, Aspose! yang dirender dengan font BriosoPro berwarna biru miring, menunjukkan integrasi font OpenType khusus dan kemampuan styling dalam pemformatan teks PDF.](custom_font.png)

### Gunakan Font khusus dari aliran

Potongan kode ini menunjukkan cara menambahkan teks ke dokumen PDF menggunakan font OpenType (OTF) khusus yang disematkan dengan Aspose.PDF for Python via .NET. Ini menunjukkan cara membuka file font sebagai aliran, menyematkannya ke dalam PDF untuk memastikan ketersediaan font di berbagai sistem, dan menerapkan pemformatan teks seperti ukuran font, warna, dan gaya miring. Pendekatan ini ideal untuk membuat PDF yang konsisten secara visual dan mempertahankan tipografi bahkan ketika dibagikan atau dilihat di perangkat tanpa font yang terpasang.

1. Muat file font sebagai aliran biner.
1. Buka dan sematkan font menggunakan 'FontRepository.open_font'.
1. Buat dokumen PDF baru dan tambahkan halaman.
1. Tambahkan fragmen teks bergaya dengan:
    - Font khusus tersemat.
    - Gaya miring dan warna biru.
    - Ukuran font tertentu dan posisi.
1. Simpan dokumen akhir ke jalur output yang ditentukan.

```python
import math
import sys
import os
import aspose.pdf as ap

def use_custom_font_from_stream(output_file_name):
    font_path = os.path.join(FONT_DIR, "BriosoPro Italic.otf")
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
        document.save(output_file_name)
```

Menyematkan font memastikan rendering yang konsisten di semua platform, menjadikan pendekatan ini ideal untuk branding, kesetiaan desain, dan dukungan multibahasa.

## Topik Teks Terkait

- [Bekerja dengan teks dalam PDF menggunakan Python](/pdf/id/python-net/working-with-text/)
- [Memformat teks PDF di Python](/pdf/id/python-net/text-formatting-inside-pdf/)
- [Ganti teks dalam PDF menggunakan Python](/pdf/id/python-net/replace-text-in-pdf/)
- [Cari dan ekstrak teks PDF di Python](/pdf/id/python-net/search-and-get-text-from-pdf/)