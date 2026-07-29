---
title: Menyiapkan SharePoint di Server Reporting Services
linktitle: Menyiapkan SharePoint di Server Reporting Services
type: docs
weight: 30
url: /id/reportingservices/setting-up-sharepoint-on-reporting-services-server/
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

Sekarang kita perlu melakukan langkah serupa seperti yang kita lakukan untuk SharePoint WFE. Hal pertama adalah menjalani instalasi Prereq uisites dan setelah selesai, memulai penyiapan SharePoint.

{{% /alert %}}

Untuk pengaturan, saya memilih Server Farm dan instalasi lengkap untuk mencocokkan SharePoint Box saya, karena saya tidak menginginkan instalasi mandiri untuk SharePoint.

## Konfigurasi SharePoint

{{% alert color="primary" %}}

**Dalam SharePoint Configuration Wizard, kami ingin terhubung ke farm yang ada.**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_1.png)

**Gambar1:- wizard konfigurasi SharePoint**
{{% /alert %}}

{{% alert color="primary" %}}

**Kami kemudian akan mengarahkannya ke basis data SharePoint_Config yang digunakan oleh farm kami. Jika Anda tidak tahu di mana letaknya, Anda dapat menemukannya melalui Central Admin melalui System Settings -> Manager Servers di farm ini.**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_2.png)

**Gambar2:- Tentukan pengaturan konfigurasi basis data**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_3.png)

**Gambar3:- wizard konfigurasi SharePoint**
{{% /alert %}}

{{% alert color="primary" %}}

**Setelah wizard selesai, itu semua yang perlu kita lakukan pada kotak Report Server untuk saat ini. Kembali ke URL ReportServer, kita akan melihat kesalahan lain, tetapi itu karena kita belum mengkonfigurasinya melalui Central Administrator.**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_4.png)

**Image4:- Kesalahan server laporan**
{{% /alert %}}
