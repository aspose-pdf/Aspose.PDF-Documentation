---
title: 以编程方式创建 PDF 文档
linktitle: 创建 PDF
type: docs
weight: 10
url: /zh/java/create-document/
description: 了解如何使用 Aspose.PDF 在 Java 中从头创建 PDF 文档。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Java 生成 PDF 文件
Abstract: 本文展示了如何使用 Aspose.PDF 在 Java 中创建 PDF 文件。示例创建了一个新的 Document 对象，添加了一页，插入了带有示例文本的 TextFragment，并将结果保存为 PDF 文件。
---
在代码中创建 PDF 文件是报告、发票和生成的业务文档的常见需求。Aspose.PDF for Java 提供了一种直接从头构建文档的方法。

## 在 Java 中创建 PDF 文件

以编程方式创建 PDF 文档：

1. 创建一个 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 对象。
1. 将一个 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 添加到文档。
1. 将一个 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) 添加到页面段落。
1. 保存 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 到输出文件。

## 创建一个简单的 PDF 文档

以下 Java 示例基于 `CreatePdfDocumentExamples.java`。

```java
public static void createNewDocument(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(new TextFragment("Hello World!"));
        document.save(outputFile.toString());
    }
}
```
