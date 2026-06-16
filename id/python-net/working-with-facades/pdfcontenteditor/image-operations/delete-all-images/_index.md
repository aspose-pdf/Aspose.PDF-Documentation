---
title: Hapus Semua Gambar dari PDF
linktitle: Hapus Semua Gambar dari PDF
type: docs
weight: 10
url: /id/python-net/delete-all-images/
description: Hapus semua gambar dari dokumen PDF menggunakan Aspose.PDF for Python via the Facades API.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Hapus Semua Gambar dari PDF Menggunakan PdfContentEditor di Python
Abstract: Contoh ini menunjukkan cara menghapus semua gambar dari dokumen PDF menggunakan Aspose.PDF for Python via the Facades API. Ini menunjukkan cara mengikat sebuah PDF, menghapus semua gambar yang tersemat, dan menyimpan dokumen yang diperbarui.
---

Dokumen PDF sering berisi gambar untuk ilustrasi, branding, atau dekorasi. Mungkin ada situasi di mana Anda perlu menghapus semua gambar dari PDF, seperti mengurangi ukuran file, melindungi visual sensitif, atau menyiapkan versi hanya teks.

Menggunakan [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), Anda dapat secara programatis menghapus semua gambar dari PDF, memastikan dokumen hanya berisi konten teks. Contoh ini mengikat PDF input, menghapus semua gambar, dan menyimpan file yang dimodifikasi.

1. Buat objek PdfContentEditor.
1. Gabungkan PDF input.
1. Hapus Semua gambar.
1. Simpan Document yang diperbarui.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def delete_all_image(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Delete all images from the document
    content_editor.delete_image()
    # Save updated document
    content_editor.save(outfile)
```
