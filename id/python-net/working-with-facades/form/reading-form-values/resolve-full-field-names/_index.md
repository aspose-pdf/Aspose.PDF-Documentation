---
title: Menyelesaikan Nama Field Lengkap
linktitle: Menyelesaikan Nama Field Lengkap
type: docs
weight: 60
url: /id/python-net/resolve-full-field-names/
description: Contoh ini menunjukkan cara mengambil nama lengkap dari field formulir dalam dokumen PDF menggunakan Aspose.PDF Facades API.
lastmod: "2026-06-12"
---

Dalam formulir PDF, field dapat diatur secara hierarkis, terutama ketika subform digunakan. Setiap field memiliki nama pendek dan nama lengkap. Nama lengkap mewakili jalur lengkap field dalam hierarki formulir dan diperlukan oleh banyak metode API yang memanipulasi atau membaca data formulir.

1. Buat Objek Form.
1. Hubungkan Dokumen PDF.
1. Akses semua nama field formulir.
1. Nama lengkap setiap field diselesaikan menggunakan get_full_field_name().

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Resolve full field names
def resolve_full_field_names(infile):
    """Resolve full field names in a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Resolve full field names
    for field in pdf_form.field_names:
        name = pdf_form.get_full_field_name(field)
        print(f"Full field name: {name}")
```
