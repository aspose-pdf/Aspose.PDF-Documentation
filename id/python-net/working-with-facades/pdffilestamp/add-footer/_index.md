---
title: Tambahkan Footer ke PDF
linktitle: Tambahkan Footer ke PDF
type: docs
weight: 10
url: /id/python-net/add-footer/
description: Pelajari cara menambahkan footer teks dan gambar ke halaman PDF menggunakan PdfFileStamp di Python.
lastmod: "2026-06-12"
TechArticle: true
AlternativeHeadline: Tambahkan Footer Teks dan Gambar ke PDF dengan Python
Abstract: Artikel ini menjelaskan cara menambahkan konten footer ke dokumen PDF dengan Aspose.PDF for Python via .NET menggunakan antarmuka PdfFileStamp. Artikel ini menunjukkan cara menambahkan footer teks, menempatkan footer gambar, dan menerapkan margin footer kustom sebelum menyimpan PDF yang telah diperbarui.
---

Aspose.PDF for Python via .NET menyediakan [PdfFileStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilestamp/) facade untuk menambahkan konten berulang ke halaman PDF. Anda dapat menggunakannya untuk menempatkan teks atau gambar footer di bagian bawah setiap halaman dan menyesuaikan margin footer untuk mengontrol penempatan.

## Tambahkan footer teks

Gunakan `add_footer()` dengan sebuah `FormattedText` objek ketika Anda ingin menempatkan footer teks yang sama pada setiap halaman PDF. Argumen kedua mengatur margin bawah yang digunakan untuk penempatan footer.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_text_footer(infile: str, outfile: str) -> None:
    """Add a text footer with a bottom margin."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        text = pdf_facades.FormattedText("Sample Footer")
        pdf_stamper.add_footer(text, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Tambahkan footer gambar

Gunakan `add_footer()` dengan aliran gambar ketika footer harus menampilkan logo atau gambar lain alih-alih teks. Contohnya membuka file gambar sebagai aliran biner dan menempatkannya di bagian bawah setiap halaman.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_image_footer(infile: str, image_file: str, outfile: str) -> None:
    """Add an image footer with a bottom margin."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.add_footer(image_file, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Tambahkan footer dengan margin khusus

Gunakan overload dengan tiga nilai margin ketika Anda membutuhkan kontrol lebih besar atas penempatan footer. Dalam contoh ini, footer ditambahkan dengan margin bawah, kiri, dan kanan yang disesuaikan.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_footer_with_margins(infile: str, outfile: str) -> None:
    """Add a text footer with bottom, left, and right margins."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        text = pdf_facades.FormattedText("This footer has margins on all sides.")
        pdf_stamper.add_footer(text, 20, 20, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```
