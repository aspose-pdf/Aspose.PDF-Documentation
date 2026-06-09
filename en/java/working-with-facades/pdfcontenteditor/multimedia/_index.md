---
title: Multimedia
type: docs
weight: 70
url: /java/pdfcontenteditor-multimedia/
description: Learn the current multimedia coverage available in the Java PdfContentEditor facade in Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Multimedia annotation workflows in Java with PdfContentEditor
Abstract: This section covers multimedia-related workflows currently supported by the Java PdfContentEditor example set. The repository includes a direct movie-annotation example, while unsupported sound topics are retained as explicit scope notes.
---
The current Java `PdfContentEditorExamples` class directly supports `addMovieAnnotation(...)`.

## Add a movie annotation

1. Bind the source PDF to the `PdfContentEditor` facade.
2. Call `createMovie(...)` with the annotation rectangle, movie file path, and page number.
3. Save the updated PDF document.

```java
public static void addMovieAnnotation(Path inputFile, Path movieFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.createMovie(new Rectangle(80, 500, 220, 120), movieFile.toString(), 1);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
