---
title: Tambahkan Aksi Dokumen
linktitle: Tambahkan Aksi Dokumen
type: docs
weight: 20
url: /id/python-net/add-document-action/
description: Contoh ini menambahkan peringatan JavaScript yang muncul ketika PDF dibuka. Skrip tersebut dilampirkan pada peristiwa buka dokumen dan dijalankan secara otomatis di penampil PDF yang mendukung.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tambahkan Aksi JavaScript Buka Dokumen ke PDF dengan Python
Abstract: Contoh ini menunjukkan cara menambahkan aksi JavaScript tingkat dokumen yang dipicu ketika PDF dibuka. Menggunakan Aspose.PDF for Python via the Facades API, contoh ini memperlihatkan cara mengikat dokumen, menetapkan aksi peristiwa buka, dan menyimpan PDF yang telah diperbarui.
---

Aksi tingkat dokumen memungkinkan Anda mendefinisikan perilaku yang dijalankan secara otomatis ketika peristiwa tertentu terjadi, seperti membuka PDF. Dengan [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), Anda dapat melampirkan kode JavaScript ke peristiwa ini. Ini dapat digunakan untuk notifikasi, logika validasi, atau alur kerja interaktif.

1. Buat objek PdfContentEditor.
1. Gabungkan PDF input.
1. Tambahkan aksi tingkat Dokumen.
1. Simpan Document yang diperbarui.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_document_action(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add JavaScript action for document open event
    content_editor.add_document_additional_action(
        content_editor.DOCUMENT_OPEN,
        "app.alert('Document opened with PdfContentEditor action');",
    )
    # Save updated document
    content_editor.save(outfile)
```
