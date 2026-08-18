---
title: 使用 Java 的标记注释
linktitle: 标记注释
type: docs
weight: 20
url: /java/pdfannotationeditor-class/markup-annotations/
description: 了解如何使用 Java 在 PDF 文档中添加、检查和删除突出显示、下划线、波浪线和删除线注释。
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: 使用 Java 处理 PDF 文件中的标记注释
Abstract: 本文介绍如何使用 Java 创建、检查和删除 PDF 文档中的文本标记注释。它涵盖了基于存储库 Java 示例的突出显示、下划线、波浪线和删除线注释。
---
## 添加突出显示、下划线、波浪线或删除线注释

1. 打开输入 PDF 并选择应显示标记注释的页面区域。
2. 创建所需的注释类型并配置其元数据或视觉属性。
3. 将注释添加到页面集合并保存文档。

```java
public static void addTextHighlightAnnotation(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HighlightAnnotation highlightAnnotation = new HighlightAnnotation(
                document.getPages().get_Item(1), new Rectangle(300, 750, 320, 770, true));
        document.getPages().get_Item(1).getAnnotations().add(highlightAnnotation);
        document.save(outputFile.toString());
    }
}
```

```java
public static void addTextUnderlineAnnotation(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        UnderlineAnnotation underlineAnnotation = new UnderlineAnnotation(
                document.getPages().get_Item(1), new Rectangle(299.988, 713.664, 308.708, 720.769, true));
        underlineAnnotation.setTitle("Aspose User");
        underlineAnnotation.setSubject("Inserted Underline 1");
        underlineAnnotation.setFlags(AnnotationFlags.Print);
        underlineAnnotation.setColor(Color.getBlue());
        document.getPages().get_Item(1).getAnnotations().add(underlineAnnotation);
        document.save(outputFile.toString());
    }
}
```
