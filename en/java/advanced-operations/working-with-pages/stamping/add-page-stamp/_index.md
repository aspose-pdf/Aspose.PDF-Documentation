---
title: Add Page Stamps to PDF in Java
linktitle: Adding Page Stamps
type: docs
weight: 30
url: /java/page-stamps-in-the-pdf-file/
description: Learn how to add PDF page stamps as overlays or backgrounds in Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add page-based stamps to PDF files with Java
Abstract: This article explains how to add a page stamp to a PDF document using Aspose.PDF for Java. The example loads another PDF page as a stamp, configures it as a background, and applies it to a target page.
---
Aspose.PDF for Java can apply a page from another PDF as a stamp or add page numbering overlays.

## Add a page stamp from another PDF

Use this example when a page from a separate PDF should be used as a background stamp.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Create a [PdfPageStamp](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/pdfpagestamp/) from the external PDF page.
1. Configure the stamp and add it to the target page, then save the result.

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

## Add a standard page number stamp

Use this example when the target page should show the current number with custom text formatting.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Create and configure a [PageNumberStamp](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/pagenumberstamp/).
1. Add the stamp to the page and save the document.

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

## Add a Roman numeral page number stamp

Use this example when page numbering should start from a custom value and use uppercase Roman numerals.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Create a [PageNumberStamp](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/pagenumberstamp/) and configure Roman numeral numbering.
1. Add the stamp to all pages and save the PDF.

```java
public static void addPageNumStampRoman(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PageNumberStamp pageNumberStamp = new PageNumberStamp();
        pageNumberStamp.setBackground(false);
        pageNumberStamp.setBottomMargin(10);
        pageNumberStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        pageNumberStamp.setStartingNumber(42);
        pageNumberStamp.setNumberingStyle(NumberingStyle.NumeralsRomanUppercase);
        pageNumberStamp.getTextState().setFont(FontRepository.findFont("Arial"));
        pageNumberStamp.getTextState().setFontSize(14.0f);
        pageNumberStamp.getTextState().setFontStyle(FontStyles.Bold);
        pageNumberStamp.getTextState().setForegroundColor(Color.getBlueViolet());

        for (Page page : document.getPages()) {
            page.addStamp(pageNumberStamp);
        }
        document.save(outputFile.toString());
    }
}
```
