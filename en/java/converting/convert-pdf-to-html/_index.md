---
title: Convert PDF to HTML in Java
linktitle: Convert PDF to HTML format
type: docs
weight: 50
url: /java/convert-pdf-to-html/
lastmod: "2026-05-27"
description: Learn how to convert PDF to HTML in Java with Aspose.PDF, including multi-page output, external image folders, SVG handling, and layered HTML rendering.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: How to Convert PDF to HTML in Java
Abstract: This article explains how to convert PDF files to HTML using Aspose.PDF for Java. It covers basic HTML export together with options for image folders, page splitting, SVG output, compressed SVG graphics, PNG page backgrounds, body-only markup, transparent text rendering, and document-layer conversion.
---
## Convert PDF to HTML

```java
public static void convertPdfToHtml(Path inputFile, Path outputFile) {
    saveDocument(inputFile, outputFile, new HtmlSaveOptions());
}
```

## Adjust HTML output behavior

The Java examples also cover:

- storing extracted images in a dedicated folder
- splitting output into multiple HTML pages
- storing SVG graphics separately
- compressing SVG graphics
- rendering raster content as PNG page backgrounds
- writing body content only
- preserving transparent or shadowed text as transparent text
- converting marked content to HTML layers
