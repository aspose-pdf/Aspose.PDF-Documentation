---
title: Hapus Stempel Berdasarkan ID
linktitle: Hapus Stempel Berdasarkan ID
type: docs
weight: 85
url: /id/python-net/delete-stamp-by-ids-examples/
description:
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Hapus Stempel Karet dengan ID Tunggal atau Ganda dalam PDF Menggunakan PdfContentEditor
Abstract: Contoh ini menunjukkan cara menghapus anotasi stempel karet dari PDF berdasarkan ID unik mereka menggunakan Aspose.PDF for Python via the Facades API. Contoh ini mencakup penghapusan dengan ID tunggal maupun ID ganda.
---

Saat bekerja dengan PDF yang berisi banyak stempel, sering kali perlu menghapus stempel tertentu tanpa memengaruhi yang lain. Dengan penghapusan berbasis ID, Anda dapat mengontrol secara tepat stempel mana yang akan dihapus:

- 'delete_stamp_by_id(stamp_id, page_number)' – menghapus satu stempel berdasarkan ID-nya pada halaman tertentu
- 'delete_stamp_by_ids(page_number, stamp_ids)' – menghapus beberapa stempel berdasarkan ID mereka pada halaman yang diberikan

1. Buat sebuah [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instansi.
1. Hubungkan dokumen PDF input.
1. Tambahkan dua stempel karet dengan ID yang berbeda.
1. Hapus stempel menggunakan metode penghapusan ID tunggal dan ID berganda.
1. Simpan PDF yang diperbarui.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def delete_stamp_by_ids_examples(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    # Create two stamps on page 1 so they can be deleted by ID
    content_editor.create_rubber_stamp(
        1,
        apd.Rectangle(120, 320, 180, 60),
        "Draft",
        "Delete by single ID",
        apd.Color.orange,
    )
    content_editor.create_rubber_stamp(
        1,
        apd.Rectangle(120, 250, 180, 60),
        "Draft",
        "Delete by multiple IDs",
        apd.Color.orange,
    )

    # Delete by single ID overload and by IDs overload
    content_editor.delete_stamp_by_id(1, 1)
    content_editor.delete_stamp_by_ids(1, [2])

    # Save updated document
    content_editor.save(outfile)
```

