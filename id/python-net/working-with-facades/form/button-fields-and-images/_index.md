---
title: Bidang Tombol dan Gambar
linktitle: Bidang Tombol dan Gambar
type: docs
weight: 40
url: /id/python-net/button-fields-and-images/
description: Contoh ini menunjukkan cara mengelola bidang tombol dalam formulir PDF menggunakan API Aspose.PDF Facades.
lastmod: "2026-06-12"
TechArticle: true
AlternativeHeadline: Menambahkan Penampilan Gambar ke Bidang Tombol \u0026 Membaca Bendera Kirim
Abstract: Formulir PDF sering kali mencakup tombol interaktif yang baik memicu aksi JavaScript maupun mengirim data formulir. Anda dapat meningkatkan tampilan bidang tombol secara visual dengan menambahkan gambar sebagai penampilannya dan secara programatis memeriksa perilaku pengirimannya.
---

## Tambahkan Penampilan Gambar ke Bidang Tombol

Potongan kode ini menjelaskan cara menambahkan penampilan gambar ke bidang tombol yang ada dalam formulir PDF. Operasi ini meningkatkan tampilan visual tombol PDF dengan mengganti penampilan defaultnya dengan gambar khusus.

1. Buat objek Form.
1. Hubungkan file PDF ke objek Form.
1. Tambahkan Image ke Button Field.

    - Tentukan jalur ke file image yang terkait dengan PDF
    - Buka image dalam mode biner sebagai image_stream.
    - Panggil fill_image_field() dengan nama button field yang sepenuhnya memenuhi syarat.

1. Simpan PDF yang diperbarui.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Add image appearance to button fields
def add_image_appearance_to_button_fields(infile, outfile):
    """Add image appearance to button fields in a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Add image appearance to button fields by providing the field name and image stream
    image_path = infile.replace(".pdf", ".jpg")
    with open(image_path, "rb") as image_stream:
        pdf_form.fill_image_field("Image1_af_image", image_stream)

    # Save updated PDF
    pdf_form.save(outfile)
```

## Dapatkan Flag Kirim

Perpustakaan Python membantu Anda mengambil flag kirim dari tombol kirim dalam formulir PDF menggunakan API Aspose.PDF Facades. Flag kirim menentukan perilaku tombol kirim, seperti apakah mengirim seluruh formulir, menyertakan anotasi, atau mengirim dalam format FDF, XFDF, PDF, atau HTML.

1. Buat objek Form.
1. Panggil get_submit_flags() pada objek form menggunakan nama tombol kirim yang lengkap.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_submit_flags(infile, outfile):
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)
    flags = pdf_form.get_submit_flags("Submit1_af_submit")

    print(f"Submit flags: {flags}")
```
