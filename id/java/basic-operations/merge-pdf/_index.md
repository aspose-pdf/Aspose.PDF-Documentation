---
title: "Menggabungkan file PDF di Java"
linktitle: "Menggabungkan file PDF"
type: docs
weight: 50
url: /id/java/merge-pdf/
description: Pelajari cara menggabungkan banyak file PDF menjadi satu dokumen di Java menggunakan Aspose.PDF.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Menggabungkan halaman PDF menggunakan Java"
Abstract: Artikel ini menjelaskan cara menggabungkan dua dokumen PDF di Java menggunakan Aspose.PDF. Contohnya membuka dua dokumen sumber, menambahkan halaman dokumen kedua ke dokumen pertama, dan menyimpan hasil gabungan sebagai file PDF baru.
---
Menggabungkan file PDF berguna ketika Anda perlu menggabungkan dokumen terkait menjadi satu file untuk distribusi, pengarsipan, atau pemrosesan.

## Contoh langsung

[Aspose.PDF Penggabung](https://products.aspose.app/pdf/merger) adalah aplikasi online gratis untuk menguji penggabungan PDF di peramban.

Topik ini menunjukkan cara menggabungkan beberapa file PDF menjadi satu dokumen dalam Java:

1. Buka kedua dokumen sumber dengan konstruktor [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Tambahkan [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) koleksi dari yang kedua [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) ke yang pertama dengan `document1.getPages().add(document2.getPages())`.
1. Simpan yang digabungkan [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) ke jalur output.

## Menggabungkan dua dokumen PDF

Contoh Java berikut didasarkan pada `MergeDocumentExamples.java`.

```java
public static void mergeTwoDocuments(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        document1.getPages().add(document2.getPages());
        document1.save(outputFile.toString());
    }
}
```
