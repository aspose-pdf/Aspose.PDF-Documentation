---
title: Tambahkan Nomor Halaman ke PDF
linktitle: Tambahkan Nomor Halaman ke PDF
type: docs
weight: 30
url: /id/python-net/page-number/
description: Pelajari cara menambahkan nomor halaman ke dokumen PDF menggunakan PdfFileStamp dalam Python.
lastmod: "2026-06-12"
TechArticle: true
AlternativeHeadline: Tambahkan Nomor Halaman ke PDF dengan Python
Abstract: Artikel ini menjelaskan cara menambahkan nomor halaman ke dokumen PDF dengan Aspose.PDF for Python via .NET menggunakan facade PdfFileStamp. Artikel ini menunjukkan cara menambahkan nomor halaman dengan penempatan default, menempatkannya pada koordinat khusus, dan mengontrol perataan serta margin.
---

Aspose.PDF for Python via .NET menyediakan [PdfFileStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilestamp/) facade untuk menambahkan konten berulang ke halaman PDF. Anda dapat menggunakannya untuk menyisipkan nomor halaman dengan penempatan default, menempatkannya pada koordinat tertentu, atau mengontrol perataan dan margin mereka.

## Tambahkan nomor halaman dengan penempatan default

Gunakan `add_page_number()` tanpa argumen posisi tambahan ketika Anda ingin nomor halaman ditambahkan di lokasi default. Ini adalah cara paling sederhana untuk memberi nomor pada setiap halaman dalam dokumen.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_page_numbers_default(infile: str, outfile: str) -> None:
    """Add centered page numbers to the bottom of each page."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.add_page_number("Page #")
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Tambahkan nomor halaman pada koordinat khusus

Gunakan overload berbasis koordinat ketika Anda memerlukan nomor halaman muncul pada posisi X dan Y tertentu pada setiap halaman. Pendekatan ini berguna ketika tata letak dokumen memerlukan penempatan khusus.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_page_numbers_at_coordinates(infile: str, outfile: str) -> None:
    """Add page numbers at explicit X/Y coordinates."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.add_page_number("Page #", 300, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Tambahkan nomor halaman dengan perataan dan margin

Gunakan overload dengan argumen posisi dan margin ketika Anda membutuhkan kontrol lebih atas tempat nomor halaman muncul. Pada contoh ini, nomor‑nomor tersebut diatur menuju area kanan atas halaman dengan margin yang eksplisit.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_page_numbers_with_position_and_margins(infile: str, outfile: str) -> None:
    """Add page numbers using a predefined position and page margins."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.add_page_number(
            "Page #",
            pdf_facades.PdfFileStamp.POS_BOTTOM_RIGHT,
            10,
            10,
            10,
            10,
        )
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Tambahkan nomor halaman dengan gaya Romawi

Fungsi 'add_page_numbers_with_roman_style' menunjukkan cara meningkatkan dokumen PDF dengan menambahkan nomor halaman menggunakan angka Romawi kapital. Fungsi ini memanfaatkan kelas PdfFileStamp dari Aspose.PDF untuk menerapkan penomoran yang konsisten di semua halaman.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_page_numbers_with_roman_style(infile: str, outfile: str) -> None:
    """Add page numbers with a custom start value and Roman numbering."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.numbering_style = ap.NumberingStyle.NUMERALS_ROMAN_UPPERCASE
        pdf_stamper.starting_number = 42
        pdf_stamper.add_page_number("Page #", pdf_facades.PdfFileStamp.POS_UPPER_RIGHT)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```
