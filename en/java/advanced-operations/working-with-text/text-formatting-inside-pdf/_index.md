---
title: Format PDF Text in Java
linktitle: Text Formatting inside PDF
type: docs
weight: 70
url: /java/text-formatting-inside-pdf/
description: Learn how to format text inside PDF documents in Java using spacing, notes, lists, multi-column layout, and styling options.
lastmod: "2026-06-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Format and style text inside PDF files with Java
Abstract: This article explains how to format text in PDF documents using Aspose.PDF for Java. It covers line spacing, character spacing, bullet and numbered lists, footnotes and endnotes, inline paragraph content, multi-column layout, forced page breaks, and custom tab stops.
---
Aspose.PDF for Java provides formatting features at the text state, paragraph, and page layout levels.

## Specify line spacing

1. Create a new PDF document.
1. Add a page to the document.
1. Set the required text formatting options.
1. Save the output PDF document.

```java
public static void specifyLineSpacingSimpleCase(Path outputFile) throws Exception {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("Lorem ipsum text");
        textFragment.getTextState().setFontSize(12);
        textFragment.getTextState().setLineSpacing(16);
        page.getParagraphs().add(textFragment);

        document.save(outputFile.toString());
    }
}
```
