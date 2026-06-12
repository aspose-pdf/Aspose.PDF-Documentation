---
title: Ganti Teks Pada Halaman Dengan State
linktitle: Ganti Teks Pada Halaman Dengan State
type: docs
weight: 20
url: /id/python-net/replace-text-on-page-with-state/
description: Dalam contoh ini, semua kemunculan kata "software" pada halaman 1 diganti dengan "SOFTWARE PAGE 1", menggunakan teks merah dengan ukuran font 12.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ganti Teks dengan Pemformatan Kustom pada Halaman Tertentu Menggunakan PdfContentEditor di Python
Abstract: Contoh ini menunjukkan cara mengganti teks pada halaman tertentu dalam PDF sambil menerapkan pemformatan kustom menggunakan Aspose.PDF for Python via the Facades API. Ini menunjukkan cara mengontrol ukuran font dan warna selama penggantian teks.
---

Terkadang mengganti teks dalam PDF juga memerlukan perubahan format seperti warna atau ukuran font. Menggunakan TextState, Anda dapat mendefinisikan properti gaya dan menerapkannya selama penggantian. Ini memungkinkan Anda menyorot teks yang dimodifikasi atau menegakkan format yang konsisten di seluruh dokumen.

1. Buat sebuah [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instansi.
1. Hubungkan dokumen PDF input.
1. Definisikan TextState dengan pemformatan kustom.
1. Konfigurasikan strategi penggantian.
1. Ganti teks pada halaman tertentu.
1. Simpan dokumen PDF yang diperbarui.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_text_on_page_with_state(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    text_state = ap.text.TextState()
    text_state.foreground_color = ap.Color.red
    text_state.font_size = 12

    # Replace text on a specific page with explicit text formatting
    content_editor.replace_text_strategy.replace_scope = (
        pdf_facades.ReplaceTextStrategy.Scope.REPLACE_ALL
    )
    content_editor.replace_text("software", 1, "SOFTWARE PAGE 1", text_state)
    # Save updated document
    content_editor.save(outfile)
```
