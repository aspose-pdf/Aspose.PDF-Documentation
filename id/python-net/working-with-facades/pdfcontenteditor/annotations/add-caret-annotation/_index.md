---
title: Tambahkan Anotasi Caret
linktitle: Tambahkan Anotasi Caret
type: docs
weight: 10
url: /id/python-net/add-caret-annotation/
description: Contoh ini memuat PDF yang sudah ada, menambahkan anotasi caret ke halaman pertama, dan menyimpan dokumen yang telah dimodifikasi. Anotasi tersebut mencakup simbol caret merah dan teks komentar deskriptif.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tambahkan Anotasi Caret ke PDF Menggunakan Python
Abstract: Contoh ini menunjukkan cara menambahkan anotasi caret ke dokumen PDF menggunakan Aspose.PDF untuk Python via API Facades. Contoh tersebut memperlihatkan cara mengikat file PDF, menentukan penempatan anotasi menggunakan persegi panjang, mengonfigurasi properti caret, dan menyimpan dokumen yang diperbarui.
---

Anotasi caret biasanya digunakan untuk menunjukkan penyisipan teks atau komentar editorial dalam dokumen. Dengan PdfContentEditor, Anda dapat menambahkan anotasi caret secara programatis dengan menentukan nomor halaman, batas anotasi, area panggilan, simbol, teks catatan, dan warna.

1. Buat [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) objek.
1. Gabungkan PDF input.
1. Definisikan parameter Anotasi Caret:
  - Nomor halaman tempat anotasi akan ditambahkan
  - Persegi Caret (posisi anotasi)
  - Persegi Callout (area teks)
  - Simbol (misalnya "P")
  - Teks anotasi
  - Warna anotasi
1. Tambahkan Anotasi Caret.
1. Simpan Document yang diperbarui.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_caret_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add caret annotation to page 1
    content_editor.create_caret(
        1,
        apd.Rectangle(350, 400, 10, 10),
        apd.Rectangle(300, 380, 115, 15),
        "P",
        "This is a caret annotation",
        apd.Color.red,
    )
    # Save updated document
    content_editor.save(outfile)
```
