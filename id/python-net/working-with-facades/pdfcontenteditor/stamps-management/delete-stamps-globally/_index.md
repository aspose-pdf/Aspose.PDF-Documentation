---
title: Hapus Stempel Secara Global
linktitle: Hapus Stempel Secara Global
type: docs
weight: 60
url: /id/python-net/delete-stamps-globally/
description: Contoh ini menunjukkan cara menghapus anotasi stempel karet secara global di semua halaman dalam PDF menggunakan Aspose.PDF for Python via the Facades API. Ini memperlihatkan cara menghapus stempel berdasarkan ID tanpa harus menentukan halaman secara individual.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Hapus Stempel Karet Secara Global dalam PDF Menggunakan PdfContentEditor di Python
Abstract: Contoh ini menunjukkan cara menghapus anotasi stempel karet secara global di semua halaman dalam PDF menggunakan Aspose.PDF for Python via the Facades API. Ini memperlihatkan cara menghapus stempel berdasarkan ID tanpa harus menentukan halaman secara individual.
---

Saat bekerja dengan banyak halaman, Anda mungkin perlu menghapus stempel tertentu di seluruh dokumen. Metode 'delete_stamp_by_id()' dan 'delete_stamp_by_ids()' memungkinkan Anda menghapus stempel secara global berdasarkan identifier mereka, menghilangkan kebutuhan untuk mengulangi proses melalui setiap halaman secara manual.

1. Buat sebuah [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instance.
1. Hubungkan dokumen PDF input.
1. Tambahkan stempel karet ke beberapa halaman.
1. Hapus stempel secara global menggunakan ID mereka.
1. Simpan dokumen PDF yang diperbarui.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def delete_stamps_globally(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    # Add stamps across multiple pages so global deletion is meaningful
    for page in range(1, 5):
        content_editor.create_rubber_stamp(
            page,
            apd.Rectangle(120, 500, 180, 60),
            "Draft",
            "Stamp for global deletion",
            apd.Color.gray,
        )

    # delete_stamp_by_id without page number removes stamp ID from all pages
    content_editor.delete_stamp_by_id(1)
    # delete_stamp_by_ids without page number removes a list of IDs from all pages
    content_editor.delete_stamp_by_ids([2, 3])

    # Save updated document
    content_editor.save(outfile)
```
