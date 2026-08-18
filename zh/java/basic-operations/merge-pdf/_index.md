---
title: 在 Java 中合并 PDF 文件
linktitle: 合并 PDF 文件
type: docs
weight: 50
url: /java/merge-pdf/
description: Learn how to merge multiple PDF files into a single document in Java using Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 合并 PDF 页面
Abstract: 本文介绍如何使用 Aspose.PDF 在 Java 中合并两个 PDF 文档。该示例打开两个源文档，将第二个文档的页面附加到第一个文档的页面，并将合并结果保存为新的 PDF 文件。
---
当您需要将相关文档合并为单个文件以进行分发、存档或处理时，合并 PDF 文件非常有用。

## 实例

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) 是一个免费的在线应用程序，用于在浏览器中测试 PDF 合并。

本主题演示如何使用 Java 将多个 PDF 文件合并为单个文档：

1. 使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 构造函数打开两个源文档。
1. 使用 `document1.getPages().add(document2.getPages())` 将第二个 [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 中的 [页面](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 集合追加到第一个集合。
1. 将合并后的[文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)保存到输出路径。

## 合并两个 PDF 文档

以下 Java 示例基于 `MergeDocumentExamples.java`。

```java
public static void mergeTwoDocuments(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        document1.getPages().add(document2.getPages());
        document1.save(outputFile.toString());
    }
}
```
