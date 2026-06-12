---
title: Tambahkan Anotasi Lingkaran
linktitle: Tambahkan Anotasi Lingkaran
type: docs
weight: 10
url: /id/python-net/add-circle-annotation/
description: Contoh ini mengikat PDF input, membuat anotasi lingkaran pada halaman pertama, dan menyimpan dokumen yang telah dimodifikasi.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tambahkan Anotasi Lingkaran ke PDF Menggunakan PdfContentEditor dalam Python
Abstract: Contoh ini menunjukkan cara menambahkan anotasi lingkaran ke dokumen PDF menggunakan Aspose.PDF untuk Python via the Facades API. Ini memperlihatkan cara mendefinisikan batas anotasi, mengatur teks konten, mengonfigurasi warna dan tampilan, serta menyimpan dokumen yang diperbarui.
---

Anotasi lingkaran berguna untuk menyoroti area yang menarik dalam dokumen PDF. Dengan [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), Anda dapat membuat bentuk melingkar dengan menentukan persegi panjang yang menentukan batas lingkaran, bersama dengan teks anotasi, warna, opsi isi, nomor halaman, dan lebar batas.

1. Buat objek PdfContentEditor.
1. Hubungkan PDF input.
1. Tentukan Batas Lingkaran.
1. Tambahkan anotasi Lingkaran.
1. Simpan Document yang diperbarui.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_circle_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    # Create CircleAnnotation object
    rect = apd.Rectangle(300, 300, 400, 400)
    contents = "This is circle annotation"
    content_editor.create_square_circle(rect, contents, apd.Color.blue, False, 1, 3)

    # Save output PDF file
    content_editor.save(outfile)
```
