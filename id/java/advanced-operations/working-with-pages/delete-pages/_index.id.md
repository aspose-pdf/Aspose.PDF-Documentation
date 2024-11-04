---
title: Hapus Halaman PDF secara programatik
linktitle: Hapus Halaman PDF
type: docs
weight: 40
url: /java/delete-pages/
description: Anda dapat menghapus halaman dari file PDF Anda menggunakan perpustakaan Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Anda dapat menghapus halaman dari file PDF menggunakan Aspose.PDF untuk Java. Untuk menghapus halaman tertentu dari [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/pagecollection) cukup panggil metode delete() dan tentukan indeks halaman tertentu yang ingin Anda hapus. Kemudian panggil metode save untuk menyimpan file PDF yang diperbarui.

## Hapus Halaman dari File PDF

1. Panggil metode Delete dan tentukan indeks halaman
1. Panggil metode Save untuk menyimpan file PDF yang diperbarui
Cuplikan kode berikut menunjukkan cara menghapus halaman tertentu dari file PDF menggunakan Java.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleDeletePage {

  private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

  public static void DeletePageFromPDFFile() {

    // Buka dokumen
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // Hapus halaman tertentu
    pdfDocument.getPages().delete(2);

    _dataDir = _dataDir + "DeleteParticularPage_out.pdf";
    // Simpan PDF yang diperbarui
    pdfDocument.save(_dataDir);    

  }
```