---
title: 使用 Java 基于文本的注释
linktitle: 文本注释
type: docs
weight: 10
url: /java/pdfannotationeditor-class/text-based-annotations/
description: Learn how to add, inspect, and delete text, free text, and strikeout annotations in PDF documents using Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: 在 Java 中处理文本 PDF 注释
Abstract: 本文介绍如何使用 Java 创建、读取和删除 PDF 文档中基于文本的注释。它涵盖了基于 Java 示例实现的文本注释、自由文本注释和删除线注释。
---
## 添加文字注释

1. 打开输入 PDF 并定位应放置文本注释的页面。
2. 创建`TextAnnotation`，定义其矩形，并设置其标题、主题、标志和颜色。
3. 将注释添加到页面并保存更新的文档。

```java
public static void textAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextAnnotation textAnnotation = new TextAnnotation(
                document.getPages().get_Item(1), new Rectangle(299.988, 613.664, 428.708, 680.769, true));
        textAnnotation.setTitle("Aspose User");
        textAnnotation.setSubject("Inserted text 1");
        textAnnotation.setFlags(AnnotationFlags.Print);
        textAnnotation.setColor(Color.getBlue());

        document.getPages().get_Item(1).getAnnotations().add(textAnnotation, false);
        document.save(outputFile.toString());
    }
}
```

## 添加自由文本注释

1. 加载源 PDF 并选择自由文本注释的目标页面和矩形。
2. 创建`FreeTextAnnotation`，初始化其默认外观，并设置标题和颜色。
3. 将注释添加到页面并保存结果。

```java
public static void freeTextAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        FreeTextAnnotation freeTextAnnotation = new FreeTextAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(299, 713, 308, 720, true),
                new DefaultAppearance());
        freeTextAnnotation.setTitle("Aspose User");
        freeTextAnnotation.setColor(Color.getLightGreen());

        document.getPages().get_Item(1).getAnnotations().add(freeTextAnnotation);
        document.save(outputFile.toString());
    }
}
```
