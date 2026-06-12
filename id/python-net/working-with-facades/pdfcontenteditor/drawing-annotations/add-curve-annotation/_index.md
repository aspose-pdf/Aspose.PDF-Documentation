---
title: Tambahkan Anotasi Kurva
linktitle: Tambahkan Anotasi Kurva
type: docs
weight: 20
url: /id/python-net/add-curve-annotation/
description: Contoh ini mengikat PDF input, menggambar kurva putus-putus pada halaman pertama, dan menyimpan dokumen yang telah dimodifikasi.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tambahkan Anotasi Kurva ke PDF Menggunakan PdfContentEditor dalam Python
Abstract: Contoh ini memperlihatkan cara menambahkan anotasi kurva ke dokumen PDF menggunakan Aspose.PDF for Python melalui Facades API. Ini menunjukkan cara mendefinisikan titik-titik kurva, gaya batas, batas anotasi, konten teks, dan menyimpan dokumen yang diperbarui.
---

Anotasi kurva digunakan untuk menyoroti jalur atau bentuk tidak teratur dalam PDF, memberikan penekanan visual atau menandai area penting. Menggunakan [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), Anda dapat menggambar kurva dengan menentukan urutan titik, gaya batas, visibilitas, persegi panjang anotasi, dan teks deskriptif.

1. Buat objek PdfContentEditor.
1. Ikat PDF onput.
1. Konfigurasikan properti Curve.
1. Gambar anotasi Curve.
1. Simpan Document yang diperbarui.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_curve_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    line_info = pdf_facades.LineInfo()
    line_info.border_style = 1  # 1 - Dashed
    line_info.vertice_coordinate = [120, 520, 160, 560, 220, 540, 280, 580]
    line_info.visibility = True
    content_editor.draw_curve(
        line_info,
        1,
        apd.Rectangle(110, 510, 220, 100),
        "This is curve annotation",
    )

    # Save output PDF file
    content_editor.save(outfile)
```
