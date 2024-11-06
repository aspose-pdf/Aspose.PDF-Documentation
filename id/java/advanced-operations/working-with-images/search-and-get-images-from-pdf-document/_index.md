---
title: Pencarian dan Mendapatkan Gambar dari Dokumen PDF
linktitle: Pencarian dan Mendapatkan Gambar
type: docs
weight: 60
url: id/java/search-and-get-images-from-pdf-document/
description: Bagian ini menjelaskan cara mencari dan mendapatkan gambar dari dokumen PDF dengan pustaka Aspose.PDF untuk Java.
lastmod: "2021-06-05"
---

[ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacementAbsorber) memungkinkan Anda untuk mencari di antara gambar-gambar di semua halaman dalam dokumen PDF.

Untuk mencari gambar di seluruh dokumen:

1. Panggil metode Accept dari koleksi [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection). Metode Accept menerima objek [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacementAbsorber) sebagai parameter. Ini mengembalikan koleksi objek [ImagePlacement](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacement).
2. Lakukan loop melalui objek ImagePlacements dan dapatkan properti mereka (Gambar, dimensi, resolusi, dan sebagainya).

Cuplikan kode berikut menunjukkan cara mencari semua gambar dalam sebuah dokumen.

```java
package com.aspose.pdf.examples;

import java.io.IOException;
import com.aspose.pdf.*;

public class ExampleSearchAndGet {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void SearchImages() throws IOException {
        // Buka dokumen
        Document doc = new Document(_dataDir + "SearchAndGetImages.pdf");

        // Buat objek ImagePlacementAbsorber untuk melakukan pencarian penempatan gambar
        ImagePlacementAbsorber abs = new ImagePlacementAbsorber();

        // Terima absorber untuk semua halaman
        doc.getPages().accept(abs);

        // Loop melalui semua ImagePlacements, dapatkan gambar dan Properti ImagePlacement
        for (ImagePlacement imagePlacement : abs.getImagePlacements()) {
            // Dapatkan gambar menggunakan objek ImagePlacement
            // XImage image = imagePlacement.getImage();

            // Tampilkan properti penempatan gambar untuk semua penempatan
            System.out.println("lebar gambar:" + imagePlacement.getRectangle().getWidth());
            System.out.println("tinggi gambar:" + imagePlacement.getRectangle().getHeight());
            System.out.println("gambar LLX:" + imagePlacement.getRectangle().getLLX());
            System.out.println("gambar LLY:" + imagePlacement.getRectangle().getLLY());
            System.out.println("resolusi horizontal gambar:" + imagePlacement.getResolution().getX());
            System.out.println("resolusi vertikal gambar:" + imagePlacement.getResolution().getY());
        }

    }
}
```

Untuk mendapatkan gambar dari halaman individu, gunakan kode berikut:

```java
doc.getPages().get_Item(1).accept(abs)
```