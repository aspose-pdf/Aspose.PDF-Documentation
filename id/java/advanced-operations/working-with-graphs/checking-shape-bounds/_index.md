---
title: "Memeriksa batas bentuk dalam grafik PDF dengan Java"
linktitle: "Memeriksa batas bentuk"
type: docs
weight: 70
url: /id/java/aspose-pdf-drawing-graph-shapes-bounds-check/
description: Pelajari cara memvalidasi batas bentuk dalam koleksi grafik PDF di Java.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Memvalidasi batas bentuk grafik dalam file PDF menggunakan Java"
Abstract: Artikel ini menunjukkan cara memvalidasi batas bentuk dalam koleksi Graph menggunakan Aspose.PDF for Java. Artikel ini mencakup mengaktifkan pemeriksaan batas ketat, mencoba menambahkan bentuk di luar jangkauan, dan menangani pengecualian yang dihasilkan sambil tetap menyimpan dokumen.
---
Gunakan `BoundsCheckMode` ketika Anda perlu memastikan bahwa bentuk berada di dalam wadah grafik.

## Memvalidasi batas bentuk grafik

1. Buat PDF baru [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Tambahkan sebuah [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ke dokumen.
1. Buat sebuah [`Graph`](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) kontainer dan tambahkan ke halaman.
1. Buat [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) bentuk dan konfigurasikan geometrinya.
1. Aktifkan pemeriksaan batas yang ketat dan coba tambahkan bentuk ke koleksi grafik dengan `BoundsCheckMode`.
1. Tangani pengecualian jika bentuk tidak cocok.
1. Simpan PDF output [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void checkShapeBounds(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(100.0, 100.0);
        graph.setTop(10);
        graph.setLeft(15);
        graph.setBorder(new BorderInfo(BorderSide.Box, 1, Color.getBlack()));
        page.getParagraphs().add(graph);

        Rectangle rectangle = new Rectangle(-1, 0, 50, 50);
        rectangle.getGraphInfo().setFillColor(Color.getTomato());
        try {
            graph.getShapes().updateBoundsCheckMode(BoundsCheckMode.ThrowExceptionIfDoesNotFit);
            graph.getShapes().addItem(rectangle);
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }

        document.save(outputFile.toString());
    }
}
```
