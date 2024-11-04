---
title: Set Ukuran Gambar
linktitle: Set Ukuran Gambar
type: docs
weight: 80
url: /java/set-image-size/
description: Bagian ini menjelaskan cara mengatur ukuran gambar dalam file PDF menggunakan pustaka Java.
lastmod: "2021-06-05"
---

Dimungkinkan untuk mengatur ukuran gambar yang ditambahkan ke file PDF. Untuk mengatur ukuran, Anda dapat menggunakan metode [setFixWidth](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image#setFixWidth-double-) dan [setFixHeight](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image#setFixHeight-double-) dari Kelas com.aspose.pdf.Image.

Cuplikan kode berikut menunjukkan cara mengatur ukuran gambar:

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleSetImageSize {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void Replace() {
        // Membuat objek Document
        Document doc = new Document();
        // menambahkan halaman ke koleksi halaman file PDF
        Page page = doc.getPages().add();
        // Membuat instance gambar
        Image img = new Image();
        // Mengatur Lebar dan Tinggi Gambar dalam Poin
        img.setFixWidth (100);
        img.setFixHeight (100);
        // Mengatur jenis gambar sebagai SVG
        img.setFileType (ImageFileType.Svg);
        // Jalur untuk file sumber
        img.setFile (_dataDir + "aspose-logo.jpg");
        page.getParagraphs().add(img);
        // Mengatur properti halaman
        page.getPageInfo().setWidth(800);
        page.getPageInfo().setHeight(800);        
        // menyimpan file PDF hasil
        doc.save(_dataDir + "SetImageSize_out.pdf");
    }
}
```