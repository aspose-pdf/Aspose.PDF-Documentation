---
title: Tambahkan Anotasi Poligon
linktitle: Tambahkan Anotasi Poligon
type: docs
weight: 40
url: /id/python-net/add-polygon-annotation/
description: Contoh ini mengaitkan PDF input, menggambar poligon padat pada halaman pertama, dan menyimpan dokumen yang dimodifikasi dengan anotasi.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tambahkan Anotasi Poligon ke PDF Menggunakan PdfContentEditor dalam Python
Abstract: Contoh ini menunjukkan cara menambahkan anotasi poligon ke dokumen PDF menggunakan Aspose.PDF for Python via the Facades API. Ini memperlihatkan cara mendefinisikan titik-titik verteks poligon, gaya batas, batas anotasi, teks deskriptif, dan menyimpan dokumen yang diperbarui.
---

Anotasi poligon digunakan untuk menyorot area atau bentuk tidak beraturan dalam PDF, memberikan penekanan visual atau menandai wilayah tertentu. Menggunakan [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), Anda dapat membuat poligon dengan menentukan koordinat verteks, gaya batas, nomor halaman, dan persegi panjang anotasi.

1. Buat objek PdfContentEditor.
1. Gabungkan PDF input.
1. Konfigurasikan properti Polygon.
1. Tambahkan anotasi Polygon.
1. Simpan Document yang diperbarui.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_polygon_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    line_info = pdf_facades.LineInfo()
    line_info.border_style = 0  # 0 - Solid
    line_info.vertice_coordinate = [100, 200, 150, 260, 220, 220, 200, 160]
    content_editor.create_polygon(
        line_info,
        1,
        apd.Rectangle(90, 150, 150, 120),
        "This is polygon annotation",
    )

    # Save output PDF file
    content_editor.save(outfile)
```
