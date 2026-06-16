---
title: Kelola Stempel Berdasarkan ID
linktitle: Kelola Stempel Berdasarkan ID
type: docs
weight: 95
url: /id/python-net/manage-stamp-by-id/
description: Cara memanipulasi anotasi stempel karet dalam PDF berdasarkan ID unik mereka menggunakan Aspose.PDF for Python
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Kelola Stempel Karet berdasarkan ID dalam PDF Menggunakan PdfContentEditor di Python
Abstract: Contoh ini menunjukkan cara memanipulasi anotasi stempel karet dalam PDF berdasarkan ID unik mereka menggunakan Aspose.PDF for Python melalui Facades API. Anda dapat menyembunyikan atau menampilkan stempel tertentu pada halaman tertentu tanpa memengaruhi stempel lain.
---

Dalam PDF dengan banyak stempel karet, mungkin berguna untuk mengendalikan stempel individual berdasarkan ID mereka. Metode 'hide_stamp_by_id()' dan 'show_stamp_by_id()' memungkinkan kontrol visibilitas selektif. Contoh ini menunjukkan cara:

- Tambahkan beberapa stempel dengan ID unik
- Sembunyikan stempel pada halaman tertentu
- Tampilkan stempel pada halaman lain

Dengan menggunakan operasi berbasis ID, Anda menghindari pelacakan stempel berdasarkan posisi halaman atau atribut lain.

1. Buat sebuah [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instansi.
1. Hubungkan dokumen PDF input.
1. Tambahkan stempel karet dengan ID tertentu.
1. Sembunyikan dan tampilkan stempel berdasarkan ID dan nomor halamannya.
1. Simpan dokumen PDF yang diperbarui.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def manage_stamp_by_id(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    content_editor.create_rubber_stamp(
        1,
        apd.Rectangle(200, 380, 180, 60),
        "Draft",
        "Draft stamp for ID-based operations",
        apd.Color.orange,
    )

    content_editor.create_rubber_stamp(
        2,
        apd.Rectangle(200, 480, 180, 60),
        "Draft",
        "Draft stamp for ID-based operations",
        apd.Color.orange,
    )

    # Apply ID-based stamp operations
    content_editor.hide_stamp_by_id(1, 1)
    content_editor.show_stamp_by_id(1, 2)

    # Save updated document
    content_editor.save(outfile)
```
