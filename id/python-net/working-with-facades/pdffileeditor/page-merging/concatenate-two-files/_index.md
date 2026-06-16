---
title: Gabungkan Dua File PDF
linktitle: Gabungkan Dua File PDF
type: docs
weight: 60
url: /id/python-net/concatenate-two-files/
description: Gabungkan dua file PDF menjadi satu dokumen menggunakan Aspose.PDF for Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gabungkan Dua File PDF menjadi Satu PDF dalam Python
Abstract: Pelajari cara menggabungkan dua file PDF menjadi satu dokumen menggunakan Aspose.PDF for Python. Contoh ini memperlihatkan cara menggabungkan dua PDF secara mulus sambil mempertahankan konten dan format aslinya.
---

Menggabungkan dua file PDF adalah tugas umum saat mengkonsolidasikan laporan, kontrak, atau formulir. Dengan menggunakan Aspose.PDF for Python, Anda dapat secara programatis menggabungkan dua PDF menjadi satu dokumen menggunakan metode concatenate dari [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) kelas. Ini memastikan semua halaman dari kedua file termasuk dalam PDF output sambil mempertahankan tata letak, konten, dan struktur asli.

1. Buat objek PdfFileEditor.
1. Gabungkan Dua File PDF.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def concatenate_two_files(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.concatenate(files_to_merge[0], files_to_merge[1], output_file)
```
