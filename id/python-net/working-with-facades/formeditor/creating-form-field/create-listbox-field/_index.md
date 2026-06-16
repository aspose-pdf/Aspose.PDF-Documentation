---
title: Buat bidang ListBox
linktitle: Buat bidang ListBox
type: docs
weight: 30
url: /id/python-net/create-listbox-field/
description: Pelajari cara menambahkan bidang formulir ListBox secara programatis ke dokumen PDF menggunakan Aspose.PDF for Python. Panduan ini menunjukkan cara menyisipkan bidang ListBox, mendefinisikan item yang dapat dipilih, dan menyimpan file PDF yang diperbarui.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Buat bidang ListBox dalam PDF menggunakan Aspose.PDF for Python
Abstract: Formulir PDF memungkinkan pengguna berinteraksi dengan dokumen dengan memilih opsi, memasukkan data, dan mengirimkan informasi secara digital. Bidang ListBox memungkinkan pengguna memilih satu atau beberapa nilai dari daftar opsi yang terlihat. Dalam tutorial ini, Anda akan belajar cara membuat bidang ListBox dalam PDF menggunakan kelas FormEditor di Aspose.PDF for Python dan mengisinya dengan item yang telah ditentukan sebelumnya.
---

Formulir PDF biasanya digunakan untuk aplikasi, survei, dan dokumen pendaftaran. Bidang ListBox menampilkan beberapa opsi secara bersamaan, memudahkan pengguna meninjau dan memilih item dari daftar.

The [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) kelas menyediakan fungsionalitas untuk menambahkan berbagai jenis bidang interaktif, termasuk elemen ListBox.

1. Muat dokumen PDF yang ada.
1. Definisikan daftar opsi yang dapat dipilih.
1. Tambahkan bidang ListBox ke halaman tertentu.
1. Tetapkan nilai default yang dipilih.
1. Simpan dokumen PDF yang diperbarui.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_listbox_field(infile, outfile):
    """Create ListBox field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add ListBox field to PDF form
    pdf_form_editor.items = ["Australia", "New Zealand", "Malaysia"]
    pdf_form_editor.add_field(
        pdf_facades.FieldType.LIST_BOX, "listbox1", "Australia", 1, 230, 398, 350, 514
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```
