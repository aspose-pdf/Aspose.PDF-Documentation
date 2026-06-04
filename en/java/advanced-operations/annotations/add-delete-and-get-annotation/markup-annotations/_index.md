---
title: Markup Annotations using Java
linktitle: Markup Annotations
type: docs
weight: 30
url: /java/markup-annotations/
description: Learn how to add, inspect, and delete highlight, underline, squiggly, and strikeout annotations in PDF documents using Aspose.PDF for Java.
lastmod: "2026-06-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Work with markup annotations in PDF files using Java.
Abstract: This article explains how to create, inspect, and remove text markup annotations in PDF documents using Aspose.PDF for Java. It covers highlight, underline, squiggly, and strikeout annotations based on the repository Java examples.
---
## Add highlight, underline, squiggly, or strikeout annotations

1. Open the source PDF document.
1. Add the annotation to the target page.
1. Save the updated PDF document.
1. Set the annotation or object properties required by the example.
1. Add the annotation to the page collection and save the document.

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

## Related annotation topics

- [Text Annotations](/pdf/java/text-based-annotations/)
- [Interactive Annotations](/pdf/java/interactive-annotations/)
- [Shape Annotations](/pdf/java/shape-annotations/)
- [Media Annotations](/pdf/java/media-annotations/)
- [Security Annotations](/pdf/java/security-annotations/)
- [Watermark Annotations](/pdf/java/watermark-annotations/)
