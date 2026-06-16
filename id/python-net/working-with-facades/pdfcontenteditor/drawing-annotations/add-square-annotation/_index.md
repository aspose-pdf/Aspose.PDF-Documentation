---
title: Tambahkan Anotasi Kotak
linktitle: Tambahkan Anotasi Kotak
type: docs
weight: 60
url: /id/python-net/add-square-annotation/
description: Contoh ini mengikat PDF input, menambahkan anotasi kotak biru berisi pada halaman pertama, dan menyimpan dokumen yang telah dimodifikasi.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tambahkan Anotasi Kotak ke PDF Menggunakan PdfContentEditor dalam Python
Abstract: Contoh ini menunjukkan cara menambahkan anotasi kotak ke dokumen PDF menggunakan Aspose.PDF for Python via the Facades API. Ini memperlihatkan cara mendefinisikan persegi panjang anotasi, konten teks, warna, opsi isi, dan menyimpan dokumen yang diperbarui.
---

Anotasi kotak biasanya digunakan untuk menyoroti area yang menarik, menandai bagian penting, atau memberikan petunjuk visual dalam dokumen PDF. Menggunakan [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), Anda dapat membuat anotasi kotak (atau bulat) dengan menentukan persegi batas, teks konten, warna batas, opsi isi, nomor halaman, dan lebar batas.

1. Buat objek PdfContentEditor.
1. Gabungkan PDF input.
1. Definisikan anotasi Square.
1. Tambahkan anotasi Square.
1. Simpan Document yang diperbarui.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_square_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    # Create SquareAnnotation object
    rect = apd.Rectangle(100, 300, 200, 400)
    contents = "This is square annotation"
    content_editor.create_square_circle(rect, contents, apd.Color.blue, True, 1, 3)

    # Save output PDF file
    content_editor.save(outfile)
```
