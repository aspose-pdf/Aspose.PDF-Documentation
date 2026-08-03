---
title: Perkenalan
linktitle: Introduction
type: docs
weight: 10
url: /reportingservices/introduction/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Aspose.PDF untuk Layanan Pelaporan telah sangat luar biasa untuk pembuatan PDF melalui Layanan Pelaporan SQL sejak bertahun-tahun dan menyediakan beragam opsi konfigurasi dan parameterisasi yang tidak didukung secara default di Layanan Pelaporan SQL. Baru-baru ini kami menerima beberapa permintaan mengenai Aspose.PDF untuk Integrasi Layanan Pelaporan dengan SharePoint. Untuk artikel ini, kami akan fokus pada MS SharePoint 2010. Sebelum melanjutkan lebih jauh, kami berasumsi bahwa Anda sudah memiliki pengaturan SharePoint Farm. Dalam contoh ini kita akan menggunakan SharePoint Cloud lengkap. Namun langkah-langkahnya serupa untuk SharePoint Foundation Server.

{{% /alert %}}

{{% alert color="primary" %}}

Sebelum melangkah lebih jauh, mari kita lihat topik referensi yang telah kita konsultasikan selama persiapan artikel ini.

- [Ikhtisar Layanan Pelaporan dan Integrasi Teknologi SharePoint](http://msdn.microsoft.com/en-us/library/bb326358.aspx)
- [Topologi Penerapan untuk Layanan Pelaporan dalam Mode Terintegrasi SharePoint](http://msdn.microsoft.com/en-us/library/bb510781.aspx)
- [Mengonfigurasi Layanan Pelaporan untuk Integrasi SharePoint 2010](http://msdn.microsoft.com/en-us/library/bb326356.aspx)

{{% /alert %}}

## Pengaturan Lingkungan

Setup keluar terdiri dari 4 server. Ini mencakup Pengontrol Domain, SQL Server, SharePoint Server dan server untuk Layanan Pelaporan. Anda dapat memilih untuk memiliki SharePoint dan Layanan Pelaporan pada kotak yang sama, yang akan sedikit menyederhanakannya dan saya akan menunjukkan beberapa perbedaannya.

## Prasyarat Instalasi

{{% alert color="primary" %}}

Add-In Layanan Pelaporan untuk SharePoint adalah salah satu komponen kunci agar Integrasi berfungsi dengan baik. Add-In harus diinstal di Web Front End (WFE) mana pun yang ada di farm SharePoint Anda bersama dengan server Admin Pusat. Salah satu perubahan baru pada SQL 2008 R2 & SharePoint 2010 adalah Add-In 2008 R2 kini menjadi prasyarat untuk Penginstalan SharePoint. Ini berarti RS Add-In akan dipasang saat Anda menginstal SharePoint. Itu telah ditunjukkan dan disorot pada gambar di bawah. Hal ini sebenarnya menghindari banyak masalah yang kita lihat dengan SP 2007 dan RS 2008 saat menginstal Add-In.

![Introduction](introduction_1.png)

**Gambar1 :- Add-in Layanan Pelaporan untuk Share Point**
{{% /alert %}}

## Otentikasi SharePoint

**Sebelum kita beralih ke bagian Integrasi RS, satu hal yang ingin saya tunjukkan tentang SharePoint Farm adalah cara Anda menyiapkan Situs. Lebih khusus lagi bagaimana Anda mengonfigurasi otentikasi untuk situs tersebut. Baik itu Klasik atau Klaim. Pilihan ini penting pada awalnya. Saya tidak yakin Anda dapat mengubah opsi ini setelah selesai. Jika Anda bisa mengubahnya, itu bukanlah proses yang sederhana.

CATATAN: ***Layanan Pelaporan 2008 R2 TIDAK mengetahui Klaim***

Meskipun Anda memilih situs SharePoint untuk menggunakan Klaim, Layanan Pelaporan itu sendiri tidak mengetahui Klaim. Meskipun demikian, hal ini memengaruhi cara kerja autentikasi dengan Layanan Pelaporan. Lantas, apa bedanya dari perspektif Reporting Services? Tergantung apakah Anda ingin meneruskan Kredensial Pengguna ke sumber data. Klasik:- Dapat menggunakan Kerberos dan meneruskan kredensial pengguna ke sumber data back end Anda (perlu menggunakan Kerberos untuk itu). Klaim:- Token Klaim digunakan dan bukan token windows. RS akan selalu menggunakan Otentikasi Tepercaya dalam skenario ini dan hanya akan memiliki akses ke token SPUser. Anda perlu menyimpan kredensial Anda dalam sumber data Anda.

Klasik :- Dapat menggunakan Kerberos dan meneruskan kredensial pengguna ke sumber data back end Anda (perlu menggunakan Kerberos untuk itu.

Klaim :- Token Klaim digunakan dan bukan token windows. RS akan selalu menggunakan Otentikasi Tepercaya dalam skenario ini dan hanya akan memiliki akses ke token SPUser. Anda perlu menyimpan kredensial Anda dalam sumber data Anda.

Untuk saat ini kami hanya ingin fokus pada setup RS. Pada titik ini SharePoint diinstal pada Kotak SharePoint saya dan diatur dengan Situs Auth Klasik pada port 80. Di Server RS ​​saya baru saja menginstal Layanan Pelaporan dan hanya itu.
