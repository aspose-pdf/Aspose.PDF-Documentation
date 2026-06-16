---
title: Hapus Bidang
linktitle: Hapus Bidang
type: docs
weight: 60
url: /id/python-net/remove-field/
description: Contoh ini menunjukkan cara menghapus bidang 'Country' dari formulir PDF menggunakan metode 'remove_field' dari kelas 'FormEditor'.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Hapus Bidang Formulir dari Dokumen PDF Menggunakan Python
Abstract: Contoh ini menunjukkan cara menghapus bidang formulir yang ada dari dokumen PDF menggunakan Aspose.PDF for Python. Kode memuat file PDF, menghapus bidang yang ditentukan menggunakan kelas FormEditor, dan menyimpan dokumen yang diperbarui.
---

Formulir PDF mungkin berisi bidang yang tidak lagi diperlukan akibat perubahan desain atau pembaruan alur kerja. Dengan Aspose.PDF for Python, pengembang dapat dengan mudah menghapus bidang formulir tertentu secara programatik.

The [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) kelas dalam Aspose.PDF menyediakan metode 'remove_field', yang memungkinkan pengembang menghapus bidang formulir berdasarkan namanya.

1. Muat dokumen PDF.
1. Buat objek FormEditor.
1. Ikat PDF ke FormEditor.
1. Hapus field formulir yang ditentukan.
1. Simpan dokumen yang diperbarui.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def remove_field(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Remove field from document
    form_editor.remove_field("Country")
    # Save updated document
    form_editor.save(outfile)
```
