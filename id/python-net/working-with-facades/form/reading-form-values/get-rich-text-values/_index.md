---
title: Dapatkan Nilai Teks Kaya
linktitle: Dapatkan Nilai Teks Kaya
type: docs
weight: 40
url: /id/python-net/get-rich-text-values/
description: Bagian ini menjelaskan cara mengambil konten teks kaya dari sebuah field formulir dalam dokumen PDF menggunakan Aspose.PDF Facades API. Tidak seperti field teks biasa, field teks kaya dapat berisi konten yang diformat seperti teks tebal, font yang berbeda, warna, dan gaya paragraf.
lastmod: "2026-06-12"
---

Formulir PDF dapat menyertakan field teks yang mendukung pemformatan teks kaya. Field-field ini dapat menyimpan konten dengan atribut gaya selain nilai teks biasa.

1. Buat Objek Form.
1. Hubungkan Dokumen PDF.
1. Ambil Nilai Teks Kaya.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Get rich text values
def get_rich_text_values(infile):
    """Get rich text values from a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Get rich text values by their names
    field_names = ["Summary"]
    for field_name in field_names:
        rich_text_value = pdf_form.get_rich_text(field_name)
        print(f"Rich text value of '{field_name}': {rich_text_value}")
```
