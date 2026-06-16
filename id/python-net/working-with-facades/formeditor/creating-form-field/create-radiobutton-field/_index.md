---
title: Buat Bidang RadioButton
linktitle: Buat Bidang RadioButton
type: docs
weight: 40
url: /id/python-net/create-radiobutton-field/
description: Pelajari cara menambahkan bidang formulir radio button secara programatis ke dokumen PDF menggunakan Aspose.PDF for Python. Contoh ini menunjukkan cara membuat grup radio button, mendefinisikan opsi yang dapat dipilih, dan menyimpan file PDF yang diperbarui.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Buat Bidang Radio Button dalam PDF Menggunakan Aspose.PDF for Python
Abstract: Radio button biasanya digunakan dalam formulir PDF untuk memungkinkan pengguna memilih satu opsi dari grup pilihan yang telah ditentukan sebelumnya. Dalam tutorial ini, Anda akan belajar cara membuat bidang radio button dalam PDF menggunakan kelas FormEditor di Aspose.PDF for Python. Contoh ini menunjukkan cara mendefinisikan item radio button, mengatur pemilihan default, dan menyimpan dokumen yang diperbarui.
---

Formulir PDF interaktif memungkinkan pengguna memberikan input terstruktur langsung di dalam dokumen. Bidang radio button berguna ketika pengguna harus memilih hanya satu opsi dari beberapa pilihan, seperti memilih negara, jenis kelamin, atau preferensi.

The [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) kelas menyediakan metode untuk membuat berbagai tipe bidang, termasuk kotak teks, kotak centang, kotak kombo, kotak daftar, dan radio button.

1. Muat dokumen PDF yang ada.
1. Definisikan daftar opsi tombol radio.
1. Tambahkan bidang tombol radio ke halaman tertentu.
1. Tetapkan nilai default yang dipilih.
1. Simpan dokumen PDF yang dimodifikasi.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_radiobutton_field(infile, outfile):
    """Create RadioButton field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add RadioButton field to PDF form
    pdf_form_editor.items = ["Australia", "New Zealand", "Malaysia"]
    pdf_form_editor.add_field(
        pdf_facades.FieldType.RADIO, "radiobutton1", "Malaysia", 1, 240, 498, 256, 514
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```
