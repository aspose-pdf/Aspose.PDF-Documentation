---
title: Introduction
type: docs
weight: 10
url: /id/reportingservices/introduction/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Aspose.PDF untuk Reporting Services telah sangat luar biasa untuk pembuatan PDF melalui SQL Reporting Services selama bertahun-tahun dan menyediakan beragam opsi konfigurasi dan parameterisasi yang tidak didukung secara default dalam SQL Reporting Services. Baru-baru ini kami menerima beberapa permintaan terkait Integrasi Aspose.PDF untuk Reporting Services dengan SharePoint. Untuk artikel ini, kami akan fokus pada MS SharePoint 2010. Sebelum kita melangkah lebih jauh, kami mengasumsikan bahwa Anda sudah memiliki pengaturan SharePoint Farm. Dalam contoh ini kami akan menggunakan SharePoint Cloud penuh. Namun langkah-langkahnya serupa untuk SharePoint Foundation Server.

{{% /alert %}}

{{% alert color="primary" %}}

Sebelum kita melangkah lebih jauh, mari kita lihat topik referensi yang telah kami konsultasikan selama persiapan artikel ini.

- [Ikhtisar Integrasi Teknologi Reporting Services dan SharePoint](http://msdn.microsoft.com/en-us/library/bb326358.aspx)
- [Deployment Topologies for Reporting Services in SharePoint Integrated Mode](http://msdn.microsoft.com/en-us/library/bb510781.aspx)
- [Configuring Reporting Services for SharePoint 2010 Integration](http://msdn.microsoft.com/en-us/library/bb326356.aspx)

{{% /alert %}}

## Pengaturan Lingkungan

Pengaturan kami terdiri dari 4 server. Ini termasuk Pengendali Domain, SQL Server, SharePoint Server, dan server untuk Layanan Pelaporan. Anda dapat memilih untuk memiliki SharePoint dan Layanan Pelaporan pada kotak yang sama, yang akan menyederhanakan ini sedikit dan saya akan menunjukkan beberapa perbedaannya.

## Persyaratan Instalasi

{{% alert color="primary" %}}

Add-In Layanan Pelaporan untuk SharePoint adalah salah satu komponen utama untuk membuat Integrasi berfungsi dengan baik. The Add-In needs to be installed on any of the Web Front Ends (WFE) that is in your SharePoint farm along with the Central Admin server. Salah satu perubahan baru dengan SQL 2008 R2 & SharePoint 2010 adalah bahwa Add-In 2008 R2 sekarang menjadi prasyarat untuk Instalasi SharePoint. Ini berarti bahwa RS Add-In akan dipasang saat Anda menginstal SharePoint. Ini telah ditunjukkan dan disorot dalam gambar di bawah ini. Ini sebenarnya menghindari banyak masalah yang kita lihat dengan SP 2007 dan RS 2008 ketika menginstal Add-In.

![todo:image_alt_text](introduction_1.png)

**Image1 :- Reporting Services Add-in for Share Point** {{% /alert %}}

## SharePoint Authentication

**Sebelum kita masuk ke bagian Integrasi RS, satu hal yang ingin saya tekankan tentang SharePoint Farm adalah bagaimana Anda mengatur Situs. Lebih spesifik tentang bagaimana Anda mengonfigurasi autentikasi untuk situs. Apakah akan menjadi Klasik atau Klaim. Pilihan ini penting di awal. Saya tidak percaya bahwa Anda dapat mengubah opsi ini setelah selesai. Jika Anda bisa mengubahnya, itu tidak akan menjadi proses yang sederhana.

CATATAN: ***Layanan Pelaporan 2008 R2 TIDAK mendukung Klaim***

Bahkan jika Anda memilih situs SharePoint Anda untuk menggunakan Klaim, Layanan Pelaporan itu sendiri tidak mendukung Klaim. Namun demikian, itu mempengaruhi bagaimana autentikasi bekerja dengan Layanan Pelaporan. Jadi, apa perbedaannya dari perspektif Layanan Pelaporan? Itu tergantung pada apakah Anda ingin meneruskan Kredensial Pengguna ke sumber data. Klasik:- Dapat menggunakan Kerberos dan meneruskan kredensial pengguna ke sumber data backend Anda (akan perlu menggunakan Kerberos untuk itu). Klaim:- Token Klaim digunakan dan bukan token windows. RS akan selalu menggunakan Autentikasi Terpercaya dalam skenario ini dan hanya akan memiliki akses ke token SPUser. Anda perlu menyimpan kredensial Anda dalam sumber data Anda.

Klasik :- Dapat menggunakan Kerberos dan meneruskan kredensial pengguna ke sumber data backend Anda (akan perlu menggunakan Kerberos untuk itu).
Claims :- Token Klaim digunakan dan bukan token windows. RS akan selalu menggunakan Autentikasi Terpercaya dalam skenario ini dan hanya akan memiliki akses ke token SPUser. Anda perlu menyimpan kredensial Anda dalam sumber data Anda.

Untuk saat ini, kami hanya ingin fokus pada pengaturan RS. Pada titik ini, SharePoint telah diinstal pada SharePoint Box saya dan diatur dengan Situs Autentikasi Klasik pada port 80. Di Server RS, saya baru saja menginstal Layanan Pelaporan dan hanya itu.