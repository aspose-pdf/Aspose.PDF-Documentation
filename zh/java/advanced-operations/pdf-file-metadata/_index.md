---
title: 在 Java 中处理 PDF 文件元数据
linktitle: PDF 文件元数据
type: docs
weight: 200
url: /zh/java/pdf-file-metadata/
description: 了解如何使用 Aspose.PDF 在 Java 中提取、更新和管理 PDF 文件元数据、文档信息以及 XMP 属性。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Java 中获取和设置 PDF 文档信息及 XMP 元数据
Abstract: 本文解释了如何使用 Aspose.PDF for Java 处理 PDF 元数据。了解如何读取文档信息，如作者、标题和关键字，更新文件属性，检查 PDF 版本和权限，设置 XMP 元数据字段，以及通过 DOM 和 facade API 保存元数据。
---
Aspose.PDF for Java 提供了两种主要的元数据处理方式：

- 通过 DOM API `Document`, `DocumentInfo`，以及 `document.getMetadata()`.
- 通过外观 API `PdfFileInfo`.

## 获取 PDF 文件信息

当您需要读取作者、标题、主题或关键字等标准文档信息字段时，请使用此示例。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
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

当需要通过使用已注册的命名空间前缀来添加或更新 XMP 属性时，请使用此示例。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 注册所需的 XMP 命名空间并添加元数据项。
1. 保存已更新的文档。

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

当您想要写入标准 PDF 文件属性（如作者、标题、生成者或创建日期）时，请使用此示例。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 访问 [DocumentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/documentinfo/) 并分配新的元数据值。
1. 保存文档以更新的文件信息。

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

当您需要存储额外的 XMP 条目（包括自定义元数据值）时，请使用此示例。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 通过添加所需的 XMP 元数据项 `document.getMetadata()`.
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
