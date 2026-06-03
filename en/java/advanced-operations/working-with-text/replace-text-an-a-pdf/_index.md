---
title: Replace Text in PDF with Java
linktitle: Replace Text in PDF
type: docs
weight: 40
url: /java/replace-text-in-pdf/
description: Learn how to replace, rearrange, and remove text in PDF documents using Java.
lastmod: "2026-05-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /python-net/replace-text-in-a-pdf-document/
TechArticle: true
AlternativeHeadline: Replace, remove, and adjust text content in PDF using Java
Abstract: This article explains text replacement workflows in PDF documents using Aspose.PDF for Java. It covers replacing text across all pages, limiting replacement to a selected region, adjusting replacement layout, using regex-based matching, replacing fonts, removing all text, and deleting hidden text.
---
Aspose.PDF for Java provides both simple replacement and layout-aware replacement features through `TextFragmentAbsorber` and replace options.

## Replace text on all pages

1. Open the source PDF document and locate the content to update.
2. Use the Aspose.PDF objects shown in the example to replace text on all pages.
3. Save the document to persist the replacement.

```java
public static void replaceTextOnAllPages(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber("PDF");
        document.getPages().accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            fragment.setText("pdf");
        }

        document.save(outputFile.toString());
    }
}
```

