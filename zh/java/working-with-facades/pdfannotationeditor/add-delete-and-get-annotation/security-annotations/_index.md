---
title: 使用 Java 的安全注释
linktitle: 安全注释
type: docs
weight: 60
url: /java/pdfannotationeditor-class/security-annotations/
description: 了解如何使用 Java 标记要密文的文本、应用密文注释以及密文 PDF 文件中的选定页面区域。
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: 使用安全注释在 Java 中编辑敏感 PDF 内容
Abstract: 本文介绍如何使用 Java 在 PDF 文档中使用密文注释。它涵盖使用密文注释标记匹配文本、永久应用密文以及根据检测到的图像放置矩形密文选定区域。
---
## 标记文本以进行密文编辑

1. 加载 PDF 并搜索所有页面以查找应编辑的文本。
2. 为每个匹配的文本片段创建一个`RedactionAnnotation`并配置其外观。
3. 将密文注释添加到其页面并保存文档。

```java
public static void markTextRedaction(Path inputFile, Path outputFile, String searchTerm) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(searchTerm);
        TextSearchOptions textSearchOptions = new TextSearchOptions(true);
        textFragmentAbsorber.setTextSearchOptions(textSearchOptions);
        document.getPages().accept(textFragmentAbsorber);

        for (TextFragment textFragment : textFragmentAbsorber.getTextFragments()) {
            Page page = textFragment.getPage();
            Rectangle annotationRectangle = textFragment.getRectangle();
            RedactionAnnotation annotation = new RedactionAnnotation(page, annotationRectangle);
            annotation.setFillColor(Color.getGray());
            annotation.setBorderColor(Color.getRed());
            annotation.setColor(Color.getWhite());
            annotation.setOverlayText("REDACTED");
            annotation.setTextAlignment(HorizontalAlignment.Center);
            annotation.setRepeat(true);
            page.getAnnotations().add(annotation, true);
        }

        document.save(outputFile.toString());
    }
}
```
