---
title: Tambahkan Anotasi Lampiran File
linktitle: Tambahkan Anotasi Lampiran File
type: docs
weight: 30
url: /id/python-net/add-file-attachment-annotation/
description: Contoh ini mengaitkan PDF input, menambahkan anotasi lampiran file ke halaman pertama menggunakan jalur file, dan menyimpan dokumen yang diperbarui.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tambahkan Anotasi Lampiran File ke PDF Menggunakan Python
Abstract: Contoh ini menunjukkan cara membuat anotasi lampiran file dalam PDF menggunakan jalur file dengan Aspose.PDF for Python via the Facades API. Ini menunjukkan cara menentukan penempatan anotasi, mengatur teks deskripsi, memilih jenis ikon, dan menyimpan dokumen yang dimodifikasi.
---

Anotasi lampiran file memungkinkan Anda menyematkan file eksternal sebagai ikon interaktif pada halaman PDF. Dengan menggunakan overload jalur file, Anda dapat melampirkan file secara langsung dari disk tanpa harus membuka aliran secara manual. Metode ini juga memungkinkan Anda menyesuaikan ikon anotasi dan menyediakan deskripsi bagi pengguna.

1. Buat [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) objek.
1. Hubungkan PDF input.
1. Tentukan Persegi Panjang Anotasi.
1. Tambahkan Anotasi Lampiran File.
1. Simpan Document yang diperbarui.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_file_attachment_annotation(infile, attachment_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Create file attachment annotation on page 1
    content_editor.create_file_attachment(
        apd.Rectangle(100, 520, 20, 20),
        "Attachment annotation contents",
        attachment_file,
        1,
        "PushPin",
    )
    # Save updated document
    content_editor.save(outfile)
```
