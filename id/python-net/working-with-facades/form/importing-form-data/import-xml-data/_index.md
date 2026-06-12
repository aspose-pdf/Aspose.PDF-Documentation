---
title: Impor Data XML
linktitle: Impor Data XML
type: docs
weight: 40
url: /id/python-net/import-xml-data/
description: Contoh ini menunjukkan cara mengimpor data formulir dari file XML ke dalam bidang formulir PDF menggunakan Aspose.PDF for Python via .NET. Ini menunjukkan cara mengikat dokumen PDF, membaca data XML terstruktur melalui aliran file, dan mengisi bidang formulir yang sesuai secara otomatis.
lastmod: "2026-06-12"
---

XML biasanya digunakan untuk menyimpan data formulir terstruktur, menjadikannya format praktis untuk mentransfer nilai antar sistem. Dalam contoh ini, the [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) facade dari [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) digunakan untuk memuat formulir PDF dan menerapkan nilai bidang langsung dari file XML. Setelah mengimpor data, PDF yang diperbarui disimpan sebagai dokumen baru.

1. Inisialisasi pdf_facades.Form() untuk berinteraksi dengan bidang formulir PDF.
1. Panggil 'bind_pdf()' untuk melampirkan templat formulir PDF.
1. Gunakan 'FileIO()' untuk mengakses file XML yang berisi data formulir.
1. Panggil 'import_xml()' untuk mengisi bidang PDF dengan nilai dari file XML.
1. Simpan PDF yang diperbarui.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Import data from XML
def import_xml_to_pdf_fields(infile, datafile, outfile):
    """Import form data from XML file into PDF form fields."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Open XML file as stream
    with FileIO(datafile, "r") as xml_input_stream:
        # Import data from XML into PDF form fields
        pdf_form.import_xml(xml_input_stream)

    # Save updated PDF
    pdf_form.save(outfile)
```
