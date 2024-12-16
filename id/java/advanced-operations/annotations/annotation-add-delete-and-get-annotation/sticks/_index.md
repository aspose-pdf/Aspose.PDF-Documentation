---
title: PDF Sticky Annotations 
linktitle: Sticky Annotation
type: docs
weight: 50
url: /id/java/sticky-annotations/
description: Topik ini tentang anotasi sticky, sebagai contoh kami menunjukkan Anotasi Watermark dalam teks. Ini digunakan untuk merepresentasikan grafik pada halaman. Periksa potongan kode untuk menyelesaikan tugas ini.
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Tambahkan Anotasi Watermark

Anotasi watermark harus digunakan untuk merepresentasikan grafik yang akan dicetak pada ukuran dan posisi tetap pada halaman, terlepas dari dimensi halaman yang dicetak.

Anda dapat menambahkan Teks Watermark menggunakan [WatermarkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/WatermarkAnnotation) pada posisi tertentu dari halaman PDF. Opasitas dari Watermark juga dapat dikendalikan dengan menggunakan properti opasitas.

Silakan periksa potongan kode berikut untuk menambahkan WatermarkAnnotation.

```java
 package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import java.util.*;

public class ExampleWatermarkAnnotation {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddWaterMarkAnnotation()
    {
        // Muat file PDF
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        //Buat Anotasi
        WatermarkAnnotation wa = new WatermarkAnnotation(page, new Rectangle(100, 500, 400, 600));

        //Tambahkan anotasi ke dalam koleksi Anotasi dari Halaman
        page.getAnnotations().add(wa);

        //Buat TextState untuk pengaturan Font
        TextState ts = new TextState();

        ts.setForegroundColor(Color.getBlue());
        ts.setFont(FontRepository.findFont("Times New Roman"));
        ts.setFontSize(32);

        //Setel tingkat opasitas dari Teks Anotasi
        wa.setOpacity(0.5);

        //Tambahkan Teks ke Anotasi
        wa.setTextAndState(new String[] { "Aspose.PDF", "Watermark", "Demo" }, ts);

        //Simpan Dokumen
        document.save(_dataDir + "sample_watermark.pdf");
    }
}
```


## Dapatkan Anotasi Watermark

```java
    public static void GetWatermarkAnnotation() {
        // Muat file PDF
        Document document = new Document(_dataDir + "sample_watermark.pdf");

        // Filter anotasi menggunakan AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new WatermarkAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> WatermarkAnnotations = annotationSelector.getSelected();

        // cetak hasil
        for (Annotation fa : WatermarkAnnotations) {
            System.out.println(fa.getRect());
        }
    }
```

## Hapus Anotasi Watermark

```java
    public static void DeleteWatermarkAnnotation() {
         // Muat file PDF
         Document document = new Document(_dataDir + "sample_watermark.pdf");

         // Filter anotasi menggunakan AnnotationSelector
         Page page = document.getPages().get_Item(1);
         AnnotationSelector annotationSelector = new AnnotationSelector(
                 new WatermarkAnnotation(page, Rectangle.getTrivial()));
         page.accept(annotationSelector);
         List<Annotation> WatermarkAnnotations = annotationSelector.getSelected();

         // hapus anotasi
         for (Annotation fa : WatermarkAnnotations) {
            page.getAnnotations().delete(fa);
        }
        document.save(_dataDir + "sample_watermark_del.pdf");
    }
```