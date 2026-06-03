---
title: Change Viewer Preferences
type: docs
weight: 20
url: /java/change-viewer-preferences/
description: Learn how to change the viewer preferences of a PDF document in Java using the PdfContentEditor facade in Aspose.PDF.
lastmod: "2026-06-03"
TechArticle: true
AlternativeHeadline: Change PDF viewer preferences in Java
Abstract: This article shows how to bind a PDF, modify the current viewer preference value, and save the updated document using the PdfContentEditor facade in Aspose.PDF for Java.
---
## Change the viewer preference

1. Bind the source PDF to the `PdfContentEditor` facade.
2. Read the current viewer preference value.
3. Combine it with the desired additional flag and pass the result to `changeViewerPreference(...)`.
4. Save the updated PDF document.

```java
public static void changeViewerPreferences(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.changeViewerPreference(editor.getViewerPreference() | 1);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
