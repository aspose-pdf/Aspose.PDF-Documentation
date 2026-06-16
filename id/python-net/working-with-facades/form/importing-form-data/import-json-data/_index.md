---
title: Impor Data JSON
linktitle: Impor Data JSON
type: docs
weight: 30
url: /id/python-net/import-json-data/
description: Contoh ini menunjukkan cara mengimpor data bidang formulir dari file JSON ke dalam formulir PDF menggunakan Aspose.PDF for Python via .NET. Ini menunjukkan cara mengaitkan dokumen PDF, membaca data JSON terstruktur melalui aliran file, dan secara otomatis mengisi bidang formulir yang cocok.
lastmod: "2026-06-12"
---

JSON banyak digunakan untuk menyimpan dan mentransfer data terstruktur antara sistem. Dalam contoh ini, the [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) fasad dari [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) modul digunakan untuk mengaitkan formulir PDF dan mengimpor nilai bidang dari file JSON eksternal. Setelah proses impor, dokumen yang diperbarui disimpan sebagai PDF baru.

1. Inisialisasi pdf_facades.Form() untuk berinteraksi dengan bidang formulir PDF.
1. Panggil 'bind_pdf()' untuk melampirkan templat formulir PDF.
1. Gunakan 'FileIO()' untuk membaca file JSON yang berisi nilai formulir.
1. Panggil 'import_json()' untuk mengisi bidang PDF menggunakan pasangan kunci–nilai JSON.
1. Simpan PDF yang diperbarui.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Import from JSON
def import_json_to_pdf_form(infile, datafile, outfile):
    """Import form data from JSON file into PDF form fields."""
    # Create Form object
    form = pdf_facades.Form()

    # Bind PDF document
    form.bind_pdf(infile)

    # Open JSON file as stream
    with FileIO(datafile, "r") as json_stream:
        # Import data from JSON into PDF form fields
        form.import_json(json_stream)

    # Save updated PDF
    form.save(outfile)
```
