---
title: Gabungkan Beberapa File PDF
linktitle: Gabungkan Beberapa File PDF
type: docs
weight: 20
url: /id/python-net/concatenate-pdf-files/
description: Gabungkan beberapa file PDF menjadi satu dokumen menggunakan Aspose.PDF for Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gabungkan Beberapa File PDF menjadi Satu PDF dalam Python
Abstract: Pelajari cara menggabungkan beberapa file PDF menjadi satu dokumen menggunakan Aspose.PDF for Python. Contoh ini menunjukkan cara menggunakan metode concatenate untuk menggabungkan beberapa PDF secara mulus sambil mempertahankan konten dan formatnya.
---

Penggabungan file PDF adalah tugas umum dalam manajemen dokumen, pelaporan, dan alur kerja otomatis. Dengan menggunakan Aspose.PDF for Python, pengembang dapat dengan mudah menggabungkan beberapa file PDF menjadi satu dokumen terintegrasi. Metode concatenate dari [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) kelas memastikan bahwa semua halaman dari file input dipertahankan dalam output akhir, menjaga tata letak dan kontennya yang asli. Pendekatan ini berguna untuk membuat laporan komprehensif, menggabungkan formulir, atau mengarsipkan banyak dokumen secara efisien.

1. Buat Objek PdfFileEditor.
1. Gabungkan Banyak File PDF.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def concatenate_pdf_files(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.concatenate(files_to_merge, output_file)
```
