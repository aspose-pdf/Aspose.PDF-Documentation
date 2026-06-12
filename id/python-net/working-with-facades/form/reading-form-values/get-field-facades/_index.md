---
title: Dapatkan Facade Bidang
linktitle: Dapatkan Facade Bidang
type: docs
weight: 10
url: /id/python-net/get-field-facades/
description: Contoh ini menunjukkan cara membaca nilai dari bidang formulir tertentu dalam dokumen PDF menggunakan Aspose.PDF Facades API.
lastmod: "2026-06-12"
---

Formulir PDF berisi bidang tempat pengguna dapat memasukkan data, seperti kotak teks, kotak centang, atau tombol radio. Untuk memproses formulir ini secara programatik, seringkali diperlukan untuk mengambil nilai saat ini dari bidang-bidang tersebut.

1. Buat objek Form.
1. Hubungkan dokumen PDF ke objek form.
1. Ambil Nilai Bidang.

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