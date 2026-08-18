---
title: 使用 Java 的安全注释
linktitle: 安全注释
type: docs
weight: 75
url: /java/security-annotations/
description: Learn how to mark text for redaction, apply redaction annotations, and redact selected page areas in PDF files using Aspose.PDF for Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用安全注释在 Java 中编辑敏感 PDF 内容。
Abstract: 本文介绍如何使用 Aspose.PDF for Java 在 PDF 文档中使用密文注释。它涵盖使用密文注释标记匹配文本、永久应用密文以及根据检测到的图像放置矩形密文选定区域。
---
本节中的安全注释工作流程重点关注对敏感 PDF 内容准备和应用修订。

## 使用密文注释标记文本

当匹配文本在永久应用密文之前应被密文注释覆盖时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 搜索目标文本并为每个匹配项创建一个 [RedactionAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/redactionannotation/)。
1. 配置密文外观并保存文档。

```java
public static void markTextRedaction(Path inputFile, Path outputFile, String searchTerm) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(searchTerm);
        TextSearchOptions textSearchOptions = new TextSearchOptions(true);
        textFragmentAbsorber.setTextSearchOptions(textSearchOptions);
        document.getPages().accept(textFragmentAbsorber);

        for (var textFragment : textFragmentAbsorber.getTextFragments()) {
            Page page = textFragment.getPage();
            RedactionAnnotation redactionAnnotation = new RedactionAnnotation(page, textFragment.getRectangle());
            redactionAnnotation.setFillColor(Color.getGray());
            redactionAnnotation.setBorderColor(Color.getRed());
            redactionAnnotation.setColor(Color.getWhite());
            redactionAnnotation.setOverlayText("REDACTED");
            redactionAnnotation.setTextAlignment(HorizontalAlignment.Center);
            redactionAnnotation.setRepeat(true);
            page.getAnnotations().add(redactionAnnotation, true);
        }
        document.save(outputFile.toString());
    }
}
```

## 应用现有的修订

此示例永久应用页面上已存在的密文注释。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 收集 [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Redaction` 类型的注释。
1. 对每个收集的注释调用 `redact()` 并保存更新的文件。

```java
public static void applyRedaction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<RedactionAnnotation> redactionAnnotations = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Redaction) {
                redactionAnnotations.add((RedactionAnnotation) annotation);
            }
        }
        for (RedactionAnnotation redactionAnnotation : redactionAnnotations) {
            redactionAnnotation.redact();
        }
        document.save(outputFile.toString());
    }
}
```

## 编辑选定的页面区域

当目标内容是通过位置而不是匹配文本来标识时，请使用此方法。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 检测页面上的目标矩形，例如从图像位置。
1. 为该区域创建一个 [RedactionAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/redactionannotation/) 并保存文档。

```java
public static void redactArea(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber imagePlacementAbsorber = new ImagePlacementAbsorber();
        Page page = document.getPages().get_Item(1);
        page.accept(imagePlacementAbsorber);

        com.aspose.pdf.Rectangle targetRect = imagePlacementAbsorber.getImagePlacements().get_Item(2).getRectangle();
        RedactionAnnotation redactionAnnotation = new RedactionAnnotation(page, targetRect);
        redactionAnnotation.setFillColor(Color.getGray());
        redactionAnnotation.setBorderColor(Color.getRed());
        redactionAnnotation.setColor(Color.getWhite());
        redactionAnnotation.setOverlayText("REDACTED");
        redactionAnnotation.setTextAlignment(HorizontalAlignment.Center);
        redactionAnnotation.setRepeat(true);

        page.getAnnotations().add(redactionAnnotation, true);
        document.save(outputFile.toString());
    }
}
```

## 相关注释主题

- [交互式注释](/pdf/java/interactive-annotations/)
- [标记注释](/pdf/java/markup-annotations/)
- [形状注释](/pdf/java/shape-annotations/)
- [文字注释](/pdf/java/text-based-annotations/)
- [水印注释](/pdf/java/watermark-annotations/)
- [导入和导出注释](/pdf/java/import-export-annotations/)
