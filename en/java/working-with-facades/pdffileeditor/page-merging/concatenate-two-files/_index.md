---
title: Concatenate Two PDF Files
linktitle: Concatenate Two PDF Files
type: docs
weight: 60
url: /java/concatenate-two-files/
description: Learn how the current Java merge sample maps to concatenating two PDF files with PdfFileEditor.
lastmod: "2026-05-28"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Concatenate two PDF files in Java with PdfFileEditor
Abstract: This article maps the two-file merge scenario to the `mergePdfDocuments` example in `PdfFileEditorExamples`. Although there is no separate `concatenateTwoFiles` method in the current Java source, the implemented sample already passes two input PDF paths into `concatenate(...)` and writes the merged output.
---
There is no separate Java method named `concatenateTwoFiles` in the current `PdfFileEditorExamples` class.

For the actual source-backed workflow, see `mergePdfDocuments`, which already merges two input PDF files by passing both paths into `concatenate(...)`.
