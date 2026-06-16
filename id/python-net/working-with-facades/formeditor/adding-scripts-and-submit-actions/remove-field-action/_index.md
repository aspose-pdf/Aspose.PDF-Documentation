---
title: Hapus Aksi Bidang
linktitle: Hapus Aksi Bidang
type: docs
weight: 20
url: /id/python-net/remove-field-action/
description: Menghapus JavaScript dari bidang formulir dapat berguna saat memodifikasi formulir PDF interaktif, menonaktifkan aksi yang sebelumnya ditetapkan, atau membersihkan dokumen yang berisi skrip yang tidak diperlukan.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Hapus Aksi JavaScript dari Bidang Formulir PDF Menggunakan Python
Abstract: Dengan menggunakan Aspose.PDF for Python, pengembang dapat secara programatis menghapus aksi JavaScript yang terlampir pada bidang formulir. Artikel ini menjelaskan cara membuka formulir PDF yang ada, menghapus skrip yang terkait dengan bidang tertentu menggunakan kelas FormEditor, memverifikasi operasi, dan menyimpan dokumen yang telah dimodifikasi.
---

Formulir PDF sering berisi aksi JavaScript yang dijalankan ketika pengguna berinteraksi dengan elemen formulir seperti tombol atau bidang input. Dalam beberapa kasus, skrip ini harus dihapus untuk menyederhanakan perilaku formulir, meningkatkan keamanan, atau memperbarui logika formulir. Hapus aksi JavaScript dari bidang formulir dalam dokumen PDF menggunakan Aspose.PDF for Python. Kode membuka formulir PDF yang ada, menemukan bidang tertentu, menghapus aksi JavaScript yang terkait, dan menyimpan dokumen yang diperbarui sebagai file PDF baru.

Menggunakan [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) kelas dari [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/), Anda dapat menghapus aksi JavaScript dari bidang tertentu dalam formulir PDF yang ada:

1. Buka formulir PDF yang ada.
1. Temukan field form bernama ‘Script_Demo_Button’.
1. Hapus aksi JavaScript yang terkait dengan field tersebut.
1. Periksa apakah penghapusan berhasil.
1. Simpan dokumen PDF yang diperbarui.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def remove_field_script(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Remove JavaScript action from the field
    if not form_editor.remove_field_action("Script_Demo_Button"):
        raise Exception("Failed to remove field script")

    # Save output PDF file
    form_editor.save(output_file_name)
```
