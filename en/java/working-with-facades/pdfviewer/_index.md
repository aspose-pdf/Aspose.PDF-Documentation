---
title: PdfViewer Class
linktitle: PdfViewer Class
type: docs
weight: 135
url: /java/pdfviewer-class/
description: Learn how to use the PdfViewer facade in Java to render PDF pages to images and inspect viewer settings such as page count, coordinate type, resolution, and bound viewer options.
lastmod: "2026-05-28"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Decode PDF pages and inspect viewer data in Java with PdfViewer
Abstract: This article explains how to use the PdfViewer facade in Aspose.PDF for Java for rendering and inspection tasks. The Java examples configure the viewer with `PageCoordinateType.MediaBox`, `150` DPI resolution, and a `1.0` scale factor, then cover decoding all pages to images, rendering a specific page, reporting page count and viewer settings, and inspecting options such as auto resize and auto rotate.
---
The Java `PdfViewerExamples` class demonstrates rendering-oriented facade workflows.

The available examples show how to:

- Decode all PDF pages into image files
- Render a specific page to a PNG image
- Inspect page count, coordinate type, and resolution
- Review bound viewer settings such as auto resize and auto rotate

All current Java examples share the same viewer setup helper, which applies:

- `PageCoordinateType.MediaBox`
- `150` DPI resolution
- `1.0f` scale factor
