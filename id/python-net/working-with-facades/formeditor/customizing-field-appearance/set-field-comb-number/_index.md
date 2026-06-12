---
title: Atur Nomor Comb Field
linktitle: Atur Nomor Comb Field
type: docs
weight: 70
url: /id/python-net/set-field-comb-number/
description: Contoh ini menunjukkan cara mengatur nomor comb untuk field formulir PDF menggunakan Aspose.PDF for Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Atur Nomor Comb untuk Field Formulir PDF Menggunakan Python
Abstract: Dengan menggunakan Aspose.PDF for Python, pengembang dapat secara programatis mengatur jumlah kotak (nomor comb) untuk sebuah field formulir guna menegakkan input dengan panjang tetap. Artikel ini menunjukkan cara mengatur nomor comb untuk field bernama "PIN".
---

Nomor comb menentukan bagaimana konten field dibagi menjadi kotak-kotak yang berjarak sama, yang sering digunakan untuk kode PIN, nomor seri, atau field input lain dengan panjang tetap. Kode tersebut membuka PDF yang ada, mengatur nomor comb untuk sebuah field, dan menyimpan dokumen yang telah dimodifikasi.

The [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) kelas menyediakan metode ‘set_field_comb_number’ untuk menentukan jumlah kotak (karakter) dalam sebuah field formulir.

1. Buka formulir PDF yang ada.
1. Membuat objek FormEditor.
1. Setel nilai comb field bernama "PIN" menjadi 5.
1. Simpan dokumen yang diperbarui.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_field_comb_number(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Set field comb number to 5
    form_editor.set_field_comb_number("PIN", 5)

    # Save updated document
    form_editor.save(outfile)
```
