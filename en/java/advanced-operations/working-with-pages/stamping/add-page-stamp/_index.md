---
title: Add Page Stamps to PDF in Java
linktitle: Adding Page Stamps
type: docs
weight: 30
url: /java/page-stamps-in-the-pdf-file/
description: Learn how to add PDF page stamps as overlays or backgrounds in Java.
lastmod: "2026-05-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add page-based stamps to PDF files with Java
Abstract: This article explains how to add a page stamp to a PDF document using Aspose.PDF for Java. The example loads another PDF page as a stamp, configures it as a background, and applies it to a target page.
---
## Add a PDF page as a stamp

1. Open the target PDF document and load the PDF page that will be used as the stamp source.
2. Create the `PdfPageStamp`, configure its placement options, and add it to the target page.
3. Save the stamped PDF document.

```java
public static void addPageStamp(Path inputFile, Path pageStampFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PdfPageStamp pageStamp = new PdfPageStamp(pageStampFile.toString(), 1);
        pageStamp.setBackground(true);
        document.getPages().get_Item(1).addStamp(pageStamp);
        document.save(outputFile.toString());
    }
}
```
