---
title: 以编程方式保存 PDF 文档
linktitle: 保存PDF
type: docs
weight: 30
url: /java/save-pdf-document/
description: 了解如何使用 Aspose.PDF 将 Java 中的 PDF 文档保存到文件、流或保存为 PDF 标准。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 中的 Aspose.PDF 库保存 PDF 文档
Abstract: This article describes how to save PDF documents in Java using Aspose.PDF.它涵盖保存到文件路径、保存到 OutputStream 以及在将文档保存为 PDF/X 标准文件之前转换文档。
---
Aspose.PDF for Java 提供了多种保存文档的方法，具体取决于目标目的地和输出要求。

## 用 Java 保存 PDF 文档

您可以保存文档：

1. 将[文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 直接保存到磁盘上的文件中。
1. 将[文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)保存到`OutputStream`。
1. 使用 [PdfFormatConversionOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformatconversionoptions/) 转换 [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并将其保存为标准格式，例如 [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/)。

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

## 将文档另存为 PDF/X

```java
public static void saveDocumentAsStandard(Path inputFile, Path outputFile) {
    Document document = new Document(inputFile.toString());
    document.getPages().add();
    document.convert(new PdfFormatConversionOptions(PdfFormat.PDF_X_3));
    document.save(outputFile.toString());
    document.close();
}
```
