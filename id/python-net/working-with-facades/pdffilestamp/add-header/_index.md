---
title: Tambahkan Header ke PDF
linktitle: Tambahkan Header ke PDF
type: docs
weight: 20
url: /id/python-net/add-header/
description: Pelajari cara menambahkan header teks dan gambar ke halaman PDF menggunakan PdfFileStamp dalam Python.
lastmod: "2026-06-12"
TechArticle: true
AlternativeHeadline: Tambahkan Header Teks dan Gambar ke PDF dalam Python
Abstract: Artikel ini menjelaskan cara menambahkan konten header ke dokumen PDF dengan Aspose.PDF for Python via .NET menggunakan fasad PdfFileStamp. Artikel ini menunjukkan cara menambahkan header teks, menempatkan header gambar, dan menerapkan margin header khusus sebelum menyimpan PDF yang diperbarui.
---

Aspose.PDF for Python via .NET menyediakan [PdfFileStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilestamp/) fasad untuk menambahkan konten berulang ke halaman PDF. Anda dapat menggunakannya untuk menempatkan teks header atau gambar di bagian atas setiap halaman dan menyesuaikan margin header untuk mengontrol penempatan.

## Tambahkan header teks

Gunakan `add_header()` dengan sebuah `FormattedText` objek ketika Anda ingin menempatkan teks header yang sama pada setiap halaman PDF. Argumen kedua mendefinisikan margin atas untuk header.

```python
import sys
from os import path

import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_text_header(infile: str, outfile: str) -> None:
    """Add a text header with a top margin."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        text = pdf_facades.FormattedText("Sample Header")
        pdf_stamper.add_header(text, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Tambahkan header gambar

Gunakan `add_header()` dengan file gambar atau aliran gambar ketika header harus menampilkan logo atau grafik lain. Ini berguna untuk tata letak dokumen bermerek.

```python
import sys
from os import path

import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_image_header(infile: str, image_file: str, outfile: str) -> None:
    """Add an image header with a top margin."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.add_header(image_file, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Tambahkan header dengan margin khusus

Gunakan overload dengan tiga nilai margin ketika Anda memerlukan kontrol lebih pada penempatan header. Pada contoh ini, header ditambahkan dengan margin atas, kiri, dan kanan yang khusus.

```python
import sys
from os import path

import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_header_with_margins(infile: str, outfile: str) -> None:
    """Add a text header with top, left, and right margins."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        text = pdf_facades.FormattedText(
            text="Sample Header",
            text_color=ap_pydrawing.Color.blue,
            font_name="Arial",
            text_encoding=pdf_facades.EncodingType.WINANSI,
            embedded=True,
            font_size=12.0,
        )
        pdf_stamper.add_header(text, 20, 20, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```
