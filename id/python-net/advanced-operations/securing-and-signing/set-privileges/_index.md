---
title: Enkripsi dan Dekripsi File PDF di Python
linktitle: Enkripsi dan Dekripsi File PDF
type: docs
weight: 70
url: /id/python-net/set-privileges-encrypt-and-decrypt-pdf-file/
description: Pelajari cara mengatur hak istimewa PDF, mengenkripsi file, mendekripsi PDF yang dilindungi, dan mengubah kata sandi dalam Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Atur izin PDF dan kelola enkripsi dalam Python
Abstract: Halaman dokumentasi ini menjelaskan cara mengatur hak istimewa dokumen, menerapkan enkripsi, dan mendekripsi file PDF menggunakan Aspose.PDF for Python. Hal ini membimbing pengembang melalui konfigurasi kata sandi pengguna dan pemilik, serta mendefinisikan pembatasan akses (seperti pencetakan, penyalinan, atau pengeditan). Contoh kode menggambarkan cara melindungi konten sensitif dan mengelola keamanan PDF secara efektif dalam aplikasi Python, memastikan akses yang terkontrol dan kerahasiaan data.
---

Mengelola keamanan dokumen sangat penting saat bekerja dengan konten sensitif atau kritis bisnis. Aspose.PDF for Python via .NET menyediakan API yang kuat untuk secara programatis menerapkan enkripsi, mengontrol akses melalui izin, dan mendekripsi file PDF yang dilindungi.

Artikel ini membimbing pengembang Python melalui contoh praktis untuk mengatur hak istimewa, menerapkan dan menghapus enkripsi, mengubah kata sandi, serta mendeteksi status perlindungan — semua dalam alur kerja PDF.

Aspose.PDF for Python via .NET memberi pengembang kontrol penuh atas keamanan PDF:

**Set Privileges** - Kontrol akses terperinci menggunakan izin.
**Enkripsi File** - Terapkan enkripsi AES atau RC4 dengan kata sandi khusus.
**Decrypt File** - Hapus keamanan menggunakan kata sandi pemilik.
**Ubah Kata Sandi** - Rotasi atau perbarui kredensial tanpa mengubah konten.
**Periksa Keamanan** - Deteksi status enkripsi atau tipe kata sandi yang diperlukan.

Gunakan halaman ini ketika Anda perlu melindungi dokumen PDF dengan kata sandi, membatasi pencetakan atau penyalinan, memutar kredensial, atau memeriksa apakah sebuah dokumen terenkripsi.

## Atur Hak Istimewa pada File PDF yang Ada

Anda dapat membatasi atau mengizinkan operasi tertentu (mis., pencetakan, penyalinan, pengisian formulir) dengan menetapkan kata sandi pengguna dan pemilik serta hak akses.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def set_privileges_on_existing_pdf_file(infile: str, outfile: str) -> None:
    """Set restricted privileges on an existing PDF document."""
    with ap.Document(infile) as document:
        document_privilege = ap.facades.DocumentPrivilege.forbid_all
        document_privilege.allow_screen_readers = True
        document.encrypt(
            "user",
            "owner",
            document_privilege,
            ap.CryptoAlgorithm.AESx128,
            False,
        )
        document.save(outfile)
```

## Enkripsi File PDF menggunakan Berbagai Tipe Enkripsi dan Algoritma

Mengenkripsi sebuah PDF memastikan hanya pengguna dengan kredensial yang valid yang dapat membuka atau memodifikasi file tersebut.

>Istilah Kunci:

- Password Pengguna. Diperlukan untuk membuka dokumen.

- Kata Sandi Pemilik. Diperlukan untuk mengubah izin atau menghapus enkripsi.

- KeySize. Gunakan AE_SX128 untuk keamanan maksimum dalam alur kerja modern.

Potongan kode berikut menunjukkan cara mengenkripsi file PDF.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def encrypt_pdf_file(infile: str, outfile: str) -> None:
    """Encrypt a PDF document with user and owner passwords."""
    with ap.Document(infile) as document:
        document.encrypt(
            "user",
            "owner",
            ap.Permissions.EXTRACT_CONTENT,
            ap.CryptoAlgorithm.AESx128,
        )
        document.save(outfile)
```

## Dekripsi File PDF menggunakan Kata Sandi Pemilik

Untuk menghapus perlindungan kata sandi dan memulihkan akses penuh:

1. Muat PDF terenkripsi menggunakan kata sandi yang benar ('password' adalah kata sandi pengguna atau pemilik).
1. Menghapus semua perlindungan kata sandi dan pengaturan enkripsi dari dokumen.
1. Menyimpan PDF yang kini tidak dilindungi ke file output yang ditentukan.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def decrypt_pdf_file(infile: str, outfile: str) -> None:
    """Decrypt a password-protected PDF document."""
    with ap.Document(infile, "password") as document:
        document.decrypt()
        document.save(outfile)
```

## Enkripsi dan Dekripsi PDF dengan Sertifikat Kunci Publik

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def pub_sec_encryption(
    crypto_algorithm,
    pub_cert: str,
    in_pfx: str,
    outfile: str,
) -> None:
    """Demonstrate public-key encryption and decryption."""
    pfx_password = "12345"

    with ap.Document() as document:
        document.info.title = "TestTitle"
        document.info.author = "TestAuthor"
        page = document.pages.add()
        page.paragraphs.add(ap.text.TextFragment("Hello World!"))

        with open(pub_cert, "rb") as file_stream:
            byte_content = file_stream.read()

        document.encrypt(
            ap.Permissions.PRINT_DOCUMENT,
            crypto_algorithm,
            [byte_content],
        )
        document.save(outfile)

    with ap.Document(
        outfile,
        ap.security.CertificateEncryptionOptions(pub_cert, in_pfx, pfx_password),
    ) as document:
        print(document.info.title)
        print(document.info.author)

        text_absorber = ap.text.TextAbsorber()
        document.pages[1].accept(text_absorber)
        print(text_absorber.text)

        document.decrypt()
        document.save(path.join(path.dirname(outfile), "pubsec_decrypted_out.pdf"))
```

## Ubah Kata Sandi File PDF

Untuk memperbarui kredensial keamanan (kata sandi pengguna dan pemilik) dari sebuah dokumen PDF sambil mempertahankan konten dan strukturnya.

1. Membuka PDF menggunakan password pemilik yang sudah ada ('owner'), yang memberikan akses penuh termasuk izin untuk mengubah pengaturan keamanan.
1. Mengganti password lama dengan password pengguna baru ('newuser') dan password pemilik baru ('newowner').
1. Menyimpan PDF dengan pengaturan kata sandi yang diperbarui.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def change_password(infile: str, outfile: str) -> None:
    """Change the passwords of a password-protected PDF document."""
    with ap.Document(infile, "owner") as document:
        document.change_passwords("owner", "newuser", "newowner")
        document.save(outfile)
```

## Cara - menentukan apakah PDF sumber dilindungi kata sandi

### Tentukan kata sandi yang benar dari Array

Dalam beberapa skenario, Anda mungkin perlu mengidentifikasi kata sandi yang benar dari daftar kandidat potensial untuk mengakses PDF yang diamankan. Potongan kode di bawah ini menunjukkan cara memeriksa apakah file PDF dilindungi kata sandi dan kemudian mencoba membuka kuncinya dengan mengiterasi daftar kata sandi yang telah ditentukan menggunakan Aspose.PDF for Python via .NET.

Proses meliputi:

1. Menggunakan PdfFileInfo untuk mendeteksi apakah PDF terenkripsi.
1. Mencoba membuka PDF dengan setiap kata sandi menggunakan ap.Document().
1. Jika berhasil, itu mencetak jumlah halaman.
1. Jika tidak, itu menangkap pengecualian dan melaporkan kata sandi yang gagal.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def determine_correct_password_from_array(infile: str) -> None:
    """Try a list of passwords until the document opens successfully."""
    with ap.facades.PdfFileInfo() as pdf_file_info:
        pdf_file_info.bind_pdf(infile)
        print(f"File is password protected {pdf_file_info.is_encrypted}")

    passwords = ["test", "test1", "test2", "test3", "sample"]

    for password in passwords:
        try:
            with ap.Document(infile, password) as document:
                if len(document.pages) > 0:
                    print(f"Password = {password} is correct")
                    print(f"Number of pages in document = {len(document.pages)}")
                    break
        except Exception:
            print(f"Password = {password} is not correct")
```

## Topik Keamanan Terkait

- [Amankan dan tanda tangani file PDF di Python](/pdf/id/python-net/securing-and-signing/)
- [Menandatangani file PDF secara digital dengan Python](/pdf/id/python-net/digitally-sign-pdf-file/)
- [Ekstrak informasi tanda tangan dari PDF dengan Python](/pdf/id/python-net/extract-image-and-signature-information/)
- [Tanda tangani dokumen PDF dari kartu pintar menggunakan Python](/pdf/id/python-net/sign-pdf-document-from-smart-card/)

