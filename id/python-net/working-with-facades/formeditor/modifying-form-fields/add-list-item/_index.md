---
title: Tambahkan Item Daftar
linktitle: Tambahkan Item Daftar
type: docs
weight: 10
url: /id/python-net/add-list-item/
description: Contoh ini menunjukkan cara menambahkan item ke bidang kotak daftar dalam dokumen PDF menggunakan Aspose.PDF for Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tambahkan Item ke Bidang Kotak Daftar PDF Menggunakan Python
Abstract: Artikel ini menunjukkan cara membuka dokumen PDF, menambahkan item ke bidang kotak daftar bernama "Country", dan menyimpan dokumen yang diperbarui.
---

Bidang kotak daftar dalam PDF memungkinkan pengguna memilih satu atau beberapa opsi dari sekumpulan yang telah ditentukan. Menggunakan Aspose.PDF for Python, pengembang dapat secara program menambahkan item baru ke bidang ini. The [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) kelas menyediakan metode ‘add_list_item’ untuk menambahkan item ke bidang kotak daftar yang sudah ada.

1. Buka formulir PDF yang ada.
1. Buat objek FormEditor.
1. Hubungkan PDF ke FormEditor.
1. Tambahkan item ke bidang kotak daftar "Country".
1. Simpan dokumen yang diperbarui.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_list_item(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Add list item to list box field
    form_editor.add_list_item("Country", ["New Zealand", "New Zealand"])
    # Save updated document
    form_editor.save(outfile)
```
