---
title: Pindahkan Stempel Berdasarkan Indeks
linktitle: Pindahkan Stempel Berdasarkan Indeks
type: docs
weight: 90
url: /id/python-net/move-stamp-by-index/
description: Cara memposisikan ulang anotasi stempel karet dalam PDF dengan menggunakan indeksnya pada halaman menggunakan Aspose.PDF for Python
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Pindahkan Stempel Karet dalam PDF Menggunakan Penempatan Berbasis Indeks
Abstract: Contoh ini menunjukkan cara memposisikan ulang anotasi stempel karet dalam PDF dengan menggunakan indeks pada halaman menggunakan Aspose.PDF for Python melalui Facades API. Contoh ini menyoroti pembuatan beberapa stempel dan menyiapkannya untuk operasi pemindahan.
---

Dalam penyuntingan PDF, mungkin perlu menyesuaikan posisi stempel karet yang ada. Cuplikan kode ini menunjukkan caranya:

- Tambahkan beberapa stempel pada halaman yang sama
- Siapkan mereka untuk dipindahkan posisinya menggunakan indeks mereka
- Opsional, pindahkan stempel dengan menentukan halaman, indeks, dan koordinat baru

Metode ‘move_stamp(page_number, stamp_index, new_x, new_y)’ dapat memposisikan ulang stempel dengan tepat.

1. Buat sebuah [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) objek.
1. Hubungkan PDF ke editor.
1. Tambahkan beberapa stempel karet ke halaman.
1. Simpan dokumen sebelum melakukan operasi pemindahan.
1. Pindahkan stempel tertentu berdasarkan indeksnya.
1. Simpan PDF yang diperbarui.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def move_stamp_by_index(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    content_editor.create_rubber_stamp(
        2,
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
    content_editor.save(outfile)

    # Move first stamp on page 1 by index
    # content_editor.move_stamp(1, 1, 10, 10)
    # Save updated document
    content_editor.save(outfile)
```    
