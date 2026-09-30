---
title: "Mengimpor dan mengekspor anotasi menggunakan Java"
linktitle: "Mengimpor dan mengekspor anotasi"
type: docs
weight: 80
url: /id/java/import-export-annotations/
description: Pelajari cara menyalin anotasi dari satu dokumen PDF ke dokumen PDF lainnya menggunakan Aspose.PDF for Java.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Mentransfer anotasi PDF antar dokumen di Java"
Abstract: Artikel ini menjelaskan cara menyalin anotasi dari PDF sumber dan mengekspornya ke dokumen PDF baru menggunakan Aspose.PDF for Java. Alur kerja memuat file sumber, membuat dokumen tujuan, menambahkan halaman, menyalin anotasi dari halaman sumber pertama, dan menyimpan hasilnya.
---
## Menyalin anotasi dari satu PDF ke PDF lain

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Tambahkan sebuah [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ke tujuan [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Tambahkan masing-masing [`Annotation`](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) ke [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) target.
1. Baca atau iterasi melalui [`Annotation`](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) item pada halaman target.
1. Simpan PDF yang diperbarui [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Enumerasikan [`Annotation`](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) item pada halaman sumber pertama dan tambahkan masing-masing ke halaman tujuan.

```java
public static void importExport(Path inputFile, Path outputFile) {
    try (Document sourceDocument = new Document(inputFile.toString());
         Document destinationDocument = new Document()) {
        Page page = destinationDocument.getPages().add();

        for (Annotation annotation : sourceDocument.getPages().get_Item(1).getAnnotations()) {
            page.getAnnotations().add(annotation, true);
        }

        destinationDocument.save(outputFile.toString());
    }
}
```
