---
title: Tambahkan Lampiran Dari Path
linktitle: Tambahkan Lampiran Dari Path
type: docs
weight: 20
url: /id/python-net/add-attachment-from-path/
description: Contoh ini mengikat PDF input, melampirkan file eksternal menggunakan path filenya, dan menyimpan PDF yang dimodifikasi dengan lampiran yang disematkan.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Lampirkan File ke PDF Menggunakan Overload Path File di Python
Abstract: Contoh ini menunjukkan cara melampirkan file eksternal ke dokumen PDF menggunakan overload path file dari ‘add_document_attachment()’ dalam Aspose.PDF for Python via the Facades API. Ini menyederhanakan penambahan lampiran tanpa harus membuka aliran file secara manual.
---

PDF dapat menyertakan file yang disematkan seperti dokumen, spreadsheet, atau gambar untuk referensi atau distribusi. Overload path file dari ‘add_document_attachment()’ memungkinkan Anda menambahkan lampiran langsung dari path file, menghilangkan kebutuhan membuka file secara manual.

1. Buat [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) objek.
1. Hubungkan PDF input.
1. Tambahkan Lampiran Menggunakan Path File.
1. Simpan Document yang diperbarui.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_attachment_from_path(infile, attachment_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add attachment using file-path overload
    content_editor.add_document_attachment(
        attachment_file,
        "Attachment added using file path overload.",
    )
    # Save updated document
    content_editor.save(outfile)
```
