---
title: "Mengubah ukuran halaman PDF dalam Java"
linktitle: "Mengubah ukuran halaman"
type: docs
weight: 40
url: /id/java/change-page-size/
description: Pelajari cara membaca dan mengubah dimensi halaman PDF dalam Java.
lastmod: "2026-09-30"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Membaca dan memperbarui dimensi halaman serta kotak dengan Java"
Abstract: Artikel ini menunjukkan cara membaca dan memodifikasi dimensi halaman PDF menggunakan Aspose.PDF for Java. Ini mencakup mendapatkan ukuran halaman, mengukur ukuran halaman dengan rotasi yang diterapkan, dan memperbarui halaman pertama ke ukuran baru sambil mencetak dimensi kotak sebelum dan sesudah perubahan.
---
Aspose.PDF for Java dapat melaporkan dimensi halaman dan memperbaruinya.

## Mengubah ukuran halaman

Gunakan contoh ini ketika Anda perlu mengubah ukuran halaman yang ada dan memeriksa kotak halaman sebelum dan sesudah perubahan.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Dapatkan [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) target dan cetak nilai kotak saat ini.
1. Atur ukuran halaman baru dan simpan dokumen.

```java
public static void setPageSize(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        printBoxes("Before set", page);
        page.setPageSize(597.6, 842.4);
        printBoxes("After set", page);
        document.save(outputFile.toString());
    }
}
```

## Mendapatkan ukuran halaman

Gunakan contoh ini ketika Anda perlu membaca dimensi terlihat dari sebuah halaman.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Dapatkan persegi panjang halaman dengan penanganan rotasi diaktifkan.
1. Keluarkan lebar dan tinggi halaman.

```java
public static void getPageSize(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Rectangle rectangle = document.getPages().get_Item(1).getPageRect(true);
        System.out.println(rectangle.getWidth() + " : " + rectangle.getHeight());
    }
}
```

## Mendapatkan ukuran halaman dengan rotasi yang diterapkan

Gunakan contoh ini ketika Anda perlu membandingkan dimensi halaman sebelum dan sesudah memperhitungkan rotasi.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Putar [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) target.
1. Baca persegi panjang halaman dengan dan tanpa penanganan rotasi serta keluarkan kedua nilai tersebut.

```java
public static void getPageSizeRotation(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        page.setRotate(Rotation.on90);
        Rectangle rectangle = page.getPageRect(false);
        System.out.println(rectangle.getWidth() + " : " + rectangle.getHeight());
        rectangle = page.getPageRect(true);
        System.out.println(rectangle.getWidth() + " : " + rectangle.getHeight());
    }
}
```
