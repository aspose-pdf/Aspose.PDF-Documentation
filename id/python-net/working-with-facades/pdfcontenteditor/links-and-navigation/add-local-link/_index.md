---
title: Tambahkan Tautan Lokal
linktitle: Tambahkan Tautan Lokal
type: docs
weight: 40
url: /id/python-net/add-local-link/
description: Contoh ini mengikat PDF masukan, menambahkan tautan lokal berwarna merah pada halaman 1 yang mengarah ke halaman 1, dan menyimpan dokumen yang telah dimodifikasi.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tambahkan Tautan Lokal ke PDF Menggunakan PdfContentEditor dalam Python
Abstract: Contoh ini menunjukkan cara menambahkan tautan lokal ke dokumen PDF menggunakan Aspose.PDF for Python via the Facades API. Ini memperlihatkan cara membuat area yang dapat diklik yang menavigasi ke halaman lain dalam PDF yang sama dan menyimpan dokumen yang diperbarui.
---

Tautan lokal dalam PDF memungkinkan navigasi cepat antar halaman dalam dokumen yang sama. Menggunakan [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), Anda dapat mendefinisikan persegi panjang yang dapat diklik yang menghubungkan satu halaman ke halaman lain, meningkatkan kegunaan dan navigasi dokumen.

1. Buat sebuah instance PdfContentEditor.
1. Hubungkan dokumen PDF input.
1. Tentukan sebuah persegi panjang untuk tautan lokal yang dapat diklik.
1. Tentukan halaman sumber dan halaman tujuan.
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


def add_local_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add a local link on page 1 to destination page 1
    content_editor.create_local_link(
        apd.Rectangle(120, 620, 220, 20),
        1,
        1,
        apd.Color.red,
    )
    # Save updated document
    content_editor.save(outfile)
```
