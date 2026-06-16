---
title: Dapatkan Offset Halaman
linktitle: Dapatkan Offset Halaman
type: docs
weight: 20
url: /id/python-net/get-page-offset/
description: Contoh ini menunjukkan cara menggunakan PdfFileInfo untuk mendapatkan offset X dan Y dari halaman tertentu dan mengubahnya menjadi inci untuk analisis tata letak dan posisi yang presisi.
lastmod: "2026-06-12"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dapatkan Offset Halaman PDF menggunakan Python
Abstract: Fungsi 'get_page_offsets' mengekstrak offset horizontal (X) dan vertikal (Y) dari setiap halaman dalam file PDF. Offset ini mewakili posisi konten halaman relatif terhadap asal PDF. Dengan mengubah poin menjadi inci, fungsi ini memberikan ukuran yang presisi dan mudah dibaca manusia yang dapat digunakan untuk penempatan anotasi, gambar, atau teks yang akurat. Fungsi ini mendukung PDF multi-halaman dan ditujukan untuk pengembang yang bekerja pada tata letak PDF, otomatisasi, atau tugas penyelarasan konten.
---

Fungsi 'get_page_offsets' memberikan pengembang offset horizontal (X) dan vertikal (Y) yang tepat dari halaman dalam file PDF. Dalam dokumen PDF, setiap halaman dapat memiliki titik asal internal yang berbeda dari sudut kiri atas halaman, yang dapat memengaruhi posisi teks, gambar, anotasi, atau konten lainnya.

Dengan menggunakan Aspose.PDF Facades, fungsi ini mengekstrak offset dalam satuan poin dan mengubahnya menjadi inci untuk interpretasi yang mudah. Ini mendukung PDF multi‑halaman, menjadikannya cocok untuk alur kerja otomatis yang memerlukan penempatan konten yang tepat.

1. Buat objek facade PDF.
1. Dapatkan jumlah halaman dalam PDF.
1. Lakukan perulangan pada setiap halaman untuk mendapatkan offset.
1. Cetak atau simpan offset.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_page_offsets(infile):
    # Get and display PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)
    page_x_offset = pdf_info.get_page_x_offset(1) / 72.0
    page_y_offset = pdf_info.get_page_y_offset(1) / 72.0
    print(f"Page X Offset: {page_x_offset} inches")
    print(f"Page Y Offset: {page_y_offset} inches")
```
