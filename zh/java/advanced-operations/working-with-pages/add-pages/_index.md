---
title: 在 Java 中添加 PDF 页面
linktitle: 添加页面
type: docs
weight: 10
url: /zh/java/add-pages/
description: 了解如何在 Java 中向 PDF 文档添加或插入页面。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 添加或插入 PDF 页面
Abstract: 本文介绍了如何使用 Aspose.PDF for Java 向 PDF 文件添加页面。内容包括在特定位置插入空白页、在文档末尾追加页面以及从其他 PDF 导入页面。
---
Aspose.PDF for Java 让您可以插入空白页或从其他文档导入页面。

## 在特定位置插入空白页

当您需要在现有 PDF 的中间添加空白页时，请使用此示例。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 在页面集合中将新页面插入目标位置。
1. 保存更新后的文档。

```java
public static void insertEmptyPage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().insert(2);
        document.save(outputFile.toString());
    }
}
```

## 在末尾追加一个空白页

当您需要在文档末尾添加一个新的空白页时，请使用此示例。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 向页面集合的末尾添加一个新页面。
1. 保存修改后的 PDF。

```java
public static void addEmptyPageToEnd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().add();
        document.save(outputFile.toString());
    }
}
```

## 从另一个文档添加页面

当您想将一个 PDF 的页面导入到另一个 PDF 时，请使用此示例。

1. 创建目标 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并打开源文档。
1. 添加任何所需的目标内容，并从源 PDF 导入目标页面。
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
