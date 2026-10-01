---
title: "Menambahkan bentuk lingkaran ke PDF dalam Java"
linktitle: "Menambahkan lingkaran"
type: docs
weight: 20
url: /id/java/add-circle/
description: Pelajari cara menggambar dan mengisi bentuk lingkaran dalam file PDF menggunakan Java.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Menggambar bentuk lingkaran dalam file PDF menggunakan Java"
Abstract: Artikel ini menunjukkan cara menambahkan bentuk lingkaran ke dokumen PDF menggunakan Aspose.PDF for Java. Ini mencakup menggambar garis tepi lingkaran, mengisi lingkaran dengan warna, dan menempatkan teks di dalam bentuk lingkaran.
---
## Menambahkan garis tepi lingkaran

1. Buat PDF baru [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Tambahkan [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ke dokumen.
1. Buat [`Graph`](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) kontainer dan tambahkan ke halaman.
1. Buat [`Circle`](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) bentuk dan konfigurasikan geometri-nya.
1. Tambahkan [`Circle`](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) ke [`Graph`](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) wadah.
1. Atur properti bentuk yang diperlukan oleh contoh, termasuk [`Color`](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/).
1. Simpan PDF output [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addCircle(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 200.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Circle circle = new Circle(100, 100, 40);
        circle.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().addItem(circle);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```

## Menambahkan lingkaran berisi dengan teks

1. Buat PDF baru [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Tambahkan [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ke dokumen.
1. Buat [`Graph`](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) kontainer dan tambahkan ke halaman.
1. Buat [`Circle`](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) bentuk dan konfigurasikan geometri-nya.
1. Tambahkan [`Circle`](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) ke [`Graph`](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) wadah.
1. Atur properti bentuk yang diperlukan oleh contoh, termasuk [`Color`](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/) dan [`TextFragment`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/).
1. Simpan PDF output [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addCircleFilled(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 200.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Circle circle = new Circle(100, 100, 40);
        circle.getGraphInfo().setColor(Color.getGreenYellow());
        circle.getGraphInfo().setFillColor(Color.getGreen());
        circle.setText(new TextFragment("Circle"));
        graph.getShapes().addItem(circle);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```
