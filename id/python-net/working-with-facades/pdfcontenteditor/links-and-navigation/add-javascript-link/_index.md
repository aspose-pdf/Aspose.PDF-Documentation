---
title: Tambahkan Tautan JavaScript
linktitle: Tambahkan Tautan JavaScript
type: docs
weight: 30
url: /id/python-net/add-javascript-link/
description: Contoh ini mengikat PDF input, menambahkan tautan JavaScript yang memicu peringatan saat diklik, dan menyimpan dokumen yang telah dimodifikasi.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tambahkan Tautan JavaScript ke PDF Menggunakan PdfContentEditor dalam Python
Abstract: Contoh ini menunjukkan cara menambahkan tautan JavaScript ke dokumen PDF menggunakan Aspose.PDF for Python via the Facades API. Ini memperlihatkan cara membuat area yang dapat diklik yang mengeksekusi kode JavaScript saat diklik, dan menyimpan PDF yang diperbarui.
---

Tautan JavaScript dalam PDF memungkinkan fungsi interaktif seperti menampilkan peringatan, melakukan perhitungan, atau memodifikasi konten dokumen secara dinamis. Menggunakan [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), Anda dapat mendefinisikan persegi panjang yang dapat diklik pada halaman dan mengaitkannya dengan kode JavaScript khusus.

1. Buat instance PdfContentEditor.
1. Hubungkan dokumen PDF masukan.
1. Tentukan persegi panjang untuk tautan JavaScript yang dapat diklik.
1. Spesifikasikan nomor halaman dan warna tautan.
1. Tetapkan kode JavaScript untuk dijalankan saat diklik.
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


def add_javascript_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add JavaScript link action
    content_editor.create_java_script_link(
        "app.alert('PdfContentEditor JavaScript link');",
        apd.Rectangle(160, 560, 260, 20),
        1,
        apd.Color.orange,
    )
    # Save updated document
    content_editor.save(outfile)
```
