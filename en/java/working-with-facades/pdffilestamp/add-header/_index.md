---
title: Add Header to PDF
linktitle: Add Header to PDF
type: docs
weight: 20
url: /java/add-header/
description: Learn how to add text and image headers to a PDF in Java with PdfFileStamp.
lastmod: "2026-05-28"
TechArticle: true
AlternativeHeadline: Add text and image headers to PDF documents in Java
Abstract: This article explains how to use the header examples from `PdfFileStampExamples` in Aspose.PDF for Java. The current Java source includes adding a text header, adding an image header from a stream, and adding a formatted text header with explicit margins.
---
The current Java source provides three header examples:

- `addTextHeader`, which creates a simple `FormattedText` object and adds it with `addHeader(text, 20)`
- `addImageHeader`, which opens the image file as an input stream and passes that stream into `addHeader(...)`
- `addHeaderWithMargins`, which builds a styled `FormattedText` object with color, font, encoding, bold text, and font size, then applies it with custom margins

These examples show the text, image, and margin-aware header workflows that are currently implemented in the Java sample set.
