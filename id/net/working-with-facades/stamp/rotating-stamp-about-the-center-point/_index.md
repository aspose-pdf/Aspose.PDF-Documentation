---
title: Memutar stempel di sekitar titik pusat
type: docs
weight: 10
url: id/net/rotating-stamp-about-the-center-point/
description: Bagian ini menjelaskan cara memutar stempel di sekitar titik pusat menggunakan Kelas Stamp.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

[Namespace Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) dalam [Aspose.PDF for .NET](/pdf/net/) memungkinkan Anda menambahkan stempel dalam file PDF yang sudah ada. Terkadang, pengguna perlu memutar stempel tersebut. Dalam artikel ini, kita akan melihat cara memutar stempel di sekitar titik pusatnya.

{{% /alert %}}

## Rincian implementasi

[Kelas Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) memungkinkan Anda menambahkan watermark dalam file PDF. Anda dapat menentukan gambar untuk ditambahkan sebagai stempel menggunakan metode [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.stamp/bindimage/methods/1). Metode [SetOrigin](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/setorigin) memungkinkan Anda untuk mengatur asal dari stempel yang ditambahkan; asal ini adalah koordinat kiri bawah dari stempel. Anda juga dapat mengatur ukuran gambar menggunakan metode [SetImageSize](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/setimagesize).

Sekarang, kita lihat bagaimana stempel dapat diputar di sekitar pusat stempel. [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) kelas menyediakan properti bernama Rotation. Properti ini mengatur atau mendapatkan rotasi dari 0 hingga 360 dari konten stempel. Kita dapat menentukan nilai rotasi apa pun dari 0 hingga 360. Dengan menentukan nilai rotasi, kita dapat memutar stempel sekitar titik pusatnya. Jika Stamp adalah objek dari tipe Stamp maka nilai rotasi dapat ditentukan sebagai aStamp.Rotation = 90. Dalam kasus ini, stempel akan diputar pada 90 derajat sekitar pusat konten stempel. Cuplikan kode berikut menunjukkan kepada Anda cara memutar stempel sekitar titik pusat:



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-RotatingStamp-RotatingStamp.cs" >}}