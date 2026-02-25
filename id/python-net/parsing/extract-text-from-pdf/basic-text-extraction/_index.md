---
title: Ekstraksi Teks Dasar menggunakan Python
linktitle: Ekstraksi Teks Dasar
type: docs
weight: 10
url: /id/python-net/basic-text-extraction/
description: Bagian ini berisi artikel tentang ekstraksi teks dasar dari dokumen PDF menggunakan Aspose.PDF dalam Python.
lastmod: "2025-11-05"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## Ekstrak teks dari semua halaman dokumen PDF

Aspose.PDF for Python mengajarkan Anda cara mengekstrak teks dari setiap halaman dokumen PDF. Ini menggunakan kelas TextAbsorber untuk menangkap semua konten teks dari seluruh dokumen dan menyimpannya ke dalam file teks terpisah.
Ideal untuk mengonversi PDF menjadi teks yang dapat dicari, melakukan analisis konten, atau mengekspor teks untuk tugas pengindeksan dan pemrosesan.

1. Muat file PDF.
1. Buat objek 'TextAbsorber'.
1. Panggil 'document.pages.accept(text_absorber)' sehingga memindai semua halaman.
1. Dapatkan teks lengkap melalui 'text_absorber.text'.
1. Tulis hasilnya ke dalam file teks.

```python

import os
import aspose.pdf as ap

def extract_text_from_all_pages(infile, outfile):
    """
    Extract all text from every page of the PDF and write to an output text file.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
    """
    # Open the PDF document
    document = ap.Document(infile)
    try:
        # Create a TextAbsorber to extract text
        text_absorber = ap.text.TextAbsorber()
        # Accept the absorber for all pages
        document.pages.accept(text_absorber)
        # Get extracted text
        extracted_text = text_absorber.text
        # Write the text to an output file
        with open(outfile, "w", encoding="utf-8") as tw:
            tw.write(extracted_text)
    finally:
        document.close()
```

## Ekstrak teks dari halaman tertentu

Ekstrak teks dari satu halaman dokumen PDF. Dengan menerapkan TextAbsorber hanya pada halaman yang ditentukan, Anda dapat mengisolasi dan menyimpan teks dari bagian tertentu dari PDF multi-halaman.

Berguna ketika Anda hanya membutuhkan konten dari satu halaman — misalnya, mengekstrak teks dari halaman faktur, bagian laporan, atau ringkasan bidang formulir.

1. Buka PDF.
1. Buat TextAbsorber.
1. Terima hanya halaman yang ditentukan (pages[page_number]).
1. Ekstrak teks dan tulis ke file.

```python

import os
import aspose.pdf as ap

def extract_text_from_page(infile, page_number, outfile):
    """
    Extract text from a specific page number of the PDF.
    Args:
        infile (str): Path to input PDF file.
        page_number (int): 1-based page index to extract.
        outfile (str): Path to output text file.
    """
    document = ap.Document(infile)
    try:
        text_absorber = ap.text.TextAbsorber()
        # Accept the absorber on only the specified page
        document.pages[page_number].accept(text_absorber)
        extracted_text = text_absorber.text
        with open(outfile, "w", encoding="utf-8") as tw:
            tw.write(extracted_text)
    finally:
        document.close()
```

