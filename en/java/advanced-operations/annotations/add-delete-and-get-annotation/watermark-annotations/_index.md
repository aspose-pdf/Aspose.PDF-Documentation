---
title: Watermark Annotations using Java
linktitle: Watermark Annotations
type: docs
weight: 70
url: /java/watermark-annotations/
description: Learn how to add, inspect, and delete watermark annotations in PDF documents using Aspose.PDF for Java.
lastmod: "2026-06-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Work with watermark annotations in PDF files using Java.
Abstract: This article explains how to create, inspect, and remove watermark annotations in PDF documents using Aspose.PDF for Java. It covers adding a text watermark annotation with custom text state and opacity, reading existing watermark annotation areas, and deleting watermark annotations.
---
## Add a watermark annotation

1. Open the source PDF document.
1. Set the required text formatting options.
1. Set the annotation or object properties required by the example.
1. Add the annotation to the target page.
1. Save the updated PDF document.
1. Create the `WatermarkAnnotation`, add it to the page, and configure the watermark text state and opacity.
1. Apply the watermark text lines and save the modified PDF.

```java
public static void watermarkAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        WatermarkAnnotation watermarkAnnotation = new WatermarkAnnotation(
                document.getPages().get_Item(1), new Rectangle(100, 0, 400, 100, true));

        document.getPages().get_Item(1).getAnnotations().add(watermarkAnnotation);

        TextState textState = new TextState();
        textState.setForegroundColor(Color.getBlue());
        textState.setFontSize(25);
        textState.setFont(FontRepository.findFont("Arial"));

        watermarkAnnotation.setOpacity(0.5);
        watermarkAnnotation.setTextAndState(new String[]{"HELLO", "Line 1", "Line 2"}, textState);

        document.save(outputFile.toString());
    }
}
```

## Related annotation topics

- [Interactive Annotations](/pdf/java/interactive-annotations/)
- [Markup Annotations](/pdf/java/markup-annotations/)
- [Security Annotations](/pdf/java/security-annotations/)
- [Shape Annotations](/pdf/java/shape-annotations/)
- [Text Annotations](/pdf/java/text-based-annotations/)
- [Import and Export Annotations](/pdf/java/import-export-annotations/)
