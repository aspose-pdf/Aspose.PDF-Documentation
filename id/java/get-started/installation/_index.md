---
title: Install Aspose.PDF untuk Java
linktitle: Instalasi
type: docs
weight: 20
url: /id/java/installation/
description: Bagian ini menunjukkan deskripsi produk dan instruksi untuk menginstal Aspose.PDF untuk Java sendiri, serta menggunakan NuGet.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Komponen Aspose.PDF untuk Java

{{% alert color="primary" %}}

**Aspose.PDF adalah komponen Java** yang dibangun untuk memungkinkan pengembang membuat dokumen PDF, baik yang sederhana maupun yang kompleks, secara langsung melalui pemrograman. Aspose.PDF untuk Java memungkinkan pengembang untuk menyisipkan tabel, grafik, gambar, hyperlink, font kustom - dan lebih banyak lagi - ke dalam dokumen PDF. Selain itu, juga dimungkinkan untuk mengompresi dokumen PDF. Aspose.PDF untuk Java menyediakan fitur keamanan yang sangat baik untuk mengembangkan dokumen PDF yang aman. Dan fitur paling khas dari Aspose.PDF untuk Java adalah mendukung pembuatan dokumen PDF melalui API dan dari template XML.

{{% /alert %}}

## Deskripsi Produk

**Aspose.PDF untuk Java** diimplementasikan menggunakan Java dan bekerja dengan JDK 1.8 dan di atasnya. Aspose.PDF untuk Java dapat diintegrasikan dengan aplikasi apa pun, misalnya aplikasi web JSP/JSF atau aplikasi Windows.

**Aspose.PDF untuk Java** cepat dan ringan. Ini membuat dokumen PDF dengan efisien dan membantu aplikasi Anda berfungsi lebih baik. Aspose.PDF untuk Java adalah pilihan pertama pelanggan kami saat membuat dokumen PDF karena harganya, kinerja yang luar biasa, dan dukungan yang hebat. Dengan menggunakan pustaka ini, Anda dapat mengimplementasikan kemampuan yang kaya untuk membuat file PDF dari awal, atau memproses sepenuhnya dokumen PDF yang ada tanpa menginstal Adobe Acrobat.

# Instalasi

## Evaluasi Aspose.PDF untuk Java

{{% alert color="primary" %}}

Anda dapat mengunduh [Aspose.PDF untuk Java](https://releases.aspose.com/java/repo/com/aspose/aspose-pdf/) untuk evaluasi.
 Unduhan evaluasi sama dengan unduhan yang dibeli. Versi evaluasi akan menjadi berlisensi ketika Anda menambahkan beberapa baris kode untuk [menerapkan lisensi](/pdf/id/java/licensing/).

{{% /alert %}}

Versi evaluasi Aspose.PDF menyediakan fungsionalitas produk penuh, tetapi memiliki dua keterbatasan:

- Ini menyisipkan tanda air evaluasi.
- Tidak lebih dari empat elemen dari koleksi mana pun dapat dilihat/diedit.
- **Sebuah dokumen yang menunjukkan tanda air evaluasi**

![Evaluasi Aspose.PDF](evaluate-aspose-pdf_1.png)

{{% alert color="primary" %}}

Jika Anda ingin menguji Aspose.PDF untuk Java tanpa batasan versi evaluasi, Anda juga dapat meminta Lisensi Sementara 30 hari. Silakan merujuk ke [Bagaimana cara mendapatkan Lisensi Sementara?](https://purchase.aspose.com/temporary-license)

{{% /alert %}}

## Menginstal Aspose.PDF untuk Java dari Repository Aspose

Aspose menyimpan semua API Java di [Repository Aspose](https://releases.aspose.com/java/repo/com/aspose/aspose-pdf/). Anda dapat dengan mudah menggunakan Aspose.PDF untuk API Java langsung dalam Proyek Maven Anda dengan konfigurasi yang sederhana.

### Tentukan Konfigurasi Repository Aspose

Pertama, Anda perlu menentukan konfigurasi / lokasi Repository Aspose di Maven pom.xml Anda sebagai berikut:

```xml
 <repositories>
    <repository>
        <id>AsposeJavaAPI</id>
        <name>Aspose Java API</name>
        <url>https://releases.aspose.com/java/repo/</url>
    </repository>
</repositories>
```

### Definisikan Ketergantungan Aspose.PDF untuk API Java

Kemudian definisikan ketergantungan Aspose.PDF untuk API Java di pom.xml Anda sebagai berikut:

```xml
 <dependencies>
    <dependency>
        <groupId>com.aspose</groupId>
        <artifactId>aspose-pdf</artifactId>
        <version>21.7</version>
    </dependency>
</dependencies>
```

Setelah melakukan langkah-langkah di atas, ketergantungan Aspose.PDF untuk Java akhirnya akan didefinisikan dalam Proyek Maven Anda.

### Kompatibilitas dan Pedoman Penggunaan JDK 11

API ini dioptimalkan untuk lingkungan Java 11 dan semua tes serta fungsionalitas bekerja dengan baik. Namun, untuk beberapa kelas Anda harus menambahkan dependensi eksternal untuk menambahkan classpath dari kelas: javax.xml.bind.annotation.adapters.HexBinaryAdapter, yang telah dihapus dari JRE.

Sebagai contoh:

```xml
<dependency>
    <groupId>javax.xml.bind</groupId>
    <artifactId>jaxb-api</artifactId>
    <version>2.3.0</version>
</dependency>
```