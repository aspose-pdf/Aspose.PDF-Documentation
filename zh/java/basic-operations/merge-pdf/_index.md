---
title: 在 Java 中合并 PDF 文件
linktitle: 合并 PDF 文件
type: docs
weight: 50
url: /zh/java/merge-pdf/
description: 了解如何在 Java 中使用 Aspose.PDF 将多个 PDF 文件合并为单个文档。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 合并 PDF 页面
Abstract: 本文说明了如何在 Java 中使用 Aspose.PDF 合并两个 PDF 文档。示例打开两个源文档，将第二个文档的页面附加到第一个文档，并将合并后的结果保存为新的 PDF 文件。
---
合并 PDF 文件在需要将相关文档合并为单个文件以进行分发、归档或处理时非常有用。

## 实时示例

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) 是一个免费在线应用程序，可在浏览器中测试 PDF 合并。

本主题展示了如何在 Java 中将多个 PDF 文件合并为一个文档：

1. 使用以下方式打开两个源文档 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 构造函数。
1. 追加 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 来自第二个的集合 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 到第一个具有 `document1.getPages().add(document2.getPages())`.
1. 保存合并的 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 到输出路径。

## 合并两个 PDF 文档

以下 Java 示例基于 `MergeDocumentExamples.java`.

```java
public static void mergeTwoDocuments(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        document1.getPages().add(document2.getPages());
        document1.save(outputFile.toString());
    }
}
```
