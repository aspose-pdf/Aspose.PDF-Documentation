---
title: Coba Menggabungkan Dua File PDF
linktitle: Coba Menggabungkan Dua File PDF
type: docs
weight: 90
url: /id/python-net/try-concatenate-two-files/
description: Gabungkan dua file PDF menggunakan Aspose.PDF for Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aman Menggabungkan Dua File PDF di Python Tanpa Pengecualian
Abstract: Pelajari cara menggabungkan dua file PDF secara aman menggunakan Aspose.PDF for Python. Metode try_concatenate menggabungkan file-file tersebut tanpa menimbulkan pengecualian, memungkinkan penanganan kesalahan yang elegan jika operasi gagal.
---

Menggabungkan dua file PDF terkadang dapat gagal karena file yang korup, format yang tidak kompatibel, atau masalah lainnya. Dengan menggunakan Aspose.PDF for Python, metode try_concatenate dari kelas PdfFileEditor memungkinkan Anda mencoba menggabungkan dua PDF dengan aman. Jika operasi gagal, metode ini mengembalikan False alih-alih menimbulkan pengecualian, memberi Anda kendali penuh atas penanganan kesalahan dalam alur kerja otomatis atau pemrosesan batch.

1. Buat Objek PdfFileEditor.
1. Coba Menggabungkan Dua File PDF.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def try_concatenate_two_files(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    if not pdf_editor.try_concatenate(
        files_to_merge[0], files_to_merge[1], output_file
    ):
        print("Concatenation failed for the provided files.")
```
