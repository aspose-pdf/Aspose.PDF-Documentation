---
title: Pindahkan Stempel Berdasarkan ID
linktitle: Pindahkan Stempel Berdasarkan ID
type: docs
weight: 80
url: /id/python-net/move-stamp-by-id-example/
description: Dalam contoh ini, sebuah stempel karet ditambahkan ke halaman 1 dan kemudian dipindahkan ke posisi baru menggunakan ID-nya sebelum menyimpan dokumen yang diperbarui.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Pindahkan Stempel Karet berdasarkan ID dalam PDF Menggunakan PdfContentEditor di Python
Abstract: Contoh ini menunjukkan cara memindahkan posisi anotasi stempel karet yang sudah ada dalam PDF menggunakan Aspose.PDF for Python via the Facades API. Ini menunjukkan cara membuat stempel dan kemudian memindahkannya secara programatik menggunakan ID-nya.
---

Setelah menambahkan anotasi stempel karet ke PDF, Anda mungkin perlu menyesuaikan posisinya. Metode 'move_stamp_by_id()' memungkinkan Anda memindahkan stempel berdasarkan pengidentifikasinya, tanpa membuatnya ulang. Ini berguna dalam alur kerja otomatis di mana penempatan stempel harus disesuaikan secara dinamis.

1. Buat sebuah [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instance.
1. Hubungkan dokumen PDF input.
1. Tambahkan anotasi stempel karet.
1. Pindahkan stempel menggunakan ID-nya.
1. Simpan dokumen PDF yang diperbarui.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def move_stamp_by_id_example(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    content_editor.create_rubber_stamp(
        1,
        apd.Rectangle(300, 420, 180, 60),
        "Approved",
        "Move this stamp by ID",
        apd.Color.green,
    )

    # Move stamp by ID overload
    content_editor.move_stamp_by_id(1, 1, 240, 360)

    # Save updated document
    content_editor.save(outfile)
```    
