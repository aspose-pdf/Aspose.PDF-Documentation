---
title: Lindungi File PDF dengan Python
linktitle: Enkripsi dan Dekripsi File PDF
type: docs
weight: 70
url: /id/python-net/protect-pdf-file/
description: Pelajari cara mengenkripsi file, mendekripsi PDF yang dilindungi, dan mengubah kata sandi di Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Atur izin PDF dan kelola enkripsi di Python
Abstract: Halaman ini menjelaskan cara mengatur hak istimewa dokumen, menerapkan enkripsi, mendekripsi file PDF, dan mengubah kata sandi menggunakan Aspose.PDF for Python via .NET. Ini mencakup konfigurasi kata sandi pengguna dan pemilik, mendefinisikan pembatasan akses (seperti mencetak, menyalin, dan mengedit), serta mengelola keamanan PDF dalam aplikasi Python.
---

## Enkripsi PDF dengan kata sandi dan izin

Gunakan Aspose.PDF for Python via .NET untuk mengamankan dokumen PDF dengan enkripsi berbasis kata sandi dan izin terbatas.

1. Muat dokumen PDF.
1. Buat sebuah `DocumentPrivilege` objek izin.
1. Aktifkan izin yang diperlukan.
1. Atur kata sandi pengguna dan pemilik.
1. Pilih algoritma enkripsi.
1. Terapkan enkripsi pada dokumen.
1. Simpan PDF yang dienkripsi.

```python
import aspose.pdf as ap

def encrypt_password(infile, outfile):
    """
    Encrypt PDF with password and permissions.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        encrypt_password("sample.pdf", "sample_protected.pdf")

    Note:
        Uses AES 128-bit encryption. Allows screen readers, forbids all other operations.
        User password: "userpassword", Owner password: "ownerpassword".
    """
    document = ap.Document(infile)
    document_privilege = ap.facades.DocumentPrivilege.forbid_all
    document_privilege.allow_screen_readers = True

    document.encrypt(
        "userpassword",
        "ownerpassword",
        document_privilege,
        ap.CryptoAlgorithm.AESx128,
        False,
    )
    document.save(outfile)
```

## Enkripsi PDF dengan izin penuh

Enkripsi dokumen PDF sambil mengizinkan izin akses penuh menggunakan Aspose.PDF for Python via .NET. Contoh ini menggunakan enkripsi RC4 128-bit untuk kompatibilitas dengan penampil PDF lama.

1. Muat dokumen PDF.
1. Tentukan kata sandi pengguna dan pemilik.
1. Atur izin akses penuh.
1. Pilih algoritma enkripsi.
1. Panggilan `encrypt()` dengan kata sandi, izin, dan algoritma.
1. Simpan PDF yang dienkripsi.

```python
import aspose.pdf as ap

def encrypt_pdf_file(infile, outfile):
    """
    Encrypt PDF with full permissions.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        encrypt_pdf_file("sample.pdf", "sample_protected.pdf")

    Note:
        Uses RC4 128-bit encryption with allow_all privileges.
    """
    document = ap.Document(infile)
    document.encrypt(
        "userpassword",
        "ownerpassword",
        ap.facades.DocumentPrivilege.allow_all,
        ap.CryptoAlgorithm.RC4x128,
        False,
    )
    document.save(outfile)
```

## Dekripsi File PDF dengan Kata Sandi Pemilik

Untuk menghapus perlindungan kata sandi dan mengembalikan akses penuh:

1. Muat PDF terenkripsi menggunakan kata sandi yang benar (pengguna atau pemilik).
1. Hapus semua perlindungan kata sandi dan pengaturan enkripsi dari dokumen.
1. Simpan PDF yang kini tidak dilindungi ke file output yang ditentukan.

```python
import aspose.pdf as ap

def decrypt_pdf_file(infile, outfile):
    """
    Decrypt password-protected PDF.

    Args:
        infile (str): Input encrypted PDF filename
        outfile (str): Output decrypted PDF filename

    Returns:
        None

    Example:
        decrypt_pdf_file("sample_protected.pdf", "sample_unprotected.pdf")

    Note:
        Requires user password to open document.
    """
    document = ap.Document(infile, "userpassword")
    document.decrypt()
    document.save(outfile)
```

## Ubah Kata Sandi File PDF

Perbarui kredensial keamanan (kata sandi pengguna dan pemilik) dari sebuah dokumen PDF sambil mempertahankan konten dan strukturnya.

1. Buka PDF menggunakan kata sandi pemilik yang ada, yang memberikan akses penuh ke pengaturan keamanan.
1. Ganti kata sandi lama dengan kata sandi pengguna baru dan kata sandi pemilik baru.
1. Simpan PDF dengan pengaturan kata sandi yang diperbarui.

```python
import aspose.pdf as ap

def change_password(infile, outfile):
    """
    Change user and owner passwords.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        change_password("sample_protected.pdf", "sample_changepassword.pdf")

    Note:
        Changes from ownerpassword to newuser/newowner.
    """
    document = ap.Document(infile, "ownerpassword")
    document.change_passwords("ownerpassword", "newuser", "newowner")
    document.save(outfile)

```

## Tentukan kata sandi yang benar dari Array

Dalam beberapa skenario, Anda mungkin perlu mengidentifikasi kata sandi yang tepat dari daftar calon yang mungkin untuk mengakses PDF yang diamankan. Cuplikan kode di bawah memeriksa apakah file PDF terenkripsi dan kemudian berusaha membukanya dengan mengiterasi melalui daftar kata sandi yang telah ditentukan.

Proses mencakup:

1. Gunakan `PdfFileInfo` untuk mendeteksi apakah PDF terenkripsi.
1. Buka PDF dengan masing-masing kata sandi menggunakan `ap.Document()`.
1. Jika berhasil, ia mencetak jumlah halaman.
1. Jika tidak, ia menangkap pengecualian dan melaporkan kata sandi yang gagal.

```python
import aspose.pdf as ap

def determine_correct_password_from_list(infile):
    """
    Test multiple passwords to find correct one.

    Args:
        infile (str): Input encrypted PDF filename

    Returns:
        None

    Example:
        determine_correct_password_from_list("sample_protected.pdf")

    Note:
        Tries passwords: test, test1, test2, test3, userpassword.
        Prints page count if password is correct.
    """
    info = ap.facades.PdfFileInfo(infile)
    print(f"File is password protected {info.is_encrypted}")

    passwords = "test", "test1", "test2", "test3", "userpassword"

    for password in passwords:
        try:
            document = ap.Document(infile, password)
            count = len(document.pages)
            if count > 0:
                print(f"Number of Page in document are = {count}")
        except RuntimeError as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
```
