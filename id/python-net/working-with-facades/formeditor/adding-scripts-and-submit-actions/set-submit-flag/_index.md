---
title: Atur Submit Flag
linktitle: Atur Submit Flag
type: docs
weight: 50
url: /id/python-net/set-submit-flag/
description: Pelajari cara secara programatis mengatur submit flag untuk tombol formulir PDF menggunakan Aspose.PDF for Python. Ini memungkinkan tombol tersebut mengirim data formulir dalam format khusus, seperti XFDF, ketika diklik oleh pengguna.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Atur Submit Flag untuk Tombol Formulir PDF Menggunakan Aspose.PDF for Python
Abstract: Formulir PDF dapat dikonfigurasi untuk mengirim data formulir ke server atau endpoint dalam berbagai format. Dengan mengatur submit flag pada bidang tombol, pengembang dapat menentukan cara data dikirim. Tutorial ini menunjukkan cara menggunakan kelas FormEditor untuk mengatur submit flag pada tombol submit yang sudah ada dalam dokumen PDF dan menyimpan file yang diperbarui.
---

Formulir PDF sering menyertakan Tombol Submit untuk mengirim masukan pengguna ke server. Submit flag menentukan format data yang dikirim (mis., XFDF, FDF, HTML).

1. Ikat dokumen PDF.
1. Akses tombol submit yang ada.
1. Setel bendera submit untuk format yang diinginkan.
1. Simpan dokumen PDF yang diperbarui.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_submit_flag(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Set submit flag for the form
    form_editor.set_submit_flag("Script_Demo_Button", ap.facades.SubmitFormFlag.XFDF)

    # Save output PDF file
    form_editor.save(output_file_name)
```
