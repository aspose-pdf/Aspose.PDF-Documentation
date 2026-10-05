---
title: "Menambahkan halaman PDF dalam Java"
linktitle: "Menambahkan halaman"
type: docs
weight: 10
url: /id/java/add-pages/
description: Pelajari cara menambahkan atau menyisipkan halaman ke dalam dokumen PDF menggunakan Java.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Menambahkan atau menyisipkan halaman PDF dengan Java"
Abstract: Artikel ini menjelaskan cara menambahkan halaman ke file PDF menggunakan Aspose.PDF for Java. Artikel ini mencakup penyisipan halaman kosong pada posisi tertentu, menambahkan halaman di akhir dokumen, dan mengimpor halaman dari PDF lain.
---
Aspose.PDF for Java memungkinkan Anda menyisipkan halaman kosong atau mengimpor halaman dari dokumen lain.

## Menyisipkan halaman kosong pada posisi tertentu

Gunakan contoh ini ketika Anda perlu menambahkan halaman kosong di tengah PDF yang sudah ada.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Masukkan halaman baru ke posisi target dalam koleksi halaman.
1. Simpan dokumen yang diperbarui.

```java
public static void insertEmptyPage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().insert(2);
        document.save(outputFile.toString());
    }
}
```

## Menambahkan halaman kosong di akhir

Gunakan contoh ini ketika Anda perlu memperluas dokumen dengan halaman terakhir yang kosong baru.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Tambahkan halaman baru ke akhir koleksi halaman.
1. Simpan PDF yang dimodifikasi.

```java
public static void addEmptyPageToEnd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().add();
        document.save(outputFile.toString());
    }
}
```

## Menambahkan halaman dari dokumen lain

Gunakan contoh ini ketika Anda ingin mengimpor halaman dari satu PDF ke PDF lain.

1. Buat tujuan [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan buka dokumen sumber.
1. Tambahkan konten tujuan yang diperlukan dan impor halaman target dari PDF sumber.
1. Simpan dokumen yang dihasilkan.

```java
public static void addPageFromAnotherDocument(Path inputFile, Path outputFile) {
    try (Document document = new Document();
         Document anotherDocument = new Document(inputFile.toString())) {
        document.getPages().add().getParagraphs().add(new TextFragment("This is first page!"));
        document.getPages().add(anotherDocument.getPages().get_Item(1));
        document.save(outputFile.toString());
    }
}
```
