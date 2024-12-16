---
title: Penggabungan PDF secara programatik
linktitle: Gabungkan file PDF
type: docs
weight: 50
url: /id/java/merge-pdf-documents/
description: Halaman ini menjelaskan cara menggabungkan dokumen PDF menjadi satu file PDF dengan Java.
lastmod: "2021-06-05"
---

Sekarang, menggabungkan file pdf adalah salah satu tugas yang paling banyak diminta.
Artikel ini menunjukkan cara menggabungkan beberapa file PDF menjadi satu dokumen PDF menggunakan Aspose.PDF untuk Java. Contohnya ditulis dalam Java, tetapi API dapat digunakan dalam bahasa pemrograman lain. File PDF digabungkan sedemikian rupa sehingga yang pertama digabungkan di akhir dokumen lainnya.

## Menggabungkan File PDF menggunakan Java

{{% alert color="primary" %}}

Anda dapat menggabungkan file PDF menggunakan Aspose.PDF dan mendapatkan hasilnya secara online di tautan ini: [products.aspose.app/pdf/merger](https://products.aspose.app/pdf/merger)

{{% /alert %}}

Untuk menggabungkan dua file PDF:

1. Buat dua objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document), masing-masing berisi salah satu file PDF input.

1. Kemudian panggil metode Add dari koleksi [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection) untuk objek Document yang ingin Anda tambahkan file PDF lainnya.
1. Lulus koleksi PageCollection dari objek Document kedua ke metode Add dari koleksi PageCollection pertama.
1. Terakhir, simpan file PDF keluaran menggunakan metode Save.

Cuplikan kode berikut menunjukkan cara menggabungkan file PDF dengan Java.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleMerge {
    // Jalur ke direktori dokumen.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void Merge() {
        
        // Buka dokumen pertama
        Document pdfDocument1 = new Document(_dataDir + "Concat1.pdf");
        // Buka dokumen kedua
        Document pdfDocument2 = new Document(_dataDir + "Concat2.pdf");

        // Tambahkan halaman dokumen kedua ke yang pertama
        pdfDocument1.getPages().add(pdfDocument2.getPages());

        // Simpan file output yang telah digabungkan
        pdfDocument1.save(_dataDir+"ConcatenatePdfFiles_out.pdf");

    }

}
```