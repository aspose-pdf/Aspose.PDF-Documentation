---
title: Bekerja dengan Formulir XFA
linktitle: Formulir XFA
type: docs
weight: 20
url: /id/python-net/xfa-forms/
description: Aspose.PDF for Python via .NET API memungkinkan Anda bekerja dengan bidang XFA dan XFA Acroform di dokumen PDF.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Konversi XFA-ke-Acroform

{{% alert color="primary" %}}

Coba secara online
Anda dapat memeriksa kualitas konversi Aspose.PDF dan melihat hasilnya secara online di tautan ini: [products.aspose.app/pdf/xfa/acroform](https://products.aspose.app/pdf/xfa/acroform)

{{% /alert %}}

Potongan kode berikut menunjukkan cara mengonversi formulir XFA (XML Forms Architecture) dinamis menjadi AcroForm standar.

**Langkah utama meliputi:**

1. Memuat dokumen PDF input.
1. Mengubah tipe formulir menjadi STANDARD.
1. Menyimpan PDF yang dikonversi ke file baru.

Konversi ini memungkinkan kompatibilitas yang lebih baik dan penanganan formulir yang konsisten di berbagai pembaca PDF dan aplikasi.

```python
import aspose.pdf as ap
import sys
from os import path

def convert_dynamic_xfa_to_acroform(infile: str, outfile: str):
    """Convert dynamic XFA form to standard AcroForm."""
    with ap.Document(infile) as document:
        document.form.type = ap.forms.FormType.STANDARD
        document.save(outfile)
```

## Penggunaan IgnoreNeedsRendering

Contoh ini menunjukkan cara mengonversi formulir XFA dinamis menjadi AcroForm standar menggunakan Aspose.PDF for Python. Kode memeriksa apakah PDF input berisi formulir XFA dan menimpa rendering jika diperlukan. Selanjutnya, kode mengatur jenis formulir menjadi STANDARD dan menyimpan PDF yang diperbarui.

```python
import aspose.pdf as ap
import sys
from os import path

def convert_xfa_form_with_ignore_needs_rendering(infile: str, outfile: str):
    """Convert XFA form ignoring needs rendering flag."""
    with ap.Document(infile) as document:
        if not document.form.needs_rendering and document.form.has_xfa:
            document.form.ignore_needs_rendering = True
        document.form.type = ap.forms.FormType.STANDARD
        document.save(outfile)
```
