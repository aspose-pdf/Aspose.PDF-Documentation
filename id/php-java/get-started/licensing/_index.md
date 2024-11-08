---
title: Lisensi dan batasan
linktitle: Lisensi dan batasan
type: docs
weight: 90
url: /id/php-java/licensing/
description: Aspose.PDF untuk PHP melalui Java mengundang pelanggannya untuk mendapatkan lisensi Klasik dan Lisensi Meteran. Serta menggunakan lisensi terbatas untuk lebih mengeksplorasi produk.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Batasan versi evaluasi

Kami ingin pelanggan kami menguji komponen kami secara menyeluruh sebelum membeli sehingga versi evaluasi memungkinkan Anda untuk menggunakannya seperti biasanya.

- **PDF dibuat dengan watermark evaluasi.** Versi evaluasi Aspose.PDF untuk PHP melalui Java menyediakan fungsionalitas produk penuh, tetapi semua halaman dalam dokumen PDF yang dihasilkan diberi watermark dengan "Hanya Evaluasi. Dibuat dengan Aspose.PDF. Hak Cipta 2002-2020 Aspose Pty Ltd" di bagian atas.

- **Batas jumlah item koleksi yang dapat diproses.**

Dalam versi evaluasi dari koleksi mana pun, Anda hanya dapat memproses empat elemen (misalnya, hanya 4 halaman, 4 bidang formulir, dll.).

Anda dapat mengunduh versi evaluasi **Aspose.PDF** untuk Java dari [Aspose Repository](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-pdf). Versi evaluasi menyediakan kemampuan yang sama persis seperti versi berlisensi dari produk tersebut. Selain itu, versi evaluasi akan menjadi berlisensi ketika Anda membeli lisensi dan menambahkan beberapa baris kode untuk menerapkan lisensi tersebut.

Setelah Anda puas dengan evaluasi **Aspose.PDF**, Anda dapat [membeli lisensi](https://purchase.aspose.com/) di situs web Aspose. Kenali berbagai jenis langganan yang ditawarkan. Jika Anda memiliki pertanyaan, jangan ragu untuk menghubungi tim penjualan Aspose.

Setiap lisensi Aspose menyertakan langganan satu tahun untuk pembaruan gratis ke versi baru atau perbaikan yang keluar selama waktu ini. Dukungan teknis gratis dan tidak terbatas dan disediakan baik untuk pengguna berlisensi maupun evaluasi.

>Jika Anda ingin menguji Aspose.PDF untuk PHP melalui Java tanpa batasan versi evaluasi, Anda juga dapat meminta Lisensi Sementara 30 hari.
 Silakan merujuk ke [Cara mendapatkan Lisensi Sementara?](https://purchase.aspose.com/temporary-license)

## Lisensi klasik

Lisensi dapat dimuat dari file atau objek stream. Cara termudah untuk mengatur lisensi adalah dengan meletakkan file lisensi di folder yang sama dengan file Aspose.PDF.dll dan menentukan nama file tanpa jalur, seperti yang ditunjukkan dalam contoh di bawah.

Lisensi adalah file XML teks biasa yang berisi detail seperti nama produk, jumlah pengembang yang dilisensikan, tanggal kadaluwarsa langganan, dan sebagainya. File ini ditandatangani secara digital, jadi jangan modifikasi file tersebut; bahkan penambahan tidak sengaja dari jeda baris ekstra dalam file akan membatalkannya.

Anda perlu mengatur lisensi sebelum melakukan operasi apa pun dengan dokumen. Anda hanya perlu mengatur lisensi sekali per aplikasi atau proses.

Lisensi dapat dimuat dari stream atau file di lokasi berikut:

1. Jalur eksplisit.
1. Folder yang berisi aspose-pdf-xx.x.jar.

Gunakan metode License.setLicense untuk melisensikan komponen. Seringkali cara termudah untuk menetapkan lisensi adalah dengan menempatkan file lisensi di folder yang sama dengan Aspose.PDF.jar dan hanya menyebutkan nama file tanpa path seperti yang ditunjukkan dalam contoh berikut:

{{% alert color="primary" %}}

Mulai dari Aspose.PDF untuk PHP melalui Java 4.2.0, Anda perlu memanggil baris kode berikut untuk menginisialisasi lisensi.

{{% /alert %}}

### Memuat lisensi dari file

Dalam contoh ini **Aspose.PDF** akan mencoba menemukan file lisensi di folder yang berisi JAR dari aplikasi Anda.

```java
// Inisialisasi Instance Lisensi
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Panggil metode setLicense untuk menetapkan lisensi
license.setLicense("Aspose.Pdf.Java.lic");
```
### Memuat lisensi dari objek stream

Contoh berikut menunjukkan cara memuat lisensi dari stream.

```java
// Inisialisasi Instance Lisensi
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Tetapkan lisensi dari Stream
license.setLicense(new java.io.FileInputStream("Aspose.Pdf.Java.lic"));
```

#### Menetapkan Lisensi yang Dibeli Sebelum 2005/01/22**Aspose.PDF** untuk Java tidak lagi mendukung lisensi lama jadi silakan hubungi [tim penjualan](https://company.aspose.com/contact) kami untuk mendapatkan file lisensi baru.

### Validasi Lisensi

Dimungkinkan untuk memvalidasi apakah lisensi telah diatur dengan benar atau tidak. Kelas Document memiliki metode isLicensed yang akan mengembalikan nilai true jika lisensi telah diatur dengan benar.

```java
License license = new License();
license.setLicense("Aspose.Pdf.Java.lic");
// Periksa apakah lisensi telah divalidasi
if (com.aspose.pdf.Document.isLicensed()) {
    System.out.println("Lisensi telah Diatur!");
}
```
## Lisensi Berbasis Penggunaan

Aspose.PDF memungkinkan pengembang untuk menerapkan kunci berbasis penggunaan. Ini adalah mekanisme lisensi baru. Mekanisme lisensi baru akan digunakan bersama dengan metode lisensi yang ada. Pelanggan yang ingin ditagih berdasarkan penggunaan fitur API dapat menggunakan lisensi berbasis penggunaan. Untuk lebih jelasnya, silakan merujuk ke bagian [FAQ Lisensi Berbasis Penggunaan](https://purchase.aspose.com/faqs/licensing/metered).

Kelas baru [Metered](https://reference.aspose.com/pdf/java/com.aspose.pdf/Metered) telah diperkenalkan untuk menerapkan kunci berbasis penggunaan.
 Berikut adalah contoh kode yang menunjukkan cara mengatur kunci publik dan privat yang diukur.

```java
String publicKey = "";
String privateKey = "";

Metered m = new Metered();
m.setMeteredKey(publicKey, privateKey);

// Secara opsional, dua baris berikut mengembalikan true jika lisensi yang valid telah diterapkan;
// false jika komponen berjalan dalam mode evaluasi.
License lic = new License();
System.out.println("Lisensi diatur = " + lic.isLicensed());
```
## Menggunakan Beberapa Produk dari Aspose

Jika Anda menggunakan beberapa produk Aspose dalam aplikasi Anda, misalnya Aspose.PDF dan Aspose.Words, berikut adalah beberapa tips berguna.

- **Atur Lisensi untuk setiap Produk Aspose Secara Terpisah.** Meskipun Anda memiliki satu file lisensi untuk semua komponen, misalnya 'Aspose.Total.lic', Anda masih perlu memanggil **License.SetLicense** secara terpisah untuk setiap produk Aspose yang Anda gunakan dalam aplikasi Anda.
- **Gunakan Nama Kelas Lisensi yang Sepenuhnya Berkualifikasi.** Setiap produk Aspose memiliki kelas **License** dalam ruang namanya. Misalnya, Aspose.PDF memiliki **com.aspose.pdf.License** dan Aspose.Words memiliki **com.aspose.words.License** class. Menggunakan nama kelas yang sepenuhnya memenuhi syarat memungkinkan Anda menghindari kebingungan tentang lisensi mana yang diterapkan pada produk mana.

```java
// Memperkenalkan kelas License dari Aspose.Pdf
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Mengatur lisensi
license.setLicense("Aspose.Total.Java.lic");

// Mengatur lisensi untuk Aspose.Words untuk Java

// Memperkenalkan kelas License dari Aspose.Words
com.aspose.words.License licenseaw = new com.aspose.words.License();
// Mengatur lisensi
licenseaw.setLicense("Aspose.Total.Java.lic");
```