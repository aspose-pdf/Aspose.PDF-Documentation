---
title: Lisensi dan batasan
linktitle: Lisensi dan batasan
type: docs
weight: 50
url: /androidjava/licensing/
description: Aspose.PDF untuk Android melalui Java mengundang pelanggannya untuk mendapatkan lisensi Klasik dan Lisensi Berbayar. Serta menggunakan lisensi terbatas untuk lebih mengeksplorasi produk.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Batasan versi evaluasi

Kami ingin pelanggan kami menguji komponen kami secara menyeluruh sebelum membeli sehingga versi evaluasi memungkinkan Anda menggunakannya seperti biasa.

- **PDF dibuat dengan watermark evaluasi.** Versi evaluasi Aspose.PDF untuk Android melalui Java menyediakan fungsionalitas produk penuh, tetapi semua halaman dalam dokumen PDF yang dihasilkan diberi watermark dengan "Hanya untuk Evaluasi. Dibuat dengan Aspose.PDF. Hak Cipta 2002-2020 Aspose Pty Ltd" di bagian atas.

- **Batasan jumlah item koleksi yang dapat diproses.**

Dalam versi evaluasi dari koleksi mana pun, Anda hanya dapat memproses empat elemen (misalnya, hanya 4 halaman, 4 bidang formulir, dll.).

Anda dapat mengunduh versi evaluasi Aspose.PDF untuk Android melalui Java dari [Aspose Repository](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-pdf). Versi evaluasi menyediakan kemampuan yang sama persis dengan versi berlisensi dari produk tersebut. Selain itu, versi evaluasi akan menjadi berlisensi ketika Anda membeli lisensi dan menambahkan beberapa baris kode untuk menerapkan lisensi tersebut.

Setelah Anda puas dengan evaluasi **Aspose.PDF**, Anda dapat [membeli lisensi](https://purchase.aspose.com/) di situs web Aspose. Kenali berbagai jenis langganan yang ditawarkan. Jika Anda memiliki pertanyaan, jangan ragu untuk menghubungi tim penjualan Aspose.

Setiap lisensi Aspose memiliki langganan satu tahun untuk pembaruan gratis ke versi baru atau perbaikan yang dirilis selama waktu ini. Dukungan teknis gratis dan tidak terbatas, dan disediakan baik untuk pengguna berlisensi maupun evaluasi.

>Jika Anda ingin menguji Aspose.PDF untuk Android melalui Java tanpa batasan versi evaluasi, Anda juga dapat meminta Lisensi Sementara 30 hari.
 Silakan merujuk ke [Cara mendapatkan Lisensi Sementara?](https://purchase.aspose.com/temporary-license)

## Lisensi klasik

Lisensi dapat dimuat dari file atau objek stream. Cara termudah untuk mengatur lisensi adalah dengan menempatkan file lisensi di folder yang sama dengan file Aspose.PDF.dll dan menentukan nama file tanpa jalur, seperti yang ditunjukkan dalam contoh di bawah ini.

Lisensi adalah file XML teks biasa yang berisi rincian seperti nama produk, jumlah pengembang yang dilisensikan, tanggal kedaluwarsa langganan, dan sebagainya. File ini ditandatangani secara digital, jadi jangan modifikasi file tersebut; bahkan penambahan tidak sengaja dari pemisah baris ekstra ke dalam file akan membatalkannya.

Anda perlu mengatur lisensi sebelum melakukan operasi apa pun dengan dokumen. Anda hanya perlu mengatur lisensi sekali per aplikasi atau proses.

Lisensi dapat dimuat dari stream atau file di lokasi berikut:

1. Jalur eksplisit.
1. Folder yang berisi aspose-pdf-xx.x.jar.

Gunakan metode License.setLicense untuk melisensikan komponen. Seringkali cara termudah untuk mengatur lisensi adalah dengan menempatkan file lisensi di folder yang sama dengan Aspose.PDF.jar dan menentukan hanya nama file tanpa path seperti yang ditunjukkan dalam contoh berikut:

{{% alert color="primary" %}}

Mulai dari Aspose.PDF untuk Java 4.2.0, Anda perlu memanggil baris kode berikut untuk menginisialisasi lisensi.

{{% /alert %}}

### Memuat lisensi dari file

Dalam contoh ini **Aspose.PDF** akan mencoba menemukan file lisensi di folder yang berisi JAR aplikasi Anda.

```java
// Inisialisasi Instance Lisensi
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Panggil metode setLicense untuk mengatur lisensi
license.setLicense("Aspose.Pdf.Java.lic");
```

### Memuat lisensi dari objek stream

Contoh berikut menunjukkan cara memuat lisensi dari stream.

```java
// Inisialisasi Instance Lisensi
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Setel lisensi dari Stream
license.setLicense(new java.io.FileInputStream("Aspose.Pdf.Java.lic"));
```

#### Mengatur Lisensi yang Dibeli Sebelum 2005/01/22
**Aspose.PDF** untuk Java tidak lagi mendukung lisensi lama jadi silakan hubungi [tim penjualan kami](https://company.aspose.com/contact) untuk mendapatkan file lisensi baru.

### Validasi Lisensi

Dimungkinkan untuk memvalidasi apakah lisensi telah diatur dengan benar atau tidak. Kelas Document memiliki metode isLicensed yang akan mengembalikan true jika lisensi telah diatur dengan benar.

```java
License license = new License();
license.setLicense("Aspose.Pdf.Java.lic");
// Periksa apakah lisensi telah divalidasi
if (com.aspose.pdf.Document.isLicensed()) {
    System.out.println("Lisensi Telah Diatur!");
}
```
## Lisensi Metered

Aspose.PDF memungkinkan pengembang untuk menerapkan kunci metered. Ini adalah mekanisme lisensi baru. Mekanisme lisensi baru akan digunakan bersamaan dengan metode lisensi yang ada. Pelanggan yang ingin ditagih berdasarkan penggunaan fitur API dapat menggunakan lisensi metered. Untuk informasi lebih lanjut, silakan merujuk ke bagian [Metered Licensing FAQ](https://purchase.aspose.com/faqs/licensing/metered).

```java
String publicKey = "";
String privateKey = "";

Metered m = new Metered();
m.setMeteredKey(publicKey, privateKey);

// Opsional, dua baris berikut mengembalikan true jika lisensi valid telah diterapkan;
// false jika komponen berjalan dalam mode evaluasi.
License lic = new License();
System.out.println("Lisensi telah diatur = " + lic.isLicensed());
```

## Menggunakan Beberapa Produk dari Aspose

Jika Anda menggunakan beberapa produk Aspose dalam aplikasi Anda, misalnya Aspose.PDF dan Aspose.Words, berikut adalah beberapa tips berguna.

- **Setel Lisensi untuk setiap Produk Aspose Secara Terpisah.** Meskipun Anda memiliki satu file lisensi untuk semua komponen, misalnya 'Aspose.Total.lic', Anda tetap perlu memanggil **License.SetLicense** secara terpisah untuk setiap produk Aspose yang Anda gunakan dalam aplikasi Anda.
- **Gunakan Nama Kelas Lisensi yang Sepenuhnya Berkualifikasi.** Setiap produk Aspose memiliki kelas **License** dalam namespace-nya. Misalnya, Aspose.PDF memiliki kelas **com.aspose.pdf.License** dan Aspose.Words memiliki kelas **com.aspose.words.License**. Menggunakan nama kelas yang sepenuhnya berkualifikasi memungkinkan Anda menghindari kebingungan tentang lisensi mana yang diterapkan pada produk mana.

```java
// Membuat instans dari kelas License dari Aspose.Pdf
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Setel lisensi
license.setLicense("Aspose.Total.Java.lic");

// Menyetel lisensi untuk Aspose.Words untuk Java

// Membuat instans dari kelas License dari Aspose.Words
com.aspose.words.License licenseaw = new com.aspose.words.License();
// Setel lisensi
licenseaw.setLicense("Aspose.Total.Java.lic");
```