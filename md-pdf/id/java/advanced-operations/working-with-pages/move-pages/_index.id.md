---
title: Pindahkan Halaman PDF
linktitle: Pindahkan Halaman
type: docs
weight: 20
url: /java/move-pages/
description: Cobalah memindahkan halaman ke lokasi yang diinginkan atau ke akhir file PDF menggunakan Aspose.PDF untuk Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Memindahkan Halaman dari satu Dokumen PDF ke Dokumen Lain

Topik ini menjelaskan cara memindahkan halaman dari satu dokumen PDF ke akhir dokumen lain menggunakan Java.
Untuk memindahkan halaman kita harus:

1. Buat objek kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) dengan file PDF sumber.
1. Buat objek kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) dengan file PDF tujuan.
1. Dapatkan Halaman dari koleksi [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection).
1. Tambahkan halaman ke dokumen tujuan.
1. Simpan PDF keluaran menggunakan metode Save.
1. Hapus halaman di dokumen sumber.
1. Simpan PDF sumber menggunakan metode Save.

Cuplikan kode berikut menunjukkan kepada Anda cara memindahkan satu halaman.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleMovePDFPages {

  private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

  public static void MovePage() {
    String srcFileName = _dataDir + "<masukkan nama file>";
    String dstFileName = _dataDir + "<masukkan nama file>";
    Document srcDocument = new Document();
    Document dstDocument = new Document();
    Page page = srcDocument.getPages().get_Item(2);
    dstDocument.getPages().add(page);
    // Simpan file output
    dstDocument.save(srcFileName);
    srcDocument.getPages().delete(2);
    srcDocument.save(dstFileName);
  }
```

## Memindahkan beberapa Halaman dari satu Dokumen PDF ke Dokumen Lain

1. Buat objek kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) dengan file PDF sumber.
1. Buat objek kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) dengan file PDF tujuan.
1. Definisikan array dengan nomor halaman yang akan dipindahkan.

1. Jalankan loop melalui array:
   1. Dapatkan Halaman dari koleksi [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection).
   1. Tambahkan halaman ke dokumen tujuan.
1. Simpan output PDF menggunakan metode Save.
1. Hapus halaman dalam dokumen sumber menggunakan array.
1. Simpan PDF sumber menggunakan metode Save.

Cuplikan kode berikut menunjukkan cara menyisipkan halaman kosong di akhir file PDF.

```java
  public static void MoveBunchPages() {
    String srcFileName = _dataDir + "<enter file name>";
    String dstFileName = _dataDir + "<enter file name>";
    Document srcDocument = new Document(srcFileName);
    Document dstDocument = new Document();

    Integer[] pages = { 1, 3 };
    for (int pageIndex : pages) {
      Page page = srcDocument.getPages().get_Item(pageIndex);
      dstDocument.getPages().add(page);
    }
    // Simpan file output
    dstDocument.save(srcFileName);
    srcDocument.getPages().delete(pages);

    srcDocument.save(dstFileName);
  }
```

## Memindahkan Halaman ke lokasi baru dalam Dokumen PDF saat ini

1. Buat objek kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) dengan file PDF sumber.
1. Dapatkan Halaman dari koleksi [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection).
1. Tambahkan halaman ke lokasi baru (misalnya ke akhir).
1. Hapus halaman di lokasi sebelumnya.
1. Simpan PDF keluaran menggunakan metode Save.

```java
  public static void MovePagesInOnePDF() {
    String srcFileName = _dataDir + "<masukkan nama file>";
    String dstFileName = _dataDir + "<masukkan nama file>";

    Document srcDocument = new Document(srcFileName);
    Page page = srcDocument.getPages().get_Item(2);
    srcDocument.getPages().add(page);
    srcDocument.getPages().delete(2);

    // Simpan file keluaran
    srcDocument.save(dstFileName);
  }
}
```