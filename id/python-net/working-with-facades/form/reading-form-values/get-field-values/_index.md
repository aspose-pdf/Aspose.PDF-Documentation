---
title: Dapatkan Nilai Field
linktitle: Dapatkan Nilai Field
type: docs
weight: 50
url: /id/python-net/get-field-values/
description: Mengambil Nilai Field dari Form PDF dengan Aspose.PDF Facades menggunakan Kelas Form.
lastmod: "2026-06-12"
---

Potongan kode ini menunjukkan cara mengambil nilai saat ini dari field formulir dalam dokumen PDF menggunakan API Aspose.PDF Facades. The [get_field()](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/#methods) metode memungkinkan Anda mengakses data yang dimasukkan ke dalam field teks, kotak centang, tombol radio, dan elemen AcroForm lainnya secara programatik.

1. Ikat PDF ke objek Form.
1. Tentukan nama bidang yang ingin Anda baca.
1. Ambil nilai setiap bidang menggunakan get_field().

```python

    from io import FileIO
    import sys
    from os import path
    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir


    # Get field values
    def get_field_values(infile):
        """Get field values from a PDF document."""
        # Create Form object
        pdf_form = pdf_facades.Form()

        # Bind PDF document
        pdf_form.bind_pdf(infile)

        # Get field values by their names
        field_names = ["First Name", "Last Name"]
        for field_name in field_names:
            value = pdf_form.get_field(field_name)
            print(f"Value of '{field_name}': {value}")
```