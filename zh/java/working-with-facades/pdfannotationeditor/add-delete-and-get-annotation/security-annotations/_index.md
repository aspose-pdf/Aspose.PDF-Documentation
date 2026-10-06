---
title: 使用 Java 的安全批注
linktitle: 安全批注
type: docs
weight: 60
url: /zh/java/pdfannotationeditor-class/security-annotations/
description: 了解如何使用 Java 标记要遮蔽的文本、应用遮蔽批注，以及在 PDF 文件中遮蔽选定的页面区域。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 在 Java 中使用安全批注对敏感 PDF 内容进行遮蔽
Abstract: 本文解释了如何在 PDF 文档中使用 Java 处理遮蔽批注。内容包括使用遮蔽批注标记匹配的文本、永久应用遮蔽，以及根据检测到的图像放置矩形遮蔽选定区域。
---
## 标记要遮蔽的文本

1. 加载 PDF 并搜索所有页面中应被编辑的文本。
2. 创建一个 `RedactionAnnotation` 针对每个匹配的文本片段并配置其外观。
3. 将编辑批注添加到相应页面并保存文档。

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
