---
title: Hapus Item Daftar
linktitle: Hapus Item Daftar
type: docs
weight: 40
url: /id/python-net/del-list-item/
description:
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Hapus Item dari Kolom Kotak Daftar PDF Menggunakan Python
Abstract: Contoh ini menunjukkan cara menghapus sebuah item dari bidang kotak daftar dalam dokumen PDF menggunakan Aspose.PDF for Python. Kode membuka PDF yang ada, menghapus item tertentu dari bidang kotak daftar, dan menyimpan dokumen yang telah diperbarui.
---

Bidang kotak daftar dalam PDF memungkinkan pengguna untuk memilih satu atau beberapa opsi yang telah ditentukan. Dengan menggunakan Aspose.PDF for Python, pengembang dapat secara programatis menghapus item dari bidang-bidang ini.

Artikel ini menjelaskan cara menghapus item 'UK' dari bidang kotak daftar bernama 'Country', memastikan bidang tersebut hanya berisi opsi yang diinginkan.

The [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) kelas menyediakan metode 'del_list_item' untuk menghapus item tertentu dari bidang kotak daftar.

1. Buka formulir PDF yang ada.
1. Buat objek FormEditor.
1. Ikat dokumen PDF ke FormEditor.
1. Hapus item "UK" dari bidang kotak daftar "Country".
1. Simpan dokumen yang telah diperbarui.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def del_list_item(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Delete list item from list box field
    form_editor.del_list_item("Country", "UK")
    # Save updated document
    form_editor.save(outfile)
```

