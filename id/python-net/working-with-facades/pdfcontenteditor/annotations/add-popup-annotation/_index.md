---
title: Tambahkan Anotasi Popup
linktitle: Tambahkan Anotasi Popup
type: docs
weight: 40
url: /id/python-net/add-popup-annotation/
description: Contoh ini memuat sebuah PDF, menambahkan anotasi popup ke halaman pertama, dan menyimpan dokumen yang telah dimodifikasi. Popup diatur agar terlihat secara default dan menampilkan teks komentar yang ditentukan.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tambahkan Anotasi Popup ke PDF Menggunakan Python
Abstract: Contoh ini menunjukkan cara menyisipkan anotasi popup ke dalam dokumen PDF menggunakan Aspose.PDF for Python via the Facades API. Ini menjelaskan cara menentukan area popup, mengatur teks anotasi, mengontrol visibilitas, dan menyimpan dokumen yang diperbarui.
---

Anotasi popup berguna untuk menambahkan komentar, penjelasan, atau catatan interaktif dalam file PDF. Menggunakan [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), Anda dapat membuat anotasi popup secara programatis dengan menentukan lokasi, konten, visibilitas, dan nomor halaman.

1. Buat objek PdfContentEditor.
1. Hubungkan PDF input.
1. Tentukan persegi panjang Popup Annotation.
1. Tambahkan Popup Annotation.
1. Simpan Document yang diperbarui.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_popup_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add popup annotation to page 1
    content_editor.create_popup(
        apd.Rectangle(220, 520, 180, 80),
        "This is a popup annotation",
        True,
        1,
    )
    # Save updated document
    content_editor.save(outfile)
```
