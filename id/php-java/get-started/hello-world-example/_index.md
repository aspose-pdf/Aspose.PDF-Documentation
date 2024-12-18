---
title: Hello World PHP via Java Contoh
linktitle: Hello World Contoh
type: docs
weight: 40
url: /id/php-java/hello-world-example/
description: Halaman ini menunjukkan bagaimana menggunakan pemrograman sederhana untuk membuat dokumen PDF berisi teks - Hello World menggunakan Aspose.PDF untuk PHP via Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Hello World Contoh

Contoh "Hello World" biasanya digunakan untuk mendemonstrasikan fitur dasar dari bahasa pemrograman atau perangkat lunak dengan kasus penggunaan langsung.

Aspose.PDF untuk PHP via Java API memungkinkan pengembang untuk membuat, membaca, mengedit, dan memanipulasi file PDF dalam aplikasi Java mereka. Ini mendukung membaca dan mengonversi berbagai jenis file ke dan dari format PDF. Artikel Hello World ini menunjukkan cara membuat file PDF menggunakan Aspose.PDF untuk PHP via Java API. Setelah [menginstal Aspose.PDF untuk PHP via Java](/pdf/id/php-java/installation/) di lingkungan Anda, Anda dapat menjalankan contoh kode di bawah ini untuk melihat bagaimana Aspose.PDF API bekerja.

Cuplikan kode di bawah ini mengikuti langkah-langkah ini:


1. Membuat objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document)
1. Tambahkan [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/page) ke objek dokumen
1. Buat objek [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/TextFragment)
1. Tambahkan TextFragment ke koleksi [Paragraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/Paragraphs) dari halaman
1. Simpan dokumen PDF hasil

Cuplikan kode berikut adalah program Hello World untuk menunjukkan cara kerja Aspose.PDF untuk PHP melalui Java API.

```php
    $document = new Document();    
    $page = $document->getPages()->add();
    $textFragment = new TextFragment("Hello World!");    
    $page->getParagraphs()->add($textFragment);
    $document->save($outputFile);
```