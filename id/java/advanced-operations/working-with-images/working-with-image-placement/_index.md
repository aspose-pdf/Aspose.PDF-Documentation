---
title: Bekerja dengan Penempatan Gambar
linktitle: Penempatan Gambar
type: docs
weight: 50
url: /id/java/working-with-image-placement/
description: Bagian ini menjelaskan fitur bekerja dengan penempatan gambar file PDF menggunakan pustaka Java.
lastmod: "2021-06-05"
---

Aspose.PDF untuk Java memperkenalkan kelas yang disebut [ImagePlacement](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacement), [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacementAbsorber) dan [ImagePlacementCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacementCollection) yang menyediakan kemampuan serupa seperti kelas yang dijelaskan di atas untuk mendapatkan resolusi dan posisi gambar dalam dokumen PDF.

- ImagePlacementAbsorber melakukan pencarian penggunaan gambar sebagai koleksi objek ImagePlacement.
- ImagePlacement menyediakan anggota Resolution dan Rectangle yang mengembalikan nilai penempatan gambar aktual.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;


import javax.imageio.ImageIO;

public class ExampleWorkingWithImagePlacement {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void WorkingWithImagePlacement() throws IOException {
        // Muat file PDF sumber
        Document doc = new Document(_dataDir + "ImageInformation.pdf");
        ImagePlacementAbsorber abs = new ImagePlacementAbsorber();

        // Muat konten halaman pertama
        doc.getPages().get_Item(1).accept(abs);
        for (ImagePlacement imagePlacement : abs.getImagePlacements()) {
            // Dapatkan properti gambar
            System.out.println("lebar gambar:" + imagePlacement.getRectangle().getWidth());
            System.out.println("tinggi gambar:" + imagePlacement.getRectangle().getHeight());
            System.out.println("LLX gambar:" + imagePlacement.getRectangle().getLLX());
            System.out.println("LLY gambar:" + imagePlacement.getRectangle().getLLY());
            System.out.println("resolusi horizontal gambar:" + imagePlacement.getResolution().getX());
            System.out.println("resolusi vertikal gambar:" + imagePlacement.getResolution().getY());

            // Ambil gambar dengan dimensi terlihat
            // Bitmap scaledImage;
            // Ambil gambar dari sumber daya
            ByteArrayOutputStream imageStream = new ByteArrayOutputStream();
            imagePlacement.getImage().save(imageStream, ImageType.getPng());

            // Bitmap resourceImage = (Bitmap)Bitmap.FromStream(imageStream);
            BufferedImage resourceImage = ImageIO.read(new ByteArrayInputStream(imageStream.toByteArray()));

            // Buat bitmap dengan dimensi aktual
            BufferedImage scaledImage = toBufferedImage( 
            resourceImage.getScaledInstance((int) imagePlacement.getRectangle().getWidth(),
                    (int) imagePlacement.getRectangle().getHeight(), java.awt.Image.SCALE_SMOOTH));

            ByteArrayOutputStream baos = new ByteArrayOutputStream();
            ImageIO.write(scaledImage, "jpg", baos);
            ByteArrayInputStream fis = new ByteArrayInputStream(baos.toByteArray());

            imagePlacement.getImage().replace(fis);
        }
    }
    
    public static BufferedImage toBufferedImage(java.awt.Image img) {
        if (img instanceof BufferedImage) {
            return (BufferedImage) img;
        }

        // Buat gambar buffered dengan transparansi
        BufferedImage bimage = new BufferedImage(img.getWidth(null), img.getHeight(null), BufferedImage.TYPE_INT_ARGB);

        // Gambar gambar ke gambar buffered
        Graphics2D bGr = bimage.createGraphics();
        bGr.drawImage(img, 0, 0, null);
        bGr.dispose();

        // Kembalikan gambar buffered
        return bimage;
    }
}
```