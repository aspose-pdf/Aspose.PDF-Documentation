---
title: Security Annotations using Java
linktitle: Security Annotations
type: docs
weight: 60
url: /java/pdfannotationeditor-class/security-annotations/
description: Learn how to mark text for redaction, apply redaction annotations, and redact selected page areas in PDF files using Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Redact sensitive PDF content in Java with security annotations
Abstract: This article explains how to work with redaction annotations in PDF documents using Java. It covers marking matched text with redaction annotations, permanently applying redactions, and redacting selected areas based on detected image placement rectangles.
---
## Mark text for redaction

1. Load the PDF and search all pages for the text that should be redacted.
2. Create a `RedactionAnnotation` for each matched text fragment and configure its appearance.
3. Add the redaction annotations to their pages and save the document.

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
