---
title: Tambahkan Tautan Web
linktitle: Tambahkan Tautan Web
type: docs
weight: 60
url: /id/python-net/add-web-link/
description: Contoh ini mengikat PDF masukan, menambahkan anotasi tautan web biru pada halaman 1 yang mengarah ke halaman produk PDF Python Aspose, dan menyimpan dokumen yang telah dimodifikasi.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tambahkan Tautan Web ke PDF Menggunakan PdfContentEditor di Python
Abstract: Contoh ini menunjukkan cara menambahkan tautan web ke dokumen PDF menggunakan Aspose.PDF for Python via the Facades API. Ini menunjukkan cara membuat area yang dapat diklik pada halaman yang membuka URL tertentu di peramban web dan menyimpan dokumen yang diperbarui.
---

Tautan web dalam PDF memungkinkan pengguna untuk menavigasi langsung ke sumber daya online, situs web, atau dokumentasi. Using [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), Anda dapat menentukan area persegi panjang pada halaman PDF yang, ketika diklik, membuka URL di peramban web default.

1. Buat sebuah instance PdfContentEditor.
1. Hubungkan dokumen PDF input.
1. Tentukan persegi panjang untuk tautan web yang dapat diklik.
1. Spesifikasikan URL, nomor halaman, dan warna tautan.
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


def add_web_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add a web link annotation to page 1
    content_editor.create_web_link(
        apd.Rectangle(100, 650, 200, 20),
        "https://products.aspose.com/pdf/python-net/",
        1,
        apd.Color.blue,
    )
    # Save updated document
    content_editor.save(outfile)
```
