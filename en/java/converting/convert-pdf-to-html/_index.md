---
title: Convert PDF to HTML in Java
linktitle: Convert PDF to HTML format
type: docs
weight: 50
url: /java/convert-pdf-to-html/
lastmod: "2026-06-16"
description: Learn how to convert PDF to HTML in Java with Aspose.PDF, including multi-page output, external image folders, SVG handling, and layered HTML rendering.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: How to Convert PDF to HTML in Java
Abstract: This article explains how to convert PDF files to HTML using Aspose.PDF for Java. It covers basic HTML export together with options for image folders, page splitting, SVG output, compressed SVG graphics, PNG page backgrounds, body-only markup, transparent text rendering, and document-layer conversion.
---
Aspose.PDF for Java supports HTML export with options for images, SVG, page splitting, transparency, and layer rendering. Use [`HtmlSaveOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/htmlsaveoptions/) to control how PDF pages, resources, and markup are written to HTML output.

## Convert PDF to HTML

Use this example when a PDF should be exported to a standard HTML document.

1. Open the source PDF in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Create default [`HtmlSaveOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/htmlsaveoptions/) for standard HTML serialization.
1. Call `document.save(outputFile.toString(), saveOptions)` so the PDF page content is exported as HTML markup.
1. Save the generated HTML output.

```java
public static void convertPdfToHtml(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convert PDF to HTML and store images separately

Use this example when extracted images should be written as separate files during HTML export.

1. Open the source PDF in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Create [`HtmlSaveOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/htmlsaveoptions/) and set `setSpecialFolderForAllImages(...)` to a dedicated image output directory.
1. Call `document.save(outputFile.toString(), saveOptions)` so raster images are emitted as separate resource files instead of inline-only output.
1. Save the HTML output together with the generated image assets.

```java
public static void convertPdfToHtmlStoringImages(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setSpecialFolderForAllImages(inputFile.getParent().resolve("images").toString());
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convert PDF to multi-page HTML

Use this example when each PDF page should be represented separately in HTML output.

1. Open the source PDF in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Create [`HtmlSaveOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/htmlsaveoptions/) and enable `setSplitIntoPages(true)`.
1. Call `document.save(outputFile.toString(), saveOptions)` so each PDF page is written as separate HTML output.
1. Save the generated HTML files.

```java
public static void convertPdfToHtmlMultiPage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setSplitIntoPages(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convert PDF to HTML and store SVG separately

Use this example when vector content should be emitted as separate SVG resources.

1. Open the source PDF in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Create [`HtmlSaveOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/htmlsaveoptions/) and set `setSpecialFolderForSvgImages(...)` to an external SVG resource directory.
1. Call `document.save(outputFile.toString(), saveOptions)` so vector graphics are stored outside the main HTML file.
1. Save the HTML output and SVG assets.

```java
public static void convertPdfToHtmlStoringSvg(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setSpecialFolderForSvgImages(inputFile.getParent().resolve("svg_images").toString());
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convert PDF to HTML with compressed SVG

Use this example when SVG output should be optimized during HTML export.

1. Open the source PDF in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Create [`HtmlSaveOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/htmlsaveoptions/) and configure a dedicated folder for SVG resources.
1. Enable `setCompressSvgGraphicsIfAny(true)` so SVG assets are compressed during export.
1. Call `document.save(outputFile.toString(), saveOptions)` and save the converted HTML files.

```java
public static void convertPdfToHtmlCompressSvg(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setSpecialFolderForSvgImages(inputFile.getParent().resolve("svg_images").toString());
        saveOptions.setCompressSvgGraphicsIfAny(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convert PDF to HTML with PNG page backgrounds

Use this example when page backgrounds should be rendered as PNG images in HTML output.

1. Open the source PDF in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Create [`HtmlSaveOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/htmlsaveoptions/) and set the raster image saving mode to PNG page backgrounds.
1. Call `document.save(outputFile.toString(), saveOptions)` so page background content is emitted as PNG-backed HTML layers.
1. Save the converted HTML output.

```java
public static void convertPdfToHtmlPngBackground(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setRasterImagesSavingMode(
                HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convert PDF to HTML body content only

Use this example when only the body markup is needed instead of a full HTML document shell.

1. Open the source PDF in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Create [`HtmlSaveOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/htmlsaveoptions/) and set the markup generation mode to `WriteOnlyBodyContent`.
1. Keep `setSplitIntoPages(true)` enabled when body-only output should still be page-separated.
1. Call `document.save(outputFile.toString(), saveOptions)` and save the HTML output.

```java
public static void convertPdfToHtmlBodyContent(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setHtmlMarkupGenerationMode(
                HtmlSaveOptions.HtmlMarkupGenerationModes.WriteOnlyBodyContent);
        saveOptions.setSplitIntoPages(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convert PDF to HTML with transparent text rendering

Use this example when transparent text should be preserved in the HTML export.

1. Open the source PDF in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Create [`HtmlSaveOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/htmlsaveoptions/) and enable transparent and shadowed text preservation.
1. Call `document.save(outputFile.toString(), saveOptions)` so the transparency-related text appearance is retained in the HTML result.
1. Save the converted HTML output.

```java
public static void convertPdfToHtmlTransparentTextRendering(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setSaveTransparentTexts(true);
        saveOptions.setSaveShadowedTextsAsTransparentTexts(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convert PDF to HTML with document layer rendering

Use this example when PDF layer visibility should be reflected in the HTML result.

1. Open the source PDF in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Create [`HtmlSaveOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/htmlsaveoptions/) and enable `setConvertMarkedContentToLayers(true)`.
1. Call `document.save(outputFile.toString(), saveOptions)` so marked PDF content is mapped into HTML layers.
1. Save the exported HTML files.

```java
public static void convertPdfToHtmlDocumentLayersRendering(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setConvertMarkedContentToLayers(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
