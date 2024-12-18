---
title: Setel Nama Font Default
linktitle: Setel Nama Font Default
type: docs
weight: 90
url: /id/java/set-default-font-name/
description: Bagian ini menjelaskan cara mengatur nama font default menggunakan pustaka Aspose.PDF untuk Java.
lastmod: "2021-06-05"
---

**Aspose.PDF untuk Java** API memungkinkan Anda untuk mengatur nama font default ketika font tidak tersedia dalam dokumen. Anda dapat menggunakan metode [setDefaultFontName](https://reference.aspose.com/pdf/java/com.aspose.pdf/RenderingOptions#setDefaultFontName-java.lang.String-) dari kelas [RenderingOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/RenderingOptions) untuk mengatur nama font default. Jika setDefaultFontName diatur ke null, font **Times New Roman** akan digunakan.

Cuplikan kode berikut menunjukkan cara mengatur nama font default saat menyimpan PDF ke dalam gambar:

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;

import com.aspose.pdf.*;
import com.aspose.pdf.devices.PngDevice;
import com.aspose.pdf.devices.Resolution;

public class ExampleSetDefaultFontName {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void SetDefaultFontName() {
        
        Document pdfDocument = new Document(_dataDir + "input.pdf");
        FileOutputStream imageStream = null;;
        try {
            imageStream = new FileOutputStream(_dataDir + "SetDefaultFontName.png");
        } catch (FileNotFoundException e) {
            // TODO Blok penanganan catch
            e.printStackTrace();
        }

        Resolution resolution = new Resolution(300);
        PngDevice pngDevice = new PngDevice(resolution);
        RenderingOptions ro = new RenderingOptions();
        ro.setDefaultFontName ("Arial");
        pngDevice.setRenderingOptions(ro);
        pngDevice.process(pdfDocument.getPages().get_Item(1), imageStream);
    }    
}
```