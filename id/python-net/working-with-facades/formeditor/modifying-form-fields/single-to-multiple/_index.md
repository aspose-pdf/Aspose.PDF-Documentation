---
title: Bidang Satu Baris ke Bidang Multi Baris
linktitle: Bidang Satu Baris ke Bidang Multi Baris
type: docs
weight: 80
url: /id/python-net/single-to-multiple/
description: Ubah bidang teks satu baris menjadi bidang multi baris dalam dokumen PDF menggunakan Aspose.PDF for Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ubah Bidang Teks Satu Baris menjadi Bidang Multi Baris dalam PDF Menggunakan Python
Abstract: Contoh ini menunjukkan cara mengubah bidang teks satu baris menjadi bidang multi baris dalam dokumen PDF menggunakan Aspose.PDF for Python. Kode tersebut memuat formulir PDF yang ada, memodifikasi bidang yang ditentukan agar memungkinkan beberapa baris teks, dan menyimpan dokumen yang telah diperbarui.
---

Formulir PDF kadang-kadang berisi bidang teks yang dirancang untuk input satu baris, yang mungkin tidak cukup untuk jenis data tertentu. Dengan Aspose.PDF for Python, pengembang dapat dengan mudah mengubah bidang tersebut menjadi bidang teks multi baris tanpa harus membuat ulang.

Menggunakan [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) class, pengembang dapat memodifikasi bidang teks yang ada tanpa mempengaruhi posisinya atau properti lainnya.

1. Muat dokumen PDF yang ada.
1. Buat instance FormEditor.
1. Ikat dokumen PDF ke editor.
1. Ubah bidang yang dipilih menjadi multi-baris.
1. Simpan dokumen yang telah diperbarui.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def single2multiple(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Change a single-lined text field to a multiple-lined one
    form_editor.single_2_multiple("City")
    # Save updated document
    form_editor.save(outfile)
```

