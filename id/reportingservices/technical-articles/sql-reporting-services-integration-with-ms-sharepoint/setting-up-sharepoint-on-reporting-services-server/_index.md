---
title: Menyiapkan SharePoint di Server Layanan Pelaporan
linktitle: Setting up SharePoint on Reporting Services Server
type: docs
weight: 30
url: /reportingservices/setting-up-sharepoint-on-reporting-services-server/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Sekarang kita perlu melakukan langkah serupa seperti yang kita lakukan untuk SharePoint WFE. Hal pertama adalah melalui instalasi Prereq uisites dan setelah selesai, mulai pengaturan SharePoint.

{{% /alert %}}

Untuk pengaturan saya memilih Server Farm dan instalasi lengkap agar sesuai dengan SharePoint Box saya, karena saya tidak ingin instalasi mandiri untuk SharePoint.

## Konfigurasi SharePoint

{{% alert color="primary" %}}

**Di Wizard Konfigurasi SharePoint, kami ingin menyambungkan ke farm yang sudah ada.**

![Panduan Konfigurasi SharePoint](setting-up-sharepoint-on-reporting-services-server_1.png)

**Gambar1:- Wizard konfigurasi SharePoint**
{{% /alert %}}

{{% alert color="primary" %}}

**Kami kemudian akan mengarahkannya ke database SharePoint_Config yang digunakan peternakan kami. Jika belum tahu ini dimana, bisa mengetahuinya melalui Admin Pusat melalui Pengaturan Sistem -> Server Manajer di peternakan ini.**

![Basis Data Konfigurasi SharePoint](setting-up-sharepoint-on-reporting-services-server_2.png)

**Gambar2:- Tentukan pengaturan konfigurasi database**

![Panduan Konfigurasi SharePoint](setting-up-sharepoint-on-reporting-services-server_3.png)

**Gambar3:- Wizard konfigurasi SharePoint**
{{% /alert %}}

{{% alert color="primary" %}}

**Setelah wizard selesai, hanya itu yang perlu kita lakukan pada Kotak Server Laporan untuk saat ini. Kembali ke URL ReportServer, kita akan melihat kesalahan lain, tapi itu karena kita belum mengkonfigurasinya melalui Administrator Pusat.**

![Kesalahan Konfigurasi SharePoint](setting-up-sharepoint-on-reporting-services-server_4.png)

**Gambar4:- Laporkan kesalahan server**
{{% /alert %}}
