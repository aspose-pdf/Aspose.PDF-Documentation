---
title: Menyiapkan SharePoint pada Server Reporting Services
linktitle: Menyiapkan SharePoint pada Server Reporting Services
type: docs
weight: 30
url: /id/reportingservices/setting-up-sharepoint-on-reporting-services-server/
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Sekarang kami perlu melakukan langkah-langkah serupa seperti yang kami lakukan untuk SharePoint WFE. Hal pertama adalah melalui instalasi Prereq uisites dan setelah selesai, memulai pengaturan SharePoint.

{{% /alert %}}

Untuk pengaturan, saya memilih Server Farm dan instalasi lengkap untuk menyesuaikan SharePoint Box saya, karena saya tidak menginginkan instalasi terpisah untuk SharePoint.

## Konfigurasi SharePoint

{{% alert color="primary" %}}

**Dalam Wizard Konfigurasi SharePoint, kami ingin terhubung ke farm yang sudah ada.**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_1.png)

**Image1:- Panduan konfigurasi SharePoint**
{{% /alert %}}

{{% alert color="primary" %}}

**Kemudian kami akan mengarahkannya ke basis data SharePoint_Config yang digunakan oleh farm kami. Jika Anda tidak tahu di mana letaknya, Anda dapat menemukannya melalui Central Admin lewat System Settings -> Manager Servers di farm ini.**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_2.png)

**Image2:- Tentukan pengaturan konfigurasi basis data**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_3.png)

**Image3:- Panduan konfigurasi SharePoint**
{{% /alert %}}

{{% alert color="primary" %}}

**Setelah wizard selesai, itu saja yang perlu kita lakukan di Report Server Box untuk saat ini. Kembali ke URL ReportServer, kita akan melihat error lain, tetapi itu karena kita belum mengkonfigurasikannya melalui Central Administrator.**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_4.png)

**Image4:- Kesalahan server laporan**
{{% /alert %}}

