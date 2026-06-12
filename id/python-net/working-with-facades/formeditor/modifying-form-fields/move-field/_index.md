---
title: Pindahkan Field
linktitle: Pindahkan Field
type: docs
weight: 50
url: /id/python-net/move-field/
description: Pindahkan bidang formulir yang ada ke posisi berbeda dalam dokumen PDF.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Pindahkan Form Field PDF ke Posisi Baru Menggunakan Python
Abstract: Contoh ini menunjukkan cara memindahkan bidang formulir yang ada ke posisi berbeda dalam dokumen PDF menggunakan Aspose.PDF for Python. Kode membuka PDF yang ada, memindahkan bidang formulir yang ditentukan ke koordinat baru, dan menyimpan dokumen yang diperbarui.
---

Formulir PDF sering memerlukan penyesuaian tata letak setelah dibuat. Dengan menggunakan Aspose.PDF for Python, pengembang dapat memindahkan bidang formulir yang ada ke posisi baru tanpa harus membuat ulang.

Contoh ini menunjukkan cara memposisikan kembali bidang \"Country\" dengan menentukan koordinat baru untuk penempatannya dalam halaman. The [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) kelas menyediakan metode move_field untuk memindahkan field dalam halaman PDF.

1. Buka formulir PDF yang ada.
1. Buat objek FormEditor.
1. Ikat dokumen PDF ke FormEditor.
1. Pindahkan field 'Country' ke posisi baru menggunakan koordinat.
1. Simpan dokumen yang dimodifikasi.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def move_field(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Move field to new page
    form_editor.move_field("Country", 200, 600, 280, 620)
    # Save updated document
    form_editor.save(outfile)
```
