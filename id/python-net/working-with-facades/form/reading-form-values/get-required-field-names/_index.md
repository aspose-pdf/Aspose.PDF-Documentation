---
title: Dapatkan Nama Field yang Diperlukan
linktitle: Dapatkan Nama Field yang Diperlukan
type: docs
weight: 30
url: /id/python-net/get-required-field-names/
description: Contoh ini menunjukkan cara mengidentifikasi dan mengambil nama-nama field formulir yang wajib dalam dokumen PDF menggunakan Aspose.PDF Facades API.
lastmod: "2026-06-12"
---

Formulir PDF dapat berisi field wajib yang harus diisi pengguna sebelum pengiriman. Field ini biasanya ditandai sebagai wajib dalam properti form.

1. Buat Objek Form.
1. Hubungkan Dokumen PDF.
1. Akses semua nama field menggunakan 'pdf_form.field_names'.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Get required field names
def get_required_field_names(infile):
    """Get required field names from a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Get required field names
    for field in pdf_form.field_names:
        if pdf_form.is_required_field(field):
            print(f"Required field: {field}")
```
