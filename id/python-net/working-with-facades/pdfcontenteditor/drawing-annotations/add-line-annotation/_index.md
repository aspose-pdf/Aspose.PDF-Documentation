---
title: Tambahkan Anotasi Garis
linktitle: Tambahkan Anotasi Garis
type: docs
weight: 30
url: /id/python-net/add-line-annotation/
description: Contoh ini mengikat PDF input, menggambar anotasi garis merah dengan ujung garis berbentuk kotak, dan menyimpan PDF yang telah dimodifikasi.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tambahkan Anotasi Garis ke PDF Menggunakan PdfContentEditor di Python
Abstract: Contoh ini menunjukkan cara menambahkan anotasi garis ke dokumen PDF menggunakan Aspose.PDF for Python via the Facades API. Ini menjelaskan cara menentukan titik awal dan akhir garis, batas persegi panjang, properti tampilan, dan menyimpan dokumen yang diperbarui.
---

Anotasi garis berguna untuk menekankan teks, menyoroti hubungan, atau menarik perhatian ke area tertentu dalam PDF. Dengan [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), Anda dapat secara programatis membuat anotasi garis dengan menentukan titik awal dan akhir, persegi panjang pembatas, warna, gaya border, dan ujung garis.

1. Buat objek PdfContentEditor.
1. Hubungkan PDF input.
1. Definisikan properti Anotasi Garis.
1. Tambahkan anotasi Garis.
1. Simpan Document yang diperbarui.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_line_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    # Create LineAnnotation object
    rect = apd.Rectangle(100, 100, 200, 200)
    contents = "This is line annotation"
    content_editor.create_line(
        rect,
        contents,
        100,
        100,
        200,
        200,
        1,
        1,
        apd.Color.red,
        "Solid",
        [3, 2],
        ["Square"],
    )

    # Save output PDF file
    content_editor.save(outfile)
```
