---
title: Ekstrak Data XFA
linktitle: Ekstrak Data XFA
type: docs
weight: 50
url: /id/python-net/extract-xfa-data/
description: Contoh ini menjelaskan cara mengekstrak data formulir XFA dari file PDF menggunakan Aspose.PDF for Python via .NET. Contoh ini menunjukkan cara mengikat dokumen PDF berbasis XFA ke facade Form dan mengekspor struktur data internalnya ke aliran file.
lastmod: "2026-06-12"
---

Formulir XFA (XML Forms Architecture) berbeda dari AcroForms tradisional karena data mereka disimpan sebagai XML dalam PDF. Dalam contoh ini, the [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) objek dari [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) modul digunakan untuk mengikat PDF dan mengekstrak data XFA-nya langsung ke sebuah file.

1. Buat sebuah instance dari pdf_facades.Form() untuk mengelola data formulir.
1. Panggil 'bind_pdf()' untuk melampirkan PDF sumber yang berisi formulir XFA.
1. Gunakan 'FileIO()' untuk membuat aliran file yang dapat ditulis.
1. Panggil 'extract_xfa_data()' untuk mengekspor data XML XFA yang disematkan.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Extract XFA Data
def export_xfa_data(infile, outfile):
    """Export XFA form data."""
    # Create Form object
    form = pdf_facades.Form()

    # Bind PDF document
    form.bind_pdf(infile)

    with FileIO(outfile, "w") as stream:
        # Export embedded XFA XML data to the output stream
        form.extract_xfa_data(stream)
```
