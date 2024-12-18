---
title: Mengatur Layanan Pelaporan
type: docs
weight: 20
url: /id/reportingservices/setting-up-reporting-services/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Pemberhentian pertama kami di Server Layanan Pelaporan adalah Pengelola Konfigurasi Layanan Pelaporan.

{{% /alert %}}

## Akun Layanan:

**Pastikan untuk memahami akun layanan apa yang Anda gunakan untuk Layanan Pelaporan. Jika kita menghadapi masalah, itu mungkin terkait dengan akun layanan yang Anda gunakan. Defaultnya adalah Network Service. Ketika kita akan menerapkan build baru, kita selalu menggunakan Akun Domain, karena di situlah kita kemungkinan akan menghadapi masalah. Untuk instance server ini, kami telah menggunakan Akun Domain yang disebut RSService.**

![todo:image_alt_text](setting-up-reporting-services_1.png)

**Gambar1:- Mengatur akun layanan**

## URL Layanan Web:

{{% alert color="primary" %}}

**Kita perlu mengkonfigurasi URL Layanan Web. This is the ReportServer virtual directory (vdir) yang menjadi host Layanan Web yang digunakan oleh Reporting Services, dan yang akan berkomunikasi dengan SharePoint. Kecuali Anda ingin menyesuaikan properti vdir (misalnya SSL, port, header host, dll...), Anda seharusnya dapat mengklik Terapkan di sini dan siap untuk melanjutkan.**

![todo:image_alt_text](setting-up-reporting-services_2.png)

**Image2:- Mengatur URL Layanan Web Setelah URL layanan web disiapkan, Anda seharusnya dapat melihat hasil berikut**

![todo:image_alt_text](setting-up-reporting-services_3.png)

**Image3:- Pengaturan URL layanan web berhasil**
{{% /alert %}}

## Database:

**Kita perlu membuat Database Katalog Layanan Pelaporan. Ini dapat ditempatkan pada Mesin Database SQL 2008 atau SQL 2008 R2 mana pun. SQL11 juga akan bekerja dengan baik, tetapi itu masih dalam versi BETA. Tindakan ini secara default akan membuat dua database, ReportServer dan ReportServerTempDB.**

{{% alert color="primary" %}}
**Langkah penting lainnya adalah memastikan bahwa Anda memilih SharePoint Integrated untuk jenis database.  Setelah pilihan ini dibuat, itu tidak dapat diubah.**

![todo:image_alt_text](setting-up-reporting-services_4.png)

**Gambar4:- Membuat database server laporan**

![todo:image_alt_text](setting-up-reporting-services_5.png)

**Gambar5:- Menyiapkan server database dan jenis otentikasi**

![todo:image_alt_text](setting-up-reporting-services_6.png)

**Gambar6:- Menyiapkan nama database dan Mode**
{{% /alert %}}

**Untuk kredensial, inilah cara Server Laporan akan berkomunikasi dengan SQL Server. Akun apa pun yang Anda pilih, akan diberikan hak tertentu di dalam database Katalog serta beberapa database sistem melalui RSExecRole. MSDB adalah salah satu dari database ini untuk penggunaan Langganan saat kami menggunakan Agen SQL.**

![todo:image_alt_text](setting-up-reporting-services_7.png)

**Gambar7:- Menyiapkan kredensial database Server Laporan**

{{% alert color="primary" %}}

**Setelah kredensial database ditentukan, kita seharusnya bisa mendapatkan hasil seperti yang ditentukan di bawah ini.**


![todo:image_alt_text](setting-up-reporting-services_8.png)
**Image8:- Kemajuan pembuatan database Report Server**

![todo:image_alt_text](setting-up-reporting-services_9.png)

**Image9:- Ringkasan penyelesaian database Report Server**
{{% /alert %}}

## URL Report Manager:

**Kita dapat melewati URL Report Manager karena tidak digunakan saat kita berada dalam mode Terintegrasi SharePoint. SharePoint adalah frontend kita. Report Manager tidak berfungsi.**

## Kunci Enkripsi:

{{% alert color="primary" %}}
**Cadangkan Kunci Enkripsi Anda dan pastikan Anda tahu di mana Anda menyimpannya. Jika Anda menghadapi situasi di mana Anda perlu memigrasikan Database atau memulihkannya, Anda akan memerlukan ini.**

![todo:image_alt_text](setting-up-reporting-services_10.png)

**Image10:- Cadangan kunci Enkripsi Report Server**
{{% /alert %}}

{{% alert color="primary" %}}
**Selamat! Kami telah berhasil mengkonfigurasi Reporting Services menggunakan Configuration Manager. Jika Anda menelusuri URL pada tab Web Service URL, itu harus menunjukkan sesuatu yang mirip dengan yang berikut.**

![todo:image_alt_text](setting-up-reporting-services_11.png)

**Image11:- Akses Server Laporan setelah instalasi**

**Reason of error: SharePoint diinstal pada WFE kami dan kami selesai mengatur Layanan Pelaporan. Dalam contoh ini, Layanan Pelaporan dan SharePoint berada di mesin yang berbeda. Jika mereka berada di mesin yang sama, Anda tidak akan melihat kesalahan ini. Secara teknis, kita perlu menginstal SharePoint pada Kotak RS. Itu berarti IIS juga akan diaktifkan.**  
{{% /alert %}}