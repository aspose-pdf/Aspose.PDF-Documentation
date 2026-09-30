---
title: "Memindahkan halaman PDF dalam Java"
linktitle: "Memindahkan halaman PDF"
type: docs
weight: 100
url: /id/java/move-pages/
description: Pelajari cara memindahkan halaman PDF dalam sebuah dokumen atau antar dokumen dalam Java.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Memindahkan halaman PDF antar dokumen dalam Java
Abstract: Artikel ini menjelaskan cara memindahkan halaman dalam PDF menggunakan Aspose.PDF for Java. Artikel ini mencakup pemindahan satu halaman atau beberapa halaman ke dokumen lain, serta memposisikan ulang sebuah halaman di dalam PDF yang sama.
---
Aspose.PDF for Java memungkinkan Anda memindahkan halaman antar dokumen atau memposisikan ulang halaman dalam PDF yang sama.

## Memindahkan satu halaman ke dokumen lain

Gunakan contoh ini ketika satu halaman harus dihapus dari PDF sumber dan disimpan ke dalam dokumen terpisah.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan buat dokumen tujuan.
1. Tambahkan halaman target ke tujuan dan hapus dari sumber.
1. Simpan kedua dokumen.

```java
public static void movePageFromOneDocumentToAnother(Path inputFile, Path sourceOutputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString());
         Document anotherDocument = new Document()) {
        anotherDocument.getPages().add(document.getPages().get_Item(2));
        document.getPages().delete(2);
        document.save(sourceOutputFile.toString());
        anotherDocument.save(outputFile.toString());
    }
}
```

## Memindahkan beberapa halaman ke dokumen lain

Gunakan contoh ini ketika beberapa halaman harus dipindahkan dari PDF sumber ke dokumen baru.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan buat dokumen tujuan.
1. Salin halaman yang dipilih ke dokumen tujuan.
1. Hapus halaman yang dipindahkan dari sumber dan simpan kedua file.

```java
public static void moveBunchPagesFromOneDocumentToAnother(Path inputFile, Path sourceOutputFile, Path outputFile) {
    try (Document srcDocument = new Document(inputFile.toString());
         Document dstDocument = new Document()) {
        Integer[] pages = {1, 2};
        for (Integer pageIndex : pages) {
            dstDocument.getPages().add(srcDocument.getPages().get_Item(pageIndex));
        }
        dstDocument.save(outputFile.toString());
        srcDocument.getPages().delete(pages);
        srcDocument.save(sourceOutputFile.toString());
    }
}
```

## Memindahkan halaman dalam dokumen yang sama

Gunakan contoh ini ketika sebuah halaman harus dipindahkan ke lokasi baru dalam PDF yang sama.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Duplikat halaman target ke posisi baru dan hapus entri halaman asli.
1. Simpan dokumen yang telah diurutkan ulang.

```java
public static void movePageInNewLocationInSameDocument(Path inputFile, Path outputFile) {
    try (Document srcDocument = new Document(inputFile.toString())) {
        srcDocument.getPages().add(srcDocument.getPages().get_Item(2));
        srcDocument.getPages().delete(2);
        srcDocument.save(outputFile.toString());
    }
}
```
