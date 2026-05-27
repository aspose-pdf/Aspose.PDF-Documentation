---
title: Security Annotations using Java
linktitle: Security Annotations
type: docs
weight: 75
url: /java/security-annotations/
description: Learn how to mark text for redaction, apply redaction annotations, and redact selected page areas in PDF files using Aspose.PDF for Java.
lastmod: "2026-05-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Redact sensitive PDF content in Java with security annotations.
Abstract: This article explains how to work with redaction annotations in PDF documents using Aspose.PDF for Java. It covers marking matched text with redaction annotations, permanently applying redactions, and redacting selected areas based on detected image placement rectangles.
---
## Mark text for redaction

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

## Apply or place redactions

`ExtraAnnotationExamples.java` also includes:

- `applyRedaction` to permanently apply existing redaction annotations
- `redactArea` to place a redaction annotation over a detected image area or fallback rectangle
