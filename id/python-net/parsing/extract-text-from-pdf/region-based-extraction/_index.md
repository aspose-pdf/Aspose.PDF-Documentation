---
title: Ekstraksi Berbasis Wilayah menggunakan Python
linktitle: Ekstraksi Berbasis Wilayah
type: docs
weight: 20
url: /id/python-net/region-based-extraction/
description: Pelajari cara mengekstrak teks dari wilayah halaman tertentu atau struktur paragraf dalam dokumen PDF dengan Aspose.PDF for Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Ekstrak teks dari wilayah tertentu pada halaman

Gunakan [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber/) bersama dengan sebuah [Rectangle](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) untuk membatasi ekstraksi ke area spesifik pada sebuah halaman. Pendekatan ini berguna untuk ekstraksi berbasis zona dari header, footer, sel tabel, form fields, faktur, atau wilayah tata letak tetap lainnya di mana posisi teks sudah diketahui sebelumnya.

1. Buka PDF sumber sebagai [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Buat sebuah `TextAbsorber` instansi.
1. Konfigurasi `text_search_options` untuk membatasi ekstraksi ke sebuah persegi panjang.
1. Terima absorber pada halaman target.
1. Tuliskan teks yang diekstrak ke file output.

```python
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

## Ekstrak Paragraf dengan mengiterasi melalui mereka

Gunakan [ParagraphAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/paragraphabsorber/) ketika Anda membutuhkan ekstraksi yang memperhatikan paragraf alih-alih teks halaman biasa. Tidak seperti [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber/) atau [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/), API ini mengatur output berdasarkan halaman, bagian, dan paragraf, yang berguna untuk analisis teks, ekspor terstruktur, dan pemrosesan sensitif tata letak.

1. Buka PDF sumber sebagai [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Buat sebuah `ParagraphAbsorber` instansi.
1. Panggilan `absorber.visit(document)` untuk menganalisis semua halaman.
1. Iterasi melalui `page_markups`, kemudian melalui setiap bagian dan paragraf.
1. Baca fragmen teks dari setiap paragraf dan tulis hasilnya ke sebuah file.

```python
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

        with open(outfile, "w", encoding="utf-8") as tw:
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
                        tw.write(
                            f"Page {page_markup.number}, Section {sec_idx}, Paragraph {para_idx}:\n"
                        )
                        tw.write(paragraph_text + "\n")
    finally:
        document.close()
```

## Ekstrak Paragraf dengan rendering poligon pembatas

Anda juga dapat menggunakan [ParagraphAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/paragraphabsorber/) untuk memeriksa geometri paragraf. Selain mengekstrak teks, pendekatan ini mencatat setiap persegi panjang bagian dan poligon paragraf, yang berguna untuk pemetaan tata letak, analisis dokumen, alat aksesibilitas, atau pemrosesan lanjutan yang menyadari wilayah.

1. Buka PDF sumber sebagai [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Buat sebuah `ParagraphAbsorber` instansi.
1. Kunjungi halaman target.
1. Baca markup halaman dari `absorber.page_markups`.
1. Iterasi melalui bagian dan paragraf untuk menangkap geometri dan teks.
1. Tulis data persegi panjang, poligon, dan teks ke file output.

```python
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
        with open(outfile, "w", encoding="utf-8") as tw:
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
