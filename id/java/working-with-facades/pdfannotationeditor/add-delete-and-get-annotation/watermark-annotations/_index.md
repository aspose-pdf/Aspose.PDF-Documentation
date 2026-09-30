---
title: "Anotasi watermark menggunakan Java"
linktitle: "Anotasi watermark"
type: docs
weight: 70
url: /id/java/pdfannotationeditor-class/watermark-annotations/
description: Pelajari cara menambahkan, memeriksa, dan menghapus anotasi watermark dalam dokumen PDF menggunakan Java.
lastmod: "2026-09-30"
TechArticle: true
AlternativeHeadline: Bekerja dengan anotasi watermark dalam file PDF menggunakan Java
Abstract: Artikel ini menjelaskan cara membuat, memeriksa, dan menghapus anotasi watermark dalam dokumen PDF menggunakan Java. Artikel ini mencakup penambahan anotasi watermark teks dengan keadaan teks khusus dan opasitas, membaca area anotasi watermark yang ada, serta menghapus anotasi watermark.
---
## Menambahkan anotasi watermark

1. Buka PDF input dan definisikan persegi panjang tempat anotasi watermark akan ditempatkan.
2. Buat `WatermarkAnnotation`, tambahkan ke halaman, dan konfigurasikan status teks watermark serta opasitas.
3. Terapkan baris teks watermark dan simpan PDF yang telah dimodifikasi.

```java
public static void watermarkAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        WatermarkAnnotation watermarkAnnotation = new WatermarkAnnotation(
                document.getPages().get_Item(1), new Rectangle(100, 0, 400, 100, true));

        document.getPages().get_Item(1).getAnnotations().add(watermarkAnnotation);

        TextState textState = new TextState();
        textState.setForegroundColor(Color.getBlue());
        textState.setFontSize(25);
        textState.setFont(FontRepository.findFont("Arial"));

        watermarkAnnotation.setOpacity(0.5);
        watermarkAnnotation.setTextAndState(new String[]{"HELLO", "Line 1", "Line 2"}, textState);

        document.save(outputFile.toString());
    }
}
```
