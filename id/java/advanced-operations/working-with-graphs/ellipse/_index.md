---
title: "Menambahkan bentuk ellips ke PDF dalam Java"
linktitle: "Menambahkan ellips"
type: docs
weight: 60
url: /id/java/add-ellipse/
description: Pelajari cara menggambar, mengisi, dan memberi label bentuk ellips dalam file PDF menggunakan Java.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Menggambar bentuk ellips dalam file PDF menggunakan Java"
Abstract: Artikel ini menunjukkan cara menambahkan bentuk ellips ke dokumen PDF menggunakan Aspose.PDF for Java. Ini mencakup ellips berkontur, ellips terisi, dan penempatan fragmen teks di dalam bentuk ellips.
---
## Menambahkan kontur ellips

1. Buat PDF baru [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Tambahkan [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ke dokumen.
1. Buat [`Graph`](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) wadah dan tambahkan ke halaman.
1. Buat [`Ellipse`](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/ellipse/) bentuk dan konfigurasikan geometri-nya.
1. Tambahkan [`Ellipse`](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/ellipse/) ke [`Graph`](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) wadah.
1. Atur properti bentuk yang diperlukan oleh contoh, termasuk [`Color`](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/) dan [`TextFragment`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/).
1. Simpan PDF output [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addEllipse(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 400.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Ellipse ellipse1 = new Ellipse(150, 100, 120, 60);
        ellipse1.getGraphInfo().setColor(Color.getGreenYellow());
        ellipse1.setText(new TextFragment("Ellipse"));
        graph.getShapes().addItem(ellipse1);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```

Contoh lengkap menambahkan dua elips outline yang berbeda ke grafik yang sama.

## Menambahkan elips terisi

`createEllipseFilled` mengisi dua elipsis dengan `Color.getGreenYellow()` dan `Color.getDarkRed()`.

## Menambahkan teks di dalam elips

1. Buat PDF baru [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Tambahkan [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ke dokumen.
1. Buat [`TextFragment`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) dan atur opsi pemformatan teks yang diperlukan.
1. Buat [`Graph`](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) wadah dan tambahkan ke halaman.
1. Buat [`Ellipse`](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/ellipse/) bentuk dan konfigurasikan geometri-nya.
1. Tambahkan [`Ellipse`](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/ellipse/) ke [`Graph`](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) wadah.
1. Simpan PDF output [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addTextInsideEllipse(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 400.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        TextFragment textFragment = new TextFragment("Ellipse");
        textFragment.getTextState().setFont(FontRepository.findFont("Helvetica"));
        textFragment.getTextState().setFontSize(24);

        Ellipse ellipse1 = new Ellipse(100, 100, 120, 180);
        ellipse1.getGraphInfo().setFillColor(Color.getGreenYellow());
        ellipse1.setText(textFragment);
        graph.getShapes().addItem(ellipse1);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```
