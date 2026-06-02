---
title: Rotate PDF Text in Java
linktitle: Rotate Text Inside PDF
type: docs
weight: 50
url: /java/rotate-text-inside-pdf/
description: Learn how to rotate text fragments and paragraphs inside PDF documents in Java.
lastmod: "2026-05-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Rotate text fragments and paragraphs in PDF documents with Java
Abstract: This article explains how to rotate text in PDF documents using Aspose.PDF for Java. It shows how to rotate individual text fragments, build paragraphs containing rotated lines, and rotate complete text paragraphs for different layout scenarios.
---
## Rotate individual text fragments

1. Open the PDF document and locate the target page or content.
2. Apply the Aspose.PDF operations shown in the example to rotate individual text fragments.
3. Save the document to preserve the rotation change.

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

## Rotate text inside a paragraph

`rotateTextInsidePdf2` builds a `TextParagraph`, appends several `TextFragment` lines, and applies different `TextState` rotations.

## Rotate paragraph content directly on the page

`rotateTextInsidePdf3` adds rotated fragments straight to `page.getParagraphs()`, while `rotateTextInsidePdf4` rotates whole `TextParagraph` objects by different angles.
