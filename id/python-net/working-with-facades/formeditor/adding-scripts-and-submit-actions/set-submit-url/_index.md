---
title: Atur URL Kirim
linktitle: Atur URL Kirim
type: docs
weight: 40
url: /id/python-net/set-submit-url/
description: Contoh ini menunjukkan cara mengonfigurasi aksi kirim untuk bidang tombol dalam formulir PDF menggunakan Aspose.PDF for Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Atur URL Kirim untuk Tombol Formulir PDF Menggunakan Python
Abstract: Artikel ini menjelaskan cara membuka formulir PDF yang ada, menetapkan URL pengiriman untuk bidang tombol menggunakan kelas FormEditor, memverifikasi bahwa operasi berhasil, dan menyimpan dokumen PDF yang diperbarui.
---

Formulir PDF dapat dirancang untuk mengirim data mereka ke server web ketika pengguna mengklik tombol kirim. Menggunakan Aspose.PDF for Python, pengembang dapat secara programatik mengonfigurasi aksi kirim untuk bidang formulir.
Dengan mengatur URL kirim, formulir dapat mengirim data yang dimasukkan pengguna ke server ketika tombol diklik. Fungsionalitas ini berguna untuk alur kerja di mana formulir PDF harus mengirim informasi ke aplikasi web, basis data, atau layanan pemrosesan.

Menggunakan [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) kelas dari [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) modul, pengembang dapat secara programatis menetapkan URL submit ke bidang tombol dalam formulir PDF yang ada.

1. Buka formulir PDF yang ada.
1. Temukan bidang tombol bernama Script_Demo_Button.
1. Tetapkan URL tempat data formulir akan dikirim.
1. Verifikasi bahwa tindakan tersebut berhasil diterapkan.
1. Simpan dokumen PDF yang diperbarui.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_submit_url(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Set license
    set_license()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Set submit URL for the button
    if not form_editor.set_submit_url(
        "Script_Demo_Button", "http://www.example.com/submit"
    ):
        raise Exception("Failed to set submit URL")

    # Save output PDF file
    form_editor.save(output_file_name)
```
