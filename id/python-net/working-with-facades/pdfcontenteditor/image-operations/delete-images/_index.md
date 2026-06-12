---
title: Hapus Gambar dari PDF
linktitle: Hapus Gambar dari PDF
type: docs
weight: 20
url: /id/python-net/delete-images/
description:
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Hapus Gambar Tertentu dari Halaman PDF Menggunakan PdfContentEditor di Python
Abstract: Contoh ini menunjukkan cara menghapus gambar tertentu dari dokumen PDF menggunakan Aspose.PDF for Python via the Facades API. Ini memperlihatkan cara menargetkan gambar pada halaman tertentu dan menyimpan dokumen yang telah diperbarui.
---

Kadang-kadang, Anda mungkin ingin menghapus hanya gambar tertentu dari PDF daripada menghapus semua visual. Dengan [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), Anda dapat menghapus gambar yang dipilih dengan menentukan nomor halaman dan indeks gambar.

Potongan kode ini mengikat PDF input, menghapus gambar kedua pada halaman 1, dan menyimpan PDF yang dimodifikasi, meninggalkan gambar lain tetap utuh.

1. Buat instance PdfContentEditor.
1. Hubungkan dokumen PDF masukan.
1. Hapus gambar tertentu dari halaman yang ditentukan.
1. Simpan dokumen PDF yang diperbarui.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def delete_images(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Delete image on page 1
    content_editor.delete_image(1, [2])
    # Save updated document
    content_editor.save(outfile)
```
