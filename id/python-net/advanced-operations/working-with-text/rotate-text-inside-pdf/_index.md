---
title: Putar Teks PDF di Python
linktitle: Putar Teks di Dalam PDF
type: docs
weight: 50
url: /id/python-net/rotate-text-inside-pdf/
description: Pelajari cara memutar fragmen teks dan paragraf di dalam dokumen PDF dengan Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Putar fragmen teks dan paragraf dalam dokumen PDF dengan Python
Abstract: Artikel ini menjelaskan cara memutar teks dalam dokumen PDF menggunakan Aspose.PDF for Python via .NET. Ini menunjukkan cara mengatur properti `rotation` pada `TextFragment`, membangun konten yang diputar dengan `TextBuilder` dan `TextParagraph`, serta menambahkan teks yang diputar secara langsung ke paragraf halaman untuk berbagai skenario tata letak.
---

Putar fragmen teks dalam dokumen PDF menggunakan Aspose.PDF for Python via .NET. Halaman ini menunjukkan cara mengontrol posisi dan rotasi teks dengan menggunakan `TextFragment`, `TextState`, dan `TextBuilder`. Dengan menyesuaikan sudut rotasi, Anda dapat membuat tata letak seperti header diagonal, label vertikal, dan anotasi yang diputar.

## Putar Fragmen Teks Menggunakan TextBuilder dalam PDF

Membuat file PDF bernama `rotated_fragments.pdf` mengandung tiga fragmen teks yang diselaraskan secara horizontal:

- teks pertama tidak diputar
- yang kedua diputar 45°
- yang ketiga diputar 90°

1. Buat dokumen PDF baru.
1. Sisipkan halaman baru untuk menampung teks yang diputar.
1. Buat fragmen teks pertama (tanpa rotasi).
1. Buat fragmen teks kedua (rotasi 45°).
1. Buat fragmen teks ketiga (rotasi 90°).
1. Tambahkan fragmen teks menggunakan `TextBuilder`.
1. Simpan dokumen.

```python
import aspose.pdf as ap

def rotate_text_inside_pdf_1(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("main text")
        text_fragment_1.position = ap.text.Position(100, 600)
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Create rotated text fragment
        text_fragment_2 = ap.text.TextFragment("rotated text")
        text_fragment_2.position = ap.text.Position(200, 600)
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        text_fragment_2.text_state.rotation = 45
        # Create rotated text fragment
        text_fragment_3 = ap.text.TextFragment("rotated text")
        text_fragment_3.position = ap.text.Position(300, 600)
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
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

## Putar Fragmen Teks Individual di Dalam Paragraf pada PDF

Putar fragmen teks individual dalam sebuah paragraf. Ini menunjukkan cara membangun paragraf multi-baris (TextParagraph) yang berisi beberapa fragmen (TextFragment), masing-masing dengan sudut rotasi sendiri. Teknik ini berguna untuk membuat dokumen yang visualnya kaya yang menggabungkan teks berorientasi horizontal dan diagonal — misalnya, header yang stylized, diagram, atau label beranotasi.

Membuat PDF bernama `rotated_paragraph_fragments.pdf` berisi paragraf dengan tiga baris teks, setiap baris diputar secara berbeda:

- baris pertama diputar 45°
- baris kedua tetap horizontal (0°)
- baris ketiga diputar -45°

1. Buat dokumen PDF baru.
1. Tambahkan halaman kosong di mana teks yang diputar akan muncul.
1. Buat sebuah `TextParagraph`.
1. Buat dan konfigurasikan fragmen teks pertama (+45° rotasi).
1. Buat fragmen teks kedua (tanpa rotasi).
1. Buat fragmen teks ketiga (-45° rotasi).
1. Tambahkan fragmen teks ke paragraf.
1. Tambahkan paragraf ke halaman menggunakan `TextBuilder`.
1. Simpan dokumen.

```python
import aspose.pdf as ap

def rotate_text_inside_pdf_2(outfile):
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
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Set rotation
        text_fragment_1.text_state.rotation = 45
        # Create text fragment
        text_fragment_2 = ap.text.TextFragment("main text")
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Create text fragment
        text_fragment_3 = ap.text.TextFragment("another rotated text")
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
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

Bagian ini menunjukkan metode sederhana untuk memutar teks dalam PDF menggunakan Aspose.PDF for Python via .NET.
Berbeda dengan pendekatan tingkat rendah dengan `TextBuilder` atau `TextParagraph`, metode ini menambahkan fragmen teks berputar langsung ke koleksi paragraf halaman (`page.paragraphs`). Ini ideal ketika Anda membutuhkan rotasi teks dasar tetapi tidak memerlukan penempatan yang tepat atau struktur paragraf.

Menghasilkan file bernama `simple_rotated_text.pdf` mengandung:

- sebuah fragmen teks horizontal utama dengan rotasi 0°
- fragmen diputar 315°
- fragmen diputar 270°

1. Inisialisasi dokumen PDF baru.
1. Buat halaman tempat teks yang diputar akan ditempatkan.
1. Buat fragmen teks pertama (tanpa rotasi).
1. Buat fragmen teks kedua (rotasi 315°).
1. Buat fragmen teks ketiga (rotasi 270°).
1. Tambahkan fragmen teks langsung ke paragraf halaman.
1. Simpan dokumen PDF.

```python
import aspose.pdf as ap

def rotate_text_inside_pdf_3(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("main text")
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Create text fragment
        text_fragment_2 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Set rotation
        text_fragment_2.text_state.rotation = 315
        # Create text fragment
        text_fragment_3 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Set rotation
        text_fragment_3.text_state.rotation = 270
        page.paragraphs.add(text_fragment_1)
        page.paragraphs.add(text_fragment_2)
        page.paragraphs.add(text_fragment_3)

        # Save the document
        document.save(outfile)
```

## Putar Seluruh Paragraf dalam PDF

Contoh ini menunjukkan rotasi teks tingkat paragraf yang canggih dalam PDF. Berbeda dengan rotasi tingkat fragmen (di mana setiap potongan teks diputar secara individual), metode ini memutar seluruh paragraf sebagai blok yang terintegrasi pada sudut yang berbeda.
Setiap paragraf berisi beberapa fragmen teks yang bergaya, dan seluruh paragraf diputar pada sudut tertentu — memungkinkan transformasi tata letak yang kompleks dan konsisten.
Ini ideal untuk tata letak artistik, watermark, atau PDF dengan desain berat di mana seluruh bagian teks perlu diorientasikan ke berbagai arah.

Membuat `rotated_paragraphs.pdf`, berisi empat paragraf yang sepenuhnya bergaya dan diputar:

- masing-masing diputar pada sudut unik (45°, 135°, 225°, dan 315°)
- setiap paragraf memiliki tiga baris teks dengan latar belakang berwarna, garis bawah, dan gaya yang konsisten

1. Buat dokumen PDF baru.
1. Tambahkan halaman kosong untuk menampung paragraf yang diputar.
1. Iterasi untuk membuat beberapa paragraf.
1. Buat dan posisikan paragraf.
1. Buat fragmen teks dengan pemformatan.
1. Terapkan pemformatan teks.
1. Tambahkan fragmen teks ke paragraf.
1. Tambahkan paragraf ke halaman menggunakan `TextBuilder`.
1. Ulangi untuk semua empat rotasi.
1. Simpan dokumen PDF.

```python
import aspose.pdf as ap

def rotate_text_inside_pdf_4(outfile):
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
            text_fragment_1.text_state.font = ap.text.FontRepository.find_font(
                "TimesNewRoman"
            )
            text_fragment_1.text_state.background_color = ap.Color.light_gray
            text_fragment_1.text_state.foreground_color = ap.Color.blue
            # Create text fragment
            text_fragment_2 = ap.text.TextFragment("Second line of text")
            # Set text properties
            text_fragment_2.text_state.font_size = 12
            text_fragment_2.text_state.font = ap.text.FontRepository.find_font(
                "TimesNewRoman"
            )
            text_fragment_2.text_state.background_color = ap.Color.light_gray
            text_fragment_2.text_state.foreground_color = ap.Color.blue
            # Create text fragment
            text_fragment_3 = ap.text.TextFragment("And some more text...")
            # Set text properties
            text_fragment_3.text_state.font_size = 12
            text_fragment_3.text_state.font = ap.text.FontRepository.find_font(
                "TimesNewRoman"
            )
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

## Topik Teks Terkait

- [Bekerja dengan teks dalam PDF menggunakan Python](/pdf/id/python-net/working-with-text/)
- [Menambahkan teks ke PDF](/pdf/id/python-net/add-text-to-pdf-file/)
- [Memformat teks PDF di Python](/pdf/id/python-net/text-formatting-inside-pdf/)
- [Ganti teks dalam PDF dengan Python](/pdf/id/python-net/replace-text-in-pdf/)