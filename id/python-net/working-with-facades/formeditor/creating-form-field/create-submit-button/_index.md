---
title: Buat Tombol Kirim
linktitle: Buat Tombol Kirim
type: docs
weight: 50
url: /id/python-net/create-submit-button/
description: Pelajari cara menambahkan Tombol Kirim ke dokumen PDF secara programatis menggunakan Aspose.PDF for Python. Tutorial ini menunjukkan cara membuat tombol yang mengirim data formulir ke URL yang ditentukan dan menyimpan PDF yang diperbarui.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Buat Tombol Kirim dalam PDF Menggunakan Aspose.PDF for Python
Abstract: Tombol Kirim dalam formulir PDF memungkinkan pengguna mengirim data formulir langsung ke server atau endpoint. Dalam panduan ini, Anda akan mempelajari cara menambahkan bidang Tombol Kirim ke PDF menggunakan kelas FormEditor dalam Aspose.PDF for Python. Contohnya menunjukkan cara mengatur nama tombol, label, URL target, dan posisi, lalu menyimpan dokumen PDF yang diperbarui.
---

Formulir PDF interaktif sering memerlukan pengguna mengirimkan masukan mereka untuk diproses, seperti mengirim hasil survei, formulir aplikasi, atau data umpan balik. Bidang Tombol Kirim menyediakan fungsi ini dengan menautkan tombol ke endpoint web.

The [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) kelas memungkinkan menambahkan tombol, kotak centang, tombol radio, bidang teks, dan kontrol formulir lainnya.

1. Muat dokumen PDF yang ada.
1. Tambahkan bidang Tombol Submit ke halaman tertentu.
1. Setel label tombol dan URL tujuan pengiriman.
1. Simpan PDF yang telah diperbarui dengan tombol baru.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_submit_button(infile, outfile):
    """Create Submit Button in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add Submit Button to PDF form
    pdf_form_editor.add_submit_btn(
        "submitbtn1",
        1,
        "Submit Button",
        "http://example.com/submit",
        100,
        450,
        200,
        470,
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```
