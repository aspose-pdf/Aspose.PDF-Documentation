---
title: Dapatkan Penampilan Field
linktitle: Dapatkan Penampilan Field
type: docs
weight: 20
url: /id/python-net/get-field-appearance/
description: Artikel ini menjelaskan cara membuka PDF, mengakses form field, mengambil pengaturan penampilannya, dan menampilkannya. Contoh ini menunjukkan cara mengambil penampilan field bernama “Last Name”.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ambil Penampilan Form Field PDF Menggunakan Python
Abstract: Contoh ini menunjukkan cara mengambil properti penampilan visual dari sebuah form field dalam dokumen PDF menggunakan Aspose.PDF for Python. Kode membuka PDF yang ada, mengakses form field tertentu, dan mencetak detail penampilannya, termasuk warna latar belakang, warna teks, warna batas, dan perataan.
---

Form field dalam dokumen PDF memiliki properti visual seperti warna latar belakang, warna teks, warna batas, dan perataan. Dengan Aspose.PDF for Python, pengembang dapat memeriksa pengaturan penampilan ini secara programatis menggunakan [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) kelas.

1. Buka dokumen PDF yang ada.
1. Buat objek FormEditor.
1. Ambil informasi tampilan dari field tertentu.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_field_appearance(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Get field appearance
    appearance = form_editor.get_field_appearance("Last Name")
    print("Field Appearance: " + str(appearance))
```
