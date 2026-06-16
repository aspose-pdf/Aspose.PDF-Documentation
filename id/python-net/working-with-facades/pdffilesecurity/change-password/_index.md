---
title: Ubah Kata Sandi File PDF
linktitle: Ubah Kata Sandi File PDF
type: docs
weight: 10
url: /id/python-net/change-password/
description: Ubah kata sandi pengguna dan pemilik dari dokumen PDF yang aman menggunakan Aspose.PDF for Python via .NET.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Perbarui Kata Sandi PDF
Abstract: Pelajari cara mengubah kedua kata sandi pengguna dan pemilik dalam file PDF yang aman menggunakan Aspose.PDF for Python via .NET. Contoh ini menunjukkan cara memperbarui kredensial akses secara aman sambil mempertahankan enkripsi dan hak akses yang ada.
---

## Ubah Kata Sandi Pengguna dan Pemilik

Dalam banyak kasus, Anda mungkin perlu memperbarui kata sandi PDF yang dilindungi tanpa mengubah pengaturan keamanan yang ada. Ini dapat berguna saat mengganti kredensial, mentransfer kepemilikan, atau meningkatkan keamanan dokumen.

Metode 'change_password' dari [PdfFileSecurity](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesecurity/) kelas memungkinkan Anda:

- Perbarui kata sandi pengguna (diperlukan untuk membuka dokumen)
- Perbarui kata sandi pemilik (digunakan untuk mengontrol izin)
- Pertahankan pengaturan enkripsi dan izin saat ini

1. Buat objek 'PdfFileSecurity'.
1. Gabungkan PDF input.
1. Ubah kata sandi dengan metode 'change_password()'.
1. Simpan PDF yang diperbarui.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Change User and Owner Password
def change_user_and_owner_password(infile, outfile):
    """Change user and owner passwords while keeping existing security settings."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Change passwords
    file_security.change_password(
        "owner_password", "new_user_password", "new_owner_password"
    )

    # Save updated PDF
    file_security.save(outfile)
```

## Ubah Kata Sandi dan Atur Ulang Keamanan

Saat bekerja dengan dokumen PDF yang diamankan, cukup mengubah kata sandi mungkin tidak cukup. Anda mungkin juga perlu menyesuaikan izin, seperti hak mencetak, menyalin, atau mengedit.

Pelajari cara memperbarui kata sandi pengguna dan pemilik sambil mereset pengaturan keamanan PDF dengan Aspose.PDF for Python via .NET. Contoh ini menunjukkan cara mendefinisikan ulang izin dokumen dan kekuatan enkripsi bersama dengan kredensial akses baru.

1. Buat objek 'PdfFileSecurity'.
1. Gabungkan PDF input.
1. Buat objek ‘DocumentPrivilege’ dan konfigurasikan tindakan yang diizinkan.
1. Ubah kata sandi dan reset keamanan.
1. Simpan PDF yang diperbarui.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Change Password and Reset Security
def change_password_and_reset_security(infile, outfile):
    """Change passwords and reset document security settings."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define new privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True

    # Change passwords and reset security
    file_security.change_password(
        "owner_password",
        "new_user_password",
        "new_owner_password",
        privilege,
        pdf_facades.KeySize.X128,
    )

    # Save updated PDF
    file_security.save(outfile)
```

## Coba Ubah Kata Sandi Tanpa Pengecualian

Dalam beberapa alur kerja, terutama dalam pemrosesan batch atau sistem otomatis, penting untuk menghindari pengecualian yang dapat menghentikan eksekusi. Alih-alih melempar kesalahan, Anda mungkin lebih memilih operasi aman yang melaporkan keberhasilan atau kegagalan.

Metode 'try_change_password' dari [PdfFileSecurity](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesecurity/) kelas menyediakan fungsi ini dengan:

1. Buat objek 'PdfFileSecurity'.
1. Muat dokumen PDF menggunakan metode 'bind_pdf()'.
1. Mencoba mengubah kata sandi.
1. Periksa hasilnya.
1. Simpan PDF yang diperbarui.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Try Change Password Without Exception
def try_change_password_without_exception(infile, outfile):
    """Attempt to change passwords without throwing an exception on failure."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Attempt to change passwords
    result = file_security.try_change_password(
        "owner_password", "new_user_password", "new_owner_password"
    )

    # Save only if operation succeeded
    if result:
        file_security.save(outfile)
    else:
        print("Password change failed. Check owner password or document security.")
```
