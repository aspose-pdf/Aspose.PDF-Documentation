---
title: Format PDF Documents in Java
linktitle: Formatting PDF Document
type: docs
weight: 11
url: /java/formatting-pdf-document/
description: Learn how to format PDF documents, embed fonts, control viewer settings, and adjust display options in Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Format document window, fonts, and zoom behavior in PDF files with Java
Abstract: This article explains how to format PDF documents using Aspose.PDF for Java. It covers reading and updating document window settings, embedding fonts, setting a default font, listing fonts, subsetting embedded fonts, and controlling the initial zoom factor.
---
Formatting in Aspose.PDF for Java includes viewer behavior, font embedding, and display settings.

## Get document window settings

Use this example to inspect the current viewer preferences stored in an existing PDF document.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Read the required window and display properties from the document.
1. Output the current settings for inspection or debugging.

```java
public static void getDocumentWindow(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        System.out.println("CenterWindow: " + document.isCenterWindow());
        System.out.println("Direction: " + document.getDirection());
        System.out.println("DisplayDocTitle: " + document.isDisplayDocTitle());
        System.out.println("FitWindow: " + document.isFitWindow());
        System.out.println("HideMenuBar: " + document.isHideMenubar());
        System.out.println("HideToolBar: " + document.isHideToolBar());
        System.out.println("HideWindowUI: " + document.isHideWindowUI());
        System.out.println("NonFullScreenPageMode: " + document.getNonFullScreenPageMode());
        System.out.println("PageLayout: " + document.getPageLayout());
        System.out.println("PageMode: " + document.getPageMode());
    }
}
```

## Set document window preferences

This example updates how the PDF should be displayed when it is opened in a compatible viewer.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Set the required window, layout, and page-mode preferences.
1. Save the updated PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void setDocumentWindow(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.setCenterWindow(true);
        document.setDirection(Direction.R2L);
        document.setDisplayDocTitle(true);
        document.setFitWindow(true);
        document.setHideMenubar(true);
        document.setHideToolBar(true);
        document.setHideWindowUI(true);
        document.setNonFullScreenPageMode(PageMode.UseOC);
        document.setPageLayout(PageLayout.TwoColumnLeft);
        document.setPageMode(PageMode.UseThumbs);
        document.save(outputFile.toString());
    }
}
```

## Embed fonts in an existing PDF

Use this approach when a document should carry its required fonts for more reliable rendering on other systems.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Enable standard font embedding and iterate through the fonts used by each [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Mark any non-embedded [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) objects for embedding.
1. Save the updated document.

```java
public static void embeddedFonts(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.setEmbedStandardFonts(true);
        for (Page page : document.getPages()) {
            for (Font pageFont : page.getResources().getFonts()) {
                if (!pageFont.isEmbedded()) {
                    pageFont.setEmbedded(true);
                }
            }
        }
        document.save(outputFile.toString());
    }
}
```

## Embed fonts when creating a new PDF

This example creates a new PDF and assigns an embedded font to the text content from the start.

1. Create a new PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) and add a [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Create the required [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/), [TextSegment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textsegment/), and [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstate/).
1. Resolve the target [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) from the repository and mark it as embedded.
1. Add the text content to the page and save the output document.

```java
public static void embeddedFontsInNewDocument(Path outputFile) {
    try (Document document = new Document()) {
        try (Page page = document.getPages().add()) {
            TextFragment fragment = new TextFragment("");
            TextSegment segment = new TextSegment(" This is a sample text using Custom font.");
            TextState textState = new TextState();
            Font font = FontRepository.findFont("Arial");
            font.setEmbedded(true);
            textState.setFont(font);
            segment.setTextState(textState);
            fragment.getSegments().add(segment);
            page.getParagraphs().add(fragment);
        }
        document.save(outputFile.toString());
    }
}
```

## Set a default font for PDF output

Use this pattern when the saved document should fall back to a specific font during output generation.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Create [PdfSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfsaveoptions/) and set the default font name.
1. Save the document with the configured save options.

```java
public static void setDefaultFont(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PdfSaveOptions saveOptions = new PdfSaveOptions();
        saveOptions.setDefaultFontName("Arial");
        document.save(outputFile.toString(), saveOptions);
    }
}
```

## Get all fonts used in a PDF

This example lists every font detected in the document so you can audit font usage before exporting or updating the file.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Enumerate the fonts returned by the document font utilities.
1. Output the name of each detected [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/).

```java
public static void getAllFonts(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Font font : document.getFontUtilities().getAllFonts()) {
            System.out.println(font.getFontName());
        }
    }
}
```

## Improve font embedding by subsetting fonts

Use this approach when you want to reduce font payload while keeping embedded font data aligned with document usage.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Run font subsetting through the document font utilities with the required [FontSubsetStrategy](https://reference.aspose.com/pdf/java/com.aspose.pdf/fontsubsetstrategy/) values.
1. Save the optimized document.

```java
public static void improveFontsEmbedding(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getFontUtilities().subsetFonts(FontSubsetStrategy.SubsetAllFonts);
        document.getFontUtilities().subsetFonts(FontSubsetStrategy.SubsetEmbeddedFontsOnly);
        document.save(outputFile.toString());
    }
}
```

## Set the document open zoom factor

This example configures the initial zoom level that should be applied when the PDF is opened.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Create a [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/) with an [XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/xyzexplicitdestination/).
1. Assign the action as the document open action and save the result.

```java
public static void setZoomFactor(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GoToAction action = new GoToAction(new XYZExplicitDestination(1, 0.0, 0.0, 0.5));
        document.setOpenAction(action);
        document.save(outputFile.toString());
    }
}
```

## Get the document open zoom factor

Use this example to inspect whether a PDF already defines an explicit zoom level for its open action.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Check whether the open action is a [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/) with an [XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/xyzexplicitdestination/).
1. Output the configured zoom value or report that no zoom is set.

```java
public static void getZoomFactor(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        if (document.getOpenAction() instanceof GoToAction action
                && action.getDestination() instanceof XYZExplicitDestination destination) {
            System.out.println("Zoom: " + destination.getZoom());
        } else {
            System.out.println("Zoom: not set");
        }
    }
}
```
