---
title: Ekstraksi Teks Dasar menggunakan Python
linktitle: Ekstraksi Teks Dasar
type: docs
weight: 10
url: /id/python-net/basic-text-extraction/
description: Pelajari cara mengekstrak teks dari dokumen PDF menggunakan Aspose.PDF for Python — dari semua halaman sekaligus atau dari halaman tertentu.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Ekstrak teks dari semua halaman dokumen PDF

Gunakan [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber) untuk menangkap semua teks dari setiap halaman dokumen PDF dan menuliskannya ke file teks. Pendekatan ini sangat cocok untuk mengonversi PDF menjadi teks yang dapat dicari, menjalankan analisis konten, atau menyiapkan teks untuk pengindeksan dan pemrosesan lanjutan.

1. Buka dokumen PDF menggunakan [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document).
1. Buat sebuah `TextAbsorber` instansi.
1. Panggilan `document.pages.accept(text_absorber)` untuk memindai semua halaman.
1. Ambil teks yang diekstrak dari `text_absorber.text`.
1. Tuliskan hasilnya ke file teks keluaran.

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
    # Create a TextAbsorber to extract text
    text_absorber = ap.text.TextAbsorber()
    # Accept the absorber for all pages
    document.pages.accept(text_absorber)
    # Get extracted text
    extracted_text = text_absorber.text
    # Write the text to an output file
    with open(outfile, "w", encoding="utf-8") as tw:
        tw.write(extracted_text)
```

## Ekstrak teks dari halaman tertentu

Terapkan [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber) ke satu halaman untuk mengisolasi dan menyimpan teks dari bagian tersebut dalam dokumen multi‑halaman. Ini berguna ketika Anda hanya membutuhkan konten dari satu halaman — misalnya, faktur, bagian laporan, atau ringkasan formulir.

1. Buka dokumen PDF menggunakan [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document).
1. Buat sebuah `TextAbsorber` instansi.
1. Panggilan `accept` pada halaman target: `document.pages[page_number].accept(text_absorber)`.
1. Ambil teks yang diekstraksi dan tulis ke sebuah file.

```python
import os
import aspose.pdf as ap


def extract_text_from_page(infile, outfile, page_number):
    """
    Extract text from a specific page number of the PDF.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
        page_number (int): 1-based page index to extract.
    """
    document = ap.Document(infile)
    text_absorber = ap.text.TextAbsorber()
    # Accept the absorber on only the specified page
    document.pages[page_number].accept(text_absorber)
    extracted_text = text_absorber.text
    with open(outfile, "w", encoding="utf-8") as tw:
        tw.write(extracted_text)
```
