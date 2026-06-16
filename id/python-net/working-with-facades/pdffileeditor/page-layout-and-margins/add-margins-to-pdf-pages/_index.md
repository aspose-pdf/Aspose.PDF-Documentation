---
title: Tambahkan Margin ke Halaman PDF
linktitle: Tambahkan Margin ke Halaman PDF
type: docs
weight: 10
url: /id/python-net/add-margins-to-pdf-pages/
description: Tambahkan margin khusus ke halaman terpilih dari PDF menggunakan Aspose.PDF for Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tambahkan Margin Khusus ke Halaman PDF Tertentu dalam Python
Abstract: Pelajari cara menambahkan margin khusus ke halaman terpilih dari PDF menggunakan Aspose.PDF for Python. Contoh ini menunjukkan cara memperluas batas halaman dengan menentukan margin atas, bawah, kiri, dan kanan untuk tiap halaman, sehingga PDF menjadi lebih mudah dicetak atau konsisten secara visual.
---

Menambahkan margin ke halaman PDF dapat meningkatkan keterbacaan, menyiapkan dokumen untuk pencetakan, atau menyediakan ruang untuk anotasi. Dengan menggunakan Aspose.PDF for Python, pengembang dapat secara programatis menambahkan margin ke halaman tertentu dari PDF tanpa mengubah tata letak konten.

Dalam potongan kode ini, the [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) kelas digunakan untuk menambahkan margin 0,5 inci ke halaman 1 dan 3 dari dokumen input. Margin didefinisikan dalam poin (1 inci = 72 poin) dan diterapkan secara individual ke kiri, kanan, atas, dan bawah masing-masing halaman.

1. Buka dokumen PDF sumber.
1. Buat instance 'PdfFileEditor'.
1. Tentukan margin dan halaman yang akan dimodifikasi.
1. Terapkan margin menggunakan metode 'add_margins'.
1. Simpan PDF yang diperbarui ke file output.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Add Margins to PDF Pages
def add_margins_to_pdf_pages(infile, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    # Define the margins to be added (in points)
    left_margin = 36  # 0.5 inch
    right_margin = 36  # 0.5 inch
    top_margin = 36  # 0.5 inch
    bottom_margin = 36  # 0.5 inch

    pdf_editor.add_margins(
        infile, outfile, [1, 3], left_margin, right_margin, top_margin, bottom_margin
    )
```
