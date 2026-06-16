---
title: Gabungkan Jumlah Besar File PDF
linktitle: Gabungkan Jumlah Besar File PDF
type: docs
weight: 10
url: /id/python-net/concatenate-large-number-files/
description: Gabungkan sejumlah besar file PDF secara efisien menggunakan Aspose.PDF for Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gabungkan File PDF Besar di Python Menggunakan Buffer Disk
Abstract: Pelajari cara menggabungkan sejumlah besar file PDF secara efisien menggunakan Aspose.PDF for Python. Contoh ini menunjukkan cara mengaktifkan buffer disk untuk menangani PDF besar tanpa menghabiskan memori sistem, memastikan penggabungan yang mulus dari banyak file.
---

Saat bekerja dengan koleksi besar file PDF, konsumsi memori dapat menjadi kendala selama penggabungan. Menggunakan Aspose.PDF for Python, Anda dapat mengaktifkan buffer disk di dalam [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) kelas untuk menggabungkan banyak PDF secara efisien. Metode concatenate menggabungkan file input menjadi satu PDF sementara buffer disk mencegah penggunaan memori yang tinggi. Pendekatan ini ideal untuk memproses dokumen dalam jumlah besar, menghasilkan laporan otomatis, atau mengkonsolidasikan arsip PDF besar.

1. Buat Objek PdfFileEditor.
1. Gabungkan beberapa file PDF.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def concatenate_large_number_files(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.use_disk_buffer = True  # Enable disk buffering for large files
    pdf_editor.concatenate(files_to_merge, output_file)
```
