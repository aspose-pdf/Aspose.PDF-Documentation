---
title: Buat Bidang ComboBox
linktitle: Buat Bidang ComboBox
type: docs
weight: 20
url: /id/python-net/create-combobox-field/
description: Periksa cara menambahkan bidang ComboBox (daftar drop-down) secara programatis ke dokumen PDF menggunakan Aspose.PDF for Python. Contoh ini menunjukkan cara menyisipkan bidang formulir ComboBox, menambahkan item yang dapat dipilih, dan menyimpan file PDF yang diperbarui.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Buat Bidang ComboBox dalam PDF Menggunakan Aspose.PDF for Python
Abstract: Bidang formulir interaktif membuat PDF lebih dinamis dan mudah digunakan. Bidang ComboBox memungkinkan pengguna memilih opsi dari daftar drop-down yang telah ditentukan sebelumnya. Dalam tutorial ini, Anda akan mempelajari cara membuat ComboBox dalam PDF menggunakan kelas FormEditor di Aspose.PDF for Python, mengisinya dengan opsi, dan menyimpan dokumen yang telah dimodifikasi.
---

Formulir PDF banyak digunakan untuk mengumpulkan informasi terstruktur dalam dokumen digital seperti aplikasi, survei, dan formulir pendaftaran. Bidang ComboBox menyediakan cara yang nyaman bagi pengguna untuk memilih dari daftar nilai yang telah ditentukan sebelumnya sambil menjaga formulir tetap ringkas dan teratur.

The [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) kelas memungkinkan Anda untuk membuat dan mengelola berbagai jenis bidang, termasuk kotak teks, kotak centang, tombol radio, dan daftar drop-down

1. Muat dokumen PDF yang ada.
1. Tambahkan bidang ComboBox dengan metode 'add_field()' dan parameter 'FieldType.COMBO_BOX'.
1. Gunakan metode 'add_list_item()' untuk menyisipkan opsi yang dapat dipilih ke dalam daftar drop-down.
1. Simpan dokumen PDF yang diperbarui.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_combobox_field(infile, outfile):
    """Create ComboBox field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add ComboBox field to PDF form
    pdf_form_editor.add_field(
        pdf_facades.FieldType.COMBO_BOX, "combobox1", "Australia", 1, 230, 498, 350, 514
    )
    pdf_form_editor.add_list_item("combobox1", ["Australia", "Australia"])
    pdf_form_editor.add_list_item("combobox1", ["New Zealand", "New Zealand"])

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```
