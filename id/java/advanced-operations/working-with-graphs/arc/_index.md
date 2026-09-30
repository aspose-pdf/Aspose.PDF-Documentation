---
title: "Menambahkan bentuk busur ke PDF di Java"
linktitle: "Menambahkan busur"
type: docs
weight: 10
url: /id/java/add-arc/
description: Pelajari cara menggambar dan mengisi bentuk busur dalam file PDF menggunakan Java.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Menggambar bentuk busur dalam file PDF menggunakan Java"
Abstract: Artikel ini menunjukkan cara menambahkan bentuk busur ke dokumen PDF menggunakan Aspose.PDF for Java. Artikel ini mencakup menggambar beberapa busur berbingkai dengan warna yang berbeda dan membuat segmen busur terisi dengan menggabungkan sebuah busur dengan garis penutup.
---
Aspose.PDF for Java menggunakan `Graph` bersama dengan objek bentuk seperti `Arc` dan `Line` untuk merender grafik vektor.

## Menambahkan garis tepi busur

1. Buat PDF baru [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Tambahkan sebuah [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ke dokumen.
1. Buat sebuah [`Graph`](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) container dan tambahkan ke halaman.
1. Buat [`Arc`](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) bentuk dan konfigurasikan geometri-nya.
1. Tambahkan [`Arc`](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) ke [`Graph`](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) wadah.
1. Atur properti bentuk yang diperlukan oleh contoh, termasuk [`Color`](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/).
1. Simpan PDF output [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addArc(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 400.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Arc arc1 = new Arc(100, 100, 95, 0, 90);
        arc1.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().addItem(arc1);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```

Contoh lengkap menambahkan tiga busur dengan jari-jari, sudut, dan warna yang berbeda ke grafik yang sama.

## Menambahkan segmen busur terisi

1. Buat PDF baru [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Tambahkan sebuah [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ke dokumen.
1. Buat sebuah [`Graph`](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) container dan tambahkan ke halaman.
1. Buat [`Line`](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) bentuk dan konfigurasikan koordinatnya.
1. Buat [`Arc`](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) bentuk dan konfigurasikan geometri-nya.
1. Tambahkan [`Line`](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) dan [`Arc`](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) ke [`Graph`](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) wadah.
1. Simpan PDF output [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addArcFilled(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 400.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Arc arc = new Arc(100, 100, 95, 0, 90);
        arc.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().addItem(arc);

        Line line = new Line(new float[]{195, 100, 100, 100, 100, 195});
        line.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().addItem(line);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```
