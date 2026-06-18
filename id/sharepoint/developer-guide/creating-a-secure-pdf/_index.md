---
title: Buat PDF Aman di SharePoint
linktitle: Membuat PDF Aman
type: docs
weight: 60
url: /id/sharepoint/creating-a-secure-pdf/
lastmod: "2026-06-18"
description: Dengan menggunakan API PDF SharePoint, Anda dapat menghasilkan PDF yang aman dan terenkripsi serta menentukan kata sandi mereka di SharePoint.
---

{{% alert color="primary" %}}

Aspose.PDF for SharePoint mendukung pembuatan PDF aman. Menginstal Aspose.PDF for SharePoint menambahkan opsi **PDF Secure Settings** di Site Setting. Di sini, Anda dapat mengatur kata sandi pengguna, kata sandi pemilik, dan nilai apa pun dari daftar algoritma untuk mengenkripsi PDF keluaran. Daftar algoritma menyediakan kombinasi berbeda dari algoritma enkripsi dan ukuran kunci. Pilih nilai yang Anda inginkan.

Artikel ini menunjukkan cara menggunakan Aspose.PDF for SharePoint untuk menghasilkan PDF terenkripsi.

{{% /alert %}}

## **Membuat PDF Aman**

Untuk mendemonstrasikan fitur ini, pertama kami mengonfigurasi opsi **PDF Secure Setting** untuk kata sandi pemilik dan pengguna serta algoritma enkripsi. Contoh kemudian menggabungkan dua dokumen dari perpustakaan dokumen.

### **Pengaturan Opsi PDF Secure Setting**

Buka opsi **PDF Secure Settings** dari Pengaturan Situs dan atur algoritma, kata sandi pemilik, serta kata sandi pengguna.

Tentukan kata sandi pengguna dan pemilik yang berbeda saat mengenkripsi file PDF.

- Kata sandi pengguna, jika diatur, adalah yang harus Anda berikan untuk membuka PDF. Acrobat Reader meminta pengguna memasukkan kata sandi pengguna. Jika salah, dokumen tidak akan terbuka.
- Kata sandi pemilik, jika diatur, mengontrol izin seperti mencetak, mengedit, mengekstrak, mengomentari, dll. Acrobat Reader melarang fitur-fitur ini berdasarkan pengaturan izin. Acrobat memerlukan kata sandi ini jika Anda ingin mengatur/mengubah izin.

![todo:image_alt_text](creating-a-secure-pdf_1.png)

### **Gabungkan Dokumen**

Gabungkan dua dokumen menggunakan opsi **Convert to PDF**. Fitur ini menggabungkan beberapa file non-PDF (HTML, teks, atau gambar) menjadi file PDF.

1. Buka perpustakaan dokumen dan pilih dokumen yang diinginkan dari daftar.

![todo:image_alt_text](creating-a-secure-pdf_2.png)


1. Gunakan opsi **Merge to PDF** dari Library Tools untuk menyimpan file output. Anda akan diminta menyimpan file output ke disk.

![todo:image_alt_text](creating-a-secure-pdf_3.png)

### **Output**

File output terenkripsi.

![todo:image_alt_text](creating-a-secure-pdf_4.png)

