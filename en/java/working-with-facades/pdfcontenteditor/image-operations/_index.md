---
title: Image Operations
type: docs
weight: 50
url: /java/pdfcontenteditor-image-operations/
description: Learn the current Java image-operation coverage available in the PdfContentEditor facade in Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Image editing workflows in Java with PdfContentEditor
Abstract: This section covers image-related workflows currently supported by the Java PdfContentEditor example set. The repository includes a direct example for replacing an image, while unsupported image-deletion topics are retained as explicit scope notes.
---
The current Java `PdfContentEditorExamples` class directly supports `replaceImage(...)`.

## Replace an image

1. Bind the source PDF to the `PdfContentEditor` facade.
2. Call `replaceImage(...)` with the page number, image index, and replacement image path.
3. Save the updated PDF document.

```java
public static void replaceImage(Path inputFile, Path imageFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.replaceImage(1, 1, imageFile.toString());
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
