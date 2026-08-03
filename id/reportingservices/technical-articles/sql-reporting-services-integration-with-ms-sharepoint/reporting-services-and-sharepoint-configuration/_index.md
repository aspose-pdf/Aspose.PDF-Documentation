---
title: Layanan Pelaporan dan konfigurasi SharePoint
linktitle: Reporting Services and SharePoint configuration
type: docs
weight: 40
url: /reportingservices/reporting-services-and-sharepoint-configuration/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Sekarang SharePoint telah diinstal dan dikonfigurasi di server RS ​​dan RS telah disiapkan dan dikonfigurasi melalui Manajer Konfigurasi Layanan Pelaporan, kita dapat beralih ke konfigurasi dalam Admin Pusat. RS 2008 R2 benar-benar menyederhanakan proses ini. Kami dulu memiliki proses 3 langkah yang harus Anda lakukan agar ini berfungsi. Sekarang kita hanya punya satu langkah.

{{% /alert %}}

{{% alert color="primary" %}}

Kami ingin pergi ke situs Web Administrator Pusat dan kemudian ke Pengaturan Aplikasi Umum. Di bagian bawah kita akan melihat Layanan Pelaporan.

![Configuration-step1](reporting-services-and-sharepoint-configuration_1.png)
**Gambar1**:- Dialog konfigurasi SharePoint

Pilih tautan "Integrasi Layanan Pelaporan". Layar berikut akan ditampilkan.

![Configuration-step2](reporting-services-and-sharepoint-configuration_2.png)
**Gambar2**:- Tentukan kredensial integrasi Layanan Pelaporan

{{% /alert %}}

## URL Layanan Web:

**Kami akan memberikan URL untuk Server Laporan yang kami temukan di Manajer Konfigurasi Layanan Pelaporan.**

## Mode Otentikasi:

**Kami juga akan memilih Mode Otentikasi. Tautan MSDN berikut menjelaskan secara rinci apa itu.
Ikhtisar Keamanan untuk Layanan Pelaporan dalam Mode Terintegrasi SharePoint**

{{% alert color="primary" %}}

**Singkatnya, jika situs Anda menggunakan Otentikasi Klaim, Anda akan selalu menggunakan Otentikasi Tepercaya apa pun yang Anda pilih di sini. Jika Anda ingin meneruskan kredensial windows, Anda dapat memilih Otentikasi Windows. Untuk Otentikasi Tepercaya, kami akan meneruskan token SPUser dan tidak bergantung pada kredensial Windows. Anda juga ingin menggunakan Otentikasi Tepercaya jika Anda telah mengonfigurasi situs Mode Klasik untuk NTLM dan RS disiapkan untuk NTLM. Kerberos diperlukan untuk menggunakan Autentikasi Windows dan meneruskannya ke sumber data Anda.**

{{% /alert %}}

## Aktifkan fitur:

{{% alert color="primary" %}}

**Ini memberi Anda pilihan untuk mengaktifkan Layanan Pelaporan di semua kumpulan Situs, atau Anda dapat memilih di mana Anda ingin mengaktifkannya. Ini berarti situs mana yang dapat menggunakan Layanan Pelaporan. Setelah selesai, Anda akan melihat hasil berikut**

![Configuration-step3](reporting-services-and-sharepoint-configuration_3.png)

**Gambar3:**- Integrasi Layanan Pelaporan yang berhasil dengan lingkungan SharePoint
{{% /alert %}}

{{% alert color="primary" %}}

Kembali ke URL ReportServer, kita akan melihat sesuatu yang mirip dengan yang berikut ini

![Configuration-step4](reporting-services-and-sharepoint-configuration_4.png)

**Gambar4:**- Layanan Pelaporan berhasil terhubung dengan lingkungan SharePoint

**CATATAN:** ​​***Jika situs SharePoint Anda dikonfigurasi untuk SSL, situs tersebut tidak akan muncul dalam daftar ini. Ini adalah masalah yang diketahui dan bukan berarti ada masalah. Laporan Anda seharusnya tetap berfungsi.***
{{% /alert %}}

{{% alert color="primary" %}}

Kini setelah kami berhasil mengintegrasikan kedua produk, kami siap menggunakan Layanan Pelaporan di SharePoint 2010. Seperti versi sebelumnya, kami memiliki fitur (diaktifkan saat kami mengonfigurasi Integrasi Layanan Pelaporan) di “Fitur Kumpulan Situs”. Instalasi juga menambahkan 3 tipe konten untuk ditambahkan ke situs kami. Pada Gambar 7 kita dapat melihat 2 tipe konten ditambahkan di pustaka dokumen untuk membuat laporan khusus menggunakan, seperti yang dapat kita lihat pada Gambar 5 di bawah.

![Configuration-step5](reporting-services-and-sharepoint-configuration_5.png)

**Gambar5:**- Pembuat Laporan

"Reporter Builder" adalah kontrol ActiveX jadi kita perlu mendownloadnya melalui server, seperti yang bisa kita lihat pada Gambar 6 di bawah.

![Configuration-step6](reporting-services-and-sharepoint-configuration_6.png)

**Gambar6:**- Unduh dan instal Pembuat Laporan
{{% /alert %}}

{{% alert color="primary" %}}

Setelah proses pengunduhan selesai, muat kontrol “Pembuat Laporan”. Sekarang kita siap merancang laporan pertama kita, seperti yang ditunjukkan pada Gambar7 di bawah.

![Configuration-step7](reporting-services-and-sharepoint-configuration_7.png)

**Gambar7:**- Pembuat Laporan – Panduan pembuatan Laporan baru
{{% /alert %}}

{{% alert color="primary" %}}

Setelah membuat laporan, kami dapat menyimpannya di pustaka dokumen yang dibuat untuk meletakkan laporan di SharePoint 2010. Tipe konten lainnya harus digunakan untuk membuat koneksi bersama sebagai sumber data dan menyimpannya di pustaka dokumen di SharePoint. Kita bisa membuat pustaka dokumen, menambahkan tipe konten ini dan setelah itu kita bisa menyediakan koneksi untuk mengubah sumber data laporan.

![Configuration-step8](reporting-services-and-sharepoint-configuration_8.png)

**Image8:**- Integrasi Aspose.PDF yang Berhasil untuk Layanan Pelaporan dengan MS SharePoint
{{% /alert %}}

