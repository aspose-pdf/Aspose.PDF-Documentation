---
title: Atur Metadata PDF
linktitle: Atur Metadata PDF
type: docs
weight: 50
url: /id/python-net/set-pdf-metadata/
description: Ubah dan simpan metadata dalam dokumen PDF menggunakan Aspose.PDF for Python via .NET.
lastmod: "2026-06-12"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Memperbarui Metadata PDF Menggunakan Aspose.PDF for Python
Abstract: Panduan ini menjelaskan cara mengubah dan menyimpan metadata dalam dokumen PDF menggunakan Aspose.PDF for Python via .NET. Panduan ini menunjukkan cara memperbarui properti standar PDF seperti judul, subjek, kata kunci, dan pembuat, serta bidang metadata khusus. Pada akhir panduan, Anda akan dapat memperbarui metadata PDF secara programatis dan menyimpan perubahan.
---

Dokumen PDF dapat berisi baik metadata standar (Title, Subject, Keywords, Creator, Author) maupun metadata khusus yang disimpan sebagai properti XMP. Aspose.PDF menyediakan API sederhana untuk mengubah properti ini dalam Python. Panduan ini mencakup cara memperbarui bidang-bidang tersebut dan menyimpan file PDF yang telah dimodifikasi menggunakan the [PdfFileInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileinfo/) kelas.

1. Muat file PDF.
1. Perbarui metadata standar.
1. Tambahkan atau perbarui metadata khusus.
1. Simpan metadata yang diperbarui.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_pdf_metadata(infile, outfile):

    # Get PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)

    # Set PDF metadata
    pdf_info.subject = "Aspose PDF for Python via .NET"
    pdf_info.title = "Aspose PDF for Python via .NET"
    pdf_info.keywords = "Aspose, PDF, Python, .NET"
    pdf_info.creator = "Aspose Team"

    pdf_info.set_meta_info("CustomKey", "CustomValue")

    # pdf_info.save_new_info(outfile)
    # Is obsolete, use save() method instead

    # Save updated metadata
    pdf_info.save(outfile)
```
