---
title: Tambahkan Tautan Aksi Kustom
linktitle: Tambahkan Tautan Aksi Kustom
type: docs
weight: 20
url: /id/python-net/add-custom-action-link/
description: Contoh ini mengikat sebuah PDF input, menambahkan tautan aksi kustom pada halaman pertama, dan menyimpan dokumen yang telah dimodifikasi. Daftar aksi kosong digunakan untuk kesederhanaan, tetapi implementasi nyata dapat menyertakan aksi sebenarnya.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tambahkan Tautan Aksi Kustom ke PDF Menggunakan PdfContentEditor dalam Python
Abstract: Contoh ini menunjukkan cara menambahkan tautan aksi kustom ke dokumen PDF menggunakan Aspose.PDF for Python via the Facades API. Ini memperlihatkan cara membuat area yang dapat diklik pada sebuah halaman, menetapkan aksi kustom, dan menyimpan dokumen yang diperbarui.
---

Tautan aksi kustom memungkinkan Anda mendefinisikan area interaktif dalam PDF yang dapat memicu aksi tertentu saat diklik, seperti menjalankan skrip, menavigasi halaman, atau menjalankan perintah khusus aplikasi. Menggunakan [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), Anda dapat membuat tautan aksi kustom dengan menentukan halaman, persegi panjang, warna, dan aksi.

1. Buat instance PdfContentEditor.
1. Hubungkan dokumen PDF masukan.
1. Tentukan persegi panjang untuk tautan yang dapat diklik.
1. Spesifikasikan nomor halaman dan warna tautan.
1. Tetapkan aksi khusus (kosong dalam contoh ini).
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


def add_custom_action_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add custom action link. Empty action list keeps the sample runnable
    # without requiring additional enum lookups.
    content_editor.create_custom_action_link(
        apd.Rectangle(200, 500, 260, 20),
        1,
        apd.Color.dark_red,
        [],
    )
    # Save updated document
    content_editor.save(outfile)
```
