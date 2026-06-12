---
title: Dapatkan Metadata PDF
linktitle: Dapatkan Metadata PDF
type: docs
weight: 20
url: /id/python-net/get-pdf-metadata/
description: Ekstrak dan tampilkan metadata dari dokumen PDF menggunakan Aspose.PDF for Python.
lastmod: "2026-06-12"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Mengambil Metadata PDF Menggunakan Aspose.PDF for Python.
Abstract: Panduan ini menunjukkan cara mengekstrak dan menampilkan metadata dari dokumen PDF menggunakan Aspose.PDF for Python. Anda akan belajar mengakses properti standar PDF seperti judul, penulis, kata kunci, tanggal pembuatan/perubahan, serta bidang metadata khusus. Selain itu, panduan ini mencakup pemeriksaan validitas PDF, enkripsi, dan status portofolio.
---

Dokumen PDF sering kali berisi metadata berharga yang menggambarkan konten dokumen, kepengarangan, dan izin. Aspose.PDF menyediakan API yang mudah digunakan untuk mengambil properti metadata standar maupun khusus. Potongan kode ini menunjukkan cara menggunakan the [PdfFileInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileinfo/) kelas untuk memeriksa file PDF secara programatis, termasuk contoh langkah demi langkah dalam Python.

1. Muat file PDF.
1. Ambil metadata standar.
1. Periksa status PDF dan keamanan.
1. Ambil metadata khusus.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_pdf_metadata(infile):

    # Get and display PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)
    print(f"Subject: {pdf_info.subject}")
    print(f"Title: {pdf_info.title}")
    print(f"Keywords: {pdf_info.keywords}")
    print(f"Creator: {pdf_info.creator}")
    print(f"Creation Date: {pdf_info.creation_date}")
    print(f"Modification Date: {pdf_info.mod_date}")

    # Check PDF status
    print(f"Is Valid PDF: {pdf_info.is_pdf_file}")
    print(f"Is Encrypted: {pdf_info.is_encrypted}")
    print(f"Has Open Password: {pdf_info.has_open_password}")
    print(f"Has Edit Password: {pdf_info.has_edit_password}")
    print(f"Is Portfolio: {pdf_info.has_collection}")

    # Retrieve and display a specific custom attribute
    reviewer = pdf_info.get_meta_info("Reviewer")
    print(f"Reviewer: {reviewer if reviewer else 'No Reviewer metadata found.'}")
```
