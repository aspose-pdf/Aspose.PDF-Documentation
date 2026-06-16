---
title: Daftar Stempel
linktitle: Daftar Stempel
type: docs
weight: 70
url: /id/python-net/list-stamps/
description: Contoh ini memuat PDF, mengambil semua stempel dari halaman 1, mencetaknya, dan menampilkan pesan jika tidak ada stempel yang ditemukan.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Daftar Anotasi Stempel Karet dalam PDF Menggunakan PdfContentEditor di Python
Abstract: Contoh ini menunjukkan cara mengambil dan mendaftar anotasi stempel karet dari dokumen PDF menggunakan Aspose.PDF for Python via the Facades API. Ini memperlihatkan cara mengakses stempel pada halaman tertentu dan menampilkan detailnya.
---

Saat bekerja dengan PDF yang beranotasi, Anda mungkin perlu memeriksa stempel karet yang ada sebelum memodifikasi atau menghapusnya. Metode 'get_stamps()' memungkinkan Anda mengambil semua stempel yang ditempatkan pada halaman tertentu. Anda kemudian dapat mengiterasi hasilnya dan memprosesnya secara programatik.

1. Buat sebuah [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instansi.
1. Hubungkan dokumen PDF input.
1. Ambil semua stempel dari halaman 1.
1. Iterasi melalui koleksi stempel.
1. Cetak setiap stempel.
1. Tampilkan pesan jika tidak ada stempel.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def list_stamps(infile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # List all stamps on page 1
    stamps = content_editor.get_stamps(1)

    count = 0
    for stamp in stamps:
        count += 1
        print(f"Stamp {count}: {stamp}")

    if count == 0:
        print("No stamps found")
```
