---
title: Format PDF Documents in Java
linktitle: Formatting PDF Document
type: docs
weight: 11
url: /java/formatting-pdf-document/
description: Learn how to format PDF documents, embed fonts, control viewer settings, and adjust display options in Java.
lastmod: "2026-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Format document window, fonts, and zoom behavior in PDF files with Java
Abstract: This article explains how to format PDF documents using Aspose.PDF for Java. It covers reading and updating document window settings, embedding fonts, setting a default font, listing fonts, subsetting embedded fonts, and controlling the initial zoom factor.
---
Formatting in Aspose.PDF for Java includes viewer behavior, font embedding, and display settings.

## Read and set document window properties

Use the [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) API to inspect or update window and page display settings:

1. Open the source PDF document with [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Set the required [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) properties, including [Direction](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/direction/), [PageMode](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/pagemode/), and [PageLayout](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/pagelayout/).
1. Save the updated PDF document with [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Read the returned values or continue with your next processing step.

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

The companion `getDocumentWindow` example prints the current values for these properties.

## Embed fonts in an existing PDF

1. Open the source PDF document with [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Enable standard font embedding on [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) and update each [Font](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/font/) on every [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/).
1. Save the updated PDF document with [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).

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

The same example class also includes `embeddedFontsInNewDocument`, which creates a new [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/), applies an embedded `Arial` font through [TextState](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/textstate/), and saves the result.

## Set a default font and improve embedding

`setDefaultFont` saves the document with [PdfSaveOptions](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/pdfsaveoptions/) and `setDefaultFontName("Arial")`, while `improveFontsEmbedding` calls `subsetFonts(...)` with [FontSubsetStrategy](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/fontsubsetstrategy/) values to reduce embedded font data.

## Set and read the initial zoom factor

1. Open the source PDF document with [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Create a [GoToAction](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/gotoaction/) with an [XYZExplicitDestination](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/xyzexplicitdestination/) and assign it to the target [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Set the required [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) properties for the opening view.
1. Save the updated PDF document with [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).

```java
public static void setZoomFactor(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GoToAction action = new GoToAction(new XYZExplicitDestination(1, 0.0, 0.0, 0.5));
        document.setOpenAction(action);
        document.save(outputFile.toString());
    }
}
```
