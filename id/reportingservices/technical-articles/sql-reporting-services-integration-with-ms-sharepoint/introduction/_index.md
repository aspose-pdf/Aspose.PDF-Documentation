---
title: Pendahuluan
linktitle: Pendahuluan
type: docs
weight: 10
url: /id/reportingservices/introduction/
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

Aspose.PDF for Reporting Services telah sangat luar biasa untuk pembuatan PDF melalui SQL Reporting Services selama bertahun‑tahun dan menyediakan beragam opsi konfigurasi serta parameterisasi yang tidak didukung secara default di SQL Reporting Services. Baru-baru ini kami menerima beberapa permintaan terkait Integrasi Aspose.PDF for Reporting Services dengan SharePoint. Untuk artikel ini, kami akan fokus pada MS SharePoint 2010. Sebelum kami melanjutkan lebih jauh, kami mengasumsikan bahwa Anda sudah memiliki setup SharePoint Farm. Dalam contoh ini kami akan menggunakan SharePoint Cloud penuh. Namun langkah‑langkahnya serupa untuk SharePoint Foundation Server.

{{% /alert %}}

{{% alert color="primary" %}}

Sebelum kami melanjutkan lebih jauh, mari kita lihat topik referensi yang telah kami konsultasikan selama persiapan artikel ini.

- [Gambaran Umum Integrasi Teknologi Reporting Services dan SharePoint](http://msdn.microsoft.com/en-us/library/bb326358.aspx)
- [Topologi Penempatan untuk Reporting Services dalam Mode Terintegrasi SharePoint](http://msdn.microsoft.com/en-us/library/bb510781.aspx)
- [Mengonfigurasi Reporting Services untuk Integrasi SharePoint 2010](http://msdn.microsoft.com/en-us/library/bb326356.aspx)

{{% /alert %}}

## Penyiapan Lingkungan

Penyiapan kami terdiri dari 4 server. Ini mencakup Domain Controller, SQL Server, Server SharePoint, dan server untuk Reporting Services. Anda dapat memilih untuk menempatkan SharePoint dan Reporting Services pada satu mesin yang sama, yang akan menyederhanakan ini sedikit dan saya akan menunjukkan beberapa perbedaan.

## Pra-syarat Instalasi

{{% alert color="primary" %}}

Add‑In Reporting Services untuk SharePoint adalah salah satu komponen kunci agar Integrasi berfungsi dengan baik. Add‑In ini perlu diinstal pada setiap Web Front End (WFE) yang ada di farm SharePoint Anda bersama dengan server Central Admin. Salah satu perubahan baru dengan SQL 2008 R2 \u0026 SharePoint 2010 adalah bahwa Add‑In 2008 R2 kini menjadi pra‑syarat untuk Instalasi SharePoint. Ini berarti Add‑In RS akan dipasang ketika Anda menginstal SharePoint. Hal ini telah ditunjukkan dan disorot pada gambar di bawah. Hal ini sebenarnya menghindari banyak masalah yang kami temui dengan SP 2007 dan RS 2008 saat menginstal Add‑In.

![todo:image_alt_text](introduction_1.png)

**Image1 :- Reporting Services Add-in untuk Share Point**
{{% /alert %}}

## Autentikasi SharePoint

**Sebelum kita melompat ke bagian Integrasi RS, ada satu hal yang ingin saya soroti tentang SharePoint Farm, yaitu bagaimana Anda menyiapkan Situs. Lebih khusus lagi, bagaimana Anda mengkonfigurasi autentikasi untuk situs tersebut. Apakah akan menggunakan Classic atau Claims. Pilihan ini penting di awal. Saya tidak percaya Anda dapat mengubah opsi ini setelah selesai. Jika Anda dapat mengubahnya, prosesnya tidak akan sederhana.**

NOTE: ***Reporting Services 2008 R2 tidak mendukung Claims***

Meskipun Anda memilih situs SharePoint Anda untuk menggunakan Claims, Reporting Services sendiri tidak mengenal Claims. Namun, hal ini memengaruhi cara otentikasi bekerja dengan Reporting Services. Jadi, apa perbedaannya dari perspektif Reporting Services? Itu tergantung pada apakah Anda ingin meneruskan Kredensial Pengguna ke sumber data. Classic:- Dapat menggunakan Kerberos dan meneruskan kredensial pengguna ke datasource backend Anda (akan memerlukan Kerberos untuk itu). Claims:- Token Claims digunakan dan bukan token Windows. RS akan selalu menggunakan Trusted Authentication dalam skenario ini dan hanya akan memiliki akses ke token SPUser. Anda perlu menyimpan kredensial Anda di dalam sumber data.

Classic :- Dapat menggunakan Kerberos dan meneruskan kredensial pengguna ke datasource backend Anda (akan memerlukan Kerberos untuk itu.

Claims :- Token Claims digunakan dan bukan token Windows. RS akan selalu menggunakan Trusted Authentication dalam skenario ini dan hanya akan memiliki akses ke token SPUser. Anda perlu menyimpan kredensial Anda di dalam sumber data.

Untuk saat ini kami hanya ingin fokus pada penyiapan RS. Pada titik ini SharePoint telah diinstal di SharePoint Box saya dan dikonfigurasi dengan Situs Autentikasi Klasik pada port 80. Di server RS saya baru saja menginstal Reporting Services dan itu saja.
