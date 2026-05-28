---
title: Stamp Class
linktitle: Stamp Class
type: docs
weight: 150
url: /java/stamp-class/
description: Learn how to use the Stamp class in Java to add image, PDF, text, page-specific, and background stamps to PDF documents through PdfFileStamp.
lastmod: "2026-05-28"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add image, PDF, and background stamps in Java with the Stamp class
Abstract: This section explains how to use the Stamp class in Aspose.PDF for Java to create reusable stamp objects for PDF documents. The Java examples cover image stamps with explicit origin and stamp ID settings, using a PDF page as a stamp, text stamps built from `FormattedText` and `TextState`, applying stamps to selected pages, and placing image stamps in the background with opacity, quality, size, and rotation controls.
---
The Java `StampExamples` class demonstrates reusable `Stamp` objects that are applied through `PdfFileStamp`.

Use these examples to learn how to:

- Add an image stamp at a fixed position
- Use a page from another PDF as a stamp
- Create a text-based approval stamp with custom styling
- Limit a stamp to specific pages
- Add a rotated background image stamp with opacity control

The current Java source also shows how to:

- assign a stamp ID with `setStampId(...)`
- bind a PDF page to a stamp with `bindPdf(...)`
- bind formatted logo text and a `TextState` with `bindLogo(...)` and `bindTextState(...)`
- size image stamps with `setImageSize(...)`
- place a stamp behind page content with `setBackground(true)`
