---
title: Hapus Aksi Buka
linktitle: Hapus Aksi Buka
type: docs
weight: 30
url: /id/python-net/remove-open-action/
description: Contoh ini memuat PDF yang ada, menghapus aksi buka, dan menyimpan dokumen yang telah dibersihkan.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Hapus Aksi Buka Dokumen dari PDF Menggunakan Python
Abstract: Contoh ini menunjukkan cara menghapus aksi buka dokumen dari PDF menggunakan Aspose.PDF for Python via the Facades API. Ini menunjukkan cara mengaitkan PDF, membersihkan aksi buka, dan menyimpan dokumen yang diperbarui.
---

Dokumen PDF dapat berisi aksi yang dijalankan secara otomatis saat file dibuka, seperti peringatan JavaScript, perintah navigasi, atau perilaku lain. Dalam beberapa skenario, Anda mungkin perlu menghapus aksi-aksi ini untuk alasan keamanan, kepatuhan, atau pengalaman pengguna.

Dengan menggunakan PdfContentEditor, Anda dapat dengan mudah menghapus aksi buka dokumen dan memastikan PDF terbuka tanpa mengeksekusi perilaku otomatis apa pun.

1. Buat objek PdfContentEditor.
1. Hubungkan PDF input.
1. Hapus Aksi Buka Dokumen.
1. Simpan Document yang diperbarui.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def remove_open_action(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Remove open action from the document
    content_editor.remove_document_open_action()
    # Save updated document
    content_editor.save(outfile)
```
