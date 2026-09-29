---
title: Tambahkan Bentuk Persegi Panjang ke PDF dalam Java
linktitle: Tambahkan Persegi Panjang
type: docs
weight: 50
url: /id/java/add-rectangle/
description: Pelajari cara menggambar dan mengisi bentuk persegi panjang dalam file PDF menggunakan Java.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gambar bentuk persegi panjang dalam file PDF menggunakan Java
Abstract: Artikel ini menunjukkan cara menambahkan bentuk persegi panjang ke dokumen PDF menggunakan Aspose.PDF for Java. Ini mencakup persegi panjang berbingkai, isi padat, isi gradien, transparansi alfa, dan kontrol urutan‑z untuk bentuk yang saling tumpang tindih.
---
## Tambahkan garis tepi persegi panjang

1. Buat PDF baru [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Tambahkan sebuah [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ke dokumen.
1. Buat sebuah [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) wadah dan tambahkan ke halaman.
1. Buat [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) bentuk dan konfigurasikan geometrinya.
1. Tambahkan [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) ke [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) kontainer.
1. Simpan PDF output [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addRectangle(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 300.0);
        page.getParagraphs().add(graph);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getRed()));

        Rectangle rectangle = new Rectangle(20, 20, 350, 250);
        graph.getShapes().addItem(rectangle);

        document.save(outputFile.toString());
    }
}
```

## Isi persegi panjang dengan warna solid atau gradien

Contoh persegi panjang meliputi:

- `createRectangleFilled` untuk isian padat dengan `Color.getRed()`
- `addDrawingWithGradientFill` untuk sebuah `GradientAxialShading` isi

## Gunakan transparansi alfa

`createRectangleWithAlphaColorChannel` menerapkan warna tembus pandang dengan `Color.fromArgb(...)` sehingga persegi panjang yang tumpang tindih tetap terlihat.

## Kontrol urutan z persegi panjang

1. Buat PDF baru [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Tambahkan sebuah [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ke dokumen.
1. Setel yang diperlukan [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ukuran.
1. Tambahkan yang dikonfigurasi [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) bentuk ke halaman target dengan urutan z yang diperlukan.
1. Simpan PDF output [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void controlZOrderOfRectangle(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.setPageSize(375, 300);
        page.getPageInfo().getMargin().setLeft(0);
        page.getPageInfo().getMargin().setTop(0);

        addRectangleToPage(page, 50, 40, 60, 40, Color.getRed(), 2);
        addRectangleToPage(page, 20, 20, 30, 30, Color.getBlue(), 1);
        addRectangleToPage(page, 40, 40, 60, 30, Color.getGreen(), 0);

        document.save(outputFile.toString());
    }
}
```
