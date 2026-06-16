---
title: Resize PDF Page Contents
linktitle: Resize PDF Page Contents
type: docs
weight: 30
url: /java/resize-pdf-page-contents/
description: Resize content on selected PDF pages in Java with the PdfFileEditor facade.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Resize existing page contents in a PDF document with Java
Abstract: Learn how to resize page contents with Aspose.PDF for Java. The Java example uses PdfFileEditor to target specific pages, apply a new content width and height, and stop the workflow if the resize operation fails.
---
## Resize PDF page contents

The Java sample resizes the content area on pages 1 and 3 and checks the boolean return value.

### Steps

1. Create a `PdfFileEditor` instance.
2. Choose the pages whose content should be resized.
3. Call `resizeContents` with the target width and height.
4. Check the return value and handle failure before continuing.
5. Save the updated document.

### Java example

```java
public static void resizePdfPageContents(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    if (!pdfEditor.resizeContents(inputFile.toString(), outputFile.toString(), new int[] {1, 3}, 400, 750)) {
        throw new IllegalStateException("Failed to resize PDF page contents.");
    }
}
```
