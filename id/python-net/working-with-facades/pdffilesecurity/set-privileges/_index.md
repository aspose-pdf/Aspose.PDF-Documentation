---
title: Atur Hak Istimewa pada File PDF yang Ada
linktitle: Atur Hak Istimewa pada File PDF yang Ada
type: docs
weight: 40
url: /id/python-net/set-privileges/
description: Atur dan kelola hak istimewa dokumen PDF untuk mengontrol tindakan pengguna seperti mencetak, menyalin, dan mengedit.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Kelola Izin PDF dan Kontrol Akses
Abstract: Pelajari cara mengontrol apa yang dapat dilakukan pengguna dengan PDF dengan mengatur hak istimewa dokumen menggunakan Aspose.PDF for Python via .NET. Panduan ini mencakup penerapan izin dengan atau tanpa kata sandi untuk membatasi tindakan seperti mencetak, menyalin, atau mengedit.
---

## Atur Hak Istimewa PDF Tanpa Kata Sandi

Periksa cara menerapkan hak istimewa dokumen ke PDF tanpa menentukan kata sandi pengguna atau pemilik menggunakan Aspose.PDF for Python via .NET. Potongan kode ini menunjukkan cara mengontrol tindakan yang diizinkan sambil menjaga dokumen tetap dapat diakses.

1. Buat objek 'PdfFileSecurity'.
1. Gabungkan PDF input.
1. Tentukan hak istimewa Dokumen.
1. Panggil metode 'set_privilege()' tanpa melewatkan kata sandi.
1. Simpan PDF yang diperbarui.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Set PDF Privileges Without Passwords
def set_pdf_privileges_without_passwords(infile, outfile):
    """Set PDF privileges without specifying user and owner passwords."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True

    # Apply privileges (owner password will be generated automatically)
    file_security.set_privilege(privilege)

    # Save updated PDF
    file_security.save(outfile)
```

## Atur Hak PDF dengan Kata Sandi Pengguna dan Pemilik

Untuk mengamankan dokumen PDF sepenuhnya, Anda biasanya memerlukan kontrol akses (kata sandi) dan pembatasan penggunaan (izin). Dengan menggabungkan keduanya, Anda dapat memastikan hanya pengguna yang berwenang yang dapat membuka dokumen dan melakukan tindakan tertentu.

Dengan menggunakan metode set_privilege dengan parameter kata sandi, Anda dapat:

- Melindungi dokumen dengan kata sandi pengguna
- Tentukan kata sandi pemilik untuk kontrol penuh
- Konfigurasikan tindakan yang diizinkan dan dibatasi
- Terapkan kebijakan keamanan tingkat dokumen

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Set PDF Privileges with User and Owner Passwords
def set_pdf_privileges_with_passwords(infile, outfile):
    """Set PDF privileges using user and owner passwords."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True
    privilege.allow_copy = False

    # Apply privileges with passwords
    file_security.set_privilege("user_password", "owner_password", privilege)

    # Save updated PDF
    file_security.save(outfile)
```

## Coba Atur Hak PDF Tanpa Pengecualian

Potongan kode ini menjelaskan cara mengontrol akses dan membatasi tindakan seperti menyalin sambil mengizinkan yang lain seperti mencetak.

1. Buat objek 'PdfFileSecurity'.
1. Muat PDF sumber menggunakan metode 'bind_pdf()'.
1. Tentukan hak istimewa Dokumen.
1. Terapkan Hak dengan Kata Sandi.
1. Simpan PDF yang diperbarui.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Try Set PDF Privileges Without Exception
def try_set_pdf_privileges_without_exception(infile, outfile):
    """Attempt to set PDF privileges without throwing an exception on failure."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True

    # Attempt to apply privileges
    result = file_security.try_set_privilege(
        "user_password", "owner_password", privilege
    )

    # Save only if operation succeeded
    if result:
        file_security.save(outfile)
    else:
        print("Setting privileges failed. Check passwords or document state.")
```
