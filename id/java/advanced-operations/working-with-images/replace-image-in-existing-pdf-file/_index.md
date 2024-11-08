---
title: Mengganti Gambar dalam File PDF yang Ada
linktitle: Ganti Gambar
type: docs
weight: 70
url: /id/java/replace-image-in-existing-pdf-file/
description: Bagian ini menjelaskan tentang mengganti gambar dalam file PDF yang ada menggunakan pustaka Java.
lastmod: "2021-06-05"
---

Metode [Replace](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection#replace-int-java.io.InputStream-) dari koleksi [XImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection) memungkinkan Anda untuk mengganti gambar dalam file PDF yang ada.

Koleksi Gambar dapat ditemukan dalam koleksi Sumber Daya halaman. Untuk mengganti gambar:

1. Buka file PDF menggunakan objek Document.
2. Ganti gambar tertentu, simpan file PDF yang diperbarui menggunakan metode Save dari objek Document.

Cuplikan kode berikut menunjukkan cara mengganti gambar dalam file PDF.

```java
package com.aspose.pdf.examples;

import java.io.FileInputStream;
import java.io.FileNotFoundException;

import com.aspose.pdf.Document;

public class ExampleReplaceImage {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";
    public static void Replace() {
        // Buka dokumen
        Document pdfDocument = new Document("input.pdf");
        // Ganti gambar tertentu
        try {
            pdfDocument.getPages().get_Item(1).getResources().getImages().replace(1, new FileInputStream("lovely.jpg"));
        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        // Simpan file PDF yang diperbarui
        pdfDocument.save(_dataDir + "output.pdf");
    }
}
```