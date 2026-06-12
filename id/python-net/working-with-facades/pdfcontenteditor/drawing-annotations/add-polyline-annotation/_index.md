---
title: Tambahkan Anotasi Polyline
linktitle: Tambahkan Anotasi Polyline
type: docs
weight: 50
url: /id/python-net/add-polyline-annotation/
description: Contoh ini mengikat PDF input, membuat polyline solid pada halaman pertama, dan menyimpan dokumen yang telah dimodifikasi dengan anotasi.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tambahkan Anotasi Polyline ke PDF Menggunakan PdfContentEditor dalam Python
Abstract: Contoh ini menunjukkan cara menambahkan anotasi polyline ke dokumen PDF menggunakan Aspose.PDF for Python via the Facades API. Ini menunjukkan cara mendefinisikan urutan titik‑titik, gaya batas, persegi panjang anotasi, teks, dan menyimpan dokumen yang diperbarui.
---

Anotasi polyline memungkinkan Anda menyorot serangkaian segmen garis yang terhubung dalam PDF. Menggunakan [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), Anda dapat menggambar polyline dengan menentukan koordinat titik, gaya batas, nomor halaman, dan batas anotasi. Ini berguna untuk merepresentasikan secara visual jalur, tren, atau koneksi dalam diagram dan dokumen.

1. Buat objek PdfContentEditor.
1. Gabungkan PDF input.
1. Konfigurasikan properti Polyline.
1. Tambahkan anotasi Polyline.
1. Simpan Document yang diperbarui.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_polyline_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    line_info = pdf_facades.LineInfo()
    line_info.border_style = 0  # 0 - Solid
    line_info.vertice_coordinate = [120, 420, 180, 460, 230, 430, 290, 470]
    content_editor.create_poly_line(
        line_info,
        1,
        apd.Rectangle(110, 410, 200, 90),
        "This is polyline annotation",
    )

    # Save output PDF file
    content_editor.save(outfile)
```
