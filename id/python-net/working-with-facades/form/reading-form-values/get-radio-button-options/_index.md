---
title: Dapatkan Opsi Tombol Radio
linktitle: Dapatkan Opsi Tombol Radio
type: docs
weight: 20
url: /id/python-net/get-radio-button-options/
description: Artikel ini menunjukkan cara mengambil nilai yang saat ini dipilih dari bidang tombol radio dalam dokumen PDF menggunakan API Aspose.PDF Facades.
lastmod: "2026-06-12"
---

Bidang tombol radio dalam formulir PDF adalah kontrol yang dikelompokkan dimana hanya satu opsi yang dapat dipilih pada satu waktu. Setiap grup memiliki nama bidang, dan setiap opsi memiliki nilai yang sesuai.

1. Buat Objek Form.
1. Hubungkan Dokumen PDF.
1. Ambil Opsi Tombol Radio yang Dipilih.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Get radio button options
def get_radio_button_options(infile):
    """Get radio button options from a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Get radio button options by their names
    field_names = ["WorkType"]
    for field_name in field_names:
        options = pdf_form.get_button_option_current_value(field_name)
        print(f"Options for '{field_name}': {options}")
```
