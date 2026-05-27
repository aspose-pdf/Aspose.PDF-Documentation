---
title: Convert HTML to PDF in Java
linktitle: Convert HTML to PDF file
type: docs
weight: 40
url: /java/convert-html-to-pdf/
lastmod: "2026-05-27"
description: Learn how to convert HTML, MHTML, and web pages to PDF in Java with Aspose.PDF, including media settings, font embedding, and single-page output.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: How to convert HTML to PDF in Java with Aspose.PDF
Abstract: This article explains how to convert HTML and MHTML files to PDF using Aspose.PDF for Java. It covers the basic HTML-to-PDF workflow and shows how to control rendering with media types, CSS page rule priority, embedded fonts, single-page output, and direct conversion from a live web page.
---
## Convert HTML to PDF

```java
public static void convertHtmlToPdf(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions();
    loadOptions.setPageLayoutOption(HtmlPageLayoutOption.ScaleToPageWidth);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
}
```

## Adjust HTML rendering options

The Java examples also show how to:

- set screen media with `setHtmlMediaType(HtmlMediaType.Screen)`
- control `@page` rule priority with `setPriorityCssPageRule(false)`
- embed fonts with `setEmbedFonts(true)`
- render content to one page with `setRenderToSinglePage(true)`

## Convert a web page or MHTML file

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
    } catch (Exception e) {
        e.printStackTrace();
    }
}
```

```java
public static void convertMhtmlToPdf(Path inputFile, Path outputFile) {
    MhtLoadOptions loadOptions = new MhtLoadOptions();
    loadOptions.getPageInfo().setWidth(842);
    loadOptions.getPageInfo().setHeight(1191);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
}
```
