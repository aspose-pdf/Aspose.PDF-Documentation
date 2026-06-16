---
title: Ganti Nama Field
linktitle: Ganti Nama Field
type: docs
weight: 70
url: /id/python-net/rename-field/
description: Ganti nama field formulir yang ada dalam dokumen PDF menggunakan Aspose.PDF for Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ganti Nama Field Form PDF Menggunakan Python
Abstract: Contoh ini menunjukkan cara mengganti nama field formulir yang ada dalam dokumen PDF menggunakan Aspose.PDF for Python. Kode ini membuka PDF input, mengubah nama field formulir yang ditentukan menggunakan kelas FormEditor, dan menyimpan dokumen yang telah diperbarui.
---

Formulir PDF sering bergantung pada nama field untuk scripting, otomatisasi, dan pemrosesan data. Dengan menggunakan Aspose.PDF for Python, pengembang dapat mengganti nama field yang ada tanpa harus membuat ulang atau mengubah tata letak formulir.

The [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) kelas menyediakan metode ’rename_field’, yang memungkinkan pengembang mengubah nama field yang ada sekaligus mempertahankan posisi, nilai, dan tampilannya.

1. Muat formulir PDF yang ada.
1. Buat instance FormEditor.
1. Hubungkan dokumen PDF ke editor.
1. Ganti nama bidang target.
1. Simpan PDF yang diperbarui.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def rename_field(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Rename field in document
    form_editor.rename_field("City", "Town")
    # Save updated document
    form_editor.save(outfile)
```

