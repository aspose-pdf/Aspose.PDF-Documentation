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
## Mark text for redaction

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Create a [TextFragmentAbsorber](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/textfragmentabsorber/) and search for the target text.
1. Configure the [TextSearchOptions](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/textsearchoptions/) required by the example.
1. Create [RedactionAnnotation](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/redactionannotation/) items for the matched text locations.
1. Set the [RedactionAnnotation](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/redactionannotation/) or related object properties required by the example.
1. Add each [RedactionAnnotation](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/redactionannotation/) to the target [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/).
1. Read or iterate through the [Annotation](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/annotation/) items on the target page.
1. Save the updated PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Create a [RedactionAnnotation](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/redactionannotation/) for each matched [TextFragment](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/textfragment/) and configure its appearance.
1. Add the redaction annotations to their pages and save the [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).

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

## Related annotation topics

- [Interactive Annotations](/pdf/java/interactive-annotations/)
- [Markup Annotations](/pdf/java/markup-annotations/)
- [Shape Annotations](/pdf/java/shape-annotations/)
- [Text Annotations](/pdf/java/text-based-annotations/)
- [Watermark Annotations](/pdf/java/watermark-annotations/)
- [Import and Export Annotations](/pdf/java/import-export-annotations/)
