---
title: "Menambahkan dan menghapus penanda PDF di Java"
linktitle: "Menambahkan dan menghapus penanda"
type: docs
weight: 10
url: /id/java/add-and-delete-bookmark/
description: Pelajari cara menambahkan dan menghapus penanda dalam dokumen PDF menggunakan Java.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Menambahkan atau menghapus penanda dalam dokumen PDF dengan Java"
Abstract: Artikel ini menunjukkan cara membuat dan menghapus bookmark menggunakan Aspose.PDF for Java. Contoh-contohnya memperlihatkan penambahan bookmark tingkat atas, pembuatan hierarki bookmark anak, menghapus semua bookmark, dan menghapus bookmark tertentu berdasarkan judul.
---
Gunakan koleksi outline dokumen untuk mengelola bookmark secara programatis.

## Menambahkan bookmark tingkat atas

Gunakan contoh ini ketika dokumen harus mencakup satu entri outline tingkat atas.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat sebuah [`OutlineItemCollection`](https://reference.aspose.com/pdf/java/com.aspose.pdf/outlineitemcollection/) dan konfigurasikan judulnya, gaya, dan aksi.
1. Tambahkan penanda buku ke outline dokumen dan simpan file.

```java
public static void addBookmark(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        OutlineItemCollection pdfOutline = new OutlineItemCollection(document.getOutlines());
        pdfOutline.setTitle("Test Outline");
        pdfOutline.setItalic(true);
        pdfOutline.setBold(true);
        pdfOutline.setAction(new GoToAction(document.getPages().get_Item(1)));

        document.getOutlines().add(pdfOutline);
        document.save(outputFile.toString());
    }
}
```

## Menambahkan bookmark anak

Contoh ini membuat bookmark induk dan menempatkan bookmark anak di bawahnya.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat induk dan anak objek [`OutlineItemCollection`](https://reference.aspose.com/pdf/java/com.aspose.pdf/outlineitemcollection/).
1. Tambahkan anak ke induk, tambahkan induk ke koleksi outline, dan simpan dokumen.

```java
public static void addChildBookmark(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        OutlineItemCollection pdfOutline = new OutlineItemCollection(document.getOutlines());
        pdfOutline.setTitle("Parent Outline");
        pdfOutline.setItalic(true);
        pdfOutline.setBold(true);

        OutlineItemCollection pdfChildOutline = new OutlineItemCollection(document.getOutlines());
        pdfChildOutline.setTitle("Child Outline");
        pdfChildOutline.setItalic(true);
        pdfChildOutline.setBold(true);

        pdfOutline.add(pdfChildOutline);
        document.getOutlines().add(pdfOutline);
        document.save(outputFile.toString());
    }
}
```

## Menghapus semua penanda buku

Gunakan pendekatan ini ketika seluruh koleksi outline harus dihapus dari dokumen.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Hapus seluruh koleksi outline.
1. Simpan file output yang telah dibersihkan.

```java
public static void deleteBookmarks(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getOutlines().delete();
        document.save(outputFile.toString());
    }
}
```

## Menghapus bookmark tertentu

Gunakan contoh ini ketika satu bookmark bernama harus dihapus tanpa mengosongkan seluruh pohon garis besar.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Hapus bookmark berdasarkan judul dari koleksi outline.
1. Simpan dokumen yang diperbarui.

```java
public static void deleteBookmark(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getOutlines().delete("Child Outline");
        document.save(outputFile.toString());
    }
}
```
