---
title: Menyiapkan Reporting Services
linktitle: Menyiapkan Reporting Services
type: docs
weight: 20
url: /id/reportingservices/setting-up-reporting-services/
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Tahap pertama kami di Server Reporting Services adalah Reporting Services Configuration Manager.

{{% /alert %}}

## Akun Layanan:

**Pastikan Anda memahami akun layanan apa yang Anda gunakan untuk Reporting Services. Jika kita mengalami masalah, mungkin terkait dengan akun layanan yang Anda gunakan. Defaultnya adalah Network Service. Saat kami melakukan penyebaran build baru, kami selalu menggunakan Akun Domain, karena di situlah kemungkinan masalah muncul. Untuk instance server ini, kami telah menggunakan Akun Domain yang disebut RSService.**

![todo:image_alt_text](setting-up-reporting-services_1.png)

**Image1:- Menyiapkan akun layanan**

## URL Layanan Web:

{{% alert color="primary" %}}

**Kami perlu mengonfigurasi URL Layanan Web. Ini adalah direktori virtual ReportServer (vdir) yang menyimpan Web Services yang digunakan Reporting Services, dan yang akan berkomunikasi dengan SharePoint. Kecuali Anda ingin menyesuaikan properti vdir (mis. SSL, port, header host, dll…), Anda cukup dapat mengklik Terapkan di sini dan siap digunakan.**
![todo:image_alt_text](setting-up-reporting-services_2.png)

**Image2:- Menyiapkan URL Layanan Web Setelah URL layanan web diatur, Anda harus dapat melihat hasil berikut**

![todo:image_alt_text](setting-up-reporting-services_3.png)

**Image3:- Penyiapan URL layanan web berhasil**
{{% /alert %}}

## Database:

**Kami perlu membuat Database Katalog Layanan Pelaporan. Ini dapat ditempatkan pada mesin Database SQL 2008 atau SQL 2008 R2 mana pun. SQL11 juga akan berfungsi dengan baik, tetapi masih dalam BETA. Tindakan ini secara default akan membuat dua basis data, ReportServer dan ReportServerTempDB.**

{{% alert color="primary" %}}
**Langkah penting lainnya adalah memastikan Anda memilih SharePoint Integrated untuk jenis basis data. Setelah pilihan ini dibuat, tidak dapat diubah.**

![todo:image_alt_text](setting-up-reporting-services_4.png)

**Image4:- Membuat basis data server laporan**

![todo:image_alt_text](setting-up-reporting-services_5.png)

**Image5:- Menyiapkan server basis data dan jenis autentikasi**

![todo:image_alt_text](setting-up-reporting-services_6.png)

**Image6:- Menyiapkan nama basis data dan Mode**
{{% /alert %}}

**Untuk kredensial, begitulah cara Report Server akan berkomunikasi dengan SQL Server. Akun apa pun yang Anda pilih, akan diberikan hak tertentu dalam basis data Catalog serta beberapa basis data sistem melalui RSExecRole. MSDB adalah salah satu basis data ini untuk penggunaan Subscription karena kami menggunakan SQL Agent.**

![todo:image_alt_text](setting-up-reporting-services_7.png)

**Image7:- Menyiapkan kredensial basis data Report Server**

{{% alert color="primary" %}}

**Setelah kredensial basis data ditentukan, kita harus dapat memperoleh hasil seperti yang ditentukan di bawah ini.**

![todo:image_alt_text](setting-up-reporting-services_8.png)

**Image8:- Progres pembuatan basis data Report Server**

![todo:image_alt_text](setting-up-reporting-services_9.png)

**Image9:- Ringkasan penyelesaian basis data Report Server**
{{% /alert %}}

## URL Report Manager:

**Kita dapat melewatkan URL Report Manager karena tidak digunakan saat kami berada dalam mode Terintegrasi SharePoint. SharePoint adalah frontend kami. Report Manager tidak berfungsi.**

## Kunci Enkripsi:

{{% alert color="primary" %}}
**Cadangkan Kunci Enkripsi Anda dan pastikan Anda tahu di mana menyimpannya. Jika Anda berada dalam situasi di mana Anda perlu memigrasikan Database atau memulihkannya, Anda akan memerlukan ini.**

![todo:image_alt_text](setting-up-reporting-services_10.png)

**Image10:- Cadangan kunci enkripsi Report Server**
{{% /alert %}}

{{% alert color="primary" %}}
**Selamat! Kami telah berhasil mengkonfigurasi Reporting Services menggunakan Configuration Manager. Jika Anda menelusuri ke URL pada tab Web Service URL, seharusnya akan muncul sesuatu yang mirip dengan berikut ini.**

![todo:image_alt_text](setting-up-reporting-services_11.png)

**Image11:- Akses Report Server setelah instalasi**

**Alasan kesalahan: SharePoint diinstal pada WFE kami dan kami telah menyelesaikan pengaturan Reporting Services. Dalam contoh ini, Reporting Services dan SharePoint berada di mesin yang berbeda. Jika mereka berada di mesin yang sama, Anda tidak akan melihat kesalahan ini. Secara teknis kami perlu menginstal SharePoint pada RS Box. Itu berarti IIS juga akan diaktifkan.**
{{% /alert %}}


