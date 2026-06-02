---
title: Format PDF Documents in Java
linktitle: Formatting PDF Document
type: docs
weight: 11
url: /java/formatting-pdf-document/
description: Learn how to format PDF documents, embed fonts, control viewer settings, and adjust display options in Java.
lastmod: "2026-05-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Format document window, fonts, and zoom behavior in PDF files with Java
Abstract: This article explains how to format PDF documents using Aspose.PDF for Java. It covers reading and updating document window settings, embedding fonts, setting a default font, listing fonts, subsetting embedded fonts, and controlling the initial zoom factor.
---
Formatting in Aspose.PDF for Java includes viewer behavior, font embedding, and display settings.

## Read and set document window properties

Use the `Document` API to inspect or update window and page display settings:

1. Open the PDF document used in this example.
2. Use the Aspose.PDF API calls shown here to read and set document window properties.
3. Read the returned values or continue with your next processing step.

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

1. Open or create the PDF document used in this example.
2. Use the Aspose.PDF API calls shown in the snippet to embed fonts in an existing PDF.
3. Save the document or inspect the result, depending on the scenario.

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

The same example class also includes `embeddedFontsInNewDocument`, which creates a new page, applies an embedded `Arial` font through `TextState`, and saves the result.

## Set a default font and improve embedding

`setDefaultFont` saves the document with `PdfSaveOptions.setDefaultFontName("Arial")`, while `improveFontsEmbedding` calls `subsetFonts(...)` with `FontSubsetStrategy` values to reduce embedded font data.

## Set and read the initial zoom factor

1. Load the PDF document or object that will be updated.
2. Apply the settings shown in the example to set and read the initial zoom factor.
3. Save the document if the change should persist.

```java
public static void setZoomFactor(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GoToAction action = new GoToAction(new XYZExplicitDestination(1, 0.0, 0.0, 0.5));
        document.setOpenAction(action);
        document.save(outputFile.toString());
    }
}
```
