---
title: Buat PDF Aman di SharePoint
linktitle: Membuat PDF Aman
type: docs
weight: 60
url: /id/sharepoint/creating-a-secure-pdf/
lastmod: "2026-08-07"
description: Dengan menggunakan API PDF SharePoint, Anda dapat menghasilkan PDF yang aman dan terenkripsi serta menentukan password-nya di SharePoint.
---

{{% alert color="primary" %}}

Aspose.PDF for SharePoint mendukung pembuatan PDF aman. Menginstal Aspose.PDF for SharePoint menambahkan opsi **PDF Secure Settings** di Pengaturan Situs. Di sini, Anda dapat mengatur kata sandi pengguna, kata sandi pemilik, dan nilai apa pun dari daftar algoritma untuk mengenkripsi PDF output. Daftar algoritma menyediakan berbagai kombinasi algoritma enkripsi dan ukuran kunci. Masukkan nilai pilihan Anda.

Artikel ini menunjukkan cara menggunakan Aspose.PDF for SharePoint untuk menghasilkan PDF terenkripsi.

{{% /alert %}}

## Membuat PDF Aman

Untuk mendemonstrasikan fitur ini, pertama kami mengonfigurasi opsi **PDF Secure Setting** untuk kata sandi pemilik dan pengguna serta algoritma enkripsi. Contoh kemudian menggabungkan dua dokumen dari perpustakaan dokumen.

### Pengaturan Opsi PDF Secure Setting

Buka opsi **PDF Secure Settings** dari Pengaturan Situs dan atur algoritma, kata sandi pemilik, dan kata sandi pengguna.

Tentukan kata sandi pengguna dan pemilik yang berbeda saat mengenkripsi file PDF.

- Kata sandi pengguna, jika diatur, adalah yang harus Anda berikan untuk membuka PDF. Acrobat Reader meminta pengguna memasukkan kata sandi pengguna. Jika salah, dokumen tidak akan terbuka.
- Password pemilik, jika diatur, mengontrol izin seperti mencetak, mengedit, mengekstrak, mengomentari, dll. Acrobat Reader melarang fitur-fitur ini berdasarkan pengaturan izin. Acrobat memerlukan password ini jika Anda ingin mengatur/mengubah izin.

![Pengaturan Keamanan PDF](creating-a-secure-pdf_1.png)

### Gabungkan Dokumen

Gabungkan dua dokumen menggunakan opsi **Convert to PDF**. Fitur ini menggabungkan beberapa file non-PDF (HTML, teks, atau gambar) ke dalam file PDF.

1. Buka perpustakaan dokumen dan pilih dokumen yang diinginkan dari daftar.

![Gabungkan Dokumen](creating-a-secure-pdf_2.png)

1. Gunakan opsi **Merge to PDF** dari Library Tools untuk menyimpan file output. Anda akan diminta untuk menyimpan file output ke disk.

![Gabungkan ke PDF](creating-a-secure-pdf_3.png)

### Output

File output terenkripsi.

![Output](creating-a-secure-pdf_4.png)

