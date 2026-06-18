---
title: Convert HTML to PDF in Java
linktitle: Convert HTML to PDF file
type: docs
weight: 40
url: /java/convert-html-to-pdf/
lastmod: "2026-06-16"
description: Learn how to convert HTML, MHTML, and web pages to PDF in Java with Aspose.PDF, including media settings, CSS page rules, font embedding, SVG content, and single-page output.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: How to convert HTML to PDF in Java with Aspose.PDF
Abstract: This article explains how to convert HTML and MHTML files to PDF using Aspose.PDF for Java. It covers the basic HTML-to-PDF workflow and shows how to control rendering with media types, CSS page rule priority, embedded fonts, SVG content, single-page output, and direct conversion from a live web page.
---
Aspose.PDF for Java can convert local HTML files, archived MHTML content, and live web pages into PDF documents. You can control the conversion pipeline with `HtmlLoadOptions` and `MhtLoadOptions` to influence layout scaling, CSS media handling, page-rule priority, font embedding, resource resolution, and single-page rendering behavior.

## Convert HTML to PDF

Use this example when a local HTML file should be converted directly into a PDF document.

1. Create an [`HtmlLoadOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/htmlloadoptions/) instance to configure how the HTML source is interpreted during import.
1. Set [`HtmlPageLayoutOption`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/htmlpagelayoutoption/) to `ScaleToPageWidth` so wide HTML content is scaled to the target PDF page width instead of being clipped.
1. Open the source HTML file by passing its path and the configured load options into the [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) constructor.
1. Save the generated [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) as a PDF file at the target output path.

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

1. Create an [`HtmlLoadOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/htmlloadoptions/) instance for the conversion settings.
1. Set [`HtmlMediaType`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/htmlmediatype/) to `Screen` when the HTML should be rendered with CSS rules intended for on-screen display instead of print media.
1. Open the HTML file with the configured load options so media-query-dependent styles are applied during conversion.
1. Save the resulting [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) as a PDF file.

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

1. Create an [`HtmlLoadOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/htmlloadoptions/) instance before opening the HTML file.
1. Configure `setPriorityCssPageRule(false)` when other layout settings should take precedence over CSS `@page` declarations in the source markup.
1. Load the HTML content into a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) with the configured options so the page layout is resolved during import.
1. Save the generated PDF file.

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

1. Create an [`HtmlLoadOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/htmlloadoptions/) instance for the HTML import configuration.
1. Enable `setEmbedFonts(true)` so the fonts resolved during HTML rendering are stored in the output PDF.
1. Open the HTML source with these load options to keep the original typography available in the final document.
1. Save the [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) as a PDF with the embedded font resources included.

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

## Render HTML content on a single PDF page

Use this example when long HTML content should be kept on one PDF page instead of flowing across multiple pages.

1. Create an [`HtmlLoadOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/htmlloadoptions/) instance for the conversion settings.
1. Enable `setRenderToSinglePage(true)` so the imported HTML is laid out on one PDF page rather than split across several pages.
1. Open the source HTML with the configured load options and let Aspose.PDF build the page layout in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Save the output PDF file.

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

1. Create an [`HtmlLoadOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/htmlloadoptions/) instance with the HTML file's parent directory as the base path so related resources can be resolved consistently during conversion.
1. Open the HTML file that contains inline SVG markup by passing the source path and load options into the [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) constructor.
1. Let Aspose.PDF render the HTML DOM together with the embedded SVG elements into the PDF page content.
1. Save the generated PDF document.

```java
public static void convertHtmlToPdfWithSvgData(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions(inputFile.getParent().toString());
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convert a web page to PDF

Use this example when a live web URL should be rendered and saved as a PDF document.

1. Create an [`HtmlLoadOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/htmlloadoptions/) instance with the target URL so relative resources such as stylesheets and images can be resolved against that address.
1. Convert the URL string into a `URL` object and open its input stream to fetch the live HTML content.
1. Create a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) from the response stream and the configured load options so the downloaded page is processed with the correct base URL.
1. Save the rendered web page as a PDF file and close the stream resources automatically with try-with-resources.

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

## Convert MHTML to PDF

Use this example when an archived MHTML file should be converted into a PDF document.

1. Create an [`MhtLoadOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/mhtloadoptions/) instance to tell Aspose.PDF to load the source as MIME HTML content.
1. Open the `.mht` or `.mhtml` file by passing its path and the MHTML load options into the [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) constructor.
1. Let Aspose.PDF parse the archived HTML content and its embedded resources into the PDF document model.
1. Save the generated PDF file.

```java
public static void convertMhtmlToPdf(Path inputFile, Path outputFile) {
    MhtLoadOptions loadOptions = new MhtLoadOptions();
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
