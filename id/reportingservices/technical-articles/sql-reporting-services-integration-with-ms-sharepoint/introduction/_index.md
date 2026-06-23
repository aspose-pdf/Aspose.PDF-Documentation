---
title: Pengantar
linktitle: Pengantar
type: docs
weight: 10
url: /id/reportingservices/introduction/
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Aspose.PDF for Reporting Services telah sangat luar biasa untuk pembuatan PDF melalui SQL Reporting Services selama bertahun‑tahun dan menyediakan opsi konfigurasi serta parametrisasi yang beragam yang tidak didukung secara default di SQL Reporting Services. Baru-baru ini kami menerima beberapa permintaan terkait Integrasi Aspose.PDF for Reporting Services dengan SharePoint. Untuk artikel ini, kami akan fokus pada MS SharePoint 2010. Sebelum kami melanjutkan, kami mengasumsikan Anda sudah memiliki setup SharePoint Farm. Dalam contoh ini kami akan menggunakan SharePoint Cloud penuh. Namun langkah‑langkahnya serupa untuk SharePoint Foundation Server.

{{% /alert %}}

{{% alert color="primary" %}}

Sebelum kami melanjutkan lebih jauh, mari kita lihat topik referensi yang telah kami konsultasikan selama persiapan artikel ini.

- [Gambaran Umum Integrasi Layanan Pelaporan dan Teknologi SharePoint](http://msdn.microsoft.com/en-us/library/bb326358.aspx)
- [Topologi Penyebaran untuk Reporting Services dalam Mode Terintegrasi SharePoint](http://msdn.microsoft.com/en-us/library/bb510781.aspx)
- [Mengonfigurasi Reporting Services untuk Integrasi SharePoint 2010](http://msdn.microsoft.com/en-us/library/bb326356.aspx)

{{% /alert %}}

## Penyiapan Lingkungan

Penyiapan kami terdiri dari 4 server. Itu mencakup sebuah Domain Controller, sebuah SQL Server, sebuah SharePoint Server, dan sebuah server untuk Reporting Services. Anda dapat memilih untuk menempatkan SharePoint dan Reporting Services pada satu kotak yang sama, yang akan menyederhanakan ini sedikit dan saya akan menunjukkan beberapa perbedaannya.

## Prasyarat Instalasi

{{% alert color="primary" %}}

Add-In Reporting Services untuk SharePoint adalah salah satu komponen utama untuk membuat Integrasi berfungsi dengan baik. Add-In harus diinstal pada salah satu Web Front Ends (WFE) yang berada di farm SharePoint Anda bersama dengan server Central Admin. Salah satu perubahan baru dengan SQL 2008 R2 & SharePoint 2010 adalah bahwa Add-In 2008 R2 kini menjadi prasyarat untuk Instalasi SharePoint. Ini berarti bahwa RS Add-In akan dipasang ketika Anda menginstal SharePoint. Hal ini telah ditampilkan dan disorot pada gambar di bawah. Ini sebenarnya menghindari banyak masalah yang kami temui dengan SP 2007 dan RS 2008 saat menginstal Add-In.

![todo:image_alt_text](introduction_1.png)

**Image1 :- Add-in Reporting Services untuk Share Point**
{{% /alert %}}

## Otentikasi SharePoint

**Sebelum kita melompat ke bagian Integrasi RS, ada satu hal yang ingin saya sampaikan tentang SharePoint Farm yaitu cara Anda menyiapkan Situs. Lebih spesifik lagi cara Anda mengonfigurasi otentikasi untuk situs tersebut. Apakah akan menggunakan Classic atau Claims. Pilihan ini penting di awal. Saya tidak percaya Anda dapat mengubah opsi ini setelah selesai. Jika dapat mengubahnya, prosesnya tidak akan sederhana.**

CATATAN: ***Reporting Services 2008 R2 tidak mendukung Claims***

Meskipun Anda memilih situs SharePoint Anda untuk menggunakan Claims, Reporting Services itu sendiri tidak mendukung Claims. Meski begitu, hal ini memengaruhi cara otentikasi bekerja dengan Reporting Services. Jadi, apa perbedaannya dari perspektif Reporting Services? Semua tergantung pada apakah Anda ingin meneruskan Kredensial Pengguna ke sumber data. Classic:- Dapat menggunakan Kerberos dan meneruskan kredensial pengguna ke datasource back‑end Anda (akan perlu menggunakan Kerberos untuk itu). Claims:- Token Claims yang digunakan, bukan token Windows. RS akan selalu menggunakan Trusted Authentication dalam skenario ini dan hanya akan memiliki akses ke token SPUser. Anda perlu menyimpan kredensial Anda di dalam sumber data.

Classic :- Dapat menggunakan Kerberos dan meneruskan kredensial pengguna ke datasource back end Anda (akan perlu menggunakan Kerberos untuk itu.

Claims :- Token Claims yang digunakan, bukan token Windows. RS akan selalu menggunakan Trusted Authentication dalam skenario ini dan hanya akan memiliki akses ke token SPUser. Anda perlu menyimpan kredensial Anda di dalam sumber data.

Untuk saat ini kami hanya ingin fokus pada pengaturan RS. Pada titik ini SharePoint telah terinstal di SharePoint Box saya dan diatur dengan Situs Autentikasi Klasik pada port 80. Di Server RS saya baru saja menginstal Reporting Services dan itu saja.

