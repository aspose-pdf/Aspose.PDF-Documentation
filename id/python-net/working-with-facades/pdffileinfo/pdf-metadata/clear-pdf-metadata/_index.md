---
title: Bersihkan Metadata PDF
linktitle: Bersihkan Metadata PDF
type: docs
weight: 10
url: /id/python-net/clear-pdf-metadata/
description: Hapus semua metadata dari dokumen PDF menggunakan Aspose.PDF for Python via .NET.
lastmod: "2026-06-12"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Membersihkan Metadata PDF Menggunakan Aspose.PDF for Python
Abstract: Panduan ini menjelaskan cara menghapus semua metadata dari dokumen PDF menggunakan Aspose.PDF for Python via .NET. Anda akan belajar menghapus baik bidang metadata standar maupun kustom serta menyimpan PDF yang telah dibersihkan. Ini berguna untuk privasi, keamanan, atau menyiapkan PDF untuk rilis publik.
---

PDF sering berisi metadata seperti judul, penulis, kata kunci, tanggal pembuatan, dan bidang kustom. Dalam beberapa skenario, Anda mungkin ingin menghapus semua metadata dari PDF, misalnya sebelum distribusi atau pengarsipan. Aspose.PDF menyediakan metode clear_info() untuk menghapus semua metadata dengan mudah. Setelah dibersihkan, Anda dapat menyimpan PDF menggunakan metode save().

1. Muat file PDF.
1. Hapus semua metadata.
1. Simpan PDF bersih.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def clear_pdf_metadata(infile, outfile):

    # Get PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)

    # Clear PDF metadata
    pdf_info.clear_info()

    # Save updated metadata
    pdf_info.save(outfile)
```
