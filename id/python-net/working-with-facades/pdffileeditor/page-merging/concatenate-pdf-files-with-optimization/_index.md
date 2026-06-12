---
title: Konkatenasi File PDF dengan Optimasi
linktitle: Konkatenasi File PDF dengan Optimasi
type: docs
weight: 30
url: /id/python-net/concatenate-pdf-files-with-optimization/
description: Konkatenasi beberapa file PDF menjadi satu PDF yang dioptimalkan menggunakan Aspose.PDF for Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gabungkan File PDF dengan Output yang Dioptimalkan di Python
Abstract: Pelajari cara menggabungkan beberapa file PDF menjadi satu PDF yang dioptimalkan menggunakan Aspose.PDF for Python. Contoh ini menunjukkan cara mengaktifkan optimasi ukuran untuk mengurangi ukuran file output sambil mempertahankan konten dan format.
---

Saat menggabungkan beberapa PDF, file yang dihasilkan dapat menjadi besar, terutama jika berisi gambar atau konten kompleks. Menggunakan Aspose.PDF for Python, pengembang dapat mengaktifkan optimasi selama konkatenasi untuk mengurangi ukuran file tanpa kehilangan kualitas. Properti optimize_size dalam [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) kelas memastikan bahwa PDF yang digabungkan menjadi ringkas dan efisien, menjadikannya cocok untuk berbagi, penyimpanan, atau pengarsipan.

1. Buat objek PdfFileEditor dan Aktifkan Optimisasi.
1. Gabungkan file PDF.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def concatenate_pdf_files_with_optimization(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.optimize_size = True  # Enable optimization for smaller output file size
    pdf_editor.concatenate(files_to_merge, output_file)
```
