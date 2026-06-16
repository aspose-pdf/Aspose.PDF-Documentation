---
title: Tambahkan Cap Karet
linktitle: Tambahkan Cap Karet
type: docs
weight: 10
url: /id/python-net/add-rubber-stamp/
description: Contoh ini menggabungkan PDF input, menambahkan cap karet berwarna hijau “Approved” pada empat halaman pertama, dan menyimpan dokumen yang telah dimodifikasi.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tambahkan Anotasi Cap Karet ke PDF Menggunakan PdfContentEditor dalam Python
Abstract: Contoh ini menunjukkan cara menambahkan anotasi cap karet ke dokumen PDF menggunakan Aspose.PDF for Python via the Facades API. Cap karet memungkinkan Anda menandai halaman secara visual dengan persetujuan, ulasan, atau label khusus.
---

Anotasi cap karet biasanya digunakan dalam PDF untuk menunjukkan persetujuan, status ulasan, atau catatan lain. Menggunakan [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), Anda dapat mendefinisikan persegi panjang untuk cap, mengatur teks dan komentar, memilih warna, dan menerapkannya ke beberapa halaman dokumen.

1. Buat sebuah instance PdfContentEditor.
1. Hubungkan dokumen PDF input.
1. Loop melalui halaman 1–4.
1. Tambahkan anotasi rubber stamp dengan teks khusus, komentar, dan warna.
1. Simpan dokumen PDF yang diperbarui.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_rubber_stamp(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    for i in range(1, 5):
        content_editor.create_rubber_stamp(
            i,
            apd.Rectangle(120, 450, 180, 60),
            "Approved",
            "Approved by reviewer",
            apd.Color.green,
        )
    # Save updated document
    content_editor.save(outfile)
```
