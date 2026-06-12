---
title: Tambahkan Markup Annotations
linktitle: Tambahkan Markup Annotations
type: docs
weight: 30
url: /id/python-net/add-markup-annotation/
description: Contoh ini mengikat PDF input, menambahkan empat anotasi markup berbeda ke halaman pertama, dan menyimpan dokumen yang diperbarui. Setiap anotasi menunjukkan gaya dan warna markup yang berbeda.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tambahkan Highlight, Underline, Strikeout, dan Squiggly Markup Annotations dalam PDF Menggunakan Python
Abstract: Contoh ini menunjukkan cara menambahkan beberapa anotasi markup—highlight, underline, strikeout, dan squiggly—ke dokumen PDF menggunakan Aspose.PDF for Python via the Facades API. Contoh tersebut memperlihatkan cara mendefinisikan area anotasi, menentukan jenis markup, menerapkan warna, dan menyimpan dokumen yang dimodifikasi.
---

Anotasi markup digunakan untuk menekankan atau meninjau teks dalam PDF. Dengan PdfContentEditor, Anda dapat secara programatis menerapkan berbagai gaya markup dengan menentukan area persegi panjang, teks komentar, jenis markup, nomor halaman, dan warna.

1. Buat [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) objek.
1. Hubungkan PDF input.
1. Definisikan persegi panjang Anotasi.
1. Tambahkan Anotasi Markup.
1. Simpan Document yang diperbarui.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_markup_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add markup annotation to page 1
    content_editor.create_markup(
        apd.Rectangle(120, 440, 200, 20),
        "This is a highlight annotation",
        0,
        1,
        apd.Color.yellow,
    )
    content_editor.create_markup(
        apd.Rectangle(110, 542, 200, 20),
        "This is a underline annotation",
        1,
        1,
        apd.Color.yellow,
    )
    content_editor.create_markup(
        apd.Rectangle(120, 568, 200, 20),
        "This is a strikeout annotation",
        2,
        1,
        apd.Color.orange_red,
    )
    content_editor.create_markup(
        apd.Rectangle(110, 598, 200, 20),
        "This is a squiggly annotation",
        3,
        1,
        apd.Color.dark_blue,
    )
    # Save updated document
    content_editor.save(outfile)
```
