---
title: 用 Java 提取 PDF 页面
linktitle: 提取 PDF 页面
type: docs
weight: 80
url: /java/extract-pages/
description: 了解如何使用 Java 将单个或多个 PDF 页面提取到新文件中。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 将 PDF 页面提取到新文档中
Abstract: 本文介绍如何使用 Aspose.PDF for Java 从 PDF 文件中提取页面。它涵盖了复制单个页面以及使用基于 1 的页面索引将多个页面提取到单独的目标文档中。
---
Aspose.PDF for Java 允许您将选定的页面复制到新的目标文档中。

## 提取单个页面

当您需要将源 PDF 中的一页保存到单独的文档中时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并创建目标文档。
1. 将目标页面复制到目标页面集合中。
1. 保存新的 PDF。

```java
public static void extractPage(Path inputFile, Path outputFile) {
    try (Document srcDocument = new Document(inputFile.toString());
         Document dstDocument = new Document()) {
        dstDocument.getPages().add(srcDocument.getPages().get_Item(2));
        dstDocument.save(outputFile.toString());
    }
}
```

## 提取多个页面

当您需要将多个页面复制到单独的 PDF 中时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并创建目标文档。
1. 迭代选定的页面索引并将它们添加到目标。
1. 保存提取的页面文档。

```java
public static void extractBunchPages(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString());
         Document anotherDocument = new Document()) {
        Integer[] pages = {2, 3};
        for (Integer pageIndex : pages) {
            anotherDocument.getPages().add(document.getPages().get_Item(pageIndex));
        }
        anotherDocument.save(outputFile.toString());
    }
}
```
