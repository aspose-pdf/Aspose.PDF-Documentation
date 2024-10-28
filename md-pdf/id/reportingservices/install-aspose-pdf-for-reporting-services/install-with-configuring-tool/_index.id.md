---
title: Install dengan Alat Konfigurasi
type: docs
weight: 30
url: /reportingservices/install-with-configuring-tool/
lastmod: "2021-06-05"
---

Aspose.Pdf untuk Alat Konfigurasi Layanan Pelaporan dapat membantu Anda untuk mengkonfigurasi ekstensi Aspose.Pdf untuk Layanan Pelaporan untuk versi Server Laporan (RS) yang didukung. Saat ini, alat ini mendukung RS2016, RS2017, RS2019, RS2022, dan Power BI Report Server. Alat Konfigurasi memerlukan .NET Framework 4.8.

Jika Anda ingin menginstal ekstensi dan mendaftarkannya dengan Server Laporan, pilih jenis tindakan 'Register'. Untuk membatalkan pendaftaran dan mencopot pemasangan ekstensi, pilih jenis tindakan 'Unregister'.

![todo:image_alt_text](install-with-configuring-tool_1.png)

**Langkah-langkah berikut menjelaskan cara menggunakannya secara detail:**

1. Masukkan atau telusuri jalur file DLL untuk ekstensi Aspose.Pdf untuk Layanan Pelaporan;
1. Pilih jenis tindakan yang sesuai: Register atau Unregister;
1. Pilih tab yang sesuai dengan versi Report Server yang ingin Anda konfigurasikan. Pastikan bahwa Anda memilih file DLL yang dimaksudkan untuk versi RS Anda. Jika versi produk yang diminta tidak terpasang di mesin, alat konfigurasi akan memberi tahu Anda dengan tips. Jika Anda mengonfigurasi ekstensi untuk instance RS2016 yang diberi nama (bukan yang 'MSSQLSERVER' default), silakan masukkan nama instance kustom, lalu tekan tombol 'Refresh'.
1. Pastikan bahwa jalur dan nama file konfigurasi yang ditampilkan di kotak teks bawah sudah benar. Jika tidak, Anda dapat menekan tombol 'Refresh' untuk mencoba menemukan instance RS lagi, atau Anda dapat mencarinya secara manual.
1. Tekan tombol 'Config'. Alat ini sekarang akan mencoba melakukan konfigurasi yang diminta, dan akan memberi tahu Anda apakah konfigurasi berhasil atau tidak.