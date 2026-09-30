---
title: "Mengekstrak halaman PDF dalam Java"
linktitle: "Mengekstrak halaman PDF"
type: docs
weight: 80
url: /id/java/extract-pages/
description: Pelajari cara mengekstrak satu atau beberapa halaman PDF ke dalam file baru menggunakan Java.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Mengekstrak halaman PDF ke dalam dokumen baru dengan Java"
Abstract: Artikel ini menjelaskan cara mengekstrak halaman dari file PDF menggunakan Aspose.PDF for Java. Artikel ini mencakup menyalin satu halaman dan mengekstrak beberapa halaman ke dalam dokumen tujuan terpisah menggunakan indeks halaman berbasis 1.
---
Aspose.PDF for Java memungkinkan Anda menyalin halaman yang dipilih ke dalam dokumen tujuan baru.

## Mengekstrak satu halaman

Gunakan contoh ini ketika Anda perlu menyimpan satu halaman dari PDF sumber ke dalam dokumen terpisah.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan buat dokumen tujuan.
1. Salin halaman target ke dalam koleksi halaman tujuan.
1. Simpan PDF baru.

```java
public static void extractPage(Path inputFile, Path outputFile) {
    try (Document srcDocument = new Document(inputFile.toString());
         Document dstDocument = new Document()) {
        dstDocument.getPages().add(srcDocument.getPages().get_Item(2));
        dstDocument.save(outputFile.toString());
    }
}
```

## Mengekstrak beberapa halaman

Gunakan contoh ini ketika Anda perlu menyalin beberapa halaman ke PDF terpisah.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan buat dokumen tujuan.
1. Iterasikan melalui indeks halaman yang dipilih dan tambahkan ke tujuan.
1. Simpan dokumen halaman-terekstrak.

```java
public static void extractBunchPages(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString());
         Document anotherDocument = new Document()) {
        Integer[] pages = {2, 3};
        for (Integer pageIndex : pages) {
            anotherDocument.getPages().add(document.getPages().get_Item(pageIndex));
        }
        anotherDocument.save(outputFile.toString());
    }
}
```
