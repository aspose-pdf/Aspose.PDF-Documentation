---
title: Dekripsi File PDF
linktitle: Dekripsi File PDF
type: docs
weight: 20
url: /id/python-net/decrypt-pdf-file/
description: Panduan ini menjelaskan cara menghapus pembatasan seperti mencetak, menyalin, dan mengedit untuk memperoleh akses penuh ke dokumen PDF Anda.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Hapus Perlindungan Kata Sandi dari PDF
Abstract: Artikel ini menunjukkan cara mendekripsi file PDF menggunakan kata sandi pemilik. Artikel ini mencakup proses menghapus pembatasan keamanan yang membatasi tindakan seperti mencetak, mengedit, atau menyalin konten. Dengan menerapkan kata sandi pemilik yang tepat, pengguna dapat membuka kunci dokumen dan mendapatkan kembali kontrol penuh atas fungsinya.
---

## Dekripsi PDF dengan Kata Sandi Pemilik

Dekripsi dokumen PDF yang dilindungi kata sandi menggunakan kata sandi pemilik dengan Aspose.PDF for Python via .NET. Operasi ini menghapus enkripsi dan memungkinkan akses tanpa batas ke dokumen.

1. Buat objek 'PdfFileSecurity'.
1. Muat PDF yang terenkripsi menggunakan metode 'bind_pdf()'.
1. Dekripsi Dokumen.
1. Simpan PDF yang didekripsi.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Decrypt PDF with Owner Password
def decrypt_pdf_with_owner_password(infile, outfile):
    """Decrypt a PDF document using the owner password."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Decrypt the PDF
    file_security.decrypt_file("owner_password")

    # Save decrypted PDF
    file_security.save(outfile)
```

## Coba Dekripsi PDF Tanpa Pengecualian

Dokumen PDF sering dilindungi dengan kata sandi untuk membatasi akses dan penggunaan. Untuk sepenuhnya mengakses atau memodifikasi dokumen tersebut, Anda mungkin perlu menghapus enkripsi. Dekripsi dokumen PDF yang aman menggunakan kata sandi pemilik untuk menghapus enkripsi dan pembatasan akses dengan Aspose.PDF for Python via .NET.

1. Buat objek 'PdfFileSecurity'.
1. Gabungkan PDF input.
1. Dekripsi PDF.
1. Simpan PDF Output.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Try Decrypt PDF Without Exception
def try_decrypt_pdf_without_exception(infile, outfile):
    """Attempt to decrypt a PDF without throwing an exception on failure."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Attempt to decrypt the PDF
    result = file_security.try_decrypt_file("owner_password")

    # Save only if decryption was successful
    if result:
        file_security.save(outfile)
    else:
        print("Decryption failed. Check password or document security.")
```
