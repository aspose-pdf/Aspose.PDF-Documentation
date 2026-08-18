---
title: 用 Java 分割 PDF 文件
linktitle: 分割 PDF 文件
type: docs
weight: 60
url: /java/split-pdf/
description: 了解如何使用 Aspose.PDF 在 Java 中将 PDF 拆分为单页 PDF 文件。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 拆分 PDF 页面
Abstract: 本文介绍如何使用 Aspose.PDF 在 Java 中将 PDF 文档拆分为单独的单页 PDF 文件。该示例打开源文档，迭代其页面，为每个页面创建一个新文档，并将每个页面保存为单独的 PDF 文件。
---
当您需要导出每个页面以供审阅、存储或下游处理时，将 PDF 拆分为单独的文件非常有用。

## 实例

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) 是一个免费的在线应用程序，用于在浏览器中测试 PDF 拆分。

[![提出分割 PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

此示例使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 类打开 PDF 文件并迭代其页面。对于每个[页面](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)，它都会创建一个新文档，向其中添加页面，并将结果保存为单独的 PDF 文件。

在 Java 中将 PDF 拆分为单独的页面文件：

1. 使用 [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 构造函数打开源 PDF。
1. 迭代`document.getPages()`返回的[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)对象。
1. 为每个页面创建一个新的空[文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 将当前[页面](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 添加到新的[文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 使用唯一的文件名保存新的[文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 处理完成后，关闭两个 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 对象。

## 将 PDF 拆分为单页文件

以下 Java 示例基于`SplitDocumentExamples.java`，并将页面保存为`Page_1.pdf`、`Page_2.pdf` 等。

```java
public static void splitDocument(Path inputFile, Path outputDir) {
    Document document = new Document(inputFile.toString());
    try {
        int pageCount = 1;
        for (Page page : document.getPages()) {
            Document newDocument = new Document();
            try {
                newDocument.getPages().add(page);
                newDocument.save(outputDir.resolve("Page_" + pageCount + ".pdf").toString());
            } finally {
                newDocument.close();
            }
            pageCount++;
        }
    } finally {
        document.close();
    }
}
```
