---
title: Mengatur SharePoint pada Server Layanan Pelaporan
type: docs
weight: 30
url: id/reportingservices/setting-up-sharepoint-on-reporting-services-server/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Sekarang kita perlu melakukan langkah-langkah serupa seperti yang kita lakukan untuk SharePoint WFE. Hal pertama adalah melalui instalasi Persyaratan dan setelah selesai, mulai pengaturan SharePoint.

{{% /alert %}}

Untuk pengaturan saya memilih Server Farm dan instalasi lengkap untuk mencocokkan SharePoint Box saya, karena saya tidak ingin instalasi SharePoint yang berdiri sendiri.

## Konfigurasi SharePoint

{{% alert color="primary" %}}

**Dalam Panduan Konfigurasi SharePoint, kita ingin terhubung ke farm yang sudah ada.**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_1.png)

**Gambar1:- Panduan konfigurasi SharePoint**
{{% /alert %}}

{{% alert color="primary" %}}

**Kita kemudian akan mengarahkannya ke database SharePoint_Config yang digunakan oleh farm kita.**
``` If you don't know where this is, you can find out through Central Admin through System Settings -> Manager Servers in this farm.**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_2.png)

**Gambar2:- Tentukan pengaturan konfigurasi database**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_3.png)

**Gambar3:- Wizard konfigurasi SharePoint**
{{% /alert %}}

{{% alert color="primary" %}}

**Setelah wizard selesai, itu semua yang perlu kita lakukan pada Report Server Box untuk saat ini. Kembali ke URL ReportServer, kita akan melihat kesalahan lain, tetapi itu karena kita belum mengkonfigurasinya melalui Central Administrator.**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_4.png)

**Gambar4:- Kesalahan server laporan**
{{% /alert %}}