---
title: Security Annotations using Java
linktitle: Security Annotations
type: docs
weight: 75
url: /java/security-annotations/
description: Learn how to mark text for redaction, apply redaction annotations, and redact selected page areas in PDF files using Aspose.PDF for Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Redact sensitive PDF content in Java with security annotations.
Abstract: This article explains how to work with redaction annotations in PDF documents using Aspose.PDF for Java. It covers marking matched text with redaction annotations, permanently applying redactions, and redacting selected areas based on detected image placement rectangles.
---
Security annotation workflows in this section focus on preparing and applying redactions to sensitive PDF content.

## Mark text with redaction annotations

Use this example when matching text should be covered by redaction annotations before the redaction is permanently applied.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Search for the target text and create a [RedactionAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/redactionannotation/) for each match.
1. Configure the redaction appearance and save the document.

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

## Apply existing redactions

This example permanently applies redaction annotations that already exist on the page.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Collect annotations of type [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Redaction`.
1. Call `redact()` on each collected annotation and save the updated file.

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

## Redact a selected page area

Use this approach when the target content is identified by position rather than by matching text.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Detect the target rectangle on the page, for example from an image placement.
1. Create a [RedactionAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/redactionannotation/) for that area and save the document.

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

## Related annotation topics

- [Interactive Annotations](/pdf/java/interactive-annotations/)
- [Markup Annotations](/pdf/java/markup-annotations/)
- [Shape Annotations](/pdf/java/shape-annotations/)
- [Text Annotations](/pdf/java/text-based-annotations/)
- [Watermark Annotations](/pdf/java/watermark-annotations/)
- [Import and Export Annotations](/pdf/java/import-export-annotations/)
