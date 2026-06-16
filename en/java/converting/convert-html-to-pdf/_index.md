---
title: Convert HTML to PDF in Java
linktitle: Convert HTML to PDF file
type: docs
weight: 40
url: /java/convert-html-to-pdf/
lastmod: "2026-06-09"
description: Learn how to convert HTML, MHTML, and web pages to PDF in Java with Aspose.PDF, including media settings, font embedding, and single-page output.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: How to convert HTML to PDF in Java with Aspose.PDF
Abstract: This article explains how to convert HTML and MHTML files to PDF using Aspose.PDF for Java. It covers the basic HTML-to-PDF workflow and shows how to control rendering with media types, CSS page rule priority, embedded fonts, single-page output, and direct conversion from a live web page.
---
Aspose.PDF for Java supports HTML-to-PDF conversion from files, HTML options, and live web pages.

## Convert HTML to PDF

Use this example when a local HTML file should be converted directly into a PDF document.

1. Open the source HTML file with the required HTML load options.
1. Create the PDF document from the HTML source.
1. Save the generated PDF file.

```java
public static void convertHtmlToPdf(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions();
    loadOptions.setPageLayoutOption(HtmlPageLayoutOption.ScaleToPageWidth);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convert HTML to PDF with media type options

Use this example when CSS media type handling should be controlled during HTML conversion.

1. Configure the HTML load options for the required media type behavior.
1. Open the HTML source with those options.
1. Save the converted PDF document.

```java
public static void convertHtmlToPdfMediaType(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions();
    loadOptions.setHtmlMediaType(HtmlMediaType.Screen);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convert HTML to PDF with CSS page rule priority

Use this example when CSS `@page` rules should influence the final PDF page layout.

1. Configure the HTML load options to honor CSS page rules.
1. Load the HTML content into a PDF document.
1. Save the resulting PDF file.

```java
public static void convertHtmlToPdfPriorityCssPageRule(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions();
    loadOptions.setPriorityCssPageRule(false);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convert HTML to PDF with embedded fonts

Use this example when the output PDF should preserve the HTML fonts by embedding them.

1. Configure the HTML load options for font embedding.
1. Open the HTML source with those options.
1. Save the PDF with embedded font resources.

```java
public static void convertHtmlToPdfEmbedFonts(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions();
    loadOptions.setEmbedFonts(true);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Render HTML content to the same page

Use this example when long HTML content should be kept on one PDF page instead of flowing across multiple pages.

1. Set the HTML conversion options for single-page rendering.
1. Load the HTML content into the PDF document.
1. Save the output file.

```java
public static void convertHtmlToPdfRenderContentToSamePage(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions();
    loadOptions.setRenderToSinglePage(true);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convert HTML containing inline SVG

Use this example when the HTML source includes inline SVG data that must be rendered in the PDF.

1. Open the HTML content that contains SVG markup.
1. Convert it with the standard HTML-to-PDF pipeline.
1. Save the generated PDF document.

```java
public static void convertHtmlToPdfRenderHtmlWithSvgData(Path inputFile, Path outputFile) {
    throw new UnsupportedOperationException("HTML with SVG data to PDF conversion is not implemented yet");
}
```

## Convert a web page to PDF

Use this example when a live web URL should be rendered and saved as a PDF document.

1. Provide the target web page URL.
1. Load the page content into the PDF conversion flow.
1. Save the rendered web page as a PDF file.

```java
public static void convertWebPageToPdf(String urlString, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions(urlString);
    try {
        URL url = URI.create(urlString).toURL();

        try (InputStream inputStream = url.openStream()) {
            try (Document document = new Document(inputStream, loadOptions)) {
                document.save(outputFile.toString());
            }
        }
        System.out.println(url + " converted into " + outputFile);
    } catch (Exception e) {
        e.printStackTrace();
    }
}
```
