---
title: Tambahkan Anotasi Teks
linktitle: Tambahkan Anotasi Teks
type: docs
weight: 50
url: /id/python-net/add-text-annotation/
description: Tambahkan anotasi teks ke dokumen PDF menggunakan kelas PdfContentEditor dalam Aspose.PDF for Python via .NET.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tambahkan Anotasi Teks di Python
Abstract: Pelajari cara menambahkan anotasi teks ke dokumen PDF menggunakan kelas PdfContentEditor dalam Aspose.PDF for Python via .NET. Contoh ini menunjukkan cara menempatkan anotasi teks pada posisi tertentu, mendefinisikan judul dan isinya, serta menyimpan file PDF yang diperbarui.
---

Artikel ini menunjukkan cara menambahkan anotasi teks ke dokumen PDF menggunakan [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) kelas dalam Aspose.PDF.

Anotasi teks memungkinkan Anda melampirkan komentar, catatan, atau informasi tambahan ke bagian tertentu dari halaman PDF. Anotasi ini dapat muncul sebagai ikon dan dapat diperluas oleh pengguna saat melihat dokumen.

Pada contoh ini:

- Dokumen PDF dimuat ke dalam PdfContentEditor.
- Anotasi teks ditambahkan pada posisi tertentu di halaman.
- Anotasi tersebut mencakup judul, konten, tipe ikon, dan pengaturan visibilitas.
- Dokumen yang telah dimodifikasi disimpan ke file baru.

1. Buat objek PdfContentEditor.
1. Hubungkan Dokumen PDF input.
1. Tentukan posisi anotasi.
1. Tambahkan anotasi Teks.
1. Simpan PDF yang diperbarui.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_text_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add text annotation to page 1
    content_editor.create_text(
        apd.Rectangle(100, 400, 50, 50),
        "Text Annotation",
        "This is a text annotation",
        True,
        "Insert",
        1,
    )
    # Save updated document
    content_editor.save(outfile)
```
