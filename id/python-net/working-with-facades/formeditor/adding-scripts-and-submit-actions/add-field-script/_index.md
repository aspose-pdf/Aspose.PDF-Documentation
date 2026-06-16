---
title: Tambahkan Skrip Bidang
linktitle: Tambahkan Skrip Bidang
type: docs
weight: 10
url: /id/python-net/add-field-script/
description: Formulir PDF interaktif dapat menyertakan JavaScript untuk mengotomatiskan tindakan ketika pengguna berinteraksi dengan bidang formulir. Dengan menggunakan Aspose.PDF for Python, pengembang dapat dengan mudah melampirkan skrip ke elemen formulir seperti tombol atau bidang teks.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tambahkan Tindakan JavaScript ke Bidang Formulir PDF Menggunakan Python
Abstract: Artikel ini menjelaskan cara membuka formulir PDF, menetapkan kode JavaScript ke bidang formulir tertentu, menambahkan tindakan skrip tambahan, dan menyimpan dokumen yang diperbarui. Contohnya menggunakan kelas FormEditor dari API Aspose.PDF Facades untuk memanipulasi perilaku formulir secara programatis.
---

## Tambahkan Tindakan JavaScript ke Bidang Formulir PDF Menggunakan Python

Potongan kode ini memungkinkan Anda menambahkan tindakan JavaScript ke bidang formulir PDF yang ada menggunakan perpustakaan Aspose.PDF for Python. Itu membuka dokumen PDF, menetapkan tindakan JavaScript ke sebuah bidang formulir, dan menambahkan skrip yang dijalankan ketika bidang tersebut dipicu. Akhirnya, PDF yang diperbarui disimpan sebagai file baru.
Menggunakan [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) kelas dari [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) modul, Anda dapat secara programatik melampirkan JavaScript ke bidang formulir yang ada:

1. Buka formulir PDF yang ada.
1. Tetapkan aksi JavaScript untuk bidang tertentu.
1. Tambahkan aksi JavaScript lain ke bidang yang sama.
1. Simpan dokumen PDF yang dimodifikasi.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_field_script(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Set JavaScript action for the field
    form_editor.set_field_script(
        "Script_Demo_Button", "app.alert('Script 1 has been executed');"
    )

    # Add JavaScript action to the field
    form_editor.add_field_script(
        "Script_Demo_Button", "app.alert('Script 2 has been executed');"
    )

    # Save output PDF file
    form_editor.save(output_file_name)
```
