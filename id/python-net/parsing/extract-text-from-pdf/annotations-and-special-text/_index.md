---
title: Anotasi dan Teks Khusus menggunakan Python
linktitle: Anotasi dan Teks Khusus
type: docs
weight: 40
url: /id/python-net/annotation-and-special-text/
description: Pelajari cara mengekstrak teks dari anotasi stempel, teks yang disorot, dan konten superskrip/subskrip dalam dokumen PDF menggunakan Aspose.PDF for Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Ekstrak Teks dari Anotasi Stempel

Gunakan [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber) untuk mengekstrak teks yang tertanam dalam sebuah [StampAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/stampannotation) appearance stream. Ini berguna ketika konten stempel dirender sebagai form XObject alih-alih disimpan sebagai teks biasa.

1. Buka [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document).
1. Akses anotasi target dari `page.annotations`.
1. Verifikasi bahwa itu adalah `StampAnnotation`, lalu ambil XForm tampilan normalnya.
1. Berikan XForm ke `TextAbsorber.visit()` untuk mengekstrak teks yang disematkan.

```python
import os
import aspose.pdf as ap


def extract_text_from_stamp(infile, page_number, annotation_index, outfile):
    """
    Extracts text from a stamp annotation on a given page in a PDF document.
    Args:
        infile (str): Path to the input PDF file.
        page_number (int): 1-based index of the page containing the stamp.
        annotation_index (int): 1-based index of the annotation in that page.
        outfile (str): Path to the output text file where extracted text will be saved.
    """
    document = ap.Document(infile)
    try:
        page = document.pages[page_number]
        annot = page.annotations[annotation_index]
        # Ensure it's a StampAnnotation
        if isinstance(annot, ap.annotations.StampAnnotation):
            # Get normal appearance XForm of the stamp
            xform = annot.appearance["N"]
            absorber = ap.text.TextAbsorber()
            absorber.visit(xform)
            extracted = absorber.text
            with open(outfile, "w", encoding="utf-8") as f:
                f.write(extracted)
    finally:
        document.close()
```

## Ekstrak Teks yang Disorot

Iterasi anotasi halaman dan gunakan [HighlightAnnotation.get_marked_text()](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/highlightannotation) untuk membaca rentang teks yang dicakup oleh setiap sorotan. Koleksi anotasi halaman bersifat 1-based.

1. Buka [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document) dan pilih halaman target.
1. Iterasi melalui `page.annotations`.
1. Gunakan `is_assignable` untuk memfilter [HighlightAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/highlightannotation) instansi.
1. Lakukan casting pada anotasi dan panggil `get_marked_text()` untuk mengambil konten yang disorot.

```python
def extract_highlight_text(infile):
    """
    Extract text from highlight annotations.

    Args:
        infile (str): Input PDF filename

    Returns:
        None

    Example:
        extract_highlight_text("sample.pdf")

    Note:
        Prints marked text from each highlight annotation on first page.
    """
    document = ap.Document(infile)
    page = document.pages[1]

    for annotation in page.annotations:
        if is_assignable(annotation, ap.annotations.HighlightAnnotation):
            highlight_annotation = cast(ap.annotations.HighlightAnnotation, annotation)
            print(highlight_annotation.get_marked_text())
```

## Ekstrak Teks Superskrip dan Subskrip

Superskrip dan subskrip muncul secara sering dalam formula, ekspresi matematika, dan nama senyawa kimia. Aspose.PDF for Python via .NET mendukung ekstraksi konten ini melalui [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber), yang mendeteksi metadata penempatan tingkat karakter.

1. Buka [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document).
1. Buat sebuah `TextFragmentAbsorber` instansi.
1. Panggilan `document.pages[page_number].accept(absorber)` untuk memindai halaman target.
1. Ambil teks lengkap yang diekstrak dari `absorber.text`.
1. Tuliskan hasil ke file dan tutup dokumen.

```python
import os
import aspose.pdf as ap


def extract_super_sub_text(infile, outfile, page_number=1):
    """
    Extract text (including superscript/subscript) from a specified page of a PDF and write to a text file.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
        page_number (int): 1‑based index of the page to extract.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.TextFragmentAbsorber()
        # Accept only the specific page for extraction
        document.pages[page_number].accept(absorber)
        extracted_text = absorber.text
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(extracted_text)
    finally:
        document.close()
```

## Iterasi melalui Text Fragments untuk Mendeteksi Superscript/Subscript

Untuk inspeksi per-fragment, iterasi atas `absorber.text_fragments` dan baca itu `text_state.superscript` dan `text_state.subscript` bendera boolean pada masing-masing [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment).

1. Buka [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document) dan buat sebuah [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber).
1. Terima absorber pada halaman target untuk mengisi `absorber.text_fragments`.
1. Untuk setiap fragmen, baca `fragment.text`, `fragment.text_state.superscript`, dan `fragment.text_state.subscript`.
1. Tulis hasilnya ke file output dan tutup dokumen.

```python
import os
import aspose.pdf as ap


def extract_super_sub_details(infile, outfile, page_number=1):
    """
    Extract details of each text fragment on a page, identifying superscript and subscript items.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
        page_number (int): 1‑based page index.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.TextFragmentAbsorber()
        document.pages[page_number].accept(absorber)

        with open(outfile, "w", encoding="utf-8") as f:
            for fragment in absorber.text_fragments:
                text = fragment.text
                is_sup = fragment.text_state.superscript  # True if superscript
                is_sub = fragment.text_state.subscript  # True if subscript
                f.write(
                    f"Text: '{text}' | Superscript: {is_sup} | Subscript: {is_sub}\n"
                )
    finally:
        document.close()
```
