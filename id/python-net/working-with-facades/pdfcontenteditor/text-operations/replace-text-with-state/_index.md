---
title: Ganti Teks Dengan State
linktitle: Ganti Teks Dengan State
type: docs
weight: 50
url: /id/python-net/replace-text-with-state/
description: Dalam contoh ini, semua kemunculan "software" diganti dengan "SOFTWARE" dan diformat berwarna biru dengan ukuran font 14.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ganti Teks dengan Pemformatan Kustom dalam PDF Menggunakan PdfContentEditor di Python
Abstract: Contoh ini menunjukkan cara mengganti teks dalam dokumen PDF sambil menerapkan pemformatan kustom menggunakan Aspose.PDF for Python via the Facades API. Ini menunjukkan cara mengontrol warna teks dan ukuran font selama penggantian.
---

Ketika memperbarui teks dalam PDF, Anda mungkin ingin konten pengganti menonjol. Dengan menggunakan objek TextState, Anda dapat mendefinisikan gaya seperti warna dan ukuran font, kemudian menerapkannya pada semua teks yang diganti.

1. Buat sebuah [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)  instansi.
1. Hubungkan dokumen PDF input.
1. Definisikan TextState dengan pemformatan kustom.
1. Konfigurasikan ruang lingkup penggantian.
1. Ganti teks di seluruh dokumen.
1. Simpan dokumen PDF yang diperbarui.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_text_with_state(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    text_state = ap.text.TextState()
    text_state.foreground_color = ap.Color.blue
    text_state.font_size = 14

    # Replace text with explicit text formatting
    content_editor.replace_text_strategy.replace_scope = (
        pdf_facades.ReplaceTextStrategy.Scope.REPLACE_ALL
    )
    content_editor.replace_text("software", "SOFTWARE", text_state)
    # Save updated document
    content_editor.save(outfile)
```
