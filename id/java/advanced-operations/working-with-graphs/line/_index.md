---
title: Tambahkan Bentuk Garis ke PDF dalam Java
linktitle: Tambahkan Garis
type: docs
weight: 40
url: /id/java/add-line/
description: Pelajari cara menggambar bentuk garis dan garis bergaya dalam file PDF menggunakan Java.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gambar bentuk garis dalam file PDF menggunakan Java
Abstract: Artikel ini menunjukkan cara menambahkan bentuk garis ke dokumen PDF menggunakan Aspose.PDF for Java. Artikel ini mencakup pembuatan garis dari array koordinat, penerapan gaya garis putus-putus dan warna, serta menggambar garis melintasi seluruh area halaman.
---
## Tambahkan garis putus-putus

1. Buat PDF baru [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Tambahkan [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ke dokumen.
1. Buat [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) container dan tambahkan ke halaman.
1. Buat [Line](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) bentuk dan konfigurasikan koordinatnya.
1. Tambahkan [Line](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) ke [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) wadah.
1. Simpan PDF output [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addLine(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(100.0, 400.0);
        page.getParagraphs().add(graph);

        Line line = new Line(new float[]{100, 100, 200, 100});
        line.getGraphInfo().setDashArray(new int[]{0, 1, 0});
        line.getGraphInfo().setDashPhase(1);
        graph.getShapes().addItem(line);

        document.save(outputFile.toString());
    }
}
```

## Tambahkan garis berwarna bertitik atau putus-putus

`addDottedDashedLine` menggunakan koordinat dan pengaturan dash yang sama, tetapi juga menerapkan `Color.getRed()`.

## Gambar garis melintasi halaman

1. Buat PDF baru [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Tambahkan [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ke dokumen.
1. Buat [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) container dan tambahkan ke halaman.
1. Buat [Line](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) bentuk dan konfigurasikan koordinatnya.
1. Tambahkan [Line](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) ke [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) wadah.
1. Simpan PDF output [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void drawLineAcrossPage(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getPageInfo().getMargin().setLeft(0);
        page.getPageInfo().getMargin().setRight(0);
        page.getPageInfo().getMargin().setBottom(0);
        page.getPageInfo().getMargin().setTop(0);

        Graph graph = new Graph(page.getPageInfo().getWidth(), page.getPageInfo().getHeight());
        Line line = new Line(new float[]{
                (float) page.getRect().getLLX(),
                0,
                (float) page.getPageInfo().getWidth(),
                (float) page.getRect().getURY()
        });
        graph.getShapes().addItem(line);
        page.getParagraphs().add(graph);

        document.save(outputFile.toString());
    }
}
```
