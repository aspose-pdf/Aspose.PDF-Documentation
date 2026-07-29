---
title: Menyiapkan Reporting Services
linktitle: Menyiapkan Reporting Services
type: docs
weight: 20
url: /id/reportingservices/setting-up-reporting-services/
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

Pemberhentian pertama kami di Server Reporting Services adalah Reporting Services Configuration Manager.

{{% /alert %}}

## Akun Layanan:

**Pastikan Anda mengerti akun layanan apa yang Anda gunakan untuk Reporting Services. Jika kami mengalami masalah, hal itu mungkin terkait dengan akun layanan yang Anda gunakan. Defaultnya adalah Network Service. Saat kami melakukan penyebaran build baru, kami selalu menggunakan Domain Account, karena di situlah kami cenderung mengalami masalah. Untuk instance server ini, kami menggunakan Domain Account yang disebut RSService.**

![todo:image_alt_text](setting-up-reporting-services_1.png)

**Image1:- Menyiapkan akun layanan**

## URL Layanan Web:

{{% alert color="primary" %}}

**Kami perlu mengkonfigurasi URL Layanan Web. Ini adalah direktori virtual ReportServer (vdir) yang menampung Layanan Web yang digunakan Reporting Services, dan yang akan berkomunikasi dengan SharePoint. Kecuali Anda ingin menyesuaikan properti vdir (mis. SSL, port, header host, dll…), Anda cukup dapat mengklik Apply di sini dan siap digunakan.**
![todo:image_alt_text](setting-up-reporting-services_2.png)

**Image2:- Menyiapkan URL Layanan Web Setelah URL layanan Web disiapkan, Anda seharusnya dapat melihat hasil berikut**

![todo:image_alt_text](setting-up-reporting-services_3.png)

**Image3:- Pengaturan URL layanan Web berhasil**
{{% /alert %}}

## Database:

**Kita perlu membuat Database Katalog Reporting Services. Ini dapat ditempatkan pada Mesin Database SQL 2008 atau SQL 2008 R2 mana saja. SQL11 juga akan berfungsi dengan baik, tetapi masih dalam BETA. Tindakan ini secara default akan membuat dua basis data, ReportServer dan ReportServerTempDB.**

{{% alert color="primary" %}}
**Langkah penting lainnya adalah memastikan bahwa Anda memilih SharePoint Integrated untuk tipe basis data. Setelah pilihan ini dibuat, tidak dapat diubah.**

![todo:image_alt_text](setting-up-reporting-services_4.png)

**Image4:- Membuat database server laporan**

![todo:image_alt_text](setting-up-reporting-services_5.png)

**Image5:- Menyiapkan server basis data dan tipe otentikasi**

![todo:image_alt_text](setting-up-reporting-services_6.png)

**Image6:- Menyiapkan nama basis data dan Mode**
{{% /alert %}}

**Untuk kredensial, inilah cara Report Server berkomunikasi dengan SQL Server. Akun apa pun yang Anda pilih, akan diberikan hak tertentu dalam basis data Catalog serta beberapa basis data sistem melalui RSExecRole. MSDB adalah salah satu basis data ini untuk penggunaan Langganan karena kami menggunakan SQL Agent.**

![todo:image_alt_text](setting-up-reporting-services_7.png)

**Image7:- Menyiapkan kredensial basis data Report Server**

{{% alert color="primary" %}}

**Setelah kredensial basis data ditentukan, kita seharusnya dapat memperoleh hasil sebagaimana dijelaskan di bawah ini.**

![todo:image_alt_text](setting-up-reporting-services_8.png)

**Image8:- Progres pembuatan basis data Report Server**

![todo:image_alt_text](setting-up-reporting-services_9.png)

**Image9:- Ringkasan penyelesaian basis data Report Server**
{{% /alert %}}

## URL Report Manager:

**Kita dapat melewatkan URL Report Manager karena tidak digunakan ketika kita berada dalam mode Terintegrasi SharePoint. SharePoint adalah frontend kita. Report Manager tidak berfungsi.**

## Kunci Enkripsi:

{{% alert color="primary" %}}
**Cadangkan Kunci Enkripsi Anda dan pastikan Anda tahu di mana Anda menyimpannya. Jika Anda berada dalam situasi di mana Anda perlu memigrasi Database atau mengembalikannya, Anda akan memerlukan kunci ini.**

![todo:image_alt_text](setting-up-reporting-services_10.png)

**Image10:- Cadangan kunci enkripsi Report Server**
{{% /alert %}}

{{% alert color="primary" %}}
**Selamat! Kami telah berhasil mengkonfigurasi Reporting Services menggunakan Configuration Manager. Jika Anda membuka URL pada tab Web Service URL, itu akan menampilkan sesuatu yang mirip dengan berikut.**

![todo:image_alt_text](setting-up-reporting-services_11.png)

**Image11:- Akses Report Server setelah instalasi**

**Alasan kesalahan: SharePoint diinstal di WFE kami dan kami telah menyelesaikan penyiapan Reporting Services. Dalam contoh ini, Reporting Services dan SharePoint berada di mesin yang berbeda. Jika mereka berada pada mesin yang sama, Anda tidak akan melihat kesalahan ini. Secara teknis kami harus menginstal SharePoint pada RS Box. Itu berarti IIS juga akan diaktifkan.**
{{% /alert %}}

