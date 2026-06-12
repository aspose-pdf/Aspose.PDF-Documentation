---
title: Format Teks PDF dalam Python
linktitle: Pemformatan Teks dalam PDF
type: docs
weight: 70
url: /id/python-net/text-formatting-inside-pdf/
description: Pelajari cara memformat teks di dalam dokumen PDF menggunakan Python dengan opsi spasi, batas, indentasi, dan gaya.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Format dan gaya teks di dalam file PDF dengan Python
Abstract: Artikel ini menjelaskan cara memformat teks dalam dokumen PDF menggunakan Aspose.PDF for Python via .NET. Pelajari cara mengontrol spasi, indentasi, border, garis bawah, efek coret, dan opsi penataan teks lainnya dalam Python.
---

## Spasi Baris dan Karakter

### Menggunakan Spasi Baris

#### Cara Memformat Teks dengan Spasi Baris Kustom di Python - Kasus Sederhana

Aspose.PDF for Python menyediakan pendekatan yang sederhana untuk mengontrol tata letak teks dan keterbacaan melalui penyesuaian jarak baris.

Potongan kode kami menunjukkan cara mengontrol jarak baris dalam dokumen PDF. Kode tersebut membaca teks dari sebuah file (atau menggunakan pesan cadangan), menerapkan ukuran font khusus dan jarak baris, serta menambahkan teks yang diformat ke halaman baru dalam PDF.

1. Buat dokumen PDF baru.
1. Muat teks sumber.
1. Inisialisasi objek TextFragment dan tetapkan teks yang dimuat ke dalamnya.
1. Atur properti font dan spasi untuk teks. Nilai-nilai ini menentukan seberapa rapat atau longgar baris teks muncul:
    - Ukuran font: 12 poin
    - Jarak baris: 16 poin
1. Masukkan fragmen teks terformat ke dalam koleksi `paragraphs` halaman.
1. Simpan dokumen.

```python
import aspose.pdf as ap
import sys
from os import path

def specify_line_spacing_simple_case(outfile):
    document = ap.Document()
    page = document.pages.add()

    lorem_path = path.join(DATA_DIR, "lorem.txt")
    if path.exists(lorem_path):
        with open(lorem_path, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        text = "Lorem ipsum text not found."

    text_fragment = ap.text.TextFragment(text)
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.line_spacing = 16
    page.paragraphs.add(text_fragment)

    document.save(outfile)
```

#### Cara Memformat Teks dengan Jarak Baris Kustom di Python - Kasus Khusus

Mari kita periksa cara menerapkan mode jarak baris yang berbeda dalam dokumen PDF menggunakan font TrueType (TTF) kustom.
Ia memuat teks dari sebuah file, menyematkan font tertentu, dan merender teks yang sama dua kali pada halaman PDF—setiap kali menggunakan mode jarak baris yang berbeda:

- Mode FONT_SIZE: Jarak baris sama dengan ukuran font.
- FULL_SIZE mode: Jarak baris memperhitungkan tinggi penuh font, termasuk ascender dan descender.

Contoh ini menunjukkan bagaimana perilaku jarak baris dapat bervariasi tergantung pada mode yang dipilih.

1. Buat dokumen PDF baru.
1. Tentukan jalur untuk file font kustom dan file sumber teks.
1. Muat konten teks.
1. Buka font khusus.
1. Buat dan konfigurasi TextFragment pertama (mode FONT_SIZE). Atur line_spacing menjadi 'TextFormattingOptions.LineSpacingMode.FONT_SIZE', yang berarti jarak baris sama dengan ukuran font.
1. Buat dan konfigurasi TextFragment kedua (mode FULL_SIZE). Atur line_spacing menjadi 'TextFormattingOptions.LineSpacingMode.FULL_SIZE', yang menggunakan tinggi penuh font.
1. Tambahkan kedua fragmen teks ke halaman PDF yang sama.
1. Simpan dokumen yang selesai ke lokasi output yang ditentukan.

```python
import aspose.pdf as ap
import sys
from os import path

def specify_line_spacing_specific_case(outfile):
    document = ap.Document()
    page = document.pages.add()

    font_file = path.join(DATA_DIR, "HPSimplified.ttf")
    lorem_path = path.join(DATA_DIR, "lorem.txt")
    if path.exists(lorem_path):
        with open(lorem_path, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        text = "Lorem ipsum text not found."

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

![Dokumen PDF yang menampilkan teks dengan spasi baris khusus yang menunjukkan jarak 16 poin antar baris untuk meningkatkan keterbacaan dan pemformatan tata letak teks.](line_spacing.png)

### Menggunakan Spasi Karakter

#### Cara mengontrol spasi karakter dalam teks PDF menggunakan kelas TextFragment

Jarak antar karakter menentukan jarak antara masing-masing karakter dalam satu baris teks—berguna untuk penyetelan halus tampilan teks atau mencapai efek tipografi tertentu.

1. Menginisialisasi objek Document baru dan menambahkan halaman kosong untuk menempatkan teks.
1. Definisikan Fragment Generator. Mengimplementasikan fungsi pembantu make_fragment(spacing):
    - buat TextFragment dengan teks contoh.
    - atur font.
1. Tambahkan fragmen teks dengan nilai spasi yang berbeda.
1. Simpan Dokumen.

```python
import aspose.pdf as ap
import sys
from os import path

def character_spacing_using_text_fragment(outfile):
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

![Dokumen PDF menampilkan tiga baris teks identik Sample Text dengan spasi karakter yang menunjukkan spasi karakter semakin rapat dari atas ke bawah, dengan baris pertama memiliki spasi antar huruf yang lebih lebar, baris tengah memiliki spasi sedang, dan baris bawah memiliki spasi karakter paling rapat, menggambarkan efek visual dari nilai spasi karakter yang berbeda dalam pemformatan teks PDF.](character_spacing_simple.png)

#### Cara mengontrol jarak karakter dalam teks PDF menggunakan TextParagraph dan TextBuilder

Aspose.PDF memungkinkan penerapan spasi karakter khusus saat menambahkan teks ke dokumen PDF menggunakan TextParagraph dan TextBuilder.
Ini mendefinisikan area spesifik pada halaman, mengonfigurasi pembungkus teks, dan merender fragmen teks dengan spasi yang disesuaikan antar karakter.

Menggunakan TextParagraph ideal bila Anda memerlukan kontrol yang presisi atas penempatan teks dan tata letaknya, seperti saat membangun blok teks yang terstruktur atau multi‑kolom.

1. Buat dokumen PDF baru.
1. Inisialisasi sebuah instance TextBuilder untuk halaman.
1. Buat dan konfigurasikan TextParagraph.
    - Atur mode pembungkus kata ke 'TextFormattingOptions.WordWrapMode.BY_WORDS'.
1. Buat TextFragment dengan jarak karakter khusus.
    - Buat TextFragment baru dan setel teksnya (mis., "Sample Text with character spacing").
    - Tentukan atribut font seperti Arial dan ukuran font 14 pt.
    - Terapkan spasi karakter = 2.0, yang meningkatkan jarak antar karakter.
1. Tambahkan TextFragment ke TextParagraph.
1. Tambahkan TextParagraph ke halaman.
1. Simpan dokumen PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def character_spacing_using_text_paragraph(outfile):
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

Saat bekerja dengan file PDF, Anda mungkin perlu menampilkan informasi terstruktur seperti daftar — apakah itu berupa bullet, bernomor, atau diformat dengan HTML atau LaTeX.
Aspose.PDF for Python via .NET menyediakan beberapa cara yang fleksibel untuk membuat dan memformat daftar langsung dalam dokumen PDF Anda, memberi Anda kontrol penuh atas tata letak, font, dan gaya.

Artikel ini menunjukkan berbagai pendekatan untuk membuat daftar dalam PDF, mulai dari pemformatan teks biasa hingga rendering HTML dan LaTeX yang canggih. Setiap metode melayani kasus penggunaan tertentu — apakah Anda lebih suka kontrol programatik yang tepat atau styling berbasis markup yang praktis.

Pada akhir artikel ini, Anda akan mengetahui cara:

- Membuat daftar bullet dan bernomor khusus menggunakan TextParagraph dan TextBuilder.

- Gunakan fragmen HTML (HtmlFragment) untuk dengan mudah merender daftar HTML ul dan ol dalam PDF.

- Manfaatkan fragmen LaTeX (TeXFragment) untuk pemformatan daftar matematis atau ilmiah.

- Kontrol pembungkus teks, gaya font, dan penempatan tata letak dalam sebuah halaman.

- Pahami perbedaan antara konstruksi daftar manual dan pendekatan berbasis markup.

### Buat daftar bernomor

```python
import aspose.pdf as ap
import sys
from os import path

def create_bullet_list(outfile):
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

### Buat daftar bullet

```python
import aspose.pdf as ap
import sys
from os import path

def create_numbered_list(outfile):
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

### Buat versi HTML daftar bernomor

Buat daftar bernomor (ordered) dalam dokumen PDF menggunakan fragmen HTML. Ini mengubah daftar Python berisi string menjadi elemen tag HTML ordered-list dan menyisipkannya ke halaman PDF sebagai HtmlFragment.

Menggunakan fragmen HTML memungkinkan Anda memasukkan fitur pemformatan berbasis HTML, seperti daftar bernomor, cetak tebal, miring, dan lainnya, langsung ke dalam PDF Anda.

1. Buat dokumen PDF baru dan tambahkan sebuah halaman.
1. Siapkan item-item daftar.
1. Ubah daftar menjadi daftar terurut HTML.
    - Gunakan tag HTML ol untuk daftar bernomor.
    - Bungkus setiap item dengan tag li menggunakan list comprehension.
1. Ubah string HTML menjadi objek HtmlFragment yang dapat ditambahkan ke halaman PDF.
1. Masukkan HtmlFragment ke dalam koleksi `paragraphs` halaman.
1. Simpan dokumen PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def create_numbered_list_html_version(outfile):
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

![Daftar bernomor yang ditampilkan dalam dokumen PDF dengan empat item bernomor otomatis: 1. First item in the list, 2. Second item with more text to demonstrate wrapping behavior, 3. Third item, dan 4. Fourth item. Daftar ini menunjukkan rendering daftar berurutan berformat HTML dalam struktur PDF dengan urutan angka, indentasi, dan jarak antar item yang tepat](numbered_list_html.png)

### Buat versi daftar poin HTML

Perpustakaan kami menunjukkan cara membuat daftar berbulu (tidak terurut) dalam dokumen PDF menggunakan fragmen HTML. Ini mengonversi daftar Python berisi string menjadi elemen tag HTML unordered-list dan menyisipkannya ke halaman PDF sebagai HtmlFragment. Menggunakan fragmen HTML memungkinkan Anda memanfaatkan fitur pemformatan HTML (seperti daftar, tebal, miring) secara langsung di PDF.

1. Buat dokumen PDF baru dan tambahkan sebuah halaman.
1. Siapkan item-item daftar.
1. Ubah daftar menjadi daftar tidak terurut HTML.
    - Gunakan tag HTML ul untuk daftar tidak terurut (berbulu).
    - Bungkus setiap item dengan tag li menggunakan list comprehension.
1. Buat sebuah HtmlFragment. Konversi string HTML menjadi objek HtmlFragment yang dapat ditambahkan ke halaman PDF.
1. Masukkan HtmlFragment ke dalam koleksi `paragraphs` halaman.
1. Simpan dokumen PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def create_bullet_list_html_version(outfile):
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

![Daftar berpoin yang ditampilkan dalam dokumen PDF dengan empat item: First item in the list, Second item with more text to demonstrate wrapping behavior, Third item, dan Fourth item. Setiap item diawali dengan poin standar dan menunjukkan rendering daftar berformat HTML dalam struktur PDF dengan indentasi dan jarak yang tepat](bullet_list_html.png)

### Buat daftar berpoin versi LaTeX

Buat daftar berbulu (tidak berurutan) dalam PDF menggunakan fragmen LaTeX (TeXFragment). Ini mengonversi daftar Python berisi string menjadi lingkungan itemize LaTeX dan memasukkannya ke halaman PDF. Menggunakan fragmen LaTeX ideal ketika Anda ingin merender formula matematika, simbol, atau daftar terstruktur dengan pemformatan yang tepat.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Definisikan daftar Python berisi string yang akan menjadi poin-poin dalam lingkungan itemize LaTeX.
1. Konversi daftar menjadi lingkungan itemize LaTeX:
    - Bungkus item dengan begin itemize dan end itemize.
    - Setiap item diawali dengan item menggunakan pemahaman daftar.
1. Konversikan string LaTeX menjadi objek TeXFragment yang dapat dirender dalam PDF.
1. Tambahkan fragmen LaTeX ke halaman.
1. Simpan dokumen PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def create_bullet_list_latex_version(outfile):
    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]
    tex_list = (
        "Lists are easy to create: \begin itemize"
        + "".join([f"\item {i}" for i in items])
        + "\end itemize"
    )
    tex_fragment = ap.TeXFragment(tex_list)
    page.paragraphs.add(tex_fragment)
    document.save(outfile)
```

![Daftar berbullet yang ditampilkan dalam PDF menampilkan format yang dihasilkan oleh LaTeX dengan teks. Daftar mudah dibuat: diikuti oleh empat item berbullet: Item pertama, Item kedua dengan teks lebih banyak untuk mendemonstrasikan perilaku pembungkusan, Item ketiga, dan Item keempat. Daftar ini menunjukkan penataan LaTeX profesional dengan format bullet yang tepat, spasi yang konsisten, dan kemampuan pembungkusan teks dalam tata letak dokumen PDF yang bersih.](bullet_list_latex.png)

### Buat daftar bernomor versi LaTeX

Buat daftar bernomor (terurut) dalam PDF menggunakan fragmen LaTeX (TeXFragment). Ini mengonversi daftar Python yang berisi string menjadi lingkungan enumerate LaTeX dan menyisipkannya ke halaman PDF. Menggunakan fragmen LaTeX ideal ketika Anda menginginkan pemformatan yang tepat, daftar terstruktur, atau notasi matematis dalam PDF.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Definisikan daftar Python berisi string yang akan menjadi item bernomor dalam lingkungan enumerate LaTeX.
1. Konversi daftar tersebut menjadi lingkungan enumerate LaTeX.
1. Konversikan string LaTeX menjadi objek TeXFragment yang dapat dirender dalam PDF.
1. Tambahkan fragmen LaTeX ke halaman.
1. Simpan dokumen PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def create_numbered_list_latex_version(outfile):
    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]
    tex_list = (
        "Lists are easy to create: \begin enumerate"
        + "".join([f"\item {i}" for i in items])
        + "\end enumerate"
    )
    tex_fragment = ap.TeXFragment(tex_list)
    page.paragraphs.add(tex_fragment)
    document.save(outfile)
```

![Daftar bernomor yang ditampilkan dalam PDF memperlihatkan pemformatan yang dirender LaTeX dengan item 1. Item pertama, 2. Item kedua dengan teks lebih banyak untuk mendemonstrasikan perilaku pembungkusan, 3. Item ketiga, dan 4. Item keempat, didahului oleh teks Daftar mudah dibuat](numbered_list_latex.png)

## Catatan kaki dan catatan akhir

### Tambahkan Catatan Kaki

Catatan kaki digunakan untuk merujuk catatan dalam isi dokumen dengan menempatkan nomor superskrip berurutan di sebelah teks yang relevan. Nomor‑nomor ini sesuai dengan catatan rinci yang biasanya diindentasi dan ditempatkan di bagian bawah halaman yang sama, memberikan konteks tambahan, sitasi, atau komentar.

Tambahkan catatan kaki ke fragmen teks dalam dokumen PDF menggunakan Aspose.PDF for Python via .NET. Catatan kaki berguna untuk menyediakan informasi tambahan, sitasi, atau klarifikasi tanpa mengacaukan konten utama. Metode ini memastikan bahwa catatan kaki terintegrasi secara visual dan struktural ke dalam tata letak PDF.

1. Buat Dokumen Baru.
1. Buat sebuah TextFragment dengan konten utama.
1. Tambahkan Teks Inline. Buat TextFragment lain yang melanjutkan dalam paragraf yang sama.
1. Simpan Dokumen.

```python
import aspose.pdf as ap
import sys
from os import path

def add_footnote(outfile):
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

### Tambahkan Catatan Kaki dengan Gaya Kustom di PDF

1. Inisialisasi dokumen PDF baru dan tambahkan halaman kosong.
1. Buat Fragmen Teks Utama.
1. Buat dan Atur Gaya Catatan Kaki (Font, Size, Color, Style).
1. Masukkan fragmen teks bergaya dengan catatan kaki ke dalam halaman.
1. Tambahkan fragmen teks lain tanpa catatan kaki.
1. Simpan Dokumen.

```python
import aspose.pdf as ap
import sys
from os import path

def add_footnote_custom_text_style(outfile):
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

### Tambahkan Catatan Kaki dengan Simbol Kustom dalam PDF

Tambahkan catatan kaki ke fragmen teks dalam dokumen PDF menggunakan Aspose.PDF for Python via .NET, dengan kemampuan untuk menyesuaikan simbol penanda catatan kaki.

1. Buat Dokumen PDF dan Halaman.
1. Tambahkan Fragmen Teks pertama dengan Simbol Catatan Kaki Kustom.
1. Tambahkan Text Fragment lain yang melanjutkan paragraf tanpa catatan kaki.
1. Tambahkan Fragmen Teks kedua dengan Catatan Kaki Default.
1. Simpan Dokumen.

```python
import aspose.pdf as ap
import sys
from os import path

def add_footnote_custom_text(outfile):
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

Sesuaikan tampilan visual garis catatan kaki dalam dokumen PDF dengan perpustakaan Python. Menyesuaikan garis catatan kaki meningkatkan kejelasan visual dan memungkinkan konsistensi gaya dalam dokumen seperti laporan, makalah akademik, dan publikasi beranotasi.

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Tentukan gaya garis khusus untuk penghubung catatan kaki (warna, lebar, dan pola garis putus-putus).
1. Tambahkan beberapa fragmen teks dengan catatan kaki.
1. Simpan dokumen akhir.

```python
import aspose.pdf as ap
import sys
from os import path

def add_footnote_with_custom_line_style(outfile):
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

### Tambahkan Catatan Kaki dengan Gambar dan Tabel dalam PDF

Bagaimana cara memperkaya catatan kaki dalam dokumen PDF dengan menyematkan gambar, teks bergaya, dan tabel menggunakan Aspose.PDF for Python via .NET?

1. Buat dokumen PDF baru dan tambahkan halaman.
1. Tambahkan fragmen teks dengan catatan kaki terlampir.
1. Sematkan gambar, teks bergaya, dan tabel di dalam catatan kaki.
1. Simpan Dokumen.

```python
import aspose.pdf as ap
import sys
from os import path

def add_footnote_with_image_and_table(outfile):
    document = ap.Document()
    page = document.pages.add()

    text = ap.text.TextFragment("This is a sample text with a footnote.")
    page.paragraphs.add(text)

    note = ap.Note()

    # Add image
    image_note = ap.Image()
    image_note.file = path.join(DATA_DIR, "logo.jpg")
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

Catatan akhir (Endnote) adalah jenis kutipan yang mengarahkan pembaca ke bagian tertentu di akhir dokumen, di mana mereka dapat menemukan referensi lengkap untuk kutipan, ide yang diparafrase, atau konten yang dirangkum. Saat menggunakan catatan akhir, nomor superskrip ditempatkan tepat setelah materi yang dirujuk, membimbing pembaca ke catatan yang sesuai di akhir makalah.

Cuplikan kode ini menunjukkan cara menambahkan catatan akhir ke fragmen teks dalam dokumen PDF. Tidak seperti catatan kaki, yang muncul di dekat teks yang dirujuk, catatan akhir biasanya ditempatkan di akhir dokumen atau bagian. Metode ini juga mensimulasikan dokumen yang lebih panjang untuk mengilustrasikan bagaimana catatan akhir berperilaku dalam konten yang diperluas.

1. Buat Dokumen PDF dan Halaman.
1. Tambahkan Fragmen Teks dengan Catatan Akhir.
1. Muat Konten Teks Eksternal.
1. Simulasikan Dokumen Panjang. Tambahkan teks yang dimuat beberapa kali untuk mensimulasikan dokumen yang lebih panjang.
1. Simpan Dokumen.

```python
import aspose.pdf as ap
import sys
from os import path

def add_endnote(outfile):
    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with an endnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.end_note = ap.Note("This is the EndNote content.")
    page.paragraphs.add(text_fragment)

    lorem_path = path.join(DATA_DIR, "lorem.txt")
    if path.exists(lorem_path):
        with open(lorem_path, encoding="utf-8") as f:
            text_content = f.read()
    else:
        text_content = "Lorem ipsum sample text not found."

    # Simulate long text
    for _ in range(5):
        tf = ap.text.TextFragment(text_content)
        tf.text_state.font = ap.text.FontRepository.find_font("Arial")
        tf.text_state.font_size = 14
        page.paragraphs.add(tf)

    document.save(outfile)
```

### Tambahkan Catatan Akhir dengan Teks Penanda Kustom dalam PDF

Tambahkan catatan akhir ke fragmen teks dalam dokumen PDF, dengan simbol penanda khusus (mis., "***"). Catatan akhir biasanya ditempatkan di akhir dokumen atau bagian dan berguna untuk memberikan konteks tambahan, sitasi, atau komentar.

1. Buat Dokumen PDF dan Halaman.
1. Tambahkan fragmen teks bergaya dengan catatan akhir.
1. Sesuaikan teks penanda catatan akhir.
1. Muat konten eksternal dari file .txt.
1. Simulasikan konten bentuk panjang untuk menggambarkan penempatan catatan akhir.
1. Simpan dokumen PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def add_endnote_custom_text(outfile):
    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with an endnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.end_note = ap.Note("This is the EndNote content.")
    text_fragment.end_note.text = "***"
    page.paragraphs.add(text_fragment)

    lorem_path = path.join(DATA_DIR, "lorem.txt")
    if path.exists(lorem_path):
        with open(lorem_path, encoding="utf-8") as f:
            text_content = f.read()
    else:
        text_content = "Lorem ipsum sample text not found."

    # Simulate long text
    for _ in range(5):
        tf = ap.text.TextFragment(text_content)
        tf.text_state.font = ap.text.FontRepository.find_font("Arial")
        tf.text_state.font_size = 14
        page.paragraphs.add(tf)

    document.save(outfile)
```

## Tata letak & kontrol halaman

### Paksa Tabel untuk Mulai pada Halaman Baru di PDF

Tambahkan konten spesifik untuk memulai pada halaman baru dalam dokumen PDF menggunakan Aspose.PDF for Python via .NET.
Dengan mengatur properti is_in_new_page, Anda dapat mengontrol tata letak dan struktur halaman secara tepat, memastikan bahwa bagian tertentu (seperti tabel, laporan, atau ringkasan) selalu dimulai pada halaman baru — ideal untuk pemformatan dokumen, laporan siap cetak, atau pembuatan output yang terorganisir.

1. Buat dan konfigurasi sebuah tabel.
1. Tambahkan data ke tabel.
1. Paksa halaman baru untuk tabel. Ini memastikan bahwa tabel mulai di bagian atas halaman baru, bahkan jika ada konten yang sudah ada pada halaman saat ini.
1. Tambahkan tabel ke halaman. Gunakan page.paragraphs.add() untuk memasukkan tabel ke dalam tata letak PDF.
1. Simpan dokumen.

```python
import aspose.pdf as ap
import sys
from os import path

def force_new_page(output_file_name):
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

### Menggunakan Properti Paragraf Inline dalam PDF

Perpustakaan kami memungkinkan Anda menggunakan properti is_in_line_paragraph untuk mengontrol aliran inline antara teks dan gambar dalam PDF.
Biasanya, ketika Anda menambahkan elemen baru (seperti fragmen teks atau gambar), masing‑masing dimulai pada baris baru atau paragraf baru.
Dengan mengatur is_in_line_paragraph = True, Anda dapat membuat elemen muncul pada baris yang sama atau dalam paragraf yang sama, menciptakan tata letak inline yang mulus—sempurna untuk menggabungkan teks dan gambar secara inline, seperti menambahkan logo, ikon, atau simbol dalam kalimat.

Fragmen teks pertama, gambar, dan fragmen teks kedua muncul pada baris yang sama, membentuk paragraf inline yang berkelanjutan.
Fragmen teks ketiga memulai paragraf baru, menunjukkan perilaku pemutusan baris default.

1. Buat dokumen PDF baru.
1. Tambahkan fragmen teks pertama.
1. Sisipkan gambar inline.
1. Tambahkan lebih banyak teks inline.
1. Tambahkan paragraf baru.
1. Simpan PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def using_inline_paragraph_property(output_file_name):
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
    image.file = path.join(DATA_DIR, "logo.jpg")
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

Buat tata letak bergaya surat kabar multi-kolom dalam PDF menggunakan Aspose.PDF for Python via .NET.
Ini menunjukkan cara menggabungkan teks, pemformatan HTML, dan grafis dalam sebuah FloatingBox, memungkinkan kontrol tata letak lanjutan serupa dengan desain majalah atau buletin multi-kolom.

1. Inisialisasi dokumen PDF.
1. Tambahkan garis pemisah horizontal di bagian atas.
1. Tambahkan judul HTML yang bergaya.
1. Buat FloatingBox untuk kontrol tata letak.
1. Konfigurasikan tata letak multi-kolom.
1. Tambahkan info penulis.
1. Gambar garis horizontal internal lainnya.
1. Tambahkan teks artikel.
1. Simpan PDF akhir.

```python
import aspose.pdf as ap
import sys
from os import path

def create_multi_column_pdf(output_file_name):
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
    lorem_path = path.join(DATA_DIR, "lorem.txt")
    if path.exists(lorem_path):
        with open(lorem_path, "r", encoding="utf-8") as f:
            lorem_text = f.read()
    else:
        lorem_text = "Lorem ipsum text not found."
    text2 = ap.text.TextFragment(lorem_text * 5)
    box.paragraphs.add(text2)

    page.paragraphs.add(box)

    # Save PDF
    document.save(output_file_name)
```

### Hentian Tab Kustom untuk Penyelarasan Teks dalam PDF

Buat tata letak teks mirip tabel dalam PDF menggunakan tab stop kustom — tanpa bergantung pada struktur tabel.
Dengan mendefinisikan posisi tab stop, perataan, dan gaya pemimpin, Anda dapat menyelaraskan teks secara tepat di seluruh kolom. Hal ini berguna untuk faktur, laporan, atau data teks terstruktur.

1. Buat dokumen PDF baru.
1. Tentukan hentian tab khusus.
1. Gunakan placeholder #$TAB dalam teks.
1. Tambahkan teks ke PDF.
1. Simpan PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def custom_tab_stops(output_file_name):
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

### Topik Teks Terkait

- [Bekerja dengan teks dalam PDF menggunakan Python](/pdf/id/python-net/working-with-text/)
- [Menambahkan teks ke PDF](/pdf/id/python-net/add-text-to-pdf-file/)
- [Memutar teks di dalam PDF menggunakan Python](/pdf/id/python-net/rotate-text-inside-pdf/)
- [Mengganti teks dalam PDF via Python](/pdf/id/python-net/replace-text-in-pdf/)

