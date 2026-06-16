---
title: Bagi PDF dari Awal
linktitle: Bagi PDF dari Awal
type: docs
weight: 10
url: /id/python-net/split-pdf-from-beginning/
description: Bagi dokumen PDF dari awal menggunakan Aspose.PDF for Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Bagi PDF dari Awal dalam Python Menggunakan Aspose.PDF
Abstract: Pelajari cara membagi dokumen PDF dari awal menggunakan Aspose.PDF for Python. Contoh ini menunjukkan cara mengekstrak sejumlah halaman tertentu mulai dari halaman pertama untuk membuat dokumen PDF baru.
---

Membagi PDF dari awal berguna ketika Anda membutuhkan beberapa halaman pertama dari sebuah dokumen sebagai file terpisah. Dengan menggunakan Aspose.PDF for Python, metode split_from_first dalam [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) kelas memungkinkan Anda mengekstrak sejumlah halaman yang ditentukan mulai dari halaman satu. Fitur ini ideal untuk membuat cuplikan, pratinjau, atau bagian lebih kecil dari PDF yang lebih besar tanpa harus mengedit file asli secara manual.

1. Buat Objek PdfFileEditor.
1. Pisahkan PDF dari Halaman Pertama.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Split PDF from Beginning
def split_pdf_from_beginning(input_pdf_path, output_pdf_path):
    pdf_file_editor = pdf_facades.PdfFileEditor()
    pdf_file_editor.split_from_first(input_pdf_path, 3, output_pdf_path)
```
