---
title: Cara Menginstal Aspose.PDF untuk .NET
linktitle: Instalasi
type: docs
weight: 20
url: id/net/installation/
description: Bagian ini menunjukkan deskripsi produk dan instruksi untuk menginstal Aspose.PDF untuk .Net sendiri, serta menggunakan NuGet.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Komponen Aspose.PDF C#

{{% alert color="primary" %}}

**Aspose.PDF adalah komponen .NET** yang dibangun untuk memungkinkan pengembang membuat dokumen PDF, entah itu sederhana atau kompleks, secara programatis secara langsung. Aspose.PDF untuk .NET memungkinkan pengembang untuk memasukkan tabel, grafik, gambar, hyperlink, font kustom - dan lebih banyak lagi - ke dalam dokumen PDF. Selain itu, juga dimungkinkan untuk mengompres dokumen PDF. Aspose.PDF untuk .NET menyediakan fitur keamanan yang sangat baik untuk mengembangkan dokumen PDF yang aman. Dan fitur paling berbeda dari Aspose.PDF untuk .NET adalah bahwa ia mendukung pembuatan dokumen PDF melalui API dan dari template XML.

{{% /alert %}}

## Deskripsi Produk

**Aspose.PDF untuk .NET** adalah komponen .NET yang kuat yang memungkinkan pengembang membuat dokumen PDF dari awal tanpa menggunakan Adobe Acrobat.
**Aspose.PDF for .NET** adalah komponen .NET yang kuat yang memungkinkan pengembang membuat dokumen PDF dari awal tanpa menggunakan Adobe Acrobat.

**Aspose.PDF for .NET** diimplementasikan menggunakan Managed C# dan dapat digunakan dengan bahasa .NET apa pun seperti C#, VB.NET dan J# dll. Ini dapat diintegrasikan dengan jenis aplikasi apa pun baik itu Aplikasi Web ASP.NET atau Aplikasi Windows.

Agar para pengembang dapat segera memulai, Aspose.PDF for .NET menyediakan demo dan contoh kerja yang lengkap ditulis dalam C#. Dengan menggunakan demo ini, pengembang dapat dengan cepat mempelajari fitur-fitur yang disediakan oleh Aspose.PDF for .NET.

Komponen yang cepat dan ringan ini membuat dokumen PDF secara efisien dan membantu aplikasi Anda berkinerja lebih baik. Aspose.PDF for .NET adalah pilihan pertama pelanggan kami ketika membuat dokumen PDF karena harganya, kinerja yang luar biasa, dan dukungan yang hebat.

**Aspose.PDF for .NET** aman multithread selama hanya satu thread yang bekerja pada dokumen pada satu waktu.
**Aspose.PDF for .NET** aman untuk multithread selama hanya satu thread yang bekerja pada dokumen pada satu waktu.

## Deklarasi

Semua komponen Aspose .NET memerlukan set izin Full Trust. Alasannya adalah, komponen Aspose .NET perlu mengakses pengaturan registry, file sistem selain direktori virtual untuk beberapa operasi seperti parsing font dll. Selain itu, Komponen Aspose .NET berdasarkan kelas sistem inti .NET yang juga memerlukan set izin Full Trust dalam banyak kasus.

Penyedia Layanan Internet yang menghosting banyak aplikasi dari berbagai perusahaan kebanyakan menerapkan tingkat keamanan Medium Trust. Dalam kasus .NET 2.0, tingkat keamanan tersebut memberlakukan batasan berikut:

- **OleDbPermission tidak tersedia.** Ini berarti Anda tidak dapat menggunakan penyedia data OLE DB yang dikelola ADO.NET untuk mengakses basis data.
- **EventLogPermission tidak tersedia.** Ini berarti Anda tidak dapat mengakses log event Windows.
- **ReflectionPermission tidak tersedia.** Ini berarti Anda tidak dapat menggunakan refleksi.
- **RegistryPermission tidak tersedia.** Ini berarti Anda tidak dapat mengakses registry.

- **RegistryPermission tidak tersedia.** Ini berarti Anda tidak dapat mengakses registri.
- **WebPermission dibatasi.** Ini berarti aplikasi Anda hanya dapat berkomunikasi dengan alamat atau rentang alamat yang Anda tentukan dalam elemen `<trust>`.
- **FileIOPermission dibatasi.** Ini berarti Anda hanya dapat mengakses file dalam hierarki direktori virtual aplikasi Anda.
Karena alasan yang disebutkan di atas, komponen Aspose .NET tidak dapat digunakan pada server yang memberikan set izin selain Full Trust.

# Instalasi

## Evaluasi Aspose.PDF untuk .NET

Anda dapat dengan mudah mengunduh Aspose.PDF untuk .Net untuk evaluasi. Unduhan evaluasi sama dengan unduhan yang dibeli. Versi evaluasi hanya menjadi berlisensi ketika Anda menambahkan beberapa baris kode untuk menerapkan lisensi.

Versi evaluasi Aspose.PDF (tanpa lisensi yang ditentukan) menyediakan fungsionalitas produk penuh, tetapi memiliki dua batasan: menyisipkan watermark evaluasi, dan hanya empat elemen dari setiap koleksi yang dapat dilihat/diedit.

{{% alert color="primary" %}}

Jika Anda ingin mencoba Aspose.PDF untuk .NET tanpa batasan versi evaluasi, Anda juga dapat meminta Lisensi Sementara selama 30 hari. Silakan merujuk ke [Cara mendapatkan Lisensi Sementara?](https://purchase.aspose.com/temporary-license)

{{% /alert %}}

## Menginstal Aspose.PDF untuk .NET melalui NuGet

NuGet adalah sistem manajemen paket yang gratis, open source dan berfokus pada pengembang untuk platform .NET yang bertujuan untuk menyederhanakan proses memasukkan pustaka pihak ketiga ke dalam aplikasi .NET selama pengembangan.
NuGet adalah sistem manajemen paket yang berfokus pada pengembang dan bersifat open source dan gratis untuk platform .NET yang bertujuan untuk mempermudah proses memasukkan pustaka pihak ketiga ke dalam aplikasi .NET selama pengembangan.

### Merujuk Aspose.PDF untuk .NET

#### Memasang paket menggunakan Konsol Manajer Paket

- Buka aplikasi .NET Anda di Visual Studio.
- Di menu Alat, pilih **Manajer Paket NuGet** lalu **Konsol Manajer Paket**.
- Ketik perintah `Install-Package Aspose.PDF` untuk memasang rilis penuh terbaru, atau ketik perintah `Install-Package Aspose.PDF -prerelease` untuk memasang rilis terbaru termasuk perbaikan mendesak.
- Tekan `Enter`

#### Memperbarui paket menggunakan Konsol Manajer Paket

Jika Anda telah merujuk komponen melalui NuGet, ikuti langkah-langkah ini untuk memperbarui rujukan ke versi terbaru:

- Buka aplikasi .NET Anda di Visual Studio.
- Di menu Alat, pilih **Manajer Paket NuGet** lalu **Konsol Manajer Paket**.
- Ketik perintah `Update-Package Aspose.PDF` untuk merujuk rilis penuh terbaru, atau ketik perintah `Update-Package Aspose.PDF -prerelease` untuk memasang rilis terbaru termasuk perbaikan mendesak.
- Ketik perintah `Update-Package Aspose.PDF` untuk merujuk rilis penuh terbaru, atau ketik perintah `Update-Package Aspose.PDF -prerelease` untuk menginstal rilis terbaru termasuk perbaikan mendesak.

#### Pasang Paket menggunakan Antarmuka Pengguna Manajer Paket

Ikuti langkah-langkah ini untuk merujuk komponen menggunakan antarmuka pengguna manajer paket:

- Buka aplikasi .NET Anda di Visual Studio.

- Dari menu Proyek pilih **Kelola Paket NuGet**.

![Installation_step](../images/install_step.png)

- Pilih tab **Browse**.

![Installation_step1](../images/install_step1.png)

- Ketik Aspose.PDF ke dalam kotak pencarian untuk menemukan Aspose.PDF untuk .NET.

- Klik Pasang/Perbarui di sebelah versi terbaru dari Aspose.PDF untuk .NET.

![Installation_step2](../images/install_step2.png)

- Dan klik Terima di jendela pop up.

![Installation_step3](../images/install_step3.png)

![Installation](../images/install.gif)

### Bekerja dengan .NET Core DLL di Lingkungan Non-Windows

Karena Aspose.PDF untuk .NET menyediakan dukungan .NET Standard 2.0 (.NET Core 2.0), sehingga dapat digunakan dalam Aplikasi Core yang berjalan di sistem operasi seperti Linux.
Sebagai Aspose.PDF untuk .NET menyediakan dukungan .NET Standard 2.0 (.NET Core 2.0), maka dapat digunakan dalam Aplikasi Core yang berjalan di sistem operasi mirip Linux.

Silakan instal:

- paket libgdiplus
- paket dengan font yang kompatibel dengan Microsoft: **ttf-mscorefonts-installer**. (misalnya `sudo apt-get install ttf-mscorefonts-installer`)
Font-font ini harus ditempatkan di direktori "/usr/share/fonts/truetype/msttcorefonts" karena Aspose.PDF untuk .NET memindai folder ini di sistem operasi mirip Linux. Jika sistem operasi memiliki folder/direktori default lain untuk font, Anda harus menggunakan baris kode berikut sebelum melakukan operasi apa pun menggunakan Aspose.PDF.

```csharp
Aspose.Pdf.Text.FontRepository.Sources.Add(new FolderFontSource("<jalur pengguna ke font ms>"));
```
