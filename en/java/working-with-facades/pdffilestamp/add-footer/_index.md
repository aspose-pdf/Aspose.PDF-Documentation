---
title: Add Footer to PDF
linktitle: Add Footer to PDF
type: docs
weight: 10
url: /java/add-footer/
description: Learn how to add text and image footers to a PDF in Java with PdfFileStamp.
lastmod: "2026-05-28"
TechArticle: true
AlternativeHeadline: Add text and image footers to PDF documents in Java
Abstract: This article explains how to use the footer examples from `PdfFileStampExamples` in Aspose.PDF for Java. The current Java source includes adding a text footer, adding an image footer from a stream, and adding a footer with explicit margins.
---
The current Java source provides three footer examples:

- `addTextFooter`, which creates a simple `FormattedText` object and adds it with `addFooter(text, 20)`
- `addImageFooter`, which opens the image file as an input stream and passes that stream into `addFooter(...)`
- `addFooterWithMargins`, which applies a text footer with left, right, and bottom margin values

These examples show the text, image, and margin-aware footer workflows that are currently implemented in the Java sample set.
