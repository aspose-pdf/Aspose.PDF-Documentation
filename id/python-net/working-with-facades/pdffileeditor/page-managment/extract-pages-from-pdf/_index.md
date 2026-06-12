---
title: Ekstrak Halaman dari PDF
linktitle: Ekstrak Halaman dari PDF
type: docs
weight: 30
url: /id/python-net/extract-pages-from-pdf/
description: Ekstrak halaman terpilih dari dokumen PDF menggunakan Aspose.PDF for Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ekstrak Halaman Spesifik dari Dokumen PDF dalam Python
Abstract: Pelajari cara mengekstrak halaman terpilih dari dokumen PDF menggunakan Aspose.PDF for Python. Contoh ini menunjukkan cara membuat PDF baru yang hanya berisi halaman yang Anda butuhkan, memungkinkan pembuatan dokumen khusus dan manipulasi tingkat halaman.
---

Mengekstrak halaman dari PDF berguna ketika Anda perlu membuat subset dari sebuah dokumen, membagikan konten tertentu saja, atau mengatur ulang PDF untuk presentasi, laporan, atau pencetakan. Dengan menggunakan Aspose.PDF for Python, pengembang dapat mengekstrak halaman secara programatis dari file PDF dan menyimpannya sebagai dokumen baru.

Pelajari cara menggunakan metode extract dari [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) kelas. Dengan menentukan daftar halaman yang akan diekstrak, Anda dapat membuat PDF baru yang hanya berisi halaman yang dipilih sambil mempertahankan konten dan format asli.

1. Buat Objek PdfFileEditor.
1. Tentukan Halaman untuk Diekstrak.
1. Ekstrak Halaman.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


# Extract Pages from PDF
def extract_pages_from_pdf(infile, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()

    # Define the page numbers to be extracted (1-based index)
    pages_to_extract = [1, 4, 3]

    # Extract the specified pages from the PDF document and save to a new PDF document
    pdf_editor.extract(infile, pages_to_extract, outfile)
```
