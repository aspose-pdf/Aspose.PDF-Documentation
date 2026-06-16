---
title: Tambahkan Tautan Dokumen PDF
linktitle: Tambahkan Tautan Dokumen PDF
type: docs
weight: 50
url: /id/python-net/add-pdf-document-link/
description: Contoh ini mengaitkan PDF input, menambahkan tautan berwarna hijau ke halaman dalam PDF lain, dan menyimpan dokumen yang telah dimodifikasi.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tambahkan Tautan Dokumen PDF Menggunakan PdfContentEditor dalam Python
Abstract: Contoh ini menunjukkan cara menambahkan tautan ke dokumen PDF lain menggunakan Aspose.PDF for Python via the Facades API. Ini memperlihatkan cara membuat area yang dapat diklik yang membuka PDF yang berbeda dan menyimpan dokumen yang telah diperbarui.
---

Tautan dokumen PDF memungkinkan pengguna menavigasi dari satu PDF ke PDF lain dengan mulus. Menggunakan [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), Anda dapat mendefinisikan persegi panjang yang dapat diklik yang menautkan ke halaman dalam file PDF yang berbeda, menjadikan dokumen Anda interaktif dan terhubung.

1. Buat sebuah instance PdfContentEditor.
1. Hubungkan dokumen PDF input.
1. Tentukan sebuah persegi panjang untuk tautan yang dapat diklik.
1. Spesifikasikan file PDF yang ditautkan, halaman sumber, dan halaman tujuan.
1. Atur warna tautan.
1. Simpan dokumen PDF yang diperbarui.

```python
import aspose.pdf.facades as pdf_facades
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as apd
import aspose.pdf as ap

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_pdf_document_link(infile, linked_pdf, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add link to another PDF document
    content_editor.create_pdf_document_link(
        apd.Rectangle(140, 590, 240, 20),
        linked_pdf,
        1,
        1,
        apd.Color.green,
    )
    # Save updated document
    content_editor.save(outfile)
```
