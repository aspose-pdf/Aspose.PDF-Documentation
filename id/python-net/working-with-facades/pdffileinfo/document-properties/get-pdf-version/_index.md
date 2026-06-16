---
title: Dapatkan Versi PDF
linktitle: Dapatkan Versi PDF
type: docs
weight: 20
url: /id/python-net/get-pdf-version/
description: Pelajari cara menentukan versi dokumen PDF secara programatis menggunakan Aspose.PDF for Python. Tutorial ini menunjukkan cara menggunakan kelas PdfFileInfo untuk memeriksa versi PDF dari sebuah file.
lastmod: "2026-06-12"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ambil Versi PDF Menggunakan Aspose.PDF for Python
Abstract: Dokumen PDF memiliki nomor versi yang menunjukkan fitur dan spesifikasi yang mereka dukung (mis., 1.4, 1.7, 2.0). Mengetahui versi PDF penting untuk kompatibilitas, dukungan fitur, dan alur kerja pemrosesan dokumen. Dalam panduan ini, Anda akan belajar cara mengambil versi PDF secara programatis menggunakan kelas PdfFileInfo dalam Aspose.PDF for Python.
---

Versi PDF menentukan fitur dan kemampuan yang didukung dalam sebuah dokumen, termasuk bidang formulir, enkripsi, anotasi, dan kompresi. Bagi pengembang yang bekerja dengan banyak PDF, memeriksa versi memastikan kompatibilitas dengan alat, perpustakaan, atau alur kerja yang memproses file-file ini.

Dengan menggunakan Aspose.PDF for Python, Anda dapat dengan mudah memeriksa versi PDF dengan [PdfFileInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileinfo/) class.

1. Muat dokumen PDF.
1. Ambil versi PDF-nya.
1. Tampilkan versi di konsol.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_pdf_version(input_file_name):

    pdf_metadata = pdf_facades.PdfFileInfo(input_file_name)
    version = pdf_metadata.get_pdf_version()
    print(f"\nPDF Version: {version}")
```
