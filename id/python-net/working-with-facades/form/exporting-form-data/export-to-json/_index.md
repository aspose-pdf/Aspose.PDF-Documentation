---
title: Ekspor ke JSON
linktitle: Ekspor ke JSON
type: docs
weight: 30
url: /id/python-net/export-to-json/
description: Contoh ini menunjukkan cara mengekspor nilai field formulir PDF ke file JSON menggunakan Aspose.PDF for Python via .NET. Ini menjelaskan cara memuat formulir PDF, mengakses field-nya melalui fasad Form, dan menyimpan data yang diekstrak dalam format JSON terstruktur.
lastmod: "2026-06-12"
---

JSON adalah format data yang banyak digunakan yang memungkinkan pertukaran mulus antara aplikasi dan layanan. Pada contoh ini, [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) objek dari [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) modul digunakan untuk mengikat file PDF dan mengekspor nilai field formulirnya ke dalam struktur JSON yang dapat dibaca.

1. Inisialisasi pdf_facades.Form() untuk bekerja dengan field formulir.
1. Gunakan 'bind_pdf()' untuk melampirkan dokumen PDF sumber.
1. Buat aliran yang dapat ditulis menggunakan 'FileIO()'.
1. Panggil 'export_json()' untuk mengekstrak nilai bidang formulir dan menyimpannya dalam JSON yang diformat.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Export Data to JSON
def export_form_to_json(infile, outfile):
    """Export PDF form field values to JSON file."""
    # Create Form object
    form = pdf_facades.Form()

    # Bind PDF document
    form.bind_pdf(infile)

    # Create JSON file stream
    with FileIO(outfile, "w") as json_stream:
        # Export form field values to JSON
        form.export_json(json_stream, indented=True)
```
