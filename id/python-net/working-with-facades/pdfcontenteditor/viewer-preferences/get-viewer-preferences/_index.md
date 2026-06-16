---
title: Dapatkan Preferensi Penampil PDF
linktitle: Dapatkan Preferensi Penampil PDF
type: docs
weight: 20
url: /id/python-net/get-viewer-preferences/
description: Cara membaca dan memodifikasi preferensi penampil PDF secara programatis menggunakan Aspose.PDF for Python
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Kelola Preferensi Penampil PDF dengan Aspose.PDF di Python
Abstract: Panduan ini menunjukkan cara membaca dan memodifikasi preferensi penampil PDF secara programatis menggunakan Aspose.PDF for Python. Preferensi penampil mengontrol bagaimana PDF ditampilkan saat dibuka di penampil PDF, seperti membuka dengan outline, menyembunyikan bilah alat, atau menggunakan tata letak satu halaman.
---

Aspose.PDF menyediakan alat untuk mengakses dan memperbarui preferensi penampil PDF. Preferensi ini menentukan tata letak awal dan perilaku presentasi dokumen PDF di pembaca PDF. Ini mencakup opsi seperti mengaktifkan tampilan outline, menyembunyikan bilah menu, atau menentukan mode tata letak halaman. Dengan menggunakan PdfContentEditor, Anda dapat mengambil preferensi yang ada, memeriksa flag tertentu, dan memperbaruinya sesuai kebutuhan.

1. Tentukan Flag ViewerPreference.
1. Inisialisasi [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) dan Bind PDF.
1. Dapatkan Preferensi Viewer Saat Ini.
1. Periksa Bendera Spesifik.
1. Tampilkan Preferensi Saat Ini.

```python
import aspose.pdf.facades as pdf_facades
import sys
from enum import IntFlag
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_viewer_preferences(infile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Read current viewer preference flags
    viewer_preference = ViewerPreference(content_editor.get_viewer_preference())
    if viewer_preference & ViewerPreference.PAGE_MODE_USE_OUTLINES:
        print("PageModeUseOutlines is enabled")
    print(f"Current viewer preference: {viewer_preference}")
```
