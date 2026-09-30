---
title: "Bekerja dengan lapisan PDF menggunakan Java"
linktitle: Bekerja dengan lapisan PDF
type: docs
weight: 50
url: /id/java/working-with-pdf-layers/
description: Pelajari cara menambahkan, mengunci, mengekstrak, meratakan, dan menggabungkan lapisan PDF dalam Java.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Mengelola lapisan PDF dengan Java"
Abstract: Artikel ini menjelaskan cara bekerja dengan lapisan PDF, yang juga dikenal sebagai Optional Content Groups, menggunakan Aspose.PDF for Java. Pelajari cara menambahkan lapisan ke halaman, mengunci lapisan yang ada, mengekstrak konten lapisan ke file atau aliran, meratakan konten berlapis, dan menggabungkan lapisan menjadi satu.
---
Aspose.PDF for Java mengekspos lapisan PDF melalui `Layer` API pada setiap halaman. Anda dapat membuat grup konten opsional, mengubah perilakunya, dan mengekspor atau meratakan kontennya bila diperlukan.

## Menambahkan lapisan ke halaman PDF

1. Buat PDF baru [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Tambahkan [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ke dokumen.
1. Buat dan konfigurasikan yang diperlukan objek [`Layer`](https://reference.aspose.com/pdf/java/com.aspose.pdf/layer/) pada halaman.
1. Simpan PDF output [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addLayers(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        Layer layer = new Layer("oc1", "Red Line");
        layer.getContents().add(new SetRGBColorStroke(1, 0, 0));
        layer.getContents().add(new MoveTo(500, 700));
        layer.getContents().add(new LineTo(400, 700));
        layer.getContents().add(new Stroke());
        page.getLayers().add(layer);

        document.save(outputFile.toString());
    }
}
```

Contoh lengkap membuat tiga lapisan terpisah dengan konten garis berwarna merah, hijau, dan biru.

## Mengunci lapisan

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Akses [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) target dan dapatkan miliknya [`Layer`](https://reference.aspose.com/pdf/java/com.aspose.pdf/layer/) koleksi.
1. Kunci [`Layer`](https://reference.aspose.com/pdf/java/com.aspose.pdf/layer/) target.
1. Simpan PDF yang diperbarui [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void lockLayer(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        if (!page.getLayers().isEmpty()) {
            Layer layer = page.getLayers().getFirst();
            layer.lock();
            document.save(outputFile.toString());
        }
    }
}
```
