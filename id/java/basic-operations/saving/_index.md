---
title: "Menyimpan dokumen PDF secara programatik"
linktitle: "Menyimpan PDF"
type: docs
weight: 30
url: /id/java/save-pdf-document/
description: Pelajari cara menyimpan dokumen PDF dalam Java ke file, ke stream, atau sebagai standar PDF menggunakan Aspose.PDF.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Menyimpan dokumen PDF menggunakan pustaka Aspose.PDF dalam Java"
Abstract: Artikel ini menjelaskan cara menyimpan dokumen PDF di Java menggunakan Aspose.PDF. Artikel ini mencakup penyimpanan ke jalur file, penyimpanan ke OutputStream, dan mengonversi dokumen sebelum menyimpannya sebagai file standar PDF/X.
---
Aspose.PDF for Java menyediakan beberapa cara untuk menyimpan dokumen tergantung pada tujuan target dan persyaratan output.

## Menyimpan dokumen PDF di Java

Anda dapat menyimpan dokumen:

1. Simpan [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) langsung ke file di disk.
1. Simpan [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) ke sebuah `OutputStream`.
1. Konversi [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dengan [`PdfFormatConversionOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformatconversionoptions/) dan simpan dalam format standar seperti [`PdfFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/).

## Menyimpan dokumen ke file

```java
public static void saveDocumentToFile(Path inputFile, Path outputFile) {
    Document document = new Document(inputFile.toString());
    document.getPages().add();
    document.save(outputFile.toString());
    document.close();
}
```

## Menyimpan dokumen ke aliran

```java
public static void saveDocumentToStream(Path inputFile, Path outputFile) throws Exception {
    Document document = new Document(inputFile.toString());
    document.getPages().add();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        document.save(stream);
    } finally {
        document.close();
    }
}
```

## Menyimpan dokumen sebagai PDF/X

```java
public static void saveDocumentAsStandard(Path inputFile, Path outputFile) {
    Document document = new Document(inputFile.toString());
    document.getPages().add();
    document.convert(new PdfFormatConversionOptions(PdfFormat.PDF_X_3));
    document.save(outputFile.toString());
    document.close();
}
```
