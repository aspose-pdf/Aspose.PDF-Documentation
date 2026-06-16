---
title: Ratakan Semua Field
linktitle: Ratakan Semua Field
type: docs
weight: 10
url: /id/python-net/flatten-all-fields/
description: Contoh ini menunjukkan cara meratakan semua field formulir dalam PDF menggunakan Aspose.PDF for Python via .NET. Ini memperlihatkan cara mengikat dokumen PDF, mengonversi setiap elemen formulir interaktif menjadi konten halaman statis, dan menyimpan file yang telah selesai.
lastmod: "2026-06-12"
---

Meratakan menghapus interaktivitas dari formulir PDF dengan menggabungkan nilai field secara langsung ke dalam tata letak dokumen. Dalam contoh ini, the [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) fasad dari [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) digunakan untuk mengikat PDF sumber dan menerapkan metode flatten_all_fields(), yang mengonversi semua field menjadi konten yang tidak dapat diedit.

1. Inisialisasi pdf_facades.Form() untuk berinteraksi dengan bidang formulir PDF.
1. Panggil 'bind_pdf()' untuk melampirkan dokumen sumber.
1. Panggil 'flatten_all_fields()' untuk mengonversi semua field interaktif menjadi konten statis.
1. Simpan Document yang diperbarui.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Flatten all fields
def flatten_all_fields(infile, outfile):
    """Flatten all fields in a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Flatten all fields in the PDF document
    pdf_form.flatten_all_fields()

    # Save updated PDF
    pdf_form.save(outfile)
```
