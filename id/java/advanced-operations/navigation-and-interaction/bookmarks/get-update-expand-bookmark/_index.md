---
title: "Mendapatkan, memperbarui, dan memperluas penanda buku PDF di Java"
linktitle: "Mendapatkan, memperbarui, dan memperluas bookmark"
type: docs
weight: 20
url: /id/java/get-update-and-expand-bookmark/
description: Pelajari cara mengambil, memperbarui, dan memperluas bookmark dalam dokumen PDF menggunakan Java.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Memeriksa properti bookmark dan memperluas outline dalam file PDF dengan Java"
Abstract: Artikel ini menjelaskan cara membaca, memperbarui, dan memperluas bookmark menggunakan Aspose.PDF for Java. Artikel ini mencakup iterasi melalui item outline, mengekstrak nomor halaman bookmark dengan PdfBookmarkEditor, membaca bookmark anak, memperbarui judul dan gaya bookmark, serta memaksa outline terbuka saat dokumen ditampilkan.
---
Aspose.PDF for Java mengekspose bookmark melalui model outline dokumen dan fasad `PdfBookmarkEditor`.

## Mendapatkan properti bookmark

Gunakan contoh ini ketika Anda perlu memeriksa entri bookmark tingkat atas dalam outline dokumen.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterasikan melalui koleksi outline.
1. Baca dan cetak nilai judul bookmark, gaya, dan warna.

```java
public static void getBookmarks(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getOutlines().size(); i++) {
            OutlineItemCollection outlineItem = document.getOutlines().get_Item(i);
            System.out.println(outlineItem.getTitle());
            System.out.println(outlineItem.getItalic());
            System.out.println(outlineItem.getBold());
            System.out.println(outlineItem.getColor());
        }
    }
}
```

## Mendapatkan nomor halaman bookmark

Contoh ini menggunakan `PdfBookmarkEditor` untuk mengekstrak judul bookmark, level, nomor halaman, dan aksi.

1. Ikat PDF sumber ke [`PdfBookmarkEditor`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdfbookmarkeditor/).
1. Ekstrak koleksi bookmark dan iterasi melaluinya.
1. Cetak tingkat, judul, nomor halaman, dan informasi aksi untuk setiap bookmark.

```java
public static void getBookmarkPageNumber(Path inputFile) {
    PdfBookmarkEditor bookmarkEditor = new PdfBookmarkEditor();
    try {
        bookmarkEditor.bindPdf(inputFile.toString());
        for (Bookmark bookmark : bookmarkEditor.extractBookmarks()) {
            String levelSeparator = "";
            for (int i = 0; i < bookmark.getLevel(); i++) {
                levelSeparator += "----";
            }

            System.out.println(levelSeparator + " Title: " + bookmark.getTitle());
            System.out.println(levelSeparator + " Page Number: " + bookmark.getPageNumber());
            System.out.println(levelSeparator + " Page Action: " + bookmark.getAction());
        }
    } finally {
        bookmarkEditor.close();
    }
}
```

## Mendapatkan bookmark anak

Gunakan contoh ini ketika Anda perlu memeriksa item outline tingkat atas dan yang bersarang.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterasikan melalui outline tingkat atas dan cetak propertinya.
1. Deteksi bookmark anak, lalu iterasi melalui mereka dan cetak propertinya.

```java
public static void getChildBookmarks(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getOutlines().size(); i++) {
            OutlineItemCollection outlineItem = document.getOutlines().get_Item(i);
            System.out.println(outlineItem.getTitle());
            System.out.println(outlineItem.getItalic());
            System.out.println(outlineItem.getBold());
            System.out.println(outlineItem.getColor());
            int count = outlineItem.size();
            if (count > 0) {
                System.out.println("Child Bookmarks");
                for (int j = 1; j <= outlineItem.size(); j++) {
                    OutlineItemCollection childOutlineItem = outlineItem.get_Item(j);
                    System.out.println(childOutlineItem.getTitle());
                    System.out.println(childOutlineItem.getItalic());
                    System.out.println(childOutlineItem.getBold());
                    System.out.println(childOutlineItem.getColor());
                }
            }
        }
    }
}
```

## Memperbarui bookmark

Gunakan contoh ini ketika judul dan gaya bookmark yang ada harus dimodifikasi.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Akses item outline target dan bookmark anaknya.
1. Perbarui properti bookmark dan simpan dokumen.

```java
public static void updateBookmarks(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        OutlineItemCollection outline = document.getOutlines().get_Item(1);
        OutlineItemCollection childOutline = outline.get_Item(1);
        childOutline.setTitle("Updated Outline");
        childOutline.setItalic(true);
        childOutline.setBold(true);

        document.save(outputFile.toString());
    }
}
```

## Memperluas bookmark secara default

Gunakan contoh ini ketika panel bookmark harus terbuka dan menampilkan item outline yang diperluas saat dokumen ditampilkan.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Atur mode halaman untuk menggunakan outline dan tandai setiap item outline sebagai terbuka.
1. Simpan dokumen yang diperbarui.

```java
public static void expandedBookmarks(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.setPageMode(PageMode.UseOutlines);
        for (int i = 1; i <= document.getOutlines().size(); i++) {
            OutlineItemCollection item = document.getOutlines().get_Item(i);
            item.setOpen(true);
        }
        document.save(outputFile.toString());
    }
}
```
