---
title: Lisensi dan keterbatasan
linktitle: Lisensi dan keterbatasan
type: docs
weight: 50
url: /id/androidjava/licensing/
description: Aspose.PDF for Android via Java mengundang pelanggannya untuk mendapatkan lisensi Classic dan lisensi Metered. Selain itu dapat menggunakan lisensi terbatas untuk menjelajahi produk dengan lebih baik.
lastmod: "2026-07-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Keterbatasan versi evaluasi

Kami ingin pelanggan kami menguji komponen kami secara menyeluruh sebelum membeli, sehingga versi evaluasi memungkinkan Anda menggunakannya seperti biasanya.

- **PDF dibuat dengan watermark evaluasi.** Versi evaluasi Aspose.PDF untuk Android via Java menyediakan fungsionalitas produk penuh, tetapi semua halaman dalam dokumen PDF yang dihasilkan memiliki watermark "Evaluation Only. Created with Aspose.PDF. Copyright 2002-2020 Aspose Pty Ltd" di bagian atas.

- **Batas jumlah item koleksi yang dapat diproses.**
Dalam versi evaluasi dari setiap koleksi, Anda hanya dapat memproses empat elemen (misalnya, hanya 4 halaman, 4 field formulir, dll).

Anda dapat mengunduh versi evaluasi Aspose.PDF untuk Android via Java dari [Aspose Repository](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-pdf). Versi evaluasi menyediakan kemampuan yang persis sama dengan versi berlisensi dari produk. Lebih lanjut, versi evaluasi secara sederhana menjadi berlisensi ketika Anda membeli lisensi dan menambahkan beberapa baris kode untuk menerapkan lisensi.

Setelah Anda puas dengan evaluasi **Aspose.PDF** Anda, Anda dapat [membeli lisensi](https://purchase.aspose.com/) di situs web Aspose. Kenali berbagai jenis langganan yang ditawarkan. Jika Anda memiliki pertanyaan, jangan ragu untuk menghubungi tim penjualan Aspose.

Setiap lisensi Aspose mencakup langganan satu tahun untuk peningkatan gratis ke versi baru atau perbaikan yang dirilis selama periode ini. Dukungan teknis gratis dan tidak terbatas serta disediakan baik untuk pengguna berlisensi maupun pengguna evaluasi.

>Jika Anda ingin menguji Aspose.PDF untuk Android via Java tanpa batasan versi evaluasi, Anda juga dapat meminta Lisensi Sementara selama 30 hari. Silakan merujuk ke [Bagaimana cara mendapatkan Lisensi Sementara?](https://purchase.aspose.com/temporary-license)

## Lisensi klasik

Lisensi dapat dimuat dari file atau objek stream. Cara termudah untuk mengatur lisensi adalah dengan menempatkan file lisensi di folder yang sama dengan file Aspose.PDF.dll dan menentukan nama file tanpa jalur, seperti yang ditunjukkan dalam contoh di bawah.

Lisensi adalah file XML teks biasa yang berisi detail seperti nama produk, jumlah pengembang yang memiliki lisensi, tanggal kedaluwarsa langganan, dan sebagainya. File ini ditandatangani secara digital, jadi jangan memodifikasi file; bahkan penambahan baris kosong ekstra secara tidak sengaja ke dalam file akan membuatnya tidak valid.

Anda harus mengatur lisensi sebelum melakukan operasi apa pun dengan dokumen. Anda hanya perlu mengatur lisensi satu kali per aplikasi atau proses.

Lisensi dapat dimuat dari aliran atau file di lokasi berikut:

1. Jalur eksplisit.
1. Folder yang berisi aspose-pdf-xx.x.jar.

Gunakan metode License.setLicense untuk melisensikan komponen. Seringkali cara termudah untuk menetapkan lisensi adalah dengan menempatkan file lisensi di folder yang sama dengan Aspose.PDF.jar dan hanya menentukan nama file tanpa jalur seperti yang ditunjukkan dalam contoh berikut:

{{% alert color="primary" %}}

Mulai dari Aspose.PDF for Java 4.2.0, Anda perlu memanggil baris kode berikut untuk menginisialisasi lisensi.

{{% /alert %}}

### Memuat lisensi dari file

Dalam contoh ini **Aspose.PDF** akan berusaha menemukan file lisensi di folder yang berisi JAR aplikasi Anda.

```java
// Initialize License Instance
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Call setLicense method to set license
license.setLicense("Aspose.Pdf.Java.lic");
```

### Memuat lisensi dari objek stream

Contoh berikut menunjukkan cara memuat lisensi dari stream.

```java
// Initialize License Instance
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Set license from Stream
license.setLicense(new java.io.FileInputStream("Aspose.Pdf.Java.lic"));
```

#### Mengatur Lisensi yang Dibeli Sebelum 2005/01/22

**Aspose.PDF** untuk Java tidak lagi mendukung lisensi lama jadi silakan hubungi tim [tim penjualan](https://company.aspose.com/contact) untuk mendapatkan file lisensi baru.

### Validasi Lisensi

Anda dapat memvalidasi apakah lisensi telah diatur dengan benar atau tidak. Kelas Document memiliki metode isLicensed yang akan mengembalikan true jika lisensi telah diatur dengan benar.

```java
License license = new License();
license.setLicense("Aspose.Pdf.Java.lic");
// Check if license has been validated
if (com.aspose.pdf.Document.isLicensed()) {
    System.out.println("License is Set!");
}
```
## Lisensi Metered

Aspose.PDF memungkinkan pengembang untuk menerapkan kunci metered. Ini adalah mekanisme lisensi baru. Mekanisme lisensi baru akan digunakan bersama dengan metode lisensi yang ada. Pelanggan yang ingin ditagih berdasarkan penggunaan fitur API dapat menggunakan lisensi metered. Untuk detail lebih lanjut, silakan merujuk ke [FAQ Lisensi Metered](https://purchase.aspose.com/faqs/licensing/metered) bagian.

```java
String publicKey = "";
String privateKey = "";

Metered m = new Metered();
m.setMeteredKey(publicKey, privateKey);

// Optionally, the following two lines returns true if a valid license has been applied;
// false if the component is running in evaluation mode.
License lic = new License();
System.out.println("License is set = " + lic.isLicensed());
```
## Menggunakan Beberapa Produk dari Aspose

Jika Anda menggunakan beberapa produk Aspose dalam aplikasi Anda, misalnya Aspose.PDF dan Aspose.Words, berikut beberapa tips berguna.

- **Setel Lisensi untuk setiap Produk Aspose secara Terpisah.** Bahkan jika Anda memiliki satu file lisensi untuk semua komponen, misalnya 'Aspose.Total.lic', Anda tetap harus memanggil **License.SetLicense** secara terpisah untuk setiap produk Aspose yang Anda gunakan dalam aplikasi Anda.
- **Gunakan Nama Kelas Lisensi yang Sepenuhnya Terkualifikasi.** Setiap produk Aspose memiliki kelas **License** di dalam namespace‑nya. Misalnya, Aspose.PDF memiliki kelas **com.aspose.pdf.License** dan Aspose.Words memiliki kelas **com.aspose.words.License**. Menggunakan nama kelas yang sepenuhnya terkualifikasi memungkinkan Anda menghindari kebingungan tentang lisensi mana yang diterapkan pada produk mana.

```java
// Instantiate the License class of Aspose.Pdf
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Set the license
license.setLicense("Aspose.Total.Java.lic");

// Setting license for Aspose.Words for Java

// Instantiate the License class of Aspose.Words
com.aspose.words.License licenseaw = new com.aspose.words.License();
// Set the license
licenseaw.setLicense("Aspose.Total.Java.lic");
```
