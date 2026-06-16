---
title: Atur Batas Field
linktitle: Atur Batas Field
type: docs
weight: 80
url: /id/python-net/set-field-limit/
description: Contoh ini menunjukkan cara mengatur batas karakter maksimum untuk bidang formulir dalam dokumen PDF menggunakan Aspose.PDF for Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Atur Batas Karakter Maksimum untuk Bidang Formulir PDF Menggunakan Python
Abstract: Contoh ini menunjukkan cara mengatur batas karakter untuk bidang yang bernama "Last Name" menjadi 10 karakter, memastikan bahwa pengguna tidak dapat memasukkan lebih dari batas yang ditentukan.
---

Bidang formulir dalam dokumen PDF mungkin memerlukan pembatasan input untuk menjaga format yang tepat. Dengan menggunakan Aspose.PDF for Python, pengembang dapat secara programatis mengatur jumlah maksimum karakter untuk sebuah bidang.

The [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) kelas menyediakan metode ‘set_field_limit’ untuk mendefinisikan panjang input maksimum untuk sebuah bidang.

1. Buka formulir PDF yang ada.
1. Buat objek FormEditor.
1. Atur batas karakter maksimum untuk bidang "Last Name".
1. Simpan PDF yang diperbarui.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_field_limit(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Set field limit to 10
    if not form_editor.set_field_limit("Last Name", 10):
        raise Exception(
            "Failed to set field limit. Field may not support specified limit."
        )

    # Save updated document
    form_editor.save(outfile)
```
