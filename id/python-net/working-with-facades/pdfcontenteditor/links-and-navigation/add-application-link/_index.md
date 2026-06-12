---
title: Tambahkan Tautan Aplikasi
linktitle: Tambahkan Tautan Aplikasi
type: docs
weight: 10
url: /id/python-net/add-application-link/
description: Contoh ini mengikat PDF input, menambahkan tautan peluncuran aplikasi pada halaman pertama, dan menyimpan dokumen yang telah dimodifikasi.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tambahkan Tautan Peluncuran Aplikasi ke PDF Menggunakan PdfContentEditor dalam Python
Abstract: Contoh ini memperlihatkan cara menambahkan tautan peluncuran aplikasi ke dokumen PDF menggunakan Aspose.PDF for Python via the Facades API. Ini menunjukkan cara membuat area yang dapat diklik yang membuka aplikasi tertentu saat diklik, dan menyimpan PDF yang diperbarui.
---

PDF dapat menyertakan elemen interaktif seperti tautan yang meluncurkan aplikasi eksternal. Menggunakan [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), Anda dapat mendefinisikan daerah persegi panjang pada halaman yang, ketika diklik, membuka file eksekusi tertentu.

1. Buat instance PdfContentEditor.
1. Hubungkan dokumen PDF masukan.
1. Tentukan area persegi panjang untuk tautan yang dapat diklik.
1. Tentukan jalur aplikasi untuk diluncurkan.
1. Atur warna tautan.
1. Simpan dokumen PDF yang diperbarui.

```python
import aspose.pdf.facades as pdf_facades
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as apd
import aspose.pdf as ap

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_application_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add application launch link
    content_editor.create_application_link(
        apd.Rectangle(180, 530, 260, 20),
        "notepad.exe",
        1,
        apd.Color.purple,
    )
    # Save updated document
    content_editor.save(outfile)
```
