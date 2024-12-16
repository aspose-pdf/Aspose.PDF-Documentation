---
title: Layanan Pelaporan dan konfigurasi SharePoint
type: docs
weight: 40
url: /id/reportingservices/reporting-services-and-sharepoint-configuration/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Sekarang SharePoint telah diinstal dan dikonfigurasi pada server RS dan RS telah disiapkan dan diatur melalui Pengelola Konfigurasi Layanan Pelaporan, kita dapat melanjutkan ke konfigurasi dalam Admin Pusat. RS 2008 R2 benar-benar menyederhanakan proses ini. Dulu kita memiliki proses 3 langkah yang harus dilakukan agar ini bekerja. Sekarang kita hanya memiliki satu langkah.

{{% /alert %}}

{{% alert color="primary" %}}

Kita ingin pergi ke situs Web Administrator Pusat dan kemudian ke Pengaturan Aplikasi Umum. Di bagian bawah kita akan melihat Layanan Pelaporan.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_1.png)
**Gambar1**:- Dialog konfigurasi SharePoint

Pilih tautan "Integrasi Layanan Pelaporan". Layar berikut akan ditampilkan.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_2.png)
```
**Image2**:- Tentukan kredensial integrasi Layanan Pelaporan

{{% /alert %}}

## URL Layanan Web:

**Kami akan menyediakan URL untuk Server Laporan yang kami temukan di Reporting Services Configuration Manager.**

## Mode Autentikasi:

**Kami juga akan memilih Mode Autentikasi. Tautan MSDN berikut menjelaskan secara rinci apa saja mode ini.
Tinjauan Keamanan untuk Layanan Pelaporan dalam Mode Terintegrasi SharePoint**

{{% alert color="primary" %}}

**Singkatnya, jika situs Anda menggunakan Autentikasi Klaim, Anda akan selalu menggunakan Autentikasi Terpercaya terlepas dari apa yang Anda pilih di sini. Jika Anda ingin mengirimkan kredensial Windows, Anda akan memilih Autentikasi Windows. Untuk Autentikasi Terpercaya, kami akan mengirimkan token SPUser dan tidak bergantung pada kredensial Windows. Anda juga ingin menggunakan Autentikasi Terpercaya jika Anda telah mengonfigurasi situs Mode Klasik Anda untuk NTLM dan RS diatur untuk NTLM. Kerberos diperlukan untuk menggunakan Autentikasi Windows dan untuk meneruskannya ke sumber data Anda.**

{{% /alert %}}

## Aktifkan fitur:

{{% alert color="primary" %}}

**Ini memberi Anda opsi untuk mengaktifkan Layanan Pelaporan pada semua koleksi Situs, atau Anda dapat memilih situs mana yang ingin Anda aktifkan. Ini benar-benar berarti situs mana yang akan dapat menggunakan Layanan Pelaporan. Ketika selesai, Anda harus melihat hasil berikut**

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_3.png)

**Gambar3:**- Integrasi Layanan Pelaporan yang sukses dengan lingkungan SharePoint
{{% /alert %}}

{{% alert color="primary" %}}

Kembali ke URL ReportServer, kita harus melihat sesuatu yang mirip dengan yang berikut

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_4.png)

**Gambar4:**- Layanan Pelaporan berhasil terhubung dengan lingkungan SharePoint

**CATATAN:** ***Jika situs SharePoint Anda dikonfigurasi untuk SSL, itu tidak akan muncul dalam daftar ini. Ini adalah masalah yang diketahui dan tidak berarti ada masalah. Laporan Anda seharusnya masih berfungsi.***
{{% /alert %}}

Sekarang setelah kami berhasil mengintegrasikan kedua produk, kami siap menggunakan Layanan Pelaporan di SharePoint 2010. Seperti versi sebelumnya, kami memiliki fitur (diaktifkan ketika kami mengkonfigurasi Integrasi Layanan Pelaporan) di "Fitur Koleksi Situs". Selain itu, instalasi menambahkan 3 tipe konten untuk ditambahkan ke situs kami. Pada Gambar 7 kita dapat melihat 2 dari tipe konten tersebut ditambahkan ke dalam perpustakaan dokumen untuk membuat laporan kustom menggunakan, seperti yang dapat kita lihat pada Gambar 5 di bawah.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_5.png)
{{% alert color="primary" %}}

**Gambar 5:**- Pembuat Laporan

"Pembuat Laporan" adalah kontrol ActiveX sehingga kita perlu mengunduhnya melalui server, seperti yang dapat kita lihat pada Gambar 6 di bawah.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_6.png)

**Gambar 6:**- Unduh dan instal Pembuat Laporan
{{% /alert %}}

{{% alert color="primary" %}}

Setelah proses pengunduhan selesai, muat kontrol "Pembuat Laporan". Sekarang kita siap merancang laporan pertama kita, seperti yang ditunjukkan pada Gambar 7 di bawah.


![todo:image_alt_text](reporting-services-and-sharepoint-configuration_7.png)

**Image7:**- Pembuat Laporan – Wizard pembuatan laporan baru
{{% /alert %}}

{{% alert color="primary" %}}

Setelah membuat laporan kami dapat menyimpannya di perpustakaan dokumen yang dibuat untuk menempatkan laporan di SharePoint 2010 kami. Jenis konten lainnya harus digunakan untuk membuat koneksi bersama sebagai sumber data dan menyimpannya di perpustakaan dokumen di SharePoint. Kita dapat membuat perpustakaan dokumen, menambahkan jenis konten ini dan setelah itu kita dapat memiliki koneksi kita tersedia untuk mengubah sumber data dari laporan.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_8.png)

**Image8:**- Integrasi Berhasil Aspose.PDF untuk Layanan Pelaporan dengan MS SharePoint
{{% /alert %}}