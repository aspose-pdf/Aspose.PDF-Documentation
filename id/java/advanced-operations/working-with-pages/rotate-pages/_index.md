---
title: "Memutar halaman PDF dalam Java"
linktitle: "Memutar halaman PDF"
type: docs
weight: 110
url: /id/java/rotate-pages/
description: Pelajari cara memutar halaman PDF dan mengubah orientasi halaman dalam Java.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Memutar halaman PDF dengan Java"
Abstract: Artikel ini menjelaskan cara memutar halaman PDF menggunakan Aspose.PDF for Java. Contohnya mengiterasi semua halaman dalam sebuah dokumen, menerapkan rotasi 90 derajat, dan menyimpan PDF yang diperbarui.
---
Gunakan API rotasi halaman ketika Anda perlu mengubah orientasi pada satu atau beberapa halaman.

## Memutar semua halaman sebesar 90 derajat

Gunakan contoh ini ketika setiap halaman dalam dokumen harus diputar searah jarum jam.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterasikan melalui semua objek [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) dan setel nilai rotasi.
1. Simpan PDF yang diperbarui.

```java
public static void rotatePage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Page page : document.getPages()) {
            page.setRotate(Rotation.on90);
        }
        document.save(outputFile.toString());
    }
}
```
