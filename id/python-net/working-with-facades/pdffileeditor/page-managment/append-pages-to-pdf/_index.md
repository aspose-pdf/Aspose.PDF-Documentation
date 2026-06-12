---
title: Tambahkan Halaman ke PDF
linktitle: Tambahkan Halaman ke PDF
type: docs
weight: 10
url: /id/python-net/append-pages-to-pdf/
description: Tambahkan halaman dari satu dokumen PDF ke dokumen lain menggunakan Aspose.PDF for Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tambahkan Halaman dari Satu PDF ke PDF Lain dalam Python
Abstract: Pelajari cara menambahkan halaman dari satu dokumen PDF ke dokumen lain menggunakan Aspose.PDF for Python. Contoh ini menunjukkan cara menggunakan kelas PdfFileEditor untuk menggabungkan halaman dari beberapa PDF dan membuat satu dokumen keluaran.
---

Menggabungkan halaman dari berbagai dokumen PDF adalah kebutuhan umum dalam alur kerja pemrosesan dokumen. Dengan menggunakan Aspose.PDF for Python, pengembang dapat dengan mudah menambahkan halaman dari satu atau lebih file PDF ke dokumen yang sudah ada.

Potongan kode ini menunjukkan cara menggunakan metode append dari [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) kelas untuk menambahkan halaman terpilih dari file PDF lain ke akhir PDF sumber. Dengan menentukan rentang halaman, pengembang dapat mengontrol secara tepat halaman mana yang termasuk dalam dokumen akhir.

1. Buat Objek PdfFileEditor.
1. Tambahkan Halaman dari PDF Lain.

Halaman yang ditentukan dari dokumen PDF sekunder ditambahkan ke akhir PDF asli, menghasilkan file output gabungan.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


# Append Pages to PDF
def append_pages_to_pdf(infile, sample_file, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    # Append pages from the specified PDF document to the end of the source PDF document
    pdf_editor.append(infile, [sample_file], 1, 2, outfile)
```
