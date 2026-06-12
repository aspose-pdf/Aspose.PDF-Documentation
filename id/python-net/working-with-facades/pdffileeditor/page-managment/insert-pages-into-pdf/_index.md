---
title: Sisipkan Halaman ke PDF
linktitle: Sisipkan Halaman ke PDF
type: docs
weight: 40
url: /id/python-net/insert-pages-into-pdf/
description: Sisipkan halaman dari satu PDF ke PDF lain menggunakan Aspose.PDF for Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Sisipkan Halaman dari PDF Lain ke PDF yang Ada dalam Python
Abstract: Pelajari cara menyisipkan halaman dari satu PDF ke PDF lain menggunakan Aspose.PDF for Python. Contoh ini menunjukkan cara menambahkan halaman yang dipilih dari PDF sekunder ke posisi spesifik dalam dokumen asli, menghasilkan PDF gabungan dengan penempatan halaman yang tepat.
---

Menyisipkan halaman ke PDF yang sudah ada merupakan kebutuhan umum saat menggabungkan dokumen, menambahkan konten, atau menyusun ulang laporan. Dengan menggunakan Aspose.PDF for Python, pengembang dapat secara programatis menyisipkan halaman dari satu PDF ke PDF lain pada lokasi yang ditentukan.

Artikel ini menunjukkan cara menggunakan metode insert dari [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) kelas. Dengan menentukan nomor halaman yang akan disisipkan dan lokasi target, Anda dapat menggabungkan konten dari PDF yang berbeda sambil mempertahankan format dan struktur asli.

1. Buat objek PdfFileEditor.
1. Tentukan Posisi Sisipan dan Halaman.
1. Sisipkan Halaman.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


# Insert Pages into PDF
def insert_pages_into_pdf(infile, sample_file, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()

    # Define the page number where new pages will be inserted (1-based index)
    insert_page_number = 2

    pdf_editor.insert(infile, insert_page_number, sample_file, [1, 2], outfile)
```
