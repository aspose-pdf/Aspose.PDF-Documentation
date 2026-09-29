---
title: Tambahkan Bentuk Kurva ke PDF di Java
linktitle: Tambahkan Kurva
type: docs
weight: 30
url: /id/java/add-curve/
description: Pelajari cara menggambar dan mengisi bentuk kurva dalam file PDF menggunakan Java.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gambar bentuk kurva dalam file PDF menggunakan Java
Abstract: Artikel ini menunjukkan cara menambahkan bentuk kurva ke dokumen PDF menggunakan Aspose.PDF for Java. Artikel ini mencakup pembuatan kurva dari array koordinat dan menerapkan baik warna garis tepi maupun warna isi di dalam kontainer Graph.
---
Kurva dalam Aspose.PDF for Java didefinisikan oleh array koordinat float yang diteruskan ke `Curve`.

## Tambahkan outline kurva

1. Buat PDF baru [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Tambahkan [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ke dokumen.
1. Buat sebuah [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) kontainer dan tambahkan ke halaman.
1. Buat [Curve](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/curve/) bentuk dan konfigurasikan titik kontrolnya.
1. Tambahkan [Curve](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/curve/) ke [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) kontainer.
1. Atur properti bentuk yang diperlukan oleh contoh, termasuk [Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/).
1. Simpan PDF output [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addCurve(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 200.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Curve curve1 = new Curve(new float[]{10, 10, 50, 60, 70, 10, 100, 120});
        curve1.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().addItem(curve1);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```
