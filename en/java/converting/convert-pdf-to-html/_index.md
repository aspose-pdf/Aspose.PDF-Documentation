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
Aspose.PDF for Java supports HTML export with options for images, SVG, page splitting, transparency, and layer rendering.

## Convert PDF to HTML

Use this example when a PDF should be exported to a standard HTML document.

1. Open the source PDF in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Create default [`HtmlSaveOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/htmlsaveoptions/) for standard HTML export.
1. Pass the save options to the shared save method so the PDF is serialized as HTML markup.
1. Save the generated HTML output.

```java
public static void convertPdfToHtml(Path inputFile, Path outputFile) {
       saveDocument(inputFile, outputFile, new HtmlSaveOptions());
   }
```

## Convert PDF to HTML and store images separately

Use this example when extracted images should be written as separate files during HTML export.

1. Open the source PDF in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Create [`HtmlSaveOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/htmlsaveoptions/) and set `setSpecialFolderForAllImages(...)` to an image output directory.
1. Pass the configured save options to the shared save method so extracted images are written as separate resources.
1. Save the HTML output together with the generated image assets.

```java
public static void convertPdfToHtmlStoringImages(Path inputFile, Path outputFile) {
    HtmlSaveOptions saveOptions = new HtmlSaveOptions();
    saveOptions.setSpecialFolderForAllImages(inputFile.getParent().resolve("images").toString());
    saveDocument(inputFile, outputFile, saveOptions);
}
```

## Convert PDF to multi-page HTML

Use this example when each PDF page should be represented separately in HTML output.

1. Open the source PDF in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Create [`HtmlSaveOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/htmlsaveoptions/) and enable `setSplitIntoPages(true)`.
1. Pass the configured save options to the shared save method so each PDF page is emitted as separate HTML output.
1. Save the generated HTML files.

```java
public static void convertPdfToHtmlMultiPage(Path inputFile, Path outputFile) {
    HtmlSaveOptions saveOptions = new HtmlSaveOptions();
    saveOptions.setSplitIntoPages(true);
    saveDocument(inputFile, outputFile, saveOptions);
}
```

## Convert PDF to HTML and store SVG separately

Use this example when vector content should be emitted as separate SVG resources.

1. Open the source PDF in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Create [`HtmlSaveOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/htmlsaveoptions/) and set `setSpecialFolderForSvgImages(...)` for external SVG resource storage.
1. Pass the configured save options to the shared save method so vector content is written outside the main HTML file.
1. Save the HTML output and SVG assets.

```java
public static void convertPdfToHtmlStoringSvg(Path inputFile, Path outputFile) {
    HtmlSaveOptions saveOptions = new HtmlSaveOptions();
    saveOptions.setSpecialFolderForSvgImages(inputFile.getParent().resolve("svg_images").toString());
    saveDocument(inputFile, outputFile, saveOptions);
}
```

## Convert PDF to HTML with compressed SVG

Use this example when SVG output should be optimized during HTML export.

1. Open the source PDF in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Create [`HtmlSaveOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/htmlsaveoptions/) and configure a dedicated SVG resource folder.
1. Enable `setCompressSvgGraphicsIfAny(true)` so SVG assets are optimized during export.
1. Save the converted HTML files through the shared save method.

```java
public static void convertPdfToHtmlCompressSvg(Path inputFile, Path outputFile) {
    HtmlSaveOptions saveOptions = new HtmlSaveOptions();
    saveOptions.setSpecialFolderForSvgImages(inputFile.getParent().resolve("svg_images").toString());
    saveOptions.setCompressSvgGraphicsIfAny(true);
    saveDocument(inputFile, outputFile, saveOptions);
}
```

## Convert PDF to HTML with PNG page backgrounds

Use this example when page backgrounds should be rendered as PNG images in HTML output.

1. Open the source PDF in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Create [`HtmlSaveOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/htmlsaveoptions/) and set the raster image saving mode to PNG page backgrounds.
1. Pass the configured save options to the shared save method so background graphics are emitted as PNG-backed page layers.
1. Save the converted HTML output.

```java
public static void convertPdfToHtmlPngBackground(Path inputFile, Path outputFile) {
    HtmlSaveOptions saveOptions = new HtmlSaveOptions();
    saveOptions.setRasterImagesSavingMode(HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground);
    saveDocument(inputFile, outputFile, saveOptions);
}
```

## Convert PDF to HTML body content only

Use this example when only the body markup is needed instead of a full HTML document shell.

1. Open the source PDF in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Create [`HtmlSaveOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/htmlsaveoptions/) and set the markup generation mode to `WriteOnlyBodyContent`.
1. Keep `setSplitIntoPages(true)` enabled when body-only output should still be page-separated.
1. Save the HTML output through the shared save method.

```java
public static void convertPdfToHtmlBodyContent(Path inputFile, Path outputFile) {
    HtmlSaveOptions saveOptions = new HtmlSaveOptions();
    saveOptions.setHtmlMarkupGenerationMode(HtmlSaveOptions.HtmlMarkupGenerationModes.WriteOnlyBodyContent);
    saveOptions.setSplitIntoPages(true);
    saveDocument(inputFile, outputFile, saveOptions);
}
```

## Convert PDF to HTML with transparent text rendering

Use this example when transparent text should be preserved in the HTML export.

1. Open the source PDF in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Create [`HtmlSaveOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/htmlsaveoptions/) and enable transparent and shadowed text preservation.
1. Pass the configured save options to the shared save method so visual transparency is retained in the generated HTML.
1. Save the converted HTML output.

```java
public static void convertPdfToHtmlTransparentTextRendering(Path inputFile, Path outputFile) {
    HtmlSaveOptions saveOptions = new HtmlSaveOptions();
    saveOptions.setSaveTransparentTexts(true);
    saveOptions.setSaveShadowedTextsAsTransparentTexts(true);
    saveDocument(inputFile, outputFile, saveOptions);
}
```

## Convert PDF to HTML with document layer rendering

Use this example when PDF layer visibility should be reflected in the HTML result.

1. Open the source PDF in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Create [`HtmlSaveOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/htmlsaveoptions/) and enable `setConvertMarkedContentToLayers(true)`.
1. Pass the configured save options to the shared save method so marked PDF content is mapped to HTML layers.
1. Save the exported HTML files.

```java
public static void convertPdfToHtmlDocumentLayersRendering(Path inputFile, Path outputFile) {
    HtmlSaveOptions saveOptions = new HtmlSaveOptions();
    saveOptions.setConvertMarkedContentToLayers(true);
    saveDocument(inputFile, outputFile, saveOptions);
}
```

## Reuse a shared HTML save method

Use this method when several HTML conversion examples should save the document through one common export function.

1. Open the source PDF in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Pass the prepared [`HtmlSaveOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/htmlsaveoptions/) into the method with the input and output paths.
1. Call `document.save(outputFile.toString(), saveOptions)` so the selected HTML export settings are applied consistently.
1. Save the converted HTML output and release the document resources automatically.

```java
private static void saveDocument(Path inputFile, Path outputFile, HtmlSaveOptions saveOptions) {
    try (Document document = new Document(inputFile.toString())) {
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
