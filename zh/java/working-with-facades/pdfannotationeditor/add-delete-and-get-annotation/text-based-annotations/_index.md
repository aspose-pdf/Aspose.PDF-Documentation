---
title: 使用 Java 的基于文本的批注
linktitle: 文本批注
type: docs
weight: 10
url: /zh/java/pdfannotationeditor-class/text-based-annotations/
description: 了解如何使用 Java 在 PDF 文档中添加、检查和删除文本批注、自由文本批注和删除线批注。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 在 Java 中操作 PDF 文本批注
Abstract: 本文解释了如何使用 Java 在 PDF 文档中创建、读取和移除基于文本的批注。内容涵盖文本批注、自由文本批注和删除线批注，并基于 Java 示例实现。
---
## 添加文本批注

1. 打开输入 PDF 并定位要放置文本注释的页面。
2. 创建 `TextAnnotation`，定义其矩形，并设置其标题、主题、标志和颜色。
3. 将注释添加到页面并保存更新后的文档。

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

1. 加载源 PDF 并选择自由文本注释的目标页和矩形区域。
2. 创建 `FreeTextAnnotation`，初始化其默认外观，并设置标题和颜色。
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
