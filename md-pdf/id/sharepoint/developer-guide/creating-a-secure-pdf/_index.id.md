title: Buat PDF Aman di SharePoint

linktitle: Membuat PDF Aman

type: docs

weight: 60

url: /sharepoint/creating-a-secure-pdf/

lastmod: "2020-12-16"

description: Menggunakan API PDF SharePoint, Anda dapat menghasilkan PDF yang aman dan terenkripsi serta menentukan kata sandi mereka di SharePoint.

---

{{% alert color="primary" %}}

Aspose.PDF untuk SharePoint mendukung pembuatan PDF yang aman. Menginstal Aspose.PDF untuk SharePoint menambahkan opsi **Pengaturan Aman PDF** di Pengaturan Situs. Di sini, Anda dapat mengatur kata sandi pengguna, kata sandi pemilik, dan nilai apa pun dari daftar algoritma untuk mengenkripsi PDF keluaran. Daftar algoritma menyediakan berbagai kombinasi algoritma enkripsi dan ukuran kunci. Masukkan nilai pilihan Anda.

Artikel ini menunjukkan cara menggunakan Aspose.PDF untuk SharePoint untuk menghasilkan PDF terenkripsi.

{{% /alert %}}

## **Membuat PDF Aman**

Untuk menunjukkan fitur ini, pertama kita konfigurasikan opsi **Pengaturan Aman PDF** untuk kata sandi pemilik dan pengguna serta algoritma enkripsi.
``` Contoh tersebut kemudian menggabungkan dua dokumen dari perpustakaan dokumen.



### **Mengatur Opsi Pengaturan Keamanan PDF**



Buka opsi **Pengaturan Keamanan PDF** dari Pengaturan Situs dan atur algoritma, kata sandi pemilik, dan kata sandi pengguna.



Tentukan kata sandi pengguna dan pemilik yang berbeda saat mengenkripsi file PDF.



- Kata sandi pengguna, jika diatur, adalah yang perlu Anda berikan untuk membuka PDF. Acrobat Reader meminta pengguna untuk memasukkan kata sandi pengguna. Jika salah, dokumen tidak terbuka.

- Kata sandi pemilik, jika diatur, mengontrol izin seperti mencetak, mengedit, mengekstrak, memberikan komentar, dll. Acrobat Reader menolak fitur-fitur ini berdasarkan pengaturan izin. Acrobat memerlukan kata sandi ini jika Anda ingin mengatur/mengubah izin.



![todo:image_alt_text](creating-a-secure-pdf_1.png)



### **Menggabungkan Dokumen**



Gabungkan dua dokumen menggunakan opsi **Konversi ke PDF**. Fitur ini menggabungkan beberapa file non-PDF (HTML, teks, atau gambar) menjadi satu file PDF.



1. Buka perpustakaan dokumen dan pilih dokumen yang diinginkan dari daftar.



![todo:image_alt_text](creating-a-secure-pdf_2.png)





1. Gunakan opsi **Gabung ke PDF** dari Alat Perpustakaan untuk menyimpan file keluaran. Anda akan diminta untuk menyimpan file keluaran ke disk.



![todo:image_alt_text](creating-a-secure-pdf_3.png)



### **Keluaran**



File keluaran dienkripsi.



![todo:image_alt_text](creating-a-secure-pdf_4.png)