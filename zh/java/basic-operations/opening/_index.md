---
title: 以编程方式打开 PDF 文档
linktitle: 打开 PDF
type: docs
weight: 20
url: /java/open-pdf-document/
description: 了解如何使用 Aspose.PDF 从文件路径、流或使用密码在 Java 中打开 PDF 文件。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 中的 Aspose.PDF 库打开 PDF 文档
Abstract: 本文介绍如何使用 Aspose.PDF 在 Java 中打开现有 PDF 文档。它涵盖了按文件路径打开 PDF、从 InputStream 打开 PDF 以及打开受密码保护的文档，每个示例都从加载的文档中读取页数。
---
Aspose.PDF for Java 支持多种加载现有 PDF 文档的方法，具体取决于源数据的来源。

## 用 Java 打开 PDF 文档

您可以打开 PDF 文档：

1. 直接从文件路径打开[文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 从`InputStream` 打开[文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 通过提供密码打开加密的[文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

## 从文件中打开文档

```java
public static void openDocumentFromFile(Path inputFile) {
    Document document = new Document(inputFile.toString());
    System.out.println("Pages: " + document.getPages().size());
    document.close();
}
```

## 从流中打开文档

```java
public static void openDocumentFromStream(Path inputFile) throws Exception {
    try (InputStream stream = Files.newInputStream(inputFile)) {
        Document document = new Document(stream);
        System.out.println("Pages: " + document.getPages().size());
        document.close();
    }
}
```

## 打开加密文档

```java
public static void openDocumentEncrypted(Path inputFile) {
    Document document = new Document(inputFile.toString(), "P@ssw0rd");
    System.out.println("Pages: " + document.getPages().size());
    document.close();
}
```
