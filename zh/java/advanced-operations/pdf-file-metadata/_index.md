---
title: 在 Java 中处理 PDF 文件元数据
linktitle: PDF 文件元数据
type: docs
weight: 200
url: /java/pdf-file-metadata/
description: 了解如何使用 Aspose.PDF 在 Java 中提取、更新和管理 PDF 文件元数据、文档信息和 XMP 属性。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在Java中获取和设置PDF文档信息和XMP元数据
Abstract: 本文介绍如何使用 Aspose.PDF for Java 处理 PDF 元数据。了解如何读取文档信息（例如作者、标题和关键字）、更新文件属性、检查 PDF 版本和权限、设置 XMP 元数据字段以及通过 DOM 和 Facade API 保存元数据。
---
Aspose.PDF for Java 提供了两种处理元数据的主要方法：

- 通过`Document`、`DocumentInfo` 和`document.getMetadata()` 的 DOM API。
- 通过 `PdfFileInfo` 的门面 API。

## 获取PDF文件信息

当您需要阅读标准文档信息字段（例如作者、标题、主题或关键字）时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 访问 [DocumentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/documentinfo/) 对象。
1. 读取所需的元数据字段并输出它们的值。

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

## 使用命名空间前缀设置元数据

当您需要使用注册的命名空间前缀添加或更新 XMP 属性时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 注册所需的 XMP 命名空间并添加元数据项。
1. 保存更新的文档。

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

## 更新文档信息字段

当您想要写入标准 PDF 文件属性（例如作者、标题、制作人或创建日期）时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 访问 [DocumentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/documentinfo/) 并分配新的元数据值。
1. 使用更新的文件信息保存文档。

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

## 设置 XMP 元数据属性

当您需要存储其他 XMP 条目（包括自定义元数据值）时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 通过`document.getMetadata()`添加所需的XMP元数据项。
1. 保存输出文件。

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
