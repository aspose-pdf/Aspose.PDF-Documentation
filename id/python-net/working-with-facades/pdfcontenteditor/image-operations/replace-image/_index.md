---
title: Ganti Gambar dalam PDF
linktitle: Ganti Gambar dalam PDF
type: docs
weight: 30
url: /id/python-net/replace-image/
description: Contoh ini mengikat PDF input, mengganti gambar pertama pada halaman 1 dengan gambar baru, dan menyimpan dokumen yang telah dimodifikasi.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ganti Gambar dalam PDF Menggunakan PdfContentEditor di Python
Abstract: Contoh ini menunjukkan cara mengganti gambar yang ada dalam dokumen PDF menggunakan Aspose.PDF for Python via the Facades API. Ini memperlihatkan cara menargetkan gambar tertentu pada sebuah halaman dan menggantinya dengan gambar baru, kemudian menyimpan PDF yang diperbarui.
---

PDF sering berisi gambar yang mungkin perlu diperbarui atau diganti, seperti logo, diagram, atau foto. Dengan [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), Anda dapat mengganti gambar tertentu pada halaman tertentu dengan memberikan nomor halaman, indeks gambar, dan jalur file gambar baru.

1. Buat instance PdfContentEditor.
1. Hubungkan dokumen PDF masukan.
1. Ganti gambar tertentu pada halaman yang diberikan.
1. Simpan dokumen PDF yang diperbarui.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_image(infile, image_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Replace image on page 1
    content_editor.replace_image(1, 1, image_file)
    # Save updated document
    content_editor.save(outfile)
```
