---
title: Text Based Annotations using Java
linktitle: Text Annotations
type: docs
weight: 10
url: /java/text-based-annotations/
description: Learn how to add, inspect, and delete text, free text, and strikeout annotations in PDF documents using Aspose.PDF for Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Work with text PDF annotations in Java.
Abstract: This article explains how to create, read, and remove text-based annotations in PDF documents using Aspose.PDF for Java. It covers text annotations, free text annotations, and strikeout annotations based on the Java example implementations.
---
## Add a text annotation

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Create the required [TextAnnotation](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/textannotation/) on the target [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/).
1. Define the annotation [Rectangle](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/rectangle/) and set its title, subject, [AnnotationFlags](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/annotationflags/), and [Color](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/color/).
1. Add the annotation to the target page.
1. Save the updated PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).

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

## Add a free text annotation

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Create the required [FreeTextAnnotation](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/freetextannotation/) on the target [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/).
1. Initialize its [DefaultAppearance](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/defaultappearance/) and set the title and [Color](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/color/).
1. Add the annotation to the target page.
1. Save the updated PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).

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

## Related annotation topics

- [Interactive Annotations](/pdf/java/interactive-annotations/)
- [Markup Annotations](/pdf/java/markup-annotations/)
- [Security Annotations](/pdf/java/security-annotations/)
- [Shape Annotations](/pdf/java/shape-annotations/)
- [Watermark Annotations](/pdf/java/watermark-annotations/)
- [Import and Export Annotations](/pdf/java/import-export-annotations/)
