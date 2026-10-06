---
title: 以编程方式保存 PDF 文档
linktitle: 保存 PDF
type: docs
weight: 30
url: /zh/java/save-pdf-document/
description: 了解如何使用 Aspose.PDF 在 Java 中将 PDF 文档保存到文件、流或作为 PDF 标准。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Java 中使用 Aspose.PDF 库保存 PDF 文档
Abstract: 本文描述了如何在 Java 中使用 Aspose.PDF 保存 PDF 文档。它涵盖了保存到文件路径、保存到 OutputStream，以及在保存为 PDF/X 标准文件之前转换文档的过程。
---
Aspose.PDF for Java 提供了多种保存文档的方式，取决于目标位置和输出需求。

## 在 Java 中保存 PDF 文档

您可以保存文档：

1. 保存 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 直接保存到磁盘上的文件。
1. 保存 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 到一个 `OutputStream`.
1. 转换 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 使用 [PdfFormatConversionOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformatconversionoptions/) 并将其保存为标准格式，例如 [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/).

## 将文档保存到文件

```java
public static void saveDocumentToFile(Path inputFile, Path outputFile) {
    Document document = new Document(inputFile.toString());
    document.getPages().add();
    document.save(outputFile.toString());
    document.close();
}
```

## 将文档保存到流

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

## 将文档保存为 PDF/X

```java
public static void saveDocumentAsStandard(Path inputFile, Path outputFile) {
    Document document = new Document(inputFile.toString());
    document.getPages().add();
    document.convert(new PdfFormatConversionOptions(PdfFormat.PDF_X_3));
    document.save(outputFile.toString());
    document.close();
}
```
