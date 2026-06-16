---
title: Set Skrip Bidang
linktitle: Set Skrip Bidang
type: docs
weight: 30
url: /id/python-net/set-field-script/
description: Cuplikan kode ini menunjukkan cara menetapkan aksi JavaScript ke bidang formulir dalam dokumen PDF menggunakan Aspose.PDF for Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Atur Aksi JavaScript untuk Bidang Formulir PDF Menggunakan Python
Abstract: Artikel ini menjelaskan cara membuka dokumen PDF, menetapkan kode JavaScript ke bidang formulir, memperbarui skrip menggunakan kelas FormEditor, dan menyimpan file yang dimodifikasi. Contohnya menunjukkan bagaimana skrip yang ada dapat digantikan untuk mengubah perilaku bidang formulir.
---

Formulir PDF interaktif sering bergantung pada JavaScript untuk melakukan tugas seperti menampilkan peringatan, memvalidasi input, atau memicu perilaku formulir yang dinamis. Dengan Aspose.PDF for Python, pengembang dapat mengelola skrip ini secara programatik.

Contoh tersebut pertama menambahkan aksi JavaScript ke bidang dan kemudian menggantinya dengan skrip lain menggunakan metode 'set_field_script'. Pendekatan ini memungkinkan pengembang untuk mengontrol atau memperbarui perilaku interaktif elemen formulir PDF seperti tombol atau bidang input.

Field formulir yang digunakan dalam contoh ini dinamakan 'Script_Demo_Button', yang biasanya mewakili tombol yang mengeksekusi skrip yang ditetapkan saat dipicu.

Menggunakan [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) kelas dari [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) module, pengembang dapat mengelola aksi JavaScript yang terkait dengan field formulir secara programatis:

1. Buka dokumen formulir PDF yang sudah ada.
1. Tambahkan aksi JavaScript ke sebuah field formulir.
1. Atur (ganti) aksi JavaScript dengan skrip baru.
1. Simpan dokumen PDF yang dimodifikasi.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_field_script(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Add JavaScript action to the field
    form_editor.add_field_script(
        "Script_Demo_Button", "app.alert('Script 1 has been executed');"
    )

    # Set JavaScript action for the field
    form_editor.set_field_script(
        "Script_Demo_Button", "app.alert('Script 2 has been executed');"
    )

    # Save output PDF file
    form_editor.save(output_file_name)
```
