---
title: 在 Java 中拆分 PDF 文件
linktitle: 拆分 PDF 文件
type: docs
weight: 60
url: /zh/java/split-pdf/
description: 了解如何使用 Aspose.PDF 在 Java 中将 PDF 拆分为单页 PDF 文件。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 拆分 PDF 页面
Abstract: 本文展示了如何使用 Aspose.PDF 在 Java 中将 PDF 文档拆分为单独的单页 PDF 文件。示例打开源文档，遍历其页面，为每一页创建一个新文档，并将每页保存为单独的 PDF 文件。
---
将 PDF 拆分为多个文件在您需要导出每页进行审阅、存储或后续处理时非常有用。

## 实时示例

[Aspose.PDF 拆分器](https://products.aspose.app/pdf/splitter) 是一款免费的在线应用程序，用于在浏览器中测试 PDF 拆分。

[![Aspose 拆分 PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

此示例使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 类用于打开 PDF 文件并遍历其页面。对于每个 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)，它会创建一个新文档，将该页面添加进去，并将结果保存为单独的 PDF 文件。

在 Java 中将 PDF 拆分为单独页面文件：

1. 使用以下方式打开源 PDF： [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 构造函数。
1. 遍历 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 返回的对象 `document.getPages()`。
1. 创建一个新的空 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 对每个页面。
1. 添加当前的 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 到新的 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 保存新的 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 使用唯一的文件名。
1. 关闭两个 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 对象处理完成后。

## 将 PDF 拆分为单页文件

以下 Java 示例基于 `SplitDocumentExamples.java` 并将页面保存为 `Page_1.pdf`, `Page_2.pdf`，等等。

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
