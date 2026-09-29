---
title: Lisensi Aspose PDF
linktitle: Lisensi dan batasan
type: docs
weight: 50
url: /id/java/licensing/
description: Aspose.PDF for Python mengundang pelanggannya untuk mendapatkan lisensi Classic. Juga dapat menggunakan lisensi terbatas untuk menjelajahi produk dengan lebih baik.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Lisensi Aspose.PDF for Java
Abstract: Artikel ini membahas keterbatasan dan opsi lisensi untuk Aspose.PDF for Python. Artikel menyoroti bahwa versi evaluasi memungkinkan pengujian fungsi penuh tetapi menambahkan watermark pada PDF yang dihasilkan, menampilkan “Evaluation Only” bersama informasi hak cipta. Untuk pengguna yang ingin menguji tanpa keterbatasan ini, tersedia Lisensi Sementara selama 30 hari. Artikel selanjutnya menjelaskan cara menerapkan lisensi klasik dengan memuatnya dari file atau aliran, menyarankan menempatkan file lisensi di direktori yang sama dengan file Aspose.PDF.dll dan mengatur lisensi menggunakan kelas `Aspose.Pdf.License`. Potongan kode disediakan untuk mengilustrasikan proses lisensi.
---
## Keterbatasan versi evaluasi

Kami ingin pelanggan kami menguji komponen kami secara menyeluruh sebelum membeli, sehingga versi evaluasi memungkinkan Anda menggunakannya seperti biasa.

- **PDF dibuat dengan watermark evaluasi.** Versi evaluasi Aspose.PDF for Java menyediakan fungsionalitas produk lengkap, tetapi semua halaman dalam dokumen PDF yang dihasilkan ditandai dengan watermark "Evaluation Only. Created with Aspose.PDF. Copyright 2002-2020 Aspose Pty Ltd" di bagian atas.

- **Batas jumlah item koleksi yang dapat diproses.**
Dalam versi evaluasi dari setiap koleksi, Anda hanya dapat memproses empat elemen (misalnya, hanya 4 halaman, 4 bidang formulir, dll.).

Anda dapat mengunduh versi evaluasi **Aspose.PDF** untuk Java dari [Aspose Repository](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-pdf). Versi evaluasi menyediakan kemampuan yang sama persis dengan versi berlisensi produk. Selanjutnya, versi evaluasi secara sederhana menjadi berlisensi ketika Anda membeli lisensi dan menambahkan beberapa baris kode untuk menerapkan lisensi.

Setelah Anda puas dengan evaluasi **Aspose.PDF**, Anda dapat [beli lisensi](https://purchase.aspose.com/) di situs web Aspose. Kenali berbagai jenis langganan yang ditawarkan. Jika Anda memiliki pertanyaan, jangan ragu untuk menghubungi tim penjualan Aspose.

Setiap lisensi Aspose mencakup langganan satu tahun untuk pembaruan gratis ke versi baru atau perbaikan yang dirilis selama periode tersebut. Dukungan teknis gratis dan tidak terbatas serta disediakan baik untuk pengguna berlisensi maupun pengguna evaluasi.

>Jika Anda ingin menguji Aspose.PDF for Java tanpa batasan versi evaluasi, Anda juga dapat meminta Lisensi Sementara selama 30 hari. Silakan merujuk ke [Bagaimana cara mendapatkan Lisensi Sementara?](https://purchase.aspose.com/temporary-license)

## Lisensi klasik

Lisensi dapat dimuat dari file atau objek aliran. Cara termudah untuk mengatur lisensi adalah dengan menempatkan file lisensi di folder yang sama dengan file Aspose.PDF.dll dan menentukan nama file tanpa jalur, seperti yang ditunjukkan dalam contoh di bawah.

Lisensi adalah file XML teks biasa yang berisi detail seperti nama produk, jumlah pengembang yang diberi lisensi, tanggal kedaluwarsa langganan, dan sebagainya. File tersebut ditandatangani secara digital, jadi jangan memodifikasi file; bahkan penambahan baris baru secara tidak sengaja ke dalam file akan membuatnya tidak valid.

Anda harus menetapkan lisensi sebelum melakukan operasi apa pun dengan dokumen. Anda hanya perlu menetapkan lisensi satu kali per aplikasi atau proses.

Lisensi dapat dimuat dari stream atau file di lokasi berikut:

1. Jalur eksplisit.
1. Folder yang berisi aspose-pdf-xx.x.jar.

Gunakan metode License.setLicense untuk memberi lisensi pada komponen. Seringkali cara termudah untuk mengatur lisensi adalah dengan menempatkan file lisensi di folder yang sama dengan Aspose.PDF.jar dan menentukan hanya nama file tanpa jalur seperti yang ditunjukkan pada contoh berikut:

{{% alert color="primary" %}}

Mulai dari Aspose.PDF for Java 4.2.0, Anda perlu memanggil baris kode berikut untuk menginisialisasi lisensi.

{{% /alert %}}

### Memuat lisensi dari file

Dalam contoh ini **Aspose.PDF** akan mencoba menemukan file lisensi di folder yang berisi JAR aplikasi Anda.

```java
// Initialize License Instance
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Call setLicense method to set license
license.setLicense("Aspose.Pdf.Java.lic");
```

### Memuat lisensi dari objek aliran

Contoh berikut menunjukkan cara memuat lisensi dari aliran.

```java
// Initialize License Instance
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Set license from Stream
license.setLicense(new java.io.FileInputStream("Aspose.Pdf.Java.lic"));
```

### Validasi Lisensi

Dimungkinkan untuk memvalidasi apakah lisensi telah diatur dengan benar atau tidak. Kelas Document memiliki metode isLicensed yang akan mengembalikan true jika lisensi telah diatur dengan benar.

```java
License license = new License();
license.setLicense("Aspose.Pdf.Java.lic");
// Check if license has been validated
if (com.aspose.pdf.Document.isLicensed()) {
    System.out.println("License is Set!");
}
```

## Lisensi Metered

Aspose.PDF memungkinkan pengembang menerapkan kunci meter. Ini merupakan mekanisme lisensi baru. Mekanisme lisensi baru akan digunakan bersama dengan metode lisensi yang ada. Pelanggan yang ingin ditagih berdasarkan penggunaan fitur API dapat menggunakan lisensi meter.В Untuk detail lebih lanjut, silakan merujuk keВ [FAQ Lisensi Metered](https://purchase.aspose.com/faqs/licensing/metered)В bagian.

Sebuah kelas baruВ [Metered](https://reference.aspose.com/pdf/java/com.aspose.pdf/Metered)В telah diperkenalkan untuk menerapkan kunci bermeter. Berikut adalah contoh kode yang menunjukkan cara mengatur kunci publik dan privat bermeter.

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

- **Gunakan Lisensi untuk Setiap Produk Aspose Secara Terpisah.** Bahkan jika Anda memiliki satu file lisensi untuk semua komponen, misalnya 'Aspose.Total.lic', Anda tetap harus memanggil **License.SetLicense** secara terpisah untuk setiap produk Aspose yang Anda gunakan dalam aplikasi Anda.
- **Gunakan Nama Kelas Lisensi yang Fully Qualified.** Setiap produk Aspose memiliki kelas **License** di dalam namespace-nya. Sebagai contoh, Aspose.PDF memiliki kelas **com.aspose.pdf.License** dan Aspose.Words memiliki kelas **com.aspose.words.License**. Menggunakan nama kelas yang fully qualified memungkinkan Anda menghindari kebingungan tentang lisensi mana yang diterapkan pada produk mana.

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
