---
title: 在 Java 中添加 PDF 页面
linktitle: 添加页面
type: docs
weight: 10
url: /java/add-pages/
description: 了解如何使用 Java 在 PDF 文档中添加或插入页面。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 添加或插入 PDF 页面
Abstract: 本文介绍如何使用 Aspose.PDF for Java 将页面添加到 PDF 文件。它包括在特定位置插入空白页面、在文档末尾附加页面以及从另一个 PDF 导入页面。
---
Aspose.PDF for Java 允许您插入空白页面或从其他文档导入页面。

## 在特定位置插入空白页

当您需要在现有 PDF 中间添加空白页面时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 将新页面插入页面集合中的目标位置。
1. 保存更新的文档。

```java
public static void insertEmptyPage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().insert(2);
        document.save(outputFile.toString());
    }
}
```

## 在末尾附加一个空页

当您需要使用新的空白最后一页来扩展文档时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 将新页面添加到页面集合的末尾。
1. 保存修改后的 PDF。

```java
public static void addEmptyPageToEnd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().add();
        document.save(outputFile.toString());
    }
}
```

## 添加另一个文档中的页面

当您想要将一个 PDF 中的页面导入到另一个 PDF 中时，请使用此示例。

1. 创建目标[文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并打开源文档。
1. 添加任何所需的目标内容并从源 PDF 导入目标页面。
1. 保存生成的文档。

```java
public static void addPageFromAnotherDocument(Path inputFile, Path outputFile) {
    try (Document document = new Document();
         Document anotherDocument = new Document(inputFile.toString())) {
        document.getPages().add().getParagraphs().add(new TextFragment("This is first page!"));
        document.getPages().add(anotherDocument.getPages().get_Item(1));
        document.save(outputFile.toString());
    }
}
```
