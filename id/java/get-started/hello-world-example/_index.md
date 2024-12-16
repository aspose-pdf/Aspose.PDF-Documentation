---
title: Hello World Contoh Java
linktitle: Hello World Contoh
type: docs
weight: 40
url: /id/java/hello-world-example/
description: Halaman ini menunjukkan cara menggunakan pemrograman sederhana untuk membuat dokumen PDF yang berisi teks - Hello World menggunakan Aspose.PDF untuk Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Contoh Hello World

Contoh “Hello World” secara tradisional digunakan untuk memperkenalkan fitur dari bahasa pemrograman atau perangkat lunak dengan kasus penggunaan sederhana.

Aspose.PDF untuk Java API memberdayakan pengembang aplikasi Java untuk membuat, membaca, mengedit, dan memanipulasi file PDF dalam aplikasi mereka. Ini memungkinkan Anda membaca dan mengonversi beberapa jenis file berbeda ke dan dari format file PDF. Artikel Hello World ini menunjukkan cara membuat file PDF di Java menggunakan Aspose.PDF untuk Java API. Setelah [menginstal Aspose.PDF untuk Java](/pdf/id/java/installation/) di lingkungan Anda, Anda dapat menjalankan contoh kode di bawah ini untuk melihat bagaimana API Aspose.PDF bekerja.

Cuplikan kode di bawah ini mengikuti langkah-langkah ini:

1. Instansiasi objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document)
1. Tambahkan [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/page) ke objek dokumen
1. Buat objek [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/TextFragment)
1. Tambahkan TextFragment ke koleksi [Paragraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/Paragraphs) dari halaman
1. Simpan dokumen PDF yang dihasilkan

Cuplikan kode berikut adalah program Hello World untuk menunjukkan cara kerja Aspose.PDF untuk Java API.

```java
// Inisialisasi objek dokumen
Document document = new Document();
 
// Tambah halaman
Page page = document.getPages().add();
 
// Tambah teks ke halaman baru
page.getParagraphs().add(new TextFragment("Hello World!"));
 
// Simpan PDF yang diperbarui
document.save("HelloWorld_out.pdf");
```