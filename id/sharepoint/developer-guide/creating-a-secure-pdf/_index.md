---
title: Buat PDF Aman di SharePoint
linktitle: Creating a Secure PDF
type: docs
weight: 60
url: /id/sharepoint/creating-a-secure-pdf/
lastmod: "2020-12-16"
description: Dengan menggunakan PDF SharePoint API, Anda dapat menghasilkan PDF yang aman dan terenkripsi serta menentukan kata sandinya di SharePoint.
---

{{% alert color="primary" %}}

Aspose.PDF untuk SharePoint mendukung pembuatan PDF yang aman. Menginstal Aspose.PDF untuk SharePoint menambahkan opsi **Pengaturan Aman PDF** di Pengaturan Situs. Di sini, Anda dapat mengatur kata sandi pengguna, kata sandi pemilik, dan nilai apa pun dari daftar algoritma untuk mengenkripsi keluaran PDF. Daftar algoritma menyediakan kombinasi algoritma enkripsi dan ukuran kunci yang berbeda. Berikan nilai pilihan Anda.

Artikel ini menunjukkan cara menggunakan Aspose.PDF untuk SharePoint untuk menghasilkan PDF terenkripsi.

{{% /alert %}}

## Membuat PDF Aman

To demonstrate the feature, first we configure the **PDF Secure Setting** option for owner and user password and encryption algorithm. The example then merges two documents from a document library.

### Mengatur Opsi Pengaturan Aman PDF

Buka opsi **Pengaturan Aman PDF** dari Pengaturan Situs dan atur algoritma, kata sandi pemilik, dan kata sandi pengguna.

Specify different user and owner passwords while encrypting PDF file.

- Kata sandi pengguna, jika disetel, adalah kata sandi yang perlu Anda berikan untuk membuka PDF. Acrobat Reader meminta pengguna untuk memasukkan kata sandi pengguna. Kalau salah maka dokumen tidak terbuka.
- Kata sandi pemilik, jika disetel, mengontrol izin seperti mencetak, mengedit, mengekstraksi, memberi komentar, dll. Acrobat Reader melarang fitur ini berdasarkan pengaturan izin. Acrobat memerlukan kata sandi ini jika Anda ingin mengatur/mengubah izin.

![PDF Secure Settings](creating-a-secure-pdf_1.png)

### Gabungkan Dokumen

Merge two documents using the **Convert to PDF** option. This feature merges multiple non-PDF files (HTML, text or image) into a PDF file.

1. Buka perpustakaan dokumen dan pilih dokumen yang diinginkan dari daftar.

![Merge Documents](creating-a-secure-pdf_2.png)

1. Gunakan opsi **Gabung ke PDF** dari Alat Perpustakaan untuk menyimpan file keluaran. Anda diminta untuk menyimpan file keluaran ke disk.

![Merge to PDF](creating-a-secure-pdf_3.png)

### Keluaran

File keluaran dienkripsi.

![Output](creating-a-secure-pdf_4.png)


