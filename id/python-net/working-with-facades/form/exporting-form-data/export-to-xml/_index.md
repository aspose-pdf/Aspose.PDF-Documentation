---
title: Ekspor ke XML
linktitle: Ekspor ke XML
type: docs
weight: 40
url: /id/python-net/export-to-xml/
description: Contoh ini menunjukkan cara mengekspor data formulir PDF ke file XML menggunakan Aspose.PDF for Python via .NET. Ini menunjukkan cara memuat dokumen PDF, mengakses bidang formulirnya melalui Form facade, dan menyimpan data yang diekstrak sebagai XML terstruktur menggunakan Form Class.
lastmod: "2026-06-12"
---

Mengekspor data formulir memungkinkan pengembang untuk menggunakan kembali informasi yang disimpan dalam PDF AcroForms tanpa menyalin nilai bidang secara manual. Dalam contoh ini, sebuah [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) objek dibuat dari aspose.pdf. Dalam modul facades, PDF sumber diikat kepadanya, dan data formulir ditulis ke dalam aliran XML.

1. Buat Objek Form. Inisialisasi pdf_facades.Form() untuk mengakses dan mengelola bidang formulir.
1. Gunakan 'bind_pdf()' untuk melampirkan dokumen PDF sumber ke instance Form.
1. Buat aliran file yang dapat ditulis menggunakan 'FileIO()'.
1. Panggil 'export_xml()' untuk mengekstrak semua nilai bidang formulir dan menuliskannya ke dalam file XML.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Export Data to XML
def export_pdf_form_data_to_xml(infile, datafile):
    """Export PDF form data to XML file."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Open XML file as stream
    with FileIO(datafile, "w") as xml_output_stream:
        # Export data from PDF form fields to XML
        pdf_form.export_xml(xml_output_stream)
```
