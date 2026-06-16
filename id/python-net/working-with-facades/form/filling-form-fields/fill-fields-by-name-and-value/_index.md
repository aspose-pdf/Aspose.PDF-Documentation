---
title: Isi Bidang Berdasarkan Nama dan Nilai
linktitle: Isi Bidang Berdasarkan Nama dan Nilai
type: docs
weight: 60
url: /id/python-net/fill-fields-by-name-and-value/
description: Artikel ini menunjukkan cara mengisi secara dinamis beberapa bidang formulir PDF berdasarkan nama dan nilai menggunakan Aspose.PDF for Python via .NET. Alih-alih mengatur setiap bidang secara individual, artikel ini menggunakan struktur kamus untuk memetakan nama bidang ke nilai dan mengisinya dalam sebuah loop.
lastmod: "2026-06-12"
---

Mengisi bidang formulir menggunakan koleksi nama–nilai memungkinkan pengembang untuk membuat solusi yang dapat diskalakan dan fleksibel untuk otomatisasi formulir PDF. Dalam contoh ini, the [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) facade dari [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) digunakan untuk mengikat dokumen PDF dan mengulangi melalui kamus data bidang. Setiap entri diterapkan menggunakan metode ‘fill_field’, memungkinkan pembaruan massal yang efisien pada bidang formulir.

1. Inisialisasi ‘pdf_facades.Form()’ untuk bekerja dengan bidang formulir interaktif.
1. Gunakan 'bind_pdf()' untuk melampirkan dokumen PDF sumber.
1. Buat kamus yang berisi nama bidang dan nilai yang ingin Anda sisipkan.
1. Iterasi melalui kamus dan panggil 'fill_field()' untuk setiap entri.
1. Simpan Document yang diperbarui.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill Fields by Name and Value
def fill_fields_by_name_and_value(infile, outfile):
    """Fill PDF form fields by name and value."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill fields by name and value
    fields = {
        "name": "Jane Smith",
        "address": "456 Elm St, Othertown, USA",
        "email": "jane.smith@example.com",
    }
    for field_name, value in fields.items():
        pdf_form.fill_field(field_name, value)

    # Save updated PDF using outfile
    pdf_form.save(outfile)
```
