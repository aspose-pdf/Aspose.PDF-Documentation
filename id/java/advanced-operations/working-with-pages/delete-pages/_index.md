---
title: Hapus Halaman PDF di Java
linktitle: Menghapus Halaman PDF
type: docs
weight: 80
url: /id/java/delete-pages/
description: Pelajari cara menghapus halaman dari file PDF di Java.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Hapus satu atau lebih halaman PDF di Java
Abstract: Artikel ini menjelaskan cara menghapus halaman dari file PDF menggunakan Aspose.PDF for Java. Artikel ini mencakup penghapusan satu halaman dan penghapusan beberapa halaman sekaligus melalui API koleksi halaman.
---
Gunakan koleksi halaman dokumen ketika Anda perlu menghapus satu atau lebih halaman dari PDF.

## Hapus satu halaman

Gunakan contoh ini ketika Anda perlu menghapus satu halaman berdasarkan indeksnya.

1. Buka PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Hapus halaman target dari koleksi halaman.
1. Simpan dokumen yang diperbarui.

```java
public static void deletePage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().delete(2);
        document.save(outputFile.toString());
    }
}
```

## Hapus beberapa halaman

Gunakan contoh ini ketika beberapa halaman harus dihapus dalam satu operasi.

1. Buka PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Berikan indeks halaman yang akan dihapus dari koleksi halaman.
1. Simpan PDF yang telah dimodifikasi.

```java
public static void deleteBunchPages(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().delete(new Integer[]{2, 3, 4});
        document.save(outputFile.toString());
    }
}
```
