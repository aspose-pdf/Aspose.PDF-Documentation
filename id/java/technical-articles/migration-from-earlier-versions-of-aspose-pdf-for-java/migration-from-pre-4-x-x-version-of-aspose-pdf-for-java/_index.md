---
title: Migrasi dari Versi Aspose.PDF untuk Java Sebelum 4.x.x
type: docs
weight: 20
url: id/java/migrasi-dari-versi-aspose-pdf-untuk-java-sebelum-4-x-x/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Versi auto-port baru dari Aspose.PDF untuk Java telah dirilis dan sekarang produk tunggal ini mendukung kemampuan untuk menghasilkan dokumen PDF dari awal serta menyediakan kemampuan untuk memanipulasi dokumen PDF yang sudah ada.

{{% /alert %}}

## Biner Produk

{{% alert color="primary" %}}

Dalam versi rilis pertama (v4.0.0), kami mengirimkan dua file jar yaitu **aspose.pdf-3.3.0.jdk15.jar** dan **aspose.pdf-new-4.0.0.jar**.

- **aspose.pdf-3.3.0.jdk14.jar**

File jar ini adalah versi produk yang sama seperti yang saat ini tersedia di modul unduhan dengan judul [Aspose.PDF untuk java 3.3.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry417659.aspx). Selanjutnya, kami akan menyebut versi rilis ini sebagai legacy Aspose.PDF untuk Java. Pada rilis pertama ini, pengguna yang sudah ada dari Aspose.PDF untuk Java mungkin tidak terpengaruh karena mereka mendapatkan versi rilis yang sama. Namun, dalam waktu dekat, kami akan menghapus file jar terpisah ini dan semua kelas serta enumerasi dari legacy Aspose.PDF untuk Java (sebelum 4.x.x) akan tersedia di bawah paket com.aspose.pdf.generator dari file aspose.pdf-new-4.x.x.jar tunggal.

- **aspose.pdf-new-4.0.0.jar**  
  File jar ini adalah versi baru yang sebenarnya yang di-porting otomatis dari Aspose.PDF untuk .NET ke platform Java.
 This jar file contains the new Document Object Model (DOM) untuk membuat serta memanipulasi file PDF yang ada dan juga Aspose.PDF.Kit saat ini untuk Java. Semua kelas dan enumerasi dari Aspose.PDF.Kit untuk Java dibundel di bawah paket com.aspose.pdf.facades dan pada Q3 tahun 2013, Aspose.PDF.Kit untuk Java akan dihentikan. Oleh karena itu, kami mendorong pelanggan Aspose.PDF.Kit untuk Java kami saat ini untuk mencoba memigrasikan kode mereka ke rilis auto-ported yang baru.

Silakan periksa posting blog berikut untuk mendapatkan wawasan lebih lanjut tentang Struktur dari autoported Aspose.PDF untuk Java.
{{% /alert %}}