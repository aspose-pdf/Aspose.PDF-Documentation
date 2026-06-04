---
title: Add Page Numbers to PDF in Java
linktitle: Adding Page Number
type: docs
weight: 30
url: /java/add-page-number/
description: Learn how to add page number stamps to PDF documents in Java.
lastmod: "2026-06-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add page number stamps to PDF files with Java
Abstract: This article explains how to add page number stamps using Aspose.PDF for Java. It covers standard page numbering with custom font styling and Roman numeral numbering with a configurable starting number.
---
## Add a page number stamp

1. Open the source PDF document.
1. Set the required text formatting options.
1. Set the properties required by the example.
1. Add the configured object to the document structure.
1. Save the updated PDF document.

```java
public static void addPageNumStamp(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PageNumberStamp pageNumberStamp = new PageNumberStamp();
        pageNumberStamp.setBackground(false);
        pageNumberStamp.setFormat("Page # of " + document.getPages().size());
        pageNumberStamp.setBottomMargin(10);
        pageNumberStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        pageNumberStamp.setStartingNumber(1);
        pageNumberStamp.getTextState().setFont(FontRepository.findFont("Arial"));
        pageNumberStamp.getTextState().setFontSize(14.0f);
        pageNumberStamp.getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
        pageNumberStamp.getTextState().setForegroundColor(Color.getBlueViolet());

        document.getPages().get_Item(1).addStamp(pageNumberStamp);
        document.save(outputFile.toString());
    }
}
```
