---
title: Ekstrak Gambar dari File PDF
linktitle: Ekstrak Gambar
type: docs
weight: 30
url: id/java/extract-images-from-pdf-file/
description: Bagian ini menunjukkan cara mengekstrak gambar dari file PDF menggunakan pustaka Java.
lastmod: "2021-06-05"
---

Setiap halaman memiliki koleksi [Resources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources), dan ini, pada gilirannya, memegang koleksi Gambar, di mana semua gambar dalam halaman disimpan. Objek [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage) mendapatkan gambar tertentu dalam koleksi Gambar.

Untuk mengekstrak gambar dari halaman:

Dapatkan gambar dari koleksi Gambar menggunakan indeks gambar.  
Gunakan metode simpan(..) dari objek [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage) untuk menyimpan gambar yang diekstraksi.

Cuplikan kode berikut menunjukkan cara mengekstrak gambar dari file PDF.

```java
package com.aspose.pdf.examples;

import java.io.FileOutputStream;
import java.io.IOException;

import com.aspose.pdf.*;
import com.aspose.pdf.internal.html.rendering.image.ImageFormat;

public class ExampleExtractImages {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ExtractImages() throws IOException {

        // Buka dokumen
        Document pdfDocument = new Document(_dataDir + "ExtractImages.pdf");

        // Ekstrak gambar tertentu
        XImage xImage = pdfDocument.getPages().get_Item(1).getResources().getImages().get_Item(1);

        FileOutputStream outputImage = new FileOutputStream(_dataDir + "output.jpg");

        // Simpan gambar keluaran
        xImage.save(outputImage, ImageFormat.Jpeg);
        outputImage.close();

        // Simpan file PDF yang diperbarui
        pdfDocument.save(_dataDir + "ExtractImages_out.pdf");
    }
}
```