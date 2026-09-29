---
title: Bekerja dengan Metadata File PDF dalam Java
linktitle: Metadata File PDF
type: docs
weight: 200
url: /id/java/pdf-file-metadata/
description: Pelajari cara mengekstrak, memperbarui, dan mengelola metadata file PDF, informasi dokumen, dan properti XMP dalam Java menggunakan Aspose.PDF.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dapatkan dan atur informasi dokumen PDF serta metadata XMP dalam Java
Abstract: Artikel ini menjelaskan cara bekerja dengan metadata PDF menggunakan Aspose.PDF for Java. Pelajari cara membaca informasi dokumen seperti penulis, judul, dan kata kunci, memperbarui properti file, memeriksa versi PDF dan hak istimewa, mengatur bidang metadata XMP, serta menyimpan metadata melalui API DOM dan facade.
---
Aspose.PDF for Java menyediakan dua cara utama untuk bekerja dengan metadata:

- API DOM melalui `Document`, `DocumentInfo`, dan `document.getMetadata()`.
- API façade melalui `PdfFileInfo`.

## Dapatkan informasi file PDF

Gunakan contoh ini ketika Anda perlu membaca bidang informasi dokumen standar seperti penulis, judul, subjek, atau kata kunci.

1. Buka PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Akses [DocumentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/documentinfo/) objek.
1. Baca bidang metadata yang diperlukan dan keluarkan nilainya.

```java
public static void getPdfFileInformation(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocumentInfo docInfo = document.getInfo();

        System.out.println("Author: " + docInfo.getAuthor());
        System.out.println("Creation Date: " + docInfo.getCreationDate());
        System.out.println("Keywords: " + docInfo.getKeywords());
        System.out.println("Modify Date: " + docInfo.getModDate());
        System.out.println("Subject: " + docInfo.getSubject());
        System.out.println("Title: " + docInfo.getTitle());
    }
}
```

## Atur metadata dengan awalan namespace

Gunakan contoh ini ketika Anda perlu menambahkan atau memperbarui properti XMP dengan menggunakan awalan namespace yang terdaftar.

1. Buka PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Daftarkan namespace XMP yang diperlukan dan tambahkan item metadata.
1. Simpan dokumen yang diperbarui.

```java
public static void setPrefixMetadata(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getMetadata().registerNamespaceUri("xmp", "http://ns.adobe.com/xap/1.0/");
        document.getMetadata().addItem("xmp:ModifyDate", OffsetDateTime.now().toString());
        document.save(outputFile.toString());
    }
    System.out.println("Prefix metadata saved to " + outputFile);
}
```

## Perbarui bidang informasi dokumen

Gunakan contoh ini ketika Anda ingin menulis properti file PDF standar seperti penulis, judul, pembuat, atau tanggal pembuatan.

1. Buka PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Akses [DocumentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/documentinfo/) dan tetapkan nilai metadata baru.
1. Simpan dokumen dengan informasi file yang diperbarui.

```java
public static void setFileInformation(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocumentInfo docInfo = document.getInfo();
        Date now = new Date();

        docInfo.setAuthor("Aspose");
        docInfo.setCreationDate(now);
        docInfo.setKeywords("Aspose.Pdf, DOM, API");
        docInfo.setModDate(now);
        docInfo.setSubject("PDF Information");
        docInfo.setTitle("Setting PDF Document Information");
        docInfo.setProducer("Custom producer");
        docInfo.setCreator("Custom creator");

        document.save(outputFile.toString());
    }
    System.out.println("File information saved to " + outputFile);
}
```

## Atur properti metadata XMP

Gunakan contoh ini ketika Anda perlu menyimpan entri XMP tambahan, termasuk nilai metadata khusus.

1. Buka PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Tambahkan item metadata XMP yang diperlukan melalui `document.getMetadata()`.
1. Simpan file output.

```java
public static void setXmpMetadata(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getMetadata().addItem("xmp:CreateDate", OffsetDateTime.now().toString());
        document.getMetadata().addItem("xmp:Nickname", "Nickname");
        document.getMetadata().addItem("xmp:CustomProperty", "Custom Value");
        document.save(outputFile.toString());
    }
    System.out.println("XMP metadata saved to " + outputFile);
}
```
