---
title: 在 Java 中获取、更新和展开 PDF 书签
linktitle: 获取、更新和展开书签
type: docs
weight: 20
url: /java/get-update-and-expand-bookmark/
description: 了解如何使用 Java 检索、更新和扩展 PDF 文档中的书签。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 检查书签属性并扩展 PDF 文件中的轮廓
Abstract: 本文介绍如何使用 Aspose.PDF for Java 读取、更新和展开书签。它包括迭代大纲项目、使用 PdfBookmarkEditor 提取书签页码、读取子书签、更新书签标题和样式以及在显示文档时强制打开大纲。
---
Aspose.PDF for Java 通过文档大纲模型和`PdfBookmarkEditor` 外观公开书签。

## 获取书签属性

当您需要检查文档大纲中的顶级书签条目时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 遍历轮廓集合。
1. 读取并打印书签标题、样式和颜色值。

```java
public static void getBookmarks(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getOutlines().size(); i++) {
            OutlineItemCollection outlineItem = document.getOutlines().get_Item(i);
            System.out.println(outlineItem.getTitle());
            System.out.println(outlineItem.getItalic());
            System.out.println(outlineItem.getBold());
            System.out.println(outlineItem.getColor());
        }
    }
}
```

## 获取书签页码

此示例使用 `PdfBookmarkEditor` 提取书签标题、级别、页码和操作。

1. 将源 PDF 绑定到 [PdfBookmarkEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdfbookmarkeditor/)。
1. 提取书签集合并迭代它。
1. 打印每个书签的级别、标题、页码和操作信息。

```java
public static void getBookmarkPageNumber(Path inputFile) {
    PdfBookmarkEditor bookmarkEditor = new PdfBookmarkEditor();
    try {
        bookmarkEditor.bindPdf(inputFile.toString());
        for (Bookmark bookmark : bookmarkEditor.extractBookmarks()) {
            String levelSeparator = "";
            for (int i = 0; i < bookmark.getLevel(); i++) {
                levelSeparator += "----";
            }

            System.out.println(levelSeparator + " Title: " + bookmark.getTitle());
            System.out.println(levelSeparator + " Page Number: " + bookmark.getPageNumber());
            System.out.println(levelSeparator + " Page Action: " + bookmark.getAction());
        }
    } finally {
        bookmarkEditor.close();
    }
}
```

## 获取子书签

当您需要检查顶级和嵌套大纲项时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 迭代顶级轮廓并打印它们的属性。
1. 检测子书签，然后迭代它们并打印它们的属性。

```java
public static void getChildBookmarks(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getOutlines().size(); i++) {
            OutlineItemCollection outlineItem = document.getOutlines().get_Item(i);
            System.out.println(outlineItem.getTitle());
            System.out.println(outlineItem.getItalic());
            System.out.println(outlineItem.getBold());
            System.out.println(outlineItem.getColor());
            int count = outlineItem.size();
            if (count > 0) {
                System.out.println("Child Bookmarks");
                for (int j = 1; j <= outlineItem.size(); j++) {
                    OutlineItemCollection childOutlineItem = outlineItem.get_Item(j);
                    System.out.println(childOutlineItem.getTitle());
                    System.out.println(childOutlineItem.getItalic());
                    System.out.println(childOutlineItem.getBold());
                    System.out.println(childOutlineItem.getColor());
                }
            }
        }
    }
}
```

## 更新书签

当应修改现有书签标题和样式时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 访问目标大纲项目及其子书签。
1. 更新书签属性并保存文档。

```java
public static void updateBookmarks(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        OutlineItemCollection outline = document.getOutlines().get_Item(1);
        OutlineItemCollection childOutline = outline.get_Item(1);
        childOutline.setTitle("Updated Outline");
        childOutline.setItalic(true);
        childOutline.setBold(true);

        document.save(outputFile.toString());
    }
}
```

## 默认展开书签

当书签面板应在显示文档时打开并显示展开的大纲项目时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 将页面模式设置为使用大纲并将每个大纲项目标记为打开。
1. 保存更新的文档。

```java
public static void expandedBookmarks(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.setPageMode(PageMode.UseOutlines);
        for (int i = 1; i <= document.getOutlines().size(); i++) {
            OutlineItemCollection item = document.getOutlines().get_Item(i);
            item.setOpen(true);
        }
        document.save(outputFile.toString());
    }
}
```
