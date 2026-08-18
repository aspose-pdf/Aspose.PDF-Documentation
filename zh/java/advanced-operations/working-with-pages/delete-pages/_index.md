---
title: 用Java删除PDF页面
linktitle: 删除 PDF 页面
type: docs
weight: 80
url: /java/delete-pages/
description: 了解如何使用 Java 从 PDF 文件中删除页面。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 删除一页或多页 PDF
Abstract: 本文介绍如何使用 Aspose.PDF for Java 从 PDF 文件中删除页面。它包括通过页面收集 API 删除单个页面和一次删除多个页面。
---
当您需要从 PDF 中删除一页或多页时，请使用文档页面集合。

## 删除单个页面

当您需要按索引删除一页时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 从页面集合中删除目标页面。
1. 保存更新的文档。

```java
public static void deletePage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().delete(2);
        document.save(outputFile.toString());
    }
}
```

## 删除多个页面

当应在一次操作中删除多个页面时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 传递要从页面集合中删除的页面索引。
1. 保存修改后的 PDF。

```java
public static void deleteBunchPages(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().delete(new Integer[]{2, 3, 4});
        document.save(outputFile.toString());
    }
}
```
