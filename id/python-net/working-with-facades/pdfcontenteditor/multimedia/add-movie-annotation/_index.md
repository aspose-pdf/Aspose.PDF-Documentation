---
title: Tambahkan Anotasi Film
linktitle: Tambahkan Anotasi Film
type: docs
weight: 10
url: /id/python-net/add-movie-annotation/
description: Contoh ini mengikat PDF input, menambahkan anotasi film pada halaman 1, dan menyimpan PDF yang diperbarui.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tambahkan Anotasi Film ke PDF Menggunakan PdfContentEditor dalam Python
Abstract: Contoh ini menunjukkan cara menyematkan film (video) ke dalam dokumen PDF menggunakan Aspose.PDF for Python via the Facades API. Ini memperlihatkan cara menambahkan anotasi yang dapat diklik yang memutar video langsung di dalam PDF.
---

Anotasi film dalam PDF memungkinkan Anda menyematkan konten multimedia, seperti video, ke dalam dokumen Anda. Menggunakan [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), Anda dapat menentukan persegi panjang pada halaman tempat video akan muncul. Saat diklik, video dapat diputar langsung dari PDF, membuat dokumen Anda lebih interaktif dan menarik.

1. Buat instance PdfContentEditor.
1. Hubungkan dokumen PDF input.
1. Tentukan persegi panjang untuk anotasi film.
1. Tentukan file video yang akan disematkan.
1. Tetapkan nomor halaman untuk anotasi.
1. Simpan dokumen PDF yang diperbarui.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_movie_annotation(infile, movie_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add movie annotation to page 1
    content_editor.create_movie(apd.Rectangle(80, 500, 220, 120), movie_file, 1)
    # Save updated document
    content_editor.save(outfile)
```
