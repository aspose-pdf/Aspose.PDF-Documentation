---
title: Ubah Preferensi Penampil PDF
linktitle: Ubah Preferensi Penampil PDF
type: docs
weight: 10
url: /id/python-net/change-viewer-preferences/
description: Modul ini menunjukkan cara menyesuaikan pengaturan penampil dokumen PDF menggunakan Aspose.PDF for Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Sesuaikan Pengalaman Penampil PDF dengan Python
Abstract: Kontrol bagaimana dokumen PDF Anda muncul saat dibuka dengan memodifikasi preferensi penampil secara programatis. Fungsionalitas ini memungkinkan Anda menyesuaikan antarmuka pengguna dan tata letak, memastikan pengalaman penampilan yang konsisten.
---

File PDF memiliki preferensi penampil bawaan yang mengontrol aspek-aspek seperti tata letak halaman, visibilitas bilah alat, dan perilaku jendela. Dengan menggunakan skrip ini, Anda dapat:

- Periksa preferensi penampil saat ini dari sebuah PDF.
- Modifikasi opsi tata letak (mis., satu halaman, satu kolom, dua kolom).
- Alihkan elemen UI seperti bilah alat, bilah menu, atau tampilan judul.
- Simpan PDF dengan preferensi yang diperbarui untuk pengalaman menonton yang terkontrol.

1. Tentukan Flag ViewerPreference.
1. Dapatkan Preferensi Viewer Saat Ini.
1. Modifikasi Preferensi.
1. Terapkan Preferensi yang Diperbarui.
1. Simpan PDF.

```python
import aspose.pdf.facades as pdf_facades
import sys
from enum import IntFlag
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Define ViewerPreference flags
class ViewerPreference(IntFlag):
    HIDE_TOOLBAR = 1
    HIDE_MENUBAR = 2
    HIDE_WINDOW_UI = 4
    FIT_WINDOW = 8
    CENTER_WINDOW = 16
    DISPLAY_DOC_TITLE = 32
    NON_FULL_SCREEN_PAGE_MODE_USE_NONE = 64
    NON_FULL_SCREEN_PAGE_MODE_USE_OUTLINES = 128
    NON_FULL_SCREEN_PAGE_MODE_USE_THUMBS = 256
    NON_FULL_SCREEN_PAGE_MODE_USE_OC = 512
    DIRECTION_L2R = 1024
    DISPLAY_DOC_TITLE_IN_TITLE_BAR = 2048
    PAGE_LAYOUT_SINGLE_PAGE = 4096
    PAGE_LAYOUT_ONE_COLUMN = 8192
    PAGE_LAYOUT_TWO_COLUMN_LEFT = 16384
    PAGE_LAYOUT_TWO_COLUMN_RIGHT = 32768
    PAGE_LAYOUT_TWO_PAGE_LEFT = 65536
    PAGE_LAYOUT_TWO_PAGE_RIGHT = 131072


def change_viewer_preferences(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    # Get current viewer preference and toggle single-page layout
    current_preference = ViewerPreference(content_editor.get_viewer_preference())
    updated_preference = current_preference | ViewerPreference.PAGE_LAYOUT_SINGLE_PAGE
    content_editor.change_viewer_preference(int(updated_preference))

    # Save updated document
    content_editor.save(outfile)
```
