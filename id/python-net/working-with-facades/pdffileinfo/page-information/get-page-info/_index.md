---
title: Dapatkan Informasi Halaman
linktitle: Dapatkan Informasi Halaman
type: docs
weight: 10
url: /id/python-net/get-page-info/
description: Pelajari cara mengakses informasi tingkat halaman dalam PDF secara programatik menggunakan Aspose.PDF for Python. Panduan ini menunjukkan cara mengambil lebar halaman, tinggi, rotasi, dan offset untuk halaman tertentu dalam dokumen PDF.
lastmod: "2026-06-12"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dapatkan Informasi Halaman PDF Menggunakan Aspose.PDF for Python
Abstract: Fungsi ini mengekstrak lebar, tinggi, rotasi, serta offset horizontal (X) dan vertikal (Y) dari sebuah halaman PDF. Properti-properti ini dikembalikan dalam satuan poin dan mencerminkan ukuran fisik halaman serta penempatan konten di dalam PDF. Fungsi ini mencetak nilai-nilai yang diambil, memungkinkan pengembang memahami tata letak dan orientasi halaman untuk manipulasi PDF lebih lanjut.
---

Fungsi utilitas ‘get_page_information’ membantu pengembang memahami struktur dan tata letak halaman PDF. Setiap halaman PDF dapat memiliki dimensi, rotasi, dan offset internal yang berbeda, yang dapat memengaruhi penempatan konten atau tugas otomatisasi.

Fitur ini meliputi pengambilan metadata kunci dan informasi tata letak untuk halaman tertentu dalam file PDF. API Aspose.PDF Facades menyediakan detail seperti lebar halaman, tinggi, rotasi, dan offset X/Y. Informasi ini penting untuk tugas seperti analisis tata letak halaman, penempatan anotasi, atau pemrosesan PDF otomatis.

1. Buat objek PDF facade.
1. Ambil dimensi halaman dan tata letaknya.
1. Cetak atau simpan nilai yang diambil.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_page_information(infile):

    # Get and display PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)
    page_width = pdf_info.get_page_width(1)
    page_height = pdf_info.get_page_height(1)
    page_rotation = pdf_info.get_page_rotation(1)
    page_x_offset = pdf_info.get_page_x_offset(1)
    page_y_offset = pdf_info.get_page_y_offset(1)

    print(f"Page Width: {page_width}")
    print(f"Page Height: {page_height}")
    print(f"Page Rotation: {page_rotation}")
```
