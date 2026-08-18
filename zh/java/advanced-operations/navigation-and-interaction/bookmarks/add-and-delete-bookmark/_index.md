---
title: 在 Java 中添加和删除 PDF 书签
linktitle: 添加和删​​除书签
type: docs
weight: 10
url: /java/add-and-delete-bookmark/
description: 了解如何使用 Java 在 PDF 文档中添加和删除书签。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 在 PDF 文档中添加或删除书签
Abstract: 本文介绍如何使用 Aspose.PDF for Java 创建和删除书签。这些示例演示了添加顶级书签、创建子书签层次结构、删除所有书签以及按标题删除特定书签。
---
使用文档大纲集合以编程方式管理书签。

## 添加顶级书签

当文档应包含单个顶级大纲条目时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 创建一个 [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/outlineitemcollection/) 并配置其标题、样式和操作。
1. 将书签添加到文档大纲并保存文件。

```java
public static void addBookmark(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        OutlineItemCollection pdfOutline = new OutlineItemCollection(document.getOutlines());
        pdfOutline.setTitle("Test Outline");
        pdfOutline.setItalic(true);
        pdfOutline.setBold(true);
        pdfOutline.setAction(new GoToAction(document.getPages().get_Item(1)));

        document.getOutlines().add(pdfOutline);
        document.save(outputFile.toString());
    }
}
```

## 添加子书签

此示例创建一个父书签并在其下嵌套一个子书签。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 创建父和子 [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/outlineitemcollection/) 对象。
1. 将子级添加到父级，将父级添加到大纲集合，然后保存文档。

```java
public static void addChildBookmark(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        OutlineItemCollection pdfOutline = new OutlineItemCollection(document.getOutlines());
        pdfOutline.setTitle("Parent Outline");
        pdfOutline.setItalic(true);
        pdfOutline.setBold(true);

        OutlineItemCollection pdfChildOutline = new OutlineItemCollection(document.getOutlines());
        pdfChildOutline.setTitle("Child Outline");
        pdfChildOutline.setItalic(true);
        pdfChildOutline.setBold(true);

        pdfOutline.add(pdfChildOutline);
        document.getOutlines().add(pdfOutline);
        document.save(outputFile.toString());
    }
}
```

## 删除所有书签

当应从文档中删除整个大纲集合时，请使用此方法。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 删除完整的轮廓集合。
1. 保存清理后的输出文件。

```java
public static void deleteBookmarks(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getOutlines().delete();
        document.save(outputFile.toString());
    }
}
```

## 删除特定书签

当应删除一个命名书签而不清除整个大纲树时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 从大纲集合中按标题删除书签。
1. 保存更新的文档。

```java
public static void deleteBookmark(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getOutlines().delete("Child Outline");
        document.save(outputFile.toString());
    }
}
```
