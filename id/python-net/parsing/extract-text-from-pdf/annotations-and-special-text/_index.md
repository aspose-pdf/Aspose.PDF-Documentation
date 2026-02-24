---
title: Anotasi dan Teks Khusus menggunakan Python
linktitle: Anotasi dan Teks Khusus
type: docs
weight: 40
url: /id/python-net/annotation-and-special-text/
description: Bagian ini berisi artikel tentang anotasi dan ekstraksi Teks khusus dari dokumen PDF menggunakan Aspose.PDF dalam Python.
lastmod: "2025-11-05"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## Ekstrak Teks dari Anotasi Stempel

Perpustakaan Aspose.PDF untuk Python memungkinkan Anda mengekstrak teks dari anotasi stempel (khususnya StampAnnotation) pada halaman PDF.

1. Buka dokumen.
1. Akses anotasi stempel dari koleksi anotasi halaman.
1. Dapatkan aliran tampilan (appearance stream) dari stempel (XForm).
1. Gunakan 'TextAbsorber' untuk mengekstrak teks yang tersemat dari tampilan tersebut.

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

Standar PDF menyediakan kemampuan untuk menyorot bagian-bagian teks dalam sebuah dokumen. Untuk mengekstrak konten yang disorot tersebut, ikuti langkah-langkah berikut:

1. Impor `aspose.pdf as ap` dan helper apa pun yang Anda gunakan (`is_assignable`, `cast`).
2. Panggil `ap.Document(infile)` untuk membuka PDF.
3. Pilih halaman yang diinginkan dengan `document.pages` (koleksi halaman dimulai dari 1).
4. Lakukan perulangan pada `page.annotations` untuk memeriksa setiap anotasi pada halaman tersebut.
5. Filter anotasi sehingga hanya anotasi sorotan yang diproses.
6. Cast anotasi menjadi `HighlightAnnotation` dan panggil `get_marked_text()` untuk membaca teks yang disorot.
7. Cetak atau tangani teks yang dikembalikan dengan cara lain.

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

**SubScripts dan SuperScripts** paling sering digunakan dalam formula, ekspresi matematis, dan spesifikasi senyawa kimia. Sulit untuk mengeditnya ketika banyak yang muncul dalam satu bagian teks.
Dalam salah satu rilis terbaru, perpustakaan **Aspose.PDF for Python via .NET** menambahkan dukungan untuk mengekstrak teks SuperScripts dan SubScripts dari PDF. Ekstrak semua teks (termasuk superskrip dan subskrip) dari halaman tertentu dokumen PDF menggunakan 'TextFragmentAbsorber'.

1. Muat dokumen PDF.
1. Buat instance 'TextFragmentAbsorber()', yang mendukung deteksi teks superskrip/subskrip sesuai kemampuan versi.
1. Panggil 'document.pages[page_number].accept(absorber)' untuk memindai hanya halaman yang diberikan.
1. Dapatkan teks yang diekstrak melalui 'absorber.text'.
1. Tulis teks ke dalam file output menggunakan I/O file standar.
1. Tutup dokumen untuk melepaskan sumber daya.

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
        with open(outfile, "w", encoding="utf‑8") as f:
            f.write(extracted_text)
    finally:
        document.close()
```

## Iterasi melalui TextFragments untuk Mendeteksi Superskrip/Subskrip

Lakukan perulangan pada setiap fragmen teks dalam sebuah halaman, periksa apakah itu superskrip atau subskrip, dan proses sesuai.

1. Muat dokumen PDF.
1. Buat 'TextFragmentAbsorber()' dan terima (accept) pada halaman yang dipilih.
1. Akses 'absorber.text_fragments', yang mengembalikan koleksi fragmen yang ditemukan pada halaman tersebut.
1. Untuk setiap fragmen:
- Dapatkan 'fragment.text'.
- Periksa 'fragment.text_state.superscript' dan 'fragment.text_state.subscript'.
- Tulis satu baris ke file output dengan teks fragmen dan flag.
1. Tutup file dan dokumen.

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

        with open(outfile, "w", encoding="utf‑8") as f:
            for fragment in absorber.text_fragments:
                text = fragment.text
                is_sup = fragment.text_state.superscript  # True if superscript
                is_sub = fragment.text_state.subscript    # True if subscript
                f.write(f"Text: '{text}' | Superscript: {is_sup} | Subscript: {is_sub}\n")
    finally:
        document.close()
```
