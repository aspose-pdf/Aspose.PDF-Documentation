---
title: 使用 Java 的安全批注
linktitle: 安全批注
type: docs
weight: 75
url: /zh/java/security-annotations/
description: 了解如何在 PDF 文件中使用 Aspose.PDF for Java 标记待删减的文本、应用删减批注以及删减选定的页面区域。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Java 中使用安全批注对敏感的 PDF 内容进行删减。
Abstract: 本文解释了如何使用 Aspose.PDF for Java 在 PDF 文档中处理编辑遮盖批注。它包括使用编辑遮盖批注标记匹配的文本、永久应用遮盖以及根据检测到的图像放置矩形对选定区域进行遮盖。
---
本节中的安全批注工作流侧重于准备和应用编辑遮盖，以处理敏感的 PDF 内容。

## 使用编辑遮盖批注标记文本

当匹配的文本需要在永久应用编辑遮盖之前先被编辑遮盖批注覆盖时，请使用此示例。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 搜索目标文本，并为每个匹配项创建一个 [RedactionAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/redactionannotation/)。
1. 配置编辑掩码外观并保存文档。

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

## 应用现有的编辑标记

此示例会永久应用页面上已存在的编辑标记。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 收集指定类型的批注 [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Redaction`。
1. 呼叫 `redact()` 对每个收集的批注执行操作并保存更新后的文件。

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

## 对选定的页面区域进行编辑

当目标内容通过位置而不是通过匹配文本来识别时，请使用此方法。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 在页面上检测目标矩形，例如来自图像放置的位置。
1. 创建一个 [RedactionAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/redactionannotation/) 用于该区域并保存文档。

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

## 相关批注主题

- [交互式批注](/pdf/zh/java/interactive-annotations/)
- [标记批注](/pdf/zh/java/markup-annotations/)
- [形状批注](/pdf/zh/java/shape-annotations/)
- [文本批注](/pdf/zh/java/text-based-annotations/)
- [水印批注](/pdf/zh/java/watermark-annotations/)
- [导入和导出批注](/pdf/zh/java/import-export-annotations/)
