---
title: Atur Hak Istimewa, Enkripsi dan Dekripsi PDF
linktitle: Enkripsi dan Dekripsi File PDF
type: docs
weight: 70
url: /id/python-net/set-privileges-encrypt-and-decrypt-pdf-file/
description: Enkripsi File PDF dengan Python menggunakan Berbagai Tipe Enkripsi dan Algoritma. Juga, dekripsi File PDF menggunakan Kata Sandi Pemilik.
lastmod: "2025-06-22"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Enkripsi atau Dekripsi File PDF dengan Python
Abstract: Halaman dokumentasi ini menjelaskan cara mengatur hak istimewa dokumen, menerapkan enkripsi, dan mendekripsi file PDF menggunakan Aspose.PDF untuk Python. Ini memandu pengembang dalam mengkonfigurasi kata sandi pengguna dan pemilik, mendefinisikan pembatasan akses (seperti mencetak, menyalin, atau mengedit). Contoh kode menggambarkan cara melindungi konten sensitif dan mengelola keamanan PDF secara efektif dalam aplikasi Python, memastikan akses terkontrol dan kerahasiaan data.
---

Mengelola keamanan dokumen sangat penting saat bekerja dengan konten sensitif atau kritis bagi bisnis. Aspose.PDF untuk Python via .NET menyediakan API yang kuat untuk secara programatis menerapkan enkripsi, mengendalikan akses melalui izin, dan mendekripsi file PDF yang dilindungi.

Artikel ini membimbing pengembang Python melalui contoh praktis untuk mengatur hak istimewa, menerapkan dan menghapus enkripsi, mengubah kata sandi, serta mendeteksi status perlindungan — semuanya dalam alur kerja PDF.

Aspose.PDF untuk Python via .NET memberi pengembang kontrol penuh atas keamanan PDF:

**Atur Hak Istimewa** - Kontrol akses yang detail menggunakan izin.
**Enkripsi File** - Terapkan enkripsi AES atau RC4 dengan kata sandi khusus.
**Dekripsi File** - Hapus keamanan menggunakan kata sandi pemilik.
**Ubah Kata Sandi** - Putar atau perbarui kredensial tanpa mengubah konten.
**Periksa Keamanan** - Deteksi status enkripsi atau jenis kata sandi yang diperlukan.

## Atur Hak Istimewa pada File PDF yang Ada

Anda dapat membatasi atau mengizinkan operasi tertentu (mis., mencetak, menyalin, mengisi formulir) dengan menetapkan kata sandi pengguna dan pemilik beserta hak akses.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Instantiate Document Privileges object
        # Apply restrictions on all privileges
        document_privilege = ap.facades.DocumentPrivilege.forbid_all
        # Only allow screen reading
        document_privilege.allow_screen_readers = True
        # Encrypt the file with User and Owner password
        # Need to set the password, so that once the user views the file with user password
        # Only screen reading option is enabled
        document.encrypt("user", "owner", document_privilege, ap.CryptoAlgorithm.AE_SX128, False)
        # Save PDF document
        document.save(path_outfile)
```

## Enkripsi File PDF menggunakan Berbagai Tipe Enkripsi dan Algoritma

Mengenkripsi PDF memastikan hanya pengguna dengan kredensial yang sah dapat membuka atau memodifikasi file.

>Istilah Kunci:

- Kata Sandi Pengguna. Diperlukan untuk membuka dokumen.

- Kata Sandi Pemilik. Diperlukan untuk mengubah izin atau menghapus enkripsi.

- UkuranKunci. Gunakan AE_SX128 untuk keamanan maksimum dalam alur kerja modern.

Potongan kode berikut menunjukkan cara mengenkripsi file PDF.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Encrypt PDF
        document.encrypt("user", "owner", ap.Permissions.EXTRACT_CONTENT, ap.CryptoAlgorithm.AE_SX128)
        # Save PDF document
        document.save(path_outfile)
```

## Dekripsi File PDF menggunakan Kata Sandi Pemilik

Untuk menghapus perlindungan kata sandi dan memulihkan akses penuh:

1. Memuat PDF terenkripsi menggunakan kata sandi yang benar ('password' adalah kata sandi pengguna atau pemilik).
1. Menghapus semua perlindungan kata sandi dan pengaturan enkripsi dari dokumen.
1. Menyimpan PDF yang kini tidak terlindungi ke file output yang ditentukan.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document with password
    with ap.Document(path_infile, "password") as document:
        # Decrypt PDF
        document.decrypt()
        # Save PDF document
        document.save(path_outfile)
```

## Ubah Kata Sandi File PDF

Untuk memperbarui kredensial keamanan (kata sandi pengguna dan pemilik) dari dokumen PDF sambil mempertahankan konten dan strukturnya.

1. Membuka PDF menggunakan kata sandi pemilik yang ada ('owner'), yang memberikan akses penuh termasuk izin untuk mengubah pengaturan keamanan.
1. Menggantikan kata sandi lama dengan kata sandi pengguna baru ('newuser') dan kata sandi pemilik baru ('newowner').
1. Menyimpan PDF dengan pengaturan kata sandi yang diperbarui.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document with password
    with ap.Document(path_infile, "owner") as document:
        # Change password
        document.change_passwords("owner", "newuser", "newowner")
        # Save PDF document
        document.save(path_outfile)
```

## Cara - menentukan apakah PDF sumber dilindungi kata sandi

### Tentukan kata sandi yang tepat dari Array

Dalam beberapa skenario, Anda mungkin perlu mengidentifikasi kata sandi yang tepat dari daftar calon yang potensial untuk mengakses PDF yang aman. Potongan kode di bawah ini menunjukkan cara memeriksa apakah file PDF dilindungi kata sandi dan kemudian mencoba membuka kuncinya dengan iterasi melalui daftar kata sandi yang telah ditentukan menggunakan Aspose.PDF untuk Python via .NET.

Proses ini meliputi:

1. Menggunakan PdfFileInfo untuk mendeteksi apakah PDF terenkripsi.
1. Mencoba membuka PDF dengan setiap kata sandi menggunakan ap.Document().
1. Jika berhasil, akan mencetak jumlah halaman.
1. Jika tidak, akan menangkap pengecualian dan melaporkan kata sandi yang gagal.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile

    with ap.facades.PdfFileInfo() as pdf_file_info:
        # Bind PDF document
        pdf_file_info.bind_pdf(path_infile)
        # Determine if the source PDF is encrypted
        print("File is password protected " + str(pdf_file_info.is_encrypted))

        passwords = ["test", "test1", "test2", "test3", "sample"]

        for password_index in range(len(passwords)):
            try:
                with ap.Document(path_infile, passwords[password_index]) as document:
                    if len(document.pages) > 0:
                        print("Number of Pages in document are = " + str(len(document.pages)))
                    password_index = password_index + 1
            except Exception as e:
                print("Password = " + passwords[password_index] + " is not correct")
                password_index = password_index + 1
```


