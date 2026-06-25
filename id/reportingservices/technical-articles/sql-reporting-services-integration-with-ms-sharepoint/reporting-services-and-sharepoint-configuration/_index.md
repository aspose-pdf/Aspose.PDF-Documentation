---
title: Reporting Services and SharePoint configuration
linktitle: Reporting Services and SharePoint configuration
type: docs
weight: 40
url: /id/reportingservices/reporting-services-and-sharepoint-configuration/
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Sekarang setelah SharePoint terinstal dan dikonfigurasi pada server RS serta RS diatur melalui Reporting Services Configuration Manager, kita dapat melanjutkan ke konfigurasi di Central Admin. RS 2008 R2 benar‑benar menyederhanakan proses ini. Dulu kami harus melalui proses 3 langkah untuk membuatnya berfungsi. Sekarang hanya ada satu langkah.

{{% /alert %}}

{{% alert color="primary" %}}

Kami ingin pergi ke situs Central Administrator Web dan kemudian ke General Application Settings. Di bagian bawah kami akan melihat Reporting Services.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_1.png)
**Image1**:- dialog konfigurasi SharePoint

Pilih tautan "Reporting Services Integration". Layar berikut akan ditampilkan.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_2.png)
**Image2**:- Tentukan kredensial integrasi Reporting Services

{{% /alert %}}

## URL Layanan Web:

**Kami akan menyediakan URL untuk Report Server yang kami temukan di Reporting Services Configuration Manager.**

## Mode Otentikasi:

**Kami juga akan memilih Mode Otentikasi. Tautan MSDN berikut menjelaskan secara detail apa itu.
Ikhtisar Keamanan untuk Reporting Services dalam Mode Terintegrasi SharePoint**

{{% alert color="primary" %}}

**Singkatnya, jika situs Anda menggunakan Claims Authentication, Anda akan selalu menggunakan Trusted Authentication terlepas dari apa yang Anda pilih di sini. Jika Anda ingin mengirimkan kredensial Windows, Anda harus memilih Windows Authentication. Untuk Trusted Authentication, kami akan mengirim token SPUser dan tidak bergantung pada kredensial Windows. Anda juga ingin menggunakan Trusted Authentication jika Anda telah mengonfigurasi situs Mode Klasik Anda untuk NTLM dan RS diatur untuk NTLM. Kerberos diperlukan untuk menggunakan Windows Authentication dan untuk meneruskannya ke sumber data Anda.**

{{% /alert %}}

## Aktifkan fitur:

{{% alert color="primary" %}}

**Ini memberi Anda opsi untuk mengaktifkan Reporting Services pada semua koleksi Situs, atau Anda dapat memilih mana yang ingin diaktifkan. Ini sebenarnya berarti situs mana yang akan dapat menggunakan Reporting Services. Setelah selesai, Anda akan melihat hasil berikut**

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_3.png)

**Image3:**- Integrasi berhasil Reporting Services dengan lingkungan SharePoint
{{% /alert %}}

{{% alert color="primary" %}}

Kembali ke URL ReportServer, kita harus melihat sesuatu yang mirip dengan berikut

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_4.png)

**Image4:**- Reporting Services berhasil terhubung dengan lingkungan SharePoint

**NOTE:** ***Jika situs SharePoint Anda dikonfigurasi untuk SSL, tidak akan muncul dalam daftar ini. Ini adalah masalah yang diketahui dan tidak berarti ada masalah. Laporan Anda tetap harus berfungsi.***
{{% /alert %}}

{{% alert color="primary" %}}

Sekarang setelah kami berhasil mengintegrasikan kedua produk, kami siap menggunakan Reporting Services di SharePoint 2010. Seperti versi sebelumnya, kami memiliki sebuah fitur (diaktifkan saat kami mengkonfigurasi Reporting Services Integration) di “Site Collection Feature”. Selain itu instalasi menambahkan 3 tipe konten ke situs kami. Pada Image 7 kami dapat melihat 2 tipe konten tersebut ditambahkan di perpustakaan dokumen untuk membuat laporan khusus us ing the, seperti yang dapat kami lihat pada Image5 di bawah.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_5.png)

**Image5:**- Report Builder

“Reporter Builder” adalah kontrol ActiveX sehingga kami perlu mengunduhnya melalui server, seperti yang dapat kami lihat pada Image 6 di bawah.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_6.png)

**Image6:**- Unduh dan instal Report Builder
{{% /alert %}}

{{% alert color="primary" %}}

Setelah proses pengunduhan selesai, muat kontrol “Report Builder”. Sekarang kami siap mendesain laporan pertama kami, seperti yang ditampilkan pada Image7 di bawah.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_7.png)

**Image7:**- Report Builder – Wizard pembuatan Laporan Baru
{{% /alert %}}

{{% alert color="primary" %}}

Setelah membuat laporan kami, kami dapat menyimpannya di perpustakaan dokumen yang dibuat untuk menempatkan laporan di SharePoint 2010 kami. Tipe konten lain harus digunakan untuk membuat koneksi bersama sebagai sumber data dan menyimpannya di perpustakaan dokumen di SharePoint. Kami dapat membuat perpustakaan dokumen, menambahkan tipe konten ini, dan setelah itu kami dapat memiliki koneksi kami tersedia untuk mengubah sumber data laporan.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_8.png)

**Image8:**- Integrasi Berhasil Aspose.PDF untuk Reporting Services dengan MS SharePoint
{{% /alert %}}


