---
title: Ekstraksi Berbasis Wilayah dengan Python
linktitle: Ekstraksi Berbasis Wilayah
type: docs
weight: 20
url: /id/python-net/region-based-extraction/
description: Bagian ini berisi artikel tentang ekstraksi berbasis wilayah dari dokumen PDF menggunakan Aspose.PDF dalam Python.
lastmod: "2025-11-05"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## Ekstrak teks dari wilayah tertentu pada halaman

Ekstrak teks dari wilayah persegi panjang yang ditentukan pada halaman tertentu dari PDF menggunakan Aspose.PDF untuk Python. Dengan menentukan koordinat, Anda dapat memfokuskan ekstraksi pada area spesifik — seperti sel tabel, blok paragraf, atau wilayah bidang formulir.

Ideal untuk ekstraksi teks berbasis zona, seperti mengambil data dari header, footer, faktur, atau laporan tata letak tetap di mana teks muncul pada posisi yang dapat diprediksi.

1. Buka dokumen PDF.
1. Buat 'TextAbsorber'.
1. Konfigurasikan 'text_search_options' untuk membatasi pada wilayah persegi panjang.
1. Terapkan absorber pada halaman tertentu.
1. Tulis teks yang diekstrak.

```python

import os
import aspose.pdf as ap

def extract_text_from_region(infile, page_number, rect_coords, outfile):
    """
    Extract text from a specified rectangular region on a given page.
    Args:
        infile (str): Path to input PDF file.
        page_number (int): 1-based index of the page.
        rect_coords (tuple): (llx, lly, urx, ury) coordinates of the rectangle.
        outfile (str): Output text file path.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.TextAbsorber()
        # Set options to restrict search to the rectangle
        absorber.text_search_options.limit_to_page_bounds = True
        llx, lly, urx, ury = rect_coords
        absorber.text_search_options.rectangle = ap.Rectangle(llx, lly, urx, ury, True)
        # Accept on the specific page
        document.pages[page_number].accept(absorber)
        extracted_text = absorber.text
        with open(outfile, "w", encoding="utf-8") as tw:
            tw.write(extracted_text)
    finally:
        document.close()
```

## Ekstrak Paragraf dengan mengiterasi mereka

Kami dapat mendapatkan teks dari dokumen PDF dengan mencari teks tertentu (menggunakan "plain text" atau "regular expressions") dari satu halaman atau seluruh dokumen, atau kami dapat mendapatkan teks lengkap dari satu halaman, rentang halaman, atau seluruh dokumen. Namun, dalam beberapa kasus, Anda perlu mengekstrak paragraf dari dokumen PDF atau teks dalam bentuk Paragraf. Kami telah mengimplementasikan fungsi untuk mencari bagian dan paragraf dalam teks halaman dokumen PDF. Kami telah memperkenalkan Kelas ParagraphAbsorber (seperti TextFragmentAbsorber dan TextAbsorber), yang dapat digunakan untuk mengekstrak paragraf dari dokumen PDF.

Pustaka Aspose.PDF memungkinkan Anda membaca file PDF dan mengekstrak semua teks paragraf dari setiap halaman menggunakan 'ParagraphAbsorber'. Ia mengatur output berdasarkan halaman, bagian, dan paragraf, serta menulis konten yang diekstrak ke dalam file teks biasa. Ini berguna untuk analisis teks, pengarsipan, atau mengubah konten PDF terstruktur menjadi format yang dapat dibaca.

1. Buka dokumen PDF.
1. Buat instance 'ParagraphAbsorber'.
1. Panggil 'absorber.visit(document)' untuk memindai semua halaman mencari paragraf.
1. Lakukan perulangan pada koleksi 'page_markups' absorber.
1. Untuk setiap page‑markup, lakukan perulangan pada 'sections'-nya, kemudian setiap 'paragraph' dalam bagian tersebut.
1. Dalam setiap paragraf, lakukan perulangan pada 'lines', kemudian setiap 'fragment' dalam baris, mengakumulasi 'fragment.text'.
1. Tulis setiap paragraf (dengan indeks halaman/bagian/paragraf) ke file output.
1. Tutup dokumen setelah selesai.

```python

import os
import aspose.pdf as ap

def extract_paragraphs_from_pdf(infile, outfile):
    """
    Extract all paragraphs from a PDF document, and write each paragraph’s text into an output file.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.ParagraphAbsorber()
        absorber.visit(document)

        with open(outfile, "w", encoding="utf‑8") as tw:
            for page_markup in absorber.page_markups:
                for sec_idx, section in enumerate(page_markup.sections, start=1):
                    for para_idx, paragraph in enumerate(section.paragraphs, start=1):
                        # Concatenate all fragments/lines in the paragraph
                        parts = []
                        for line in paragraph.lines:
                            for fragment in line:
                                parts.append(fragment.text)
                            parts.append("\r\n")
                        paragraph_text = "".join(parts)
                        tw.write(f"Page {page_markup.number}, Section {sec_idx}, Paragraph {para_idx}:\n")
                        tw.write(paragraph_text + "\n")
    finally:
        document.close()
```

## Ekstrak Paragraf dengan rendering poligon pembatas

Potongan kode ini mengekstrak teks tingkat paragraf dan informasi tata letak dari halaman tertentu dalam PDF. Ia menangkap persegi panjang pembatas dan koordinat poligon masing‑masing paragraf, bersamaan dengan konten teks sebenarnya, dan menulis hasilnya ke file teks. Ini berguna untuk menganalisis struktur dokumen, pemetaan tata letak, atau menyiapkan data untuk tugas aksesibilitas dan ekstraksi konten.

1. Buka PDF dan muat dokumen.
1. Buat instance 'ParagraphAbsorber'.
1. Panggil 'absorber.visit(page)' untuk halaman spesifik yang Anda inginkan.
1. Dapatkan 'page_markup' pertama dari 'absorber.page_markups'.
1. Untuk setiap bagian dalam markup tersebut:
- Ambil 'rectangle'-nya.
1. Untuk setiap paragraf dalam bagian:
- Dapatkan 'points' (poligon) nya.
- Ekstrak teks dengan melakukan perulangan 'paragraph.lines' - 'fragment.text'.
1. Tulis informasi geometri dan teks ke file output.
1. Tutup dokumen.

```python

import os
import aspose.pdf as ap

def extract_paragraphs_with_geometry(infile, outfile):
    """
    Extract paragraphs and record geometry info (rectangle / polygon) for each paragraph in a PDF.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.ParagraphAbsorber()
        absorber.visit(document.pages[1])  # Visit page 2 (pages are 1-indexed)

        page_markup = absorber.page_markups[0]
        with open(outfile, "w", encoding="utf‑8") as tw:
            for sec_idx, section in enumerate(page_markup.sections, start=1):
                tw.write(f"Section {sec_idx}: rectangle = {section.rectangle}\n")
                for para_idx, paragraph in enumerate(section.paragraphs, start=1):
                    tw.write(f"  Paragraph {para_idx}: polygon = {paragraph.points}\n")
                    # Concatenate paragraph text
                    parts = []
                    for line in paragraph.lines:
                        for fragment in line:
                            parts.append(fragment.text)
                        parts.append("\r\n")
                    tw.write("    Text: " + "".join(parts) + "\n\n")
    finally:
        document.close()
```

