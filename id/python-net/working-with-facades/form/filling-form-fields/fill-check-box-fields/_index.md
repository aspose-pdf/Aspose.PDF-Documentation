---
title: Isi Field Kotak Centang
linktitle: Isi Field Kotak Centang
type: docs
weight: 20
url: /id/python-net/fill-check-box-fields/
description: Contoh ini menunjukkan cara mengisi field kotak centang secara programatik dalam formulir PDF menggunakan Aspose.PDF for Python via .NET. Ini memperlihatkan cara mengaitkan dokumen PDF, memperbarui nilai kotak centang berdasarkan nama field, dan menyimpan file yang telah dimodifikasi.
lastmod: "2026-06-12"
---

Kotak centang biasanya digunakan dalam formulir PDF untuk mewakili pilihan biner seperti langganan atau konfirmasi persetujuan. Dalam contoh ini, the [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) fasad dari [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) digunakan untuk mengakses field formulir dan menetapkan nilai mereka ke keadaan terpilih. Setelah memperbarui kotak centang, PDF yang telah diisi disimpan sebagai dokumen baru.

1. Inisialisasi 'pdf_facades.Form()' untuk mengelola interaksi field formulir.
1. Gunakan 'bind_pdf()' untuk melampirkan PDF sumber yang berisi bidang kotak centang.
1. Panggil 'fill_field()' untuk menandai bidang seperti 'subscribe_newsletter' dan 'accept_terms' sebagai terpilih.
1. Simpan Document yang diperbarui.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill Check Box Fields
def fill_check_box_fields(infile, outfile):
    """Fill check box fields in PDF form."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill check box fields by name
    pdf_form.fill_field("subscribe_newsletter", "Yes")
    pdf_form.fill_field("accept_terms", "Yes")

    # Save updated PDF
    pdf_form.save(outfile)
```
