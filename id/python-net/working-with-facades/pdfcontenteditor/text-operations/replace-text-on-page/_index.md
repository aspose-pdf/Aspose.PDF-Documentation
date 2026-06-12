---
title: Ganti Teks Pada Halaman
linktitle: Ganti Teks Pada Halaman
type: docs
weight: 10
url: /id/python-net/replace-text-on-page/
description: Dalam contoh ini, kemunculan pertama kata "PDF" diganti dengan "Page 1 Replaced Text" menggunakan ukuran font yang ditentukan.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ganti Teks pada Halaman Tertentu Menggunakan PdfContentEditor dalam Python
Abstract: Contoh ini menunjukkan cara mengganti teks dalam dokumen PDF menggunakan Aspose.PDF for Python via the Facades API. Ini menunjukkan cara mengganti kemunculan pertama teks pada sebuah halaman dan menyimpan dokumen yang diperbarui.
---

Penggantian teks merupakan kebutuhan umum saat memperbarui dokumen PDF. Menggunakan [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), Anda dapat mencari teks tertentu dan menggantinya dengan konten baru. Properti 'replace_text_strategy' memungkinkan Anda mengontrol berapa banyak kemunculan yang diganti.

1. Buat sebuah instance PdfContentEditor.
1. Hubungkan dokumen PDF input.
1. Konfigurasikan strategi penggantian teks.
1. Ganti teks target.
1. Simpan dokumen PDF yang diperbarui.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_text_on_page(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Replace text on page 1
    content_editor.replace_text_strategy.replace_scope = (
        pdf_facades.ReplaceTextStrategy.Scope.REPLACE_FIRST
    )
    content_editor.replace_text("PDF", "Page 1 Replaced Text", 14)
    # Save updated document
    content_editor.save(outfile)
```
