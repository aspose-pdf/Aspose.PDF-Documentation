---
title: Kelas Stamp
linktitle: Kelas Stamp
type: docs
weight: 150
url: /id/python-net/stamp-class/
description: Pelajari cara bekerja dengan kelas Stamp untuk menambahkan stempel berbasis gambar, PDF, dan teks ke dokumen PDF dalam Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF for Python via .NET menyediakan [Stempel](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/stamp/) kelas untuk menempatkan konten visual yang dapat digunakan kembali pada halaman PDF. Sebuah stamp dapat didasarkan pada teks, gambar, atau bahkan halaman dari PDF lain, dan dapat diposisikan, diputar, diberi gaya, serta dibatasi pada halaman tertentu.

Artikel ini menunjukkan beberapa alur kerja cap umum:

1. Buat sumber daya teks yang dapat digunakan kembali untuk stempel berbasis teks.
1. Tambahkan stempel gambar dan halaman PDF.
1. Tambahkan stempel teks bergaya.
1. Batasi stempel pada halaman yang dipilih.
1. Konfigurasikan cap gambar latar belakang.

Contoh ini menggunakan dua fungsi pembantu: satu membuat teks terformat untuk cap berbasis teks, dan yang lainnya membuat sebuah `TextState` objek yang digunakan untuk menata stempel teks.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def _create_text_logo(text: str) -> pdf_facades.FormattedText:
    """Create formatted text for text stamp examples."""
    return pdf_facades.FormattedText(
        text,
        drawing.Color.blue,
        drawing.Color.light_gray,
        pdf_facades.FontStyle.HELVETICA_BOLD,
        pdf_facades.EncodingType.WINANSI,
        True,
        14,
    )


def _create_text_state() -> ap.text.TextState:
    """Create a text state used to style text stamps."""
    text_state = ap.text.TextState()
    text_state.foreground_color = ap.Color.dark_blue
    text_state.font_size = 16
    text_state.font_style = ap.text.FontStyles.BOLD
    return text_state
```

## Tambahkan cap gambar

Gunakan `bind_image()` ketika stempel harus menampilkan gambar seperti logo, lencana, atau ikon. Setelah mengikat gambar, Anda dapat mengatur ID stempel dan asalnya sebelum menambahkannya ke dokumen.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def add_image_stamp(infile: str, image_file: str, outfile: str) -> None:
    """Add an image stamp to the PDF."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_image(image_file)
        stamp.stamp_id = 1
        stamp.set_origin(36, 520)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Tambahkan halaman PDF sebagai stempel

Gunakan `bind_pdf()` ketika Anda ingin menggunakan halaman dari file PDF lain sebagai konten stamp. Ini berguna untuk overlay seperti persetujuan, templat, atau elemen visual yang sudah dibuat sebelumnya yang disimpan dalam dokumen terpisah.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def add_pdf_page_as_stamp(infile: str, stamp_pdf: str, outfile: str) -> None:
    """Add the first page of another PDF as a stamp."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_pdf(stamp_pdf, 1)
        stamp.page_number = 1
        stamp.set_origin(36, 250)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Tambahkan text stamp dengan text state

Gunakan `bind_logo()` bersama dengan `bind_text_state()` ketika Anda ingin membuat stempel berbasis teks dengan gaya font khusus. Pendekatan ini berguna untuk tanda persetujuan, label, dan anotasi khusus alur kerja.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def add_text_stamp_with_text_state(infile: str, outfile: str) -> None:
    """Add a text stamp and style it with a TextState object."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_logo(_create_text_logo("Approved by signing workflow"))
        stamp.bind_text_state(_create_text_state())
        stamp.set_origin(36, 700)
        stamp.rotation = 15.0

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Tambahkan stempel ke halaman tertentu

Jika cap tidak seharusnya muncul di setiap halaman, tetapkan nomor halaman target ke `pages` properti. Contoh ini menambahkan stempel gambar hanya pada halaman pertama.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def add_stamp_to_specific_pages(infile: str, image_file: str, outfile: str) -> None:
    """Add an image stamp only to the selected pages."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_image(image_file)
        stamp.pages = [1]
        stamp.set_origin(400, 40)
        stamp.set_image_size(120, 60)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Tambahkan cap gambar latar belakang

Gunakan stempel latar belakang ketika gambar harus muncul di belakang konten halaman. Anda juga dapat mengontrol opasitas stempel, rotasi, kualitas, ukuran, dan posisi untuk membuat efek gaya watermark.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def add_background_image_stamp(infile: str, image_file: str, outfile: str) -> None:
    """Add a rotated background image stamp with opacity and quality settings."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_image(image_file)
        stamp.is_background = True
        stamp.opacity = 0.35
        stamp.quality = 90
        stamp.rotation = 45.0
        stamp.set_image_size(160, 80)
        stamp.set_origin(200, 300)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Topik Facade Terkait

- [Bekerja dengan PDF Facades di Python](/pdf/id/python-net/working-with-facades/)
- [Tambahkan header, footer, dan cap dengan PdfFileStamp](/pdf/id/python-net/pdffilestamp-class/)
- [Tambahkan cap halaman ke file PDF dalam Python](/pdf/id/python-net/add-stamp/)
