---
title: Ubah Ukuran Konten Halaman PDF
linktitle: Ubah Ukuran Konten Halaman PDF
type: docs
weight: 30
url: /id/python-net/resize-pdf-page-contents/
description: Ubah ukuran konten halaman PDF tertentu menggunakan Aspose.PDF for Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ubah Ukuran Konten Halaman PDF secara Programatis di Python
Abstract: Pelajari cara mengubah ukuran konten halaman PDF tertentu menggunakan Aspose.PDF for Python. Contoh ini menunjukkan cara menyesuaikan lebar dan tinggi konten halaman sambil mempertahankan struktur dokumen, memudahkan mengoptimalkan tata letak untuk pencetakan atau penampilan.
---

Menyesuaikan ukuran konten halaman PDF sering diperlukan saat menyiapkan dokumen untuk pencetakan, menempatkan konten ke dalam tata letak tertentu, atau menstandarisasi format halaman di seluruh dokumen. Dengan menggunakan Aspose.PDF for Python, pengembang dapat mengubah ukuran konten halaman yang dipilih secara programatis tanpa harus mengedit dokumen secara manual.

Artikel ini menunjukkan cara menggunakan metode \u0027resize_contents\u0027 dari [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) kelas untuk mengubah dimensi konten halaman untuk halaman tertentu dalam file PDF. Dengan menentukan lebar dan tinggi target, konten pada halaman yang dipilih diubah ukurannya secara sesuai.

1. Buat Objek PdfFileEditor.
1. Ubah Ukuran Konten Halaman.

Parameter:

- [1, 3] – daftar nomor halaman yang kontennya akan diubah ukurannya.
- 400 – lebar baru konten halaman (dalam point).
- 750 – tinggi baru konten halaman (dalam point).

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Resize PDF Page Contents
def resize_pdf_page_contents(infile, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()

    if not pdf_editor.resize_contents(
        FileIO(infile), FileIO(outfile, "w"), [1, 3], 400, 750
    ):
        raise Exception("Failed to resize PDF page contents.")
```
