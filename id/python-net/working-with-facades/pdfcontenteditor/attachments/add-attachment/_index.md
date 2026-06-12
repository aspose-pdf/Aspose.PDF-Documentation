---
title: Tambahkan Lampiran
linktitle: Tambahkan Lampiran
type: docs
weight: 10
url: /id/python-net/add-attachment/
description: Contoh ini mengikat PDF input, melampirkan file eksternal ke halaman pertama, dan menyimpan PDF yang dimodifikasi dengan lampiran yang disematkan.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tambahkan Lampiran File ke PDF Menggunakan Python
Abstract: Contoh ini menunjukkan cara melampirkan file eksternal ke dokumen PDF menggunakan Aspose.PDF for Python via the Facades API. Ini menunjukkan cara mengikat PDF, menambahkan lampiran dengan deskripsi, dan menyimpan dokumen yang diperbarui.
---

Lampiran file dalam PDF memungkinkan Anda menyertakan dokumen tambahan, gambar, atau sumber daya lainnya langsung dalam PDF. Dengan [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), Anda dapat secara programatis melampirkan file ke halaman tertentu, mengatur nama lampiran, dan memberikan deskripsi.

1. Buat objek PdfContentEditor.
1. Hubungkan PDF input.
1. Buka file Attachment.
1. Tambahkan Attachment ke PDF.
1. Simpan Document yang diperbarui.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_attachment(infile, attachment_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add attachment to page 1
    with open(attachment_file, "rb") as attachment_stream:
        content_editor.add_document_attachment(
            attachment_stream,
            path.basename(attachment_file),
            "This is a sample attachment for demonstration purposes.",
        )
    # Save updated document
    content_editor.save(outfile)
```
