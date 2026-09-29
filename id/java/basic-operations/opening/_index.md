---
title: Buka dokumen PDF secara programatik
linktitle: Buka PDF
type: docs
weight: 20
url: /id/java/open-pdf-document/
description: Pelajari cara membuka file PDF di Java menggunakan Aspose.PDF dari jalur file, aliran, atau dengan kata sandi.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Membuka dokumen PDF menggunakan pustaka Aspose.PDF di Java
Abstract: Artikel ini menunjukkan cara membuka dokumen PDF yang ada di Java menggunakan Aspose.PDF. Ini mencakup membuka PDF berdasarkan jalur file, membuka PDF dari InputStream, dan membuka dokumen yang dilindungi kata sandi, dengan setiap contoh membaca jumlah halaman dari dokumen yang dimuat.
---
Aspose.PDF for Java mendukung beberapa cara untuk memuat dokumen PDF yang ada tergantung dari sumber data asal.

## Buka dokumen PDF di Java

Anda dapat membuka dokumen PDF:

1. Buka sebuah [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) langsung dari jalur file.
1. Buka sebuah [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dari sebuah `InputStream`.
1. Buka yang terenkripsi [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dengan memberikan kata sandi.

## Buka dokumen dari file

```java
public static void openDocumentFromFile(Path inputFile) {
    Document document = new Document(inputFile.toString());
    System.out.println("Pages: " + document.getPages().size());
    document.close();
}
```

## Buka dokumen dari aliran

```java
public static void openDocumentFromStream(Path inputFile) throws Exception {
    try (InputStream stream = Files.newInputStream(inputFile)) {
        Document document = new Document(stream);
        System.out.println("Pages: " + document.getPages().size());
        document.close();
    }
}
```

## Buka dokumen terenkripsi

```java
public static void openDocumentEncrypted(Path inputFile) {
    Document document = new Document(inputFile.toString(), "P@ssw0rd");
    System.out.println("Pages: " + document.getPages().size());
    document.close();
}
```
