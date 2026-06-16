---
title: Tambahkan Anotasi Teks Bebas
linktitle: Tambahkan Anotasi Teks Bebas
type: docs
weight: 20
url: /id/python-net/add-free-text-annotation/
description: Contoh ini memuat file PDF yang ada, menambahkan anotasi teks bebas ke halaman pertama pada posisi yang telah ditentukan, dan menyimpan dokumen yang telah dimodifikasi.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tambahkan Anotasi Teks Bebas ke PDF Menggunakan Python
Abstract: Contoh ini menunjukkan cara menyisipkan anotasi teks bebas ke dalam dokumen PDF menggunakan Aspose.PDF for Python via the Facades API. Ini memperlihatkan cara mengikat PDF, menentukan penempatan anotasi, menambahkan teks kustom, dan menyimpan dokumen yang diperbarui.
---

Anotasi teks bebas memungkinkan Anda menempatkan teks yang terlihat langsung pada halaman PDF tanpa memerlukan komentar pop-up. Menggunakan PdfContentEditor, Anda dapat menentukan persegi panjang anotasi, teks yang ditampilkan, dan halaman target.

1. Buat [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) objek.
1. Hubungkan PDF input.
1. Tentukan posisi Anotasi.
1. Tambahkan Anotasi Teks Bebas.
1. Simpan Document yang diperbarui.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_free_text_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add free text annotation to page 1
    content_editor.create_free_text(
        apd.Rectangle(200, 480, 150, 25), "This is a free text annotation", 1
    )
    # Save updated document
    content_editor.save(outfile)
```
