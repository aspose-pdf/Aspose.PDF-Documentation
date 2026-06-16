---
title: Ganti Teks Regex
linktitle: Ganti Teks Regex
type: docs
weight: 30
url: /id/python-net/replace-text-regex/
description: Dalam contoh ini, semua angka empat digit dalam dokumen diganti dengan placeholder "[NUMBER]". Ini berguna untuk menyamarkan data sensitif, menormalkan konten, atau menganonimkan dokumen.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ganti Teks Menggunakan Ekspresi Reguler dengan PdfContentEditor di Python
Abstract: Contoh ini menunjukkan cara mengganti teks dalam PDF menggunakan ekspresi reguler dengan Aspose.PDF untuk Python melalui API Facades. Ini memperlihatkan cara mencari pola dan mengganti semua kecocokan di seluruh dokumen.
---

Ekspresi reguler memungkinkan penggantian teks yang fleksibel berdasarkan pola daripada string tetap. Dengan mengaktifkan dukungan regex dalam 'replace_text_strategy', Anda dapat mencocokkan konten dinamis seperti angka, tanggal, atau string yang diformat.

1. Buat sebuah [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instansi.
1. Hubungkan dokumen PDF input.
1. Konfigurasikan strategi penggantian untuk menggunakan regex.
1. Ganti pola yang cocok di seluruh dokumen.
1. Simpan dokumen PDF yang diperbarui.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_text_regex(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Replace text in the whole document
    content_editor.replace_text_strategy.replace_scope = (
        pdf_facades.ReplaceTextStrategy.Scope.REPLACE_ALL
    )
    content_editor.replace_text_strategy.is_regular_expression_used = True
    content_editor.replace_text(r"\d{4}", "[NUMBER]")
    # Save updated document
    content_editor.save(outfile)
```
