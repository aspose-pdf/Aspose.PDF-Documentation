---
title: Ekspor ke XFDF
linktitle: Ekspor ke XFDF
type: docs
weight: 20
url: /id/python-net/export-to-xfdf/
description: Contoh ini menunjukkan cara mengekspor data bidang formulir PDF ke file XFDF (XML Forms Data Format) menggunakan Aspose.PDF for Python via .NET. Ini mendemonstrasikan cara memuat formulir PDF, mengakses bidangnya melalui fasad Form, dan menyimpan nilai yang diekstrak ke dalam stream XFDF.
lastmod: "2026-06-12"
---

XFDF adalah representasi XML dari data formulir PDF yang memungkinkan pengembang mentransfer nilai bidang formulir secara independen dari dokumen asli. Dalam contoh ini, the [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) object from [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) digunakan untuk mengikat PDF sumber dan mengekspor datanya ke dalam file XFDF yang terstruktur.

1. Inisialisasi pdf_facades.Form() untuk mengelola data formulir PDF.
1. Panggil 'bind_pdf()' untuk melampirkan dokumen PDF sumber.
1. Gunakan 'open()' untuk membuat aliran biner yang dapat ditulis.
1. Ekspor Data Formulir. Panggil 'export_xfdf()' untuk mengekstrak dan menyimpan nilai bidang formulir dalam format XFDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Export Data to XFDF
def export_pdf_form_to_xfdf(infile, outfile):
    """Export PDF form data to XFDF file."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Create XFDF file stream
    with open(outfile, "wb") as xfdf_output_stream:
        # Export form data to XFDF file
        pdf_form.export_xfdf(xfdf_output_stream)
```
