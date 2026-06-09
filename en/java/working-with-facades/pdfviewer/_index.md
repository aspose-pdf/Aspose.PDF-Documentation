---
title: PdfViewer Class
type: docs
weight: 135
url: /java/pdfviewer-class/
description: Learn how to use the PdfViewer facade in Java to decode PDF pages and inspect viewer-related settings.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Decode PDF pages and inspect viewer data in Java with PdfViewer
Abstract: This section explains how to use the PdfViewer facade in Aspose.PDF for Java for page decoding and viewer-related inspection tasks. The current Java examples cover rendering all pages to images, decoding a specific page, and inspecting page count, coordinate type, resolution, and bound viewer settings.
---
The Java `PdfViewerExamples` class demonstrates the main viewer workflows available through the Facades API.

## Decode all PDF pages

Use this workflow when every page of the source PDF should be rendered as an image.

### Steps

1. Create and configure a `PdfViewer` instance.
2. Bind the source PDF with `bindPdf`.
3. Call `decodeAllPages()` to render the document into a `BufferedImage` array.
4. Save each decoded page to an output image file.
5. Close the bound PDF file.

### Java example

```java
public static void decodeAllPages(Path inputFile, Path outputDir) throws Exception {
    PdfViewer viewer = createViewer();
    try {
        viewer.bindPdf(inputFile.toString());
        BufferedImage[] pages = viewer.decodeAllPages();
        for (int index = 0; index < pages.length; index++) {
            ImageIO.write(pages[index], "png", outputDir.resolve("decode_all_pages_" + (index + 1) + ".png").toFile());
        }
    } finally {
        viewer.closePdfFile();
    }
}
```

## Decode a specific PDF page

Use this workflow when only one page needs to be rendered to an image.

### Steps

1. Create and configure a `PdfViewer` instance.
2. Bind the source PDF.
3. Call `decodePage()` for the page you want to render.
4. Save the decoded page to an output image file.
5. Close the viewer.

### Java example

```java
public static void decodeSpecificPage(Path inputFile, Path outputFile) throws Exception {
    PdfViewer viewer = createViewer();
    try {
        viewer.bindPdf(inputFile.toString());
        ImageIO.write(viewer.decodePage(1), "png", outputFile.toFile());
    } finally {
        viewer.close();
    }
}
```

## Inspect PDF metadata

Use this workflow when you need viewer-related document information before rendering or printing.

### Steps

1. Create and configure a `PdfViewer` instance.
2. Bind the source PDF.
3. Read the page count, coordinate type, and rendering resolution.
4. Use or print the retrieved values.
5. Close the bound PDF file.

### Java example

```java
public static void inspectPdfMetadata(Path inputFile) {
    PdfViewer viewer = createViewer();
    try {
        viewer.bindPdf(inputFile.toString());
        System.out.println("Page count: " + viewer.getPageCount());
        System.out.println("Coordinate type: " + viewer.getCoordinateType());
        System.out.println("Resolution: " + viewer.getResolution());
    } finally {
        viewer.closePdfFile();
    }
}
```

## Inspect bound viewer settings

Use this workflow when you need to confirm or adjust viewer behavior after binding the PDF.

### Steps

1. Create and configure a `PdfViewer` instance.
2. Bind the source PDF.
3. Set viewer options such as auto-resize, auto-rotate, and print dialog visibility.
4. Read the active viewer settings and page count.
5. Close the viewer.

### Java example

```java
public static void inspectBoundViewerSettings(Path inputFile) {
    PdfViewer viewer = createViewer();
    try {
        viewer.bindPdf(inputFile.toString());
        viewer.setAutoResize(true);
        viewer.setAutoRotate(true);
        viewer.setPrintPageDialog(false);
        System.out.println("Page count: " + viewer.getPageCount());
        System.out.println("Print as image: " + viewer.getPrintAsImage());
        System.out.println("Auto resize: " + viewer.getAutoResize());
        System.out.println("Auto rotate: " + viewer.getAutoRotate());
    } finally {
        viewer.close();
    }
}
```
