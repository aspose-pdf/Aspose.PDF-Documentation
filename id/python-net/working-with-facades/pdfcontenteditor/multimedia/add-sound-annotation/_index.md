---
title: Tambahkan Anotasi Suara
linktitle: Tambahkan Anotasi Suara
type: docs
weight: 20
url: /id/python-net/add-sound-annotation/
description: Contoh ini mengikat PDF input, menambahkan anotasi suara pada halaman 1, dan menyimpan PDF yang telah dimodifikasi.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tambahkan Anotasi Suara ke PDF Menggunakan PdfContentEditor di Python
Abstract: Contoh ini menunjukkan cara menyisipkan audio ke dalam dokumen PDF menggunakan Aspose.PDF for Python via the Facades API. Ini menunjukkan cara menambahkan anotasi suara yang dapat diklik yang memutar file audio langsung di dalam PDF.
---

Anotasi suara dalam PDF memungkinkan Anda menambahkan konten audio seperti catatan suara, musik, atau efek suara ke dokumen Anda. Menggunakan [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), Anda dapat mendefinisikan sebuah persegi kecil yang dapat diklik pada halaman yang memutar file audio tertentu ketika diaktifkan.

1. Buat instance PdfContentEditor.
1. Hubungkan dokumen PDF input.
1. Tentukan persegi panjang untuk anotasi suara.
1. Spesifikasikan file audio, nama anotasi, nomor halaman, dan laju sampling.
1. Simpan dokumen PDF yang diperbarui.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_sound_annotation(infile, sound_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add sound annotation to page 1
    content_editor.create_sound(
        apd.Rectangle(80, 450, 30, 30), sound_file, "Speaker", 1, "8000"
    )
    # Save updated document
    content_editor.save(outfile)
```
