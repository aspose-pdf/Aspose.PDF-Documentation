---
title: Enkripsi File PDF
linktitle: Enkripsi File PDF
type: docs
weight: 30
url: /id/python-net/encrypt-pdf-file/
description: Enkripsi dokumen PDF dan atur izin untuk mengontrol apa yang dapat dilakukan pengguna dengan file tersebut.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Enkripsi PDF dan Kontrol Aksi Pengguna
Abstract: Pelajari cara mengenkripsi PDF sambil menentukan izin pengguna spesifik menggunakan Aspose.PDF for Python via .NET. Panduan ini menunjukkan cara mengizinkan atau membatasi aksi seperti mencetak dan menyalin sambil menjaga dokumen tetap aman.
---

## Enkripsi PDF dengan Kata Sandi Pengguna dan Pemilik

Mengamankan dokumen PDF sangat penting saat membagikan konten yang sensitif atau terbatas. Enkripsi memungkinkan Anda melindungi dokumen dengan kata sandi dan menentukan tindakan apa yang diizinkan bagi pengguna. Potongan kode ini menunjukkan cara menerapkan kata sandi pengguna dan pemilik beserta izin akses untuk mengamankan sebuah file PDF.

1. Buat objek PdfFileSecurity.
1. Gabungkan PDF input.
1. Tentukan Hak Dokumen.
1. Enkripsi PDF.
1. Simpan PDF yang Dienkripsi.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Encrypt PDF with User and Owner Password
def encrypt_pdf_with_user_owner_password(infile, outfile):
    """Encrypt a PDF document using user and owner passwords."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define document privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True

    # Encrypt the PDF
    file_security.encrypt_file(
        "user_password", "owner_password", privilege, pdf_facades.KeySize.X128
    )

    # Save encrypted PDF
    file_security.save(outfile)
```

## Enkripsi PDF dengan Izin

Potongan kode berikut menjelaskan cara mengizinkan tindakan tertentu seperti mencetak dan menyalin sambil membatasi yang lain.

1. Inisialisasi [PdfFileSecurity](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesecurity/) kelas.
1. Ikat PDF Input.
1. Konfigurasikan Privilege Dokumen.
1. Panggil metode 'encrypt_file()'.
1. Simpan PDF yang Dienkripsi.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Encrypt PDF with Permissions
def encrypt_pdf_with_permissions(infile, outfile):
    """Encrypt a PDF document and configure specific permissions."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Configure privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True
    privilege.allow_copy = True

    # Encrypt the PDF
    file_security.encrypt_file(
        "user_password", "owner_password", privilege, pdf_facades.KeySize.X128
    )

    # Save encrypted PDF
    file_security.save(outfile)
```

## Enkripsi PDF dengan Algoritma Enkripsi

Enkripsi PDF tidak hanya melindungi dokumen dengan kata sandi tetapi juga memungkinkan Anda memilih algoritma enkripsi dan kekuatannya. Memilih algoritma yang tepat memastikan keamanan yang lebih kuat untuk dokumen sensitif.

1. Buat objek PdfFileSecurity.
1. Ikat PDF Input.
1. Tentukan Hak Dokumen.
1. Enkripsi PDF dengan Algoritma.
1. Simpan PDF yang Dienkripsi.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Encrypt PDF with Encryption Algorithm
def encrypt_pdf_with_encryption_algorithm(infile, outfile):
    """Encrypt a PDF document using a specific encryption algorithm."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True

    # Encrypt the PDF using AES algorithm
    file_security.encrypt_file(
        "user_password",
        "owner_password",
        privilege,
        pdf_facades.KeySize.X256,
        pdf_facades.Algorithm.AES,
    )

    # Save encrypted PDF
    file_security.save(outfile)
```
