---
title: Tambahkan Stempel ke PDF
linktitle: Tambahkan Stempel ke PDF
type: docs
weight: 40
url: /id/python-net/add-stamp/
description: Pelajari cara menambahkan stempel ke halaman PDF menggunakan PdfFileStamp di Python.
lastmod: "2026-06-12"
TechArticle: true
AlternativeHeadline: Tambahkan Cap Teks ke PDF dengan Python
Abstract: Artikel ini menjelaskan cara menambahkan konten stempel ke dokumen PDF dengan Aspose.PDF for Python via .NET menggunakan fasad PdfFileStamp. Artikel ini menunjukkan cara membuat stempel, menempatkannya pada halaman, mengontrol rotasi dan opasitas, serta menyimpan PDF yang diperbarui.
---

Aspose.PDF for Python via .NET menyediakan [PdfFileStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilestamp/) fasad untuk menambahkan konten berulang ke halaman PDF. Selain header, footer, dan nomor halaman, Anda dapat menggunakannya untuk menempatkan stempel berbasis teks pada setiap halaman dokumen.

## Tambahkan stempel ke PDF

Setelah stempel dikonfigurasi, hubungkan PDF input ke `PdfFileStamp`, tambahkan stempel, dan simpan file output. Ini menerapkan stempel yang dikonfigurasi di seluruh dokumen.

```python
import sys
from os import path

import aspose.pdf.facades as pdf_facades

CURRENT_DIR = path.dirname(__file__)
EXAMPLES_DIR = path.abspath(path.join(CURRENT_DIR, "..", ".."))
if EXAMPLES_DIR not in sys.path:
    sys.path.insert(0, EXAMPLES_DIR)

from config import initialize_data_dir, set_license


def add_stamp_to_pdf(infile: str, image_file: str, outfile: str) -> None:
    """Add an image stamp to a PDF file."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_image(image_file)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```
