---
title: "Anotasi bentuk via Java"
linktitle: "Anotasi bentuk"
type: docs
weight: 40
url: /id/java/pdfannotationeditor-class/shape-annotations/
description: Pelajari cara menambah, memeriksa, dan menghapus anotasi persegi, lingkaran, poligon, dan polyline dalam dokumen PDF menggunakan Java.
lastmod: "2026-09-30"
TechArticle: true
AlternativeHeadline: Bekerja dengan anotasi PDF geometris di Java
Abstract: Artikel ini menjelaskan cara membuat, memeriksa, dan menghapus anotasi geometris dalam dokumen PDF menggunakan Java. Artikel ini mencakup anotasi persegi, lingkaran, poligon, dan polyline dengan warna, opacity, popup, dan konfigurasi titik.
---
## Menambahkan anotasi bentuk

1. Buka PDF input dan pilih halaman serta persegi panjang yang akan berisi anotasi bentuk.
2. Buat anotasi bentuk yang diperlukan, kemudian atur judul, warna, opasitas, dan titik-titiknya bila diperlukan.
3. Tambahkan anotasi ke halaman dan simpan PDF yang telah dimodifikasi.

```java
public static void squareAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        SquareAnnotation squareAnnotation = new SquareAnnotation(
                document.getPages().get_Item(1), new Rectangle(60, 600, 250, 450, true));
        squareAnnotation.setTitle("John Smith");
        squareAnnotation.setColor(Color.getBlue());
        squareAnnotation.setInteriorColor(Color.getBlueViolet());
        squareAnnotation.setOpacity(0.25);

        document.getPages().get_Item(1).getAnnotations().add(squareAnnotation);
        document.save(outputFile.toString());
    }
}
```

```java
public static void polygonAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PolygonAnnotation polygonAnnotation = new PolygonAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(200, 300, 400, 400, true),
                new Point[]{
                        new Point(200, 300),
                        new Point(220, 300),
                        new Point(250, 330),
                        new Point(300, 304),
                        new Point(300, 400)
                });
        polygonAnnotation.setTitle("John Smith");
        polygonAnnotation.setColor(Color.getBlue());
        polygonAnnotation.setInteriorColor(Color.getBlueViolet());
        polygonAnnotation.setOpacity(0.25);

        document.getPages().get_Item(1).getAnnotations().add(polygonAnnotation);
        document.save(outputFile.toString());
    }
}
```
