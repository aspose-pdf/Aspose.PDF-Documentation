---
title: Buat Field CheckBox
linktitle: Buat Field CheckBox
type: docs
weight: 10
url: /id/python-net/create-checkbox-field/
description: Pelajari cara menambahkan field form checkbox secara programatis ke dokumen PDF menggunakan Aspose.PDF for Python. Panduan ini menunjukkan cara menggunakan kelas FormEditor untuk menyisipkan checkbox interaktif ke dalam file PDF yang ada dan menyimpan dokumen yang diperbarui.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Buat Field Checkbox dalam PDF Menggunakan Aspose.PDF for Python
Abstract: Field form interaktif memungkinkan pengguna mengisi dan berinteraksi dengan dokumen PDF secara digital. Dalam tutorial ini, Anda akan mempelajari cara menambahkan field checkbox ke PDF menggunakan Aspose.PDF Python API. Contoh ini menunjukkan cara mengikat dokumen PDF yang ada, membuat field form checkbox pada koordinat yang ditentukan, dan menyimpan file yang telah dimodifikasi.
---

Formulir PDF banyak digunakan untuk mengumpulkan masukan pengguna dalam dokumen seperti aplikasi, survei, dan perjanjian. Field checkbox memungkinkan pengguna memilih atau membatalkan pilihan dalam sebuah form.

Dengan menggunakan Aspose.PDF for Python, pengembang dapat memanipulasi formulir PDF secara programatis. The [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) kelas menyediakan metode untuk menambahkan, mengedit, dan mengelola bidang formulir dalam dokumen PDF.

1. Muat file PDF yang ada.
1. Panggil metode 'add_field()' dengan parameter 'FieldType.CHECK_BOX' untuk membuat kotak centang dan menentukan posisinya.
1. Tentukan nama bidang, keterangan, dan posisi.
1. Simpan dokumen PDF yang diperbarui.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_checkbox_field(infile, outfile):
    """Create CheckBox field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add CheckBox field to PDF form
    pdf_form_editor.add_field(
        pdf_facades.FieldType.CHECK_BOX,
        "checkbox1",
        "Check Box 1",
        1,
        240,
        498,
        256,
        514,
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```
