---
title: 在 Java 中移动 PDF 页面
linktitle: 移动 PDF 页面
type: docs
weight: 100
url: /java/move-pages/
description: 了解如何使用 Java 在文档内或文档之间移动 PDF 页面。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 在文档之间移动 PDF 页面
Abstract: 本文介绍如何使用 Aspose.PDF for Java 移动 PDF 中的页面。它涵盖将单个页面或多页面移动到另一个文档，以及在同一 PDF 中重新定位页面。
---
Aspose.PDF for Java 允许您在文档之间移动页面或在同一 PDF 内重新定位页面。

## 将页面移动到另一个文档

当应从源 PDF 中删除单个页面并将其保存到单独的文档中时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并创建目标文档。
1. 将目标页面添加到目标并将其从源中删除。
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

当需要将多个页面从源 PDF 传输到新文档时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并创建目标文档。
1. 将选定的页面复制到目标文档中。
1. 从源中删除移动的页面并保存这两个文件。

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

## 在同一文档中移动页面

当需要将页面重新定位到同一 PDF 中的新位置时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
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
