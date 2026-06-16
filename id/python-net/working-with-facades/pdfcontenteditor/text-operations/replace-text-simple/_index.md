---
title: Ganti Teks Sederhana
linktitle: Ganti Teks Sederhana
type: docs
weight: 40
url: /id/python-net/replace-text-simple/
description: Dalam contoh ini, semua kemunculan "33" diganti dengan "XXXIII " di seluruh dokumen. Ini menunjukkan penggantian string sederhana tanpa format khusus atau regex.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ganti Teks di Seluruh PDF Menggunakan PdfContentEditor dalam Python
Abstract: Contoh ini menunjukkan cara mengganti teks di seluruh dokumen PDF menggunakan Aspose.PDF for Python via the Facades API. Ia mengganti semua kemunculan string yang ditentukan dengan teks baru.
---

Penggantian teks sederhana berguna saat memperbarui nilai berulang dalam sebuah dokumen. Dengan [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), Anda dapat menentukan ruang lingkup penggantian dan mengganti teks secara global di semua halaman.

1. Buat sebuah [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instansi.
1. Hubungkan dokumen PDF input.
1. Konfigurasikan ruang lingkup penggantian untuk semua kemunculan.
1. Ganti teks target.
1. Simpan dokumen PDF yang diperbarui.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_text_simple(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Replace text in the whole document
    content_editor.replace_text_strategy.replace_scope = (
        pdf_facades.ReplaceTextStrategy.Scope.REPLACE_ALL
    )
    content_editor.replace_text("33", "XXXIII ")
    # Save updated document
    content_editor.save(outfile)
```
