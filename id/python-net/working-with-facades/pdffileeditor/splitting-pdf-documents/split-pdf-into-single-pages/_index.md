---
title: Pisahkan PDF menjadi Halaman Tunggal
linktitle: Pisahkan PDF menjadi Halaman Tunggal
type: docs
weight: 30
url: /id/python-net/split-pdf-into-single-pages/
description: Pisahkan dokumen PDF menjadi PDF satu halaman menggunakan Aspose.PDF for Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Pisahkan PDF menjadi Halaman Individu dalam Python
Abstract: Pelajari cara membagi dokumen PDF menjadi PDF satu halaman menggunakan Aspose.PDF for Python. Metode ini mengekstrak setiap halaman dari PDF asli dan menyimpannya sebagai file terpisah untuk manajemen dan pemrosesan dokumen yang fleksibel.
---

Membagi PDF menjadi halaman tunggal berguna untuk pemrosesan tingkat halaman, pencetakan, atau mendistribusikan bagian-bagian dokumen secara individual. Menggunakan Aspose.PDF for Python, metode \u0027split_to_pages\u0027 dari [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) kelas membuat file PDF terpisah untuk setiap halaman dalam dokumen sumber. Pendekatan ini memungkinkan ekstraksi halaman secara otomatis untuk pengarsipan, peninjauan, atau berbagi individual sambil mempertahankan tata letak dan konten asli.

1. Buat Objek PdfFileEditor.
1. Pisahkan PDF menjadi Halaman Individu.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Split PDF into Single Pages
def split_pdf_into_single_pages(input_pdf_path, output_pdf_path):
    pdf_file_editor = pdf_facades.PdfFileEditor()
    pdf_file_editor.split_to_pages(input_pdf_path, output_pdf_path)
```
