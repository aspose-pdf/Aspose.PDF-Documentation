---
title: Get Viewer Preferences
type: docs
weight: 10
url: /java/get-viewer-preferences/
description: Learn how to read the viewer preferences of a PDF document in Java using the PdfContentEditor facade in Aspose.PDF.
lastmod: "2026-06-03"
TechArticle: true
AlternativeHeadline: Read PDF viewer preferences in Java
Abstract: This article shows how to bind a PDF and print the current viewer preference value using the PdfContentEditor facade in Aspose.PDF for Java.
---
## Get the current viewer preference

1. Bind the source PDF to the `PdfContentEditor` facade.
2. Call `getViewerPreference()` to read the current value.
3. Inspect or print the returned preference flag.

```java
public static void getViewerPreferences(Path inputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        System.out.println("Current viewer preference: " + editor.getViewerPreference());
    } finally {
        editor.close();
    }
}
```
