---
title: Buat Field TextBox
linktitle: Buat Field TextBox
type: docs
weight: 60
url: /id/python-net/create-textbox-field/
description: Pelajari cara menambahkan field TextBox secara programatis ke dokumen PDF menggunakan Aspose.PDF for Python. Tutorial ini menunjukkan cara menyisipkan beberapa field teks, mengatur nilai default, dan menyimpan dokumen PDF yang diperbarui.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Buat Field TextBox dalam PDF Menggunakan Aspose.PDF for Python
Abstract: Field TextBox dalam formulir PDF memungkinkan pengguna memasukkan dan mengedit teks, menjadikan dokumen interaktif dan ramah pengguna. Dalam tutorial ini, Anda akan belajar cara membuat field formulir TextBox dalam PDF menggunakan kelas FormEditor di Aspose.PDF for Python. Contoh ini menunjukkan penambahan beberapa field, menentukan nilai default, dan menyimpan PDF yang dimodifikasi.
---

Formulir PDF sering memerlukan masukan teks dari pengguna, seperti nama, alamat, atau komentar. Field TextBox memungkinkan fungsi ini dengan menyediakan field yang dapat diedit langsung dalam dokumen PDF.

The [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) kelas memungkinkan penambahan field teks, kotak centang, tombol radio, kotak daftar, kotak kombo, dan tombol, memudahkan pembuatan PDF interaktif.

1. Muat dokumen PDF yang ada.
1. Tambahkan beberapa bidang TextBox untuk input pengguna.
1. Tetapkan nilai default untuk setiap bidang.
1. Simpan dokumen PDF yang diperbarui.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_textbox_field(infile, outfile):
    """Create TextBox field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add TextBox field to PDF form
    pdf_form_editor.add_field(
        pdf_facades.FieldType.TEXT, "first_name", "Alexander", 1, 50, 570, 150, 590
    )
    pdf_form_editor.add_field(
        pdf_facades.FieldType.TEXT, "last_name", "Smith", 1, 235, 570, 330, 590
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```
