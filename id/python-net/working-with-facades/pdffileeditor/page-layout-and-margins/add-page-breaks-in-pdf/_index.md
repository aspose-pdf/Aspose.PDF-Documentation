---
title: Tambahkan Pemisah Halaman dalam PDF
linktitle: Tambahkan Pemisah Halaman dalam PDF
type: docs
weight: 20
url: /id/python-net/add-page-breaks-in-pdf/
description: Sisipkan pemisah halaman ke dalam dokumen PDF menggunakan Aspose.PDF for Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tambahkan Pemisah Halaman ke Halaman PDF secara Programatis dengan Python
Abstract: Pelajari cara menyisipkan pemisah halaman ke dalam dokumen PDF menggunakan Aspose.PDF for Python. Contoh ini menunjukkan cara memotong halaman pada posisi vertikal yang ditentukan, memungkinkan pengembang untuk menata ulang konten dan membuat halaman tambahan secara dinamis.
---

Pemisah halaman berguna ketika Anda perlu memecah halaman PDF yang panjang menjadi beberapa halaman atau mengontrol bagaimana konten didistribusikan di seluruh dokumen. Dengan menggunakan Aspose.PDF for Python, pengembang dapat menyisipkan pemisah halaman pada posisi tertentu tanpa harus mengedit PDF secara manual.

Artikel ini menunjukkan cara menggunakan metode 'add_page_break' dari [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) kelas untuk menyisipkan jeda halaman pada koordinat vertikal yang ditentukan pada halaman yang dipilih. Metode ini membuat halaman baru dan memindahkan konten di bawah titik jeda ke halaman itu.

1. Buat Objek PdfFileEditor.
1. Tentukan Posisi Jeda Halaman.
1. Sisipkan Jeda Halaman.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Add Page Breaks in PDF
def add_page_breaks_in_pdf(infile, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.add_page_break(
        infile,
        outfile,
        [
            pdf_facades.PdfFileEditor.PageBreak(1, 400),
        ],
    )
```
