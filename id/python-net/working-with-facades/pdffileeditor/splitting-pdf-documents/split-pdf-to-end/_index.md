---
title: Pisahkan PDF ke Akhir
linktitle: Pisahkan PDF ke Akhir
type: docs
weight: 40
url: /id/python-net/split-pdf-to-end/
description: Pisahkan dokumen PDF dari halaman tertentu hingga halaman terakhir menggunakan Aspose.PDF for Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Pisahkan PDF dari Halaman Tertentu ke Akhir dalam Python
Abstract: Pelajari cara memisahkan dokumen PDF dari halaman tertentu hingga halaman terakhir menggunakan Aspose.PDF for Python. Contoh ini menunjukkan cara mengekstrak semua halaman mulai dari halaman yang ditentukan untuk membuat file PDF baru.
---

Memisahkan PDF dari halaman tertentu hingga akhir berguna ketika Anda memerlukan bagian akhir dokumen sebagai file terpisah. Dengan menggunakan Aspose.PDF for Python, metode split_to_end dari [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) kelas memungkinkan Anda mengekstrak halaman mulai dari nomor halaman apapun hingga halaman terakhir dokumen. Ini ideal untuk membuat kutipan, mengekstrak bab, atau memproses bagian dari PDF besar tanpa harus mengeditnya secara manual.

1. Buat objek PdfFileEditor.
1. Pisahkan PDF dari Halaman Tertentu ke Akhir.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Split PDF to End
def split_pdf_to_end(input_pdf_path, output_pdf_path):
    pdf_file_editor = pdf_facades.PdfFileEditor()
    pdf_file_editor.split_to_end(input_pdf_path, 2, output_pdf_path)
```
