---
title: 在 Java 中移动 PDF 页面
linktitle: 移动 PDF 页面
type: docs
weight: 100
url: /zh/java/move-pages/
description: 了解如何在 Java 中在文档内部或文档之间移动 PDF 页面。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Java 中在文档之间移动 PDF 页面
Abstract: 本文介绍了如何使用 Aspose.PDF for Java 在 PDF 中移动页面。它涵盖了将单页或多页移动到另一个文档，以及在同一 PDF 内重新定位页面。
---
Aspose.PDF for Java 允许您在文档之间移动页面或在同一 PDF 内重新定位页面。

## 将页面移动到另一个文档

当需要将单页从源 PDF 中删除并保存到单独的文档时，请使用此示例。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并创建目标文档。
1. 将目标页面添加到目标文档中，并从源文档中删除它。
1. 保存两个文档。

```java
public static void movePageFromOneDocumentToAnother(Path inputFile, Path sourceOutputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString());
         Document anotherDocument = new Document()) {
        anotherDocument.getPages().add(document.getPages().get_Item(2));
        document.getPages().delete(2);
        document.save(sourceOutputFile.toString());
        anotherDocument.save(outputFile.toString());
    }
}
```

## 将多个页面移动到另一个文档

当需要将多个页面从源 PDF 转移到新文档时，请使用此示例。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并创建目标文档。
1. 将选定的页面复制到目标文档中。
1. 从源文档中删除已移动的页面，并保存两个文件。

```java
public static void moveBunchPagesFromOneDocumentToAnother(Path inputFile, Path sourceOutputFile, Path outputFile) {
    try (Document srcDocument = new Document(inputFile.toString());
         Document dstDocument = new Document()) {
        Integer[] pages = {1, 2};
        for (Integer pageIndex : pages) {
            dstDocument.getPages().add(srcDocument.getPages().get_Item(pageIndex));
        }
        dstDocument.save(outputFile.toString());
        srcDocument.getPages().delete(pages);
        srcDocument.save(sourceOutputFile.toString());
    }
}
```

## 在同一个文档中移动页面

当需要将页面重新定位到同一 PDF 中的新位置时，请使用此示例。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 将目标页面复制到新位置并删除原始页面条目。
1. 保存重新排序的文档。

```java
public static void movePageInNewLocationInSameDocument(Path inputFile, Path outputFile) {
    try (Document srcDocument = new Document(inputFile.toString())) {
        srcDocument.getPages().add(srcDocument.getPages().get_Item(2));
        srcDocument.getPages().delete(2);
        srcDocument.save(outputFile.toString());
    }
}
```
