---
title: Hapus Lampiran
linktitle: Hapus Lampiran
type: docs
weight: 50
url: /id/python-net/remove-attachments/
description: Contoh ini mengikat PDF input, menghapus semua lampiran, dan menyimpan PDF yang dimodifikasi tanpa file yang tersemat.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Hapus Semua Lampiran dari PDF Menggunakan Python
Abstract: Contoh ini menunjukkan cara menghapus semua lampiran file dari dokumen PDF menggunakan Aspose.PDF for Python via the Facades API. Ini memperlihatkan cara mengikat PDF, menghapus lampiran yang tersemat, dan menyimpan dokumen yang diperbarui.
---

PDF dapat berisi lampiran seperti dokumen, gambar, atau file lainnya. Ada skenario di mana Anda perlu membersihkan PDF dari semua lampiran untuk tujuan keamanan, privasi, atau distribusi. Menggunakan [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), Anda dapat secara programatis menghapus semua lampiran yang tersemat dalam dokumen.

1. Buat objek PdfContentEditor. 
1. Gabungkan PDF input.
1. Hapus Semua Lampiran.
1. Simpan Document yang diperbarui.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def remove_attachments(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Remove all attachments from document
    content_editor.delete_attachments()
    # Save updated document
    content_editor.save(outfile)
```
