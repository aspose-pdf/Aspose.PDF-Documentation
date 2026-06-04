---
title: Rotate PDF Text in Java
linktitle: Rotate Text Inside PDF
type: docs
weight: 50
url: /java/rotate-text-inside-pdf/
description: Learn how to rotate text fragments and paragraphs inside PDF documents in Java.
lastmod: "2026-06-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Rotate text fragments and paragraphs in PDF documents with Java
Abstract: This article explains how to rotate text in PDF documents using Aspose.PDF for Java. It shows how to rotate individual text fragments, build paragraphs containing rotated lines, and rotate complete text paragraphs for different layout scenarios.
---
## Rotate individual text fragments

1. Create a new PDF document.
1. Add a page to the document.
1. Create the required text objects and add them to the page.
1. Set the required text formatting options.
1. Save the output PDF document.

```java
public static void rotateTextInsidePdf1(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment2 = new TextFragment("rotated text");
        textFragment2.setPosition(new Position(200, 600));
        textFragment2.getTextState().setRotation(45);

        TextBuilder builder = new TextBuilder(page);
        builder.appendText(textFragment2);

        document.save(outputFile.toString());
    }
}
```
