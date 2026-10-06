---
title: 在 Java 中删除 PDF 页面
linktitle: 删除 PDF 页面
type: docs
weight: 80
url: /zh/java/delete-pages/
description: 了解如何在 Java 中从 PDF 文件删除页面。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Java 中删除一个或多个 PDF 页面
Abstract: 本文解释了如何使用 Aspose.PDF for Java 从 PDF 文件中删除页面。它涵盖了通过页面集合 API 删除单个页面以及一次删除多个页面。
---
当需要从 PDF 中删除一个或多个页面时，请使用文档页面集合。

## 删除单个页面

当需要通过索引删除单页时，请使用此示例。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 从页面集合中删除目标页面。
1. 保存更新后的文档。

```java
public static void deletePage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().delete(2);
        document.save(outputFile.toString());
    }
}
```

## 删除多个页面

当需要一次性删除多个页面时，请使用此示例。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 将要删除的页面索引传递给页面集合。
1. 保存已修改的 PDF。

```java
public static void deleteBunchPages(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().delete(new Integer[]{2, 3, 4});
        document.save(outputFile.toString());
    }
}
```
